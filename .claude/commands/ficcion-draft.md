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

### 🔴 REGLA ESTRUCTURAL — COMPONER EN ES DIRECTO, NO TRADUCIR (añadida 2026-04-20)

**Regla principal del pipeline, aplica a todos los pasos que generen prosa.**

La prosa del relato se compone **en castellano peninsular literario desde el primer token**. Prohibido pensar una frase en inglés y traducirla. Prohibido usar plantillas narrativas anglosajonas traducidas. La voz y la sintaxis se construyen en ES nativo.

**Heurística operativa cuando hay duda:**

- Si al escribir una frase surge duda sobre colocación (*"¿se dice así?"*), **descartar la frase entera y reescribirla desde cero** con sintaxis ES nativa. No parchear calco por calco — reestructurar.
- Si una frase necesita leerse dos veces para entenderse, es calco casi seguro. Reescribir.
- Si una palabra compuesta traducida (*"centro de X"*, *"sistema de Y"*) suena corporativa cuando el registro es doméstico, omitirla o nativizarla.

**Carga obligatoria de knowledge ES antes de escribir:**

1. Antes de la primera frase del paso 6 (prosa), **releer** [`@references/ficciones/castellano-literario-es.md §§ 3, 3.bis, 4`](../../references/ficciones/castellano-literario-es.md) (los 16 calcos a evitar + los 4 casos de estudio canónicos + los 12 recursos ES positivos). Activar estos patrones como guía de composición, no como checklist a posteriori.
2. Si durante la redacción se detecta vicio (frase que suena traducida), **volver a §§ 3 + 3.bis** antes de continuar. No acumular errores para corregir al final.

**Por qué esta regla existe:**

Incidente 2026-04-20: el relato `el-que-viene-a-tomar-cafe` v2 pasó las 25 validaciones automáticas del skill pero Rafael detectó leyendo dos frases básicas sin sentido (*"El centro de demostración fue en septiembre"* · *"vio la escena en boca de una actriz contratada para hacer de abuela"*) y ~10 casos más del mismo tenor (voz técnica de manual infiltrándose en prosa doméstica, pasivas anglo, colocaciones idiomáticas forzadas). La raíz no es falta de validación sino **método de composición**: el skill estaba traduciendo del inglés en vez de componer directamente en ES. Esta regla ataca la causa, no el síntoma. Los calcos 13-16 y los casos de estudio canónicos están en `castellano-literario-es.md § 3 + § 3.bis`.

---

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

### 0.5. Detectar categoría tonal — auto-balanceo del catálogo

Después de detectar modo, declarar **categoría tonal** del relato. Catálogo canon en [`@references/ficciones/tonalidad-y-mix-editorial.md`](../../references/ficciones/tonalidad-y-mix-editorial.md) — matriz objetivo:

- 🩻 **inquietante** — 40% (sello casa Black Mirror)
- 🪤 **radical** — 15% (extremo)
- 🤔 **ambiguo** — 25% (sin villano claro)
- 💚 **inspirador** — 10% (NO triste — criterio reforzado)
- 🍵 **mundano** — 10% (slice of life especulativo)

Subcategoría documentada: **inquietante-heavy** dentro del 40% inquietante (más cerca de radical sin llegar). Definida en `tonalidad-y-mix-editorial.md § 2.1`.

**Lógica de detección:**

1. **Si Rafael especifica tonal explícitamente** (`--tono=inquietante-heavy`, *"escribe una radical sobre X"*, *"algo ambiguo con Y"*) → usar esa.
2. **Si Rafael NO especifica tonal** → ejecutar **auto-balanceo**:
   - Leer [`content/registro-ficciones.md`](../../content/registro-ficciones.md) (catálogo histórico con `categoria-tonal` por relato — si no existe, crear con la entrada de *El operador nocturno*).
   - Calcular % real publicado por categoría sobre los últimos 12 relatos.
   - Identificar la categoría con mayor déficit en puntos porcentuales respecto a la matriz §1.
   - Proponer esa categoría como default y mostrar el cálculo a Rafael: *"Catálogo actual: inquietante 67% · radical 8% · ambiguo 8% · inspirador 0% · mundano 17%. Déficits: inspirador -10pp, ambiguo -17pp. Default propuesto: ambiguo. ¿Confirmas o sobrescribes?"*.
3. **Aviso de desviación:** si Rafael fuerza la misma categoría 3 veces seguidas (sobrescribiendo el default), avisar: *"el mix está desviado — categoría X lleva N% del catálogo, objetivo Y%. ¿Seguimos o equilibramos?"*.

**Default si no hay registro de catálogo:** inquietante (sello casa).

**Output del paso 0.5:** declarar `categoria-tonal` en variable de trabajo. Se inscribe en frontmatter del relato (paso de Output).

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

**Modulación por categoría tonal** (declarada en paso 0.5; detalle en [`@references/ficciones/tonalidad-y-mix-editorial.md § 4`](../../references/ficciones/tonalidad-y-mix-editorial.md)):

| Categoría tonal | Estructura | Tipo de cliffhanger | Densidad sensorial |
|---|---|---|---|
| 🩻 inquietante / inquietante-heavy | Spine completo + foreshadowing en acto 1 + revelación parcial en acto 2 | Emocional con elisión (alguien calla, borra, no cuenta) | Alta — detalles del cuerpo y el espacio |
| 🪤 radical | Spine acelerado + apertura cotidiana engañosa | Acto irreversible + alguien sigue como si nada | Media — la trama lleva el peso |
| 🤔 ambiguo | Spine bifurcado: dos posiciones igual de defendibles en acto 2 | Decisión tomada sin juicio narrativo | Media-baja — la cabeza del lector lleva el peso |
| 💚 inspirador | Spine suave + descubrimiento gradual | Gesto compartido o decisión que abre futuro. **Nunca cierre con muerte ni pérdida** (criterio anti-#16) | Alta — luz, gestos, pequeños actos |
| 🍵 mundano | 5-Sentence Story para flash | Cierre descriptivo plano sin promesa | Alta concentrada en 1-2 detalles especulativos |

### 3.5. Declarar `left-wall` + `big-lie` (antes del villano) — ORGÁNICO, NO OPCIONAL

**Este paso se ejecuta SIEMPRE, por defecto, sin que Rafael lo pida.** Antes de pasar al conflicto humano, el skill declara dos campos que se registran en 3 sitios a la vez:

- **`left-wall:`** — la restricción real/científica/regulatoria inviolable del relato. Lo que la realidad ES de 2030-2040 **sí dice** que es posible. Ejemplos: `"AI Act art. 6: humanoides domésticos son alto riesgo, requieren homologación CE"`, `"Aspirador 2033 sin brazos, LiDAR 360° solo superficies sólidas"`, `"Protocolo SAMUR Madrid real para ictus"`.
- **`big-lie:`** — la única licencia creativa mayor que el relato pide aceptar al lector (1 por relato, **no negociable**). Ejemplos: `"Humanoide refurbished accesible a familia media ES"`, `"Aspirador ha desarrollado modelo mental de rutinas humanas"`, `"Humanoide de cuidados diagnostica ictus 30s antes con sensores embedded"`.

**Regla de plausibilidad** (Adrian Tchaikovsky, *How I Write* 2025-12-31): *"You can get away with one big lie… but in order to support your one big lie, everything else needs to be true."* Todo lo que no sea el `big-lie` se verifica. Todo lo que contradiga el `left-wall` se elimina.

**Si el skill detecta 2 big lies** (p. ej. humanoide barato + memoria persistente ilimitada + habla 40 idiomas): o se recorta a uno, o se reescribe el concepto. No avanzar al paso 4 con 2 big lies.

**Registro en 3 sitios (obligatorio, sin pedir confirmación):**

1. **Frontmatter YAML** del relato (`YYYY-MM-DD-<slug>.md`): campos `left-wall:` y `big-lie:` rellenos.
2. **Bloque visible inmediatamente debajo del H1** del relato (antes del primer párrafo de prosa), con formato callout editorial para que Rafael lo vea al abrir el archivo y pueda cambiarlo antes de publicar:

   ```markdown
   # <Título del relato>

   > **Mentira grande:** <big-lie en una frase>.
   > **Muro izquierdo:** <left-wall en una frase>.
   > *Registradas por `/ficcion-draft` · cambiar antes de publicar si no encajan.*

   <primera línea del relato…>
   ```

3. **Reporte al chat tras generar el borrador** (paso 9): incluir explícitamente ambas declaraciones al mismo nivel que el resumen del relato. Formato canónico:

   ```
   ✓ Generado: content/ficciones/<serie>/YYYY-MM-DD-<slug>.md (<N> palabras)

   📌 Mentira grande elegida: "<big-lie>"
   🧱 Muro izquierdo: "<left-wall>"

   Resumen del episodio: …
   Villano humano: …
   Cliffhanger: …

   Si la mentira grande no encaja con lo que tenías en mente, dímelo antes de que generes siguiente episodio.
   ```

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

#### 5.5 Arquitectura lectora — declarar antes de expandir a prosa (OBLIGATORIO)

Antes de saltar al paso 6 (prosa), cargar [`@references/ficciones/arquitectura-lectora.md`](../../references/ficciones/arquitectura-lectora.md) y declarar, sobre el outline recién generado, tres decisiones estructurales de información. Son decisiones de outline — no se improvisan en prosa.

- **Anclaje de premisa (§1.1):** identificar los 1-3 hechos ficcionales clave que el lector debe registrar en los primeros 200 palabras para no descifrar mientras siente. Proponer una frase elíptica (no expositiva) para cada uno. Ejemplo canónico: *"Cinco años muerto y cada mañana en la cocina."* — ancla muerte del personaje sin explicarla.
- **Punto de mayor carga (§1.2):** marcar en el outline **cuál es el giro, revelación o pivote moral central** del relato. Debe haber uno, no más. Reservarle párrafo propio en prosa + micro-acción física (gesto, no pensamiento) del personaje procesándolo. Ejemplo canónico: el pulgar que se detiene sobre la pantalla, el móvil que se baja y se vuelve a subir.
- **Saltos temporales (§1.3):** enumerar los saltos de presente a pasado dentro de cada escena. Para cada uno, decidir marcador mínimo — punto y aparte, frase-bisagra de una línea sin glosa (*"El centro fue en septiembre."*), o anacoluto sintáctico. Sin glosa expositiva tipo *"al recordar…"* / *"Pilar pensó en…"*.

**Regla de parada:** si el outline no permite identificar con claridad el punto de mayor carga (§1.2), o si los 1-3 hechos clave no caben en frases elípticas tempranas (§1.1), volver a paso 4-5 antes de pasar a prosa. El arreglo de arquitectura cuesta 10 veces menos en outline que en prosa ya escrita.

Archivo vivo: los tres principios actuales nacen del feedback editorial 2026-04-20 sobre *El que viene a tomar café* v1. Si en futuras sesiones llega feedback nuevo que identifica otro patrón reproducible de arquitectura lectora, se añade a `arquitectura-lectora.md § 1.N` siguiendo su protocolo § 3 y se replica aquí la referencia al nuevo principio.

### 6. Expandir a prosa con MRUs — voz castellana literaria peninsular

**Antes de generar prosa, cargar OBLIGATORIAMENTE [`@references/ficciones/castellano-literario-es.md`](../../references/ficciones/castellano-literario-es.md) como contexto.** Este archivo es la base de la voz: 10 referentes ES contemporáneos con muestra textual (Urraca · Amat · Morales · Martínez · de la Cruz · Adón · Barba · Moreno · Mesa · Otero), 5 patrones transversales, 12 calcos EN→ES con alternativas literarias, 12 recursos ES positivos y checklist operativa. Origen: feedback Rafael 2026-04-19 sobre *El operador nocturno v1* — la prosa sonaba a traducción del inglés porque el skill no cargaba ningún modelo de prosa narrativa española literaria, solo frameworks universales (Pixar, MRUs, Paint The Villain).

Prompt MRU (reformulado en español, no inglés — la voz de generación debe ser ES desde el inicio):

```
Actúa como editor literario de prosa narrativa española peninsular contemporánea.

Te paso una frase del borrador. Tu tarea:
1. Predice las 3 preguntas que un lector tendría justo después de leerla.
2. Ordénalas por urgencia emocional (1 = la más urgente).
3. Para la pregunta #1, escribe la siguiente frase del relato que la responde,
   manteniendo la voz y el ritmo del input.

Voz de referencia: castellano peninsular literario contemporáneo
(referentes en `references/ficciones/castellano-literario-es.md` § 1).
- Si el POV está en interior de personaje vulnerable → registro Urraca/Adón
  (corporalización, contención poética, amenaza en subjuntivo).
- Si el POV es operativo o administrativo (call center, panel, app) →
  registro Cristina Morales: superponer voz personaje sobre el registro técnico,
  fricción de registros como motor narrativo. Nunca neutro/documental sin digerir.
- Si el POV es outsider observador (robot-narrador, tercero distante) →
  registro Lara Moreno *La menuda* + Sara Mesa: distancia no hostil, ironía,
  metáfora oculta en verbo.

Reglas de la prosa (todas obligatorias):
- Cuerpo como instrumento de exactitud: dramatizar emoción en gesto/objeto físico,
  no nombrarla (`sintió miedo` ❌).
- Elipsis como motor: si una frase explica algo que el lector podía inferir, recortar.
- Espacio doméstico activo: las cosas (cartón, descansillo, encimera) son trama, no decoración.
- Sin calcos del inglés: 0 posesivo redundante con cuerpo ("sus manos" → "las manos"),
  0 emoción nombrada antes de mostrada, 0 "de repente", 0 adverbios -mente acumulados,
  0 pasiva ser+participio, 0 conectores anglo ("sin embargo", "de hecho", "por supuesto"),
  0 pronombre sujeto explícito redundante. Lista completa: castellano-literario-es.md § 3.
- Recursos ES positivos: usar perífrasis verbales vivas (`se quedó mirando`,
  `lleva sin`, `acaba de`), voz media reflexiva, imperfecto modulador,
  oraciones nominales sin verbo principal en cierre rítmico, dativo ético.
  Lista completa: castellano-literario-es.md § 4.

POV: {pov}. Tiempo verbal: {tiempo verbal coherente con episodios previos}.

Frase de entrada:
{SENTENCE}
```

Reglas de prosa (obligatorias, condensadas del knowledge base):

- **Ritmo:** ratio orientativo 60% frases medias (12-25 palabras), 25% cortas (≤8), 15% largas (≥30). **Nunca 5 frases cortas seguidas** (ritmo metralleta = tell de Hemingway traducido). Nunca 3 largas seguidas.
- **Diálogo en raya española (—)**, no comillas. Cada personaje debe tener registro declarado (edad + lugar + clase + muletilla recurrente) antes de generar diálogo. Dos personajes no pueden hablar igual; test: tapar las acotaciones, ¿se distingue quién habla?
- **Nombres propios distinguibles fonéticamente entre personajes principales.** No nombrar dos protagonistas con la misma inicial + sílaba inicial parecida (ej. *Miguel* + *Martín* — ambos M+vocal cerrada o abierta + R/G; confunden tanto leyendo como en audiolibro TTS). Verificación pre-output: si dos personajes con líneas de POV o diálogo significativo comparten inicial, comprobar que la segunda sílaba diverge claramente (*Daniel* vs *Martín* OK · *Joel* vs *Martín* OK · *Miguel* vs *Martín* ❌). Origen: feedback Rafael 2026-04-19 sobre *El operador nocturno v1/v2* — Miguel/Martín se confundían en lectura y en TTS; renombrado a Joel Santos en v2 final. Excepción: si dos personajes secundarios o de fondo comparten patrón fonético, documenta el riesgo en PASOS.md y prioriza lectura/escucha de prueba.
- **Presente para inmediatez / pasado para reflexión.** No mezclar en la misma escena salvo justificación narrativa explícita (flashback marcado).
- **Cada 300-400 palabras**, una frase-gancho que reabra loop nuevo.
- **Hook de primera frase:** elegir de la tabla de `@references/writewithai/07-ficcion-y-narrativa-serializada.md § 5` (in medias res, objeto mundano crítico, diálogo cortado, etc.). Prohibido párrafo de orientación inicial estilo anglo (*"Era una mañana de abril en Madrid…"* ❌).
- **Tecnología digerida** (regla específica ROBOHOGAR): nunca término técnico sin caracterización del narrador o personaje. El robot debe tener mote afectivo en focalización interior de al menos un personaje (no solo *"el humanoide"* en todas las escenas). Detalle en `castellano-literario-es.md § 7`.
- **Anclaje genérico técnico — REGLA DEL BALANCE (`castellano-literario-es.md § 7.1`):** cada escena del relato debe contener **al menos 1 mención del término técnico genérico** correspondiente a la categoría editorial (`humanoide` · `aspirador` · `cortacésped` · `mascota-robot` · `fregasuelos` · `autómata` · `androide`). Esto preserva la coherencia con tags Beehiiv, llms.txt y el lector que llega desde el catálogo. Después del anclaje, libertad léxica POV (*aparato*, *bicho*, *cabrón*, *chisme*, *armatoste*) según registro del personaje. Verificación pre-output: `grep -c "<término-categoría>" <relato>` por escena → ≥1 cada escena.
- **Jerga sci-fi clásica permitida (`castellano-literario-es.md § 7.2`):** Asimov (*autómata*, *modelo*, *unidad*), Dick (*androide*, *réplica*, *simulacro*), Tchaikovsky (*espécimen*, *terminal*, *nodo*), genérico contemporáneo (*humanoide*, *unidad doméstica*, *asistente robótico*). Bienvenida en escenas corporativas, bocas de personajes técnicos, anclajes de género literario. Evitar en boca de personajes ajenos al sector (yaya, niño, padre madrileño) salvo justificación; respeta canon ROBOHOGAR (sin marcas comerciales reales en narrador).

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
- [ ] **Curse of knowledge en NARRADOR** (no en diálogo): acrónimos/jerga técnica del universo ficcional deben tener contexto mínimo la primera vez que aparecen en la voz del narrador. Ej: `"el LiDAR"` → `"el LiDAR, el láser que gira buscando muros"`. En diálogo se relaja — un personaje puede hablar técnico sin explicar, es verosímil. Ver `@rules/editorial.md § Curse of knowledge`.
- [ ] **SIN marcas comerciales reales en narrador.** 0 apariciones de `Dreame | Roborock | Ecovacs | Samsung | Cecotec | Xiaomi | iRobot | Roomba | Mova | Unitree | 1X | Figure | Agility | Apptronik | Neura | Sanctuary` en prosa/descripción/narrador. Permitido excepcionalmente en diálogo con parsimonia. Usar robots ficticios del canon ROBOHOGAR (Tico, Hugo, Eva, RONDA-3, MAIA) o categorías genéricas ("el aspirador", "el humanoide de cuidados"). Ver `@rules/editorial.md § Narrativa especulativa — SIN MARCAS COMERCIALES`.

Si hay violación en narrador → reescribir. Si es en diálogo → validar que sea verosímil, no tic del narrador infiltrado en la voz del personaje.

### 8.3. Anti-calco EN→ES en ficción narrativa — OBLIGATORIO antes de output

Cargar [`@references/ficciones/castellano-literario-es.md § 8 Checklist operativa pre-output`](../../references/ficciones/castellano-literario-es.md) y correr la checklist completa sobre el borrador.

**Verificación automática (grep patterns)** — los umbrales son orientativos para standalone (2.500-3.500 palabras); ajustar proporcionalmente para flash/episodio-serie:

```bash
# Calco 1 — posesivo redundante con partes del cuerpo
grep -E "sus (manos|ojos|piernas|brazos|labios|dedos|pies|hombros|rodillas|cabezas?|caras?)" <relato.md> | wc -l   # → meta 0

# Calco 3 — "de repente"
grep -ic "de repente" <relato.md>   # → meta ≤1

# Calco 4 — adverbios -mente
grep -oE "[a-záéíóúñ]+mente" <relato.md> | wc -l   # → meta ≤4 en standalone

# Calco 5 — pasiva ser+participio
grep -E "\b(fue|fueron|era|eran) [a-záéíóú]+ad[oa]s?\b" <relato.md>   # → revisar caso a caso

# Calco 7 — conectores anglo
grep -ic "sin embargo\|de hecho\|por supuesto\|en definitiva" <relato.md>   # → meta ≤1 cada uno

# ═══ PATRONES UNICODE-SAFE (cross-platform Windows/Linux/macOS) ═══
# IMPORTANTE: grep GNU bajo Windows+bash falla silenciosamente con clases [oó], [aá].
# Los patterns usan alternaciones literales (con-tilde|sin-tilde) en vez de clases Unicode.

# Calco 13 — sustantivos compuestos anglo "X center" (v3 · 2026-04-20 tarde)
grep -niE "(centro de (demostración|demostracion|llamadas|datos|servicio|atención|atencion|operaciones)|call center|data center)" <relato.md>   # → meta 0

# Calco 14 — expresiones "en [órgano] de [actor]" en contexto no-verbal
grep -niE "en (boca|ojos|cabeza|mano) de [^.]*(actriz|actor|personaje|humanoide|robot|máquina|maquina)" <relato.md>   # → revisar contexto

# Calco 15 — voz técnica de manual infiltrándose en narrador (v3 · ampliado)
grep -niE "\b(configuré|configuró|configuro|configura|configurado|configurada|registra|registró|registro|registrado|registrada|activó|activo|activa|activado|activada|ejecutó|ejecuto|ejecuta|módulo|modulo|input|output|backend|lanzó (la|una) (actualización|actualizacion)|cruzó con (los |las |el |la )?(datos|fotos|archivos|registros|imágenes|imagenes|perfiles|contactos|campos))\b" <relato.md>   # → revisar contexto · si está en narrador, sustituir por verbo doméstico

# Calco 16 — colocaciones idiomáticas forzadas
grep -niE "(de medio lado|a medio camino de|en el medio de)" <relato.md>   # → meta 0

# Calco 17 — microcopy UI anglo
grep -niE "(No, gracias|¿Estás seguro|¿Estas seguro|Enviar feedback|Aprender más|Aprender mas|Configuraciones|[Gg]ot it)" <relato.md>   # → meta 0 en UI/app

# Calco 18 — preposición espacial con objeto/persona en contexto no-espacial (v3)
grep -niE "\b(enfrente|en frente) (del|de la|de los|de las) (humanoide|robot|androide|autómata|automata|aparato|asistente|máquina|maquina|sistema|ordenador|teléfono|telefono|madre|padre|hijo|hija|hermano|hermana|usuario|cliente|cuidadora?|operadora?)" <relato.md>   # → meta 0

# Calco 19 — clarificación anglosajona "Es decir, X, y..." (v3)
grep -niE "\bEs decir, [^.,]{1,40}, y [a-z]" <relato.md>   # → revisar

# Calco 20 — inciso em-dash cerrando con ", y, " (coma obligatoria tras "y" · close third anglo · v3 refinado)
grep -niE "— [^—]{3,80} — y, " <relato.md>   # → meta 0 · reescribir con punto seguido o paréntesis

# Calco 21 — pasiva con dar/entregar a actor institucional (v3)
grep -niE "\bse (da|dio|daba|dan|dieron|daban) (al|a los|a las|a la) (tutora?|usuario|cliente|representante|sistema|responsable|cuidadora?|paciente|administradora?)" <relato.md>   # → meta 0 · reescribir con "se entrega/se concede al X"

# Calco 22 — frase relativa descriptiva en lugar de adjetivo/sustantivo ES idiomático (v5 · 2026-04-24)
# Origen: subtítulo "un botón que no hace ruido" en La objeción · validador no lo detectó porque patrón nuevo
grep -niE "(un[oa]?|el|la|los|las|este|esta|estos|estas|ese|esa|esos|esas) [a-záéíóúñ]+ que no (hace|se [a-záéíóúñ]+|para de [a-záéíóúñ]+|deja de [a-záéíóúñ]+|tiene [a-záéíóúñ]+)" <relato.md>   # → revisar caso a caso · si existe adjetivo/sustantivo ES más conciso (silencioso, mudo, perpetuo, callado, ciego), reescribir · si la relativa es deliberadamente literaria, defender
```

**Read-aloud test — último filtro obligatorio (añadido 2026-04-20):** si algún grep de los calcos 14 · 15 · 17 · 18 devuelve match ambiguo (imposible decidir con grep si es error o uso buscado), LEER LA FRASE EN VOZ ALTA o pasar por TTS ES peninsular. Si el oído tropieza — si hay que releer para entender — reescribir. El grep es el primer filtro; el oído nativo ES es el filtro definitivo.

**Verificación de presencia de recursos ES positivos:**
- ≥1 perífrasis verbal viva (`se quedó mirando`, `anda diciendo`, `lleva sin`, `acaba de`)
- ≥1 voz media reflexiva (`se le cayó`, `se durmió`, `se le quedó`)
- ≥1 coloquialismo peninsular en diálogo donde aplique al personaje
- ≥1 oración nominal sin verbo principal en posición de cierre rítmico
- Diálogo con al menos 1 muletilla, titubeo o anacoluto

**Verificación de espacio doméstico activo:**
- El hogar/escenario tiene ≥3 detalles concretos no decorativos (objetos con función narrativa)
- La tensión doméstica preexistente (lo que el robot va a revelar) está señalada antes de que el robot actúe

**Regla de decisión:** ≥4 fallos en checklist → reescribir el relato (no solo las líneas afectadas) · 1-3 fallos → reescribir los párrafos concretos · 0 fallos → proceder al paso 8.4.

Esta checklist complementa (no sustituye) la `anti-ia-checklist § 1 + § 2`. La diferencia: anti-ia-checklist cubre tics universales de prosa LLM (palabras como `tejer`, `tapiz`, `susurrar`); castellano-literario-es § 8 cubre los calcos específicos EN→ES de prosa narrativa que detecta el ojo del lector ES literario contemporáneo.

### 8.4 Second reader externo · `/validate-prose-es` — OBLIGATORIO antes de output (añadido 2026-04-20)

Los greps automáticos de 8.3 cogen calcos sintácticos específicos con patrones concretos (17 regex), pero NO cogen colocaciones ambiguas, registros mezclados, frases que requieren releer, o cualquier vicio léxico no previsto. Para eso existe el validador externo `/validate-prose-es`: un segundo lector sin contexto del proceso de generación que hace challenge mediante preguntas específicas a frases sospechosas.

**Invocación obligatoria y autónoma:** tras pasar 8.3 con 0 fallos, invocar `/validate-prose-es <path-al-md-del-relato>`. **El skill se ejecuta sin pedir autorización a Rafael** — es paso del pipeline, no decisión editorial. Saltarlo rompe el contrato del skill `/ficcion-draft`: si lo detectas saltado en generación previa, ejecutarlo inmediatamente sobre el relato pendiente. Rafael recibe el reporte como parte del output del draft. El skill ejecuta 3 fases (challenge · respuesta · veredicto) según [`@.claude/commands/validate-prose-es.md`](validate-prose-es.md).

**Qué hace el validador (sin acceso al proceso del generador):**

1. **Fase 1 · Challenge:** Agent Explore lee SÓLO el texto + el knowledge ES. Devuelve 5-15 preguntas específicas a frases sospechosas (colocaciones, registros, voz técnica).
2. **Fase 2 · Respuesta:** el generador (este skill) responde articulando la intención de cada frase cuestionada. Respuestas aceptables: referencia concreta al knowledge ES (*"cita del manual — fricción Morales §1.3"*, *"dativo ético del recurso ES §4 #7"*). Respuestas no aceptables: *"suena bien"*, *"es elegante"*, *"no sé"* — esas fuerzan reescritura.
3. **Fase 3 · Veredicto:** el mismo Agent clasifica cada respuesta y devuelve:
   - **READY** — proceder al paso 8.5.
   - **PENDING_FIXES** — aplicar los fixes de la tabla al `borrador.html` + `.md` en pasada atómica. Re-invocar `/validate-prose-es` una vez más. Si sigue PENDING, mostrar a Rafael.
   - **MAJOR_REWRITE** — BLOQUEAR output. Volver al paso 6 (prosa) con el reporte del validador.

**Por qué ojo fresco y no auto-auditoría:** el generador tiene sesgo estructural hacia las decisiones que ya ha tomado. El validador externo no comparte ese sesgo porque no ve el prompt, no ve `PASOS.md`, no ve el razonamiento. Es la lección del incidente 2026-04-20: el relato `el-que-viene-a-tomar-cafe` v2 pasó las 25 validaciones del propio skill pero Rafael detectó 10+ frases sin sentido al leer. El second reader es la defensa sistémica contra esto.

**Log:** cada invocación guarda reporte en `content/ficciones/<slug>/validator-reports/YYYY-MM-DD-report.md` (trazabilidad editorial permanente).

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
- [ ] **Pasa la checklist de [`@references/ficciones/castellano-literario-es.md § 8`](../../references/ficciones/castellano-literario-es.md)** — anti-calco EN→ES + presencia de recursos ES positivos + ritmo + espacio doméstico activo + voz por personaje + tecnología digerida. Si falla ≥4 ítems, reescribir el relato; si falla 1-3, reescribir párrafos concretos.
- [ ] **`categoria-tonal` declarada en frontmatter** (`inquietante` · `inquietante-heavy` · `radical` · `ambiguo` · `inspirador` · `mundano`) y **desenlace coherente** con la categoría según [`@references/ficciones/tonalidad-y-mix-editorial.md § 2`](../../references/ficciones/tonalidad-y-mix-editorial.md). Verificación específica:
  - Inquietante → final con elisión (alguien calla / borra / acepta en silencio); el lector cierra con nudo
  - Inquietante-heavy → vuelta de tuerca obligatoria que el lector solo entiende en escena final; territorio incómodo (manipulación íntima, voyeurismo coordinado, coerción suave) sin cruzar a violencia explícita
  - Radical → cierre irreversible + alguien sigue como si nada
  - Ambiguo → decisión tomada sin juicio narrativo; dos lecturas igualmente sostenibles
  - Inspirador → cierre positivo sin pena residual; **prohibido cerrar con muerte/duelo/pérdida** (criterio anti-#16: el inspirador-triste cae en inquietante disfrazado)
  - Mundano → cierre descriptivo plano sin promesa; ≥1 detalle especulativo 2030-2040 obligatorio
- [ ] **Arquitectura lectora — correr checklist de [`@references/ficciones/arquitectura-lectora.md § 4`](../../references/ficciones/arquitectura-lectora.md):**
  - **§1.1 Anclaje de premisa:** los 1-3 hechos ficcionales clave quedan registrables en los primeros 200 palabras mediante frase elíptica (no expositiva). Test: un lector que lee solo los primeros 3 párrafos, ¿sabe qué está pasando sin esperar al párrafo 5?
  - **§1.2 Ralentización del punto de mayor carga:** está identificado cuál es el giro central del relato (debe haber uno, no más); tiene párrafo propio, no embebido; hay micro-acción física (gesto, no pensamiento) del personaje procesándolo.
  - **§1.3 Bisagra en saltos temporales:** cada salto de presente a pasado dentro de una escena tiene señal mínima (punto y aparte / frase-bisagra de una línea sin glosa / anacoluto). Sin *"al recordar…"* ni *"Pilar pensó en…"*.
  - Archivo vivo: si tras el feedback pre-output Rafael identifica un patrón de arquitectura lectora no cubierto, se amplía `arquitectura-lectora.md` siguiendo su protocolo § 3 y se replica la nueva verificación aquí.

## Output — estructura obligatoria

### Archivos a generar

```
content/ficciones/<serie>/
  ├── YYYY-MM-DD-<slug>.md        ← el relato (Markdown con frontmatter)
  ├── YYYY-MM-DD-<slug>.html      ← versión HTML Beehiiv (opcional, si se va a publicar)
  ├── PASOS.md                    ← checklist de publicación + metadata SEO
  └── assets/
      └── hero-<slug>.png         ← hero still cinematográfico (opcional)

$HBX_VAULT/.../05-01_Robotica Newsletter/02-Drafts/Ficciones/
  └── <Título del relato> (audiolibro).md   ← copia optimizada para TTS (OBLIGATORIA, ver § Copia audiolibro)
```

**Reglas:**
- El `.md` del repo es la **fuente de verdad** para revisión y publicación (frontmatter, metadata, cursivas, comentarios HTML con dato-real y villano-humano).
- La copia audiolibro del vault es **mirror derivado** pensado exclusivamente para que Rafael escuche el relato en el móvil antes de publicar. Se regenera si el original cambia. No se publica nunca.

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
categoria-tonal: inquietante | inquietante-heavy | radical | ambiguo | inspirador | mundano
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

### Copia audiolibro para el vault Obsidian — OBLIGATORIA

Rafael escucha los borradores en el móvil antes de publicar (vía ElevenLabs Reader o TTS nativo) para detectar con el oído lo que los checkers no ven: ritmo, frases que tropiezan, diálogo que suena a guion. Esta copia es parte del entregable del skill — no opcional.

**Ruta exacta:**

```
$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/02-Drafts/Ficciones/<Título del relato> (audiolibro).md
```

- `$HBX_VAULT` se resuelve según la máquina (desktop=cri-c, laptop=bakal) vía la misma convención que el skill `/obsidian-robohogar`.
- Nombre: el título literario del relato + sufijo ` (audiolibro)`, sin fecha en el filename. Si ya existe, sobreescribir (la copia audiolibro es derivada del original, siempre refleja la última versión).

**Estructura del archivo (obligatoria):**

```markdown
---
tipo: ficcion-audiolibro
estado: borrador
duracion-estimada: <N> min a velocidad normal
palabras: <N>
voz-recomendada: es-ES neural — ElevenLabs Reader (Mateo o Valentina) · fallback TTS nativo iOS/Android
created: YYYY-MM-DD
fuente: content/ficciones/<serie>/YYYY-MM-DD-<slug>.md
---

# <Título del relato>

## Notas para narrarlo

<Breve nota 2-4 frases sobre cómo usar el archivo: qué se pronuncia cómo (frases en inglés, tagalo u otros idiomas del relato), cómo copiar el bloque de lectura. Se escribe a mano por relato — no es boilerplate.>

---

## Texto para escuchar — copia este bloque

`` ` `` `` ` `` `` ` ``
<PROSA COMPLETA DEL RELATO, TRANSFORMADA PARA TTS — ver reglas abajo>
`` ` `` `` ` `` `` ` ``
```

**Por qué bloque de código triple-backtick:** Obsidian renderiza todo bloque fenced con un botón *Copy* en la esquina superior derecha del bloque en Reading view. Rafael toca el botón una vez y tiene toda la prosa limpia en el portapapeles, lista para pegar en ElevenLabs Reader. Sin el bloque de código tiene que seleccionar manualmente desde el móvil, lo que es frágil y a menudo arrastra metadata.

**Transformaciones obligatorias sobre la prosa original para TTS:**

1. **Frontmatter YAML del original → fuera del bloque** (en la cabecera del archivo audiolibro como metadata propia). El bloque empieza en el título en prosa y termina con el "Fin." del relato.
2. **Blockquote `left-wall` / `big-lie` y comentarios HTML → fuera del bloque** (no se leen).
3. **Números de reloj a palabras** en castellano natural:
   - `03:14` → *"tres y catorce de la madrugada"*.
   - `09:23:47` → *"nueve horas, veintitrés minutos y cuarenta y siete segundos"*.
   - `12:06` → *"doce y seis del mediodía"*.
   - Regla: solo escribir en palabras si aparece en narrador; si es texto de pantalla o display (*"Time on-task: 09:23:47"*), también convertir porque el TTS lo leería como "cero nueve dos puntos dos tres".
4. **Siglas problemáticas suavizadas** en primera mención del narrador:
   - `LED` → *"piloto [color]"* / *"la luz"* según contexto.
   - `OCR` → *"sistema de reconocimiento óptico"*.
   - `Q1` / `Q2` → *"primer trimestre"* / *"segundo trimestre"*.
   - Años con dígitos (`2029`, `2033`) → palabras (*"dos mil veintinueve"*, *"dos mil treinta y tres"*).
   - `AI Act` → dejar (el TTS lo pronuncia decente); si el relato lo exige claro, *"el reglamento europeo de inteligencia artificial"* la primera vez.
   - Siglas que el TTS ES pronuncia bien (`IA`, `NEO`, `app`, `km`) → dejar.
5. **Cursivas `*texto*` → eliminadas.** TTS las ignora o las lee como guiones. Si el énfasis era crítico, reformular con orden sintáctico. Las comillas (`"`, `"…"`) sí se mantienen.
6. **Labels de UI en inglés con traducción → preferir la traducción** cuando el diegetismo lo permite. `Session ended` → *"sesión terminada"* (en narrador). Los rótulos que SON inglés en la escena (p. ej. cartel plastificado en un call center) se mantienen en inglés — es diegético.
7. **Diálogo en inglés diegético (traducido simultáneamente en la escena) → se mantiene en inglés.** Es parte del relato que el inglés suene extranjero; el TTS español con voz neural lo pronuncia aceptable y refuerza el tono. La traducción de la traductora aparece justo después en castellano.
8. **Palabras extranjeras puntuales (tagalo, japonés, etc.) → se mantienen** y se explican una vez en la sección *"Notas para narrarlo"* con pronunciación aproximada. No se escriben en fonética dentro del bloque; rompería la prosa.
9. **Separadores de escena (`---` + `## I.` del original) → sustituir por** una línea en blanco + *"Parte uno. <localización natural en palabras>."* / *"Parte dos. …"* / *"Parte tres. …"* al inicio de cada escena, como párrafo propio. Los dividers de markdown no se leen.
10. **Cierre:** el bloque termina con una línea *"Fin."* para dar pausa natural al narrador.

**Verificación pre-output del archivo audiolibro:**

- [ ] El bloque `` ```` ` ``` `` abre con el título del relato y termina con la palabra "Fin.".
- [ ] Ningún número en formato `HH:MM` dentro del bloque (`grep -E "[0-9]{2}:[0-9]{2}"` → 0).
- [ ] Ningún carácter `*` dentro del bloque (cursivas eliminadas).
- [ ] Ningún separador `---` dentro del bloque.
- [ ] Ninguna etiqueta frontmatter ni comentario HTML dentro del bloque.
- [ ] Al final del archivo (fuera del bloque), mensaje operativo: *"Copia el contenido del bloque anterior con el botón de copiar en la esquina superior derecha. Pégalo en ElevenLabs Reader con voz es-ES y escucha."*

**Regeneración:** al editar el original (`content/ficciones/<serie>/YYYY-MM-DD-<slug>.md`), la copia audiolibro queda desactualizada. `/post-publish` debe comprobar que la fecha de modificación de la copia audiolibro es ≥ que la del original antes de cerrar; si es menor, regenerar automáticamente. En fase previa a `/post-publish`, Rafael puede pedir *"regenera audiolibro de <slug>"* y el skill rehace solo esa copia sin tocar el original.

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
8. **`left-wall` + `big-lie` son obligatorios y orgánicos.** El skill los declara siempre, sin esperar a que Rafael los pida. Se registran en frontmatter YAML + bloque visible bajo H1 + reporte al chat. 1 big-lie por relato, no más. Si el paso 3.5 no se ha completado, no avanzar al paso 4.

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
  - **Tonalidad y mix editorial — sistema tonal canon (OBLIGATORIO, carga en paso 0.5):** `@references/ficciones/tonalidad-y-mix-editorial.md` — matriz 40/15/25/10/10, definición operativa por categoría, auto-balanceo del catálogo, criterio anti-triste para inspirador.
  - **Castellano literario ES — referentes peninsulares + calcos EN→ES + recursos positivos (OBLIGATORIO, carga en paso 6):** `@references/ficciones/castellano-literario-es.md`
  - **Arquitectura lectora — dosificación de información dentro de la escena (OBLIGATORIO, carga en paso 5.5 + checklist en paso 9):** `@references/ficciones/arquitectura-lectora.md`. Archivo vivo: admite nuevos principios y casos de estudio vía protocolo § 3.
  - Knowledge base completa frameworks universales: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`
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
