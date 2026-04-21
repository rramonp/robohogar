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
- **Promoción del tangible en artículos: banner Dark oficial.** Scope **estricto** del banner Hoja de Compra (tangible decidiendo-compra de **robots de limpieza de suelos**): categorías donde las 10 preguntas del PDF (m² del piso, umbrales, mascotas de pelo, fregado vs aspirado, ecosistema Matter/SmartThings) responden al dolor concreto del lector — `aspirador · fregasuelos · limpia-cristales`. Banner en **2 posiciones** (tras intro + tras veredicto) si >1.500 palabras; solo final si <800.
  - **Exclusiones totales** (NO banner Hoja de Compra): `humanoide` · `mascota-robot` · `asistente-ia-escritorio` · **`cortacésped`** · `ficcion` · `editorial-sin-angulo-compra`.
  - **Por qué excluir cortacésped** (ajuste 2026-04-21 tras rechazo de Rafael sobre `mejor-robot-cortacesped-2026`): las 10 preguntas de la Hoja de Compra son aspirador-céntricas. Nada de eso aplica a cortacésped (donde las preguntas reales son: pendiente del jardín, cable perimetral sí/no, ruido por horarios de vecindario, navegación LiDAR/satélite/cámara, distribución ES del servicio técnico, m² de césped, cobertura de árboles). Promocionar Hoja de Compra en artículo cortacésped → lector descarga PDF que no responde a su pregunta → decepción + baja en welcome → ensucia el funnel. Esperar tangible específico "Hoja de Compra cortacésped — 7 preguntas antes de comprar" (pendiente F2, las 7 preguntas ya redactadas inline en `mejor-robot-cortacesped-2026` como checklist accionable reutilizable cuando se active el PDF).
  - **Por qué excluir mascota-robot / asistente-ia** (2026-04-19 tras rechazo de Rafael sobre `mejor-robot-asistente-ia-2026`): el tangible responde a preguntas de aspirador (succión, fregado, estación, LiDAR, precio/m²) que NO aplican al lector de Loona/LOOI/Eilik. Promocionar Hoja de Compra en esos artículos → suscriptor incorrecto → churn en welcome + riesgo spam report → ensucia el funnel. Esperar tangible específico "Guía del asistente IA de escritorio" / "Mascota-robot: qué esperar y qué no" (pendiente F2).
  - **Por qué excluir humanoides**: mismo razonamiento pero más obvio (intención y precio 15-50K € vs 500-1.500 €). Tangible específico "Guía del early adopter de humanoides" pendiente mes 3-4.
  - **Regla general (2026-04-21):** un banner solo se pega a un artículo si el tangible al que apunta **responde las preguntas concretas que el lector de ese artículo tiene en la cabeza**. "Categoría consumer dentro de 500-1.500 €" NO es criterio suficiente — el contenido del PDF tiene que coincidir con el dolor concreto del lector. Si no hay variante específica del tangible para la categoría, el artículo va **sin banner** hasta que la haya.
  - UTM obligatoria estándar Beehiiv: `?utm_source=<slug-artículo>&utm_medium=banner&utm_campaign=hoja-compra`. Snippets pre-personalizados en [`content/lead-magnets/hoja-compra/snippets-para-pegar.md`](../../content/lead-magnets/hoja-compra/snippets-para-pegar.md) (Snippet 1 marcado como DESACTIVADO).
  - El skill `/content-draft` inserta el banner automáticamente en el borrador HTML para artículos dentro del scope; para categorías excluidas, omite el banner sin preguntar (ver `.claude/commands/content-draft.md § 8.8`).
  - Regla activa desde 2026-04-18; scope ajustado 2026-04-19 (fuera mascota-robot y asistente-ia); ajustado 2026-04-21 (fuera cortacésped + regla general "tangible debe responder el dolor concreto").
- **Ficha Beehiiv Digital Product obligatoria por tangible.** Todo tangible PDF tiene además una `beehiiv-ficha.md` en `content/lead-magnets/<slug>/` con los 10 campos del Digital Product de Beehiiv pre-rellenados. Template canónico: [`content/templates/beehiiv-digital-product-template.md`](../../content/templates/beehiiv-digital-product-template.md) — incluye Product name, Description, **Product details** (rich text en 6 bloques: Qué es · Qué cubre · Para quién es · Para quién no es · Qué incluye · Qué pasa al descargarlo), Call-to-action copy, Post-purchase redirect, Survey, Product page URL, Send review request emails, Images. Defaults fijos para F1-F2 (0-500 subs): CTA `Descargar gratis` · redirect vacío · survey OFF · review emails **OFF** · image primary = portada PDF 1280×720. El skill `/pdf-brand cheatsheet` genera esta ficha automáticamente junto al PDF (ver `.claude/commands/pdf-brand.md § 6`). La ficha pasa por los mismos validators que el PDF (sin roadmap, sin fechas, sin byline, voz plural, anti-IA §1). Regla activa desde 2026-04-18.
- **Versionar, nunca sobrescribir** (memoria `feedback_never_overwrite_images.md`).
- **Mobile-first:** legible en 375px, fuente mínima 11pt.
- **"Tangible" es jerga interna del pipeline.** Nunca aparece en copy visible al lector (banner, landing, OG description, subtítulo de artículo, email CTA, subject). Sustituir siempre por "PDF gratis", "guía gratis", "descargable" o el formato concreto ("checklist", "tabla comparativa"). Auditoría 2026-04-19 confirmó que ningún newsletter ES de éxito usa "tangible" en copy público — es término de marketing digital traducido del inglés que el lector ES no reconoce como categoría. Excepciones permitidas: comentarios HTML internos (`<!-- SECCIÓN TANGIBLE 1 -->`), docs del repo, nombres de marca real (ej: "TangibleFuture" en review del LOOI). El validator `/pdf-brand` bloquea patrones `el/este/nuestro tangible` como jerga filtrada al lector.
- Voz y anti-patterns heredados de [`editorial.md`](editorial.md).

## Microcopy de conversión — trust-lines bajo CTA

Todo botón/CTA de lead magnet (banner en artículo, ficha Beehiiv Digital Product, email de welcome flow, P.D. en newsletter) lleva debajo una **trust-line breve** que resuelve las 3 objeciones del lector ES al suscribirse: (a) qué recibo, (b) me van a spamear, (c) cuánto me comprometo.

**Prohibido:**
- Promesas de velocidad de entrega (`llega en 15 segundos`, `instantáneo`, `al momento`). Razón: Beehiiv entrega en 30–90 s reales y el filtro Promotions puede retrasarlo a minutos. Incumplir la promesa rompe la confianza ANTES de que el PDF se abra. Incidente 2026-04-19: el snippet banner original (`content/templates/banner-lead-magnet.html` línea 36) decía "te llega al email en 15 segundos" — rechazado por Rafael.
- Promesas sobre ausencia futura de publicidad/afiliados (`sin publicidad`, `sin promociones`, `sin spam comercial`). Razón: inconsistente con modelo de negocio (afiliados eventuales en F2+). No se promete lo que el modelo puede romper en 6 meses.
- Exclamaciones, imperativos agresivos, CAPS, emojis promocionales, hype anglosajón traducido (`Join 10,000+ readers`, `Don't miss out`, `¡Apúntate ya!`). Razón: patrón CTA no-spammy de `references/writewithai/extractions/ctas.md`.
- Copy opaco o vago (`sin letra pequeña`, `sin trucos`, `de verdad`). Razón: no resuelve objeción concreta, huele a marketer.

**Obligatorio — el trust-line debe incluir AL MENOS 2 de estos 3 elementos:**
1. **Formato concreto del tangible:** "PDF · 2 páginas", "Checklist 7 preguntas", "Comparativa 6 modelos".
2. **Baja fricción de salida:** "Cancela cuando quieras", "Un clic para salir". Evitar "baja"/"darte de baja" — registro administrativo ES (Movistar/Seguridad Social), no editorial (ver research 2026-04-19 abajo).
3. **Transparencia del vínculo:** "con tu suscripción" / "con tu suscripción semanal" / "gratis" (si la suscripción es obligatoria para descargar, decirlo explícitamente usando la palabra *suscripción* — es el término ES dominante en newsletters editoriales).

**Formato:** una o dos frases con punto final (patrón ES editorial). El separador `·` (middot) es aceptable pero NO obligatorio; los newsletters ES de éxito usan mayoritariamente frase con punto, no middots (patrón tech/SaaS US-driven). Máximo ~80 caracteres — debe caber en una línea a 375px.

**Default canónico ROBOHOGAR (Hoja de Compra y derivados):**
> `PDF gratis con tu suscripción semanal. Cancela cuando quieras.`

Elegido 2026-04-19 tras research sobre newsletters ES de éxito (Kloshletter, Suma Positiva, Xataka, Marketing4eCommerce, El Orden Mundial, El Confidencial) y validación de Rafael. Patrón ES confirmado: palabra *suscripción* domina sobre *newsletter* como sustantivo, *cancela* > *baja* como verbo (baja = registro administrativo), frase con punto > middots. Cadencia explícita ("semanal") se mantiene como diferencial ROBOHOGAR — ningún newsletter ES auditado la pone en la trust-line, por lo que nos sirve para resolver proactivamente la objeción *"¿cuánto me van a bombardear?"* en el banner de lead magnet (contexto distinto al form home).

**Hallazgos del research 2026-04-19 (newsletters ES auditados):**
- "Suscripción / Suscríbete / Suscribirse" gana 5/6 vs "newsletter" como verbo principal.
- "Baja" / "cancela" → 0 apariciones en trust-lines ES editoriales. El patrón ES dominante es la aceptación de política de privacidad ("Al suscribirte aceptas…"), no la promesa SaaS "cancela cuando quieras".
- Cadencia en trust-line → 0 menciones. Va en heading/eyebrow.
- "Sin spam" → 0 apariciones.
- Separador `·` → no es patrón ES, es tech/startup US.

En ROBOHOGAR adaptamos el patrón ES editorial (frase, *suscripción*, *cancela*) sin caer en el trust-line meramente legal — añadimos cadencia explícita ("semanal") porque el contexto banner-en-artículo sí la demanda.

**Variantes descartadas (documentadas como anti-patterns):**
- `PDF gratis · newsletter semanal · baja cuando quieras` — Rechazada tras research ES: "baja" es registro administrativo, middots son patrón tech US, "newsletter" como sustantivo principal va contra el uso dominante ES.
- `PDF gratis · te suscribes a la newsletter · baja cuando quieras` — Rechazada: cláusula verbal central rompe el ritmo.
- `PDF · 2 páginas · gratis · te das de baja en un clic` — Rechazada: oculta la suscripción; riesgo de disonancia en el primer welcome email.
- `Gratis · directo al email · sin letra pequeña` — Rechazada: "sin letra pequeña" es vago; "directo al email" no es elemento obligatorio.
- `Te llega al email en 15 segundos` — Rechazada (incidente original): promesa de velocidad incontrolable (Beehiiv 30-90s + Promotions).

**Validación pre-commit (`grep` sobre el HTML/markdown del banner, ficha o email):**
```
grep -iE "15 segundos|llega al email en|instantáneo|al momento|sin publicidad|sin promociones|sin letra pequeña|join [0-9]|don.t miss|apúntate ya" <archivo>
```
Si matchea, reescribir antes de pegar en artículo o publicar ficha. El validator del skill `/pdf-brand` (`skills/pdf_brand/validators.py`) aplica la misma regex como bloqueo duro pre-export.

**Herencia:** toda skill que genere copy de conversión (`/content-draft` § 8.8 · `/pdf-brand` § 6 · futuro `/social-content`) aplica esta regla sin excepción. Referencia, no duplicación.

Regla validada por Rafael 2026-04-19 tras pedir best practices certificadas — investigación en `references/writewithai/extractions/ctas.md`, `references/writewithai/extractions/lead-magnets.md`, `references/writewithai/04-email-newsletter-patterns.md` §§ 58-70, `references/newsletter/email-marketing-playbook.md` §13. Memoria: `feedback_microcopy_trust_lines.md`.

## Roadmap

- **F1 (hoy, 0-50 subs):** tangible definido en PASOS.md + entregado inline en el HTML del artículo. PDFs descargables activos vía `/pdf-brand cheatsheet` (adelantado desde 2026-04-18 al tener plan Scale y primer PDF Hoja de Compra v2 validado).
- **~50 subs:** expandir skill a las 3 variantes restantes (comparativa, guia, relato) según demanda. Primeros 4-5 tangibles en PDF activos en landing.
- **~100 subs:** ~15 tangibles acumulados + sección "Descargas" en landing robohogar.com.
- **~500 subs:** bundle temático + ebook recopilatorio de Ficciones Domésticas.
- **~5K subs (F3):** tangibles premium detrás de paywall en ROBOHOGAR+, paywall-at-cliffhanger pattern activo.

Plan completo: `../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md`. Operativa: `docs/guia-implementacion.md` § FASE 4C. Roadmap paid tier: `docs/plan-v2.md` §11 + [`08-paid-newsletter-blueprint-2026.md`](../../references/writewithai/08-paid-newsletter-blueprint-2026.md).
