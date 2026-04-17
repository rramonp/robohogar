# 05 — Prompts útiles (biblioteca operativa)

> Prompts literales de Write With AI extraídos + variantes ROBOHOGAR. Los prompts originales se conservan en inglés entre bloques de código porque están diseñados para ese idioma y traducirlos rompe comportamiento. Cross-refs: [voz](01-voz-y-estructura.md) · [estructura](02-estructura-articulo-visual.md) · [emails](04-email-newsletter-patterns.md).

## TL;DR

- **8 prompts núcleo** destilados: 3 completos literales (EIG Machine, ABC Method, Hook-Story-Offer) + 5 más con estructura conocida pero [PAYWALL] parcial.
- **Regla:** usar los prompts en inglés con Claude/ChatGPT, pedir output en español. Funciona mejor que traducir el prompt.
- **Mapear cada prompt a un skill ROBOHOGAR** — al final del documento, tabla de uso.
- Los 3 para probar primero (mayor ROI/riesgo): **EIG Machine, Customer Avatar (Jim Hamilton), Pinpoint Writing**.

---

## Prompt 1 · Idea Generation (EIG Machine)

**Fuente:** *Idea Generation On Autopilot* (Nicolas Cole, 135 likes). **Scrapeado completo, sin paywall.**

### Original (inglés)

```
I am going to train you to become an Endless Idea Generation Machine.

There are 4 primary types of content ideas:
- Actionable (Here's How)
- Analytical (Here's the Breakdown)
- Aspirational (I Did, You Can Too)
- Anthropological (Here's the Psychology)

Sub-topics within each:
Actionable: Tips, Tools, Hacks, Advice, Resources, Frameworks, Ultimate Guides, Curation
Analytical: Trends, Numbers, Reasons, Examples, Teardowns, Swipe Files
Aspirational: Lessons, Mistakes, Reflections, Personal Stories, Stories of Growth, Underrated Traits, Advice to Past Self
Anthropological: Fears, Failures, Struggles, Paradoxes, Observations, Comparisons, Why Others Are Wrong, Why You've Been Misled

I will give you:
- Topic
- FOR WHO (audience)
- SO THAT (desired outcome)

You generate 1 idea (as a specific headline) per sub-topic.
Rules: headlines in plain English, no marketing jargon, specific not vague, each headline must pass the "I'd click that" test.
```

### Variante ROBOHOGAR (ejecutable ya)

```
[Ejecuta el prompt original arriba, y añade al final:]

Topic: robótica doméstica (aspiradores, cortacésped, humanoides de servicio)
FOR WHO: adultos 30-55 años en España, intereses tecnológicos pero no ingenieros,
         con piso o casa media (50-120 m²), presupuesto 300-800 €
SO THAT: elegir qué robot comprar con confianza, sin leer 10 blogs en inglés,
         y disfrutar un contenido editorial bien escrito en español.

Output: genera las ideas COMO TITULARES en español (incluso si el prompt está en inglés).
Prioriza especificidad sobre generalidad: "Cómo limpiar bajo el sofá" > "Mejores robots".
```

**Output esperado:** ~30 titulares distribuidos en los 4 buckets. Banco de contenido para 2-3 meses.

---

## Prompt 2 · Hustle Headline Generator

**Fuente:** *The Hustle Newsletter Formula* (121 likes). Prompt completo sin paywall.

### Original (inglés)

```
You are a veteran writer for The Hustle newsletter. Your specialty is crafting
headlines that blend unexpected business angles, specific numbers,
and just enough mystery to compel the click.

I will give you: Topic + Recent Trend + Target Audience + Preferred Angle.

Generate 10 headlines using these 5 patterns (2 per pattern):
1. Unexpected Business Angle (hidden economics, counterintuitive take)
2. Contrarian ("Everyone thinks X, actually Y")
3. Hidden Story (behind-the-scenes, origin)
4. Question-based Mystery (open loop)
5. Superlative Twist (specific number, unusual comparison)

Rules:
- Conversational tone, not corporate
- Specific numbers over vague (prefer "$237" over "millions")
- One key idea per headline
- No clickbait, no CAPS, no emojis
```

### Variante ROBOHOGAR

Cambia "The Hustle newsletter" por "ROBOHOGAR newsletter" y "business angles" por "home robotics angles". Pide output en español. Ejemplos que debería generar:

- (Unexpected angle) *"La guerra secreta entre iRobot y Dreame que se libra en tus enchufes"*
- (Contrarian) *"Todo el mundo compra en Black Friday. Aquí un motivo para esperar a enero."*
- (Hidden story) *"El ingeniero español que diseñó el cepillo que ahora copian todos"*
- (Mystery) *"¿Cuánto cuesta de verdad un robot aspirador tras 3 años?"*
- (Superlative twist) *"Este robot de 249 € supera al flagship de 999 € en 4 de 7 pruebas"*

---

## Prompt 3 · Hustle Article Generator

**Fuente:** mismo artículo (121 likes). Sin paywall.

```
Write an article in the style of The Hustle:
1. Headline (use Headline Prompt pattern)
2. Subheading (one specific benefit or tease)
3. Opening anecdote: 2-3 first-person paragraphs, conversational
4. Context: 2-3 paragraphs with stats, trends, quotes
5. Body: thematic sections, 1-3-1 paragraph rhythm
6. Conclusion: circular (reference opening anecdote)
7. Tone: casual-informed, smart friend over coffee
```

**Variante ROBOHOGAR:** sustituir *The Hustle* → *ROBOHOGAR* y añadir: `First-person plural ("hemos", "os contamos"). Include at least one personal opinion. If mentioning a product include brand + model + EUR price. Close with a 1-line takeaway. Write in Spanish (Spain, "tú").`

---

## Prompt 4 · Article Writing Templates (Problem/Solution · Mistakes · How-To)

**Fuente:** *Article Writing Templates — The Shortcut* (124 likes). [PAYWALL en prompt definitivo; estructura inferida.]

```
Write an article using the [TEMPLATE] template.

[A] Problem/Solution: state problem → failed solutions → your solution steps
[B] Common Mistakes: 3-5 mistakes → consequence → how to avoid
[C] Step-by-Step: goal upfront → prerequisites → steps → troubleshooting

Input: Topic + Template letter + Target audience + Angle.
Output: 800-1200 words, 1/3/1 rhythm, 1 specific example per section,
close with action step.
```

**Variante ROBOHOGAR:** añadir `Write in Spanish (Spain). First-person plural. Include Pinpoint header as blockquote: "> Después de leer, [lector] sabrá [promesa] para [acción]". Reviews → B · Tutorials → C · Comparatives → A.`

---

## Prompt 5 · Jobs-To-Be-Done 5-part sequence

**Fuente:** *Jobs-To-Be-Done framework for writing newsletters* (86 likes). [PAYWALL parcial.]

```
Understand the Jobs-To-Be-Done my newsletter audience hires me for.
Newsletter: [name + 1-line description]. Topic: [broad]. Audience: [describe].

Generate 5 candidate JTBDs in format:
"When I [situation], I want to [motivation], so I can [outcome]."

For each JTBD:
1. Emotional state of the subscriber
2. 3 alternatives they currently use
3. What makes them "fire" those alternatives
4. What we must deliver to be "hired"
5. A content pillar (3-5 articles) that would serve that JTBD
```

**Variante ROBOHOGAR:** ya hicimos esto manualmente en [growth playbook](03-growth-playbook.md) §JTBD. Correr el prompt valida y añade ángulos.

---

## Prompt 6 · Headline formulas (How To X Without Y · 1-5-50)

**Fuente:** *5 Steps To Effortlessly Write A First Draft* (138 likes) + *The 1-5-50 Method* (45 likes).

```
Pattern A — How To X Without Y:
"Give me 25 headlines with pattern: How to {outcome} without {obstacle}.
 Audience: [describe]. Outcome: [specific]. Obstacles: [5 items].
 Rules: specific obstacles; concrete outcomes (€ or hours);
 include 5 variants swapping 'How to' for 'How I'."

Pattern B — 1-5-50 Method:
"Topic: [one topic].
 Step 1: 5 distinct 1-sentence hooks, each using different technique
 (metaphor, contrarian, stat, question, story fragment).
 Step 2: for the strongest hook, 10 variations. Total output: 50."
```

**Variante ROBOHOGAR:** añadir `Output in Spanish. Examples on home robotics (vacuums, mowers, humanoids, smart home).`

Ejemplos que generaría: *Cómo limpiar sin renunciar a los sábados · Cómo elegir robot sin gastarte 800 € · Cómo integré mi robot con HomeKit sin hub*.

---

## Prompt 7 · Voice capture (Voice Lab)

**Fuente:** *The Digital Writer's Voice Lab* (25 likes) + *Instant Writing Remixer* (67 likes). [PAYWALL parcial — estructura inferida.]

```
I want to train you on my writing voice.
Below are 5 samples of my published writing. Analyze and extract:
1. Average sentence length range
2. Vocabulary markers (frequent / avoided words)
3. Punctuation patterns (em-dashes, colons, ellipses)
4. Tone markers (humor, directness, formality)
5. Structural habits (paragraph rhythm, bold/italic use)

Samples:
<sample 1> [paste] </sample 1>
... (5 samples)

Then: produce a "voice rules" document I can paste at the start of every
future prompt to guarantee consistency.
```

**Variante ROBOHOGAR:** pegar 5 mejores artículos + `docs/brand-voice.md`. Guardar output en `docs/ai-voice-rules.md` y usarlo como prefix en todo prompt de generación.

**Bonus (Instant Writing Remixer):** *"Escribe como ROBOHOGAR mezclado con el rigor técnico de Wirecutter y el humor seco de David Sedaris."* — para explorar deriva sin romper voz base.

---

## Prompt 8 · Customer Avatar (Jim Hamilton) ⭐

**Fuente:** *How To Design A Winning Customer Avatar* (75 likes). Prompt scrapeado casi completo.

```
Today, you are a world-class marketing analyst with 20 years of experience.

Create a customer avatar for [OFFER].
Typical customer: [DESCRIBE demographics briefly].
They struggle with: [CORE PROBLEM].

Provide:
- Demographics (age, location, income, family)
- Psychographics (values, lifestyle, media habits)
- Values (explicit cares)

Then 5 examples of each:
- Pains (present)      - Fears (future)
- Frustrations         - Desires
- False Beliefs        - Trigger Moments (events that surface the pain)
- Painful Questions (never said out loud)

Finally:
- Core Problem (root cause) — give it a unique name
- Ultimate Desire (vision of solved future)
- Give this avatar a real first + last name

Format as a narrative profile, not a bullet list.
```

**Variante ROBOHOGAR:** ejecutar × 3 con perfiles **María** (42, Madrid, 2 hijos, alérgica), **Javier** (55, Valencia, padres mayores, chalet), **Laura** (35, Barcelona, freelance, piso 55 m², mascota). Output a `docs/customer-avatars.md`. Regla editorial: cada pieza debe poder responder *"¿A cuál de los 3 sirve?"*.

---

## Prompt 9 · Niche Creation / Category Of One

**Fuente:** *Category Of One* (67 likes) + *FOR WHO / SO THAT* (59 likes). [PAYWALL parcial.]

```
I want a "Category of One" niche — not "better than X".

My current positioning: [current]
Main alternative readers use: [competitor]

Generate 3 differentiation angles:
1. Different Problem — reframe of the usual problem
2. Different Solution — a mechanism no one else proposes
3. Different Audience — sub-segment ignored by incumbents

For each angle:
- 1-sentence positioning statement
- FOR WHO / SO THAT declaration
- Landing hero headline
- 5 content pillars that reinforce it
```

**Variante ROBOHOGAR:** input `Current positioning: Newsletter en español sobre robótica doméstica` + `Main alternative: traducir posts de The Verge / blogs generalistas`. Elegir uno de los 3 ángulos como rector 2026.

---

## Tabla · Prompts ↔ Skills ROBOHOGAR

| Prompt | Skill principal | Skill secundario | Cuándo ejecutarlo |
|---|---|---|---|
| 1 · EIG Machine | `/research-digest` | `/content-draft` | Trimestral (banco de ideas) |
| 2 · Hustle Headline | `/content-draft` | `/social-content` | Cada vez que se decide tema |
| 3 · Hustle Article | `/content-draft` | — | Por artículo (draft 1) |
| 4 · Article Templates | `/content-draft` | — | Por artículo (elegir esqueleto) |
| 5 · JTBD 5-part | — (manual) | `/research-digest` | 1 vez al año + revisión |
| 6 · Headline formulas | `/content-draft` | `/social-content` | Por artículo + por post social |
| 7 · Voice capture | — (manual) | — | Una vez, luego evergreen |
| 8 · Customer Avatar | — (manual) | `/research-digest` | 1 vez, revisar anual |
| 9 · Niche / Category Of One | — (manual) | — | Estratégico, anual |

---

## Aplicabilidad ROBOHOGAR concreta

**Orden de ejecución recomendado (próximas 4 semanas):**
1. **Semana 1:** Prompt 8 (Customer Avatar × 3) → `docs/customer-avatars.md`.
2. **Semana 1:** Prompt 7 (Voice capture) → `docs/ai-voice-rules.md`.
3. **Semana 2:** Prompt 1 (EIG Machine) → 30+ titulares → `content/calendario-editorial.md`.
4. **Semana 2:** Prompt 5 (JTBD) → validar/refinar [growth playbook](03-growth-playbook.md) §JTBD.
5. **Semana 3-4:** integrar Prompts 2-4-6 al skill `/content-draft` como plantillas seleccionables.
6. **Trimestral:** reejecutar Prompts 1 + 5 + 8 para ver deriva.
