---
name: ROBOHOGAR content gate respects subscriber phase (F1 = no gate)
description: No proponer ni implementar content gate en ROBOHOGAR mientras suscriptores <50 (F1). Paywall-at-cliffhanger se activa solo en F3 (~5K subs).
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
En ROBOHOGAR no se activa content gate (ni paywall) en artículos mientras los suscriptores estén en fase F1 (0-50 subs), aunque el usuario lo pida como experimento. El tangible va inline siempre.

**Why:** Rafael lo validó el 2026-04-18 en el borrador de `mejor-robot-aspirador-2026`. Se diseñó con gate antes de la tabla comparativa por solicitud inicial suya; al revisarlo él mismo vio la inconsistencia y preguntó dónde encajaba. Tres razones objetivas sostienen la regla:

1. **Regla del repo:** `@.claude/rules/tangibles.md` § Roadmap prescribe **F1 (0-50 subs): tangible inline sin PDF ni gate**. Gate/paywall entra en F3 (~5K subs). Paywall-at-cliffhanger pattern documentado en `@references/writewithai/08-paid-newsletter-blueprint-2026.md` como feature F3.
2. **SEO evergreen:** en pre-audiencia (0-30 subs hoy), Google/Bing son el único canal de crecimiento. Gatear contenido puede reducir indexación y tiempo en página de visitantes orgánicos — justo el tráfico que tiene que convertirse en suscriptores.
3. **Debilidad estructural del cliffhanger en guías simplificadas:** Rafael fuerza tablas mobile-first ≤4 cols y celdas <25 chars (`@rules/editorial.md § Formato técnico`). Una tabla simplificada al final del artículo no tiene peso suficiente para justificar gate — cuando el lector llega, ya ha recorrido 6 secciones de modelo y tiene criterio. Gatear tabla o veredicto solo añade fricción.

**How to apply:**
- Si Rafael pide "añadir gate/paywall/content gate" a un artículo mientras subs <50, la respuesta por defecto es proponer **diferir a F3** y documentar la razón en PASOS.md con referencia a `@rules/tangibles.md` F1 + `@references/writewithai/08-paid-newsletter-blueprint-2026.md` F3.
- Si Rafael insiste en experimentar con gate en F1, hacerlo solo en un **artículo nuevo con tangible genuinamente denso** (benchmark propio, ebook, comparativa ≥10 modelos con datos exclusivos) — no forzarlo en guías de compra estándar que ya entregan todo el valor en el cuerpo libre.
- Cuando los subs crucen ~50, activar **FASE 4C** (skill `/pdf-brand` para tangibles PDF descargables, aún con opt-in email sin gate). Gate sistémico solo a partir de ~5K subs según el roadmap `@docs/plan-v2.md` § 11.
- **Regla de no-repetición:** si ya se descartó gate en un artículo concreto, el PASOS.md debe dejar documentado el descarte y la fecha de retoma. No re-abrir el debate por pereza editorial — releer el § 4B antes de proponer.
