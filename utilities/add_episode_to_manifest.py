"""
Añade (o actualiza) una entrada de episodio en `content/podcast/episodes.json`.

Uso:
    python utilities/add_episode_to_manifest.py <slug>

Recolecta los datos del episodio:
  - `slug`, `title`, `subtitle` (display_title), `summary` (meta_description):
    del frontmatter del relato `.md` en `content/ficciones/**/<slug>/`.
  - `pub_date_rfc2822`: del frontmatter `published:` o `date:` del .md, o del
    filename `YYYY-MM-DD-<slug>.md` como fallback. Hora canónica 09:00 UTC.
  - `duration_hms`, `mp3_bytes`: del `<slug>-chunks-index.json` y del MP3 local
    en `assets/audio/ficciones/`.
  - `cover_cache_bust`: la fecha actual YYYYMMDD (cambia cada vez que el script
    corre — fuerza refetch del cover en plataformas que cachean por URL).
  - `guid`: derivado del slug (`robohogar-ficciones-<slug>`), inmutable.

**Idempotente:** si ya existe entrada para ese slug, se actualiza in-place
preservando `guid` (el GUID es inmutable; todo lo demás puede refrescarse).
Si no existe, se prepende al inicio de la lista (más reciente arriba).

**Why:** el manifest es la fuente de verdad commiteada al repo (fix
arquitectónico 2026-04-27). Antes los episodios se descubrían escaneando
`assets/audio/ficciones/*-chunks-index.json` (que están en .gitignore y
solo viven en una máquina). Este script formaliza el append manifest →
generate_podcast_rss.py → upload a R2.

Invocado por `/audiobook-distribute § paso 5` automáticamente, o manual
para backfill.
"""

import json
import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "content" / "podcast" / "episodes.json"
FICTIONS_ROOT = REPO_ROOT / "content" / "ficciones"
AUDIO_DIR = REPO_ROOT / "assets" / "audio" / "ficciones"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(md_path: Path) -> dict:
    """Parser simple sin PyYAML — mismo patrón que generate_podcast_rss.py."""
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


def find_relato_md(slug: str) -> Path:
    """Busca `<fecha>-<slug>.md` o cualquier `.md` no PASOS/README en el slug dir."""
    matches = list(FICTIONS_ROOT.glob(f"**/{slug}/*-{slug}.md"))
    if matches:
        return matches[0]
    fallback = [m for m in FICTIONS_ROOT.glob(f"**/{slug}/*.md")
                if m.stem.lower() not in {"pasos", "readme"}]
    if fallback:
        return fallback[0]
    sys.exit(f"ERROR: no se encontró .md para slug '{slug}' en content/ficciones/")


def derive_pub_date_rfc2822(fm: dict, md_path: Path) -> str:
    """Devuelve pub_date en formato RFC 2822 a las 09:00 UTC.

    Orden: frontmatter `published:` → `date:` → filename YYYY-MM-DD- prefix.
    """
    for key in ("published", "date", "pubDate"):
        date_str = fm.get(key)
        if date_str:
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d").replace(
                    hour=9, tzinfo=timezone.utc
                )
                return format_datetime(dt)
            except ValueError:
                continue
    name = md_path.stem
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", name)
    if m:
        year, month, day = map(int, m.groups())
        dt = datetime(year, month, day, 9, 0, 0, tzinfo=timezone.utc)
        return format_datetime(dt)
    sys.exit(f"ERROR: no pude determinar pub_date para {md_path.name}")


def format_duration_hms(total_seconds: float) -> str:
    """Apple/Spotify aceptan HH:MM:SS — lo más universal."""
    s = int(round(total_seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def build_episode_entry(slug: str) -> dict:
    """Construye la entrada del manifest a partir del estado local."""
    md = find_relato_md(slug)
    fm = parse_frontmatter(md)

    title = fm.get("title", slug.replace("-", " ").title())
    subtitle = fm.get("display_title", title)  # fallback al title corto si no hay display_title
    summary = fm.get("meta_description", "")
    if not summary:
        sys.exit(f"ERROR: {md.name} no tiene meta_description (obligatorio para summary RSS)")

    pub_date_rfc2822 = derive_pub_date_rfc2822(fm, md)

    chunks_index_file = AUDIO_DIR / f"{slug}-chunks-index.json"
    if not chunks_index_file.exists():
        sys.exit(
            f"ERROR: no existe {chunks_index_file.relative_to(REPO_ROOT)}.\n"
            "Genera el audiolibro primero con `/audiobook-generate <slug>`."
        )
    chunks = json.loads(chunks_index_file.read_text(encoding="utf-8"))

    mp3_file = AUDIO_DIR / f"{slug}.mp3"
    if not mp3_file.exists():
        sys.exit(f"ERROR: no existe {mp3_file.relative_to(REPO_ROOT)}.")

    return {
        "slug": slug,
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "pub_date_rfc2822": pub_date_rfc2822,
        "duration_hms": format_duration_hms(chunks["total_duration_seconds"]),
        "mp3_bytes": mp3_file.stat().st_size,
        "cover_cache_bust": datetime.now(timezone.utc).strftime("%Y%m%d"),
        "guid": f"robohogar-ficciones-{slug}",
    }


def update_manifest(slug: str) -> dict:
    """Add o update entrada para `slug`. Devuelve el dict del entry final."""
    if not MANIFEST.exists():
        sys.exit(f"ERROR: no existe {MANIFEST.relative_to(REPO_ROOT)}")

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    new_entry = build_episode_entry(slug)

    # Idempotente: si ya existe slug, actualizar in-place preservando guid.
    existing_idx = next(
        (i for i, ep in enumerate(data["episodes"]) if ep.get("slug") == slug),
        None,
    )
    if existing_idx is not None:
        old_guid = data["episodes"][existing_idx].get("guid")
        if old_guid:
            new_entry["guid"] = old_guid  # GUID inmutable
        data["episodes"][existing_idx] = new_entry
        action = "actualizado"
    else:
        # Más reciente arriba: prepend al principio.
        data["episodes"].insert(0, new_entry)
        action = "añadido"

    # Pretty-print con indent=2 para que los diffs git sean legibles.
    MANIFEST.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"OK · episodio '{slug}' {action} en {MANIFEST.relative_to(REPO_ROOT)}")
    print(f"   title          : {new_entry['title']}")
    print(f"   subtitle       : {new_entry['subtitle'][:80]}{'...' if len(new_entry['subtitle']) > 80 else ''}")
    print(f"   pub_date       : {new_entry['pub_date_rfc2822']}")
    print(f"   duration       : {new_entry['duration_hms']}")
    print(f"   mp3_bytes      : {new_entry['mp3_bytes']:,}")
    print(f"   cover cache_bust: ?v={new_entry['cover_cache_bust']}")
    print(f"   guid           : {new_entry['guid']}")
    print()
    print("Próximo paso:")
    print("  python utilities/generate_podcast_rss.py")
    print("  python utilities/upload_rss_to_r2.py")
    return new_entry


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: python utilities/add_episode_to_manifest.py <slug>")
    update_manifest(sys.argv[1])


if __name__ == "__main__":
    main()
