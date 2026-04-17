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

## Marca principal — Monograma R

**`assets/branding/master/robohogar-logo-monogram-v11.png/jpg`** · R bold negra, ojos ámbar grandes, antena espiral. Uso: landing hero, avatar, OG, favicon, cualquier contexto "marca editorial". **Es la imagen principal de la marca.**

## Mascota

Robot pequeño, cabeza esférica, ojos LED ámbar, delantal azul a cuadros con corazón, taza de café. Prompt base: `assets/branding/mascota-prompt.md`. Uso: emails, social cards, CTAs cercanos, 404 — contextos personales/cálidos. **NO usar donde va el monograma.**

## Principios visuales

Clean, editorial, magazine-style (inspiración MIT Technology Review). Espaciado generoso. Imágenes grandes. Monograma R = marca editorial, mascota = tono cercano.

## Mobile-first (NO negociable)

>50% lectores leen en móvil. Validar SIEMPRE a 375px antes de copy para landing/email/social/cards:

- Bullets/headlines ≤40 chars (más → wrap raro)
- Sin em-dashes (`—`) en headlines cortos: usar `:` o `·`
- Cards 3-up horizontal > 4 stacked
- WebP <200KB email · <500KB web
