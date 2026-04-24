---
name: CTA suscripción final obligatorio en artículos ROBOHOGAR
description: Todo artículo no-ficción cierra con snippet dark "¿Te ha servido este análisis?" → botón Suscribirse → https://robohogar.com; posición: tras ¿Sabías que? + separator, antes de Más en ROBOHOGAR; sin UTM
type: feedback
originSessionId: 749cb54f-081c-4d7c-81a5-0a9108ab2b98
---
Todo borrador ROBOHOGAR **no-ficción** (review, comparativa, editorial, guía, tutorial, newsletter semanal) cierra con el snippet canónico CTA dark de suscripción al newsletter raíz. HTML exacto y canon en `robohogar/.claude/rules/newsletter.md § Snippet canónico · banner CTA suscripción al final de artículo (no-ficción)`. Aplicación automática en `/content-draft § 8.8 bis`.

Estructura fija del bloque (4 elementos, texto NO se varía por artículo):
- Título `¿Te ha servido este análisis?`
- Subtítulo `Cada semana, comparativas, reviews, editoriales y relatos.`
- Botón `Suscribirse` (infinitivo — distinto del de ficción que es `Suscribirme`)
- Trust-line `Newsletter gratis. Un email por semana. Cancela cuando quieras.`

Todo texto en `#FFFFFF` sobre fondo `#283642` + botón `#F5A623`. `href` apunta a `https://robohogar.com` **sin UTM** (regla `rules/newsletter.md § URL destino de CTAs de suscripción — SIEMPRE landing`). Excepción única que sí lleva UTM sigue siendo el banner Hoja de Compra.

**Posición canónica** en el esqueleto del borrador: después del bloque `¿Sabías que…?` + su `<div class="separator"></div>`, antes de `Más en ROBOHOGAR` (internal linking) + disclaimer. El CTA principal va antes del jumpoff a otros artículos — si el lector convierte, lo hace aquí; si no, los links de abajo siguen ofreciendo consumo.

**Formato en el borrador**: `<div class="snippet-block">` con HTML escapado dentro de `<pre><code>` — igual patrón que el banner Hoja de Compra. Razón: Rafael publica copy-paste del borrador al editor Beehiiv vía `/html` → Custom HTML block, que necesita el HTML como texto copiable, no renderizado.

**Ficciones Domésticas NO usan este CTA**. Tienen el suyo propio (`La próxima Ficción Doméstica, en tu correo` · botón `Suscribirme`), canonizado en `rules/newsletter.md § Snippet canónico · banner suscripción al final de ficción`.

**Why:** Rafael pidió 2026-04-22 un bloque de cierre fijo y reconocible de marca que convierta al final de cada artículo, después de entregar el "¿Sabías que?" (premio editorial). Antes no había CTA final estandarizado — unos artículos cerraban con "Más en ROBOHOGAR" y disclaimer, otros con tangible, inconsistente. Snippet fijo = señal de marca + CTA claro.

**How to apply:**
- Al generar cualquier borrador no-ficción con `/content-draft`, insertar el snippet-block canónico en la posición descrita. Usar HTML de `rules/newsletter.md` literal, sin reescribir el copy.
- Verificación pre-output: `grep -c "¿Te ha servido este análisis?" <borrador.html>` → debe ser 1 exacto. `grep -nE '¿Te ha servido[^<]*</div>.*utm_' <borrador.html>` → 0 (sin UTM). Orden en el HTML: Sabías → ¿Te ha servido → Más en ROBOHOGAR.
- Typo histórico: el borrador inicial que Rafael pegó decía `Suscríbirse` — corregido a `Suscribirse` al canonizar.
- Si Rafael pide cambiar pregunta/beneficio/botón, actualizar `rules/newsletter.md` (fuente de verdad) y notificar — nunca redactar variantes por artículo.
