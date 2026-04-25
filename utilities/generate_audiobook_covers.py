"""
Genera covers derivados del hero de un relato para distribución multi-plataforma.

Uso:
    python utilities/generate_audiobook_covers.py <slug>

Inputs:
  - Hero image del relato. Búsqueda automática en `content/ficciones/**/<slug>/assets/`
    siguiendo patrones canónicos (`hero-<slug>-1K.png`, `hero-<slug>-v<N>.png`,
    `hero-<slug>-v<N>.webp`, etc.). Prefiere -1K si existe; si no, la versión
    más reciente.

Outputs (idempotentes — sobrescriben si ya existen):
  - `assets/audio/ficciones/covers/<slug>-yt-1280x720.png`
    Cover YouTube 16:9 sin texto sobreimpreso. El skill `/audiobook-distribute`
    overlay el chyron del título en runtime al MP4 — el cover queda limpio
    para servir también como thumbnail del vídeo (que YouTube acepta como
    static frame antes de play).
  - `assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg`
    Cover podcast 1:1 JPEG. Apple Podcasts acepta 1400×1400 mín y 3000×3000
    máx; 1400 es el sweet spot peso/calidad para episode artwork (el canal
    artwork sí va a 3000, pero ese es asset único de marca, no por episodio).

Estrategia de transformación:
  - Crop al center con aspect ratio target (no letterbox/pillarbox — preserva
    composición editorial del hero, que suele tener sujeto centrado).
  - Resize Lanczos para alta calidad.
  - YouTube → PNG sin compresión perdida (es nuestro asset master).
  - Podcast → JPEG quality 88 (~150-300 KB típico, dentro del peso ideal
    para cover de podcast — Apple no comprime el JPG antes de servirlo).

Falla amigablemente si no encuentra hero, sugiriendo invocación `/nano-banana`.
Dependencia única: Pillow (`pip install pillow`).
"""

import sys
from pathlib import Path


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
FICTIONS_ROOT = REPO_ROOT / "content" / "ficciones"
COVERS_OUT_DIR = REPO_ROOT / "assets" / "audio" / "ficciones" / "covers"

# Targets canónicos. YouTube exige 1280×720 mín para thumbnails custom y
# 16:9 para vídeos full HD; podcast Apple/Spotify recomiendan 1400×1400+.
YT_TARGET = (1280, 720)
PODCAST_TARGET = (1400, 1400)


def find_hero_image(slug: str) -> Path:
    """Localiza el hero del relato siguiendo patrones canónicos.

    Orden de preferencia:
      1. hero-<slug>-1K.png/webp (formato producto-hero del pipeline)
      2. hero-<slug>-v<N>.png/webp con N más alto (versión más reciente)
      3. hero-<slug>.png/webp sin versión
      4. hero-*-v<N>.png/webp (series con hero por episodio)
      5. cualquier hero-*.png/webp en el directorio del relato

    Devuelve el primer match más específico, o None si nada matchea.
    """
    patterns = [
        f"**/{slug}/assets/hero-{slug}-1K.png",
        f"**/{slug}/assets/hero-{slug}-1K.webp",
        f"**/{slug}/assets/hero-{slug}-v*.png",
        f"**/{slug}/assets/hero-{slug}-v*.webp",
        f"**/{slug}/assets/hero-{slug}.png",
        f"**/{slug}/assets/hero-{slug}.webp",
        f"**/{slug}/assets/hero-*-v*.png",
        f"**/{slug}/assets/hero-*-v*.webp",
        f"**/{slug}/assets/hero-*.png",
        f"**/{slug}/assets/hero-*.webp",
    ]
    for pattern in patterns:
        # `sorted(reverse=True)` favorece -v3 sobre -v2 sobre -v1 lexicográficamente.
        matches = sorted(FICTIONS_ROOT.glob(pattern), reverse=True)
        if matches:
            return matches[0]
    return None


def import_pillow():
    """Import lazy con mensaje claro si Pillow no está instalado."""
    try:
        from PIL import Image
        return Image
    except ImportError:
        sys.exit("ERROR: Pillow no esta instalado. `pip install pillow`")


def crop_to_aspect(img, target_aspect: float):
    """Recorta la imagen al center con el aspect ratio target.

    Si la fuente es más ancha que el target → recorta laterales.
    Si la fuente es más alta que el target → recorta arriba+abajo.
    Preserva el centro de la composición (asume sujeto centrado, que es
    la convención de los hero generados con `/nano-banana` para ROBOHOGAR).
    """
    src_w, src_h = img.size
    src_aspect = src_w / src_h

    if abs(src_aspect - target_aspect) < 0.001:
        # Ya tiene el aspect correcto, no recortes.
        return img

    if src_aspect > target_aspect:
        # Fuente más panorámica que target → recorta laterales.
        new_w = int(round(src_h * target_aspect))
        left = (src_w - new_w) // 2
        return img.crop((left, 0, left + new_w, src_h))
    else:
        # Fuente más vertical que target → recorta arriba+abajo.
        new_h = int(round(src_w / target_aspect))
        top = (src_h - new_h) // 2
        return img.crop((0, top, src_w, top + new_h))


def generate_youtube_cover(hero_path: Path, output: Path) -> None:
    """Cover YouTube 1280×720 PNG. Sin texto overlay (eso lo añade ffmpeg)."""
    Image = import_pillow()
    img = Image.open(hero_path).convert("RGB")
    target_w, target_h = YT_TARGET
    img = crop_to_aspect(img, target_w / target_h)
    img = img.resize(YT_TARGET, Image.LANCZOS)
    output.parent.mkdir(parents=True, exist_ok=True)
    # PNG porque es nuestro master; YouTube acepta tanto JPG como PNG para
    # thumbnails y el peso (~500-900 KB) está dentro del límite 2 MB.
    img.save(output, "PNG", optimize=True)


def generate_podcast_cover(hero_path: Path, output: Path) -> None:
    """Cover podcast 1400×1400 JPEG. Sin texto overlay (cover de episodio)."""
    Image = import_pillow()
    img = Image.open(hero_path).convert("RGB")
    img = crop_to_aspect(img, 1.0)  # 1:1
    img = img.resize(PODCAST_TARGET, Image.LANCZOS)
    output.parent.mkdir(parents=True, exist_ok=True)
    # JPEG quality 88: balance peso/calidad sweet spot para cover podcast.
    # Apple sugiere <500 KB; con quality 88 + Lanczos resize estamos en ~150-300 KB.
    img.save(output, "JPEG", quality=88, optimize=True)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(
            f"Uso: python {sys.argv[0]} <slug>\n"
            f"Ejemplo: python utilities/generate_audiobook_covers.py papa-desde-singapur"
        )
    slug = sys.argv[1]

    print(f"Buscando hero del relato '{slug}' en {FICTIONS_ROOT.relative_to(REPO_ROOT)}/...")
    hero = find_hero_image(slug)
    if hero is None:
        sys.exit(
            f"ERROR: no se encontro hero para '{slug}'.\n"
            f"Esperado en: content/ficciones/**/{slug}/assets/hero-{slug}-*.png\n"
            f"Genera primero el hero con `/nano-banana` (estilo cinematográfico still)."
        )
    print(f"  Hero localizado: {hero.relative_to(REPO_ROOT)}")
    print(f"  Tamano: {Path(hero).stat().st_size / 1024:.0f} KB")
    print()

    yt_out = COVERS_OUT_DIR / f"{slug}-yt-1280x720.png"
    podcast_out = COVERS_OUT_DIR / f"{slug}-podcast-1400x1400.jpg"

    print(f"Generando cover YouTube 1280x720...")
    generate_youtube_cover(hero, yt_out)
    print(f"  -> {yt_out.relative_to(REPO_ROOT)} ({yt_out.stat().st_size / 1024:.0f} KB)")

    print(f"Generando cover podcast 1400x1400...")
    generate_podcast_cover(hero, podcast_out)
    print(f"  -> {podcast_out.relative_to(REPO_ROOT)} ({podcast_out.stat().st_size / 1024:.0f} KB)")

    print()
    print("=" * 72)
    print(f"COVERS GENERADOS · {slug}")
    print("=" * 72)
    print(f"YouTube  : {yt_out.relative_to(REPO_ROOT)}")
    print(f"Podcast  : {podcast_out.relative_to(REPO_ROOT)}")
    print("=" * 72)


if __name__ == "__main__":
    main()
