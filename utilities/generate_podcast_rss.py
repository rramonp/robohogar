"""
Genera el RSS feed del podcast Ficciones Domésticas para hosting en R2.

Uso:
    python utilities/generate_podcast_rss.py

Lee:
  - `content/podcast/canal-metadata.md` — frontmatter con metadata canónica
    del canal (título, descripción, idioma, categoría iTunes, autor, owner,
    artwork URL, copyright).
  - `content/registro-articulos.md` (opcional) y `content/ficciones/**/<slug>/`
    para descubrir los relatos publicados con audiolibro.
  - Por cada slug detectado:
      * `assets/audio/ficciones/<slug>-chunks-index.json` (duración, chapters)
      * `content/ficciones/**/<slug>/<fecha>-<slug>.md` (frontmatter: title,
        meta_description, fecha publicación)
      * URL pública del MP3 en R2 (construida desde R2_FEED_PUBLIC_URL +
        slug.mp3)
      * URL del cover podcast (construida desde R2_FEED_PUBLIC_URL +
        covers/<slug>-podcast-1400x1400.jpg)

Output:
  - `content/podcast/feed.xml` — RSS 2.0 con itunes namespace, válido en
    Apple Podcasts / Spotify / Amazon Music. Reemplaza versión anterior.

Spec: https://podcasters.apple.com/support/823-podcast-requirements
Validador recomendado tras cada generación: https://castfeedvalidator.com

Idempotente: re-ejecutar produce el mismo XML si nada cambió. El `<guid>`
de cada item se deriva del slug (NO del URL ni del path) para que las
plataformas no traten un episodio como "nuevo" si la URL del MP3 cambia.

Si no hay episodios todavía (setup inicial, Bloque 3 de la guía), genera
un canal válido con 0 items — Spotify y Amazon aceptan, Apple los rechaza
para review (subir el primer episodio antes de pedir alta en Apple).
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
FICTIONS_ROOT = REPO_ROOT / "content" / "ficciones"
AUDIO_DIR = REPO_ROOT / "assets" / "audio" / "ficciones"
COVERS_DIR = AUDIO_DIR / "covers"
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
# Descubrimiento de episodios
# ══════════════════════════════════════════════════════════════════════════

def discover_episodes() -> list[dict]:
    """Encuentra todos los relatos con audiolibro generado.

    Heurística: existe `<slug>-chunks-index.json` en `assets/audio/ficciones/`.
    Para cada uno, busca el `.md` correspondiente para extraer metadata.
    Devuelve lista ordenada por pubDate descendente (más reciente primero
    al final del proceso, porque RSS readers asumen orden cronológico).
    """
    episodes = []
    for index_file in AUDIO_DIR.glob("*-chunks-index.json"):
        # Slug = nombre sin sufijo "-chunks-index.json"
        slug = index_file.stem.replace("-chunks-index", "")
        try:
            data = json.loads(index_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  WARNING: {index_file.name} no es JSON valido, saltando.")
            continue

        # Buscar el .md del relato.
        md_matches = list(FICTIONS_ROOT.glob(f"**/{slug}/*-{slug}.md"))
        if not md_matches:
            md_matches = [m for m in FICTIONS_ROOT.glob(f"**/{slug}/*.md")
                          if m.stem.lower() not in {"pasos", "readme"}]
        if not md_matches:
            print(f"  WARNING: chunks-index para '{slug}' pero sin .md fuente, saltando.")
            continue

        md = md_matches[0]
        fm = parse_frontmatter(md)

        # Fecha de publicación: primera opción frontmatter['date'], si no
        # parsear del filename `YYYY-MM-DD-<slug>.md`, si no fallback a
        # mtime del .md (creado tarde pero mejor que nada).
        pub_date = parse_pub_date(fm, md)

        episodes.append({
            "slug": slug,
            "title": fm.get("title", slug.replace("-", " ").title()),
            "description": fm.get("meta_description") or fm.get("subtitle", ""),
            "pub_date": pub_date,
            "duration_seconds": data["total_duration_seconds"],
            "narration_chars": data.get("narration_chars", 0),
        })

    # Orden: más reciente primero (RSS standard).
    episodes.sort(key=lambda e: e["pub_date"], reverse=True)
    return episodes


def parse_pub_date(fm: dict, md_path: Path) -> datetime:
    """Determina la fecha de publicación del episodio.

    Orden de preferencia:
      1. frontmatter['date'] si está presente y parseable.
      2. Filename `YYYY-MM-DD-<slug>.md` → parsea YYYY-MM-DD.
      3. Mtime del .md como fallback.
    """
    date_str = fm.get("date") or fm.get("pubDate")
    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.replace(tzinfo=timezone.utc, hour=9)  # 9 AM CET típico
        except ValueError:
            pass

    # Filename pattern: YYYY-MM-DD-<slug>.md
    name = md_path.stem
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", name)
    if m:
        year, month, day = map(int, m.groups())
        return datetime(year, month, day, 9, 0, 0, tzinfo=timezone.utc)

    # Fallback: mtime.
    return datetime.fromtimestamp(md_path.stat().st_mtime, tz=timezone.utc)


# ══════════════════════════════════════════════════════════════════════════
# Generación del XML
# ══════════════════════════════════════════════════════════════════════════

def format_itunes_duration(seconds: float) -> str:
    """Apple Podcasts acepta HH:MM:SS, MM:SS o segundos. HH:MM:SS es lo más universal."""
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


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
    """XML de un único `<item>` del feed."""
    slug = episode["slug"]
    feed_base = env["R2_FEED_PUBLIC_URL"].rstrip("/")
    mp3_url = f"{feed_base}/{slug}.mp3"
    # Cache-bust automático en la cover del episodio: `?v=<hash8>` derivado
    # del contenido del JPG local. Si el cover cambia (re-generación tras
    # editar el hero), el hash cambia → URL distinta para Spotify/Amazon
    # → refetch automático. NO se aplica al MP3 (`enclosure`) porque
    # cambiar la URL del MP3 puede hacer que Apple duplique el episodio.
    local_cover = COVERS_DIR / f"{slug}-podcast-1400x1400.jpg"
    cover_url = f"{feed_base}/covers/{slug}-podcast-1400x1400.jpg{cache_bust_query(local_cover)}"

    # Tamaño del MP3 para `<enclosure length>`. Si no podemos medirlo
    # localmente, fallback a 0 (Apple lo tolera pero no es ideal).
    local_mp3 = AUDIO_DIR / f"{slug}.mp3"
    mp3_size = local_mp3.stat().st_size if local_mp3.exists() else 0

    pub_date = format_datetime(episode["pub_date"])
    duration = format_itunes_duration(episode["duration_seconds"])

    # Show notes: hook narrativo + CTA al post web. Va en `<itunes:summary>`
    # y `<description>` (HTML permitido en description vía CDATA).
    # `home_url` es la landing del newsletter (sin /p/<slug>) — la usamos
    # para envolver la última mención "robohogar.com" del párrafo de cierre
    # como <a href> clickable. Amazon Music y Apple respetan los <a> del
    # CDATA, Spotify hace strip.
    web_url = f"{canal['link'].rstrip('/')}/p/{slug}"
    home_url = canal["link"].rstrip("/")
    summary_text = episode["description"]
    description_html = f"""<p>{escape(summary_text)}</p>

<p>▶ Lee el relato completo + suscríbete al newsletter: <a href="{escape(web_url)}">{escape(web_url)}</a></p>

<p>Ficciones Domésticas — relatos de ciencia ficción próxima sobre robótica en el hogar. Cada semana, junto al newsletter en <a href="{escape(home_url)}">robohogar.com</a>.</p>"""

    # GUID derivado del slug = inmutable para siempre. Las plataformas
    # identifican el episodio por GUID, no por URL del MP3.
    guid = f"robohogar-ficciones-{slug}"

    return f"""    <item>
      <title>{escape(episode['title'])}</title>
      <link>{escape(web_url)}</link>
      <description><![CDATA[{description_html}]]></description>
      <itunes:summary>{escape(summary_text)}</itunes:summary>
      <itunes:author>{escape(canal['author'])}</itunes:author>
      <itunes:image href="{escape(cover_url)}" />
      <enclosure url="{escape(mp3_url)}" length="{mp3_size}" type="audio/mpeg" />
      <guid isPermaLink="false">{escape(guid)}</guid>
      <pubDate>{pub_date}</pubDate>
      <itunes:duration>{duration}</itunes:duration>
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

    print(f"Descubriendo episodios en {AUDIO_DIR.relative_to(REPO_ROOT)}...")
    episodes = discover_episodes()
    print(f"  Encontrados {len(episodes)} episodio(s):")
    for ep in episodes:
        date_str = ep["pub_date"].strftime("%Y-%m-%d")
        dur_min = ep["duration_seconds"] / 60
        print(f"  - {date_str} · {ep['slug']} ({dur_min:.1f} min)")
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
