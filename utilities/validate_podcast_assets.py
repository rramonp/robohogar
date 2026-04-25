"""
Validador (+ auto-heal opcional) de assets referenciados por el feed RSS.

Uso:
    python utilities/validate_podcast_assets.py            # solo check
    python utilities/validate_podcast_assets.py --heal     # check + sube faltantes vía REST API

Resuelve el bug sistémico detectado 2026-04-25 (incidente "Amazon Music
muestra el-que-viene-a-tomar-cafe sin miniatura"): el pipeline genera
`<itunes:image>` y `<enclosure url=...>` en feed.xml apuntando a R2, pero
ninguna utility del pipeline subía los covers de podcast por episodio a R2.
La de la-objecion estaba subida por intervención manual previa; la de
el-que-viene-a-tomar-cafe se quedó solo en local hasta que las plataformas
hicieron HEAD y vieron 404. Cualquier futuro episodio reproduciría el fallo.

Garantía que provee este script:

  Antes de publicar `feed.xml` a R2, el feed YA referenciaba 0 URLs en
  estado 404. Si hay 404, el script (en modo --heal) intenta subir desde
  local. Si la fuente local también falta, el script aborta y propaga el
  fallo al uploader que lo invocó (bloqueando la publicación del feed).

Cómo se invoca en producción:

  - Como pre-step obligatorio dentro de `upload_rss_to_r2_via_api.py`
    (REST) y `upload_rss_to_r2.py` (S3). En ambos casos el uploader
    importa `validate_podcast_assets.validate_and_heal()` y aborta si
    la validación devuelve assets no reparables.
  - También invocable manual para auditoría puntual del feed actual sin
    tocar el upload del feed.xml en sí.

Cobertura del validador:

  - `<itunes:image href>` del canal (top-level).
  - `<itunes:image href>` de cada episodio.
  - `<enclosure url>` de cada episodio (MP3).

  No valida el `<atom:link rel="self" href>` (es la URL del propio feed,
  que se resuelve siempre desde donde lo está leyendo).

El "heal" usa la REST API de Cloudflare (`api.cloudflare.com`) — mismo
endpoint que el fallback `upload_rss_to_r2_via_api.py`. Razón: la
detección del incidente fue durante un outage del rango S3 (172.64.x.x),
y el patrón "validar-antes-de-publicar" debe ser robusto al mismo modo
de fallo. Requiere `CLOUDFLARE_API_TOKEN` en `.claude/settings.local.json`.

Mapeo URL pública → ruta local (para reparar):

  https://feed.robohogar.com/<key>  →  R2 key = <key>

  Ruta local según patrón de la key:
    covers/<file>.jpg                       → assets/audio/ficciones/covers/<file>.jpg
    <slug>.mp3                               → assets/audio/ficciones/<slug>.mp3
    podcast-canal-artwork-3000x3000.jpg     → assets/branding/podcast-canal-artwork-3000x3000.jpg

  Si una URL referenciada no encaja en ninguno de estos patrones, el
  validador la marca como "no reparable" y aborta. Eso protege contra
  drift futuro: si alguien añade un asset nuevo al feed con un path
  no-canónico, sale a la luz aquí en lugar de fallar silenciosamente
  ante las plataformas.

Dependencias: solo stdlib. Mismo patrón que el resto de utilities/.
"""

import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
FEED_LOCAL = REPO_ROOT / "content" / "podcast" / "feed.xml"

# Endpoint REST API Cloudflare — igual que upload_rss_to_r2_via_api.py.
CF_API_BASE = "https://api.cloudflare.com/client/v4"

# Namespace iTunes podcasting — necesario para xml.etree al parsear feed.xml.
NS = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}

# Mapeo de Content-Type por extensión, usado para uploads de heal.
CONTENT_TYPES = {
    ".mp3": "audio/mpeg",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".xml": "application/rss+xml",
}


def load_env(require_token: bool = True) -> dict:
    """Carga config desde settings.local.json. CLOUDFLARE_API_TOKEN solo
    obligatorio si se va a hacer heal (require_token=True).
    """
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    required = ["R2_ACCOUNT_ID", "R2_BUCKET", "R2_FEED_PUBLIC_URL"]
    if require_token:
        required.append("CLOUDFLARE_API_TOKEN")
    missing = [k for k in required if not env.get(k) or "REEMPLAZAR" in env.get(k, "")]
    if missing:
        sys.exit(f"ERROR: faltan en settings.local.json: {', '.join(missing)}")
    return env


def collect_referenced_urls(feed_path: Path) -> list[dict]:
    """Parsea feed.xml y extrae URLs públicas referenciadas con su tipo.

    Tipos soportados:
      - 'channel-image': <itunes:image href> a nivel <channel>.
      - 'item-image':    <itunes:image href> dentro de cada <item>.
      - 'enclosure':     <enclosure url> dentro de cada <item> (MP3).

    Devuelve lista de dicts: [{'url': str, 'kind': str, 'context': str}, ...]
    """
    if not feed_path.exists():
        sys.exit(f"ERROR: no existe {feed_path}")
    tree = ET.parse(feed_path)
    root = tree.getroot()
    channel = root.find("channel")
    if channel is None:
        sys.exit(f"ERROR: feed.xml malformado — no se encuentra <channel>")

    refs: list[dict] = []

    # itunes:image del canal — UNA por feed.
    ch_img = channel.find("itunes:image", NS)
    if ch_img is not None and ch_img.get("href"):
        refs.append({
            "url": ch_img.get("href"),
            "kind": "channel-image",
            "context": "Canal (top-level)",
        })

    # Por cada episodio: itunes:image + enclosure.
    for item in channel.findall("item"):
        # Título del item para mensajes legibles.
        title_el = item.find("title")
        title = (title_el.text if title_el is not None else "?").strip()

        # Enclosure (MP3) — uno por item.
        enclosure = item.find("enclosure")
        if enclosure is not None and enclosure.get("url"):
            refs.append({
                "url": enclosure.get("url"),
                "kind": "enclosure",
                "context": f"Episodio: {title}",
            })

        # itunes:image del episodio.
        item_img = item.find("itunes:image", NS)
        if item_img is not None and item_img.get("href"):
            refs.append({
                "url": item_img.get("href"),
                "kind": "item-image",
                "context": f"Episodio: {title}",
            })

    return refs


def derive_paths(url: str, env: dict) -> tuple[str, Path | None]:
    """Dada una URL pública del feed, deriva (r2_key, ruta_local).

    `r2_key` se extrae quitando el dominio público; usado tanto para HEAD
    como para subir (la REST API necesita la key, no la URL).

    `ruta_local` es la ruta canónica donde DEBERÍA estar el asset si lo
    generó el pipeline. Devuelve None si la key no encaja en patrones
    canónicos — caso "no reparable" que el caller debe tratar como fallo
    duro.
    """
    public_base = env["R2_FEED_PUBLIC_URL"].rstrip("/")
    if not url.startswith(public_base + "/"):
        # URL externa — no podemos ni HEAD-checkearla con confianza ni
        # subirla. El feed no debería referenciar URLs externas (todo el
        # contenido viene de nuestro R2). Lo marcamos no reparable.
        return ("", None)
    key = url[len(public_base) + 1:]  # +1 para saltar el "/"
    # Quitar query string (`?v=N` para cache busting) y fragment (`#...`).
    # R2 storage solo conoce la key sin params; el query lo añade el feed
    # para forzar refresh en plataformas que cachean por URL completa.
    for sep in ("?", "#"):
        if sep in key:
            key = key.split(sep, 1)[0]

    # Patrones canónicos del pipeline ROBOHOGAR audiolibros.
    if key.startswith("covers/") and key.endswith(".jpg"):
        # covers/<slug>-podcast-1400x1400.jpg
        local = REPO_ROOT / "assets" / "audio" / "ficciones" / "covers" / Path(key).name
    elif re.fullmatch(r"[a-z0-9-]+\.mp3", key):
        # <slug>.mp3
        local = REPO_ROOT / "assets" / "audio" / "ficciones" / Path(key).name
    elif key == "podcast-canal-artwork-3000x3000.jpg":
        # Artwork del canal vive en branding (no en audio/ficciones).
        local = REPO_ROOT / "assets" / "branding" / "podcast-canal-artwork-3000x3000.jpg"
    else:
        # Patrón no reconocido — marcar como no reparable.
        return (key, None)

    return (key, local)


def head_check(url: str, timeout: float = 8.0) -> int:
    """HEAD request, devuelve status code. 0 si fallo de red.

    User-Agent obligatorio: Cloudflare R2 + custom domain rechaza con 403
    los HEAD sin User-Agent identificable (incidente 2026-04-25). curl y
    los podcast clients reales mandan UA siempre, así que sin él el HEAD
    no representa lo que verán las plataformas.
    """
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "ROBOHOGAR-feed-validator/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except (urllib.error.URLError, TimeoutError):
        return 0


def upload_via_rest(env: dict, key: str, local: Path) -> None:
    """PUT del asset a R2 vía REST API. Lanza SystemExit si falla.

    Misma técnica que upload_rss_to_r2_via_api.py — separada aquí para no
    crear dependencia circular entre módulos.
    """
    body = local.read_bytes()
    ext = local.suffix.lower()
    content_type = CONTENT_TYPES.get(ext, "application/octet-stream")
    # Cache-Control distinto según tipo: feed se re-lee cada hora, los
    # assets binarios son inmutables → cache largo en CDN.
    cache_control = "max-age=3600" if ext == ".xml" else "public, max-age=86400"

    url = (
        f"{CF_API_BASE}/accounts/{env['R2_ACCOUNT_ID']}"
        f"/r2/buckets/{env['R2_BUCKET']}/objects/{key}"
    )
    req = urllib.request.Request(
        url,
        data=body,
        method="PUT",
        headers={
            "Authorization": f"Bearer {env['CLOUDFLARE_API_TOKEN']}",
            "Content-Type": content_type,
            "Cache-Control": cache_control,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = resp.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(payload)
                if not parsed.get("success", True):
                    sys.exit(f"FAIL heal {key}: API success=false: {parsed.get('errors')}")
            except json.JSONDecodeError:
                pass  # Algunos endpoints devuelven body vacío en éxito.
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        sys.exit(f"FAIL heal {key}: HTTP {e.code} {e.reason}\n{body_err[:300]}")
    except urllib.error.URLError as e:
        sys.exit(f"FAIL heal {key}: {e.reason}")


def validate_and_heal(env: dict, feed_path: Path = FEED_LOCAL, heal: bool = False) -> dict:
    """Función principal — invocable como módulo desde los uploaders.

    Devuelve dict con resumen:
      {
        'total_refs': int,
        'ok': int,
        'missing_repaired': int,
        'missing_unrepairable': list[dict],  # vacía si todo OK
      }

    Si hay assets no reparables (incluso tras heal), lanza SystemExit con
    código 1 — el uploader que lo invocó debe abortar.
    """
    refs = collect_referenced_urls(feed_path)
    print(f"Validando {len(refs)} URLs referenciadas en {feed_path.relative_to(REPO_ROOT)}...")

    missing_repaired = 0
    unrepairable: list[dict] = []

    for ref in refs:
        status = head_check(ref["url"])
        if status == 200:
            print(f"  OK    [{status}] {ref['url']}  ({ref['context']})")
            continue

        # No 200 — investigamos.
        key, local = derive_paths(ref["url"], env)
        if local is None:
            # No encaja en patrón canónico ni podemos saber dónde buscar local.
            unrepairable.append({**ref, "status": status, "reason": "URL fuera de patrones canónicos"})
            print(f"  ❌ FAIL [{status}] {ref['url']}  ({ref['context']})  — patrón no canónico")
            continue
        if not local.exists():
            unrepairable.append({**ref, "status": status, "reason": f"falta local en {local}"})
            print(f"  ❌ FAIL [{status}] {ref['url']}  ({ref['context']})  — falta local: {local.relative_to(REPO_ROOT)}")
            continue

        # Tenemos local. Si heal=False solo reportamos. Si heal=True subimos.
        if not heal:
            unrepairable.append({**ref, "status": status, "reason": f"reparable, ejecuta con --heal: subiría {local.relative_to(REPO_ROOT)}"})
            print(f"  ⚠️  MISS [{status}] {ref['url']}  ({ref['context']})  — local OK, ejecuta con --heal")
            continue

        # heal=True: subimos.
        print(f"  ↑    HEAL  {ref['url']}  ← {local.relative_to(REPO_ROOT)}")
        upload_via_rest(env, key, local)
        missing_repaired += 1

    summary = {
        "total_refs": len(refs),
        "ok": len(refs) - len(unrepairable) - missing_repaired,
        "missing_repaired": missing_repaired,
        "missing_unrepairable": unrepairable,
    }

    print()
    print("=" * 72)
    print(f"RESUMEN VALIDACIÓN")
    print("=" * 72)
    print(f"Refs totales         : {summary['total_refs']}")
    print(f"Ya en R2 (200)       : {summary['ok']}")
    print(f"Reparados ahora      : {summary['missing_repaired']}")
    print(f"NO reparables        : {len(unrepairable)}")
    if unrepairable:
        for u in unrepairable:
            print(f"  - {u['url']}  ({u['context']})  → {u['reason']}")
    print("=" * 72)

    if unrepairable:
        sys.exit(
            f"FAIL: {len(unrepairable)} asset(s) referenciados en el feed no están en R2 "
            f"y no se pueden reparar automáticamente. Subir/regenerar los locales y reintentar."
        )

    return summary


def main() -> None:
    heal = "--heal" in sys.argv[1:]
    env = load_env(require_token=heal)
    validate_and_heal(env, FEED_LOCAL, heal=heal)


if __name__ == "__main__":
    main()
