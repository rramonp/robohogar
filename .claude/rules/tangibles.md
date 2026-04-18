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

## Mapeo — momento del funnel → tangible descargable

Arquitectura ampliada 2026-04-18 tras validación de Rafael sobre 3 formatos probados (checklists de pre-compra, "qué debes saber antes de…", guías prácticas de uso post-compra). Cada momento del funnel requiere un tangible distinto porque el dolor del lector es distinto.

| Momento funnel | Pregunta mental | Formato tangible | Ejemplo ROBOHOGAR | Skill |
|---|---|---|---|---|
| **Investigando** (aún no sabe qué quiere) | *"¿Esto vale la pena para mí?"* | "Qué debes saber antes de comprar un X — 7 mitos y realidades" (educacional narrativo, 2-3 pp) | "Qué debes saber antes de comprar un robot aspirador" | `cheatsheet` |
| **Decidiendo** (ya va a comprar, compara) | *"¿Cómo no equivocarme?"* | "Preguntas antes de comprar" / Hoja de Compra (checklist accionable 2 pp) | `content/lead-magnets/hoja-compra/` | `cheatsheet` |
| **Estrenando** (ya compró, está perdido primer mes) | *"¿Y ahora qué hago con esto?"* | "Guía primer mes / Guía práctica de uso" (step-by-step por días/semanas, 3-4 pp) | `content/lead-magnets/guia-primer-mes-aspirador/` | `guia` |
| **Optimizando** (usuario medio, quiere sacarle más) | *"¿Lo estoy usando bien?"* | "20 trucos avanzados / cómo exprimir tu X" (tips + atajos, 2-3 pp) | Futuro, mes 6+ | `cheatsheet` |

**Estrategia multi-tangible en un mismo artículo** (viable en Beehiiv Scale): un artículo puede tener 3 banners distintos, uno por momento del funnel, cada uno con UTM propia → automation distinta → welcome flow diferenciado. Posiciones recomendadas:
- Tras intro: CTA al tangible "investigando".
- Mid-article (tras criterios): CTA al tangible "decidiendo".
- Al final (tras veredicto): CTA al tangible "estrenando".

El lector se autoclasifica según su momento real. Ventaja: captura 3 segmentos distintos del mismo tráfico SEO vs el listicle que solo captura al que está "decidiendo".

**Ventaja defensiva del formato "Estrenando" (onboarding post-compra):** los listicles "mejores X" saturan el top de Google, pero las guías de onboarding post-compra en español son raras. Quien las escribe bien captura la audiencia más leal — el que ya gastó 500-1.500 € y está frustrado. Si le salvas el mes 1, se suscribe de por vida.

## Reglas operativas

- **Ninguna promesa futura ni byline personal dentro del PDF tangible.** Tres prohibiciones duras validadas por Rafael 2026-04-18:
  1. **No listar próximos tangibles** ni roadmap ("Próximos tangibles para suscriptores: Glosario, Calendario, Guía de humanoides…" ❌). Crea compromiso público incómodo y diluye el valor del que el lector tiene delante.
  2. **No prometer fechas de revisión** ("Actualizamos cada 6 meses", "Próxima revisión octubre 2026", "Los suscriptores reciben la v2, v3 automáticamente" ❌). No hay contrato de cadencia con el lector.
  3. **No byline personal** ("Rafael de ROBOHOGAR" ❌). La firma del PDF es solo `ROBOHOGAR` + icon robot como firma visual. El PDF es documento editorial del medio, no artículo de opinión. Excepción: artículos Beehiiv SÍ admiten byline (regla editorial.md).
  
  Sustituir el clásico bloque "Actualización viva" por un **bloque de invitación a compartir** (mismo impacto visual, cero compromiso): eyebrow *"SI TE HA SERVIDO"* · título *"Reenvía esta guía a quien esté mirando robots"* · subtítulo *"No hace falta permiso. Lo único que pedimos es que le sirva al siguiente."*. Verificación pre-export: `grep -E "Próximos tangibles|Próxima revisión|actualizamos cada|vamos expandiendo|Rafael de ROBOHOGAR"` en HTML+markdown del tangible — si matchea, reescribir. Ver memoria `feedback_tangible_no_promises_no_byline.md`.
- **Definir tangible ANTES del copy** en cada `PASOS.md` (obligatorio tras el pivote Cole 2026).
- **Checklist accionable como tangible mínimo obligatorio.** Todo artículo ROBOHOGAR (review, comparativa, guía, editorial, tutorial, newsletter) incluye al menos una checklist de 3-7 ítems accionables y concretos antes del veredicto/cierre. Es el tangible más rentable: 5-7 líneas, 10 min de trabajo, máximo valor percibido. Si el tema no admite checklist natural, sustituir por decision tree mini (4-6 bifurcaciones), dossier "3 datos clave" o cuadro "qué hacer / qué no hacer". Nunca cerrar un artículo sin un bloque accionable etiquetado visualmente (callout crema `#FFF9EF` + borde `#F5A623`). H2 del bloque empieza con la palabra `Checklist —` (ej: "Checklist — 5 preguntas antes de comprar") para que el lector lo reconozca como producto. Regla validada por Rafael 2026-04-18 tras ver que la checklist de `samsung-jet-bot-steam-ultra-review` § "5 cosas antes de comprar" funcionaba como producto real independiente de la comparativa.
- **Promocionar el tangible en subtítulo + meta description.** El subtítulo del artículo (lo que aparece bajo el H1 y se replica en la OG card / landing thumbnail) y la `meta_description` deben mencionar el tangible con cifra o promesa concreta. Fórmula: `<qué entrega el artículo> + <tangible con número>`. Razón: la OG card es el primer contacto del lector — si el subtítulo dice solo "la guía honesta", compite peor con otros titulares. Si dice "checklist de 5 preguntas que te ahorra 600 €", compite mejor. Ejemplos:
  - ✅ "6 robots aspirador por perfil y una checklist de 5 preguntas que te ahorra 600 € antes de comprar"
  - ✅ "Review del Samsung Steam Ultra + checklist de 5 cosas que verificar en cualquier aspirador con vapor"
  - ❌ "La guía honesta, sin hype" (sin cifra, sin tangible concreto — OG card débil)
- **Cliffhanger pattern:** el copy entrega el tangible solo tras el CTA (email gate en F1-F2, paywall en F3). En F1 (0-50 subs hoy): tangible inline sin gate, ver `feedback_gate_respects_phase.md`.
- **Límite 30 min/tangible:** 4 "ok" > 2 "perfectos". Con el skill `/pdf-brand cheatsheet` activo desde 2026-04-18, generar un PDF desde un `data.py` válido tarda <5 min de compute; la iteración de copy + CSS minor ajustes cabe dentro del límite. Aplica igual al bloque inline del artículo.
- **Generación de tangibles: skill `/pdf-brand cheatsheet` (plan Scale disponible).** Invocación desde Claude: `/pdf-brand cheatsheet <slug> [version]`. Código: `skills/pdf_brand/` · command: `.claude/commands/pdf-brand.md` · template: `templates/cheatsheet.html.jinja2` (destilado del v2 validado de Hoja de Compra). El validator pre-export (`validators.py`) bloquea automáticamente los PDFs que contengan las 3 prohibiciones de arriba — sin bypass.
- **Promoción del tangible en artículos: banner Dark oficial.** Cada artículo de categoría consumer (aspirador · cortacésped · mascota-robot · fregasuelos · limpia-cristales) incluye el banner de [`content/templates/banner-lead-magnet.html`](../../content/templates/banner-lead-magnet.html) en **2 posiciones** (tras intro + tras veredicto, en artículos >1.500 palabras; solo final en <800 palabras). Exclusiones: humanoides, ficciones y editoriales sin ángulo de compra. UTM obligatoria `?lm=hoja-compra&src=<slug-artículo>` para tracking por fuente en Beehiiv Automations. Snippets pre-personalizados listos para copy-paste en [`content/templates/banner-lead-magnet-snippets.md`](../../content/templates/banner-lead-magnet-snippets.md). El skill `/content-draft` inserta el banner automáticamente en el borrador HTML para futuros artículos consumer (ver `.claude/commands/content-draft.md § 8.8`). Regla activa desde 2026-04-18 validada por Rafael tras elegir variante Dark.
- **Ficha Beehiiv Digital Product obligatoria por tangible.** Todo tangible PDF tiene además una `beehiiv-ficha.md` en `content/lead-magnets/<slug>/` con los 10 campos del Digital Product de Beehiiv pre-rellenados. Template canónico: [`content/templates/beehiiv-digital-product-template.md`](../../content/templates/beehiiv-digital-product-template.md) — incluye Product name, Description, **Product details** (rich text en 6 bloques: Qué es · Qué cubre · Para quién es · Para quién no es · Qué incluye · Qué pasa al descargarlo), Call-to-action copy, Post-purchase redirect, Survey, Product page URL, Send review request emails, Images. Defaults fijos para F1-F2 (0-500 subs): CTA `Descargar gratis` · redirect vacío · survey OFF · review emails **OFF** · image primary = portada PDF 1280×720. El skill `/pdf-brand cheatsheet` genera esta ficha automáticamente junto al PDF (ver `.claude/commands/pdf-brand.md § 6`). La ficha pasa por los mismos validators que el PDF (sin roadmap, sin fechas, sin byline, voz plural, anti-IA §1). Regla activa desde 2026-04-18.
- **Versionar, nunca sobrescribir** (memoria `feedback_never_overwrite_images.md`).
- **Mobile-first:** legible en 375px, fuente mínima 11pt.
- Voz y anti-patterns heredados de [`editorial.md`](editorial.md).

## Roadmap

- **F1 (hoy, 0-50 subs):** tangible definido en PASOS.md + entregado inline en el HTML del artículo. PDFs descargables activos vía `/pdf-brand cheatsheet` (adelantado desde 2026-04-18 al tener plan Scale y primer PDF Hoja de Compra v2 validado).
- **~50 subs:** expandir skill a las 3 variantes restantes (comparativa, guia, relato) según demanda. Primeros 4-5 tangibles en PDF activos en landing.
- **~100 subs:** ~15 tangibles acumulados + sección "Descargas" en landing robohogar.com.
- **~500 subs:** bundle temático + ebook recopilatorio de Ficciones Domésticas.
- **~5K subs (F3):** tangibles premium detrás de paywall en ROBOHOGAR+, paywall-at-cliffhanger pattern activo.

Plan completo: `../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md`. Operativa: `docs/guia-implementacion.md` § FASE 4C. Roadmap paid tier: `docs/plan-v2.md` §11 + [`08-paid-newsletter-blueprint-2026.md`](../../references/writewithai/08-paid-newsletter-blueprint-2026.md).
