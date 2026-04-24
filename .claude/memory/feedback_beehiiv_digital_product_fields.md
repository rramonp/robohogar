---
name: Ficha Beehiiv Digital Product obligatoria por tangible + defaults fijos F1-F2
description: Todo tangible ROBOHOGAR genera además una beehiiv-ficha.md con 10 campos Beehiiv y 4 defaults fijos (CTA, redirect, survey, review emails) para pase directo al dashboard.
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
Todo tangible ROBOHOGAR (cada lead magnet PDF en `content/lead-magnets/<slug>/`) DEBE tener además una ficha `beehiiv-ficha.md` en el mismo directorio con los 10 campos de configuración del Digital Product de Beehiiv pre-rellenados. El objetivo: Rafael solo hace copy-paste al dashboard, sin pensar defaults por cada tangible.

**Why:** Rafael lo estableció el 2026-04-18 durante el setup en Beehiiv del primer Digital Product (Hoja de Compra). Observación literal: *"actualizar el pipeline para contenido digital y tangibles futuros, poniendo que también se tienen que rellenar estos campos que me acabas de dar y también el campo de Product Details"*. Contexto: durante el setup se encontró con 6 campos adicionales al "Name / Description / File" básicos (CTA copy, post-purchase redirect, survey, Product page URL, review emails toggle, images) y el Product details rich-text. Cada uno requería pensar un default. Sistematizar evita repetir la decisión 5 veces.

**Defaults fijos en fase F1-F2 (0-500 subs):**

| Campo | Default | Razón |
|---|---|---|
| Call-to-action copy | `Descargar gratis` | Match exacto con el botón del banner del artículo (coherencia canal a canal). |
| Post-purchase redirect | (vacío) | Thank-you default Beehiiv cumple; crear landing custom requiere 30-45 min sin ROI claro. Activar en ≥100 descargas. |
| Survey | `No survey` | Feedback cualitativo se captura via reply al Email 1 del welcome flow (mejor señal Gmail + research real). Survey añade fricción. |
| Send review request emails | ❌ **OFF** | Pedir review a primeros 5-10 subs es cringe y rompe la voz editorial. Además reviews placeholder de Beehiiv pueden confundir. Activar en ≥100 descargas reales. |

**Campos variables por tangible (Claude extrae de `data.py` del skill `/pdf-brand`):**

- **Product name:** `title_big + title_small + " · " + descriptor-corto` del data.py.
- **Description:** `subtitle` del data.py (≤200 chars).
- **Product details** (rich text): 6 bloques obligatorios con bold en encabezados → Qué es · Qué cubre · Para quién es · Para quién no es · Qué incluye · Qué pasa al descargarlo. Construido desde `descriptor + intro_paragraphs + items (como lista resumida) + welcome flow info`.
- **Product page URL:** slug corto 2-4 palabras (Claude sugiere, Rafael valida al subir). No usar el slug interno largo.
- **Images:** Primary = portada PDF recortada a 1280×720. Secondary opcional.

**How to apply:**

1. **Template canónico:** [`content/templates/beehiiv-digital-product-template.md`](../../../robohogar/content/templates/beehiiv-digital-product-template.md) — estructura completa + razones de cada default + ejemplo aplicado.
2. **Ficha concreta por tangible:** cada `content/lead-magnets/<slug>/beehiiv-ficha.md` usa el template. Primer precedente: `content/lead-magnets/hoja-compra/beehiiv-ficha.md` (2026-04-18).
3. **Generación automática por `/pdf-brand`:** el skill genera `beehiiv-ficha.md` junto al PDF desde `data.py`. Los 4 defaults fijos se aplican sin preguntar; los campos variables se extraen del data. Documentado en `.claude/commands/pdf-brand.md § 6`.
4. **Validators aplicables:** la ficha pasa por los mismos checks que el PDF (sin roadmap de próximos tangibles, sin fechas de revisión, sin byline "Rafael de ROBOHOGAR", voz plural, anti-IA §1). Si el Product details viola alguna regla → reescribir antes de entregar.
5. **Regla sistémica:** [`rules/tangibles.md`](../../../robohogar/.claude/rules/tangibles.md) § Reglas operativas tiene entry específico "Ficha Beehiiv Digital Product obligatoria por tangible" que cubre los 10 campos + los 4 defaults fijos.

**Product details — estructura de los 6 bloques obligatorios:**

1. **Qué es** — 1-2 frases que definen el tangible + formato (ej. PDF 2 páginas, PDF ilustrado, etc.).
2. **Qué cubre** — scope concreto de categorías/temas incluidos + exclusiones declaradas ("quedan fuera: humanoides, ficciones…").
3. **Para quién es** — 3 bullets describiendo perfiles de lector objetivo.
4. **Para quién no es** — 2 bullets honestos con cuándo NO aplica el tangible.
5. **Qué incluye** — lista con las secciones/preguntas/contenidos del tangible (~10 líneas).
6. **Qué pasa al descargarlo** — flow exacto (doble opt-in → PDF email 1 + reply request → email 2 con 2 artículos + cadencia semanal martes 9:00).

**Cuándo cambiar los defaults (fase F3, ~5K+ subs):**

- Post-purchase redirect → página custom en robohogar.com con CTA a otro tangible o artículo.
- Survey → 1-2 preguntas cualitativas para refinar backlog editorial.
- Send review request emails → ON (con N≥100 descargas orgánicas).

Precedente: todos los cambios de default se anotan aquí al subir la primera ficha con valores nuevos.
