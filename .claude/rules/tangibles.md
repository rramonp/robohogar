# Tangibles — principio editorial (pivote Cole 2026)

> **Estado actual (abr 2026):** el skill `/pdf-brand` NO existe todavía, pero el **principio editorial sí aplica desde ya**. Aunque los tangibles PDF formales (FASE 4C) se activen cerca de los 50 subs, el framing "tangible = producto" se puede aplicar a cada borrador con medios actuales (tablas inline, checklists de cierre, decision trees en markdown, bloques "Descarga" vacíos por ahora).

## Principio — tangible = producto, no bonus

**Pivote Cole 2026:** el lector no paga (ni se suscribe) por "explicaciones", paga por **algo concreto**. El artículo no es el producto con un tangible como regalo al final — el **tangible ES el producto** y el copy lleva hasta él. Nicolas Cole atribuye a este reframe el 90% del crecimiento de Write With AI.

### Cómo se aplica en `/content-draft`

1. **Antes de escribir el copy, definir el tangible entregable.** En `PASOS.md` del artículo, lista explícitamente qué tangible entrega el post: "checklist de 5 preguntas", "tabla comparativa 4 modelos", "decision tree mobile-first", "dossier 3-datos", etc.
2. **El copy se estructura para llevar al tangible.** El hook, el contexto y el desarrollo son la *subida* hacia el tangible. No al revés.
3. **Cliffhanger pattern:** el CTA (suscripción hoy, paywall en F3) va JUSTO antes de entregar el tangible. *"Aquí tienes la tabla con los 7 modelos y el que compramos nosotros → [email gate / paywall]"*.
4. **El tangible se versiona, nunca se sobreescribe** (regla heredada de [`feedback_never_overwrite_images.md`](../../../RRP-DEV/.claude/memory/feedback_never_overwrite_images.md)).

Fuente literal: [post Cole 2026](https://writewithai.substack.com/p/my-6-step-checklist-to-build-a-100000) y parseo adaptado a Beehiiv en [`references/writewithai/08-paid-newsletter-blueprint-2026.md`](../../references/writewithai/08-paid-newsletter-blueprint-2026.md).

## Mapeo — tipo de contenido → tangible entregable

Tabla operativa. El tangible se define ANTES que el copy.

| Tipo de contenido | Tangible (el producto real) | Formato entregable | Variante skill `/pdf-brand` (F4C) |
|---|---|---|---|
| Review | Checklist compra + specs 1-pager | Tabla inline + PDF descargable | `cheatsheet` |
| Comparativa | Tabla comparativa standalone con ganador marcado | Tabla responsive + PDF | `comparativa` |
| Editorial / Opinión | "3 datos clave" mini-dossier | Bloque destacado + PDF 1-pager | `cheatsheet` |
| Guía / How-to | Flowchart decisión o checklist paso a paso | Decision tree SVG + PDF | `guia` |
| Ficción Doméstica | Mini-poster (ilustración + quote + dato real) | Imagen + PDF high-res para imprimir | `relato` |
| Newsletter | Cheatsheet "Lo esencial en 3 minutos" | Bloque recuadrado + PDF | `cheatsheet` |
| Tutorial técnico | Guía step-by-step imprimible | Markdown + PDF | `guia` |

## Reglas operativas

- **Definir tangible ANTES del copy** en cada `PASOS.md` (obligatorio tras el pivote Cole 2026).
- **Cliffhanger pattern:** el copy entrega el tangible solo tras el CTA (email gate en F1-F2, paywall en F3).
- **Límite 30 min/tangible:** 4 "ok" > 2 "perfectos". Aplica cuando el skill `/pdf-brand` exista; mientras tanto, aplica al bloque inline.
- **Versionar, nunca sobrescribir** (memoria `feedback_never_overwrite_images.md`).
- **Mobile-first:** legible en 375px, fuente mínima 11pt.
- Voz y anti-patterns heredados de [`editorial.md`](editorial.md).

## Roadmap

- **F1 (hoy, 0-50 subs):** tangible definido en PASOS.md + entregado inline en el HTML del artículo. Sin PDF descargable aún.
- **~50 subs:** activar FASE 4C — construir skill `/pdf-brand` con los 4 variantes (cheatsheet, comparativa, guia, relato). Primeros 4-5 tangibles en PDF.
- **~100 subs:** ~15 tangibles acumulados + sección "Descargas" en landing robohogar.com.
- **~500 subs:** bundle temático + ebook recopilatorio de Ficciones Domésticas.
- **~5K subs (F3):** tangibles premium detrás de paywall en ROBOHOGAR+, paywall-at-cliffhanger pattern activo.

Plan completo: `../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md`. Operativa: `docs/guia-implementacion.md` § FASE 4C. Roadmap paid tier: `docs/plan-v2.md` §11 + [`08-paid-newsletter-blueprint-2026.md`](../../references/writewithai/08-paid-newsletter-blueprint-2026.md).
