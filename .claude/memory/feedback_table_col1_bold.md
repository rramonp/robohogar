---
name: ROBOHOGAR — tablas, columna 1 del body SÍ puede ir en bold
description: Excepción a "sin bold en tablas" — la col 1 del tbody (etiqueta de fila) va en <strong> para anclar escaneo móvil; thead y cols 2+ siguen en regular
type: feedback
originSessionId: b7cd7662-3738-46e0-8b2b-47e9a986d811
---
En tablas HTML de borradores ROBOHOGAR, la **columna 1 del `<tbody>`** (la etiqueta de fila — nombre de modelo, categoría, concepto) SÍ puede ir envuelta en `<strong>`. El `<thead>` y el resto de columnas siguen la regla general (sin bold).

**Why:** Rafael lo corrigió el 2026-04-18 tras aplicar la regla estricta "sin bold en tablas ni header ni body" del commit fbf6627. La columna 1 en una tabla es la *etiqueta* de la fila — funciona como un mini-heading lateral y el lector escanea por ahí en móvil. Quitarle el bold la convierte en texto plano que desaparece visualmente. El bold solo es ruido cuando aparece en *todas* las celdas o en el header (donde Beehiiv ya aplica peso).

**How to apply:**
- Al generar/editar tablas en `content/articulos/<slug>/borrador.html`: envolver `<td>` de la primera columna del body en `<strong>`. Resto de columnas, regular.
- Si la col 1 contiene año o anotación en `<em>`, el `<strong>` solo envuelve el nombre: `<td><strong>Samsung Steam Ultra</strong><br><em>(2026)</em></td>`.
- Aplica tanto a comparativas (el caso típico) como a cualquier tabla cuya col 1 sea la etiqueta de la fila.
- Ya recogido en `.claude/rules/editorial.md` § "Formato técnico (Beehiiv)" — si se edita la regla, mantener consistencia.

Precedentes en el repo: `content/articulos/humanoides-domesticos-2026-comparativa/borrador.html` y `content/articulos/samsung-jet-bot-steam-ultra-review/borrador.html` (ambos actualizados el 2026-04-18).
