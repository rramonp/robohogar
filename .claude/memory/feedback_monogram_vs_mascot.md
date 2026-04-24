---
name: Monograma vs Icon — los dos logos oficiales de ROBOHOGAR
description: ROBOHOGAR usa 2 logos (Monograma R + Icon robot). La mascota antigua ya no forma parte del sistema visual — cleanup 2026-04-18.
type: feedback
originSessionId: 2d73fa9d-bb8a-45e2-9b53-c7f832f25be7
---
ROBOHOGAR tiene **2 logos oficiales** en `assets/branding/social/final/`:

- **Monograma R** (`og-seo-monogram-1200x630` + `profile-monogram-1080x1080`, PNG+WebP): R bold negra con ojos ámbar. **Marca con espacio** — landing hero, OG de artículos, avatar grande, portada newsletter.
- **Icon robot** (`og-seo-icon-1200x630` + `profile-icon-1080x1080`, PNG+WebP): cabeza robot minimalista. **Marca compacta** — favicon, navbar, avatar pequeño, footer de email.

Regla: **Monograma = espacio editorial. Icon = densidad/tamaño pequeño.**

**Why:** Rafael decidió el 2026-04-18 consolidar la marca en estos 2 logos y archivar todo lo demás (19 poses de mascota, monogram-v11 antiguo, icon-v6, lockups, badges, variantes con fondos accent/cream/glow). La mascota "robot con delantal + café" ya NO forma parte del sistema visual — se archivó en `assets/branding/_archive/2026-04-18-cleanup-marca-oficial/`. Motivo: simplificar el sistema para un hobby project solo, la mascota generaba iteraciones innecesarias y confusión de uso.

**How to apply:**
- Nunca recomendar "la mascota" para ningún contexto — ya no existe como asset activo
- Nunca integrar ningún logo dentro de la hero del artículo (la hero es fotográfica/conceptual)
- Las variantes `tight-white` y `tight-transparent` en `social/` son útiles para overlays/watermarks
- Si se pide un logo para email/Beehiiv: siempre fondo blanco #FFFFFF (nunca transparente ni cream)
- Catálogo completo: `assets/branding/asset-catalog.md` (reescrito 2026-04-18)
- La `assets/landing.html` **está pendiente de rediseño** — todavía referencia mascotas archivadas
