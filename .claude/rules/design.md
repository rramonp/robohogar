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

## Integridad imagen ↔ caption

Toda pareja `<img>` + `<p class="fig-caption">` en un borrador va precedida por un comentario HTML identificador en línea única, inmediatamente antes del `<img>`:

```html
<!-- FIG N: <marca + modelo + detalle clave> -->
<img class="inline" src="assets/..." alt="...">
<p class="fig-caption">Imagen: ...</p>
```

- `N` es el índice secuencial empezando por 0 (hero = FIG 0).
- El detalle clave es la característica que justifica la imagen (ej: "fregado por rodillo", "patas extensibles 6 cm", "rodillo antienredos"). Sirve para que al mover/reordenar secciones, el caption nunca quede huérfano ni apuntando a otra imagen.
- El comentario NO se copia a Beehiiv (es HTML comment, invisible).

**Why:** incidente 2026-04-19 — Rafael pegó un caption que se refería a una figura distinta de la que había seleccionado. El marcador FIG N evita swaps accidentales al reordenar secciones del borrador.

Skills que generan borradores (`/content-draft`, futuros) aplican esta regla sin excepción. Verificación pre-output: cada `<img>` del borrador debe tener exactamente un comentario `<!-- FIG N: ... -->` en la línea inmediatamente anterior.

## Bloques de código para snippets HTML inline en borradores

Cuando un borrador necesita un snippet HTML que NO forma parte del cuerpo editorial (banners de lead magnet, tangibles embebidos, widgets Beehiiv custom), se representa en el borrador como **bloque de código visible** (`.snippet-block`), no como `<div>` renderizado.

**Por qué:** Rafael publica haciendo copy-paste desde el borrador al editor Beehiiv. Los banners se pegan vía `/html` → Custom HTML block, que requiere el **HTML como texto copiable**, no como elemento ya renderizado. Si el banner vive como `<div>` inline en el borrador, al copiar desde navegador se copia el texto visible, no el código source.

**Estructura obligatoria:**

```html
<div class="snippet-block">
  <p class="snippet-header">📋 Snippet N · <tipo de snippet> · <posición>"</p>
  <p class="snippet-hint">En Beehiiv: escribe <code>/html</code> → "Custom HTML block" → pega el código.</p>
  <pre><code>&lt;div style="..."&gt;...&lt;/div&gt;</code></pre>
</div>
```

- `<pre><code>` contiene el HTML del snippet **escapado** (`<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`).
- Todo el contenido del snippet cabe dentro del mismo `<pre>` para selección fácil en el navegador.
- El `.snippet-block` es visualmente distinto del cuerpo del artículo (fondo gris, borde dashed) para que Rafael lo identifique al instante como "esto no es contenido publicable, es para copy-paste a Beehiiv".

**CSS canónico** (copiar al `<style>` de cada borrador):

```css
.snippet-block { background: #F0F0F0; border: 2px dashed #535252; border-radius: 8px; padding: 16px 18px; margin: 32px 0; }
.snippet-block .snippet-header { font-family: 'DM Sans', sans-serif; font-weight: 700; font-size: 14px; color: #283642; margin: 0 0 6px; letter-spacing: 0.5px; text-transform: uppercase; }
.snippet-block .snippet-hint { font-style: italic; font-size: 13px; color: #6B7280; margin: 0 0 12px; }
.snippet-block pre { background: #FFFFFF; border: 1px solid #C0C0C0; border-radius: 4px; padding: 12px 14px; margin: 0; overflow-x: auto; }
.snippet-block code { font-family: 'Courier New', Consolas, Monaco, monospace; font-size: 12px; color: #0C0C0C; white-space: pre-wrap; word-break: break-word; }
```

Skills que generan borradores aplican esta regla cuando el HTML destino incluye cualquier banner lead magnet o snippet embebible.
