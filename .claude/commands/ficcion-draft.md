---
description: Generate short speculative fiction drafts ("Ficciones Domésticas") for ROBOHOGAR with recurring characters, character-bible continuity, and Pixar/MRU/Paint-The-Villain frameworks. Supports 5 invocation modes (one-shot, episodio-serie, episode-0, piloto, tie-in). Use for serialized near-future domestic sci-fi stories (flash 500-800, episodio-serie 1.200-1.800, standalone 2.500-3.500) starring home robotics. Enforces anti-IA checklist and emotional (not physical) cliffhangers.
---

# Ficcion Draft — Borrador de relatos "Ficciones Domésticas"

Genera relatos cortos de ciencia ficción doméstica próxima (2030-2040) con personajes recurrentes, continuidad inter-episodio y voz narrativa propia. Pilar experimental de ROBOHOGAR — ~10% del content mix.

**Knowledge base completa:** `@references/writewithai/07-ficcion-y-narrativa-serializada.md`
**Bible maestra y catálogo de series:** `@references/ficciones/series-bible-maestra.md`
**Patrones serialized newsletter:** `@references/ficciones/serialized-newsletter-patterns.md`
**Anti-IA checklist (OBLIGATORIA):** `@references/anti-ia-checklist.md` — §1 Universal + §2 Ficción
**Roadmap ebook:** `@references/ficciones/ebook-roadmap.md`
**Voz de marca y excepciones:** `@.claude/rules/editorial.md` → sección "Narrativa especulativa"

## Frases trigger — invocación desde Rafael

Rafael usa una de estas frases para invocar el skill en el modo correspondiente. El skill detecta modo en paso 0.5.

| Intención | Frase trigger exacta | Modo interno |
|---|---|---|
| One-shot (sin serie, experimento) | **`/ficcion-draft one-shot <semilla>`** | `one-shot` |
| Nuevo episodio de serie activa | **`/ficcion-draft serie <slug> episodio <N>`** | `episodio-serie` |
| Episode 0 de nueva serie (entrada suave) | **`/ficcion-draft serie <slug> episode-0`** | `episode-0` |
| Flash piloto (testar serie antes de comprometer) | **`/ficcion-draft piloto <serie-candidata>`** | `piloto` |
| Tie-in con artículo publicado | **`/ficcion-draft tie-in <url-articulo>`** | `tie-in` |
| Ver estado del pilar | **`¿Qué series tengo activas y qué episodios llevo?`** | `estado` (lee `series-bible-maestra.md` y reporta) |

## When to activate

- "escribe ficción", "relato", "ficciones domésticas", "mini-relato"
- "flash fiction", "episodio de [serie]", "nuevo capítulo"
- "/ficcion-draft", "genera una historia corta"
- "escena con Tico/Eva/Cortés" (o cualquier personaje de una serie existente)

## Inputs esperados

Rafael pasa 3 parámetros (pregunta si falta alguno, pero **`{semilla-narrativa}` y `{dato-real}` son opcionales si existe research digest reciente** — ver paso 0):

| Parámetro | Valores | Ejemplo |
|---|---|---|
| `{semilla-narrativa}` | Tema/gancho en 1-2 frases. **Opcional** si hay backlog Ficciones en calendario | `"robot aspirador descubre consciencia contando pasos"` |
| `{personajes-involucrados}` | Nombres (deben existir en character bible) o `"nuevos"` | `"Amparo, Hugo, Vicky"` |
| `{longitud}` | `flash` (500-800) · `episodio-serie` (1.200-1.800) · `standalone` (2.500-3.500) | `episodio-serie` |

**Longitudes actualizadas 2026-04-18** según research serialized fiction 2025 (ver `@references/ficciones/serialized-newsletter-patterns.md` § 3.1). La ventana "corto 1.500-3.000" y "mini-serie-episodio 1.500-3.000" queda sustituida por **episodio-serie 1.200-1.800** (email mobile-first) y **standalone 2.500-3.500** (SEO web).

Parámetros opcionales:
- `{serie}`: slug de serie existente (ej. `familia-cortes`). Si no existe, se crea.
- `{pov}`: `omnisciente` (default) · `primera-persona-{personaje}`
- `{dato-real}`: estadística/ley concreta sobre la que anclar (INE, AI Act, spec técnica). Si falta, se intenta extraer del research digest más reciente antes de proponer uno.

## Workflow — 9 pasos obligatorios

### 0. Detectar modo de invocación

Primer paso ANTES de leer inputs: detectar qué modo pide Rafael según la frase trigger. Cada modo altera los pasos siguientes.

| Modo | Qué hace distinto |
|---|---|
| `one-shot` | Relato standalone sin serie. Va a `content/ficciones/_one-shots/`. No lee bible. No exige continuidad. Longitud por defecto: `flash` o `standalone` (no `episodio-serie`). |
| `episodio-serie` | Episodio numerado de serie activa. Lee `character-bible.md` + `arco-serie.md` + último episodio publicado. Exige continuidad canon. Longitud por defecto: `episodio-serie` (1.200-1.800). |
| `episode-0` | Entrada suave a nueva serie. Lee `character-bible.md` + `arco-serie.md` (recién rellenados). Presenta universo + personajes + regla del universo. Debe funcionar standalone (lector nuevo puede empezar aquí). Longitud ~1.500. |
| `piloto` | Flash testador — serie candidata aún no activada. Lee propuesta en `series-bible-maestra.md` si existe. NO canoniza nada — es desechable. Longitud `flash` (500-800). |
| `tie-in` | Relato flash que dialoga con un artículo publicado. Lee el artículo (URL o path), extrae dato real + tensión humana, genera relato flash. Slot destacado en email siguiente al artículo. Longitud `flash`. |
| `estado` | NO genera relato. Lee `references/ficciones/series-bible-maestra.md` + `content/ficciones/<slug>/character-bible.md` de series activas + calendario editorial. Devuelve tabla: series activas · último episodio · próximo previsto · hilos pendientes. |

**Si Rafael no especifica modo**: preguntar por la frase trigger adecuada. NO asumir.

### 1. Check inputs desde research digest (si falta semilla o dato real)

Si Rafael NO ha pasado `{semilla-narrativa}` o `{dato-real}`:

1. **Leer** `content/calendario-editorial.md` → sección "Backlog Ficciones Domésticas". Si tiene semillas pendientes (añadidas por `/research-digest` paso 8b), presentarle a Rafael las 3 más relevantes con formato:
   ```
   [1] <Gancho> — tema humano: <X> — formato sugerido: <flash/corto> — dato real: <Y>
   [2] ...
   [3] ...
   ¿Cuál elegimos o prefieres proponer una nueva?
   ```
2. Si además `{dato-real}` falta, **leer** el research-digest más reciente en `content/drafts/research-digest-*.md` y extraer 1-2 estadísticas/leyes/specs verificables relacionadas con la semilla. Ofrecer a Rafael o usar directamente si es evidente.
3. Si no hay backlog ni digest reciente (>30 días) → pedir a Rafael ejecutar `/research-digest` primero, O que proponga semilla manualmente.

**Regla:** no avanzar a paso 1 sin `{semilla-narrativa}` resuelta (del backlog, del digest, o manual) y `{dato-real}` resuelto.

### 2. Cargar contexto de serie

Si `{serie}` es una serie existente:
- Leer `content/ficciones/<serie>/character-bible.md` → pegar fichas de `{personajes-involucrados}` en el contexto de trabajo
- Leer `content/ficciones/<serie>/arco-serie.md` → identificar arco activo y episodios anteriores
- Leer el último episodio publicado para verificar tono/tiempo verbal

Si es serie nueva:
- Crear `content/ficciones/<serie>/` con copias de `content/ficciones/_template-character-bible.md` y `_template-arco-serie.md`
- Avisar a Rafael: "Antes de generar el borrador, rellena la character bible aquí: `<ruta>`. ¿Continúo con placeholders o esperamos?"
- **No generar borrador sobre bible vacía sin autorización explícita.**

Si `{serie}` no se especifica pero hay personajes → buscar en todas las bibles. Si ambiguo, preguntar.

### 3. Elegir framework narrativo

Tres frameworks disponibles, elegir según longitud/intención:

| Framework | Cuándo | Output |
|---|---|---|
| **Pixar Story Spine** (8 frases) | `corto` o `mini-serie-episodio` — arco completo | Esqueleto en 8 frases para validar antes de escribir |
| **5-Sentence Story** | `flash` — escena única | Setup · Incidente · Complicación · Giro · Payoff |
| **MRUs** (Motivation-Reaction Units) | Todos — durante la escritura de prosa | Cada frase abre pregunta, la siguiente la responde |

Además, SIEMPRE correr **Paint The Villain invertido** (paso 4) para validar que el villano es un problema humano, no el robot.

### 3.5. Declarar `left-wall` + `big-lie` (antes del villano)

Antes de pasar al conflicto humano, el skill pide al borrador dos declaraciones explícitas que se añaden al frontmatter YAML del relato:

- **`left-wall:`** — la restricción real/científica/regulatoria inviolable del relato. Lo que la realidad ES de 2030-2040 **sí dice** que es posible. Ejemplos: `"AI Act art. 6: humanoides domésticos son alto riesgo, requieren homologación CE"`, `"Aspirador 2033 sin brazos, LiDAR 360° solo superficies sólidas"`, `"Protocolo SAMUR Madrid real para ictus"`.
- **`big-lie:`** — la única licencia creativa mayor que el relato pide aceptar al lector (1 por relato, **no negociable**). Ejemplos: `"Humanoide refurbished accesible a familia media ES"`, `"Aspirador ha desarrollado modelo mental de rutinas humanas"`, `"Humanoide de cuidados diagnostica ictus 30s antes con sensores embedded"`.

**Regla de plausibilidad** (Adrian Tchaikovsky, *How I Write* 2025-12-31): *"You can get away with one big lie… but in order to support your one big lie, everything else needs to be true."* Todo lo que no sea el `big-lie` se verifica. Todo lo que contradiga el `left-wall` se elimina.

**Si el skill detecta 2 big lies** (p. ej. humanoide barato + memoria persistente ilimitada + habla 40 idiomas): o se recorta a uno, o se reescribe el concepto. No avanzar al paso 4 con 2 big lies.

Detalle + ejemplos en `@references/ficciones/serialized-newsletter-patterns.md § 2.4`.

### 4. Paint The Villain — validar conflicto humano

**Prompt literal** (ejecutar antes de outline):

```
Act as a story editor for "domestic sci-fi near-future."

Protagonist: {NAME + 1-line description}
Universe: {SERIES_PREMISE}
Episode theme: {SEMILLA_NARRATIVA}

Task: Generate 5 candidate "villains." The villain must NOT be a robot or the protagonist.
It must be an invisible human problem (loneliness, parental burnout, generational digital
gap, fear of obsolescence) that the robot REVEALS or AMPLIFIES but does not cause.

For each: [evocative 1-line name, e.g. "The 6pm Silence"] + [2-line explanation of what
it steals] + [1 concrete scene where it manifests].
```

Rafael (o el skill si Rafael delega) elige 1 villano humano. **Ese es el corazón del relato** — el robot lo expone, no lo causa.

### 5. Generar outline

#### 4a. Si longitud = `corto` o `mini-serie-episodio` → Pixar Story Spine literal:

```
I want you to create a Story Spine for my topic.

Topic = Serie "{serie}". Personajes: {personajes-involucrados}.
Universe: {premisa de arco-serie.md}. Año in-universe: {año}.
Tema: {semilla-narrativa}. Villano humano (de paso 3): {villano elegido}.
Tono: especulativo pero cercano, humor sutil, anclado en realidad española.

You are master of dramatic storytelling. You embody the creativity and energy of Pixar.

Please write 1 sentence for each of the following sentence stems for my topic:

1. Once upon a time...
2. Every day...
3. One day...
4. Because of that...
5. Because of that...
6. Because of that...
7. Until finally...
8. And ever since then...
```

Output en español. Validar: cada frase avanza la acción, ninguna es decorativa.

#### 4b. Si longitud = `flash` → 5-Sentence Story:

Generar 5 frases siguiendo estructura: (1) Setup · (2) Incidente · (3) Complicación · (4) Turning point · (5) Payoff/lección. Cada frase ≤20 palabras.

### 6. Expandir a prosa con MRUs

Prompt a usar durante la escritura (aplicar frase a frase al desarrollar el outline):

```
You are a reader-modeling AI trained in Dwight Swain's Motivation-Reaction Units.

I will paste one sentence from my draft. Your job:
1. Predict the top 3 questions a reader would have right after reading it.
2. Rank them by emotional urgency (1 = most urgent).
3. For the #1 question, write the next sentence of the story that answers it —
   matching voice and pacing of the input.

Voice reference: Spanish (Spain), sentences under 20 words, no adverbs when a stronger
verb works. POV: {pov}. Tense: {tiempo verbal coherente con episodios previos}.

Input sentence:
{SENTENCE}
```

Reglas de prosa:
- Frases cortas (<20 palabras mediana), alternar con 1 frase larga cada 3-4 para respiración
- Diálogo en raya española (—), no comillas
- Presente para inmediatez / pasado para reflexión. **No mezclar en la misma escena.**
- Cada 300-400 palabras, una frase-gancho que reabra loop nuevo
- Hook de primera frase: elegir de la tabla de `@references/writewithai/07-ficcion-y-narrativa-serializada.md` sección 5 (in medias res, objeto mundano crítico, diálogo cortado, etc.)

### 7. Validar continuidad — Character Voice Checker

Tras terminar el borrador, correr este prompt por cada personaje con diálogo/interioridad:

```
You are a continuity editor for a serialized fiction project.

Character bible for {CHARACTER_NAME}:
---
{PASTE_FULL_BIBLE_SECTION}
---

Scene draft:
---
{PASTE_DRAFT}
---

Check 4 things:
1. Voice drift — dialogue/internal monologue off-character?
2. Limitations breach — does the character do something its fisiología forbids?
3. "Would never do" breach — violates guardarraíl?
4. Arc coherence — advances arcos largos or contradicts them?

For each issue: quote offending line + suggest specific rewrite. If clean: "Consistent."
```

Si hay issues → reescribir líneas ofensivas antes de output final. Si bible aún está en placeholder, marcar `[PENDING BIBLE]` y avisar a Rafael.

### 8. Anti-IA checklist — OBLIGATORIO antes de output

Cargar [`@references/anti-ia-checklist.md`](../../references/anti-ia-checklist.md) completo y correr **§1 Universal + §2 Ficción** sobre el borrador. Ambas secciones son obligatorias en ficción (§2 añade: cero thought verbs Palahniuk, cliffhanger emocional/moral no físico, POV coherente, 1 detalle raro Chiang por escena, diálogo con imperfecciones, dato real anclado).

**Regla de decisión:** ≥3 flags → rechazar output y reescribir · 1-2 flags → reescribir líneas ofensivas y re-correr · 0 flags → proceder al paso 9.

Complementa las excepciones de voz ficción en `@rules/editorial.md § Narrativa especulativa`.

### 8.2. Anti-anglicismos ES — OBLIGATORIO antes de output

Verificar contra `@rules/editorial.md § Apertura y cierre del cuerpo del email — anti-anglicismos` (regla activa desde 2026-04-19, basada en auditoría de 20 newsletters ES). En ficción NARRADOR y PROSA siguen la regla; en **diálogo de personaje** se relaja (un personaje puede decir "Hola, Amparo" de forma natural — es diálogo realista, no tic anglo del narrador).

Checklist rápida sobre el texto del relato (excluyendo contenido entre comillas/guiones de diálogo):
- [ ] 0 saludos anglo fuera de diálogo: `Hola X,` + nombre · `Querido/a lector/a` · `Hey` · `Espero que estés bien`
- [ ] 0 cierres anglo: `Cheers` · `Best` · `Atentamente`
- [ ] Em-dash (`—`) permitido en narración (es puntuación editorial ES legítima); prohibido en trust-lines <15 palabras si el relato incluye CTA/landing.

Si hay violación en narrador → reescribir. Si es en diálogo → validar que sea verosímil, no tic del narrador infiltrado en la voz del personaje.

### 8.5. Formato técnico Beehiiv — OBLIGATORIO antes de output

Verificar contra `@rules/editorial.md § Formato técnico (Beehiiv)`. Política de negritas aplicable también a ficción:

- [ ] Ningún `<strong>`/`<b>`/`**...**` dentro de `<h1>`, `<h2>`, `<h3>` (títulos de episodio, cortes narrativos, epígrafes)
- [ ] Ningún `<strong>`/`<b>` dentro de `<th>`/`<td>` si el relato incluye alguna tabla/ficha
- [ ] Ningún `<strong>`/`<b>` dentro de `<div class="checklist">` u otro callout con fondo crema `#FFF9EF`
- [ ] SÍ permitido: negrita puntual dentro de párrafos de prosa para énfasis

Si hay violaciones → limpiar antes de entregar (no se pregunta al usuario).

### 9. Validaciones finales antes de output

- [ ] **Longitud**: flash 500-800 | episodio-serie 1.200-1.800 | standalone 2.500-3.500. Contar palabras. Si supera por más del 15% → recortar.
- [ ] **Nivel ≈4**: gramática simple (frases cortas, subordinación mínima) + concepto complejo (tensión sci-fi/social real). Evitar léxico rebuscado si el concepto ya exige esfuerzo.
- [ ] **Dato real anclado**: ≥1 fact verificable (AI Act, INE, spec de robot). Citar en comentario HTML invisible al final: `<!-- dato-real: ... -->`
- [ ] **Villano humano, no robot**: el conflicto emocional debe ser identificable en 1 frase.
- [ ] **Voz**: POV consistente (omnisciente O 1ª persona del personaje). **Excepción explícita a la regla de "primera persona plural" baseline.**
- [ ] **Hook de primera frase**: el primer período debe provocar "una más".
- [ ] **Tag visual**: "Ficciones Domésticas" en frontmatter + categoría Beehiiv "Opinión" o tag dedicado.

## Output — estructura obligatoria

### Archivos a generar

```
content/ficciones/<serie>/
  ├── YYYY-MM-DD-<slug>.md        ← el relato (Markdown con frontmatter)
  ├── YYYY-MM-DD-<slug>.html      ← versión HTML Beehiiv (opcional, si se va a publicar)
  ├── PASOS.md                    ← checklist de publicación + metadata SEO
  └── assets/
      └── hero-<slug>.png         ← hero still cinematográfico (opcional)
```

### Frontmatter YAML del relato

```yaml
---
title: "Título del relato"
seo_title: "Título SEO (max 55 chars)"
meta_description: "Resumen con gancho (110-155 chars)"
slug: slug-kebab-case
serie: familia-cortes
episodio: 03
longitud: flash | corto | mini-serie-episodio
palabras: 847
personajes: [Tico, Abuela Cortés]
pov: omnisciente | primera-persona-tico
tiempo-verbal: presente | pasado
tag: Ficciones Domésticas
tags-beehiiv: [Opinión]
dato-real: "INE: 20,1% españoles +65 años en 2033"
villano-humano: "El silencio de las 18:00 (soledad de los mayores solos)"
left-wall: "Fisiología aspirador 2033: sin brazos, LiDAR 360° solo superficies sólidas, sin acceso telefónico directo"
big-lie: "Aspirador ha desarrollado modelo mental de rutinas humanas lo bastante preciso para detectar ausencia"
framework: pixar-spine | 5-sentence | mrus
status: borrador
created: YYYY-MM-DD
hero-image: assets/hero-<slug>.png
---
```

### Hero image — 1 código visual por serie (regla editorial)

Cada serie (y cada one-shot) de Ficciones Domésticas tiene **un código visual propio y consistente** para que el lector la reconozca de un vistazo. Sistema completo + precedentes en la memoria [`feedback_ficcion_hero_style.md`](../../../RRP-DEV/.claude/memory/feedback_ficcion_hero_style.md) (léela ANTES de generar cualquier hero de ficción).

**Regla universal (los 5 estilos la cumplen):**
- Siempre humano + robot/tech en el mismo frame. Si solo sale humano → no es hero ROBOHOGAR.
- No ventana exterior visible (Gemini mete neones con caracteres asiáticos — ver `assets/branding/nano-banana-prompt-base.md`).
- No LEDs/neones/glow en robots (excepciones puntuales: glow dorado ojos Asimov, pinpoint azul Black Mirror).
- No texto, letras ni caracteres asiáticos.

**Códigos visuales activos (consultar arco-serie.md § 9 de cada serie + memoria para precedente canónico):**

| Serie | Código | Rasgos clave |
|---|---|---|
| La Casa de Amparo | domestic warm | Hugo humanoide + Amparo + Lavapiés constante · lámpara tulipán ámbar · butaca floral · After Yang + Amor sin escalas |
| Crónicas de Ronda 3 | documental social | RONDA-3 utility 55cm constante + humano distinto cada ep · piso VPO distinto · ocre sucio verdoso desaturado · grano denso · Perfect Days + Real Humans |
| Cartas a MAIA | epistolar literario dual | NO humanoide (laptop + lámpara brass como "tech") · Clara + ocasionales vía mensaje · Cáceres burgundy cálido VS Berlín azul frío desaturado según POV · After Yang + 84 Charing Cross Road |

**Estilos reservados (NO usar en episodios):**
- **Asimov oil painting** — solo para tapa de ebook recopilatorio (~500 subs, roadmap ficciones)
- **Black Mirror frío** — solo para sub-línea *"Relatos inversos de Black Mirror"* (relatos inquietantes, sistema humano como amenaza, robot neutro)

**Al crear una nueva serie o one-shot:**
1. Definir el código visual en `arco-serie.md` § 9 "Notas de producción" → "Hero image recurrente" ANTES del primer episodio — framing + paleta + luz + referencias cinematográficas + elementos constantes del universo.
2. Registrarlo también en esta tabla del skill si va a reutilizarse.
3. Mantener el código estable episodio a episodio — variar escena y humano, no el sistema visual.

**Prompt base por serie (adaptar a la escena del episodio):**

```
[FRAMING del código de serie], 2033 [ESPACIO del universo de la serie], [ESCENA CLAVE del episodio].
[DESCRIPCIÓN del humano con cara visible + postura emocional del episodio].
[DESCRIPCIÓN del robot/tech del universo — matte, sin LEDs, cuerpo entero].
[LUZ del código — motivada, una única fuente].
[PALETA del código]. [DETALLES DOMÉSTICOS ESPAÑOLES del código].
[REFERENCIAS CINEMATOGRÁFICAS del código].
No text, no letters, no Asian characters, no windows to exterior, no LEDs.
```

- **Fallback si Rafael no quiere hero:** usar monograma R sobre fondo ámbar claro como placeholder neutro.
- Añadir la nueva imagen a `assets/branding/asset-catalog.md` bajo sección "Heros ficción" indicando código visual aplicado.

### PASOS.md del relato

Debe contener:
1. **SEO metadata** (title, description, slug, tag Beehiiv) para copiar a Beehiiv
2. **Hero elegido** (ruta relativa)
3. **Checklist de publicación**: edit Rafael → tag "Ficciones Domésticas" → publish `Email and web`
4. **Log canónico para la bible**: qué eventos hay que añadir a `character-bible.md` sección "Episodios publicados" tras publicar (fecha in-universe, cambios de estado de personajes, elementos nuevos del universo)
5. **Hooks para siguiente episodio** (si aplica): preguntas abiertas, objetos colocados sin resolver, relaciones tensadas

## Reglas inviolables

1. **Nunca escribir sobre character bible vacía sin autorización explícita de Rafael.**
2. **El robot NO es el villano.** Si tras paso 3 el villano propuesto es el robot → repetir paso 3.
3. **Voz plural de ROBOHOGAR NO aplica en ficción.** En ficción: omnisciente o 1ª persona del personaje. Es la única excepción editorial documentada.
4. **No canonizar detalles no establecidos** sin añadirlos a `character-bible.md` sección "Canon establecido". Si un relato introduce hecho nuevo (ej: Eva tiene hermana en Murcia) → añadir al log.
5. **Borrador siempre**, Rafael edita y publica manualmente. Nunca auto-publicar.
6. **Dato real obligatorio** — sin fact anclado, el relato es fantasía genérica. Rechazar borrador.
7. Si el skill detecta que los personajes pedidos no existen en ninguna bible → crear estructura de serie nueva pero NO inventar personajes "canon" sin Rafael.

## Cross-references

- **Upstream (alimenta este skill):**
  - `@.claude/commands/research-digest.md` → genera "Backlog Ficciones Domésticas" + datos reales (paso 0 lee de aquí)
  - `@content/calendario-editorial.md` → sección "Backlog Ficciones Domésticas"
  - `content/drafts/research-digest-*.md` → datos reales anclables
- **Downstream (consume output de este skill):**
  - `@.claude/commands/post-publish.md` → limpieza tras publicar episodio
  - `@.claude/commands/social-content.md` → posts de redes anunciando el episodio
  - `@.claude/commands/pdf-brand.md` → **pendiente F2:** cuando la variante `/pdf-brand relato` esté activa, generar mini-poster PDF del relato (ilustración hero + quote memorable + dato real ancla + firma ROBOHOGAR). Roadmap en `@rules/tangibles.md § Mapeo contenido→tangible`. Mientras no exista, el tangible de ficción es inline (quote destacado + dato real en caja crema) y el ebook recopilatorio queda diferido a ~500 subs.
- **Knowledge/soporte:**
  - Knowledge base completa: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`
  - **Bible maestra (catálogo de series + canon transversal):** `@references/ficciones/series-bible-maestra.md`
  - **Patrones serialized newsletter 2025-2026:** `@references/ficciones/serialized-newsletter-patterns.md`
  - **Anti-IA checklist (OBLIGATORIA):** `@references/anti-ia-checklist.md`
  - **Roadmap ebook:** `@references/ficciones/ebook-roadmap.md`
  - Voz editorial (sección Narrativa especulativa): `@.claude/rules/editorial.md`
  - Plantillas: `@content/ficciones/_template-character-bible.md` · `@content/ficciones/_template-arco-serie.md`
  - Guía del pilar: `@content/ficciones/README.md`
  - Prompts genéricos: `@references/writewithai/05-prompts-utiles.md`
  - Voz/hooks genéricos: `@references/writewithai/01-voz-y-estructura.md`
  - Asset catalog (estilo hero ficción): `@assets/branding/asset-catalog.md` → sección "Heros ficción"

<!-- created by wwai-integration 2026-04-17 -->
