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

## Mobile-first (NO negociable · 80 % del tráfico ROBOHOGAR)

**Refuerzo 2026-04-23 — regla dura sobre todo elemento visual, no solo headlines.** El 80 % del tráfico de ROBOHOGAR llega desde móvil. **Cualquier contenedor, gráfico, tabla, árbol de decisión, infografía o bloque visual** que no renderice legible en viewport de 375 px se considera defectuoso y **no es entregable**. No hay excepciones.

**Reglas duras:**

1. **Prohibido ASCII art para contenidos publicables al lector** (árboles `├ └ ─ │`, diagramas monospace con indentación progresiva, flowcharts con box-drawing). En móvil los caracteres monospace sin wrap se desbordan por la derecha o rompen las líneas, y la estructura visual se destruye entera. **Sustituir por HTML semántico:** tarjetas apiladas con CSS (patrón `.decision-cards` + `.decision-card` con preguntas numeradas y paths `Sí → modelo` / `No → modelo`), listas numeradas con conectores textuales, o bloques separados con flechas visuales vía paleta ámbar. Ver ejemplo vivo: `content/articulos/mejor-robot-aspirador-mascotas-2026/borrador.html § decision-cards`.

2. **Tablas.** Máximo 4 `<th>` por `<thead>` + ≤25 caracteres por celda orientativo. Nombres de producto cortos. Sin paréntesis largos en celdas (los matices van al caption o al cuerpo). Detalle completo en `@rules/editorial.md § Formato técnico Beehiiv (tablas)`.

3. **`<pre>` con texto ancho en prosa publicable.** Prohibido. Solo permitido en snippets de código para copy-paste a Beehiiv (donde el scroll horizontal es aceptable porque el lector NO los lee, solo los copia vía botón Copy). Para cualquier otro contenido: HTML semántico + CSS responsive.

4. **Gráficos, diagramas, infografías inline.** Si la idea no se entiende en 375 px con ≤12 palabras por línea visible, rediseñar antes de entregar. Imágenes-diagrama generadas con IA van con alt-text descriptivo y caption que explique la idea en prosa — por si el render en móvil se lee mal.

5. **Headlines / bullets**: ≤40 chars (más → wrap raro). Sin em-dashes (`—`) en headlines cortos: usar `:` o `·`.

6. **Cards**: 3-up horizontal sobre 4-stacked. Apilar natural en móvil vía `flex-wrap` / CSS grid auto-fit.

7. **Peso de imágenes**: WebP <200 KB email · <500 KB web.

**Validación pre-output OBLIGATORIA.** Antes de cerrar cualquier borrador, simular el render en viewport 375 px. Si un bloque (tabla, árbol, diagrama, card grande) requiere **scroll horizontal para leerse** o **se corta por el borde derecho** en ese ancho → **rediseñar antes de entregar**, no documentar como "mejora futura".

**Incidente origen 2026-04-23:** árbol de decisión ASCII del borrador #10 (*mejor-robot-aspirador-mascotas-2026*) usaba caracteres box-drawing con indentación progresiva. En desktop se veía bien; en móvil las líneas largas de la rama más profunda rompían wrap donde no tocaba y la estructura del árbol se perdía entera — Rafael lo detectó al instante (*"el cuadro es inviable en móvil, todo se desorganiza"*). Solución canonizada: patrón `.decision-cards` con tarjetas apiladas + preguntas numeradas + paths Sí/No como pill-blocks. El patrón antiguo (monospace `<pre>`) queda prohibido para contenidos publicables.

Skills que generan contenido publicable (`/content-draft`, `/ficcion-draft`, `/pdf-brand`, `/social-content`, futuros) aplican esta regla sin excepción.

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

**Regla complementaria — cobertura visual de productos analizados** (2026-04-23): en artículos de comparativa, guía de compra, review multi-producto o editorial que analice productos concretos, **todo producto con sección de análisis propio** (`<div class="model-card">`, H2/H3 con nombre de modelo + bloque de precio) DEBE llevar foto inline. Los descartados NO. Regla + script de verificación: `@rules/editorial.md § Controles pre-publicación § B5` + `@.claude/commands/content-draft.md § 8.5 cinco`.

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

**Ampliación 2026-04-23 — bloques visuales complejos del cuerpo editorial (árboles de decisión, infografías, tarjetas apiladas, tablas estilizadas).** El patrón `.snippet-block` no es solo para banners/CTAs: aplica también a **cualquier bloque visual del cuerpo del artículo que dependa de CSS propio** y tenga que pegarse en Beehiiv vía `/html` → Custom HTML block. Ejemplo canónico: el árbol de decisión de 4 preguntas en `content/articulos/mejor-robot-aspirador-mascotas-2026/borrador.html` (3 snippets totales: CTA final · Banner Hoja de Compra · Árbol de decisión).

**Regla: preview renderizado + snippet inline copy-paste.** Cuando un bloque visual del cuerpo requiere CSS para leerse correctamente (decision-tree, pasos numerados con iconos, tarjetas comparativas, callouts estilizados), el borrador lleva **dos representaciones en orden**:

1. **Preview renderizado** (HTML con clases CSS del `<style>` global del borrador) — Rafael lo ve al abrir el preview en navegador para validar que el bloque queda bien con el resto del artículo. Precedido por comentario HTML: `<!-- Preview renderizado del X (solo visible en el borrador; no copiar a Beehiiv) -->`.

2. **Snippet-block con el HTML en estilos inline** inmediatamente después — `<pre><code>` escapado con `&lt;` / `&gt;` / `&amp;`. Rafael lo copia a Beehiiv vía `/html` → Custom HTML block. **Los estilos inline son obligatorios**: las clases CSS del borrador no viajan a Beehiiv (el editor aplica su propio estilo al hacer paste directo), así que cada elemento del snippet-inline debe llevar `style="..."` con todos los estilos necesarios para sobrevivir al paste.

**Requisitos del HTML del snippet inline** (mobile-first obligatorio):
- Stack natural vertical sin `@media queries` (Beehiiv Custom HTML no siempre respeta media queries según plantilla/email).
- Padding + font-size + line-height razonables para 375 px.
- Paleta ROBOHOGAR: crema `#FFF9EF`, ámbar `#F5A623`, gris `#6B7280`, texto `#0C0C0C`, blanco `#FFFFFF`.
- `font-family` declarada explícitamente en el contenedor raíz (`'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif` para cuerpo, `'DM Sans',sans-serif` para títulos).
- Sin `<strong>` dentro de elementos con fondo crema si el bloque es tipo checklist/callout (regla `@rules/editorial.md § Política de negritas`); usar `<span style="font-weight:700;...">` con color que justifique el énfasis.

**Incidente origen:** borrador #10 *mejor-robot-aspirador-mascotas-2026* entregó el árbol de decisión solo con clases CSS (`.decision-cards / .decision-card / .path`). Rafael al pegarlo a Beehiiv perdió todos los estilos (*"no me queda bien ponerlo como texto directamente desde el newsletter"*). Solución: añadir `.snippet-block` con el HTML inline equivalente, manteniendo el preview renderizado arriba para validación visual del borrador. El patrón ahora es norma para cualquier bloque visual complejo del cuerpo — no solo banners y CTAs.

Skills que generan borradores (`/content-draft`, `/pdf-brand`, futuros) aplican esta regla cuando el borrador incluye bloques visuales con CSS propio. Verificación pre-output: por cada `<div class="decision-cards">`, `<div class="infographic">`, `<div class="comparison-cards">` o equivalente con CSS de clase en el cuerpo editorial, debe existir un `.snippet-block` correspondiente con el HTML en estilos inline equivalentes.
