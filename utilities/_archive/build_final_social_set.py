"""
build_final_social_set.py
==========================

Construye la carpeta "final" de assets sociales con SOLO las imagenes que
Rafael va a subir a cada plataforma, con tamanos correctos y nombres
autodocumentados para no liarse.

Origen (ya existen):
  - assets/branding/social/icon-tight-transparent-v3.png       (icono recortado)
  - assets/branding/social/monogram-tight-transparent-v3.png   (R monogram recortado)
  - assets/branding/social/icon-square-cream-v3.*              (profile 1080, elegido)
  - assets/branding/social/monogram-square-cream-v3.*          (profile 1080, elegido)

Destino (carpeta nueva final/):
  - profile-monogram-1080x1080.{png,webp}   Avatar IG + LinkedIn (R monogram)
  - profile-icon-1080x1080.{png,webp}       Avatar IG + LinkedIn (icono cabeza)
  - og-seo-monogram-1200x630.{png,webp}     OG / Beehiiv SEO (R monogram) - scale 0.85
  - og-seo-icon-1200x630.{png,webp}         OG / Beehiiv SEO (icono) - scale 0.85

Los profile son copia/rename de los square-cream elegidos. Los OG se
regeneran con el logo mas grande (0.85) para que tenga mas presencia
en feeds de X/LinkedIn/WhatsApp.

Uso: uv run --with pillow utilities/build_final_social_set.py
"""

# ═══ Imports ═══════════════════════════════════════════════════════════════
import shutil
from pathlib import Path
from PIL import Image

# ═══ Config ════════════════════════════════════════════════════════════════
REPO_ROOT = Path(__file__).resolve().parent.parent
SOCIAL = REPO_ROOT / "assets/branding/social"
FINAL = SOCIAL / "final"
FINAL.mkdir(parents=True, exist_ok=True)

# Paleta ROBOHOGAR
CREAM = (250, 247, 241)   # fondo crema calido, igual que en las square


# ═══ Helpers ══════════════════════════════════════════════════════════════
def save_png_webp(img: Image.Image, base: Path, webp_quality: int = 90) -> None:
    """Guarda PNG master + WebP optimizado."""
    img.save(base.with_suffix(".png"), "PNG")
    img.convert("RGB").save(
        base.with_suffix(".webp"), "WEBP", quality=webp_quality, method=6
    )
    png_kb = base.with_suffix(".png").stat().st_size // 1024
    webp_kb = base.with_suffix(".webp").stat().st_size // 1024
    print(f"  -> {base.name}.png ({png_kb} KB) + .webp ({webp_kb} KB)")


def compose_og(logo_tight_path: Path, scale: float = 0.85) -> Image.Image:
    """
    Compone un OG 1200x630 con el logo grande centrado sobre crema.
    scale=0.85 significa que el logo ocupa el 85% del alto (lado menor).
    El icono tiene mas aire arriba/abajo porque es cuadrado; la R un poco menos.
    """
    W, H = 1200, 630
    canvas = Image.new("RGB", (W, H), CREAM).convert("RGBA")

    logo = Image.open(logo_tight_path).convert("RGBA")
    lw, lh = logo.size
    # Escalamos al target height - dejamos 15% de aire vertical total
    target_h = int(H * scale)
    ratio = target_h / lh
    new_w, new_h = int(lw * ratio), int(lh * ratio)
    # Si despues del escalado el ancho no cabe, reescalamos por ancho
    # (pasa poco con estos logos pero proteccion barata)
    if new_w > W * 0.85:
        ratio = (W * 0.85) / lw
        new_w, new_h = int(lw * ratio), int(lh * ratio)
    resized = logo.resize((new_w, new_h), Image.LANCZOS)

    # Centramos
    x = (W - new_w) // 2
    y = (H - new_h) // 2
    canvas.paste(resized, (x, y), resized)
    return canvas.convert("RGB")


# ═══ Paso 1: copiar los square-cream elegidos (profile 1080) ══════════════
print(f"Destino: {FINAL}\n")

print("[profile 1080x1080] copiando los square-cream elegidos:")
profile_pairs = [
    ("monogram-square-cream-v3", "profile-monogram-1080x1080"),
    ("icon-square-cream-v3",     "profile-icon-1080x1080"),
]
for src_name, dst_name in profile_pairs:
    for ext in (".png", ".webp"):
        src = SOCIAL / f"{src_name}{ext}"
        dst = FINAL / f"{dst_name}{ext}"
        shutil.copy2(src, dst)
        kb = dst.stat().st_size // 1024
        print(f"  -> {dst.name} ({kb} KB)")


# ═══ Paso 2: regenerar OG 1200x630 con logo grande (scale 0.85) ══════════
print("\n[og 1200x630] regenerando con el logo al 85% (mas presencia en feed):")
og_pairs = [
    ("monogram-tight-transparent-v3.png", "og-seo-monogram-1200x630"),
    ("icon-tight-transparent-v3.png",     "og-seo-icon-1200x630"),
]
for src_name, dst_name in og_pairs:
    src_path = SOCIAL / src_name
    composed = compose_og(src_path, scale=0.85)
    save_png_webp(composed, FINAL / dst_name)


# ═══ Resumen ══════════════════════════════════════════════════════════════
print("\nResumen carpeta final/:")
for f in sorted(FINAL.iterdir()):
    kb = f.stat().st_size // 1024
    print(f"  {f.name:<42} {kb} KB")
