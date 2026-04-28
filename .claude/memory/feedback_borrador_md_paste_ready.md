---
name: borrador.md paste-ready obligatorio en /content-draft
description: Todo artículo emitido por /content-draft entrega borrador.md paste-ready Markdown junto al borrador.html (canonizado 2026-04-26, reincidente 2026-04-28)
type: feedback
---

Regla dura establecida por Rafael 2026-04-26 (canonizada con `mejor-robot-aspirador-barato-2026`) y reforzada 2026-04-28 (incidente reincidente con `robot-cortacesped-rentabilidad-3-anos`).

**Regla:** todo artículo emitido por `/content-draft` entrega DOS archivos co-iguales en `content/articulos/<slug>/`:

1. `borrador.html` — preview con CSS ROBOHOGAR + 3 variantes hooks/veredicto/sabias visibles + snippets HTML escapados embebidos para revisión visual y pipeline `/post-publish`.
2. `borrador.md` — **paste-ready Markdown del cuerpo editorial para pegar en bloque al editor de Beehiiv**.

**Why:** Rafael publica en Beehiiv haciendo copy-paste. El editor de Beehiiv acepta Markdown nativo (H1, H2, párrafos, blockquotes, listas, tablas) en el área de cuerpo editorial, pero NO acepta los snippets HTML con estilos inline — esos van aparte vía `/html` → "Custom HTML block". El `borrador.html` mezcla las dos cosas (es preview), así que sin un `.md` limpio Rafael tiene que extraer manualmente la prosa, decidir variantes, eliminar snippets embebidos y convertir tags HTML a Markdown — trabajo que el skill puede emitir directamente y elimina ~20 minutos de fricción por artículo.

**How to apply:**

- En cada invocación de `/content-draft`, emitir el `borrador.md` junto al `borrador.html` en el mismo turno.
- Estructura canónica del `.md` documentada en `.claude/commands/content-draft.md § 5 bis`. Resumen:
  - H1 + subtítulo + byline al inicio
  - Hook elegido (recomendación IA v1) + intro callout como 2 blockquotes consecutivas
  - `🖼️ HERO` marcador + caption en cursiva
  - (Si aplica) `📋 Pega aquí Snippet N — Banner Hoja de Compra` (solo aspirador / fregasuelos / limpia-cristales)
  - H2 secciones con prosa Markdown puro
  - Tablas Markdown puro + (opcional) marcador para versión HTML estilizada
  - Veredicto elegido + ¿Sabías que? elegido (1 variante cada uno, no las 3)
  - `📋 Pega aquí Snippet N — CTA Suscripción final` (siempre)
  - Disclaimer en cursiva
- **Cero HTML en el `.md`.** Solo Markdown. Si un bloque requiere HTML (callouts, decision-cards), va como `📋 Pega aquí Snippet N` + opcionalmente la versión Markdown plana como fallback.
- **Variantes ya elegidas:** el `.md` lleva UNA versión de hook + UNA de veredicto + UNA de ¿sabías que? (la recomendada por la IA en el `.html`). Las 3 variantes solo viven en el `.html` para preview/selección. Si Rafael cambia de opinión, edita el `.md` antes de pegar.
- Verificación pre-output: existencia + 0 tags HTML + marcadores `📋 Pega aquí Snippet` y `🖼️ HERO` numerados en orden.

**Incidente origen 1 (canonización 2026-04-26):** Rafael creó manualmente el primer `borrador.md` paste-ready con `mejor-robot-aspirador-barato-2026` tras pedir la versión limpia. El skill `/content-draft` no lo emitía automáticamente; se asumió que se canonizaba para próximas invocaciones.

**Incidente origen 2 (reincidente 2026-04-28):** borrador #14 (`robot-cortacesped-rentabilidad-3-anos`) generado solo con `borrador.html` (sin `.md`). Rafael preguntó *"se te ha olvidado el .md o qué ha ocurrido?"*. Causa: el skill `.claude/commands/content-draft.md § 5 Output` mencionaba `.md` solo en el contexto del vault Obsidian, no en el repo. Solución: añadido `§ 5 bis` con estructura canónica + verificación pre-output + esta memoria + entrada en MEMORY.md.

**Aplicación retroactiva:** ninguna. Los artículos previos al canon 2026-04-26 (`mejor-robot-asistente-ia-2026` … `mejor-robot-aspirador-mascotas-2026`) se quedan sin `.md` (ya están publicados). Aplica desde `mejor-robot-aspirador-barato-2026` (que tiene `.md` manual) y `robot-cortacesped-rentabilidad-3-anos` (que recibe `.md` post-feedback). Próximas invocaciones de `/content-draft` lo emiten automáticamente.

**Patrón de referencia:** [`content/articulos/mejor-robot-aspirador-barato-2026/borrador.md`](../../content/articulos/mejor-robot-aspirador-barato-2026/borrador.md) (canonización) y [`content/articulos/robot-cortacesped-rentabilidad-3-anos/borrador.md`](../../content/articulos/robot-cortacesped-rentabilidad-3-anos/borrador.md) (post-incidente).
