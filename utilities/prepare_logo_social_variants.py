"""
prepare_logo_social_variants.py
================================

Prepara variantes de redes sociales para los dos logos principales de ROBOHOGAR:
- robohogar-logo-monogram-v11.png  (R con ojos ambar + antena rizada)
- robohogar-logo-icon-v6.png       (cabeza de robot, rectangulo redondeado)

Para cada logo genera:
  1. Version "tight" recortada al contenido (sin padding blanco) -
     transparente + sobre blanco puro. Util para landing hero centrado.
  2. Variantes sociales cuadradas 1080x1080 con 3 fondos distintos:
       (a) cream: crema calida #FAF7F1 (warm clean)
       (b) glow:  radial amber glow sobre crema (editorial)
       (c) accent: crema + barra de acento ambar lateral (magazine)
  3. Thumbnail OG 1200x630 con fondo cream para link previews de
     Beehiiv/LinkedIn/WhatsApp.

Salida: todas las variantes .png + .webp en assets/branding/social/ (v3).
La logica de recorte detecta el bbox del contenido (pixeles no-blancos)
y anade un padding relativo al tamano del contenido.

Dependencias: Pillow (PIL). Ejecutar con `uv run` o `python`.
"""

# ═══ Imports ═══════════════════════════════════════════════════════════════
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

# ═══ Config ════════════════════════════════════════════════════════════════
# Raiz del repo - el script vive en utilities/ asi que subimos un nivel
REPO_ROOT = Path(__file__).resolve().parent.parent

# Logos fuente - los dos que Rafael usa como marca editorial
SOURCES = {
    "monogram": REPO_ROOT / "assets/branding/master/robohogar-logo-monogram-v11.png",
    "icon":     REPO_ROOT / "assets/branding/master/robohogar-logo-icon-v6.png",
}

# Destino - todo va a social/ con sufijo -v3 para no pisar las actuales (v2)
OUT_DIR = REPO_ROOT / "assets/branding/social"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Paleta ROBOHOGAR (ver rules/design.md)
CREAM = (250, 247, 241)   # fondo calido principal - mas calido que blanco puro
AMBER = (245, 166, 35)    # #F5A623 - acento
BLACK = (12, 12, 12)      # #0C0C0C - texto/tinta
WHITE = (255, 255, 255)

# Umbral para considerar un pixel "blanco/fondo" en el bbox detection.
# RGB > 245 en los 3 canales = fondo. Dejamos margen para JPEG artifacts.
WHITE_THRESHOLD = 245


# ═══ Helpers: recorte tight ═══════════════════════════════════════════════
def content_bbox(img: Image.Image) -> tuple[int, int, int, int]:
    """
    Devuelve el bounding box del contenido del logo (pixeles no-blancos).

    Si la imagen tiene canal alpha, usamos el alpha para detectar contenido
    (cualquier pixel con alpha > 10 cuenta). Si es RGB sobre blanco, buscamos
    pixeles donde al menos un canal este por debajo del WHITE_THRESHOLD.
    """
    if img.mode == "RGBA":
        # Caso transparente: el alpha indica contenido directamente
        alpha = img.split()[-1]
        return alpha.getbbox()

    # Caso RGB sobre blanco: construimos una mascara de "no blanco"
    rgb = img.convert("RGB")
    pixels = rgb.load()
    w, h = rgb.size
    # PIL Image.getbbox() no admite threshold custom, asi que construimos mask
    mask = Image.new("L", (w, h), 0)
    mask_px = mask.load()
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            # Si algun canal es claramente oscuro, es contenido
            if r < WHITE_THRESHOLD or g < WHITE_THRESHOLD or b < WHITE_THRESHOLD:
                mask_px[x, y] = 255
    return mask.getbbox()


def tight_crop(src_path: Path, padding_pct: float = 0.06) -> Image.Image:
    """
    Carga el logo y lo recorta al contenido + padding relativo.
    padding_pct=0.06 significa un 6% del lado mayor como margen respirable.
    Devuelve RGBA con fondo transparente.
    """
    img = Image.open(src_path).convert("RGBA")
    # Si el logo viene sobre blanco opaco, lo convertimos a transparente primero
    img = whiten_to_transparent(img)
    bbox = content_bbox(img)
    if bbox is None:
        raise ValueError(f"No se detecto contenido en {src_path}")
    cropped = img.crop(bbox)
    w, h = cropped.size
    pad = int(max(w, h) * padding_pct)
    # Creamos un canvas transparente mas grande y pegamos el logo centrado
    out = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    out.paste(cropped, (pad, pad), cropped)
    return out


def whiten_to_transparent(img: Image.Image) -> Image.Image:
    """
    Convierte los pixeles blancos/casi-blancos a alpha=0.
    Necesario porque el logo original viene sobre blanco sin transparencia.
    Solo tocamos pixeles muy claros para no quemar los halos ambar de los ojos.
    """
    img = img.convert("RGBA")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            # Solo blanco puro o casi-puro -> transparente
            if r > 248 and g > 248 and b > 248:
                px[x, y] = (255, 255, 255, 0)
    return img


# ═══ Helpers: fondos para redes ═══════════════════════════════════════════
def bg_cream(size: tuple[int, int]) -> Image.Image:
    """Fondo crema plano - el mas limpio y editorial."""
    return Image.new("RGB", size, CREAM)


def bg_amber_glow(size: tuple[int, int]) -> Image.Image:
    """
    Fondo crema con un radial glow ambar sutil detras del logo.
    Le da profundidad sin distraer - estilo editorial magazine.
    """
    w, h = size
    base = Image.new("RGB", size, CREAM)
    # Capa del glow: circulo ambar muy difuminado en el centro
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(glow)
    # Radio del glow ~40% del lado menor, centrado
    radius = int(min(w, h) * 0.42)
    cx, cy = w // 2, h // 2
    # Ambar con alpha bajo para que sea un halo, no un bloque
    draw.ellipse(
        (cx - radius, cy - radius, cx + radius, cy + radius),
        fill=(AMBER[0], AMBER[1], AMBER[2], 70),
    )
    # Blur fuerte para el efecto glow cinematografico
    glow = glow.filter(ImageFilter.GaussianBlur(radius=int(radius * 0.45)))
    base = base.convert("RGBA")
    base.alpha_composite(glow)
    return base.convert("RGB")


def bg_amber_accent(size: tuple[int, int]) -> Image.Image:
    """
    Fondo crema con una barra de acento ambar vertical a la izquierda.
    Referencia visual tipo portada de revista - mas editorial y distintivo.
    """
    w, h = size
    base = Image.new("RGB", size, CREAM)
    draw = ImageDraw.Draw(base)
    # Barra ambar del 6% del ancho total, pegada al borde izquierdo
    bar_w = int(w * 0.06)
    draw.rectangle((0, 0, bar_w, h), fill=AMBER)
    return base


# ═══ Composicion de variantes ═════════════════════════════════════════════
def fit_logo(logo: Image.Image, canvas: Image.Image, scale: float) -> Image.Image:
    """
    Pega el logo centrado en el canvas, escalado a `scale` del lado menor.
    scale=0.60 -> el logo ocupa el 60% del lado menor del canvas.
    """
    cw, ch = canvas.size
    target = int(min(cw, ch) * scale)
    # Mantenemos aspect ratio del logo
    lw, lh = logo.size
    ratio = min(target / lw, target / lh)
    new_w, new_h = int(lw * ratio), int(lh * ratio)
    resized = logo.resize((new_w, new_h), Image.LANCZOS)
    # Centramos - conversion a RGBA para preservar transparencia al pegar
    out = canvas.convert("RGBA")
    x = (cw - new_w) // 2
    y = (ch - new_h) // 2
    out.paste(resized, (x, y), resized)
    return out


def save_png_and_webp(img: Image.Image, base_path: Path) -> None:
    """Guarda PNG (master) + WebP (optimizado) con el mismo basename."""
    # PNG conserva transparencia / calidad bit-exact
    img.save(base_path.with_suffix(".png"), "PNG")
    # WebP a calidad 90 - excelente ratio tamano/calidad para logos
    img.convert("RGB").save(
        base_path.with_suffix(".webp"),
        "WEBP",
        quality=90,
        method=6,  # metodo 6 = compresion mas lenta pero mejor resultado
    )
    # Log para confirmar
    png_kb = base_path.with_suffix(".png").stat().st_size // 1024
    webp_kb = base_path.with_suffix(".webp").stat().st_size // 1024
    print(f"  -> {base_path.name}.png ({png_kb} KB) + .webp ({webp_kb} KB)")


# ═══ Pipeline principal ═══════════════════════════════════════════════════
def process_logo(name: str, src_path: Path) -> None:
    """
    Para un logo dado, genera:
      - tight (transparente) y tight-white (sobre blanco)
      - 3 variantes cuadradas 1080 (cream, glow, accent)
      - 1 thumbnail OG 1200x630 (cream, la mas segura para link previews)
    """
    print(f"\n=== {name.upper()} ({src_path.name}) ===")

    # 1. Recorte tight - version base sin padding blanco
    tight = tight_crop(src_path, padding_pct=0.06)
    tw, th = tight.size
    print(f"  bbox tight: {tw}x{th}px")

    # Guardamos dos sabores del tight:
    # (a) transparente: para landing hero donde se embebe en HTML con CSS bg
    save_png_and_webp(tight, OUT_DIR / f"{name}-tight-transparent-v3")
    # (b) sobre blanco: para email/Beehiiv donde la transparencia da artefactos
    on_white = Image.new("RGB", (tw, th), WHITE)
    on_white.paste(tight.convert("RGBA"), (0, 0), tight)
    save_png_and_webp(on_white, OUT_DIR / f"{name}-tight-white-v3")

    # 2. Variantes sociales cuadradas 1080x1080 - para avatares IG/LinkedIn/X
    square_size = (1080, 1080)
    variants_square = {
        "square-cream":  (bg_cream(square_size),       0.65),
        "square-glow":   (bg_amber_glow(square_size),  0.58),
        "square-accent": (bg_amber_accent(square_size), 0.62),
    }
    for variant_name, (bg, scale) in variants_square.items():
        composed = fit_logo(tight, bg, scale)
        save_png_and_webp(composed, OUT_DIR / f"{name}-{variant_name}-v3")

    # 3. OG thumbnail 1200x630 - link previews en Beehiiv, WhatsApp, LinkedIn
    # Cream plano porque es el mas neutro y se renderiza bien en cualquier feed
    og_size = (1200, 630)
    og_composed = fit_logo(tight, bg_cream(og_size), 0.55)
    save_png_and_webp(og_composed, OUT_DIR / f"{name}-og-1200x630-v3")


def main() -> None:
    print(f"Repo root:  {REPO_ROOT}")
    print(f"Output dir: {OUT_DIR}")
    for name, path in SOURCES.items():
        if not path.exists():
            print(f"!! No existe {path}, saltando")
            continue
        process_logo(name, path)
    print("\nOK. Revisa los archivos -v3 en assets/branding/social/")


if __name__ == "__main__":
    main()
