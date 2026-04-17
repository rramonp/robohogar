"""
Convierte el fondo crema (#FAF7F1) a blanco puro (#FFFFFF) en los assets sociales
que se detectaron con tinte accidental.

Contexto: el lote de iconos/OG de ROBOHOGAR se generó sobre canvas crema (250,247,241).
Beehiiv y otras plataformas muestran el fondo gris claro de su UI detrás del avatar,
y el tinte cálido se lee como "mancha" en lugar de fundirse. Este script reemplaza
el color de fondo exacto por blanco puro sin regenerar la imagen.

Estrategia:
  - Lee cada archivo
  - Sustituye TODOS los píxeles con RGB exactamente = (250,247,241) por (255,255,255)
    preservando alpha original
  - Reexporta PNG (lossless) y WebP (quality 92)
  - Hace backup previo en _archive/crema-bg-2026-04-17/

Notas:
  - El antialiasing en el borde del robot (transiciones crema→negro) queda inalterado;
    a tamaños de avatar (80-200px) el efecto es imperceptible
  - Los archivos .webp se regeneran desde el PNG arreglado — NO se lee el .webp original
"""

# ═══════════════════════════════════════════════════════════════════════
# Imports y configuración
# ═══════════════════════════════════════════════════════════════════════

from PIL import Image
from pathlib import Path
import shutil

# Raíz del directorio social — todas las rutas se construyen desde aquí
SOCIAL_ROOT = Path(r"C:\Users\bakal\robohogar\assets\branding\social")

# Carpeta de backup con fecha del fix para trazabilidad (nunca sobrescribir sin copia)
ARCHIVE = SOCIAL_ROOT / "_archive" / "crema-bg-2026-04-17"

# Color crema accidental que hay que reemplazar → blanco puro
CREAM_RGB = (250, 247, 241)
WHITE_RGB = (255, 255, 255)

# Lista explícita de assets a arreglar (rutas relativas a SOCIAL_ROOT, sin extensión)
# Cada entry se procesa en PNG + WebP
TARGETS = [
    "final/profile-icon-1080x1080",
    "final/profile-monogram-1080x1080",
    "final/og-seo-icon-1200x630",
    "final/og-seo-monogram-1200x630",
    "icon-og-1200x630-v3",
    "monogram-og-1200x630-v3",
]


# ═══════════════════════════════════════════════════════════════════════
# Funciones
# ═══════════════════════════════════════════════════════════════════════

def replace_bg(img: Image.Image) -> Image.Image:
    """
    Reemplaza todos los píxeles con color crema exacto por blanco puro.
    Preserva el canal alpha si existe.
    """
    # Normalizamos a RGBA para manejar PNG con transparencia y PNG sin alpha uniformemente
    had_alpha = img.mode == "RGBA"
    rgba = img.convert("RGBA")
    pixels = rgba.load()
    w, h = rgba.size

    # Recorrido pixel-by-pixel — aceptable para imágenes ≤1200x1080 (<1.5M px)
    # No usamos numpy para evitar dependencia extra; PIL puro basta
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == CREAM_RGB:
                pixels[x, y] = (*WHITE_RGB, a)

    # Si el original no tenía alpha, devolvemos RGB (sino el PNG crecería sin razón)
    return rgba if had_alpha else rgba.convert("RGB")


def fix_asset(stem: str) -> None:
    """
    Procesa un asset por stem (sin extensión): hace backup, arregla PNG, regenera WebP.
    """
    png_src = SOCIAL_ROOT / f"{stem}.png"
    webp_src = SOCIAL_ROOT / f"{stem}.webp"

    # Backup — preservamos la ruta relativa dentro del archivo de archivo
    backup_dir = ARCHIVE / Path(stem).parent
    backup_dir.mkdir(parents=True, exist_ok=True)
    if png_src.exists():
        shutil.copy2(png_src, backup_dir / f"{png_src.name}")
    if webp_src.exists():
        shutil.copy2(webp_src, backup_dir / f"{webp_src.name}")

    # Fix: leemos PNG (source of truth), arreglamos, re-exportamos PNG + WebP
    img = Image.open(png_src)
    fixed = replace_bg(img)
    fixed.save(png_src, "PNG", optimize=True)
    # WebP quality 92: visualmente lossless para assets de marca, ~40% más pequeño que PNG
    fixed.save(webp_src, "WEBP", quality=92, method=6)

    print(f"  OK {stem} (PNG + WebP)")


# ═══════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════

def main() -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    print(f"Backup en: {ARCHIVE}")
    print(f"Fix {len(TARGETS)} assets ({len(TARGETS)*2} archivos):")
    for stem in TARGETS:
        fix_asset(stem)
    print("Done.")


if __name__ == "__main__":
    main()
