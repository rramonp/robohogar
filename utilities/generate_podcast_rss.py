"""
Genera el RSS feed del podcast Ficciones Domésticas para hosting en R2.

Uso:
    python utilities/generate_podcast_rss.py

Lee:
  - `content/podcast/canal-metadata.md` — frontmatter con metadata del canal
    (título, descripción, idioma, categoría iTunes, autor, owner, artwork URL).
  - `content/podcast/episodes.json` — manifest declarativo de episodios
    (fuente de verdad commiteada al repo). Cada entrada lleva: slug, title,
    subtitle (display_title YouTube-style), summary, pub_date_rfc2822,
    duration_hms (HH:MM:SS), mp3_bytes, cover_cache_bust, guid.

Output:
  - `content/podcast/feed.xml` — RSS 2.0 con itunes namespace, válido en
    Apple Podcasts / Spotify / Amazon Music.

Spec: https://podcasters.apple.com/support/823-podcast-requirements
Validador recomendado: https://castfeedvalidator.com

**Por qué el manifest declarativo (decisión arquitectónica 2026-04-27):**
Antes el script descubría episodios escaneando `assets/audio/ficciones/*-chunks-index.json`.
Esos chunks-index están en `.gitignore` (son outputs grandes del TTS, no fuente),
así que viven solo en la máquina donde se generó el audiolibro. Si Rafael
trabajaba desde otra máquina o cambiaba hardware, regenerar el feed borraba
todos los episodios cuyos chunks-index no estaban localmente. Solución: el
manifest commiteado al repo es la fuente única de verdad. Los chunks-index
siguen en su sitio para `audiobook-distribute § generate_youtube_video`
(necesita los timestamps de capítulos), pero el feed RSS es independiente.

Spec: https://podcasters.apple.com/support/823-podcast-requirements
Validador recomendado: https://castfeedvalidator.com

Idempotente: re-ejecutar produce el mismo XML si nada cambió en el manifest.
El `<guid>` de cada item es inmutable (declarado en el manifest).

Si el manifest tiene 0 episodios, genera un canal válido vacío — Spotify y
Amazon aceptan, Apple los rechaza para review (subir el primer episodio
antes de pedir alta en Apple).
"""

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
CANAL_METADATA_FILE = REPO_ROOT / "content" / "podcast" / "canal-metadata.md"
EPISODES_MANIFEST = REPO_ROOT / "content" / "podcast" / "episodes.json"
OUTPUT_FEED = REPO_ROOT / "content" / "podcast" / "feed.xml"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def cache_bust_query(local_file: Path) -> str:
    """Devuelve `?v=<hash8>` calculado del contenido del archivo local.

    Sirve para que Spotify, Amazon Music y otros podcast players invaliden
    su caché del artwork automáticamente cuando la imagen cambia, sin
    intervención manual. La URL del feed pasa de `cover.jpg` a
    `cover.jpg?v=ab12cd34` y, si re-generamos el cover, el hash cambia →
    URL distinta para la plataforma → re-fetch garantizado.

    Cloudflare R2 ignora el query string al resolver el objeto, así que la
    misma key sigue sirviendo el contenido — lo único que cambia es lo que
    ven las plataformas como string de URL.

    Solo aplica a `<itunes:image>`. NO aplicar a `<enclosure>` del MP3:
    cambiar la URL del MP3 puede hacer que Apple Podcasts trate el
    episodio como nuevo y duplique la entrada en la app.

    Si el archivo local no existe, devuelve string vacío (sin cache bust).
    El validador de assets (`validate_podcast_assets.py`) detectará
    después si el remoto también falta y abortará el upload del feed.
    """
    if not local_file.exists():
        return ""
    h = hashlib.sha256(local_file.read_bytes()).hexdigest()[:8]
    return f"?v={h}"


def load_env() -> dict:
    """Carga env. Solo necesitamos R2_FEED_PUBLIC_URL para construir enclosure URLs."""
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    if not env.get("R2_FEED_PUBLIC_URL"):
        sys.exit(
            "ERROR: falta R2_FEED_PUBLIC_URL en settings.local.json\n"
            "Esperado: https://feed.robohogar.com (o el R2 dev URL si custom domain pendiente).\n"
            "Ver Docs/Guia Distribucion Audiolibros.md § Bloque 2.2."
        )
    return env


def parse_frontmatter(md_path: Path) -> dict:
    """Parser simple de frontmatter (sin PyYAML)."""
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def load_canal_metadata() -> dict:
    """Lee y valida `content/podcast/canal-metadata.md`."""
    if not CANAL_METADATA_FILE.exists():
        sys.exit(
            f"ERROR: no existe {CANAL_METADATA_FILE.relative_to(REPO_ROOT)}\n"
            "Crear con la plantilla de Docs/Guia Distribucion Audiolibros.md § Bloque 3.1."
        )
    fm = parse_frontmatter(CANAL_METADATA_FILE)
    required = ["title", "description", "language", "author", "owner_name",
                "owner_email", "category_main", "artwork_url", "link"]
    missing = [k for k in required if not fm.get(k)]
    if missing:
        sys.exit(f"ERROR: faltan campos en canal-metadata.md: {', '.join(missing)}")
    return fm


# ══════════════════════════════════════════════════════════════════════════
# Carga de episodios desde el manifest declarativo
# ══════════════════════════════════════════════════════════════════════════

REQUIRED_EPISODE_FIELDS = (
    "slug", "title", "subtitle", "summary",
    "pub_date_rfc2822", "duration_hms", "mp3_bytes", "guid",
)


def load_episodes_from_manifest() -> list[dict]:
    """Lee episodios del manifest commiteado al repo.

    El manifest es la fuente única de verdad del feed (fix arquitectónico
    2026-04-27 — antes el script glob los chunks-index, que están en
    .gitignore y solo viven en la máquina donde se generó el audiolibro).

    Valida que cada entrada tenga los campos obligatorios. Falla amigablemente
    con el slug exacto del episodio incompleto.
    """
    if not EPISODES_MANIFEST.exists():
        sys.exit(
            f"ERROR: no existe {EPISODES_MANIFEST.relative_to(REPO_ROOT)}\n"
            "Crear con la plantilla del fix 2026-04-27 — ver el commit que añadió este script."
        )

    try:
        data = json.loads(EPISODES_MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: episodes.json inválido: {e}")

    episodes = data.get("episodes", [])
    if not isinstance(episodes, list):
        sys.exit("ERROR: episodes.json: 'episodes' debe ser una lista.")

    for i, ep in enumerate(episodes):
        missing = [f for f in REQUIRED_EPISODE_FIELDS if f not in ep]
        if missing:
            slug = ep.get("slug", f"<entry #{i}>")
            sys.exit(
                f"ERROR: episodio '{slug}' en episodes.json sin campos: {', '.join(missing)}.\n"
                f"Campos obligatorios: {', '.join(REQUIRED_EPISODE_FIELDS)}."
            )

    # El manifest viene ya ordenado más-reciente-arriba por convención
    # (las entradas nuevas se prependen). Si el orden está roto, ordenamos
    # por pub_date descendente como fallback defensivo.
    return episodes


# ══════════════════════════════════════════════════════════════════════════
# Generación del XML
# ══════════════════════════════════════════════════════════════════════════

def build_channel_xml(canal: dict, items_xml: str) -> str:
    """Compone el XML completo del feed con namespace iTunes + content."""
    now = format_datetime(datetime.now(timezone.utc))
    explicit = "true" if str(canal.get("explicit", "false")).lower() == "true" else "false"

    # Cache-bust del artwork del canal: hash del archivo local en
    # `assets/branding/podcast-canal-artwork-3000x3000.jpg`. Si re-generamos
    # el artwork, el hash cambia y las plataformas re-fetchan automático.
    canal_artwork_local = REPO_ROOT / "assets" / "branding" / "podcast-canal-artwork-3000x3000.jpg"
    artwork_url_busted = canal["artwork_url"] + cache_bust_query(canal_artwork_local)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <atom:link href="{escape(canal.get('feed_self_url', ''))}" rel="self" type="application/rss+xml" />
    <title>{escape(canal['title'])}</title>
    <link>{escape(canal['link'])}</link>
    <description>{escape(canal['description'])}</description>
    <language>{escape(canal['language'])}</language>
    <copyright>{escape(canal.get('copyright', ''))}</copyright>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:author>{escape(canal['author'])}</itunes:author>
    <itunes:summary>{escape(canal['description'])}</itunes:summary>
    <itunes:owner>
      <itunes:name>{escape(canal['owner_name'])}</itunes:name>
      <itunes:email>{escape(canal['owner_email'])}</itunes:email>
    </itunes:owner>
    <itunes:image href="{escape(artwork_url_busted)}" />
    <itunes:category text="{escape(canal['category_main'])}">
      {f'<itunes:category text="{escape(canal["category_sub"])}" />' if canal.get('category_sub') else ''}
    </itunes:category>
    <itunes:explicit>{explicit}</itunes:explicit>
    <itunes:type>episodic</itunes:type>
{items_xml}
  </channel>
</rss>
"""


def build_item_xml(episode: dict, env: dict, canal: dict) -> str:
    """XML de un único `<item>` del feed.

    Toma todos los datos del manifest (no del filesystem). Idempotente:
    misma entrada del manifest → mismo XML byte-a-byte.
    """
    slug = episode["slug"]
    feed_base = env["R2_FEED_PUBLIC_URL"].rstrip("/")
    mp3_url = f"{feed_base}/{slug}.mp3"

    # Cache-bust del cover episode: query string `?v=<cache_bust>` declarado
    # en el manifest. Si Rafael regenera el cover (e.g. tras editar hero),
    # bumpear `cover_cache_bust` en el manifest fuerza refetch en plataformas
    # que cachean por URL. NO se aplica al MP3 (`enclosure`) porque cambiar
    # la URL haría que Apple duplique el episodio.
    cache_bust = episode.get("cover_cache_bust", "")
    cover_url = f"{feed_base}/covers/{slug}-podcast-1400x1400.jpg"
    if cache_bust:
        cover_url += f"?v={cache_bust}"

    # Show notes: hook narrativo + CTA al post web. Va en `<itunes:summary>`
    # y `<description>` (HTML permitido vía CDATA). Amazon Music y Apple
    # respetan los <a> del CDATA, Spotify hace strip.
    web_url = f"{canal['link'].rstrip('/')}/p/{slug}"
    home_url = canal["link"].rstrip("/")
    summary_text = episode["summary"]
    description_html = f"""<p>{escape(summary_text)}</p>

<p>▶ Lee el relato completo + suscríbete al newsletter: <a href="{escape(web_url)}">{escape(web_url)}</a></p>

<p>Ficciones Domésticas — relatos de ciencia ficción próxima sobre robótica en el hogar. Cada semana, junto al newsletter en <a href="{escape(home_url)}">robohogar.com</a>.</p>"""

    return f"""    <item>
      <title>{escape(episode['title'])}</title>
      <link>{escape(web_url)}</link>
      <description><![CDATA[{description_html}]]></description>
      <itunes:subtitle>{escape(episode['subtitle'])}</itunes:subtitle>
      <itunes:summary>{escape(summary_text)}</itunes:summary>
      <itunes:author>{escape(canal['author'])}</itunes:author>
      <itunes:image href="{escape(cover_url)}" />
      <enclosure url="{escape(mp3_url)}" length="{episode['mp3_bytes']}" type="audio/mpeg" />
      <guid isPermaLink="false">{escape(episode['guid'])}</guid>
      <pubDate>{episode['pub_date_rfc2822']}</pubDate>
      <itunes:duration>{episode['duration_hms']}</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
      <itunes:episodeType>full</itunes:episodeType>
    </item>"""


def main() -> None:
    env = load_env()
    canal = load_canal_metadata()
    # Construir el self-link del feed (atom:link rel=self) — Apple lo recomienda.
    canal["feed_self_url"] = f"{env['R2_FEED_PUBLIC_URL'].rstrip('/')}/feed.xml"

    print(f"Canal: {canal['title']}")
    print(f"Feed self URL: {canal['feed_self_url']}")
    print()

    print(f"Cargando manifest {EPISODES_MANIFEST.relative_to(REPO_ROOT)}...")
    episodes = load_episodes_from_manifest()
    print(f"  Encontrados {len(episodes)} episodio(s):")
    for ep in episodes:
        # Extracción defensiva del año-mes-día del RFC2822 para reportar
        # con formato consistente, sin parsear (evita romper si el formato
        # tiene variantes de zona horaria).
        date_token = ep["pub_date_rfc2822"].split(" ", 4)
        date_str = f"{date_token[3]}-{date_token[2]}-{date_token[1]}" if len(date_token) >= 4 else ep["pub_date_rfc2822"]
        print(f"  - {date_str} · {ep['slug']} ({ep['duration_hms']})")
    print()

    items_xml = "\n".join(build_item_xml(ep, env, canal) for ep in episodes)
    feed_xml = build_channel_xml(canal, items_xml)

    OUTPUT_FEED.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FEED.write_text(feed_xml, encoding="utf-8")

    print("=" * 72)
    print(f"FEED GENERADO")
    print("=" * 72)
    print(f"Local : {OUTPUT_FEED.relative_to(REPO_ROOT)} ({OUTPUT_FEED.stat().st_size:,} bytes)")
    print(f"Items : {len(episodes)}")
    print()
    print("Próximo paso:")
    print(f"  python utilities/upload_rss_to_r2.py")
    print()
    print("Validar tras subir:")
    print(f"  curl -I {canal['feed_self_url']}")
    print(f"  Pegar en https://castfeedvalidator.com")
    print("=" * 72)


if __name__ == "__main__":
    main()
