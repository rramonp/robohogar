# 10 · Fundamentals — 5 lecciones fundacionales de Write With AI

Destilado de los 5 emails fundacionales de Nicolas Cole ("Write with AI Lessons", abr 2026): ideación subatómica, validación, viralidad, principios de digital writing y long-form. Este archivo cubre **solo lo nuevo** respecto al resto de `references/writewithai/`. Lo ya destilado se referencia con enlace, nunca se copia.

## Qué hay aquí vs qué hay en otros archivos

| Concepto | Ya cubierto en | Aquí hay |
|---|---|---|
| FOR WHO / SO THAT · JTBD · EIG | [03-growth-playbook.md](03-growth-playbook.md) · [05-prompts-utiles.md](05-prompts-utiles.md) · [09-content-library-elements-of-value.md](09-content-library-elements-of-value.md) | Remisión |
| Hook-Story-Offer · 10 tipos de hooks · 1-3-1 | [01-voz-y-estructura.md](01-voz-y-estructura.md) · [05-prompts-utiles.md](05-prompts-utiles.md) | Remisión |
| 5 arquetipos de subject line | [04-email-newsletter-patterns.md](04-email-newsletter-patterns.md) · [extractions/subject-lines.md](extractions/subject-lines.md) | Remisión |
| Substack 5 patterns + templates Problem/Solution, Mistakes, How-to | [02-estructura-articulo-visual.md](02-estructura-articulo-visual.md) | Remisión |
| Tangibles como producto · pivote Cole 2026 | [08-paid-newsletter-blueprint-2026.md](08-paid-newsletter-blueprint-2026.md) · [`@rules/tangibles.md`](../../.claude/rules/tangibles.md) | Remisión |
| **4A Framework** (Analytical/Aspirational/Anthropological/Actionable) | — | § Lección 1 |
| **Atomic Essay** (250w como unidad de práctica) + trípode **WHO/WHAT/WHY** | — | § Lección 4 |
| **5 Headline Templates** (List · Story · Opinion · Question · Framework) | — | § Lección 4 + Tabla A |
| **5 Métodos de Expansión** (Reasons/Mistakes/Action Steps/Personal Story/Curated Examples) | — | § Lección 5 |
| **Outline as Content** + refinamiento V1→V5 | — | § Lección 2 |
| Lead-In + Main Points + CTA de Thread + prompt verbatim L3 | — | § Lección 3 |
| **Matriz de variedad editorial** (tablas A-F para romper monotonía) | — | § Matriz |

---

## Lección 1 — Idea subatómica y 4A Framework

Cole defiende que no escribes sobre un tema — escribes sobre **1 problema subatómico de alguien concreto**. Antes del primer token, fijar:

- Tema → formulación `FOR WHO [audiencia muy específica] SO THAT [outcome concreto]`. Regla y ejemplos: [`03-growth-playbook.md § JTBD`](03-growth-playbook.md).
- Ángulo editorial → uno de los 4 ángulos del **4A Framework**.

**4A Framework** — 4 formas de tratar el mismo tema. Elegir 1 dominante antes de escalar a estructura. Mezcla permitida solo si se declara en `PASOS.md` el dominante y por qué mezclas.

| Ángulo | Promesa al lector | Ejemplo ROBOHOGAR (mismo tema: robot aspirador para pisos <50m²) |
|---|---|---|
| **Analytical** | "Aquí está el análisis" | *"Cómo 3 marcas están resolviendo el problema del pelo largo en pisos pequeños ES: Dreame rediseña el rodillo, Roborock añade doble LiDAR, Ecovacs apuesta por IA de obstáculos."* |
| **Aspirational** | "Te enseño el estado futuro posible" | *"Vuelves a casa, el suelo está limpio, el robot ya ha dejado la estación lista. Esto es lo que compras hoy por 500 € si tu piso tiene <50m²."* |
| **Anthropological** | "Aquí está la psicología detrás" | *"El lector español de pisos pequeños compra aspirador robot por 2 razones que no coinciden con el americano: el vecino de abajo y el sonido del domingo por la mañana."* |
| **Actionable** | "Aquí cómo hacerlo — paso a paso" | *"3 cosas que decidir antes de comprar un aspirador robot si vives en <50m²: presencia de mascota con pelo largo, número de umbrales, si lavas o solo aspiras."* |

Regla: no cambiar de ángulo a mitad de artículo. Los 4 ángulos del mismo tema son 4 artículos distintos, no 4 secciones del mismo artículo.

---

## Lección 2 — Validar antes de expandir

Dos ideas que encajan mal con F1 (0-50 subs ROBOHOGAR) y se adaptan:

**Subatomic Idea · V1→V5** — refinamiento iterativo de la idea hasta que no puedas ser más específico.

```
V1 "escribo sobre domótica"
V2 "escribo sobre robots aspirador"
V3 "escribo sobre robots aspirador en pisos pequeños"
V4 "escribo sobre qué preguntar antes de comprar un robot aspirador para un piso <50m²"
V5 "escribo sobre las 3 preguntas que evitan que un aspirador robot decepcione en un piso <50m² con perro de pelo largo"
```

Regla: si el tema todavía cabe en la página de categoría de Amazon, no es subatómico.

**Outline as Content** — Cole publica el outline (lista) antes de expandir a long-form para validar con la audiencia cuál lista merece convertirse en artículo. Adaptación ROBOHOGAR F1 (sin audiencia social): el **backlog editorial** en `content/calendario-editorial.md` hace de mercado interno. Un tema que sobrevive al digest (el ángulo resiste 1 semana entre otros candidatos) vale artículo; si no sobrevive, vuelve al pool B.

---

## Lección 3 — Thread: Lead-In + Main Points + CTA

Estructura Cole del thread de Twitter (X), portable a thread de LinkedIn y a carrusel IG. Este archivo es referencia; el enganche operativo a `/social-content` queda fuera de alcance por ahora.

- **Lead-In Tweet:** 1 sola frase gancho. Sin hashtags, sin emojis, sin "thread 🧵". Debe abrir un loop que solo se cierra leyendo abajo.
- **Main Points:** 3-5 bullets, cada tweet **standalone** (legible sin contexto de los otros). Mismo número de tweets que de puntos del outline.
- **CTA:** 1 sola llamada al final. Suscribirse al newsletter, leer el artículo largo, responder una pregunta. Nunca 2.

Reglas duras Cole: ≤280 chars por tweet, sin hashtags, sin emojis, cada tweet legible por sí mismo si lo encuentras suelto en el timeline.

**Prompt verbatim de L3** (EN original — Cole lo deja literal para pegar en GPT):

```
I am going to train you to write a Twitter Thread.

A Twitter Thread has 3 parts:
1. The Lead-In Tweet (Hook)
2. The Main Points
3. The Call-To-Action (CTA)

Rules:
1. Make each tweet stand alone (280 characters or less)
2. Do not use hashtags and emojis. Ever.
3. Write 1 sentence for the Hook.
```

Adaptación ES obligatoria al usarlo: mantener reglas estructurales; adaptar voz al plural editorial ("hemos"), reglas [`@rules/editorial.md § Apertura y cierre`](../../.claude/rules/editorial.md) (no *"Hey"*, no *"Querido lector"*), subject-line [`@rules/newsletter.md`](../../.claude/rules/newsletter.md) (≤45 chars, preferencia ≤35).

---

## Lección 4 — Atomic Essay + 5 Headline Templates + WHO/WHAT/WHY

**Atomic Essay** — unidad de práctica deliberada: 1 idea, 250 palabras, los 5 elementos del digital writing aislados para masterizar uno a uno (headlines · introductions · main points · rhythms · conclusions). No se aplica al output de ROBOHOGAR (los artículos son >800w); se cita como metodología para afilar una dimensión específica fuera de un artículo real.

**Trípode WHO / WHAT / WHY** — todo headline necesita los 3 a la vez:

- **WHO** — audiencia nombrada (yoga teachers, renters, padres con mascotas, propietarios de pisos pequeños).
- **WHAT** — el objeto concreto (3 tips, 5 errores, una checklist, una razón, una fórmula).
- **WHY** — el outcome que el lector gana (ahorrar tiempo, no equivocarse, decidir en 10 min).

Si el titular tiene solo 2 de los 3, es tibio. Si tiene los 3, se lee.

**Tabla A · 5 Headline Templates × ejemplo ROBOHOGAR (respetando `@rules/seo.md` ≤55 chars y `@rules/editorial.md § Honestidad`):**

| Template | Cuándo | Ejemplo ROBOHOGAR |
|---|---|---|
| **List** | Comparativas, guías con finalistas contables | *"6 robots aspiradores 2026 para pisos con mascotas"* |
| **Story** | Reviews con ángulo de decisión, editoriales | *"Así elegimos el aspirador definitivo en 2 semanas"* |
| **Opinion** | Editorial contrarian, tesis fuerte | *"Por qué el humanoide doméstico no llega en 2026"* |
| **Question** | Artículos de decisión, dudas frecuentes | *"¿Vale la pena el robot fregasuelos con vapor?"* |
| **Framework** | Guías paso a paso con método con nombre | *"10 preguntas antes de comprar un aspirador robot"* |

**Tabla B · Subtítulo · 3 variantes** (el subtítulo cumple `@rules/tangibles.md § Promocionar el tangible en subtítulo`):

| Variante | Ejemplo |
|---|---|
| **Cifra + tangible** (default Cole-Bush) | *"6 finalistas, 3 perfiles y una checklist de 10 preguntas para no equivocarte al comprar."* |
| **Pregunta-gancho** | *"¿Cuál ganaría si tu piso tiene <50m² y perro de pelo largo? Esta es la única comparativa que separa los 6 por perfil real."* |
| **Afirmación provocadora** | *"El más vendido no es el mejor. Y el más caro, tampoco. Seis finalistas y una regla de descarte que resuelve el 80%."* |

Regla: el subtítulo debe ser leíble en OG card sin contexto. 120-180 chars orientativo.

---

## Lección 5 — Pillar Blog = 5 Atomic Essays + 5 Métodos de Expansión

Cole: un pillar blog de ~1500-2000w no se escribe de una vez, se compone de 5 atomic essays (250w × 5 = 1250w + transiciones + cierre).

**5 Métodos de Expansión** — cómo desarrollar CUALQUIER `<section>`. El método dicta el tipo de contenido de esa sección.

| Método | Qué mete en la sección | Ejemplo ROBOHOGAR (sección "Criterios de selección" aspirador 2026) |
|---|---|---|
| **Reasons** | 3-5 porqués de la tesis | *"Priorizamos 3 criterios porque en pisos ES <70m² son los únicos que mueven la aguja: succión suficiente para pelo de mascota, fregado que no moje el parqué, estación que no haga ruido a las 07:00."* |
| **Mistakes** | Qué hace mal el lector sin esta guía | *"3 errores que detectamos en reviews internacionales: comprar por succión sin mirar el rodillo, ignorar el nivel sonoro de la estación, fiarse del precio de salida sin revisar Amazon ES en 2 semanas."* |
| **Action Steps** | Paso 1 / 2 / 3 accionables | *"Paso 1: medir m² reales. Paso 2: contar umbrales. Paso 3: decidir si lava o solo aspira. Con esas 3 respuestas, 4 de los 6 finalistas caen solos."* |
| **Personal Story** (reinterpretado para ROBOHOGAR) | Análisis editorial **real** del equipo, NUNCA experimento físico inventado | *"Comparamos 14 modelos y descartamos 8 tras cruzar ficha oficial + 3 reviews internacionales. Los 6 que quedan son los que resisten al filtro."* |
| **Curated Examples** | 2-3 citas externas que refuerzan | *"Vacuum Wars llegó a la misma conclusión sobre el rodillo antienredos del Dreame X50 Ultra; Xataka Home confirma que el Roborock Qrevo Curv 2 sube umbrales de 3 cm."* |

**Caveat crítico ROBOHOGAR**: `Personal Story` **nunca** es *"lo probé en casa"*, *"lo escuché"*, *"lo medí"*. Es análisis real del equipo editorial sobre información pública. Regla dura: [`@rules/editorial.md § Honestidad de primera persona`](../../.claude/rules/editorial.md).

Regla de composición: **no repetir método en secciones contiguas**. Si las secciones 1 y 2 son Reasons + Reasons, aburren. Reasons + Mistakes + Action Steps + Curated Examples + Personal Story varía ritmo y tipo de contenido.

---

## Matriz de variedad editorial ROBOHOGAR

Herramienta operativa que `/content-draft § 1 bis` carga para romper monotonía. Seis tablas + reglas de anti-repetición.

**Tabla C · Longitud buckets**

| Bucket | Palabras | Nº H2 | Cuándo |
|---|---|---|---|
| **Flash** | 600-900 | 3 | Editorial reactivo sobre noticia concreta · explicativo de concepto · opinión corta |
| **Medio** | 1000-1500 | 4-5 | Review de 1 producto · editorial de tesis · guía paso a paso corta |
| **Largo** | 1800-2500 | 5-6 | Comparativa de 3-5 productos · guía de compra categoría · editorial profundo |
| **Pillar** | 2500+ | 6-7 | Guía evergreen "X 2026" con finalistas · análisis de mercado · ebook capítulo |

**Tabla D · Tangible equivalente** (rota según anti-repetición; `@rules/tangibles.md` ya permite sustitución)

| Tangible | Formato | Encaja en |
|---|---|---|
| **Checklist accionable** (3-7 ítems) | Callout crema + borde ámbar | Reviews, comparativas, guías de compra |
| **Decision tree mini** (4-6 bifurcaciones) | Árbol de preguntas "si sí / si no" | Guías de decisión rápida |
| **Dossier "3 datos clave"** | 3 cifras destacadas con fuente | Editoriales con tesis de mercado |
| **Cuadro qué-sí / qué-no** | 2 columnas confrontadas | Antipatterns · "qué no comprar" |
| **Tabla comparativa standalone** | Tabla ≤4 cols con ganador marcado | Comparativas con ≥3 productos |

**Tabla E · 6 cierres**

| Cierre | Estructura | Ejemplo detonante |
|---|---|---|
| **Checklist + CTA** | Checklist final + banner newsletter | *"5 preguntas antes de comprar · [banner]"* |
| **Veredicto suelto** | 2-3 frases de posición editorial, sin checklist | *"Si vives en <50m², el Dreame. Si tienes jardín, ninguno todavía. Volvemos en 6 meses."* |
| **Pregunta abierta** | Pregunta directa al lector | *"¿Qué suelo tienes tú? Respóndenos al email — ajustamos el siguiente artículo a lo que nos contéis."* |
| **Manifiesto** | Posición editorial punzante 3-5 frases | *"ROBOHOGAR no recomienda ningún humanoide doméstico en 2026. Ninguno. Volveremos cuando alguno cueste menos que un coche y funcione sin wifi."* |
| **Tabla-resumen** | Tabla final como último bloque, sin prosa de cierre | Tabla comparativa con columna "Veredicto" rellena |
| **Mínimo solo banner** | Solo banner CTA, sin prosa | Para flash bucket donde el cuerpo ya entregó |

Nota: el snippet canónico de banner CTA suscripción (`@rules/newsletter.md § Snippet canónico`) se inserta SIEMPRE al final. Varía **solo la prosa que lo precede**.

**Tabla F · Reglas de anti-repetición** (checkables contra los últimos N `PASOS.md`)

| Dimensión | Regla dura |
|---|---|
| Headline template | No repetir la misma template en 2 de los últimos 3 artículos. En ventana de 5, ≥3 templates distintas |
| Ángulo 4A | No repetir el mismo 4A en 2 de los últimos 3. En ventana de 5, ≥3 ángulos distintos |
| Subtítulo variante | No repetir la misma variante en 2 de los últimos 3 |
| Longitud bucket | Máximo 2 artículos consecutivos del mismo bucket |
| Tangible | No repetir el mismo tangible en 2 de los últimos 3 |
| Cierre | No repetir el mismo cierre en 2 de los últimos 3 |
| Nº de H2 | Escala con bucket (flash 3 · medio 4-5 · largo 5-6 · pillar 6-7). No clonar el nº exacto del artículo anterior |
| Método de expansión | Prohibido repetir método en secciones contiguas del mismo artículo |

**Cómo aplica el skill**: `/content-draft § 1 bis` lee los últimos 5 `PASOS.md` de `content/articulos/*/PASOS.md`, extrae los 6 campos editoriales y computa una tabla diff antes de decidir el combo del artículo nuevo. Si una dimensión colisiona con los últimos 3, fuerza cambio. Las decisiones se declaran en `PASOS.md § Decisiones editoriales` para que el siguiente artículo las pueda leer.

---

## Mini-mapa · si buscas otra cosa

- Subject lines + welcome sequence + CTAs → [`04-email-newsletter-patterns.md`](04-email-newsletter-patterns.md)
- Hook-Story-Offer + 10 tipos de hooks + 1-3-1 → [`01-voz-y-estructura.md`](01-voz-y-estructura.md)
- JTBD + FOR WHO/SO THAT + growth tactics → [`03-growth-playbook.md`](03-growth-playbook.md)
- Substack 5 patterns + plantillas Problem-Solution · Mistakes · How-to → [`02-estructura-articulo-visual.md`](02-estructura-articulo-visual.md)
- Prompts literales ejecutables (EIG Machine, ABC, Hook-Story-Offer, Customer Avatar, Pinpoint) → [`05-prompts-utiles.md`](05-prompts-utiles.md)
- HBR 30 Elements of Value + idea matrix → [`09-content-library-elements-of-value.md`](09-content-library-elements-of-value.md)
- Paid newsletter blueprint (F3 paywall) → [`08-paid-newsletter-blueprint-2026.md`](08-paid-newsletter-blueprint-2026.md)
- Tangibles como producto (pivote Cole 2026) → [`@rules/tangibles.md`](../../.claude/rules/tangibles.md)
- Anti-IA checklist universal + ficción → [`@references/anti-ia-checklist.md`](../anti-ia-checklist.md)
- Prosa editorial ES (no-ficción) + microcopy + social → [`references/editorial-es/`](../editorial-es/)
