---
name: Branding — fondo debe ser blanco puro #FFFFFF, no crema
description: ROBOHOGAR social/branding assets need pure white backgrounds, not cream tints that blend on cream UIs but clash on gray platforms
type: feedback
originSessionId: a966e388-756a-4c49-be8e-11c5e99dd00f
---
Los assets de branding social de ROBOHOGAR (profile-icon, og-seo, monograma, etc.) deben tener fondo **blanco puro `#FFFFFF`**, nunca crema `#FAF7F1` o variantes cálidas similares — salvo que el nombre lo indique explícitamente (`-cream`, `-accent`, `-glow`).

**Why:** El lote original generado con nano-banana salió con canvas `#FAF7F1` (tinte crema muy sutil, solo 5 puntos RGB bajo blanco). En `assets/branding/social/final/` es invisible sobre fondo blanco/oscuro, pero en plataformas con UI gris claro (Beehiiv avatar preview, X, LinkedIn) el tinte se lee como "mancha cálida" en lugar de fundirse. Rafael lo detectó en el preview de Beehiiv Profile Picture el 2026-04-17.

**How to apply:**
- Al generar nuevos assets con `/nano-banana` o manualmente: especificar en el prompt "pure white background `#FFFFFF`, no off-white, no cream"
- Tras generar, verificar con PIL: `img.getpixel((8, 8))` debe ser `(255, 255, 255)`, no `(250, 247, 241)`
- Script de corrección existente (por si aparece otro lote con el mismo bug): `utilities/fix_social_bg_to_white.py` — hace replace exacto del color crema a blanco
- Excepción válida: variantes decorativas cuyo nombre ya declare el fondo (`-cream-v3`, `-accent-v3`, `-glow-v3`) son intencionales
