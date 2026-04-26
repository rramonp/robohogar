"""
Backfill de playlists YouTube para audiolibros ya distribuidos.

Para cada `content/ficciones/**/<slug>/distribucion-snapshot.md`:
  1. Extrae `video_id` y `slug` del snapshot.
  2. Lee el frontmatter del relato fuente (`<fecha>-<slug>.md`).
  3. Llama `assign_video_to_playlists(video_id, frontmatter)` para que el
     vídeo entre en sus playlists canónicas (master + One-shots o serie).

Idempotente: re-ejecutar no duplica nada. Las playlists ya creadas se
detectan por título exacto, los items ya presentes se detectan vía
`playlistItems.list(videoId=...)`. Re-correr el script tras cualquier
cambio o tras añadir relatos nuevos no tiene efecto sobre lo previamente
asignado.

Uso:

    # Dry-run (lista qué haría sin tocar YouTube):
    python utilities/backfill_youtube_playlists.py --dry-run

    # Aplicar cambios:
    python utilities/backfill_youtube_playlists.py

    # Solo un slug específico (útil para tests):
    python utilities/backfill_youtube_playlists.py --slug el-operador-nocturno

Pre-requisitos: OAuth ya hecho (`python utilities/upload_youtube.py --auth`).

Coste API estimado en setup inicial:
  - 1 unit por listar playlists del canal (1 vez al principio, cacheable).
  - Por cada vídeo: 50 units por playlist nueva creada (one-time) +
    51 units por insert (1 list + 50 insert). ~100 units por vídeo.
  - 3 vídeos backfill iniciales + crear 2 playlists nuevas (master + One-shots) =
    50*2 + 100*3 ≈ 400 units (de los 10.000/día disponibles). $0.

  Re-ejecuciones idempotentes: ~3 units por vídeo (solo los lists). Trivial.
"""

import json
import re
import sys
from pathlib import Path

# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
FICTIONS_ROOT = REPO_ROOT / "content" / "ficciones"


# Regex para extraer videoId del snapshot. Soporta dos formatos vistos en
# el repo:
#   `| Video ID | \`OgWaX-rcVfU\` |` (formato actual sin bold)
#   `| **Video ID** | \`OgWaX-rcVfU\` |` (formato con bold del operador-nocturno)
# Captura el id YouTube canónico (11 chars de [A-Za-z0-9_-]).
VIDEO_ID_RE = re.compile(
    r"\|\s*\*{0,2}Video ID\*{0,2}\s*\|\s*`([A-Za-z0-9_-]{11})`",
    re.IGNORECASE,
)


def find_distribution_snapshots() -> list[Path]:
    """Devuelve todas las distribucion-snapshot.md del repo, ordenadas por path."""
    return sorted(FICTIONS_ROOT.glob("**/distribucion-snapshot.md"))


def parse_video_id(snapshot_path: Path) -> str | None:
    """Extrae el videoId YouTube del snapshot. Devuelve None si no aparece."""
    text = snapshot_path.read_text(encoding="utf-8")
    m = VIDEO_ID_RE.search(text)
    if m:
        return m.group(1)
    return None


def find_relato_md(slug: str) -> Path | None:
    """Localiza el .md fuente del relato (el que tiene el frontmatter)."""
    matches = list(FICTIONS_ROOT.glob(f"**/{slug}/*-{slug}.md"))
    if not matches:
        # Fallback: cualquier .md en el directorio del slug que no sea PASOS/README.
        candidates = list(FICTIONS_ROOT.glob(f"**/{slug}/*.md"))
        candidates = [
            m for m in candidates
            if m.stem.lower() not in {"pasos", "pasosgenerales", "readme",
                                      "distribucion-snapshot"}
        ]
        if candidates:
            return candidates[0]
        return None
    return matches[0]


# Reusamos el parser de frontmatter del upload — mismo contrato simple.
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(md_path: Path) -> dict:
    """Parser muy simple de YAML frontmatter — extrae key: value de top-level."""
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip().strip('"').strip("'")
        fm[key.strip()] = value
    return fm


def slug_from_snapshot_path(path: Path) -> str:
    """Extrae el slug del path del snapshot.

    Path típico: content/ficciones/_one-shots/el-operador-nocturno/distribucion-snapshot.md
    Slug = nombre del directorio padre del snapshot.
    """
    return path.parent.name


def collect_targets(only_slug: str | None) -> list[dict]:
    """Recorre todos los snapshots y devuelve lista de targets para backfill.

    Cada target es dict con:
      - slug
      - snapshot_path
      - video_id
      - md_path
      - frontmatter

    Se omiten snapshots sin videoId parseable (warning) o sin .md fuente (warning).
    """
    snapshots = find_distribution_snapshots()
    targets = []
    for sp in snapshots:
        slug = slug_from_snapshot_path(sp)
        if only_slug and slug != only_slug:
            continue

        video_id = parse_video_id(sp)
        if not video_id:
            print(f"  WARN: no se encontró videoId en {sp.relative_to(REPO_ROOT)} — skip.")
            continue

        md = find_relato_md(slug)
        if not md:
            print(f"  WARN: no se encontró .md fuente para slug '{slug}' — skip.")
            continue

        fm = parse_frontmatter(md)

        targets.append({
            "slug": slug,
            "snapshot_path": sp,
            "video_id": video_id,
            "md_path": md,
            "frontmatter": fm,
        })

    return targets


def main() -> None:
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    only_slug = None
    if "--slug" in args:
        idx = args.index("--slug")
        if idx + 1 >= len(args):
            sys.exit("ERROR: --slug requiere un valor (ej: --slug el-operador-nocturno).")
        only_slug = args[idx + 1]

    print("=" * 72)
    print("BACKFILL YOUTUBE PLAYLISTS")
    print("=" * 72)
    print(f"Modo       : {'DRY-RUN (sin tocar YouTube)' if dry_run else 'EJECUCIÓN REAL'}")
    print(f"Slug filter: {only_slug or '(todos)'}")
    print()

    print("Localizando snapshots...")
    targets = collect_targets(only_slug)
    if not targets:
        print("  (ninguno aplicable)")
        return
    print(f"  {len(targets)} relato(s) a procesar:")
    for t in targets:
        serie = t["frontmatter"].get("serie", "(sin serie)")
        print(f"    - {t['slug']} · videoId={t['video_id']} · serie={serie}")
    print()

    # Importar destinos canónicos para reportar en dry-run sin tocar YouTube.
    from youtube_playlists import determine_target_playlists, playlist_public_url

    if dry_run:
        print("DRY-RUN: playlists destino por relato:")
        for t in targets:
            playlists = determine_target_playlists(t["frontmatter"])
            print(f"  {t['slug']}:")
            for title, _desc in playlists:
                print(f"    → {title}")
        print()
        print("Re-ejecutar sin --dry-run para aplicar.")
        return

    # Ejecución real: cargar credenciales y procesar uno a uno.
    from googleapiclient.discovery import build as _build
    from upload_youtube import load_credentials, load_env
    from youtube_playlists import assign_video_to_playlists

    env = load_env()
    creds = load_credentials(env)
    youtube = _build("youtube", "v3", credentials=creds, cache_discovery=False)

    # Resumen agregado para reportar al final.
    summary = []  # [(slug, video_id, [(playlist_title, playlist_id, was_added)])]

    for t in targets:
        print("─" * 72)
        print(f"Procesando {t['slug']} (videoId={t['video_id']})...")
        result = assign_video_to_playlists(
            youtube, t["video_id"], t["frontmatter"], verbose=True,
        )
        playlist_lines = []
        for title, info in result.items():
            playlist_lines.append((title, info["playlist_id"], info["video_was_added"]))
        summary.append((t["slug"], t["video_id"], playlist_lines))
        print()

    # Reporte final.
    print("=" * 72)
    print("BACKFILL COMPLETADO")
    print("=" * 72)
    for slug, video_id, lines in summary:
        print(f"\n{slug} · {video_id}")
        for title, pl_id, was_added in lines:
            tag = "+" if was_added else "·"
            print(f"  {tag} {title}")
            print(f"      {playlist_public_url(pl_id)}")
    print()
    print("Total relatos procesados:", len(summary))


if __name__ == "__main__":
    main()
