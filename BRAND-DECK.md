# BRAND DECK — ROBOHOGAR

> Sistema de identidad visual multi-plataforma. Archivo ejecutable: la sección 13 contiene el mega-script que genera todos los assets.
>
> **No duplica definiciones existentes** — referencia los archivos fuente:
> - Paleta y tipografía → [`.claude/rules/design.md`](.claude/rules/design.md)
> - Voz y tono → [`docs/brand-voice.md`](docs/brand-voice.md)
> - Mascota base → [`assets/branding/mascota-prompt.md`](assets/branding/mascota-prompt.md)
> - Catálogo actual → [`assets/branding/asset-catalog.md`](assets/branding/asset-catalog.md)
> - Reglas editoriales → [`.claude/rules/editorial.md`](.claude/rules/editorial.md)
> - Reglas newsletter → [`.claude/rules/newsletter.md`](.claude/rules/newsletter.md)

---

## Índice

1. [Inventario actual](#1-inventario-actual)
2. [Gaps identificados](#2-gaps-identificados)
3. [Logo variants](#3-logo-variants)
4. [Social card templates](#4-social-card-templates)
5. [YouTube brand pack](#5-youtube-brand-pack)
6. [Patterns y texturas de fondo](#6-patterns-y-texturas-de-fondo)
7. [Icon library](#7-icon-library)
8. [Email template elements](#8-email-template-elements)
9. [Banner CTA de suscripción](#9-banner-cta-de-suscripción)
10. [Variaciones de mascota](#10-variaciones-de-mascota)
11. [Slide deck para sponsors](#11-slide-deck-para-sponsors)
12. [Reglas de uso y consistencia](#12-reglas-de-uso-y-consistencia)
13. [Mega-script de generación](#13-mega-script-de-generación)
14. [Actualización del asset-catalog](#14-actualización-del-asset-catalog)
15. [Checklist de verificación](#15-checklist-de-verificación)

---

## 1. Inventario actual

Lo que ya tenemos y NO hay que regenerar:

| Categoría | Assets | Ubicación |
|-----------|--------|-----------|
| Mascota (11 poses, 2K) | principal, saludando, casita, leyendo, thumbsup, detective, herramientas, megafono, pensativo, compras, trofeo | `assets/branding/master/` |
| Mascota (11 poses, 1K) | Mismas poses en resolución menor | `assets/branding/flash-1K/` |
| Mascota en contexto | Referencia hogar | `assets/branding/con-fondo/` |
| Logo header | `robohogar-logo-header-v3-bahnschrift.png` | `assets/branding/master/` |
| Logo icon | `robohogar-logo-icon-v6.png` | `assets/branding/master/` |
| Landing banners | 3 versiones + mascota hogar | `assets/images/` |
| OG images | 2 versiones | `assets/images/` |
| Social card template | 2 versiones | `assets/images/` |
| Newsletter header | 1 versión | `assets/images/` |
| Hero BG patterns | circuit, dots, grid (v1) | `assets/images/` |
| Hero artículos | 5 artículos con hero generado | `content/articulos/*/assets/` |

**Total existente:** ~45 assets. Detalles en [`asset-catalog.md`](assets/branding/asset-catalog.md).

---

## 2. Gaps identificados

Lo que falta para un sistema multi-plataforma completo:

| # | Gap | Assets a generar | Prioridad |
|---|-----|-----------------|-----------|
| G1 | Social card templates por plataforma | 5 templates (IG square, IG story, LinkedIn, X, WhatsApp) | Alta |
| G2 | YouTube brand pack | 6 assets (banner, 3 thumbnails, end-card, lower-third) | Alta |
| G3 | Patterns/texturas para fondos | 4 patterns (wave, hexagon, circuit-dark, dots-amber) | Media |
| G4 | Icon library (categorías) | 8 iconos (aspirador, cortacésped, humanoide, IA, comparativa, guía, opinión, novedad) | Media |
| G5 | Email template elements | 5 elements (divider, CTA button, footer, welcome hero, section header) | Media |
| G6 | Banner CTA suscripción | 3 variantes (inline, floating, exit-intent) | Alta |
| G7 | Variaciones de mascota (moods) | 6 nuevas poses (sorprendido, enfadado, celebrando, durmiendo, corriendo, cocinando) | Baja |
| G8 | Logo variants | 4 variantes (lockup horizontal, badge circular, monograma, dark mode) | Alta |
| G9 | Slide deck para sponsors | 8 slides (portada, misión, audiencia, métricas, contenido, tarifas, casos, contacto) | Media |

**Total a generar:** ~49 assets nuevos.

---

## 3. Logo variants

### 3.1 Lockup horizontal

Logo + nombre en línea. Para headers de web, firma de email, watermark de video.

```
Archivo de salida: assets/branding/master/robohogar-logo-lockup-horizontal.png
Dimensiones: 1200x300 px
```

**Prompt (inglés, nano-banana):**
```
Clean horizontal logo lockup on transparent background. Left: a small friendly robot icon with amber LED eyes and blue checkered apron (matching reference image). Right: "ROBOHOGAR" text in clean sans-serif font, weight 400. Colors: robot in white/gray/amber/cyan, text in #0C0C0C. Minimal, editorial style. High resolution, sharp edges.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 4:1
--model flash
```

### 3.2 Badge circular

Para avatares, favicons grandes, stickers. El icono del robot dentro de un círculo ámbar.

```
Archivo de salida: assets/branding/master/robohogar-logo-badge.png
Dimensiones: 800x800 px
```

**Prompt:**
```
Circular badge logo on transparent background. A small friendly robot with spherical white head, amber LED eyes, blue checkered apron with cyan heart, inside a perfect circle with #F5A623 amber border (4px weight). Background inside circle: white #FFFFFF. Clean vector style, works at 32px favicon size. No text.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 1:1
--model 2
```

### 3.3 Monograma

Letra "R" estilizada con elementos robot. Para watermarks, marca de agua en video.

```
Archivo de salida: assets/branding/master/robohogar-logo-monogram.png
Dimensiones: 600x600 px
```

**Prompt:**
```
Minimalist monogram letter "R" on transparent background. The letter incorporates subtle robotic elements: two small amber LED dots as eyes near the top of the R, a tiny antenna with orange ball on top. Letter color: #0C0C0C. Clean sans-serif font style similar to Jost. No other decorations. Works at 24px size.
--aspect 1:1
--model 2
```

### 3.4 Dark mode variant

Logo completo para fondos oscuros.

```
Archivo de salida: assets/branding/master/robohogar-logo-header-dark.png
Dimensiones: 1200x300 px
```

**Prompt:**
```
Clean horizontal logo lockup on transparent background, designed for dark backgrounds. Left: small friendly robot icon with bright amber LED eyes (#F5A623) and blue checkered apron, body in light gray/white. Right: "ROBOHOGAR" text in #FFFFFF white, clean sans-serif font weight 400. Minimal editorial style.
--reference assets/branding/master/robohogar-logo-header-v3-bahnschrift.png
--aspect 4:1
--model flash
```

---

## 4. Social card templates

Templates reutilizables por plataforma. Cada uno tiene zona para título, zona para imagen hero, y logo ROBOHOGAR.

### 4.1 Instagram Square (1080x1080)

```
Archivo de salida: assets/images/social-template-ig-square.png
```

**Prompt:**
```
Clean editorial social media card template, square format 1080x1080. White background #FFFFFF. Top: small robot mascot icon in top-left corner with "ROBOHOGAR" text next to it in dark sans-serif. Center: large empty rectangular area (placeholder for product image) with subtle #F2F2F2 gray background. Bottom: wide amber #F5A623 banner strip (80px height) for headline text area. Overall: magazine-style, generous white space, no clutter. Minimalist, modern.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 1:1
--model flash
```

### 4.2 Instagram Story (1080x1920)

```
Archivo de salida: assets/images/social-template-ig-story.png
```

**Prompt:**
```
Clean editorial social media story template, vertical 9:16 format. White background #FFFFFF. Top section: small robot mascot icon centered with "ROBOHOGAR" below it. Middle: large empty area with subtle dotted pattern background in #F2F2F2 (placeholder for product/hero image). Bottom third: solid amber #F5A623 section with space for headline and CTA. Clean, magazine-style, generous spacing.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 9:16
--model flash
```

### 4.3 LinkedIn / X post (1200x628)

```
Archivo de salida: assets/images/social-template-linkedin.png
```

**Prompt:**
```
Professional editorial social media card template, landscape 1200x628. White background #FFFFFF. Left third: vertical amber #F5A623 accent strip (40px wide). Small robot mascot icon in bottom-left corner. Center-right: large clean area for product image with subtle #F2F2F2 background. Top-right corner: "ROBOHOGAR" text in #0C0C0C small sans-serif. Bottom: thin dark #0C0C0C strip (60px) for headline area. Magazine editorial style, MIT Technology Review inspiration.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 1200:628
--model flash
```

### 4.4 X/Twitter post (1200x675)

```
Archivo de salida: assets/images/social-template-x.png
```

**Prompt:**
```
Clean social media card template, 16:9 landscape format. Minimal white #FFFFFF background. Top-left: tiny robot mascot icon. Top-right: "ROBOHOGAR" in small #6B7280 gray text. Center: dominant empty area for hero image with rounded corners and subtle shadow. Bottom: amber #F5A623 gradient fade strip (thin, 40px) at very bottom edge. Ultra-clean, modern, editorial.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 16:9
--model flash
```

### 4.5 WhatsApp share card (1200x630)

```
Archivo de salida: assets/images/social-template-whatsapp.png
```

**Prompt:**
```
Clean OG share card template, 1200x630 pixels landscape. White #FFFFFF background. Left side: friendly robot mascot (full body, small, ~200px) standing and waving. Right side: large clean area for title text on white background, with thin amber #F5A623 underline decoration. Bottom-right corner: "robohogar.com" in small #6B7280 gray text. Minimal, friendly, not corporate.
--reference assets/branding/master/robohogar-mascot-saludando.png
--aspect 1200:630
--model flash
```

---

## 5. YouTube brand pack

### 5.1 Banner canal (2560x1440)

Área segura para texto: 1546x423 (centro). Debe verse bien en TV, desktop y móvil.

```
Archivo de salida: assets/branding/master/youtube-banner.png
```

**Prompt:**
```
YouTube channel banner 2560x1440 for a home robotics channel called "ROBOHOGAR". Clean editorial design. Center safe area (1546x423): "ROBOHOGAR" in large clean sans-serif white text, subtitle below "Robots que YA llegan a tu hogar" in smaller text. Small robot mascot with amber LED eyes and blue apron standing to the right of text. Background: dark gradient from #0C0C0C to #1a1a2e with subtle hexagonal pattern overlay. Amber #F5A623 thin line accent under the title. Professional, magazine-style, not gaming/clickbait aesthetic.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 2560:1440
--model 2
```

### 5.2 Thumbnail template — Review

```
Archivo de salida: assets/images/youtube-thumb-review.png
```

**Prompt:**
```
YouTube thumbnail template 1280x720 for product review video. Clean white background. Left 60%: large empty area for product photo (placeholder, subtle #F2F2F2 background). Right 40%: bold verdict area with amber #F5A623 background, space for large rating number and short verdict text. Top-left corner: small "ROBOHOGAR" text in #0C0C0C. Bottom-right: tiny robot mascot giving thumbs up. MKBHD-inspired clean grid style, not clickbait. No excessive text, no arrows, no shocked faces.
--reference assets/branding/master/robohogar-mascot-thumbsup.png
--aspect 16:9
--model flash
```

### 5.3 Thumbnail template — Comparativa

```
Archivo de salida: assets/images/youtube-thumb-vs.png
```

**Prompt:**
```
YouTube thumbnail template 1280x720 for product comparison video. Clean split design: left half and right half separated by a thin amber #F5A623 vertical line with "VS" text in the center. Each half: clean #F2F2F2 light gray background area for product images. Top center: "ROBOHOGAR" in small dark text. Bottom: thin #0C0C0C dark strip for subtitle area. Magazine editorial style, not gaming clickbait. Minimal, professional.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 16:9
--model flash
```

### 5.4 Thumbnail template — Editorial/Opinión

```
Archivo de salida: assets/images/youtube-thumb-editorial.png
```

**Prompt:**
```
YouTube thumbnail template 1280x720 for editorial/opinion video. Dark background #0C0C0C with subtle circuit pattern overlay. Center: large empty area for dramatic product or concept image. Bottom-left: robot mascot in thinking pose (hand on chin). Top-right: "ROBOHOGAR" in amber #F5A623 text. Dramatic lighting feel, cinematic, editorial. MIT Technology Review aesthetic for video.
--reference assets/branding/master/robohogar-mascot-pensativo.png
--aspect 16:9
--model flash
```

### 5.5 End card (1920x1080)

```
Archivo de salida: assets/branding/master/youtube-endcard.png
```

**Prompt:**
```
YouTube end screen template 1920x1080. Dark background #1a1a2e with subtle dot pattern. Left side: robot mascot waving goodbye, friendly pose. Center: two rounded rectangles (300x170 each, outlined in amber #F5A623) as placeholders for recommended videos. Right: "SUSCRÍBETE" text with amber circle button placeholder below. Bottom: "robohogar.com" in small white text. Clean, not cluttered. Cinematic dark theme.
--reference assets/branding/master/robohogar-mascot-saludando.png
--aspect 16:9
--model flash
```

### 5.6 Lower-third (1920x200)

```
Archivo de salida: assets/branding/master/youtube-lower-third.png
```

**Prompt:**
```
YouTube lower-third banner graphic on transparent background, 1920x200 pixels. Left: small robot mascot icon (head only, ~100px). Center: clean dark #0C0C0C semi-transparent rectangle (80% opacity) with space for name/title text in white. Right edge: amber #F5A623 vertical accent bar (8px wide). Subtle, professional, not distracting. Broadcast-quality design.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 1920:200
--model flash
```

### 5.7 Watermark (150x150)

```
Archivo de salida: assets/branding/master/youtube-watermark.png
```

**Prompt:**
```
Tiny branding watermark 150x150 on transparent background. Simple robot head silhouette (spherical, two amber dot eyes, tiny antenna) in white with 50% opacity. Must be recognizable at actual 150px display size. Ultra-minimal, no text, no details beyond the silhouette.
--aspect 1:1
--model flash
```

---

## 6. Patterns y texturas de fondo

Patrones sutiles para fondos de secciones, newsletters, slides. Deben funcionar como background sin robar protagonismo.

### 6.1 Wave pattern

```
Archivo de salida: assets/images/pattern-wave-amber.png
Uso: Fondos de newsletter, secciones destacadas
Tile: sí (seamless)
```

**Prompt:**
```
Seamless tileable pattern, subtle wave lines in very light amber #F5A623 at 10% opacity on white #FFFFFF background. Gentle, flowing horizontal waves. Spacing between waves: generous. Must work as repeating CSS background-image. Editorial, magazine-quality. Not busy, very subtle.
--aspect 1:1
--model flash
```

### 6.2 Hexagon tech pattern

```
Archivo de salida: assets/images/pattern-hexagon-tech.png
Uso: Fondos tech/futurista para secciones de humanoides
Tile: sí
```

**Prompt:**
```
Seamless tileable pattern, subtle hexagonal grid in very light gray #F2F2F2 lines on white #FFFFFF background. Thin lines (1px feel), generous spacing between hexagons. One hexagon in every ~20 has a tiny amber #F5A623 dot in center. Tech/futuristic feel but extremely subtle. Works as repeating background without distracting from content.
--aspect 1:1
--model flash
```

### 6.3 Circuit pattern (dark mode)

```
Archivo de salida: assets/images/pattern-circuit-dark.png
Uso: Fondos oscuros (YouTube, slides, secciones premium)
Tile: sí
```

**Prompt:**
```
Seamless tileable pattern, subtle circuit board traces in #1a1a2e dark navy on #0C0C0C near-black background. Very thin lines forming circuit paths with occasional small dots at intersections. A few dots in amber #F5A623 (5% of total). Extremely subtle, cinematic, premium feel. Must tile seamlessly.
--aspect 1:1
--model flash
```

### 6.4 Dots pattern (ámbar suave)

```
Archivo de salida: assets/images/pattern-dots-amber-soft.png
Uso: Fondos universales, newsletters, cards
Tile: sí
```

**Prompt:**
```
Seamless tileable pattern, regular grid of small dots (3px diameter) in very light amber #F5A623 at 15% opacity on white #FFFFFF background. Dots spaced 24px apart in both directions. Clean, geometric, Swiss design influenced. Ultra-subtle, works behind text.
--aspect 1:1
--model flash
```

---

## 7. Icon library

Iconos de categorías de contenido. Estilo: line icons monocolor (ámbar sobre transparente), trazo 2px, 200x200 base.

### 7.1 Aspirador

```
Archivo: assets/images/icon-aspirador.png
```

**Prompt:**
```
Simple line icon of a robot vacuum cleaner, top-down view showing circular shape with sensor bump. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px. Clean vector style.
--aspect 1:1
--model flash
```

### 7.2 Cortacésped

```
Archivo: assets/images/icon-cortacesped.png
```

**Prompt:**
```
Simple line icon of a robotic lawn mower, side view profile showing low body with wheels and grass cutting. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.3 Humanoide

```
Archivo: assets/images/icon-humanoide.png
```

**Prompt:**
```
Simple line icon of a humanoid robot, front view, standing pose. Rounded head, simple body, two arms, two legs. Single color amber #F5A623 on transparent background. Line weight 2px, friendly not menacing, recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.4 IA / Inteligencia artificial

```
Archivo: assets/images/icon-ia.png
```

**Prompt:**
```
Simple line icon representing artificial intelligence: a stylized brain with circuit connections emanating from it. Single color amber #F5A623 on transparent background. Line weight 2px, modern, not cliché. Recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.5 Comparativa (VS)

```
Archivo: assets/images/icon-comparativa.png
```

**Prompt:**
```
Simple line icon of a balance scale with two platforms, representing comparison/versus. Single color amber #F5A623 on transparent background. Line weight 2px, symmetrical, clean. Recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.6 Guía / Tutorial

```
Archivo: assets/images/icon-guia.png
```

**Prompt:**
```
Simple line icon of an open book with a small gear/cog on one page, representing a how-to guide. Single color amber #F5A623 on transparent background. Line weight 2px, clean. Recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.7 Opinión

```
Archivo: assets/images/icon-opinion.png
```

**Prompt:**
```
Simple line icon of a speech bubble with three small dots inside, representing opinion/editorial. Single color amber #F5A623 on transparent background. Line weight 2px, rounded corners. Recognizable at 32px.
--aspect 1:1
--model flash
```

### 7.8 Novedad / Breaking

```
Archivo: assets/images/icon-novedad.png
```

**Prompt:**
```
Simple line icon of a lightning bolt inside a circle, representing breaking news/new product. Single color amber #F5A623 on transparent background. Line weight 2px, energetic but clean. Recognizable at 32px.
--aspect 1:1
--model flash
```

---

## 8. Email template elements

Elementos modulares para construir newsletters en Beehiiv. Estilo coherente con el design system.

### 8.1 Divider / Separador

```
Archivo: assets/images/email-divider.png
Dimensiones: 600x40 px
```

**Prompt:**
```
Horizontal email divider element on transparent background, 600x40 pixels. Center: thin amber #F5A623 line (1px) with a tiny robot head silhouette (amber, 20px) centered on the line. Clean, minimal, email-safe design. Works on both white and light gray backgrounds.
--aspect 600:40
--model flash
```

### 8.2 CTA button graphic

```
Archivo: assets/images/email-cta-button.png
Dimensiones: 300x60 px
```

**Prompt:**
```
Email CTA button on transparent background, 300x60 pixels. Rounded rectangle (8px radius) with solid amber #F5A623 fill. White text placeholder area centered inside. Clean shadow (2px, 10% opacity black). Professional, high contrast, works in email clients.
--aspect 300:60
--model flash
```

### 8.3 Footer branding

```
Archivo: assets/images/email-footer.png
Dimensiones: 600x120 px
```

**Prompt:**
```
Email footer element on transparent background, 600x120 pixels. Top: thin gray #E5E7EB line separator. Center: small robot mascot (60px) next to "ROBOHOGAR" text in #6B7280 gray. Below: small text area for "Robots que YA llegan a tu hogar" tagline. Clean, small, unobtrusive.
--reference assets/branding/master/robohogar-logo-icon-v6.png
--aspect 600:120
--model flash
```

### 8.4 Welcome hero (email de bienvenida)

```
Archivo: assets/images/email-welcome-hero.png
Dimensiones: 600x300 px
```

**Prompt:**
```
Welcome email hero banner, 600x300 pixels. White background #FFFFFF. Center: friendly robot mascot waving (full body, ~200px tall). Above robot: "¡Bienvenido a ROBOHOGAR!" text in dark #0C0C0C clean sans-serif. Below robot: amber #F5A623 underline decoration. Warm, friendly, inviting. Not corporate.
--reference assets/branding/master/robohogar-mascot-saludando.png
--aspect 600:300
--model 2
```

### 8.5 Section header (para newsletter semanal)

```
Archivo: assets/images/email-section-header.png
Dimensiones: 600x80 px
```

**Prompt:**
```
Newsletter section header element, 600x80 pixels on transparent background. Left: amber #F5A623 vertical bar (6px wide, full height). Right of bar: clean area for section title text in dark #0C0C0C. Bottom: very subtle #F2F2F2 gray line. Minimal, editorial, magazine-style.
--aspect 600:80
--model flash
```

---

## 9. Banner CTA de suscripción

Banners "¿Te está gustando? Suscríbete gratis" para incrustar en artículos y landing.

### 9.1 Inline (dentro de artículo)

```
Archivo: assets/images/cta-banner-inline.png
Dimensiones: 600x150 px
```

**Prompt:**
```
Inline subscription banner for blog article, 600x150 pixels. Light amber #FEF3C7 (10% amber tint) background with rounded corners (12px). Left: small robot mascot with megaphone pose (~100px). Right: space for text "¿Te está gustando?" headline and "Suscríbete gratis" CTA below. Clean amber #F5A623 button shape in bottom-right area. Friendly, not aggressive. Magazine editorial style.
--reference assets/branding/master/robohogar-mascot-megafono.png
--aspect 600:150
--model flash
```

### 9.2 Wide banner (para landing page)

```
Archivo: assets/images/cta-banner-wide.png
Dimensiones: 1200x200 px
```

**Prompt:**
```
Wide subscription banner for landing page, 1200x200 pixels. Gradient background from #0C0C0C to #1a1a2e dark with subtle circuit pattern. Left: robot mascot waving in full color (~150px). Center: "Tu dosis semanal de robótica doméstica" in white text, clean sans-serif. Right: large amber #F5A623 button shape for CTA. Premium, cinematic feel. Not clickbait.
--reference assets/branding/master/robohogar-mascot-saludando.png
--aspect 1200:200
--model 2
```

### 9.3 Square pop-up card (para redes)

```
Archivo: assets/images/cta-banner-square.png
Dimensiones: 800x800 px
```

**Prompt:**
```
Square subscription card, 800x800 pixels. White #FFFFFF background. Center: robot mascot holding a small house (casita pose, ~300px). Above: "ROBOHOGAR" in dark text. Below mascot: "Newsletter gratis cada semana" text area. Bottom: amber #F5A623 rounded button shape with "Suscríbete" text area. Generous white space, clean, inviting. Works as Instagram post or popup.
--reference assets/branding/master/robohogar-mascot-casita.png
--aspect 1:1
--model flash
```

---

## 10. Variaciones de mascota

6 nuevas poses para ampliar el rango emocional. Siguen las reglas de consistencia de [`mascota-prompt.md`](assets/branding/mascota-prompt.md): ojos LED ámbar, delantal cuadros azules con corazón, antenas con bolas naranjas, proporciones kawaii.

### 10.1 Sorprendido

```
Archivo: assets/branding/master/robohogar-mascot-sorprendido.png
Uso: Noticias inesperadas, "¿Sabías que...?", datos sorprendentes
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two wide-open amber/orange LED eyes in surprised expression, mouth shaped as small "O". Two thin antennas with orange balls on tips, raised higher than normal. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart and ruffled edges. Both hands raised to cheeks in surprise gesture, no objects held. Short legs with white rounded boots. Copper/orange joint details. Clean illustration style, consistent lighting.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

### 10.2 Enfadado / Frustrado

```
Archivo: assets/branding/master/robohogar-mascot-enfadado.png
Uso: Reviews negativos, "Lo que NO nos gusta", productos decepcionantes
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes narrowed in mild frustration, small frown. Two thin antennas with orange balls, slightly tilted. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Arms crossed over chest, no objects held. Short legs with white rounded boots. Expression is mildly annoyed, NOT angry or scary — still cute and approachable. Clean illustration style.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

### 10.3 Celebrando

```
Archivo: assets/branding/master/robohogar-mascot-celebrando.png
Uso: Lanzamientos, hitos del newsletter, mejores productos del año
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes curved upward in joy, big smile. Two thin antennas with orange balls, bouncing upward. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Both arms raised high above head, small confetti particles around (amber #F5A623 and cyan colored). One leg slightly lifted in dance pose. White rounded boots. Festive but clean. Clean illustration style.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

### 10.4 Durmiendo

```
Archivo: assets/branding/master/robohogar-mascot-durmiendo.png
Uso: "Modo silencioso", mantenimiento, "Volvemos pronto", error 503
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes as closed horizontal lines (sleeping). Two thin antennas with orange balls, drooping down slightly. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Sitting on ground, head tilted to one side, coffee mug resting beside it. Three small "Z" letters floating above head in amber #F5A623. White rounded boots. Peaceful, adorable. Clean illustration style.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

### 10.5 Corriendo / Urgente

```
Archivo: assets/branding/master/robohogar-mascot-corriendo.png
Uso: Breaking news, ofertas flash, "Última hora"
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes wide and determined. Two thin antennas with orange balls, swept back by wind. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart, apron fluttering behind. Running pose: one leg forward, one back, arms pumping. Right hand holds a small rolled newspaper or tablet. Motion lines behind the robot (2-3 thin lines). White rounded boots. Energetic but cute. Clean illustration style.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

### 10.6 Cocinando

```
Archivo: assets/branding/master/robohogar-mascot-cocinando.png
Uso: Contenido "recetas/tips del hogar", home automation, smart kitchen
```

**Prompt:**
```
Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes happy and focused. Two thin antennas with orange balls. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart — apron now makes extra sense as cooking apron. Right hand holds a wooden spoon, left hand holds a small steaming pot. Tiny chef hat (white, tilted slightly) on top of head between antennas. White rounded boots. Cozy, domestic, charming. Clean illustration style.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 1:1
--model 2
```

---

## 11. Slide deck para sponsors

8 slides conceptuales para presentar ROBOHOGAR a potenciales sponsors/anunciantes. Las imágenes de fondo de cada slide se generan con nano-banana. El contenido de texto se superpone manualmente (Canva, Google Slides, PowerPoint).

### Estructura del deck

| Slide | Título | Imagen de fondo | Texto clave |
|-------|--------|-----------------|-------------|
| 1 | Portada | Mascota + logo sobre fondo oscuro premium | "ROBOHOGAR — El medio de robótica doméstica en español" |
| 2 | Misión | Robot aspirador en hogar real, estilo cinematográfico | "Ayudamos a decidir qué robot merece la pena" |
| 3 | Audiencia | Iconos de personas + dispositivos | "Adultos 30-55, España + LATAM, interesados en tech doméstica" |
| 4 | Canales | Grid con iconos de plataformas | "Newsletter + Web + LinkedIn + X + YouTube" |
| 5 | Métricas | Gráfico placeholder (actualizar con datos reales) | "Open rate, suscriptores, pageviews" |
| 6 | Contenido | Collage de artículos/screenshots | "Reviews honestas, comparativas, guías, editorial" |
| 7 | Tarifas | Diseño limpio tipo pricing table | "Sponsor newsletter / Banner / Review patrocinada" |
| 8 | Contacto | Mascota saludando + datos | "Rafael — bakalap2@gmail.com — robohogar.com" |

### Slides como imágenes de fondo

```
Directorio de salida: assets/branding/slides/
```

**Slide 1 — Portada:**
```
Archivo: assets/branding/slides/slide-01-portada.png
```
```
Presentation slide background 1920x1080. Dark premium background, gradient from #0C0C0C to #1a1a2e. Center: friendly robot mascot with coffee mug (full body, ~400px) on right side. Left side: large clean area for title text. Subtle hexagonal pattern overlay at 5% opacity. Bottom: thin amber #F5A623 line across full width. Cinematic, premium, professional. NOT startup/tech-bro aesthetic.
--reference assets/branding/master/robohogar-mascot-principal.png
--aspect 16:9
--model 2
```

**Slide 2 — Misión:**
```
Archivo: assets/branding/slides/slide-02-mision.png
```
```
Presentation slide background 1920x1080. Warm, cinematic photo-style image of a modern living room with a robot vacuum cleaner working on hardwood floor. Golden hour lighting from large windows. Soft depth of field. Clean, aspirational home setting. Semi-transparent dark overlay (40% opacity) on left half for text area. Amber #F5A623 accent line on left edge. Photorealistic, editorial quality.
--aspect 16:9
--model 2
```

**Slide 3 — Audiencia:**
```
Archivo: assets/branding/slides/slide-03-audiencia.png
```
```
Presentation slide background 1920x1080. Clean white #FFFFFF background. Subtle grid of small icons representing audience: smartphones, tablets, homes, families — all in light #F2F2F2 gray as background pattern. Left side: large clean area for text and bullet points. Right side: abstract illustration of diverse people silhouettes looking at devices. Amber #F5A623 accent details on 2-3 icons. Professional, data-presentation style.
--aspect 16:9
--model flash
```

**Slide 4 — Canales:**
```
Archivo: assets/branding/slides/slide-04-canales.png
```
```
Presentation slide background 1920x1080. Dark #0C0C0C background. Five evenly spaced circular icons in a horizontal row across the center: envelope (newsletter), globe (web), briefcase (LinkedIn), bird/X shape (Twitter/X), play button (YouTube). Icons outlined in amber #F5A623, not filled. Subtle connecting lines between icons. Clean area above and below for text. Minimal, professional infographic style.
--aspect 16:9
--model flash
```

**Slide 5 — Métricas:**
```
Archivo: assets/branding/slides/slide-05-metricas.png
```
```
Presentation slide background 1920x1080. White #FFFFFF background. Three large placeholder card shapes arranged horizontally: each is a rounded rectangle (400x300) with #F2F2F2 background and thin #F5A623 amber top border (4px). Cards have space for metric number (large) and label (small). Clean area at top for slide title. Data dashboard aesthetic, clean and professional. No actual numbers — just placeholder shapes.
--aspect 16:9
--model flash
```

**Slide 6 — Contenido:**
```
Archivo: assets/branding/slides/slide-06-contenido.png
```
```
Presentation slide background 1920x1080. White background. Mosaic/grid layout of 6 placeholder rectangles (representing article screenshots) in 2 rows of 3, each with subtle shadow and rounded corners. One rectangle has amber #F5A623 border (featured). Small robot mascot with magnifying glass (detective pose) in bottom-right corner. Editorial, portfolio-style layout. Clean spacing.
--reference assets/branding/master/robohogar-mascot-detective.png
--aspect 16:9
--model flash
```

**Slide 7 — Tarifas:**
```
Archivo: assets/branding/slides/slide-07-tarifas.png
```
```
Presentation slide background 1920x1080. White #FFFFFF background. Three pricing column placeholders side by side: left (basic, #F2F2F2 header), center (featured, amber #F5A623 header, slightly taller), right (premium, #0C0C0C header). Each column has horizontal lines suggesting bullet points of features. Clean, SaaS-style pricing table aesthetic. Professional, trustworthy.
--aspect 16:9
--model flash
```

**Slide 8 — Contacto:**
```
Archivo: assets/branding/slides/slide-08-contacto.png
```
```
Presentation slide background 1920x1080. Split design: left 60% dark #0C0C0C background with subtle circuit pattern, right 40% white #FFFFFF. On the white side: robot mascot waving (full body, ~350px). On the dark side: large clean area for contact info text in white. Amber #F5A623 thin vertical divider between sections. Bottom: thin amber line. Warm, inviting, professional closing slide.
--reference assets/branding/master/robohogar-mascot-saludando.png
--aspect 16:9
--model flash
```

---

## 12. Reglas de uso y consistencia

### Cuándo usar cada variante de logo

| Contexto | Variante | Archivo |
|----------|----------|---------|
| Header web / newsletter | Logo header | `robohogar-logo-header-v3-bahnschrift.png` |
| Avatar redes (IG, X, LinkedIn) | Badge circular | `robohogar-logo-badge.png` |
| Favicon grande / sticker | Badge circular | `robohogar-logo-badge.png` |
| Watermark video | Monograma | `robohogar-logo-monogram.png` |
| Sobre fondo oscuro | Dark mode | `robohogar-logo-header-dark.png` |
| Inline con texto | Lockup horizontal | `robohogar-logo-lockup-horizontal.png` |

### Cuándo usar cada pose de mascota

| Contexto | Pose | Archivo |
|----------|------|---------|
| Avatar por defecto | Principal (café) | `robohogar-mascot-principal.png` |
| Email bienvenida, saludo | Saludando | `robohogar-mascot-saludando.png` |
| CTA suscripción | Megáfono o Casita | según contexto |
| Review positiva | Thumbs up | `robohogar-mascot-thumbsup.png` |
| Review negativa | Enfadado | `robohogar-mascot-enfadado.png` |
| Comparativa | Detective | `robohogar-mascot-detective.png` |
| Noticias urgentes | Corriendo | `robohogar-mascot-corriendo.png` |
| Dato curioso | Sorprendido | `robohogar-mascot-sorprendido.png` |
| Artículo pensado | Pensativo | `robohogar-mascot-pensativo.png` |
| Error / mantenimiento | Durmiendo | `robohogar-mascot-durmiendo.png` |
| Ranking / premio | Trofeo | `robohogar-mascot-trofeo.png` |
| Guía compras | Compras | `robohogar-mascot-compras.png` |
| Tutorial / guía | Herramientas | `robohogar-mascot-herramientas.png` |
| Lectura / digest | Leyendo | `robohogar-mascot-leyendo.png` |
| Hito / lanzamiento | Celebrando | `robohogar-mascot-celebrando.png` |
| Smart home / cocina | Cocinando | `robohogar-mascot-cocinando.png` |

### Reglas visuales invariables

1. **Ojos LED ámbar** (#F5A623) en TODAS las variantes de mascota — sin excepciones
2. **Delantal cuadros azules con corazón cyan** — siempre presente
3. **Antenas con bolas naranjas** — siempre visibles
4. **Proporciones kawaii** — cabeza grande, cuerpo compacto
5. **Sin mascota en hero images de artículos** — el producto es protagonista
6. **Logo ROBOHOGAR siempre legible a 120px** de ancho mínimo
7. **Patterns nunca a más del 15% de opacidad** — son fondos, no protagonistas
8. **Color ámbar para CTAs y acentos solamente** — nunca como color de fondo dominante

---

## 13. Mega-script de generación

Script bash que genera todos los assets del deck. Ejecutar desde la raíz del repo.

**Requisitos:**
- `GEMINI_API_KEY` configurada como variable de entorno
- Acceso al skill `/nano-banana` de Claude Code (o script equivalente en `utilities/`)
- ~$4-5 en créditos Gemini (50-60 imágenes)

**Ejecución:**
```bash
cd c:\Users\bakal\robohogar   # o la ruta que corresponda
bash BRAND-DECK-generate.sh
```

**Ejecución por secciones (para escalonar coste):**
```bash
bash BRAND-DECK-generate.sh logos        # Solo sección 3
bash BRAND-DECK-generate.sh social       # Solo sección 4
bash BRAND-DECK-generate.sh youtube      # Solo sección 5
bash BRAND-DECK-generate.sh patterns     # Solo sección 6
bash BRAND-DECK-generate.sh icons        # Solo sección 7
bash BRAND-DECK-generate.sh email        # Solo sección 8
bash BRAND-DECK-generate.sh cta          # Solo sección 9
bash BRAND-DECK-generate.sh mascota      # Solo sección 10
bash BRAND-DECK-generate.sh slides       # Solo sección 11
bash BRAND-DECK-generate.sh all          # Todo (default)
```

> **NOTA:** El mega-script se genera como archivo separado (`BRAND-DECK-generate.sh`) para mantener este deck como documento de referencia. El script lee los prompts de este archivo y los ejecuta secuencialmente.

```bash
#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
# BRAND-DECK-generate.sh — Generador de assets ROBOHOGAR
# Lee los prompts del BRAND-DECK.md y ejecuta nano-banana por lotes
# Idempotente: verifica existencia antes de generar, usa -v2 si existe
# ═══════════════════════════════════════════════════════════════════

set -euo pipefail

# --- Configuración ---
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SECTION="${1:-all}"
GENERATED=0
SKIPPED=0
FAILED=0

# --- Colores para stdout ---
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_ok()   { echo -e "${GREEN}[OK]${NC} $1"; }
log_skip() { echo -e "${YELLOW}[SKIP]${NC} $1 — ya existe"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $1"; }
log_section() { echo -e "\n${YELLOW}═══ $1 ═══${NC}"; }

# --- Verificación de entorno ---
if [ -z "${GEMINI_API_KEY:-}" ]; then
    echo -e "${RED}ERROR: GEMINI_API_KEY no está configurada${NC}"
    echo "Configúrala con: export GEMINI_API_KEY='tu-clave-aquí'"
    exit 1
fi

# --- Crear directorios necesarios ---
mkdir -p "$REPO_ROOT/assets/branding/master"
mkdir -p "$REPO_ROOT/assets/branding/slides"
mkdir -p "$REPO_ROOT/assets/images"

# --- Función principal de generación ---
# Genera una imagen con nano-banana. Si el archivo ya existe, salta.
# Si existe y hay conflicto, genera con sufijo -v2.
generate() {
    local output_path="$1"
    local prompt="$2"
    local reference="${3:-}"
    local aspect="${4:-1:1}"
    local model="${5:-flash}"

    local full_path="$REPO_ROOT/$output_path"

    # Idempotencia: no sobrescribir
    if [ -f "$full_path" ]; then
        log_skip "$output_path"
        SKIPPED=$((SKIPPED + 1))
        return 0
    fi

    echo "  Generando: $output_path (model=$model, aspect=$aspect)..."

    # Construir comando nano-banana
    local cmd="claude -p 'Usa /nano-banana para generar esta imagen. Prompt: $prompt"
    if [ -n "$reference" ]; then
        cmd="$cmd --reference $REPO_ROOT/$reference"
    fi
    cmd="$cmd --aspect $aspect --model $model"
    cmd="$cmd. Guarda el resultado en $full_path'"

    # Ejecutar (esto requiere claude CLI con nano-banana disponible)
    if eval "$cmd" 2>/dev/null; then
        if [ -f "$full_path" ]; then
            log_ok "$output_path"
            GENERATED=$((GENERATED + 1))
        else
            log_fail "$output_path — comando ejecutó pero archivo no creado"
            FAILED=$((FAILED + 1))
        fi
    else
        log_fail "$output_path"
        FAILED=$((FAILED + 1))
    fi
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 3: LOGOS
# ═══════════════════════════════════════════════════════════════════
run_logos() {
    log_section "LOGOS (4 assets)"

    generate "assets/branding/master/robohogar-logo-lockup-horizontal.png" \
        "Clean horizontal logo lockup on transparent background. Left: a small friendly robot icon with amber LED eyes and blue checkered apron (matching reference image). Right: ROBOHOGAR text in clean sans-serif font, weight 400. Colors: robot in white/gray/amber/cyan, text in #0C0C0C. Minimal, editorial style. High resolution, sharp edges." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "4:1" "flash"

    generate "assets/branding/master/robohogar-logo-badge.png" \
        "Circular badge logo on transparent background. A small friendly robot with spherical white head, amber LED eyes, blue checkered apron with cyan heart, inside a perfect circle with #F5A623 amber border (4px weight). Background inside circle: white #FFFFFF. Clean vector style, works at 32px favicon size. No text." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1:1" "2"

    generate "assets/branding/master/robohogar-logo-monogram.png" \
        "Minimalist monogram letter R on transparent background. The letter incorporates subtle robotic elements: two small amber LED dots as eyes near the top of the R, a tiny antenna with orange ball on top. Letter color: #0C0C0C. Clean sans-serif font style similar to Jost. No other decorations. Works at 24px size." \
        "" "1:1" "2"

    generate "assets/branding/master/robohogar-logo-header-dark.png" \
        "Clean horizontal logo lockup on transparent background, designed for dark backgrounds. Left: small friendly robot icon with bright amber LED eyes (#F5A623) and blue checkered apron, body in light gray/white. Right: ROBOHOGAR text in #FFFFFF white, clean sans-serif font weight 400. Minimal editorial style." \
        "assets/branding/master/robohogar-logo-header-v3-bahnschrift.png" "4:1" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 4: SOCIAL CARDS
# ═══════════════════════════════════════════════════════════════════
run_social() {
    log_section "SOCIAL CARD TEMPLATES (5 assets)"

    generate "assets/images/social-template-ig-square.png" \
        "Clean editorial social media card template, square format 1080x1080. White background #FFFFFF. Top: small robot mascot icon in top-left corner with ROBOHOGAR text next to it in dark sans-serif. Center: large empty rectangular area (placeholder for product image) with subtle #F2F2F2 gray background. Bottom: wide amber #F5A623 banner strip (80px height) for headline text area. Overall: magazine-style, generous white space, no clutter. Minimalist, modern." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1:1" "flash"

    generate "assets/images/social-template-ig-story.png" \
        "Clean editorial social media story template, vertical 9:16 format. White background #FFFFFF. Top section: small robot mascot icon centered with ROBOHOGAR below it. Middle: large empty area with subtle dotted pattern background in #F2F2F2 (placeholder for product/hero image). Bottom third: solid amber #F5A623 section with space for headline and CTA. Clean, magazine-style, generous spacing." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "9:16" "flash"

    generate "assets/images/social-template-linkedin.png" \
        "Professional editorial social media card template, landscape 1200x628. White background #FFFFFF. Left third: vertical amber #F5A623 accent strip (40px wide). Small robot mascot icon in bottom-left corner. Center-right: large clean area for product image with subtle #F2F2F2 background. Top-right corner: ROBOHOGAR text in #0C0C0C small sans-serif. Bottom: thin dark #0C0C0C strip (60px) for headline area. Magazine editorial style." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1200:628" "flash"

    generate "assets/images/social-template-x.png" \
        "Clean social media card template, 16:9 landscape format. Minimal white #FFFFFF background. Top-left: tiny robot mascot icon. Top-right: ROBOHOGAR in small #6B7280 gray text. Center: dominant empty area for hero image with rounded corners and subtle shadow. Bottom: amber #F5A623 gradient fade strip (thin, 40px) at very bottom edge. Ultra-clean, modern, editorial." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "16:9" "flash"

    generate "assets/images/social-template-whatsapp.png" \
        "Clean OG share card template, 1200x630 pixels landscape. White #FFFFFF background. Left side: friendly robot mascot (full body, small, ~200px) standing and waving. Right side: large clean area for title text on white background, with thin amber #F5A623 underline decoration. Bottom-right corner: robohogar.com in small #6B7280 gray text. Minimal, friendly, not corporate." \
        "assets/branding/master/robohogar-mascot-saludando.png" "1200:630" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 5: YOUTUBE
# ═══════════════════════════════════════════════════════════════════
run_youtube() {
    log_section "YOUTUBE BRAND PACK (7 assets)"

    generate "assets/branding/master/youtube-banner.png" \
        "YouTube channel banner 2560x1440 for a home robotics channel called ROBOHOGAR. Clean editorial design. Center safe area (1546x423): ROBOHOGAR in large clean sans-serif white text, subtitle below Robots que YA llegan a tu hogar in smaller text. Small robot mascot with amber LED eyes and blue apron standing to the right of text. Background: dark gradient from #0C0C0C to #1a1a2e with subtle hexagonal pattern overlay. Amber #F5A623 thin line accent under the title. Professional, magazine-style, not gaming/clickbait aesthetic." \
        "assets/branding/master/robohogar-mascot-principal.png" "2560:1440" "2"

    generate "assets/images/youtube-thumb-review.png" \
        "YouTube thumbnail template 1280x720 for product review video. Clean white background. Left 60%: large empty area for product photo (placeholder, subtle #F2F2F2 background). Right 40%: bold verdict area with amber #F5A623 background, space for large rating number and short verdict text. Top-left corner: small ROBOHOGAR text in #0C0C0C. Bottom-right: tiny robot mascot giving thumbs up. MKBHD-inspired clean grid style, not clickbait." \
        "assets/branding/master/robohogar-mascot-thumbsup.png" "16:9" "flash"

    generate "assets/images/youtube-thumb-vs.png" \
        "YouTube thumbnail template 1280x720 for product comparison video. Clean split design: left half and right half separated by a thin amber #F5A623 vertical line with VS text in the center. Each half: clean #F2F2F2 light gray background area for product images. Top center: ROBOHOGAR in small dark text. Bottom: thin #0C0C0C dark strip for subtitle area. Magazine editorial style, not gaming clickbait. Minimal, professional." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "16:9" "flash"

    generate "assets/images/youtube-thumb-editorial.png" \
        "YouTube thumbnail template 1280x720 for editorial/opinion video. Dark background #0C0C0C with subtle circuit pattern overlay. Center: large empty area for dramatic product or concept image. Bottom-left: robot mascot in thinking pose (hand on chin). Top-right: ROBOHOGAR in amber #F5A623 text. Dramatic lighting feel, cinematic, editorial." \
        "assets/branding/master/robohogar-mascot-pensativo.png" "16:9" "flash"

    generate "assets/branding/master/youtube-endcard.png" \
        "YouTube end screen template 1920x1080. Dark background #1a1a2e with subtle dot pattern. Left side: robot mascot waving goodbye, friendly pose. Center: two rounded rectangles (300x170 each, outlined in amber #F5A623) as placeholders for recommended videos. Right: SUSCRIBETE text with amber circle button placeholder below. Bottom: robohogar.com in small white text. Clean, not cluttered. Cinematic dark theme." \
        "assets/branding/master/robohogar-mascot-saludando.png" "16:9" "flash"

    generate "assets/branding/master/youtube-lower-third.png" \
        "YouTube lower-third banner graphic on transparent background, 1920x200 pixels. Left: small robot mascot icon (head only, ~100px). Center: clean dark #0C0C0C semi-transparent rectangle (80% opacity) with space for name/title text in white. Right edge: amber #F5A623 vertical accent bar (8px wide). Subtle, professional, not distracting. Broadcast-quality design." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "1920:200" "flash"

    generate "assets/branding/master/youtube-watermark.png" \
        "Tiny branding watermark 150x150 on transparent background. Simple robot head silhouette (spherical, two amber dot eyes, tiny antenna) in white with 50% opacity. Must be recognizable at actual 150px display size. Ultra-minimal, no text, no details beyond the silhouette." \
        "" "1:1" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 6: PATTERNS
# ═══════════════════════════════════════════════════════════════════
run_patterns() {
    log_section "PATTERNS Y TEXTURAS (4 assets)"

    generate "assets/images/pattern-wave-amber.png" \
        "Seamless tileable pattern, subtle wave lines in very light amber #F5A623 at 10% opacity on white #FFFFFF background. Gentle, flowing horizontal waves. Spacing between waves: generous. Must work as repeating CSS background-image. Editorial, magazine-quality. Not busy, very subtle." \
        "" "1:1" "flash"

    generate "assets/images/pattern-hexagon-tech.png" \
        "Seamless tileable pattern, subtle hexagonal grid in very light gray #F2F2F2 lines on white #FFFFFF background. Thin lines (1px feel), generous spacing between hexagons. One hexagon in every ~20 has a tiny amber #F5A623 dot in center. Tech/futuristic feel but extremely subtle." \
        "" "1:1" "flash"

    generate "assets/images/pattern-circuit-dark.png" \
        "Seamless tileable pattern, subtle circuit board traces in #1a1a2e dark navy on #0C0C0C near-black background. Very thin lines forming circuit paths with occasional small dots at intersections. A few dots in amber #F5A623 (5% of total). Extremely subtle, cinematic, premium feel. Must tile seamlessly." \
        "" "1:1" "flash"

    generate "assets/images/pattern-dots-amber-soft.png" \
        "Seamless tileable pattern, regular grid of small dots (3px diameter) in very light amber #F5A623 at 15% opacity on white #FFFFFF background. Dots spaced 24px apart in both directions. Clean, geometric, Swiss design influenced. Ultra-subtle, works behind text." \
        "" "1:1" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 7: ICONOS
# ═══════════════════════════════════════════════════════════════════
run_icons() {
    log_section "ICON LIBRARY (8 assets)"

    local icon_names=("aspirador" "cortacesped" "humanoide" "ia" "comparativa" "guia" "opinion" "novedad")
    local icon_prompts=(
        "Simple line icon of a robot vacuum cleaner, top-down view showing circular shape with sensor bump. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px. Clean vector style."
        "Simple line icon of a robotic lawn mower, side view profile showing low body with wheels and grass cutting. Single color amber #F5A623 on transparent background. Line weight 2px, minimal detail, recognizable at 32px."
        "Simple line icon of a humanoid robot, front view, standing pose. Rounded head, simple body, two arms, two legs. Single color amber #F5A623 on transparent background. Line weight 2px, friendly not menacing, recognizable at 32px."
        "Simple line icon representing artificial intelligence: a stylized brain with circuit connections emanating from it. Single color amber #F5A623 on transparent background. Line weight 2px, modern, not cliche. Recognizable at 32px."
        "Simple line icon of a balance scale with two platforms, representing comparison/versus. Single color amber #F5A623 on transparent background. Line weight 2px, symmetrical, clean. Recognizable at 32px."
        "Simple line icon of an open book with a small gear/cog on one page, representing a how-to guide. Single color amber #F5A623 on transparent background. Line weight 2px, clean. Recognizable at 32px."
        "Simple line icon of a speech bubble with three small dots inside, representing opinion/editorial. Single color amber #F5A623 on transparent background. Line weight 2px, rounded corners. Recognizable at 32px."
        "Simple line icon of a lightning bolt inside a circle, representing breaking news/new product. Single color amber #F5A623 on transparent background. Line weight 2px, energetic but clean. Recognizable at 32px."
    )

    for i in "${!icon_names[@]}"; do
        generate "assets/images/icon-${icon_names[$i]}.png" \
            "${icon_prompts[$i]}" \
            "" "1:1" "flash"
    done
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 8: EMAIL ELEMENTS
# ═══════════════════════════════════════════════════════════════════
run_email() {
    log_section "EMAIL TEMPLATE ELEMENTS (5 assets)"

    generate "assets/images/email-divider.png" \
        "Horizontal email divider element on transparent background, 600x40 pixels. Center: thin amber #F5A623 line (1px) with a tiny robot head silhouette (amber, 20px) centered on the line. Clean, minimal, email-safe design." \
        "" "600:40" "flash"

    generate "assets/images/email-cta-button.png" \
        "Email CTA button on transparent background, 300x60 pixels. Rounded rectangle (8px radius) with solid amber #F5A623 fill. White text placeholder area centered inside. Clean shadow (2px, 10% opacity black). Professional, high contrast." \
        "" "300:60" "flash"

    generate "assets/images/email-footer.png" \
        "Email footer element on transparent background, 600x120 pixels. Top: thin gray #E5E7EB line separator. Center: small robot mascot (60px) next to ROBOHOGAR text in #6B7280 gray. Below: small text area for tagline. Clean, small, unobtrusive." \
        "assets/branding/master/robohogar-logo-icon-v6.png" "600:120" "flash"

    generate "assets/images/email-welcome-hero.png" \
        "Welcome email hero banner, 600x300 pixels. White background #FFFFFF. Center: friendly robot mascot waving (full body, ~200px tall). Above robot: Bienvenido a ROBOHOGAR text in dark #0C0C0C clean sans-serif. Below robot: amber #F5A623 underline decoration. Warm, friendly, inviting." \
        "assets/branding/master/robohogar-mascot-saludando.png" "600:300" "2"

    generate "assets/images/email-section-header.png" \
        "Newsletter section header element, 600x80 pixels on transparent background. Left: amber #F5A623 vertical bar (6px wide, full height). Right of bar: clean area for section title text in dark #0C0C0C. Bottom: very subtle #F2F2F2 gray line. Minimal, editorial, magazine-style." \
        "" "600:80" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 9: BANNERS CTA
# ═══════════════════════════════════════════════════════════════════
run_cta() {
    log_section "BANNERS CTA SUSCRIPCIÓN (3 assets)"

    generate "assets/images/cta-banner-inline.png" \
        "Inline subscription banner for blog article, 600x150 pixels. Light amber #FEF3C7 (10% amber tint) background with rounded corners (12px). Left: small robot mascot with megaphone pose (~100px). Right: space for text headline and CTA below. Clean amber #F5A623 button shape in bottom-right area. Friendly, not aggressive. Magazine editorial style." \
        "assets/branding/master/robohogar-mascot-megafono.png" "600:150" "flash"

    generate "assets/images/cta-banner-wide.png" \
        "Wide subscription banner for landing page, 1200x200 pixels. Gradient background from #0C0C0C to #1a1a2e dark with subtle circuit pattern. Left: robot mascot waving in full color (~150px). Center: clean text area for tagline in white. Right: large amber #F5A623 button shape for CTA. Premium, cinematic feel." \
        "assets/branding/master/robohogar-mascot-saludando.png" "1200:200" "2"

    generate "assets/images/cta-banner-square.png" \
        "Square subscription card, 800x800 pixels. White #FFFFFF background. Center: robot mascot holding a small house (casita pose, ~300px). Above: ROBOHOGAR in dark text. Below mascot: newsletter tagline text area. Bottom: amber #F5A623 rounded button shape. Generous white space, clean, inviting." \
        "assets/branding/master/robohogar-mascot-casita.png" "1:1" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 10: NUEVAS POSES MASCOTA
# ═══════════════════════════════════════════════════════════════════
run_mascota() {
    log_section "VARIACIONES DE MASCOTA (6 assets)"

    generate "assets/branding/master/robohogar-mascot-sorprendido.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two wide-open amber/orange LED eyes in surprised expression, mouth shaped as small O. Two thin antennas with orange balls on tips, raised higher than normal. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart and ruffled edges. Both hands raised to cheeks in surprise gesture, no objects held. Short legs with white rounded boots. Copper/orange joint details. Clean illustration style, consistent lighting." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-enfadado.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes narrowed in mild frustration, small frown. Two thin antennas with orange balls, slightly tilted. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Arms crossed over chest, no objects held. Short legs with white rounded boots. Expression is mildly annoyed, NOT angry or scary — still cute and approachable. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-celebrando.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes curved upward in joy, big smile. Two thin antennas with orange balls, bouncing upward. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Both arms raised high above head, small confetti particles around (amber and cyan colored). One leg slightly lifted in dance pose. White rounded boots. Festive but clean. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-durmiendo.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes as closed horizontal lines (sleeping). Two thin antennas with orange balls, drooping down slightly. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Sitting on ground, head tilted to one side, coffee mug resting beside it. Three small Z letters floating above head in amber #F5A623. White rounded boots. Peaceful, adorable. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-corriendo.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes wide and determined. Two thin antennas with orange balls, swept back by wind. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart, apron fluttering behind. Running pose: one leg forward, one back, arms pumping. Right hand holds a small rolled newspaper or tablet. Motion lines behind the robot (2-3 thin lines). White rounded boots. Energetic but cute. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"

    generate "assets/branding/master/robohogar-mascot-cocinando.png" \
        "Character illustration on clean white background. A small cute kawaii robot, round spherical white head with large black LED visor display showing two amber/orange LED eyes happy and focused. Two thin antennas with orange balls. Blue/gray circle on head side. Compact body, light blue checkered apron with cyan heart. Right hand holds a wooden spoon, left hand holds a small steaming pot. Tiny chef hat (white, tilted slightly) on top of head between antennas. White rounded boots. Cozy, domestic, charming. Clean illustration style." \
        "assets/branding/master/robohogar-mascot-principal.png" "1:1" "2"
}

# ═══════════════════════════════════════════════════════════════════
# SECCIÓN 11: SLIDES
# ═══════════════════════════════════════════════════════════════════
run_slides() {
    log_section "SLIDE DECK BACKGROUNDS (8 assets)"

    generate "assets/branding/slides/slide-01-portada.png" \
        "Presentation slide background 1920x1080. Dark premium background, gradient from #0C0C0C to #1a1a2e. Center: friendly robot mascot with coffee mug (full body, ~400px) on right side. Left side: large clean area for title text. Subtle hexagonal pattern overlay at 5% opacity. Bottom: thin amber #F5A623 line across full width. Cinematic, premium, professional." \
        "assets/branding/master/robohogar-mascot-principal.png" "16:9" "2"

    generate "assets/branding/slides/slide-02-mision.png" \
        "Presentation slide background 1920x1080. Warm, cinematic photo-style image of a modern living room with a robot vacuum cleaner working on hardwood floor. Golden hour lighting from large windows. Soft depth of field. Semi-transparent dark overlay (40% opacity) on left half for text area. Amber #F5A623 accent line on left edge. Photorealistic, editorial quality." \
        "" "16:9" "2"

    generate "assets/branding/slides/slide-03-audiencia.png" \
        "Presentation slide background 1920x1080. Clean white #FFFFFF background. Subtle grid of small icons representing audience: smartphones, tablets, homes, families — all in light #F2F2F2 gray as background pattern. Left side: large clean area for text and bullet points. Right side: abstract illustration of diverse people silhouettes looking at devices. Amber #F5A623 accent details on 2-3 icons. Professional." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-04-canales.png" \
        "Presentation slide background 1920x1080. Dark #0C0C0C background. Five evenly spaced circular icons in a horizontal row across the center: envelope (newsletter), globe (web), briefcase (LinkedIn), X shape (Twitter/X), play button (YouTube). Icons outlined in amber #F5A623, not filled. Subtle connecting lines between icons. Minimal, professional infographic style." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-05-metricas.png" \
        "Presentation slide background 1920x1080. White #FFFFFF background. Three large placeholder card shapes arranged horizontally: each is a rounded rectangle (400x300) with #F2F2F2 background and thin #F5A623 amber top border (4px). Cards have space for metric number (large) and label (small). Data dashboard aesthetic, clean and professional." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-06-contenido.png" \
        "Presentation slide background 1920x1080. White background. Mosaic/grid layout of 6 placeholder rectangles (representing article screenshots) in 2 rows of 3, each with subtle shadow and rounded corners. One rectangle has amber #F5A623 border (featured). Small robot mascot with magnifying glass in bottom-right corner. Editorial, portfolio-style layout." \
        "assets/branding/master/robohogar-mascot-detective.png" "16:9" "flash"

    generate "assets/branding/slides/slide-07-tarifas.png" \
        "Presentation slide background 1920x1080. White #FFFFFF background. Three pricing column placeholders side by side: left (basic, #F2F2F2 header), center (featured, amber #F5A623 header, slightly taller), right (premium, #0C0C0C header). Each column has horizontal lines suggesting bullet points. Clean, SaaS-style pricing table aesthetic." \
        "" "16:9" "flash"

    generate "assets/branding/slides/slide-08-contacto.png" \
        "Presentation slide background 1920x1080. Split design: left 60% dark #0C0C0C background with subtle circuit pattern, right 40% white #FFFFFF. On the white side: robot mascot waving (full body, ~350px). On the dark side: large clean area for contact info text in white. Amber #F5A623 thin vertical divider between sections. Warm, inviting, professional closing slide." \
        "assets/branding/master/robohogar-mascot-saludando.png" "16:9" "flash"
}

# ═══════════════════════════════════════════════════════════════════
# DISPATCHER
# ═══════════════════════════════════════════════════════════════════
case "$SECTION" in
    logos)    run_logos ;;
    social)   run_social ;;
    youtube)  run_youtube ;;
    patterns) run_patterns ;;
    icons)    run_icons ;;
    email)    run_email ;;
    cta)      run_cta ;;
    mascota)  run_mascota ;;
    slides)   run_slides ;;
    all)
        run_logos
        run_social
        run_youtube
        run_patterns
        run_icons
        run_email
        run_cta
        run_mascota
        run_slides
        ;;
    *)
        echo "Uso: $0 {logos|social|youtube|patterns|icons|email|cta|mascota|slides|all}"
        exit 1
        ;;
esac

# ═══════════════════════════════════════════════════════════════════
# RESUMEN
# ═══════════════════════════════════════════════════════════════════
echo ""
echo "═══════════════════════════════════════"
echo -e "  Generados: ${GREEN}$GENERATED${NC}"
echo -e "  Saltados:  ${YELLOW}$SKIPPED${NC} (ya existían)"
echo -e "  Fallidos:  ${RED}$FAILED${NC}"
echo "═══════════════════════════════════════"
echo ""
echo "Siguiente paso: actualizar assets/branding/asset-catalog.md"
echo "Ver sección 14 del BRAND-DECK.md para el texto exacto."
```

> **IMPORTANTE:** Este script usa `claude -p` para invocar nano-banana. Si prefieres ejecutar los prompts manualmente uno a uno con `/nano-banana` dentro de una sesión de Claude Code, puedes copiar cada prompt de las secciones 3-11 de este deck.

---

## 14. Actualización del asset-catalog

Tras ejecutar el mega-script, añadir estas filas al [`asset-catalog.md`](assets/branding/asset-catalog.md):

### Nuevas filas para la tabla de logos

```markdown
| `robohogar-logo-lockup-horizontal.png` | Logo + nombre horizontal | `master/` | Header web, firma email, watermark | flash |
| `robohogar-logo-badge.png` | Badge circular para avatares | `master/` | Avatar redes, favicon, sticker | model 2 |
| `robohogar-logo-monogram.png` | Monograma "R" con elementos robot | `master/` | Watermark video, marca de agua | model 2 |
| `robohogar-logo-header-dark.png` | Logo horizontal para fondos oscuros | `master/` | YouTube, slides, dark sections | flash |
```

### Nuevas filas para la tabla de mascota

```markdown
| L | Sorprendido | Ojos abiertos, manos en mejillas | Noticias inesperadas, datos curiosos | `robohogar-mascot-sorprendido.png` |
| M | Enfadado | Ojos entrecerrados, brazos cruzados | Reviews negativos, decepciones | `robohogar-mascot-enfadado.png` |
| N | Celebrando | Brazos arriba, confeti | Lanzamientos, hitos, premios | `robohogar-mascot-celebrando.png` |
| O | Durmiendo | Ojos cerrados, sentado, "Zzz" | Mantenimiento, error 503, pausa | `robohogar-mascot-durmiendo.png` |
| P | Corriendo | Pose dinámica, periódico en mano | Breaking news, ofertas flash | `robohogar-mascot-corriendo.png` |
| Q | Cocinando | Cuchara + olla, gorro chef | Smart kitchen, home automation | `robohogar-mascot-cocinando.png` |
```

### Nueva sección: Social templates

```markdown
## Social Card Templates

| Archivo | Plataforma | Dimensiones | Ubicación |
|---------|-----------|-------------|-----------|
| `social-template-ig-square.png` | Instagram feed | 1080x1080 | `assets/images/` |
| `social-template-ig-story.png` | Instagram story | 1080x1920 | `assets/images/` |
| `social-template-linkedin.png` | LinkedIn | 1200x628 | `assets/images/` |
| `social-template-x.png` | X/Twitter | 1200x675 | `assets/images/` |
| `social-template-whatsapp.png` | WhatsApp share | 1200x630 | `assets/images/` |
```

### Nueva sección: YouTube

```markdown
## YouTube Brand Pack

| Archivo | Elemento | Dimensiones | Ubicación |
|---------|---------|-------------|-----------|
| `youtube-banner.png` | Banner canal | 2560x1440 | `assets/branding/master/` |
| `youtube-thumb-review.png` | Thumbnail review | 1280x720 | `assets/images/` |
| `youtube-thumb-vs.png` | Thumbnail comparativa | 1280x720 | `assets/images/` |
| `youtube-thumb-editorial.png` | Thumbnail editorial | 1280x720 | `assets/images/` |
| `youtube-endcard.png` | End card | 1920x1080 | `assets/branding/master/` |
| `youtube-lower-third.png` | Lower-third | 1920x200 | `assets/branding/master/` |
| `youtube-watermark.png` | Watermark | 150x150 | `assets/branding/master/` |
```

### Nueva sección: Elementos varios

```markdown
## Patterns, Iconos y Email Elements

| Archivo | Tipo | Uso | Ubicación |
|---------|------|-----|-----------|
| `pattern-wave-amber.png` | Pattern | Fondos newsletter, secciones | `assets/images/` |
| `pattern-hexagon-tech.png` | Pattern | Fondos tech/futurista | `assets/images/` |
| `pattern-circuit-dark.png` | Pattern | Fondos oscuros premium | `assets/images/` |
| `pattern-dots-amber-soft.png` | Pattern | Fondos universales | `assets/images/` |
| `icon-aspirador.png` | Icono | Categoría aspiradores | `assets/images/` |
| `icon-cortacesped.png` | Icono | Categoría cortacéspedes | `assets/images/` |
| `icon-humanoide.png` | Icono | Categoría humanoides | `assets/images/` |
| `icon-ia.png` | Icono | Categoría IA | `assets/images/` |
| `icon-comparativa.png` | Icono | Categoría comparativas | `assets/images/` |
| `icon-guia.png` | Icono | Categoría guías | `assets/images/` |
| `icon-opinion.png` | Icono | Categoría opinión | `assets/images/` |
| `icon-novedad.png` | Icono | Categoría novedades | `assets/images/` |
| `email-divider.png` | Email | Separador newsletter | `assets/images/` |
| `email-cta-button.png` | Email | Botón CTA | `assets/images/` |
| `email-footer.png` | Email | Footer branding | `assets/images/` |
| `email-welcome-hero.png` | Email | Hero bienvenida | `assets/images/` |
| `email-section-header.png` | Email | Cabecera sección | `assets/images/` |
| `cta-banner-inline.png` | CTA | Banner inline artículo | `assets/images/` |
| `cta-banner-wide.png` | CTA | Banner wide landing | `assets/images/` |
| `cta-banner-square.png` | CTA | Card cuadrada redes | `assets/images/` |
```

### Nueva sección: Slides

```markdown
## Slide Deck — Sponsors

| Archivo | Slide | Ubicación |
|---------|-------|-----------|
| `slide-01-portada.png` | Portada | `assets/branding/slides/` |
| `slide-02-mision.png` | Misión | `assets/branding/slides/` |
| `slide-03-audiencia.png` | Audiencia | `assets/branding/slides/` |
| `slide-04-canales.png` | Canales | `assets/branding/slides/` |
| `slide-05-metricas.png` | Métricas | `assets/branding/slides/` |
| `slide-06-contenido.png` | Contenido | `assets/branding/slides/` |
| `slide-07-tarifas.png` | Tarifas | `assets/branding/slides/` |
| `slide-08-contacto.png` | Contacto | `assets/branding/slides/` |
```

---

## 15. Checklist de verificación

### Inmediata (tras escribir este deck)

- [ ] `BRAND-DECK.md` existe en la raíz del repo
- [ ] Las 15 secciones están presentes y numeradas
- [ ] Todos los paths de output usan la estructura de carpetas existente
- [ ] No se duplican definiciones de paleta/tipografía/voz (solo referencias)
- [ ] Prompts en inglés, texto del deck en español
- [ ] Filenames en kebab-case
- [ ] El mega-script tiene check de idempotencia (`if [ -f file ]`)

### En el PC de Rafael (tras `git pull`)

- [ ] Abrir `BRAND-DECK.md` — renderiza correctamente
- [ ] Ejecutar `bash BRAND-DECK-generate.sh logos` como test
- [ ] Verificar que los archivos se crean en los paths correctos
- [ ] Ejecutar `bash BRAND-DECK-generate.sh all` para generar todo
- [ ] Revisar progreso en stdout (sección por sección)

### Visual QA (tras generación)

- [ ] Cada asset reconocible a 300px (miniatura)
- [ ] Mascota mantiene ojos LED ámbar en todas las variantes
- [ ] Mascota mantiene delantal cuadros azules con corazón en todas las variantes
- [ ] Mascota mantiene antenas con bolas naranjas
- [ ] Banners CTA tienen espacio claro para texto (no saturados)
- [ ] Patterns son sutiles como fondos (no roban protagonismo)
- [ ] Logo legible a 120px de ancho mínimo
- [ ] Templates sociales tienen zonas vacías claras para contenido

### Post-generación

- [ ] Actualizar `assets/branding/asset-catalog.md` con filas de sección 14
- [ ] Commit con mensaje descriptivo
- [ ] Mover `BRAND-DECK-generate.sh` a `utilities/_archive/` tras usar (one-shot)

---

## Coste estimado

| Modelo | Uso | Cantidad | Coste/imagen | Total |
|--------|-----|----------|-------------|-------|
| Flash | Drafts, templates, iconos, patterns | ~35 | ~$0.02 | ~$0.70 |
| Model 2 | Assets definitivos (mascota, YouTube banner, slides premium) | ~14 | ~$0.10 | ~$1.40 |
| **Total** | | **~49** | | **~$2.10** |

> Se puede ejecutar por secciones para escalonar el coste. Las secciones son independientes entre sí.
