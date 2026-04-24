---
name: Banner lead magnet ROBOHOGAR = variante Dark oficial
description: Banner Hoja de Compra en artículos usa variante DARK (#283642 + ámbar). Scope **solo robots de limpieza de suelos** (aspirador/fregasuelos/limpia-cristales). Excluido desde 2026-04-21: cortacésped (tangible aspirador-céntrico no encaja), mascota-robot, asistente-ia, humanoide, ficcion. Regla general: banner solo si el tangible responde al dolor concreto del lector. UTM obligatoria por artículo.
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
El banner de promoción del tangible "Hoja de Compra" (y cualquier futuro lead magnet de ROBOHOGAR) usa la **variante DARK** validada por Rafael 2026-04-18: fondo `#283642`, eyebrow ámbar `#F5A623` en mayúsculas, título DM Sans 22pt blanco, botón ámbar sólido. Mismo patrón que el bloque dark "Si te ha servido" del PDF backcover → consistencia PDF ↔ artículo reconocible.

**Why:** Rafael comparó dark vs light (callout crema + borde ámbar) el 2026-04-18 y eligió dark. Razones objetivas:

- Máximo contraste en el cuerpo del artículo → el ojo para ahí obligatoriamente.
- Reutiliza el patrón visual del PDF → el lector que descargó el PDF y vuelve al blog reconoce el componente.
- En fase 0-30 subs el CVR marginal importa más que el refinamiento tonal; dark gana por visibilidad.
- La variante light queda documentada para uso en artículos editoriales (no descartada, aparcada para fase ≥500 subs con A/B test).

**How to apply:**

**Template oficial:** [`content/templates/banner-lead-magnet.html`](../../../robohogar/content/templates/banner-lead-magnet.html).

**Snippets pre-personalizados por artículo:** [`content/templates/banner-lead-magnet-snippets.md`](../../../robohogar/content/templates/banner-lead-magnet-snippets.md). Cada snippet lleva UTM `?lm=hoja-compra&src=<slug>` ya sustituida.

**Scope (artículos donde va el banner) — actualizado 2026-04-21:**
- ✅ Aspirador, fregasuelos, limpia-cristales (robots de limpieza de suelos — las 10 preguntas del PDF responden a su dolor: m² piso, umbrales, pelo mascota, fregado/aspirado, ecosistema Matter).
- ✅ Reviews / comparativas / guías de compra de esas categorías.
- ❌ Cortacésped — **excluido 2026-04-21** tras rechazo de Rafael sobre `mejor-robot-cortacesped-2026`. Las 10 preguntas son aspirador-céntricas; el lector cortacésped pregunta otras cosas (pendiente jardín, cable perimetral sí/no, ruido vecindario, navegación LiDAR/satélite/cámara, distribución ES servicio técnico). Tangible específico "Hoja de Compra cortacésped" pendiente F2 (las 7 preguntas ya redactadas como checklist inline en `mejor-robot-cortacesped-2026`, reutilizable cuando se active el PDF).
- ❌ Mascota-robot (Aibo/Loona/LOOI) — excluido 2026-04-19. Intención ≠ aspirador.
- ❌ Asistentes IA de escritorio (Eilik, etc.) — excluido 2026-04-19.
- ❌ Humanoides domésticos — tangible propio "Guía early adopter humanoides" pendiente mes 3-4.
- ❌ Ficciones Domésticas — tangible propio pendiente ("Dossier Ficciones Domésticas"). No mezclar canales narrativos con CTA comercial.
- ❌ Editoriales/opinión sin ángulo de compra.

**Regla general (2026-04-21):** un banner solo se pega si el tangible al que apunta **responde las preguntas concretas del lector de ese artículo**. "Categoría consumer dentro de 500-1.500 €" NO es criterio suficiente — el contenido del PDF tiene que coincidir con el dolor concreto. Si no hay variante específica del tangible para la categoría → artículo **sin banner** hasta que la haya.

**Posiciones en el artículo:**
- Artículos largos (>1.500 palabras): **2 banners** — tras intro + tras veredicto.
- Artículos cortos (<800 palabras): **1 banner** al final.
- UTM distinto por posición no es necesario (con el `src=<slug>` basta para trazar qué artículo convierte; no queremos el detalle de "intro vs cierre" todavía).

**Automatización en skill `/content-draft`:**

El skill `.claude/commands/content-draft.md § 8.8` (añadido 2026-04-18) inserta el banner automáticamente en el borrador HTML para futuros artículos de categoría consumer, sustituyendo `<SRC_SLUG>` por el slug del frontmatter. Rafael solo tiene que pegar el snippet ya preparado en Beehiiv al publicar — no tiene que acordarse de incluirlo artículo a artículo.

**Artículos con banner activo (backfill 2026-04-18):**

| Slug | Categoría | Banner |
|---|---|---|
| mejor-robot-asistente-ia-2026 | Asistentes IA + mascotas | ✅ borderline (monitorear CVR) |
| roborock-saros-z70-review | Review aspirador | ✅ |
| samsung-jet-bot-steam-ultra-review | Review aspirador | ✅ |
| humanoides-en-casa-cuanto-falta | Editorial humanoides | ❌ |
| neo-humanoide-fabricas-eqt | Editorial humanoides | ❌ |
| humanoides-domesticos-2026-comparativa | Comparativa humanoides | ❌ |

**Guía operativa para activarlo:** [`docs/activar-tangible-hoja-compra.md`](../../../robohogar/docs/activar-tangible-hoja-compra.md) — checklist paso a paso de 6 pasos (subir digital product → double opt-in → automation welcome flow → pegar banners en 3 artículos → validación incógnito → monitoreo 2-3 semanas).

**Regla futura:** cuando se active un segundo tangible (ej. Glosario ROBOHOGAR), podrán coexistir 2 banners en el mismo artículo — uno por momento del funnel (investigando vs decidiendo). Requiere que cada banner lleve UTM distinta (`?lm=glosario&...` vs `?lm=hoja-compra&...`) y Automations de Beehiiv segmentadas por tag. Hasta entonces, 1 banner de Hoja de Compra por artículo.
