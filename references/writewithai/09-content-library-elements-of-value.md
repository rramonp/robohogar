# 09 — Content Library & HBR 30 Elements of Value

> Framework operativo destilado de [*Build A Lead Generating Content Library*](https://writewithai.substack.com/p/build-a-lead-generating-content-library) (Nicolas Cole & Dickie Bush, 20-mar-2024). Complementa y convierte en ejecutable la táctica #2 de [03-growth-playbook.md](03-growth-playbook.md) ("Content Library HBR 30 Elements"). Cross-refs: [prompts útiles](05-prompts-utiles.md) · [análisis corto del PDF](extractions/short-form-posts.md#1-construye-una-biblioteca-de-contenido-que-genera-leads).

## TL;DR

- **Tesis Cole:** el objetivo no es "ir viral" sino construir una biblioteca que responda TODAS las preguntas del prospecto antes de que compre. Cada pieza = un lead-generation flywheel.
- **Framework:** HBR 30 Elements of Value (Bain & Co, 2016) en 4 niveles piramidales. Cada elemento dispara 2-3 preguntas específicas que un comprador real se hace → banco editorial enorme.
- **Workflow 3 pasos → 210 short-form posts en 30 días:** (1) brainstorm 90 preguntas con IA, (2) calendar de 30 días, (3) multiplicar cada pregunta × 7 templates.
- **Aplicabilidad ROBOHOGAR:** ejercicio no ejecutado aún. Una vez hecho produce 6-12 meses de backlog editorial (SEO evergreen + social).
- **Relación con Prompt 1 (EIG Machine) de [05-prompts-utiles.md](05-prompts-utiles.md#prompt-1--idea-generation-eig-machine):** EIG genera titulares por tipo de contenido (actionable/analytical/aspirational/anthropological); Elements of Value genera preguntas por dimensión de valor percibido. Son ortogonales y complementarios. Matriz ideal: 30 Elements × 4 EIG buckets = 120 ángulos posibles.

## Frase trigger para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Ejecutar el ejercicio | **"Retomamos content library — genera las 90 preguntas para ROBOHOGAR"** |
| Solo un elemento concreto | **"Genera 3 preguntas del elemento `Reduces Anxiety` para compradores de robot aspirador"** |
| Calendar 30 días | **"Con las 90 preguntas, arma el calendar de 30 días"** |
| Multiplicar × 7 templates | **"Para el día X del calendar, genera los 7 short-form"** |

## Los 30 Elements of Value (literal HBR)

Pirámide de 4 niveles, 30 elementos. Orden piramidal = mayor impacto emocional/de compra en niveles superiores, pero la base funcional es el prerrequisito.

### Nivel 1 — Functional (14 elementos)

| Elemento | Definición Cole |
|---|---|
| Saves Time | achieves something faster |
| Simplifies | makes some action or process easier |
| Makes Money | has monetary benefits |
| Reduces Risk | shown to be the safest choice |
| Organizes | helps you to organize something complex |
| Integrates | integrates different aspects of a process |
| Connects | connects with other people |
| Reduces Effort | helps you get things done with less effort |
| Avoid Hassles | reduces or avoids a problem |
| Cost Reduction | saves money in any monetary transaction |
| Quality | provides high-quality goods or services |
| Variety | provides a wide variety range |
| Sensory Appeal | appeals to one or several senses |
| Informs | provides reliable and trusted information |

### Nivel 2 — Emotional (10 elementos)

| Elemento | Definición Cole |
|---|---|
| Reduces Anxiety | helps you feel more secure and less worried |
| Rewards Me | provides benefits and special offers |
| Nostalgia | reminds you of something positive in the past |
| Design / Aesthetics | has a visually appealing form |
| Badge Value | represents a certain aspiration or status |
| Wellness | improves physical or mental state |
| Therapeutic Value | provides therapeutic well-being |
| Fun / Entertainment | offers some type of entertainment |
| Attractiveness | helps you feel more attractive |
| Provides Access | gives access to exclusive and valuable items |

### Nivel 3 — Life-Changing (5 elementos)

| Elemento | Definición Cole |
|---|---|
| Self-Actualization | provides a sense of personal accomplishment |
| Provides Hope | gives a sense of optimism about something |
| Motivation | helps you achieve a certain goal |
| Heirloom | seems like an investment for a future generation |
| Affiliation / Belonging | gives access to a community |

### Nivel 4 — Social Impact (1 elemento)

| Elemento | Definición Cole |
|---|---|
| Self-Transcendence | helps other people |

## Workflow de 3 pasos (Cole 2024, literal)

### Paso 1 — Brainstorm: 90 preguntas

Prompt literal Cole (inglés; lo usamos en inglés, pedimos output en español):

```
I'm writing about {TOPIC} for {TARGET AUDIENCE}.

Please create 3 questions for each element in the Elements Of Value Pyramid.

Be colloquial and ask each question as my target audience.

For reference, here's a list of the 30 Elements Of Value:

Level 1: Functional
- Saves Time: achieves something faster.
- Simplifies: makes some action or process easier.
- Makes Money: has monetary benefits.
- Reduces Risk: shown to be the safest choice.
- Organizes: helps you to organize something complex.
- Integrates: it's able to integrate different aspects of a process.
- Connects: connects with other people.
- Reduces Effort: helps you to get things done with less effort.
- Avoid Hassles: reduces or avoids a problem.
- Cost Reduction: saves money in any type of monetary transaction.
- Quality: provides high-quality goods or services.
- Variety: provides a wide variety range.
- Sensory Appeal: appeals to one or several senses.
- Informs: provides reliable and trusted information.

Level 2: Emotional
- Reduces Anxiety: helps you feel more secure and less worried.
- Rewards Me: provides benefits and special offers.
- Nostalgia: reminds you of something positive in the past.
- Design: has a visually appealing form.
- Badge Value: represents a certain aspiration or status.
- Wellness: improves physical or mental state.
- Therapeutic Value: provides therapeutic well-being.
- Fun: offers some type of entertainment.
- Attractiveness: helps you to feel more attractive.
- Provides Access: gives you access to exclusive and valuable items.

Level 3: Life Changing
- Self-Actualization: provides a sense of personal accomplishment.
- Provides Hope: gives you a sense of optimism about something.
- Motivation: help you to achieve a certain goal.
- Heirloom: it seems like an investment for a future generation.
- Affiliation: gives you access to a community.

Level 4: Social Impact
- Self-Transcendence: helps other people.
```

### Paso 2 — Calendar de 30 días

Prompt literal (concatenar al mismo chat de Paso 1):

```
Great, now take this list and turn it into a 30 day content calendar.

Please give me 1 question per day.

Everyday should be a different element of value.

Questions for the same element of value should not be used for consecutive days.

Give me the calendar in a table with the following columns: Day, Question, Element Of Value.
```

### Paso 3 — Multiplicación × 7 templates (210 short-form posts)

Prompt literal (concatenar al mismo chat). Sustituir `{X}` por el día del calendar que quieras desarrollar:

````
Great, now for day {X}, please answer the question 7 different ways using the 7 templates below.

# Writing Style
Write in a plain and simple tone. Be spartan.

# TEMPLATES =

## Template 1: The Benefits
Benefits of {Topic}:

{Benefit #1}

{Benefit #2}

{Benefit #3}

{Benefit #4}

Which is why {Topic} is so valuable.

## Template 2: Tips To Hang On Your Wall
3 {Topic} tips you should hang on your wall:

{Tip #1}

{Tip #2}

{Tip #3}

## Template 3: Reasons To Start
Here are {X} reasons why anyone struggling with {Problem} should start {Topic}:

{Reason #1}

{Reason #2}

{Reason #3}

{Reason #4}

I firmly believe this.

## Template #4: The Compounding Steps
Even if you are {Obstacle}, you can still:

{ActionStep1}

{ActionStep2}

{ActionStep3}

{ActionStep4}

{ActionStep5}

The barrier to entry has never been lower. And tiny steps compound over time.

## Template 5: Biggest Mistakes
The {X} biggest mistakes {Topic People} make:

{Mistake #1}

{Mistake #2}

{Mistake #3}

Let's fix them:

{Easy Solution #1}

{Easy Solution #2}

{Easy Solution #3}

## Template 6: Unforgettable Lessons
Unforgettable lessons after doing {Topic} for {X} years:

{Lesson #1}

{Lesson #2}

{Lesson #3}

{Lesson #4}

Learning these changed my life.

## Template 7: The Best Examples
The best examples of {Topic} I've ever seen:

{Example #1}

{Example #2}

{Example #3}

{Example #4}

What others would you add?
````

## Variante ROBOHOGAR — adaptación ejecutable

### Inputs fijos

- `TOPIC` = **robótica doméstica (aspiradores, friegasuelos, cortacésped, cocina, piscina, humanoides de servicio)**
- `TARGET AUDIENCE` = **adultos 30-55 años en España, interesados en tecnología pero no ingenieros, con piso o casa (50-120 m²), presupuesto 300-800 € por robot, viven con pareja/hijos/padres o mascota**

Invocación completa del Paso 1 (copia-pega en Claude):

```
[Paso 1 prompt arriba] +

Topic: robótica doméstica (aspiradores, friegasuelos, cortacésped, robots de cocina, robots de piscina, humanoides de servicio domésticos).
Target audience: adultos 30-55 años en España, interesados en tecnología pero no ingenieros, con piso o casa media (50-120 m²), presupuesto 300-800 € por robot, muchos con mascotas o niños pequeños.

Output: preguntas COMO las formularía un comprador real, EN ESPAÑOL (no inglés).
Usa "tú" (no "usted"). Tono coloquial — como lo preguntaría alguien en un grupo de WhatsApp.
Prioriza especificidad: mejor "¿puede subir el escalón del salón al pasillo?" que "¿es bueno en superficies irregulares?".
```

### Adaptación del Paso 3 (7 templates) a voz ROBOHOGAR ES

Los templates de Cole son en inglés y en primera persona singular. ROBOHOGAR usa **primera persona plural** ([editorial.md:26-33](../../.claude/rules/editorial.md)). Adaptación de los cierres:

| Template Cole (EN) | Cierre original | Adaptación ROBOHOGAR (ES) |
|---|---|---|
| 1. The Benefits | "Which is why {Topic} is so valuable." | "Por eso {Topic} nos parece imprescindible en un hogar actual." |
| 2. Tips On Your Wall | (sin cierre explícito) | "Tres pautas que nosotros tenemos siempre en mente." |
| 3. Reasons To Start | "I firmly believe this." | "Lo creemos firmemente." |
| 4. Compounding Steps | "The barrier to entry has never been lower. And tiny steps compound over time." | "La barrera nunca ha sido tan baja. Los pasos pequeños se acumulan." |
| 5. Biggest Mistakes | "Let's fix them: {3 soluciones}" | "Los resolvemos así: {3 soluciones}" |
| 6. Unforgettable Lessons | "Learning these changed my life." | "Entenderlas nos cambió la forma de mirar los robots domésticos." |
| 7. Best Examples | "What others would you add?" | "¿Qué otros añadirías?" |

Regla de oro: mantener tono coloquial, no vender, 1-3-1 rhythm, sin superlativos vacíos ([editorial.md §Reglas de contenido](../../.claude/rules/editorial.md)).

### Cuándo usar cada template

| Template | Encaja bien para | No encaja para |
|---|---|---|
| 1. Benefits | Reviews, comparativas | Editorial, opinión |
| 2. Tips On Your Wall | Tutoriales, mantenimiento | Reviews |
| 3. Reasons To Start | Conversión (por qué un robot aspirador) | Humanoides (aún no se compran) |
| 4. Compounding Steps | Onboarding, configuración progresiva | Noticias |
| 5. Biggest Mistakes | Reviews negativas, advertencias | Futuro/editorial |
| 6. Unforgettable Lessons | Editorial, primera persona plural larga | Tutoriales |
| 7. Best Examples | Comparativas multi-marca | Opinión subjetiva |

## Output esperado del ejercicio completo

Cuando Rafael invoque la frase trigger de arriba, Claude debe producir:

1. **Banco de 90 preguntas** (30 Functional × 3 + 30 Emotional × 3 + 15 Life-Changing × 3 + 3 Social Impact × 3) adaptadas a robótica doméstica en español, mapeadas a elemento y categoría de robot (aspirador / cortacésped / humanoide / etc.).
2. **Calendar de 30 días** opcional: una tabla Day / Question / Element que Rafael puede imprimir.
3. **Al pedirlo por días:** 7 short-form posts en español con los 7 templates adaptados.

Destino del output:
- El banco de 90 preguntas → nueva sección **"Banco de preguntas · Elements of Value"** en [`content/calendario-editorial.md`](../../content/calendario-editorial.md).
- Los 7 short-form generados por día → si se integra el flag `--templates=cole7` en `/social-content`, entrarían automáticamente al pipeline social. Mientras, se pegan manualmente en Buffer.

## Relación con otras tácticas ROBOHOGAR

- **[03-growth-playbook.md](03-growth-playbook.md) táctica #2 (Content Library HBR):** este archivo es la ejecución. Táctica marcada F1 🔥🔥🔥.
- **[05-prompts-utiles.md](05-prompts-utiles.md) Prompt 1 (EIG Machine) + Prompt 8 (Customer Avatar):** complementarios. Matriz: 30 Elements × 4 EIG buckets × 3 avatares (María/Javier/Laura) = cobertura editorial casi exhaustiva.
- **[`/social-content`](../../.claude/commands/social-content.md):** flag `--templates=cole7` pendiente de implementar (ver plan FASE F1 diferida).
- **[`/research-digest`](../../.claude/commands/research-digest.md):** ortogonal — el digest trae noticias reactivas; este framework llena el espacio evergreen.

## Referencia

- Artículo original Cole & Bush (sin paywall al momento del parseo): https://writewithai.substack.com/p/build-a-lead-generating-content-library
- Framework HBR: Almquist, E. et al., "The Elements of Value", *Harvard Business Review*, sept 2016.
- Análisis corto del mismo artículo en el archivo de extractions: [extractions/short-form-posts.md#1](extractions/short-form-posts.md#1-construye-una-biblioteca-de-contenido-que-genera-leads).
