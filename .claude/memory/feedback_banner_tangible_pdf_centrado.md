---
name: Formato canónico centrado banner tangible PDF ROBOHOGAR
description: Banner dark para promoción de tangibles PDF usa text-align:center + estructura eyebrow·título·botón·trust-line (separada). Botón canónico "Enviádmelo al correo". Canon 2026-04-22.
type: feedback
originSessionId: 749cb54f-081c-4d7c-81a5-0a9108ab2b98
---
Todo banner de promoción de tangible PDF en artículo ROBOHOGAR usa el formato **dark centrado** canonizado 2026-04-22. Fuente de verdad HTML: `robohogar/content/templates/banner-lead-magnet.html`. Regla completa: `rules/tangibles.md § Snippet canónico — banner tangible PDF (formato centrado)`.

**Cambios respecto al formato anterior (2026-04-18 → 2026-04-22):**

- `text-align:center;` añadido al contenedor → todos los elementos centrados horizontalmente (eyebrow, título, botón, trust-line).
- Estructura: **eyebrow → título → botón → trust-line**. Desaparece el párrafo intermedio de beneficio (que antes mezclaba copy editorial + trust-line). La trust-line vive ahora como `<p>` separado DESPUÉS del botón, con color `rgba(255,255,255,0.65)` más apagado.
- Eyebrow describe el **formato del tangible**, no un genérico "Antes de comprar". Patrón: `<Tipo> · <N> <unidad> · <P> páginas`. Ejemplo: `Checklist · 10 preguntas · 2 páginas`.
- Título-beneficio específico del tangible para el artículo concreto, no copy genérico. Ejemplo aspirador: *"Las 10 preguntas clave antes de comprar un aspirador que te ahorran cientos de euros"*.
- Botón canónico: `Enviádmelo al correo` (antes `Descargar gratis →`). Describe el flow real: click → formulario email → PDF en la bandeja.
- Trust-line canónica se mantiene: `PDF gratis con tu suscripción semanal. Cancela cuando quieras.`
- Coherencia banner ↔ product page: el campo `Call-to-action copy` de la ficha Beehiiv Digital Product (`content/lead-magnets/<slug>/beehiiv-ficha.md`) pasa al mismo texto `Enviádmelo al correo` para que el lector no tenga disonancia entre el CTA del artículo y el botón del product page.

**Archivos canon actualizados 2026-04-22:**
- `content/templates/banner-lead-magnet.html` (template con placeholders `<EYEBROW>`, `<TITULO_BENEFICIO>`, `<SRC_SLUG>`, `<CTA_TEXTO>`, `<TRUST_LINE>`).
- `content/templates/banner-lead-magnet-snippets.md` (sección "Snippet canónico 2026-04-22").
- `content/lead-magnets/hoja-compra/snippets-para-pegar.md` (entrada #4 mejor-robot-aspirador-2026).
- `content/lead-magnets/hoja-compra/beehiiv-ficha.md` (CTA copy + tabla resumen).
- `content/articulos/mejor-robot-aspirador-2026/borrador.html` (2 banners intro + cierre).
- `content/published/2026-04-19-mejor-robot-aspirador-2026.html` (2 banners intro + cierre).
- `.claude/rules/tangibles.md` (nueva sección canónica).

**No actualizados** (formato anterior mantenido porque ya están publicados en Beehiiv, migrar solo si rebote lo justifica):
- Snippet Roborock Saros Z70 review en `banner-lead-magnet-snippets.md` y `snippets-para-pegar.md`.
- Snippet Samsung Jet Bot Steam Ultra review en los mismos archivos.
- Artículo desactivado `mejor-robot-asistente-ia-2026` (banner ya quitado de Beehiiv).

**Why:** Rafael 2026-04-22 tras probar visualmente el snippet en Beehiiv preview. El formato viejo con párrafo intermedio de beneficio rompía la jerarquía visual y el CTA quedaba alineado a la izquierda sobre un contenedor centrado en la columna de Beehiiv. El nuevo formato tiene jerarquía limpia: descriptor del tangible (eyebrow) → promesa (título) → acción (botón grande centrado) → cierre de confianza (trust-line apagada). Es el mismo flow visual que usan Substack y referentes ES en product pages.

**How to apply:**
- Al generar borrador nuevo con `/content-draft` en categorías dentro del scope (aspirador · fregasuelos · limpia-cristales para Hoja de Compra): insertar el banner con formato centrado nuevo, **no el viejo**. Copy por artículo sustituye placeholders según la tabla de `rules/tangibles.md`.
- Al crear tangible nuevo (Guía primer mes, Glosario, etc.): usar el mismo template, adaptar eyebrow (`Guía · N días · P páginas`) y título-beneficio. Botón y trust-line canónicos no se tocan.
- Verificación pre-output: grep en rules/tangibles.md § Snippet canónico (4 greps sobre el HTML del banner). Si `text-align:center` falta, o el botón no dice `Enviádmelo al correo`, o la trust-line no va después del botón → reescribir.
- Coherencia banner ↔ product page: cuando se crea una ficha Beehiiv Digital Product nueva, el campo `Call-to-action copy` debe ser `Enviádmelo al correo` por defecto. Si se cambia el CTA del banner por razón editorial, el CTA del product page se cambia en el mismo movimiento.
