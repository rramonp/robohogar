# Revisión de integración — Write With AI × ROBOHOGAR

**Fecha:** 2026-04-17
**Ejercicio:** Extracción y asimilación sistemática del newsletter `writewithai.substack.com` (Nicolas Cole & Dickie Bush, 113K subs, $400K ARR) en el repositorio ROBOHOGAR.
**Propósito de este documento:** auditoría para que Rafael revise todo lo que se ha integrado y entienda cómo se beneficia en cada flujo.

---

## 1. TL;DR ejecutivo

| Capa | Creado | Modificado | Deliverable |
|---|---|---|---|
| **Knowledge base externa** | 45 archivos (8 síntesis + 36 fichas + _README) | — | `references/writewithai/` · 5.461 líneas |
| **Skills (`/commands`)** | 1 nuevo (`/ficcion-draft`) | 2 (`/research-digest`, `/content-draft`) | Flujo end-to-end con integración bidireccional |
| **Rules (`.claude/rules`)** | — | 2 (`editorial.md`, `newsletter.md`) | Nueva sección narrativa + patrones subject line |
| **Docs estratégicos** | — | 3 (`brand-voice.md`, `plan-v2.md`, `email-marketing-playbook.md`) | Patrones de voz + 5 growth tactics + welcome sequence |
| **Content scaffold** | 3 (`ficciones/README.md` + 2 templates) | 2 (`calendario-editorial.md`, `asset-catalog.md`) | Pilar "Ficciones Domésticas" operativo |

**Total material generado/añadido:** ~6.400 líneas. **Coste Firecrawl:** ~66 créditos. **Tiempo:** una sesión.

---

## 2. Inventario completo de archivos tocados

### 2.1 Creados desde cero

```
references/writewithai/                                        ← knowledge base externa
├── 00-index-completo.md              (457L)   catálogo de 142 artículos en 35 categorías
├── 01-voz-y-estructura.md            (128L)   patrones de voz Cole/Bush aplicados a ROBOHOGAR
├── 02-estructura-articulo-visual.md  (233L)   anatomía block-by-block + 3 templates
├── 03-growth-playbook.md             (143L)   5 tácticas $400K ARR adaptadas a fases
├── 04-email-newsletter-patterns.md   (170L)   subject lines, welcome, CTAs, 1-3-1
├── 05-prompts-utiles.md              (299L)   8 prompts literales (EN) + variantes ROBOHOGAR
├── 06-branding-visual.md             (158L)   colores/tipo/componentes + 3 ideas
├── 07-ficcion-y-narrativa-serializada.md (356L) pilar narrativa: Pixar Spine, MRUs, Villain
└── extractions/                              (36 fichas por subcategoría, ~3.500L)
    ├── _README.md
    ├── newsletters.md, long-form-posts.md, hooks-and-headlines.md, …
    └── [33 más]

.claude/commands/
└── ficcion-draft.md                  (287L)   skill nuevo — Ficciones Domésticas end-to-end

content/ficciones/
├── README.md                         (130L)   guía del pilar narrativa
├── _template-character-bible.md      (106L)   plantilla rellenable por Rafael
└── _template-arco-serie.md           ( 99L)   plantilla de arco de serie

docs/
└── wwai-integration-review.md        (este archivo)
```

### 2.2 Modificados (aditivos, sin reescribir)

```
.claude/commands/
├── research-digest.md                (125 → 173L)  +48L: semillas narrativas + handoff
└── content-draft.md                  (123 → 205L)  +82L: templates + hook checklist

.claude/rules/
├── editorial.md                      ( 32 →  47L)  +15L: sección "Narrativa especulativa"
└── newsletter.md                     ( 32 →  40L)  +8L:  tabla subject + fórmula 1-3-1

docs/
├── brand-voice.md                    (192 → 254L)  +62L: sección 11 "Aprendizajes externos"
└── plan-v2.md                        (297 → 386L)  +89L: sección 10 "Growth tactics F2-3"

references/newsletter/
└── email-marketing-playbook.md       (362 → 453L)  +91L: welcome sequence + CTAs + subjects

content/
└── calendario-editorial.md           ( 52 →  75L)  +23L: slot ficciones + backlog ficciones

assets/branding/
└── asset-catalog.md                  (387 → 450L)  +63L: sección "Heros ficción"
```

**Nada se ha commiteado.** Todo está en tu working tree para que hagas diff cuando quieras.

---

## 3. Knowledge base externa — qué contiene cada archivo

| Archivo | Úsalo cuando necesites… |
|---|---|
| [00-index-completo.md](../references/writewithai/00-index-completo.md) | Buscar un tema concreto de Cole/Bush por categoría o por likes |
| [01-voz-y-estructura.md](../references/writewithai/01-voz-y-estructura.md) | Entender su voz (hooks, ritmo 1/3/1, cierres) para imitarla en español |
| [02-estructura-articulo-visual.md](../references/writewithai/02-estructura-articulo-visual.md) | Estructurar un artículo con los 3 templates (Problem/Solution, Common Mistakes, How-To) |
| [03-growth-playbook.md](../references/writewithai/03-growth-playbook.md) | Planificar crecimiento del newsletter — 5 tácticas $400K ARR por fase |
| [04-email-newsletter-patterns.md](../references/writewithai/04-email-newsletter-patterns.md) | Escribir subject lines, welcome emails, CTAs |
| [05-prompts-utiles.md](../references/writewithai/05-prompts-utiles.md) | Copiar prompts literales probados (Hustle Formula, Idea Generation, etc.) |
| [06-branding-visual.md](../references/writewithai/06-branding-visual.md) | Referencia visual: colores/tipo/componentes observados en writewithai.com |
| [07-ficcion-y-narrativa-serializada.md](../references/writewithai/07-ficcion-y-narrativa-serializada.md) | Base teórica del pilar Ficciones Domésticas (Pixar Spine, MRUs, Paint The Villain) |
| `extractions/*.md` | Fichas por subcategoría con top artículos analizados (solo consultar si el archivo de síntesis no basta) |

---

## 4. Cambios por skill — ANTES vs DESPUÉS

### 4.1 `/research-digest`

**Antes:**
- Scrapeaba fuentes, categorizaba noticias, evaluaba viralidad
- Output: digest semanal + wiki update + backlog general en calendario
- No hablaba con el pilar ficción

**Después (4 cambios clave):**

1. **Paso 5 nuevo — extracción de semillas narrativas:** de las Top + Notable stories, detecta 2-4 que tengan "alma" narrativa (tensión humana latente, escenas evocativas). Para cada una extrae: gancho 1-frase especulativo 2030-2040, **dato real ancla**, **villano humano implícito** (soledad, burnout, brecha digital), personajes tipo que podrían encajar.
2. **Nueva sección en output:** "Semillas narrativas — Ficciones Domésticas" en el Markdown del digest.
3. **Paso 8 desdoblado — actualiza DOS backlogs:**
   - `8a.` Backlog de temas (artículos) — como siempre
   - `8b.` Backlog Ficciones Domésticas — semillas con columnas Prioridad/Semilla/Formato/Serie/Tema humano/Dato real/Notas
4. **Sección "Handoff a otros skills"** al final documentando cómo `/content-draft`, `/ficcion-draft` y `/social-content` consumen el output del digest.

**Qué verás al ejecutar `/research-digest`:**

- El digest MD ahora tendrá una sección extra al final: "Semillas narrativas — Ficciones Domésticas" con 2-4 ganchos accionables
- `content/calendario-editorial.md` → "Backlog Ficciones Domésticas" se poblará automáticamente
- Si llevas 3 semanas sin escribir ficción, ya tendrás 6-12 semillas en el banco esperando

---

### 4.2 `/content-draft`

**Antes:**
- Generaba borrador HTML desde el digest seleccionado
- Aplicaba voz ROBOHOGAR + SEO checklist
- No tenía templates estructurales explícitos

**Después (2 cambios clave):**

1. **Sección "Templates estructurales"** con parámetro `--template=<tipo>`:
   - `--template=problem-solution` (tutoriales, how-to, cartas de venta)
   - `--template=mistakes` (reviews, advertencias, análisis críticos)
   - `--template=how-to` (guías paso a paso)
   - Cada template tiene su estructura block-by-block mapeada
2. **Sección "Hook checklist"** con 5 tipos de apertura a considerar antes del borrador:
   - Scene-setting inmediato
   - Pregunta retórica provocadora
   - Dato contra-intuitivo
   - Anécdota personal corta
   - Contradicción obvia que pocos ven

**Qué verás al ejecutar `/content-draft`:**

- Si no pasas `--template`, el skill te preguntará cuál encaja mejor con el ángulo elegido
- El hook no se improvisa: pasa por la checklist de 5 tipos y se elige deliberadamente
- Los borradores ganan estructura reproducible, no cada uno improvisado

---

### 4.3 `/ficcion-draft` (NUEVO)

Skill completo desde cero. No existía antes. 287 líneas. Autocontenido: lleva los prompts literales inline, no necesita abrir la knowledge base para ejecutar.

**Inputs aceptados:**

| Parámetro | Valores | Obligatorio |
|---|---|---|
| `{semilla-narrativa}` | Tema/gancho 1-2 frases | **Opcional** si hay backlog Ficciones reciente |
| `{personajes-involucrados}` | Nombres (de bible) o `"nuevos"` | Sí |
| `{longitud}` | `flash` · `corto` · `mini-serie-episodio` | Sí |
| `{serie}` | Slug (`familia-cortes`, etc.) | Opcional |
| `{pov}` | `omnisciente` (default) · `primera-persona-<personaje>` | Opcional |
| `{dato-real}` | Estadística/ley/spec | Opcional — se extrae del digest si falta |

**Workflow en 8 pasos:**

0. **Check inputs desde research digest** — si falta semilla o dato real, lee backlog Ficciones + último digest. Si ambos faltan >30 días, pide a Rafael ejecutar `/research-digest` primero
1. **Cargar contexto de serie** — lee `character-bible.md` + `arco-serie.md` + último episodio publicado. Si bible vacía → se niega a escribir sin autorización
2. **Elegir framework narrativo** — Pixar Story Spine (corto/episodio) · 5-Sentence Story (flash) · MRUs (prosa)
3. **Paint The Villain invertido** — prompt que genera 5 villanos candidatos; el villano DEBE ser un problema humano (soledad, burnout, brecha digital), nunca el robot
4. **Generar outline** — con el framework elegido, output en español
5. **Expandir a prosa con MRUs** — frase a frase, aplicando Motivation-Reaction Units de Dwight Swain
6. **Reglas de prosa** — frases <20 palabras, diálogo en raya (—), tiempo verbal consistente
7. **Character Voice Checker** — valida continuidad con la bible de cada personaje
8. **Validaciones finales** — longitud, nivel ≈4, dato real anclado, villano humano, POV consistente, hook de primera frase

**Qué verás al ejecutar `/ficcion-draft`:**

- Genera archivos en `content/ficciones/<serie>/YYYY-MM-DD-<slug>.md` con frontmatter YAML completo
- Produce `PASOS.md` con metadata SEO + checklist de publicación + log canónico para la bible + hooks para siguiente episodio
- Opcional: hero image estilo "still cinematográfico" (Black Mirror doméstico, After Yang, Her)

---

## 5. Cambios en rules

### 5.1 `.claude/rules/editorial.md`

**Añadido:** sección "**Narrativa especulativa — Ficciones Domésticas**" con:

- Excepción explícita a la regla "primera persona plural" — en ficción vale omnisciente o 1ª persona del personaje POV
- Longitudes: 1.500-3.000 palabras (corto) · 500-1.000 (flash)
- Cadencia: 1 cada 3-4 semanas
- Regla del villano humano (nunca robot)
- Tag visual "Ficciones Domésticas"
- Hero style: still cinematográfico (no product-hero)
- Link al skill y a la KB

### 5.2 `.claude/rules/newsletter.md` (40 líneas exactas)

**Añadido compactamente:**

- Tabla de **5 arquetipos de subject line** probados con ejemplos ROBOHOGAR en español
- **Fórmula 1-3-1** como estándar CTA único (1 gancho + 3 puntos + 1 CTA)
- Link a `email-marketing-playbook.md` para el detalle completo

---

## 6. Cambios en docs

### 6.1 `docs/brand-voice.md` (+62L, sección nueva 11)

**Sección 11 — "Aprendizajes de referencias externas"** con:

- **3 hooks probados** de Cole/Bush adaptados al español plural ROBOHOGAR
- **Ritmo 1/3/1** como patrón de párrafo (1 frase de setup + 3 frases de desarrollo + 1 frase de cierre)
- **Transiciones con preguntas retóricas** (*"¿Cómo funciona esto?"*)
- **Cierre ritual** "Eso es todo. / Os dejamos." + P.D. opcional con upsell editorial
- Link a `01-voz-y-estructura.md` para el detalle

### 6.2 `docs/plan-v2.md` (+89L, sección nueva 10)

**Sección 10 — "Growth tactics Fase 2-3 (aprendidos de Write With AI)"** con las 5 palancas $400K ARR adaptadas a ROBOHOGAR:

| # | Táctica | Fase | ROI | Esfuerzo |
|---|---|---|---|---|
| 1 | Digital product drops trimestrales | F2+ (300+ subs) | Alto | Medio |
| 2 | Founding Member tier (Beehiiv Scale) | F3 (1K+ subs) | Alto | Bajo |
| 3 | Master Content Library por categoría | F1-F2 (desde ya) | Medio | Bajo |
| 4 | Welcome email + survey + gift + upsell | F1 (ya) | Muy alto | Medio |
| 5 | Distribución LinkedIn + Instagram Reels | F1-F2 | Medio-alto | Alto |

Cada una con descripción, fase recomendada, ROI esperado, esfuerzo, dependencias, y adaptación concreta a Beehiiv (free vs Scale).

### 6.3 `references/newsletter/email-marketing-playbook.md` (+91L, 4 secciones nuevas)

**Añadidos:**

- **Sección 12 — Welcome sequence 4-5 emails** (template completo con propósito, hook, cuerpo, CTA por email). Nota: Beehiiv free no soporta automations multi-paso → se proponen como **broadcasts manuales** segmentados a subs `<14 días`, con migración a automation al subir a Scale
- **Sección 13 — CTA above-fold + final** (patrón dual que Cole/Bush usan: CTA en los primeros 200px Y al cierre)
- **Sección 14 — 7 estilos de subject line** con ejemplos ROBOHOGAR (curiosidad, número, contradicción, pregunta, urgencia, beneficio, personalización)
- **Sección 15 — Typeform + gift + upsell** (flujo Cole/Bush adaptado a **poll nativo Beehiiv** como alternativa gratuita, con trade-offs explicados)

---

## 7. Cambios en content y assets

### 7.1 `content/calendario-editorial.md`

**Añadido:**

- Fila nueva en tabla cadencia: "Ficciones Domésticas · 1 cada 3-4 semanas · Email and web tag"
- Sección **"Slot Ficciones Domésticas"** con detalle de cadencia, formato, skill, piloto recomendado
- Sección **"Backlog Ficciones Domésticas"** (tabla vacía con columnas: Prioridad, Semilla, Formato, Serie sugerida, Tema humano, **Dato real ancla**, Notas) — `/research-digest` la rellenará automáticamente

### 7.2 `content/ficciones/` (estructura nueva)

- [`README.md`](../content/ficciones/README.md) — guía del pilar narrativa con flujo de trabajo end-to-end y diagrama
- [`_template-character-bible.md`](../content/ficciones/_template-character-bible.md) — plantilla rellenable de biblia de personajes (frontmatter YAML + ficha por personaje + Canon establecido + Episodios publicados + Arcos pendientes)
- [`_template-arco-serie.md`](../content/ficciones/_template-arco-serie.md) — plantilla de arco de mini-serie (premisa, tema, arco emocional, episodios planeados, cliffhanger)

### 7.3 `assets/branding/asset-catalog.md` (+63L)

**Añadida sección "Heros ficción — still cinematográfico"** con:

- Diferenciación explícita vs product-hero de artículos
- Referencias cinematográficas: *Black Mirror* doméstico, *After Yang*, *Her*, *Ex Machina* ligero
- Prompt base para `/nano-banana` adaptado a ficciones
- Parámetros sugeridos (luz motivada, desaturación ligera, grano suave, sensación anamórfica)
- Fallback: monograma R sobre fondo ámbar claro si Rafael no quiere hero dedicado

---

## 8. Qué verás cuando…

### 8.1 Cuando ejecutes `/research-digest`

**Antes:** recibías un digest con Top/Notable/Monitoring + imágenes + actualización de backlog general y wiki.

**Ahora, además, verás:**

- Una nueva sección al final del digest: **"Semillas narrativas — Ficciones Domésticas"** con 2-4 ganchos ya procesados (gancho + dato real ancla + villano humano + personajes tipo + formato sugerido)
- `calendario-editorial.md` con dos backlogs actualizados simultáneamente: artículos + ficciones
- El log de handoff: "has X semillas esperando para `/ficcion-draft`"
- Datos reales aislados (ley, estadística, spec) que luego `/ficcion-draft` puede reusar como ancla

**Beneficio concreto:** nunca más una sesión de ficción te pillará "con el cerebro en blanco". Cada digest semanal te deja 2-4 semillas listas para convertir en relato.

---

### 8.2 Cuando generes contenidos (`/content-draft`)

**Antes:** el skill te generaba un borrador HTML desde el digest con voz ROBOHOGAR y SEO. Cada borrador improvisado estructuralmente.

**Ahora, además, verás:**

- Una pregunta al inicio: *"¿Qué template aplico? `problem-solution` / `mistakes` / `how-to`"*
- Una checklist de hook en el proceso: antes de escribir la intro, se selecciona deliberadamente entre 5 tipos
- Estructura block-by-block mapeada al template elegido (H2s, CTAs intermedios, orden de secciones)
- Voz aplicada siguiendo ritmo 1/3/1, frases cortas, transiciones con pregunta retórica, cierre ritual

**Beneficio concreto:** los artículos ganan homogeneidad estructural — tu marca editorial empieza a tener "firma" reconocible en la forma, no solo en el tono. Menos editing tras borrador.

---

### 8.3 Cuando hagas búsquedas

No hay un skill nuevo para "búsquedas" puras, pero sí mejoras indirectas:

- **Firecrawl MCP** sigue igual, pero `/research-digest` ahora exprime mejor cada hallazgo (extrae ángulo editorial Y ángulo narrativo de la misma noticia)
- Si buscas referencia sobre cualquier tema de writing/newsletter/growth, el camino directo es ahora `references/writewithai/*` en lugar de googlear
- Si un tema necesita más profundidad que la ficha sintetizada, hay 36 fichas individuales en `extractions/` y el índice maestro con 142 artículos enlazados

**Beneficio concreto:** menos tiempo googleando "how to write a subject line that converts" — ya está destilado en [`04-email-newsletter-patterns.md`](../references/writewithai/04-email-newsletter-patterns.md).

---

### 8.4 Cuando escribas con los nuevos templates

**Caso 1 — Artículo tipo review/análisis crítico:**
`/content-draft --template=mistakes` →
1. H1 con patrón "Los 5 errores que X comete con Y"
2. Intro con pregunta retórica
3. Listado numerado con: error → consecuencia → corrección
4. Cierre con takeaway y CTA single

**Caso 2 — Artículo tipo tutorial:**
`/content-draft --template=how-to` →
1. H1 con patrón "Cómo [objetivo] sin [obstáculo]"
2. Intro con beneficio upfront
3. Pasos numerados con screenshots/ejemplos
4. Sección "Errores comunes" al final
5. CTA single

**Caso 3 — Artículo tipo defensa de tesis:**
`/content-draft --template=problem-solution` →
1. H1 con el problema concreto
2. Intro con agravamiento del dolor
3. Enfoques que fallan (por qué)
4. Tu solución paso a paso
5. CTA single

**Caso 4 — Relato corto de ficción:**
`/ficcion-draft` → workflow 8 pasos con Pixar Spine/MRU/Voice Checker

**Beneficio concreto:** cada tipo de contenido tiene una ruta estructural reproducible. No reinventas la rueda cada semana.

---

### 8.5 Cómo cambia la forma de escribir

**Voz — lo que cambia:**

| Antes | Ahora |
|---|---|
| Párrafos variables en longitud, improvisados | Ritmo **1/3/1** (1 frase setup + 3 desarrollo + 1 cierre) como patrón base |
| Transiciones con nexos ("además", "también") | Transiciones con **pregunta retórica en cursiva** (*"¿Cómo se mide eso?"*) |
| Cierres neutros ("Esperamos que os haya gustado") | Cierre ritual: "Eso es todo. / Os dejamos." + **P.D. opcional con upsell editorial** |
| Hooks improvisados | Hook deliberado de **5 tipos** (checklist explícita antes de escribir) |
| Cursiva/negrita por intuición | Negrita para **marcas y datos**, cursiva para **énfasis emocional y frases-gancho** |

**Estructura — lo que cambia:**

| Antes | Ahora |
|---|---|
| Cada artículo con estructura ad-hoc | 3 templates reproducibles seleccionables por parámetro |
| CTAs inconsistentes (a veces al final, a veces embebidos) | **CTA único** above-fold Y al final (patrón dual Cole/Bush) |
| Longitud variable | Objetivos claros: artículo ≥800 palabras · flash 500-1.000 · relato corto 1.500-3.000 |

**Ficción — nuevo eje completo:**

- Voz omnisciente o 1ª persona del personaje (excepción a la regla plural)
- Frases <20 palabras mediana, diálogo en raya (—), tiempo verbal consistente
- Dato real obligatorio anclado en cada relato
- Villano = problema humano, nunca el robot
- Personajes recurrentes con biblia canónica actualizada tras cada episodio

---

## 9. Beneficios inmediatos (los 5 más palpables)

1. **Banco perpetuo de semillas narrativas** — cada research-digest semanal alimenta el backlog Ficciones con 2-4 ganchos listos; ya no empiezas de cero cuando te apetece escribir ficción
2. **Welcome sequence de 4-5 emails** lista para implementar hoy en Beehiiv (como broadcasts segmentados, sin esperar a upgrade) — potencial alto lift en retención temprana
3. **3 templates de artículo reproducibles** — cortas el tiempo de borrador inicial porque la estructura ya está decidida antes de empezar
4. **Pilar "Ficciones Domésticas" operativo al 100%** — skill invocable, templates listos, flujo de calendario integrado, solo falta que rellenes la primera character-bible
5. **Biblioteca de 8 prompts probados** en español (Hustle Formula, Idea Generation, Pixar Spine, Paint The Villain, MRUs, Character Voice Checker, Voice capture, Category Of One) — cada uno adaptado a robótica doméstica

---

## 10. Qué te toca hacer para activar todo

### Obligatorio para lanzar Ficciones Domésticas (cuando quieras)

1. **Decidir primera serie:** slug, nombre, premisa, año in-universe, localización
2. **Copiar** `content/ficciones/_template-character-bible.md` → `content/ficciones/<tu-serie>/character-bible.md` y rellenar con al menos 2 personajes (voz, limitaciones, relaciones, guardarraíles)
3. **Copiar** `_template-arco-serie.md` → `<tu-serie>/arco-serie.md` con premisa global, tema humano, 5-8 episodios de trabajo
4. **Ejecutar** `/research-digest` una vez → poblará el backlog Ficciones con semillas automáticamente
5. **Invocar** `/ficcion-draft longitud=flash personajes="<los de tu bible>"` — el skill te ofrecerá 3 semillas del backlog

### Recomendado para consolidar voz

1. **Revisar** [`01-voz-y-estructura.md`](../references/writewithai/01-voz-y-estructura.md) una vez — aplicar los 3 hooks en español a los próximos 3 artículos conscientemente
2. **Probar** `/content-draft --template=<tipo>` en un artículo — ver si el borrador inicial requiere menos editing

### Recomendado para crecimiento (cuando llegues a 100+ subs)

1. Activar **welcome sequence** como broadcasts segmentados en Beehiiv (detalle en [`email-marketing-playbook.md §12`](../references/newsletter/email-marketing-playbook.md))
2. Crear **Master Content Library** en Beehiiv agrupando artículos por categoría (aspiradores / cortacésped / humanoides / reviews / editoriales / ficciones)
3. Añadir **CTA above-fold + final** en cada artículo a partir del próximo

---

## 11. Paywalls conocidos y cosas que quedaron incompletas

Write With AI es un newsletter de pago. El 70% de los artículos tiene paywall que corta antes del prompt decisivo. Esto está marcado honestamente en las fichas de `extractions/` con `[PAYWALL]` o `[PAYWALL — takeaway incompleto]`.

**Artículos cuyo prompt literal quedó tras paywall** (estructura inferida pero prompt específico no verificable):

- The 1 Chip Rule — 6 aperturas específicas no accesibles
- Category Of One — 7 prompts de niche-down truncados
- The 2-Year Test / Idea Machine 180 Days — templates completos tras paywall
- Voice Lab / Instant Writing Remixer — prompt de voice-cloning truncado
- The Automated Sales Machine (welcome sequence) — contenido tras 7-day trial
- Metaphor Maker, $1MM Evergreen, 6-Figure Prepper, Ultimate About Page — prompts literales tras paywall

Si en el futuro Rafael valora suscribirse a Write With AI ($20/mes), estos 10+ prompts literales son el mayor motivo. El resto (70% del valor estructural y de voz) ya está capturado.

---

## 12. Cross-references para navegar

### Docs ROBOHOGAR actualizados
- [`docs/brand-voice.md`](brand-voice.md) §11 "Aprendizajes de referencias externas"
- [`docs/plan-v2.md`](plan-v2.md) §10 "Growth tactics Fase 2-3"
- [`.claude/rules/editorial.md`](../.claude/rules/editorial.md) §"Narrativa especulativa"
- [`.claude/rules/newsletter.md`](../.claude/rules/newsletter.md) (tabla subject + 1-3-1)
- [`references/newsletter/email-marketing-playbook.md`](../references/newsletter/email-marketing-playbook.md) §12-15

### Skills (con cambios visibles)
- [`.claude/commands/research-digest.md`](../.claude/commands/research-digest.md) — paso 5 + 8b + handoff
- [`.claude/commands/content-draft.md`](../.claude/commands/content-draft.md) — templates + hook checklist
- [`.claude/commands/ficcion-draft.md`](../.claude/commands/ficcion-draft.md) — skill nuevo

### Content pilar ficciones
- [`content/ficciones/README.md`](../content/ficciones/README.md) — guía del pilar
- [`content/ficciones/_template-character-bible.md`](../content/ficciones/_template-character-bible.md)
- [`content/ficciones/_template-arco-serie.md`](../content/ficciones/_template-arco-serie.md)
- [`content/calendario-editorial.md`](../content/calendario-editorial.md) — slot + backlog

### Knowledge base externa
- [`references/writewithai/`](../references/writewithai/) — 8 archivos síntesis + 36 fichas + índice

---

<!-- wwai-integration-review 2026-04-17 · no committed yet -->
