---
name: ROBOHOGAR — Cero referencias fantasma en el cuerpo del artículo
description: Nunca prometer/referenciar tabla, gráfico, bloque, dato, imagen o sección que no exista literalmente en el artículo entregado. Integridad editorial > copy atractivo.
type: feedback
originSessionId: 5636afe5-eaaa-4e44-a929-38053b0dd3cd
---
## Regla

En todo contenido publicable de ROBOHOGAR (artículo, review, comparativa, editorial, guía, newsletter, ficción), **cada referencia interna a otra parte del mismo artículo debe corresponder a algo que existe literalmente en el artículo**. Si el subtítulo dice "la tabla de abajo", debe haber una tabla abajo. Si un callout dice "hay que leer lo mismo desde otra tabla", esa otra tabla tiene que estar en el mismo post. Si el cuerpo promete "la checklist que cierra este artículo", la checklist tiene que existir al cierre.

**Prohibido específicamente:**
- "La noticia real está una tabla de [X] abajo" · "hay que leer lo mismo desde otra tabla" → si no hay tabla
- "como verás en el gráfico de [X]" → si no hay gráfico
- "la infografía/diagrama más adelante" → si no se inserta ninguno
- "el análisis completo abajo" → si el artículo no tiene un análisis subsecuente claro bajo ese título
- Referencias cruzadas a artículos ROBOHOGAR que aún no están publicados (pueden ir al final en "Más en ROBOHOGAR" **solo si la URL existe y está en `registro-articulos.md`**)
- Datos concretos que no están citados con fuente verificable en `references/fuentes-por-categoria.md`

**Why:** es el tipo de error que rompe la confianza editorial de un solo golpe. El lector promete tiempo al leer; si el artículo le promete una tabla y no la encuentra, percibe aggregator / relleno / LLM-generated. En un newsletter con voz personal como ROBOHOGAR, el coste es desproporcionado al ahorro de escribir rápido. Incidente origen: artículo #8 *"Humanoide bate récord media maratón"* (2026-04-20) — el subtítulo y un callout callout-amber prometían "la tabla del AI Index Report 2026 de Stanford abajo" pero el artículo solo citaba el informe en prosa + un gráfico Behavior-1K; no había tabla ninguna. Rafael tuvo que reescribir el subtítulo y eliminar el callout entero tras publicar.

**How to apply:**

1. **Regla activa en `content-draft.md § 8.4 bis`:** antes de entregar el borrador.html, escanear el documento y verificar que cada promesa de "abajo / arriba / más adelante / al final / a continuación" tiene un referente real (`<table>`, `<img>`, sección con H2 correspondiente, bloque checklist, etc.). Si aparece ≥1 fantasma → rechazar output y reescribir.
2. **Regla activa en `post-publish.md § 1` con triaje evidente/ambiguo (ajuste 2026-04-20):** contrastar el artículo publicado contra referencias fantasma antes de committear a `content/published/`.
   - **Fantasma evidente + fix obvio** (≤1 frase tocada, sentido gramatical preservado, tesis intacta — p.ej. quitar "la tabla de abajo —" del subtítulo cuando no hay tabla; borrar un link cuyo destino no existe en `registro-articulos.md`; sustituir fuente mal citada por la del cuerpo) → **arreglar directamente** en `borrador.html` + `content/published/YYYY-MM-DD-<slug>.html` y reportar el fix aplicado en el resumen final. Rafael valida vía diff del commit. NO preguntar.
   - **Fantasma ambiguo** (reescritura >1 frase, estructura del bloque afectada, o dato sin fuente que podría ser correcto pero sin referencia en el cuerpo) → PARAR y avisar con lista + propuesta de fix por cada una. Rafael decide.
3. **Grep canónico:** `grep -nE "(tabla|gráfico|infografía|diagrama|imagen|sección|checklist|cuadro|bloque) (de abajo|abajo|arriba|que (te mostramos|verás|ves)|a continuación|más adelante|al final|al principio|al cierre)" borrador.html` — cualquier match revisar manualmente que el referente existe.
4. **Si se detecta una referencia fantasma:** reescribir la frase que la contiene (no eliminar el bloque entero si la frase es recuperable), o eliminar la promesa y dejar solo la prosa informativa.

**Ejemplos canónicos (para ilustrar el triaje):**

| Fantasma | Categoría | Acción |
|---|---|---|
| Subtítulo: *"…la **tabla de Stanford abajo**…"* cuando no hay tabla | Evidente | Auto-fix: quitar el sub-fragmento del em-dash. Reportar. |
| Callout: *"hay que leer lo mismo desde **otra tabla del AI Index Report**"* cuando no hay tabla | Evidente (bloque entero promete algo inexistente) | Auto-fix: eliminar el callout si solo promete la tabla + reporte. Si el callout tiene más contenido útil, auto-fix de la frase promesa + mantener el resto. |
| *"Lee nuestra **guía de cortacéspedes** [link]"* con URL que no está en `registro-articulos.md` | Evidente | Auto-fix: eliminar el link manteniendo el texto descriptivo, o eliminar el sub-fragmento entero si queda raro. Reportar. |
| *"Según **Gartner**, el 25%…"* cuando el cuerpo cita Stanford con ese 25% | Evidente | Auto-fix: sustituir "Gartner" por "Stanford" + reporte. |
| Un párrafo de 3 frases construido sobre *"como verás en la tabla"* (la tabla no existe) | Ambiguo (reescribir afecta al argumento) | Consultar: mostrar el párrafo + propuesta de reescritura sin la promesa. |
| Cifra *"los humanoides supervisan 47% de…"* sin fuente citada en el cuerpo | Ambiguo (podría ser cifra real sin cita) | Consultar: preguntar origen de la cifra antes de borrarla o citarla. |

## Extensión — fuentes y datos (regla hermana 2026-04-20)

Aplica la misma lógica a datos citados: si el artículo dice "según Stanford, 12%", debe existir cita con link en el cuerpo o un `figure-caption` que lo ancle. Si el dato no está verificado en `references/fuentes-por-categoria.md` para esa categoría, añadirlo o descartar el dato.

**Ampliación 2026-04-20 tras auditoría de los 8 primeros artículos ROBOHOGAR** (14 claims sin fuente detectados — Samsung NaviBot 2003 posiblemente erróneo, Tesla 20.000M sin cita, 99,99% bacterias sin link, "el único compañero inteligente" exagerado, etc.):

Creada regla hermana **`@rules/editorial.md § Datos con fuente rastreable`** con taxonomía de 9 categorías que obligan link/cita o framing explícito:
1. Cifras de ventas/unidades · 2. Ratings/valoraciones (plataforma explícita) · 3. Eficacia/estadísticas · 4. Inversión/financiación · 5. Proyecciones de mercado · 6. Fechas regulatorias · 7. Datos históricos · 8. Tests del fabricante (cualificar siempre como claim) · 9. "Único/primero/mejor jamás".

Pipeline extendido con 3 greps pre-output (cifras sin href, "únic/primer/jamás", "tests internos/según la marca") aplicados en `/content-draft § 8.4 ter` y `/post-publish § 1` con mismo triaje auto-fix/consultar. Corpus empírico canónico: [`references/audit-2026-04-20-unsourced-claims.md`](../../robohogar/references/audit-2026-04-20-unsourced-claims.md).

## Integración con skills existentes

- `content-draft.md` hereda esta regla vía referencia (paso pre-output).
- `ficcion-draft.md` aplica solo parcialmente: en ficción la prosa puede insinuar elementos fuera de escena (Chekhov), pero NO debe prometer al lector secciones del relato que no existen. Los datos anclados (dato-real) sí tienen que existir y ser verificables.
- `post-publish.md` paso 1 (verificación): grep de referencias fantasma contra el HTML publicado.
- Memoria `feedback_article_voice_authority.md` es complementaria (cómo se citan las fuentes externas). Esta cubre las referencias *internas* al mismo artículo.
