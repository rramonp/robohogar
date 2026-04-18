# Design System — ROBOHOGAR

Paleta, tipografía completa y assets de branding → `docs/brand-voice.md` + `assets/branding/asset-catalog.md`.

## Paleta esencial

| Role | Hex |
|---|---|
| Background | `#FFFFFF` |
| Acento ámbar (CTAs, links, highlights) | `#F5A623` |
| Texto principal | `#0C0C0C` |
| Gris secundario (texto) | `#6B7280` |
| Borders/separadores | `rgba(12,12,12,0.15)` |

## Tipografía

Jost (titulares, weight 400) · DM Sans (cuerpo y labels). Solo para assets propios — Beehiiv controla las fuentes en web/email.

## Logos oficiales

Los 2 logos de marca viven en **`assets/branding/social/final/`** (única fuente de verdad). Todo lo demás deriva de aquí.

- **Monograma R** (`og-seo-monogram-1200x630` + `profile-monogram-1080x1080`, PNG+WebP): R bold negra con ojos ámbar + antena. Uso en contextos con espacio: landing hero, OG de artículos, avatar grande, portada newsletter.
- **Icon robot** (`og-seo-icon-1200x630` + `profile-icon-1080x1080`, PNG+WebP): cabeza robot minimalista (visor + antenas + ojos). Uso en contextos compactos: favicon, navbar, avatar redes, footer de email.

Regla rápida: **Monograma = espacio. Icon = densidad.** Nunca integrar el logo dentro de la hero del artículo — el logo vive en avatares/headers.

## Principios visuales

Clean, editorial, magazine-style (inspiración MIT Technology Review). Espaciado generoso. Imágenes grandes. Monograma R para contextos editoriales amplios; Icon para tamaños pequeños y headers/footers.

## Mobile-first (NO negociable)

>50% lectores leen en móvil. Validar SIEMPRE a 375px antes de copy para landing/email/social/cards:

- Bullets/headlines ≤40 chars (más → wrap raro)
- Sin em-dashes (`—`) en headlines cortos: usar `:` o `·`
- Cards 3-up horizontal > 4 stacked
- WebP <200KB email · <500KB web
