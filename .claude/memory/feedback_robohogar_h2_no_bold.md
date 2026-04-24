---
name: ROBOHOGAR — Formato técnico Beehiiv (tipografía, negritas, tablas)
description: Config tipográfica global de Beehiiv (DM Sans Bold headings, Inter Regular body), política de negritas (NO en headings/tablas/checklist) y regla de tablas mobile-first (máx 4 cols, cells ≤25 chars).
type: feedback
originSessionId: 01b876ab-8a57-41a4-b71a-67ab8bf11ed1
---

## Config global de Beehiiv (ROBOHOGAR)

- **Headings (H1/H2/H3):** DM Sans, **Bold** (aplicado como global setting en Beehiiv)
- **Body / párrafo:** Inter, Regular
- Esta config vive en Beehiiv admin, no en los borradores. Los borradores producen Markdown/HTML semántico plano y Beehiiv aplica el estilo al renderizar.

## Política de negritas — DÓNDE SÍ / DÓNDE NO

**SÍ negritas (permitidas y recomendadas cuando aportan énfasis):**
- Dentro de párrafos de texto corrido (cualquier tipo de párrafo: intro, desarrollo, callout simple, nota al pie, etc.)
- Bullets/listas de prosa dentro de párrafos

**NO negritas (nunca, aunque la fuente lo permita):**
- Headings H1, H2 y H3 — Beehiiv ya aplica DM Sans Bold global; añadir bold inline sobrescribe/duplica el estilo y rompe la consistencia
- Tablas — celdas ni de header ni de body llevan bold
- Recuadros tipo checklist (callout box con fondo crema/naranja, ej. clase `.checklist` con `background: #FFF9EF; border: 1px solid #F5A623;` como el del artículo Samsung Jet Bot Steam Ultra) — los items del checklist van en peso regular, sin `<strong>` ni `**...**`

**Why:** limpieza visual y consistencia entre artículos. Bold en headings rompe el global setting; bold en tablas y checklists satura elementos que ya destacan por caja/borde/fondo propio.

**How to apply:**
- Markdown: `## Título` nunca `## **Título**`; `| celda |` nunca `| **celda** |`; items de checklist en plano, no con `**...**`
- HTML: `<h2>Título</h2>` nunca `<h2><strong>...</strong></h2>`; `<td>celda</td>` nunca `<td><strong>...</strong></td>`; dentro de `<div class="checklist">` los `<li>` van sin `<strong>`
- Revisar también contenido copiado desde fuentes externas (suele traer bold embebido)
- Si un borrador existente viola la regla, limpiarlo antes de publicar

## Tablas — mobile-first (≥50% lectores en móvil)

- **Máximo 4 columnas.** Si una comparativa pide más: (a) recortar a las 4 más críticas y el resto en prosa, o (b) partir en 2 tablas temáticas.
- **Texto corto por celda (≤25 chars orientativo).** Sin paréntesis largos, sin disclaimers en celda (eso al caption o al cuerpo).
- **Nombres de producto cortos:** marca + modelo en 2-3 palabras ("Ecovacs X8 Pro Omni", no "Ecovacs Deebot X8 Pro Omni").
- **Unidades pegadas sin espacio:** "100°C", "1.399€" (ayuda a evitar wrap feo en 375px).
- **Referencia que renderiza bien:** tabla de `content/articulos/mejor-robot-asistente-ia-2026/borrador.html` (4 cols).
- **Fallo real documentado:** tabla original de `content/articulos/samsung-jet-bot-steam-ultra-review/borrador.html` tenía 7 columnas con cells largas → ilegible en 375px (abril 2026). Corregida a 4 cols.

## Nota de consistencia

`.claude/rules/design.md` menciona Jost + DM Sans como "fuentes de referencia para assets propios". Eso aplica a diseño de assets (landing, social cards, PDFs). El newsletter/web en Beehiiv usa la config de arriba — son stacks distintos y compatibles.
