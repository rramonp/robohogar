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
| Exploración pre-escritura (pitch) | **`/ficcion-draft pitch <semilla>`** · *"cuéntame más sobre X"* · *"explora el pitch de X"* · *"desarrolla X"* | `pitch` |
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
| `pitch` | NO genera prosa. Devuelve **pitch canónico de exploración** (template descrito en "Modo `pitch` — formato canónico de exploración" al final del doc). Rafael lee, elige entre variantes ofrecidas por bloque, y luego reinvoca otro modo (`one-shot`/`serie`/`piloto`) con la semilla refinada. Saltar pasos 2-9; solo ejecutar paso 0 (detectar modo) + 0.5 (declarar tonal) + bloque pitch. Output: chat + opcionalmente guardar en `content/ficciones/_pitches/<slug>.md` si Rafael lo pide. |
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

### 5.6 Variability gate — OBLIGATORIO antes de prosa (regla dura 2026-04-26 PM, bloqueo duro)

**Por qué este paso existe.** Auditoría 2026-04-26 sobre 9 relatos detectó: copy-paste literal de párrafo entero (cafetera+geranios+luz) entre *El que viene a tomar café* y *El chaval*; 14 tropos saturados (gestos, símiles, frases-fórmula, setting clichés); 66% del catálogo en mismo conflicto humano (duelo+demencia+soledad-cuidadora); 77% en mismo POV; 67% en misma postura humanoide. Cita Rafael: *"No digo la forma o la composición, sino directamente copy-paste. Esto es inviable."* La regla cumple su objetivo: *"Lo que haga falta para que esto no vuelva nunca a ocurrir."* Detalle completo en memoria `feedback_ficcion_anti_self_plagio.md` y plan `se-han-utilizado-recursos-scalable-duckling.md`.

**Lógica del gate — bloqueo duro.** Antes de avanzar al hook (5.7) y a prosa (6), el skill ejecuta este paso obligatoriamente sobre el outline declarado en pasos 4-5.5.

**1. Leer registro estructural** ([`content/registro-ficciones.md`](../../content/registro-ficciones.md)) — tomar las **5 filas más recientes** (publicados + drafts pre-pub combinados, ordenados por fecha) y extraer 4 columnas:
- `Perfil POV` (edad±5 + género + relación familiar dominante)
- `Setting` (ciudad + momento del día + objeto-testigo central)
- `Conflicto humano` (uno o dos canónicos del catálogo)
- `Cliffhanger tipo` (uno del catálogo)

**2. Leer registro de tropos quemados** ([`references/ficciones/tropos-quemados.md`](../../references/ficciones/tropos-quemados.md)) — tomar la lista de tropos en estado 🔴 QUEMADO (≥2 usos en últimos 5 relatos).

**3. Calcular ejes saturados.** Reportar al chat:

```
🔴 Ejes saturados en últimos 5 relatos:
- Perfil POV: <N>/5 son <perfil dominante> → próximo NO puede ser ese perfil
- Setting: <N>/5 son <triple dominante> → próximo en otra combinación
- Conflicto humano: <N>/5 giran en <conflicto dominante> → próximo en otro vector
- Cliffhanger: <N>/5 cierran con <tipo dominante> → próximo en otro tipo
- Tropos quemados activos: <lista de los 🔴 con ventana de enfriamiento aún activa>
```

**4. Validar el outline contra los 4 ejes.** Para cada eje, comparar el valor del outline declarado con el conjunto `ejes_saturados`:

| Eje | Resultado | Acción |
|---|---|---|
| `Perfil POV` ya está en últimos 5 | ❌ BLOQUEO | Volver a paso 4 (Paint The Villain / outline) — cambiar protagonista a perfil distinto |
| `Setting` triple ya está en últimos 5 | ❌ BLOQUEO | Cambiar al menos uno de los tres componentes (ciudad / hora / objeto-testigo) |
| `Conflicto humano` principal ya está en últimos 5 | ❌ BLOQUEO | Reformular el conflicto desde otro vector canónico |
| `Cliffhanger tipo` ya está en últimos 5 | ❌ BLOQUEO | Cambiar el cierre antes de prosa |
| Algún tropo 🔴 QUEMADO planeado para el outline | ❌ BLOQUEO | Reescribir el outline sin ese tropo |

**Excepción única — sello de serie declarado:** una serie puede mantener un eje fijo (ej: serie epistolar siempre POV-1ª-confesional) si está declarado explícitamente en su `arco-serie.md` como sello editorial. Sin declaración escrita previa al relato, no aplica la excepción.

**5. Si todos los ejes pasan → continuar a paso 5.7 (hook).** Si alguno falla → reportar a Rafael:

```
❌ Variability gate FALLIDO en N ejes:
- <Eje>: <valor outline> ya está en últimos 5 (<relatos>) → propuesta de cambio: <X>
...

¿Cambio el outline a <X>, o documentas excepción de serie en arco-serie.md?
```

Si Rafael confirma cambio → re-ejecutar paso 5.6 sobre el outline corregido. Si Rafael documenta excepción de serie → registrarla y avanzar.

**6. Anti-tropos canónicos como sugerencia inspiradora.** Si los 4 ejes están en saturación grave (la lista canónica está agotada), `tropos-quemados.md § 5` lista los anti-tropos del universo: POVs no explorados, settings no usados, conflictos sin tocar, cliffhangers nuevos. Sugerir a Rafael 2-3 combinaciones de la lista anti-tropos para inspirar el siguiente outline.

**7. Registrar la decisión.** El paso de Output del skill (al cerrar el relato) actualiza `content/registro-ficciones.md` con los 4 valores estructurales del nuevo relato + actualiza `tropos-quemados.md` con las 5-10 figuras dominantes detectadas.

### 5.6.bis Saturación de catálogo de voces — sub-paso del Variability gate (canonizado 2026-04-26 PM)

**Por qué este sub-paso existe.** El catálogo de referentes en [`@references/ficciones/castellano-literario-es.md § 1 + § 1.bis`](../../references/ficciones/castellano-literario-es.md) tiene 17 autores. Si el skill siempre carga los mismos 3-4 (Urraca/Adón/Mesa para inquietante, Vilas para popular, Chirbes para radical), aunque los 4 ejes estructurales de § 5.6 pasen, la **voz** de los relatos converge igual. El feedback Rafael 2026-04-26 PM lo pidió explícitamente: *"si te das cuenta de que se está quedando corto el número de autores españoles que hay dentro de Castellano literario es, sugiéreme aumentar el registro en más autores."*

**Ejecutar siempre tras el Variability gate (§5.6) y antes del hook (§5.7).**

**1. Leer columna `Referente principal`** de [`content/registro-ficciones.md`](../../content/registro-ficciones.md) — extraer el valor de los últimos 5 y los últimos 10 relatos (publicados + drafts pre-pub).

**2. Calcular métricas de saturación** según [`castellano-literario-es.md § 2.bis.1`](../../references/ficciones/castellano-literario-es.md):

| Métrica | Umbral | Estado |
|---|---|---|
| Referentes distintos en últimos 5 | ≤ 2 | 🔴 SATURACIÓN CRÍTICA |
| Referentes distintos en últimos 5 | 3 | 🟡 SATURACIÓN LEVE |
| Referentes distintos en últimos 10 | < 6 | 🟡 SATURACIÓN LEVE |
| Mismo referente repetido en últimos 3 consecutivos | sí | 🔴 RACHA SATURANTE |
| Referentes distintos en últimos 10 | ≥ 8 | 🟢 SANO (no reportar) |

**3. Si estado 🟢 SANO** → no reportar. Continuar al paso 5.7.

**4. Si estado 🟡 LEVE** → incluir línea informativa en el reporte normal del Variability gate sin bloquear:

```
ℹ️ Saturación leve de catálogo: 3 referentes distintos en últimos 5 relatos (Adón, Mesa, Urraca).
   Considera tirar del catálogo §1.bis (Vilas/Mendoza/Aramburu/Pron/Chirbes/Grandes/Enriquez)
   o del banco curado §2.bis.2 (Abreu/Sara Torres/Jiménez Serrano/Sánchez/Portela/Muñoz Molina/
   Marías/Vila-Matas/Gopegui/Marta Sanz/Schweblin/Travacio) para el próximo relato.
```

Continuar al paso 5.7.

**5. Si estado 🔴 CRÍTICA o RACHA SATURANTE** → INTERRUMPIR el flujo y reportar a Rafael:

```
🔴 Saturación de catálogo detectada — el sistema sugiere ampliar el registro:

   Distribución últimos 5: <X usos de Adón, Y usos de Mesa, Z usos de Urraca>
   Referentes distintos últimos 10: <N> de 17 disponibles
   <Si racha:> "Adón ha sido referente principal de los últimos 3 relatos consecutivos."

📚 Catálogo §1+§1.bis SIN usar en últimos 5 relatos:
   <listado>

📦 Banco curado §2.bis.2 (12 candidatos disponibles para activar):
   <listado completo de los 12 con descripción de 1 línea>

Para el relato actual ({semilla}, categoría tonal {X}, hook propuesto {Y}):
   - Mejor encaje del catálogo §1.bis: <recomendación con razón>
   - Mejor encaje del banco §2.bis.2: <recomendación con razón>

¿Cómo procedemos?
   (a) Activar <candidato A del banco> como referente principal del relato actual (Nivel A puntual).
   (b) Activar <candidato B del catálogo §1.bis> que aún no se ha usado.
   (c) Sigues con el referente que ya tenías propuesto en mente.
   (d) Sugiéreme nombres distintos que no estén ni en catálogo ni en banco — ampliemos el banco.
```

**6. Si Rafael elige (d) ampliar el banco**: el skill propone 2-3 autores ES/iberoamericanos no presentes en §1, §1.bis ni §2.bis.2 con justificación de qué registro nuevo aportan. Si Rafael acepta uno → se añade al banco §2.bis.2 con el formato canónico (registro · aporta · cuándo activarlo · NO usar para). Si Rafael lo descarta → entra a la lista §2.bis.4 ("descartados con razón documentada").

**7. Registrar `referente-principal` en frontmatter** del relato (uno del catálogo §1, §1.bis, banco §2.bis.2 activado, o nuevo si Rafael lo aceptó). Opcional `referente-secundario` cuando la prosa mezcla dos registros (común en relatos largos).

**8. Aviso de banco corto.** Si el banco §2.bis.2 tiene ≤2 candidatos sin promover (porque varios ya pasaron a §1.tris), avisar a Rafael: *"Banco de ampliación con solo {N} candidatos sin activar. Considera proponer nombres nuevos para mantener variabilidad futura."* Esa es la regla recursiva: la propia detección de saturación se aplica al banco también.

### 5.6.tris Intensidad narrativa — declaración + validación de outline (canonizado 2026-04-26 PM tarde)

**Por qué este paso existe.** El catálogo histórico (9 relatos) era 56% Atmosférico + 22% Slice = **78% bajo en eventos**. Eso es prosa literaria peninsular preciosa pero NO funciona para audiencia ROBOHOGAR (audionovelas en newsletter de gente acostumbrada a YouTube/TikTok). Cita Rafael: *"todos los relatos parecen iguales… aquí no ha ocurrido nada y siempre parece que aquí no ha pasado nada. Por defecto quiero que ocurran más cosas."* La nueva matriz canon ([`intensidad-narrativa.md`](../../references/ficciones/intensidad-narrativa.md)) pone **Cinematográfico (≥5 eventos) como default** y limita Atmosférico al 20% + Slice al 5%.

**Ejecutar tras Variability gate (5.6) + Saturación de catálogo (5.6.bis), antes de hook (5.7).**

**1. Detectar categoría de intensidad declarada por Rafael.** Si Rafael especificó (`--intensidad=cinematografico`, *"escribe algo dinámico"*, *"flash atmosférico"*) → usar esa. Si no especifica → ejecutar **auto-balanceo** sobre [`content/registro-ficciones.md § Intensidad`](../../content/registro-ficciones.md):
- Calcular % real publicado por categoría sobre los últimos 12 relatos.
- Identificar la categoría con mayor déficit respecto a la matriz canon (40/35/20/5).
- Default propuesto = categoría con mayor déficit. Reportar el cálculo a Rafael:

```
🎬 Catálogo intensidad: Cinematográfico 0% / Dinámico 22% / Atmosférico 56% / Slice 22%
   Déficits respecto a matriz canon:
   - Cinematográfico: -40pp (objetivo 40%, actual 0%)
   - Dinámico: -13pp (objetivo 35%, actual 22%)
   - Atmosférico: +36pp (sobre-representado)
   - Slice: +17pp (sobre-representado)

   Default propuesto: 🎬 CINEMATOGRÁFICO. ¿Confirmas o sobrescribes?
```

**2. Si la categoría es 🎬 Cinematográfico o ⚡ Dinámico**, validar el outline declarado en pasos 4-5.5 contra el target de eventos:

| Categoría | Mínimo eventos significativos en outline |
|---|---|
| 🎬 Cinematográfico | ≥ 5 |
| ⚡ Dinámico | 3-4 |
| 🌫️ Atmosférico | 1-2 |
| 🍵 Slice of life | 0-1 |

**Contar eventos del outline** según definición de [`intensidad-narrativa.md § 2`](../../references/ficciones/intensidad-narrativa.md):
- ✅ Cuentan: alguien gana/pierde algo · alguien decide algo irreversible · alguien hace algo concreto con consecuencia · humanoide rompe patrón programado · llega noticia externa que cambia escenario · encuentro con personaje nuevo.
- ❌ No cuentan: descripción atmosférica, recuerdo, observación interior, gesto cotidiano repetido, diálogo informativo sin tensión.

**3. Si el outline NO cumple el target**:

```
🔴 Intensidad insuficiente:
   Categoría declarada: Cinematográfico (≥5 eventos)
   Eventos en outline: 3 (lista)
     1. <evento>
     2. <evento>
     3. <evento>

   Faltan ≥2 eventos significativos. Propuestas para añadir al outline:
   - <evento sugerido A — encaja con la semilla>
   - <evento sugerido B>
   - <evento sugerido C>

   ¿Cuáles añadimos al outline antes de prosa?
```

**Volver a paso 4-5 (Paint The Villain / Pixar Spine) hasta que el outline tenga eventos suficientes.**

**4. Cargar referente secundario de género** (recomendado para Cinematográfico/Dinámico): proponer al menos 1 referente del banco §2.bis.2 ampliado para combinar con la voz literaria peninsular ya elegida en `§ 5.6.bis`. Opciones según semilla:
- Conflicto moral con consecuencia ineludible → **Pierre Lemaitre** (thriller psicológico).
- Eventos físicos en cadena (asalto, motín, evacuación) → **Don Winslow** (acción rápida).
- Colapso sistémico (Reset, blackout, fallo masivo) → **Daniel Suarez** (sci-fi colapso, ya canon en setting `el-gran-reset.md`).
- Thriller con anclaje peninsular ES (urbano, policial, secreto familiar) → **Eva García Sáenz de Urturi**.

Registrar en frontmatter `referente-secundario: <Nombre>` cuando aplique.

**5. Registrar `intensidad-narrativa` en frontmatter** del relato (uno de las 4 categorías canon). Sin él, el output del skill se bloquea.

**6. Documentar la lista de eventos en `PASOS.md`** del relato bajo el epígrafe `### Eventos del relato`. Esto sirve para verificación pre-output (`§ 9`) y para auditoría futura.

### 5.7 Elegir tipo de hook de apertura — OBLIGATORIO antes de prosa (regla dura 2026-04-26)

**Por qué este paso existe.** Todo relato Ficciones Domésticas abre con un gancho fuerte estilo cold open de piloto HBO o teaser de YouTube — no apertura ambiental literaria neutra. Y la variedad de hooks entre relatos es regla dura: si ROBOHOGAR siempre abre igual (siempre cold open con anomalía, siempre flash-forward, siempre cuenta atrás), el lector recurrente baja la guardia. Razón completa: `@rules/editorial.md § Narrativa especulativa § Hook de apertura`. Origen del feedback: memoria `feedback_ficcion_hook_obligatorio.md`.

**1. Cargar catálogo canon (obligatorio).** Leer [`@references/ficciones/hooks-taxonomia.md`](../../references/ficciones/hooks-taxonomia.md) — 24 tipos en 6 familias (A Evento detonante · B Pregunta-enigma · C Estructura temporal · D Voz-forma · E Personaje · F Atmósfera-mundo) + tabla de encaje por semilla narrativa § 4 + lista de anti-patterns § 5.

**2. Calcular `hooks_recientes` (obligatorio).** Leer las últimas 5 filas de [`content/registro-ficciones.md`](../../content/registro-ficciones.md) (publicados + drafts en pre-pub) y extraer la columna `Hook`. Computar el conjunto de tipos concretos usados recientemente.

**3. Sugerir 3 candidatos al lector** (Rafael), con razón explícita:

```
📚 Catálogo: 24 hooks · Últimos 5 relatos: <hook_a, hook_b, hook_c, hook_d, hook_e>

Para esta semilla (<semilla>) + categoría tonal <X>, propongo:

  [1] <Hook_concreto> (familia <Y>) — <razón de encaje con la semilla> · NO usado en últimos 5 ✓
  [2] <Hook_concreto> (familia <Y>) — <razón de encaje con la semilla> · NO usado en últimos 5 ✓
  [3] <Hook_concreto> (familia <Y>) — <razón de encaje con la semilla> · NO usado en últimos 5 ✓

¿Cuál usamos, o prefieres otro del catálogo?
```

**Lógica de priorización del skill al elegir los 3 candidatos:**

- **Filtro duro:** descartar tipos presentes en `hooks_recientes` (excepción "sello de serie" documentada en `arco-serie.md` o "tie-in con artículo" documentada en `PASOS.md`).
- **Filtro semántico:** priorizar tipos de la tabla § 4 que encajan con la semilla narrativa.
- **Filtro de variedad de familia:** si la última familia usada fue X, priorizar candidatos de familias distintas a X.
- **Cobertura tonal:** filtrar por las categorías tonales del hook que encajan con la `categoria-tonal` declarada en paso 0.5.

**4. Si Rafael delega o no responde** → usar el candidato [1] sin pedir confirmación adicional. El paso no bloquea el flujo si Rafael ya está en modo automático.

**5. Registrar `hook_type` elegido.** El valor exacto (uno de los 24, ej: `A4 Ruptura mínima de rutina`, `B2 Anomalía minúscula que obsesiona`, `D1 Apertura epistolar`) entra en:
- Frontmatter YAML del relato: `hook_type: <Letra><Número> <Nombre canónico>`.
- Variable de trabajo del skill (se valida en paso 9).
- Fila correspondiente del registro al publicar (paso de Output / `/post-publish`).

**6. Excepciones documentadas.** Si Rafael fuerza un hook que ya está en `hooks_recientes`, el skill registra la excepción con razón en `PASOS.md` del relato (`hook_repetido_justificacion: <razón>`) y avisa: *"Rafael, este hook (X) se usó hace 3 relatos. ¿Confirmas la repetición y la razón? (sello-serie / tie-in / decisión editorial)"*. Sin razón → no avanzar.

### 5.7-bis Elegir display title YouTube-style — OBLIGATORIO antes de prosa (regla dura 2026-04-26 PM)

**Por qué este paso existe.** El `title:` corto interno (sustantivo simple 2-6 palabras: *La objeción*, *El operador nocturno*) sigue siendo el nombre del fichero `.md`, breadcrumb y URL slug. Pero el lector escaneando inbox de email, feed de YouTube o card OG en redes recibe primero un display title que aparece bajo la miniatura. La forma sustantivo-simple no compite con el algoritmo de descubrimiento; la forma declarativa con paradoja embebida (*"La cuidadora que reza para que su humanoide no la sustituya antes del tribunal médico"*) sí. Razón completa + canon: [`@rules/editorial.md § Display title declarativo YouTube-style`](../../.claude/rules/editorial.md). Catálogo familia G: [`@references/ficciones/hooks-taxonomia.md § Familia G`](../../references/ficciones/hooks-taxonomia.md).

**1. Cargar catálogo G + display titles recientes.**
- Leer [`@references/ficciones/hooks-taxonomia.md § Familia G`](../../references/ficciones/hooks-taxonomia.md) — 4 subtipos (G1 Oficio + acción imposible · G2 Acto cotidiano + objeto imposible · G3 Sujeto + paradoja temporal · G4 Función + sustitución imposible) + lista de anti-patterns.
- Leer las últimas 5 filas de [`content/registro-ficciones.md`](../../content/registro-ficciones.md) (publicados + drafts en pre-pub) y extraer columnas `Display title family` y `Display title band` (esta última solo aplicable cuando family = G1).
- Computar el conjunto `display_titles_recientes` (5 elementos) y `bandas_recientes` (subset de las G1).

**2. Sugerir 3 candidatos al lector** (Rafael), con razón explícita:

```
🎬 Catálogo G: 4 subfamilias · Últimos 5 display titles: <G_a, G_b, G_c, G_d, G_e>
   · Bandas usadas en últimos 5 G1: <A, C, D>

Para esta semilla (<semilla>) + categoría tonal <X> + display_title sugerido:

  [1] "<Display title 1>" (G1, banda <Y>) — <razón de paradoja embebida> · <N> palabras · NO usado en últimos 5 ✓
  [2] "<Display title 2>" (G2) — <razón de paradoja embebida> · <N> palabras · NO usado en últimos 5 ✓
  [3] "<Display title 3>" (G4) — <razón de paradoja embebida> · <N> palabras · NO usado en últimos 5 ✓

¿Cuál usamos, o prefieres reformular?
```

**Lógica de priorización del skill al elegir los 3 candidatos:**

- **Filtro duro 1:** descartar subfamilias G presentes en `display_titles_recientes` (excepción documentada en `arco-serie.md` si una serie tiene un G como sello editorial).
- **Filtro duro 2 (solo G1):** descartar la banda de personaje si ya domina los últimos 3 G1 (regla "no encadenar 3 relatos en misma banda"). Banda obligada si una banda nunca apareció en los primeros 10 heros del paradigma personaje.
- **Filtro semántico:** la paradoja embebida del display title debe estar **anclada al tema del relato + dato real**. Si el dato real es "AI Act art. 50", la paradoja del título lo materializa en una acción concreta (*"La cuidadora que reza para que su humanoide no la sustituya antes del tribunal médico"* refleja outsourcing-de-cuidados + brecha legal).
- **Longitud:** entre **10 y 15 palabras** (ajustado 2026-04-26 PM tarde — suelo sube de 8 a 10 para garantizar hook compositivo mínimo de fórmula G). Demasiado corto (<10) = sin hook compositivo. Demasiado largo (>15) = se corta en línea 2 de Apple Mail / Gmail preview pane (≈70 chars).
- **Anti-patterns prohibidos** (lista cerrada en `hooks-taxonomia.md § Familia G`):
  - Sustantivo simple sin acción (formato del `title:` corto, no del `display_title:`).
  - Pregunta retórica al lector ("¿Quién cuida a quién…?").
  - Resumen explícito de la trama (anula la paradoja).
  - Frase con dos cláusulas separadas por dos puntos ("Madrid, 2034: una cuidadora…").
  - Em-dash en el medio del título ("El humanoide — y los sueños…").
  - **Nombre propio real de figura pública** ("La ministra Yolanda Díaz que…") — bloqueo duro.
  - Fuera de rango **10-15 palabras**.

**3. Si Rafael delega o no responde** → usar el candidato [1] sin pedir confirmación adicional.

**4. Registrar en frontmatter:**
- `display_title: "<Display title elegido>"` (entre comillas, mayúscula inicial sola, sin punto final).
- `display_title_family: <G1|G2|G3|G4>`.
- `display_title_band: <A|B|C|D|E>` solo si family = G1; vacío en otros casos.

**5. Validar con grep pre-output (en paso § 9):**
- `display_title:` presente y entre comillas.
- Conteo de palabras **10-15** (rango ajustado 2026-04-26 PM tarde — suelo 8→10).
- `display_title_family:` presente con valor canónico.
- Si G1 → `display_title_band:` presente.
- Display title NO contiene nombre propio real de figura pública (matching contra lista futura `references/ficciones/figuras-publicas-vetadas.md`; mientras la lista no exista, lectura manual obligatoria por parte del skill).

**6. Excepciones documentadas.** Si Rafael fuerza una subfamilia G ya en `display_titles_recientes`, el skill registra la excepción con razón en `PASOS.md` (`display_title_repetido_justificacion: <razón>`) y avisa antes de avanzar.

### 5.7-ter Elegir tag poético tonal — OBLIGATORIO antes de prosa (regla dura 2026-04-26 PM)

**Por qué este paso existe.** Las categorías tonales canon (inquietante / radical / ambiguo / inspirador / mundano) son **internas al pipeline** — sirven al algoritmo de matriz canon 40/15/25/10/10 y al auto-balanceo. Pero el lector que llega a un post de ficción se beneficia de una etiqueta editorial **ES poética y reconocible** que ancla el relato en una micro-categoría visible. Esa etiqueta es el `tag_poetico:`, mapeado de un catálogo cerrado de 10 a las 5 categorías tonales. Razón completa: [`@rules/editorial.md § Tag poético tonal`](../../.claude/rules/editorial.md).

**1. Cargar mapeo canon (catálogo cerrado, 10 etiquetas):**

| Categoría tonal | Tag poético ES (elegir 1 según eje dominante) |
|---|---|
| inquietante | *Hogar uncanny* (eje técnico-sensorial) · *Habitaciones extrañas* (eje espacial) |
| radical | *Cuidados rotos* (eje afecto-cuidado) · *Diálogos rotos* (eje comunicativo) |
| ambiguo | *Memorias prestadas* (eje memoria-identidad) · *Espacios subconscientes* (eje psíquico) |
| inspirador | *Cocinas tibias* (eje material-doméstico) · *Anatomía emocional* (eje introspectivo) |
| mundano | *Domingos eléctricos* (eje cotidiano) · *Física melancólica* (eje observacional) |

**2. Sugerir 1 tag** del par correspondiente a la `categoria-tonal` declarada en paso 0.5, justificando el eje dominante:

```
🏷️ Categoría tonal: <inquietante | radical | ambiguo | inspirador | mundano>
   Pares disponibles: "<Tag A> (<eje A>)" o "<Tag B> (<eje B>)"

Para esta semilla, el eje dominante es <eje>: <razón>.
Tag propuesto: "<Tag elegido>"

¿Confirmas o prefieres el otro del par?
```

**3. Si Rafael delega** → usar el tag propuesto.

**4. Registrar en frontmatter:** `tag_poetico: "<Tag elegido>"`.

**5. Catálogo cerrado.** Si Rafael propone una etiqueta fuera de las 10 → no aceptar a nivel de relato individual. Documentar la propuesta en `PASOS.md § Tag poético propuesto fuera de catálogo` y abrir una nota para ampliar la regla en `editorial.md` antes del próximo relato. Mientras tanto, elegir el tag más cercano del catálogo cerrado.

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
- **Hook de apertura:** ya elegido en paso 5.7 (`hook_type` declarado). La primera frase / primer párrafo debe **ejecutar literalmente** ese hook según el ejemplo canónico de [`@references/ficciones/hooks-taxonomia.md § 2`](../../references/ficciones/hooks-taxonomia.md). Prohibidos los 8 anti-patterns de `hooks-taxonomia.md § 5` (apertura ambiental sin tensión · resumen biográfico · filosofía declarativa · *"Todo empezó cuando…"* · primera frase explicativa del universo · pregunta retórica al lector · presentación con adjetivos · descripción del robot como decorado).
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
- [ ] **Hook de apertura — `hook_type` declarado en frontmatter** (uno de los 24 canon de [`@references/ficciones/hooks-taxonomia.md § 2`](../../references/ficciones/hooks-taxonomia.md)). Sin él, output bloqueado.
- [ ] **Display title YouTube-style — `display_title:` y `display_title_family:` declarados en frontmatter** (regla dura 2026-04-26 PM). Verificación grep:

  ```bash
  # (a) display_title presente, entre comillas, no vacío
  grep -E '^display_title:\s*"[^"]+"' <relato.md>          # → 1 match

  # (b) display_title 10-15 palabras
  awk -F'"' '/^display_title:/ {n=split($2, w, " "); print n}' <relato.md>   # → 10-15

  # (c) display_title_family presente con valor canónico G1-G4
  grep -E '^display_title_family:\s*G[1-4]\b' <relato.md>   # → 1 match

  # (d) Si family = G1 → display_title_band con valor A-E
  grep -E '^display_title_family:\s*G1\b' <relato.md> && grep -E '^display_title_band:\s*[A-E]\b' <relato.md>
  ```

  Si alguno falla → output bloqueado. Detalle de la regla y catálogo G: § 5.7-bis + [`@references/ficciones/hooks-taxonomia.md § Familia G`](../../references/ficciones/hooks-taxonomia.md).
- [ ] **Display title NO menciona nombre propio real de figura pública.** Lectura manual obligatoria + grep cruzado. Lista de nombres a vigilar (provisional hasta crear `references/ficciones/figuras-publicas-vetadas.md`): miembros del Gobierno de España actual, presidentes autonómicos, líderes de partidos parlamentarios, jueces del TC, presentadores y deportistas top-50 ES. Si match → reescribir como rol genérico ("La ministra que…", "El delantero que…", "El presentador que…"). Excepción permitida: diálogo del relato (no en título ni hero).
- [ ] **Subfamilia G NO repetida en últimos 5 display titles del registro.** Consultar columna `Display title family` de [`content/registro-ficciones.md`](../../content/registro-ficciones.md). Excepción documentada en `arco-serie.md` (sello editorial de serie) o `PASOS.md § display_title_repetido_justificacion`.
- [ ] **Si `display_title_family: G1` → banda no encadenada 3 veces seguidas.** Consultar columna `Display title band`. Detalle en [`assets/branding/ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`](../../assets/branding/ficcion-hero-archetypes.md).
- [ ] **Tag poético — `tag_poetico:` declarado en frontmatter** (regla dura 2026-04-26 PM). Verificación grep:

  ```bash
  # tag_poetico presente con valor del catálogo cerrado de 10
  grep -E '^tag_poetico:\s*"(Hogar uncanny|Habitaciones extrañas|Cuidados rotos|Diálogos rotos|Memorias prestadas|Espacios subconscientes|Cocinas tibias|Anatomía emocional|Domingos eléctricos|Física melancólica)"' <relato.md>   # → 1 match
  ```

  Si falla → output bloqueado. Detalle: § 5.7-ter + [`@.claude/rules/editorial.md § Tag poético tonal`](../../.claude/rules/editorial.md).
- [ ] **Hero paradigma — `hero_paradigma:` declarado en frontmatter** con valor `personaje-accion-imposibilidad` (default desde 2026-04-26 PM para one-shots/miniseries) o `minimalista` (declarativo cuando objeto-testigo > personaje). Para episodios de serie con código declarado (Amparo, Ronda 3, MAIA), el campo puede omitirse o llevar el código de serie como valor (`amparo-domestic-warm`, `ronda-3-documental-social`, `maia-epistolar-dual`). Verificación: si one-shot/miniserie nueva y campo ausente → output bloqueado.
- [ ] **Hook concreto NO repetido en últimos 5 relatos** (consultar columna `Hook` de [`content/registro-ficciones.md`](../../content/registro-ficciones.md)). Excepción documentada en `arco-serie.md` (sello de serie) o `PASOS.md` (tie-in / decisión editorial); sin justificación → cambiar.
- [ ] **Primera frase / primer párrafo coincide con el `hook_type` declarado** — lectura manual obligatoria. Si no coincide o cae en uno de los 8 anti-patterns de `hooks-taxonomia.md § 5` (apertura ambiental neutra, resumen biográfico, filosofía abstracta, *"Todo empezó cuando…"*, primera frase explicativa, pregunta retórica al lector, presentación con adjetivos, descripción del robot como decorado) → reescribir antes de entregar.
- [ ] **Variabilidad inter-relatos — 4 ejes estructurales NO repetidos en últimos 5** (regla dura 2026-04-26 PM). Verificar contra [`content/registro-ficciones.md`](../../content/registro-ficciones.md):
  - `Perfil POV` del relato (edad±5 + género + relación familiar dominante) NO presente en últimos 5 relatos.
  - `Setting` triple (ciudad + momento del día + objeto-testigo central) NO presente en últimos 5.
  - `Conflicto humano` principal NO presente en últimos 5.
  - `Cliffhanger tipo` NO presente en últimos 5.

  Excepción única documentada: sello de serie declarado explícitamente en `arco-serie.md`. Sin declaración previa, no aplica. Si alguno repite → bloqueo, reescribir el outline. Detalle en [`@.claude/rules/editorial.md § Variabilidad inter-relatos`](../../.claude/rules/editorial.md).
- [ ] **Referente principal declarado en frontmatter** (`referente-principal: <Nombre>`) — uno del catálogo activo de [`@references/ficciones/castellano-literario-es.md § 1 + § 1.bis + § 1.tris`](../../references/ficciones/castellano-literario-es.md) o del banco §2.bis.2 si Rafael lo activó en el paso 5.6.bis. Sin declaración → bloqueo. Opcional `referente-secundario` cuando la prosa mezcla dos registros.
- [ ] **Saturación de catálogo de voces verificada** (regla dura 2026-04-26 PM). Si el paso 5.6.bis detectó 🔴 SATURACIÓN CRÍTICA o 🔴 RACHA SATURANTE y Rafael activó un candidato del banco curado, confirmar que el relato escrito **efectivamente refleja** la voz del candidato activado (no solo que se haya declarado en frontmatter). Lectura manual obligatoria: ¿la prosa final tiene el patrón sintáctico/distancia narrativa/registro del candidato? Si solo coincide en frontmatter pero la prosa sigue siendo Adón/Urraca por defecto → reescribir antes de entregar.
- [ ] **`intensidad-narrativa` declarada en frontmatter** (uno de `Cinematográfico` · `Dinámico` · `Atmosférico` · `Slice of life`). Sin él, output bloqueado. Detalle en [`@references/ficciones/intensidad-narrativa.md`](../../references/ficciones/intensidad-narrativa.md).
- [ ] **Eventos significativos del relato listados en `PASOS.md § Eventos del relato`** y conteo cumple el target de la categoría declarada:

  | Categoría | Mínimo eventos | ¿Cumple? |
  |---|---|---|
  | 🎬 Cinematográfico | ≥ 5 | ✅/❌ |
  | ⚡ Dinámico | 3-4 | ✅/❌ |
  | 🌫️ Atmosférico | 1-2 | ✅/❌ |
  | 🍵 Slice of life | 0-1 | ✅/❌ |

  Si Cinematográfico declarado y solo hay 3 eventos → reescribir antes de entregar. Definición de "evento significativo" en [`intensidad-narrativa.md § 2`](../../references/ficciones/intensidad-narrativa.md).
- [ ] **Si Cinematográfico/Dinámico** — verificar las 4 condiciones específicas de [`intensidad-narrativa.md § 3.1` o `§ 3.2`](../../references/ficciones/intensidad-narrativa.md):
  - [ ] **Decisión moral concreta del protagonista** en al menos una escena (no solo registro emocional).
  - [ ] **Intervención del humanoide** que sale de patrón programado en al menos un beat (acción, no solo observación).
  - [ ] **Cliffhanger fuerte al cierre**: pregunta concreta que el lector se hace al cerrar y que NO se responde en el relato.
  - [ ] **Ratio acción/atmósfera**: ≥75% acción/decisión/diálogo/consecuencia · ≤25% descripción atmosférica pura para Cinematográfico (ratio 60/40 para Dinámico).
- [ ] **Robot NO villano** (regla canon): el humanoide actúa pero el villano humano sigue siendo el motor del conflicto. Aplica especialmente en Cinematográfico, donde el ritmo puede tentar a hacer del robot la amenaza.
- [ ] **Tropos quemados — verificar contra [`@references/ficciones/tropos-quemados.md`](../../references/ficciones/tropos-quemados.md)**. El borrador no debe contener ningún tropo en estado 🔴 QUEMADO (≥2 usos, ventana de enfriamiento 5 relatos activa). Particularmente atento a setting clichés (cafetera italiana, geranios sin florecer, luz que no calienta, tortilla francesa), gestos físicos (pelusa-codo-dos-dedos, gesto de servirse café que no bebe, bata azul abrochada al revés), símiles (humanoide=abrigo en percha) y frases-fórmula (*"Cinco años hace ya"*, *"Hace tres años que no le hace ya nada"*). Si match → reescribir.
- [ ] **Validación grep cruzada — anti-auto-plagio léxico** (regla dura 2026-04-26 PM). Ejecutar:

  ```bash
  python utilities/check_self_plagiarism.py <ruta-al-relato.md> --window 5
  ```

  El script compara n-gramas ≥6 palabras del nuevo borrador contra los últimos 5 relatos publicados + drafts pre-pub. Resultado:
  - **Match ≥6 palabras consecutivas** → BLOQUEO. Reescribir las frases marcadas antes de entregar.
  - **Match 4-5 palabras de fórmula reconocible** (ej: *"Hace tres años que"*, *"luz de … que no calienta"*) → warning. Revisar y reescribir si la fórmula está saturada en `tropos-quemados.md`.
  - **0 matches ≥4 palabras** → procede al output.

  Saltar este paso rompe el contrato del skill — no es opcional.
- [ ] **Actualizar registro al cerrar el relato:** añadir fila a [`content/registro-ficciones.md`](../../content/registro-ficciones.md) con los 4 valores estructurales (Perfil POV, Setting, Conflicto humano, Cliffhanger tipo) + actualizar [`references/ficciones/tropos-quemados.md`](../../references/ficciones/tropos-quemados.md) con las 5-10 figuras dominantes detectadas en el relato (gesto físico clave, metáfora dominante, objeto-testigo cargado, frase-fórmula recurrente). Sin esta actualización, el siguiente relato no tendrá registro contra el que comparar.
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
content/ficciones/<serie>/<slug>/
  ├── YYYY-MM-DD-<slug>.md         ← el relato (Markdown con frontmatter, fuente de verdad)
  ├── audiolibro.txt               ← versión TTS-optimizada (OBLIGATORIA, input de /audiobook-generate)
  ├── beehiiv-paste.html           ← bloques copy-paste para Beehiiv (8 snippets con audio · 6 sin audio)
  ├── lo-real-snippet.html         ← snippet "Lo real detrás del relato" inline-styled
  ├── PASOS.md                     ← checklist de publicación + metadata SEO
  └── assets/
      └── hero-<slug>.png          ← hero still cinematográfico

assets/audio/ficciones/
  ├── <slug>.mp3                   ← audiolibro completo (intro + narración + outro), ContentType audio/mpeg
  └── <slug>-chunks-index.json     ← timestamps por capítulo para YouTube/Podcast chapters

R2 bucket robohogar-audio:
  ├── <slug>.mp3                   ← MP3 público (URL https://pub-...r2.dev/<slug>.mp3)
  └── covers/<slug>-podcast-1400x1400.jpg  ← cover (generado por /audiobook-distribute)

$HBX_VAULT/.../05-01_Robotica Newsletter/02-Drafts/Ficciones/
  └── <Título del relato> (audiolibro).md   ← mirror del audiolibro.txt + bloque triple-backtick para Reader
```

### Auto-encadenado /audiobook-generate — REGLA DURA 2026-04-27

**Cuando Rafael pide un relato de Ficciones Domésticas, el output esperado incluye MP3 subido a R2 + `beehiiv-paste.html` con 8 snippets canónicos**, NO solo el `.md` del relato. El skill encadena automáticamente:

1. Generar `audiolibro.txt` aplicando las reglas TTS canon (§ Copia audiolibro paso 9 — romanos→`Parte N. <título>.`, modelos `HOGAR-K3`→`HOGAR ka tres`, cursivas eliminadas, sin "Lo real", sin frontmatter, sin separadores).
2. Pre-flight de saldo ElevenLabs vía `utilities/elevenlabs_balance.py check`. Si insuficiente → bloqueo con mensaje claro a Rafael ("Saldo X créditos, necesarios Y. Esperar reset día 25 / subir plan / generar sin audio con `--no-audio`").
3. Llamar `python utilities/generate_audio.py <audiolibro.txt> <slug>` → MP3 final + URL R2 + duración tras concat.
4. Reescribir `beehiiv-paste.html` al patrón canon **8 snippets** (Meta A/B/C + Snippet 1=audio email + Snippet 2=audio web + Snippet 2.5=Frontispicio título corto + Snippet 3=Lo real + Snippet 4=CTA). Detalle: [`@.claude/commands/audiobook-generate.md § 6.4`](audiobook-generate.md).

**Override `--no-audio`:** si Rafael pide explícitamente *"genérame el relato sin audio"* o el saldo ElevenLabs es insuficiente, el flujo cierra con 6 snippets (Meta A/B/C + Snippet 1=Frontispicio + Snippet 2=Lo real + Snippet 3=CTA), sin tocar la API. El frontispicio (Snippet 1 sin audio · Snippet 2.5 con audio) **es OBLIGATORIO en ambos casos** — patrón Anagrama/Penguin Modern Classics canonizado 2026-04-27, detalle: [`feedback_ficcion_frontispicio_titulo_corto.md`](../memory/feedback_ficcion_frontispicio_titulo_corto.md).

**Voz default:** canon híbrido bumpers Luis (`GojDwihhnL1f7RrBuXsJ`) + cuerpo Gabo (`o0SveC0zgHFuCsEO3vHR`) desde 2026-04-28 (revertido el experimento "100% Gabo" del 2026-04-27 PM tarde). Detalle: [`feedback_audiobook_voz_default_gabo.md`](../memory/feedback_audiobook_voz_default_gabo.md).

**Cambia la regla previa "MANUAL-ONLY":** la economía de API se gestiona por pre-flight de saldo + opción `--no-audio`, no por bloqueo manual default. Razón: Rafael publica el relato en el newsletter Beehiiv y quiere que el lector escuche el audiolibro desde el email/web sin segundo paso manual. Cita literal 2026-04-27: *"para el futuro, si pido que me generes el artículo de un relato de ficcion también quiero que me generes el mp3 y lo subas ya que quiero los snippets html para escucharlo desde el newsletter"*.

**Reglas:**
- El `.md` del repo es la **fuente de verdad** para revisión y publicación (frontmatter, metadata, cursivas, comentarios HTML con dato-real y villano-humano).
- La copia audiolibro del vault es **mirror derivado** pensado exclusivamente para que Rafael escuche el relato en el móvil antes de publicar. Se regenera si el original cambia. No se publica nunca.
- **Subtítulos descriptivos OBLIGATORIOS en cada sección** (regla permanente desde 2026-04-24, tras feedback de Rafael): cada `<h2>` del relato lleva número romano + título descriptivo en formato `## I. <Título sobrio>` · `## II. <Título sobrio>` · etc. Tres formatos consistentes (markdown fuente · HTML Beehiiv · audiolibro TTS): los tres comparten exactamente los mismos subtítulos. **Prohibido publicar romanos pelados** (`## I` sin texto) en ninguno de los tres. Razón: la audiencia Beehiiv es lectura mainstream en móvil/email, no minimalismo literario peninsular tipo Bolaño/Adón. Subtítulos cortos (1-4 palabras), sobrios (no Wattpad), sin spoiler, ES peninsular. Plantilla canónica de elección: la primera línea narrativa o el objeto-testigo de la escena (ej: *"El botón"*, *"Hernán"*, *"La diapositiva"*, *"La cláusula"*, *"Managua"*, *"La una y dieciséis"*). En el TXT de audiolibro se transforma `## I. El botón` → `Parte uno. El botón.` Detalle de transformación TTS en § Copia audiolibro paso 9. Memoria de la regla: `feedback_ficcion_subtitulos_descriptivos.md`.

### Cierre canónico del relato — OBLIGATORIO en cada `.md` fuente y cada borrador HTML Beehiiv

Regla permanente desde 2026-04-25, tras feedback de Rafael (*"siempre pongas un Fin. al final como en el relato de behiiv de el que viene a tomar cafe y que siempre pongas al final el dato real como en el que viene a tomar cafe; en La objeción lo omitiste"*). Patrón canónico replicable a TODOS los relatos futuros (one-shot, episodio-serie, episode-0, piloto, tie-in).

Tras la última frase narrativa, el relato cierra SIEMPRE con tres bloques en este orden:

1. **`Fin.`** como párrafo separado (línea en blanco antes y después). Marca el cierre absoluto de la prosa narrativa. Si el `.md` se exporta a HTML Beehiiv, va como `<p class="fin">Fin.</p>` (clase CSS para que el editor pueda darle formato distinto — centrado, espaciado, kerning ligero).

2. **Separador `---` + sección `## Lo real detrás del relato`** — bloque visible en prosa breve (90-140 palabras orientativo) que aterriza para el lector los hechos reales en los que se ancla la ficción. Estructura:
   - Hipertextos `[texto](url)` a las fuentes verificables (legislación, organismo oficial, paper, comunicado de fabricante, dataset INE/Eurostat, medio reputado). Mínimo 2-3 enlaces; idealmente uno por dato no obvio.
   - Mezcla *lo que existe ya* + *lo que es licencia narrativa* + *lo que pasa en hogares reales* (no solo regulación seca).
   - Voz: editorial ROBOHOGAR plural (*"existe", "ocurrió", "es discusión académica abierta"*). Tono breve, claro, sin condescendencia. Cierra con una frase que devuelva al lector al territorio íntimo del relato (no con disclaimer corporativo).
   - **No es un disclaimer ni un summary del relato**: es prosa periodística breve sobre el sustrato real. El lector que pase por encima entiende qué es real y qué es ficción sin que el relato pierda su efecto.

3. **Comentarios HTML invisibles** con la trazabilidad editorial completa:
   ```html
   <!-- dato-real: ... -->
   <!-- villano-humano: ... -->
   ```
   Estos no se ven en Beehiiv (son comentarios HTML). Sirven al equipo editorial para auditoría, no al lector. La sección `## Lo real detrás del relato` (visible) y los comentarios (invisibles) **no se duplican palabra por palabra**: la visible es prosa para el lector, los comentarios son notas internas en taquigrafía.

**Estructura final del `.md` fuente:**

```markdown
[última frase narrativa de la sección final]

Fin.

---

## Lo real detrás del relato

[Párrafo breve con 2-3 hipertextos a fuentes reales, prosa editorial ROBOHOGAR plural, cierre que vuelva al territorio íntimo del relato.]

<!-- dato-real: ... -->
<!-- villano-humano: ... -->
```

**Estructura final del borrador HTML Beehiiv:**

```html
<p class="fin">Fin.</p>

<!-- ═══ LO REAL DETRÁS DEL RELATO ═══ -->
<div class="lo-real">
  <span class="lo-real-title">Lo real detrás del relato</span>
  <p>[Mismo párrafo breve con hipertextos.]</p>
</div>

<!-- ═══ OUTRO SERIE (opcional) ═══ -->
<p class="serie-outro">Ficciones Domésticas es la serie de relatos especulativos de ROBOHOGAR — cada tres o cuatro semanas, una historia corta desde el hogar robotizado que viene. Cero futurismo de laboratorio, todo cocina, pasillo y salón.</p>
```

**Lo que NO va en el bloque "Lo real detrás del relato":**
- Resumen de la trama (el lector acaba de leerla).
- Fórmulas tipo *"Esta historia plantea cuestiones sobre…"* (ensayismo barato).
- Disclaimers legales (*"Toda semejanza con la realidad…"* — el bloque hace lo contrario: subraya las semejanzas reales).
- Llamadas a la acción comerciales (eso va en el snippet CTA suscripción del § canon `rules/newsletter.md`, en bloque distinto y posterior).

**En la copia audiolibro Obsidian (`<Título> (audiolibro).md`):** el bloque `## Lo real detrás del relato` **NO se incluye** en el `<bloque triple-backtick>` de copy-paste para ElevenLabs Reader — el lector lo escucha como ficción, no quiere romper el espell con prosa periodística. Solo se incluye el `Fin.` final dentro del bloque (que da pausa natural al narrador).

**Snippet HTML para Beehiiv — entregable OBLIGATORIO** (regla 2026-04-25 tras feedback de Rafael: *"esta seccion siempre quiero que me la des con snipet html para beehix"*). Junto al `.md` fuente, el skill genera SIEMPRE un archivo separado `content/ficciones/<serie>/<slug>/lo-real-snippet.html` con el bloque HTML estilizado en inline-CSS, listo para pegar en Beehiiv vía `/html` → "Custom HTML block". Razón: las clases CSS no viajan a Beehiiv en paste directo (regla `rules/design.md § Bloques de código para snippets HTML inline`); el `.md` fuente es markdown plano que Rafael revisa, pero al publicar necesita el HTML inline-styled separado para no perder el formato.

**Plantilla canónica:** [`content/templates/lo-real-snippet.html`](../../content/templates/lo-real-snippet.html) — `<div>` con fondo crema `#FFF9EF`, borde izquierdo ámbar `#F5A623` 4px, eyebrow uppercase ámbar letter-spacing 1.5px, prosa Inter 15px line-height 1.65, hipertextos `<a>` ámbar subrayados. Estilos inline obligatorios (no clases). Em-dashes como entidad `&mdash;` (Beehiiv los renderiza Unicode al guardar).

**Estructura del snippet** (idéntica al markdown, solo cambia el wrapping):
```html
<div style="margin:32px 0;padding:24px 28px;background:#FFF9EF;border-left:4px solid #F5A623;border-radius:4px;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;">
  <div style="color:#F5A623;font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px;">Lo real detrás del relato</div>
  <p style="margin:0 0 12px;font-size:15px;line-height:1.65;color:#0C0C0C;">[primer párrafo con hipertextos]</p>
  <p style="margin:0;font-size:15px;line-height:1.65;color:#0C0C0C;">[segundo párrafo con hipertextos]</p>
</div>
```

**Ubicación de salida** — los archivos `lo-real-snippet.html` viven en la carpeta del relato junto al `.md` fuente, no en `content/templates/` (allí solo vive la plantilla genérica). Esto facilita que `/post-publish` los detecte automáticamente y se los recuerde a Rafael en el resumen del paso 11.

**Verificación pre-output (5 greps):**
```bash
# (a) Fin. al final del .md
grep -nE "^Fin\.\s*$" <relato.md>   # → ≥1 match

# (b) Sección "Lo real detrás del relato" en el .md
grep -nE "^## Lo real detrás del relato\s*$" <relato.md>   # → 1 match

# (c) ≥2 hipertextos en el bloque del .md
awk '/^## Lo real detrás del relato/,/^<!--/' <relato.md> | grep -oE '\[[^]]+\]\([^)]+\)' | wc -l   # → ≥2

# (d) Comentarios trazabilidad presentes en el .md
grep -ciE "<!-- dato-real:|<!-- villano-humano:" <relato.md>   # → ≥2

# (e) Snippet HTML para Beehiiv generado en la carpeta del relato
ls <carpeta-relato>/lo-real-snippet.html   # → existe
```

Si (e) falla → el relato no se considera entregable. Generar el snippet HTML antes de cerrar el output.

**Verificación pre-output del `.md`:**

```bash
# (a) "Fin." al final, como párrafo solo
grep -nE "^Fin\.\s*$" <relato.md>   # → ≥1 match

# (b) Sección "Lo real detrás del relato" presente
grep -nE "^## Lo real detrás del relato\s*$" <relato.md>   # → 1 match

# (c) Al menos 2 hipertextos en el bloque (mínimo viable)
awk '/^## Lo real detrás del relato/,/^<!--/' <relato.md> | grep -oE '\[[^]]+\]\([^)]+\)' | wc -l   # → ≥2

# (d) Comentarios trazabilidad presentes
grep -ciE "<!-- dato-real:|<!-- villano-humano:" <relato.md>   # → ≥2
```

Si alguno falla → completar antes de cerrar el borrador. Skill `/post-publish` aplica los mismos greps en su validación pre-publicación.

**Aplicar retroactivamente solo si el relato no se ha publicado aún o si Rafael lo pide.** Relatos ya publicados en Beehiiv no se actualizan retroactivamente (la metadata se congela en plataformas — ver regla `automation.md § Descripción y título del episodio NO se actualizan al re-publish del feed`); el editor manual de Beehiiv sí permite añadir el bloque a posteriori si se prefiere consistencia visual del archivo público.

Memoria de la regla: `feedback_ficcion_cierre_canonico.md`.

### Frontmatter YAML del relato

```yaml
---
title: "Título del relato"                              # Sustantivo simple 2-6 palabras (interno, slug-friendly fallback, breadcrumb)
display_title: "El/La [rol] que [acción + objeto-imposibilidad]"   # Declarativo paradójico 10-15 palabras (subject newsletter, H1 web, OG title, alt-text miniatura, copy redes). OBLIGATORIO desde 2026-04-26 PM. Rango ajustado 2026-04-26 PM tarde (suelo 8→10).
seo_title: "Título SEO (max 55 chars)"
meta_description: "Resumen con gancho (110-155 chars)"
slug: slug-kebab-case                                    # URL pública estable; deriva del title corto, no del display_title
serie: familia-cortes
episodio: 03
longitud: flash | corto | mini-serie-episodio
palabras: 847
personajes: [Tico, Abuela Cortés]
pov: omnisciente | primera-persona-tico
tiempo-verbal: presente | pasado
tag: Ficciones Domésticas
tags-beehiiv: [Opinión]
tag_poetico: "Hogar uncanny | Habitaciones extrañas | Cuidados rotos | Diálogos rotos | Memorias prestadas | Espacios subconscientes | Cocinas tibias | Anatomía emocional | Domingos eléctricos | Física melancólica"   # OBLIGATORIO. Catálogo cerrado de 10 mapeado a categoría tonal. Detalle: § 5.7-ter.
dato-real: "INE: 20,1% españoles +65 años en 2033"
villano-humano: "El silencio de las 18:00 (soledad de los mayores solos)"
left-wall: "Fisiología aspirador 2033: sin brazos, LiDAR 360° solo superficies sólidas, sin acceso telefónico directo"
big-lie: "Aspirador ha desarrollado modelo mental de rutinas humanas lo bastante preciso para detectar ausencia"
framework: pixar-spine | 5-sentence | mrus
categoria-tonal: inquietante | inquietante-heavy | radical | ambiguo | inspirador | mundano
hook_type: "A3 Acto irreversible inminente"              # Hook de prosa (familia A-F), § 5.7. OBLIGATORIO.
display_title_family: G1 | G2 | G3 | G4                  # Hook de display title (familia G), § 5.7-bis. OBLIGATORIO.
display_title_band: A | B | C | D | E                    # Solo si display_title_family = G1. Banda de personaje. Catálogo: ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad.
hero_paradigma: minimalista | personaje-accion-imposibilidad     # § 5 vs § 5.bis de asset-catalog.md. Default desde 2026-04-26 PM = personaje-accion-imposibilidad.
modalidad_visual: M1 | M2 | M3 | M4 | M5 | M6                    # Modalidad visual del hero (eje cromático ortogonal a paradigma + archetype). Catálogo: ficcion-hero-archetypes.md § Modalidades visuales. Anti-repetición últimos 3. OBLIGATORIO desde 2026-04-27 PM. M1=Ámbar nocturno (default heredado) · M2=Cobalto tormenta · M3=Diurno plomizo · M4=Atardecer magenta · M5=Amanecer brumoso · M6=Fluorescente clínico.
angulo_camara: A1 | A2 | A3 | A4 | A5                            # Encuadre del hero. A1=lateral eye-level · A2=cenital · A3=ángulo bajo · A4=a través de marco · A5=extreme macro. Anti-repetición últimos 3. OBLIGATORIO desde 2026-04-27 PM.
composicion_canon: C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19   # Patrón compositivo macro del frame (eje ortogonal a modalidad/ángulo/banda). Catálogo: ficcion-hero-composiciones-canon.md. Anti-repetición últimos 5 + bloqueo familia (I-V) si las últimas 3 son misma familia. OBLIGATORIO desde 2026-04-28. Selección aleatoria con filtro tonal — el skill propone 3 candidatos del pool, Rafael decide. C-01 Two-shot íntimo · C-02 Close-up emocional · C-03 Detalle manos · C-04 Espacio monumental · C-05 Eje simétrico · C-06 Pantalla/holograma · C-07 Ventana al exterior · C-08 Frontal teatral · C-09 Over-the-shoulder · C-10 Exterior nocturno · C-11 Decadencia/caos · C-12 Color-pop saturado · C-13 Three-shot teatral horizontal · C-14 Contrapicado escala asimétrica · C-15 Bóveda/cúpula con reunión circular · C-16 Foco cenital extremo quirúrgico · C-17 Ritual outdoor con horizonte desolado · C-18 Detalle manos con altar simétrico · C-19 Cabina cerrada con ventana exterior radical.
status: borrador
created: YYYY-MM-DD
hero-image: assets/hero-<slug>.png
---
```

### Hero image — bifurcación de paradigma (one-shots/miniseries vs series con código declarado)

Tras 2026-04-26 PM, los heros de Ficciones Domésticas se generan en uno de **3 paradigmas posibles**, decididos en este orden:

1. **Si el relato pertenece a una serie con código visual ya declarado** (La Casa de Amparo · Crónicas de Ronda 3 · Cartas a MAIA) → aplicar el **código de la serie** (existente, sin cambios). Ver tabla más abajo.
2. **Si el relato es one-shot o miniserie nueva sin código declarado y `hero_paradigma:` del frontmatter es `personaje-accion-imposibilidad`** (default desde 2026-04-26 PM) → aplicar el **canon § 5.bis** de [`assets/branding/asset-catalog.md`](../../assets/branding/asset-catalog.md) + archetype del grupo `personaje-acción-imposibilidad` de [`assets/branding/ficcion-hero-archetypes.md`](../../assets/branding/ficcion-hero-archetypes.md).
3. **Si el relato es one-shot/miniserie nueva y `hero_paradigma: minimalista`** (declarativo cuando el objeto-testigo aislado del relato es más fuerte que cualquier personaje en frame, ej: tela ceremonial de *La objeción*) → aplicar el **canon § 5** minimalista existente + archetype 01-15 de [`ficcion-hero-archetypes.md`](../../assets/branding/ficcion-hero-archetypes.md).

**Regla universal (los 3 paradigmas la cumplen):**
- No ventana exterior visible salvo cuando la modalidad la requiere explícitamente (M2 Cobalto tormenta, M4 Atardecer, M5 Amanecer); en esos casos la ventana es plana, sin paisaje urbano detallado, para evitar que Gemini meta neones con caracteres asiáticos. Ver `assets/branding/nano-banana-prompt-base.md`.
- No LEDs/neones/glow en robots (excepciones puntuales: glow dorado ojos Asimov, pinpoint azul Black Mirror; nunca en heros del nuevo paradigma).
- No texto, letras ni caracteres asiáticos.
- Dimensiones obligatorias 1200×630 (`--model 2 --aspect 16:9 --size 2K` + crop Pillow).
- Banda D (figuras públicas por rol) del paradigma personaje-acción-imposibilidad: **identidad por rol y atrezzo**, nunca cara reconocible de figura real. Regen si Gemini la mete.
- **Modalidad visual `M1-M6` declarada en frontmatter + ángulo `A1-A5` declarado** (paradigmas 2 y 3 — los one-shots/miniseries). Anti-repetición transversal a paradigmas: ninguna modalidad ni ángulo en los últimos 3 heros publicados. Series activas (Amparo/Ronda 3/MAIA, paradigma 1) NO usan M1-M6 — mantienen código fijo declarado. Catálogo + prompt fragments: `assets/branding/ficcion-hero-archetypes.md § Modalidades visuales (M1-M6)`.

#### Paradigma 1 — Serie con código visual declarado (La Casa de Amparo · Ronda 3 · MAIA)

Cada serie tiene un **código visual propio y consistente** para que el lector la reconozca de un vistazo. Sistema completo + precedentes en la memoria [`feedback_ficcion_hero_style.md`](../../../RRP-DEV/.claude/memory/feedback_ficcion_hero_style.md) (léela ANTES de generar cualquier hero de serie). En este paradigma, **siempre humano + robot/tech en el mismo frame** (regla heredada del canon de serie).

| Serie | Código | Rasgos clave |
|---|---|---|
| La Casa de Amparo | domestic warm | Hugo humanoide + Amparo + Lavapiés constante · lámpara tulipán ámbar · butaca floral · After Yang + Amor sin escalas |
| Crónicas de Ronda 3 | documental social | RONDA-3 utility 55cm constante + humano distinto cada ep · piso VPO distinto · ocre sucio verdoso desaturado · grano denso · Perfect Days + Real Humans |
| Cartas a MAIA | epistolar literario dual | NO humanoide (laptop + lámpara brass como "tech") · Clara + ocasionales vía mensaje · Cáceres burgundy cálido VS Berlín azul frío desaturado según POV · After Yang + 84 Charing Cross Road |

**Estilos reservados (NO usar en episodios):**
- **Asimov oil painting** — solo para tapa de ebook recopilatorio (~500 subs, roadmap ficciones)
- **Black Mirror frío** — solo para sub-línea *"Relatos inversos de Black Mirror"* (relatos inquietantes, sistema humano como amenaza, robot neutro)

**Al crear una nueva serie:**
1. Definir el código visual en `arco-serie.md` § 9 "Notas de producción" → "Hero image recurrente" ANTES del primer episodio — framing + paleta + luz + referencias cinematográficas + elementos constantes del universo.
2. Registrarlo también en esta tabla si va a reutilizarse.
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

#### Paradigma 2 — One-shots/miniseries nuevas con `hero_paradigma: personaje-accion-imposibilidad` (DEFAULT desde 2026-04-26 PM)

Canon `personaje-acción-imposibilidad` de [`asset-catalog.md § 5.bis`](../../assets/branding/asset-catalog.md). Adaptación de la gramática compositiva YouTube anglo (personaje + acción + objeto-imposibilidad) al lenguaje fotográfico still-life ROBOHOGAR (After Yang / Hammershoi / Wenders), **sin** copiar oil painting / digital painting.

**Composición obligatoria** (resumen del canon § 5.bis — referenciar el archivo para detalle completo):

1. **Personaje** identificable por oficio/rol/atrezzo en primer plano. Edad/género coherente con `Perfil POV` del frontmatter.
2. **Acción visible** ejecutada por el personaje — pose dinámica que traduce visualmente el verbo del `display_title:`.
3. **Objeto-imposibilidad** materializado físicamente que traduce la paradoja del `display_title:` (humo de color, líquido luminoso, partículas que escriben, luz que escapa, humanoide en gesto incoherente).
4. **Composición regla de tercios** — personaje en una zona, objeto-imposibilidad a contrapunto, foco lumínico ámbar diagonal sobre la unión.
5. **Fondo** azul `#1E2A3A` matte plain unmarked en tercio superior. Reduce vs minimalista (2/3) porque el personaje ocupa más altura.

**Algoritmo de selección de composición + archetype + modalidad + ángulo** (skill `/nano-banana` modo ficción + `/ficcion-draft`):

1. Leer del frontmatter: `categoria-tonal:` + `display_title:` + `display_title_family:` + `display_title_band:` (si G1) + `Perfil POV` (de la fila correspondiente del registro).
2. Cargar [`ficcion-hero-archetypes.md § Grupo personaje-acción-imposibilidad`](../../assets/branding/ficcion-hero-archetypes.md) **y § Modalidades visuales (M1-M6)** **y [`ficcion-hero-composiciones-canon.md`](../../assets/branding/ficcion-hero-composiciones-canon.md) § Catálogo (C-01..C-19)**.
3. Filtrar archetypes por banda obligada (`display_title_band` si G1) o sugerida (mejor encaje con el `display_title` y `Perfil POV` si no es G1).
4. Filtrar por compatibilidad con la categoría tonal (tabla de "Algoritmo de selección por categoría tonal" del catálogo).
5. **Anti-repetición acotada al paradigma:** excluir archetypes presentes en últimos 5 heros del paradigma personaje-acción-imposibilidad (columna `Archetype` de la tabla `§ 5 · Registro de heros ficción` filtrada por `Paradigma = personaje-acción-imposibilidad`). Excluir banda dominante en últimos 3 (no encadenar 3 relatos en misma banda).
6. **Forzado de cobertura banda:** si en los primeros 10 heros del paradigma una banda nunca apareció, bloquear las otras hasta que el siguiente relato corresponda a la banda faltante.
6.bis. **Selección de composición canon (C-01..C-19) — eje compositivo ortogonal · ALEATORIO con anti-repetición** (regla 2026-04-28 tras feedback Rafael "necesito más variedad compositiva tipo YouTube anglo" + ampliación 2026-04-28 PM tarde con C-13..C-19 tras estudio de capturas adicionales del canal Domestic Fictions):
   - Leer `content/registro-ficciones.md` columna `Comp.` y guardar las **5 últimas composiciones** publicadas + las **3 últimas familias** (I-V) publicadas.
   - Filtrar pool de 19 composiciones por compatibilidad con `categoria-tonal` (mapeo del catálogo § Mapeo composición → tonalidades preferentes).
   - Excluir las 5 últimas composiciones publicadas → pool A.
   - Si las 3 últimas composiciones publicadas pertenecen a la misma familia (I-V), excluir esa familia entera del pool → pool B.
   - Aplicar compatibilidad con banda si paradigma personaje-acción (mapeo § Compatibilidades especiales con bandas).
   - Si pool resultante < 3 candidatos: relajar filtro tonal (paso de "preferentes" a "todas excepto anti-repetición").
   - **Random.choice de 3 candidatos** del pool resultante — **REGLA DURA: las 3 composiciones C-XX deben ser totalmente distintas entre sí** (canonizada 2026-04-28 PM tras feedback Rafael en Pipo: *"quiero tres opciones con composiciones totalmente distintas, no tres prácticamente idénticas con pequeñas diferencias muy sutiles"*). Prohibido devolver 3 variantes de la misma C-XX cambiando solo el objeto-imposibilidad / pose / luz secundaria. Si una C-XX parece encajar perfecto, aun así proponer 2 más de C-XX distintas para que Rafael elija con contraste real. **Ideal:** las 3 vienen además de **familias distintas** (I/II/III/IV/V) cuando el pool lo permita, para máximo contraste compositivo macro. Verificación pre-output del paso: si `len(set(candidatos.C)) < 3` → resamplear hasta tener 3 únicos. Si `len(set(candidatos.familia)) < 3` → resamplear si el pool lo permite; si no, declarar el motivo en la respuesta.
   - **Forzado de cobertura:** si en los primeros 19 heros desde 2026-04-28 una composición nunca apareció, bloquear las otras hasta que toque la faltante.
   - Skill propone los 3 candidatos a Rafael con razón explícita (composición + familia + por qué encaja con tonal/POV/display_title + ejemplo del referente anglo del catálogo).

7. **Selección de modalidad visual (M1-M6) — eje cromático ortogonal** (regla 2026-04-27):
   - Leer `content/registro-ficciones.md` columnas `Modalidad visual` + `Ángulo` y guardar las **3 últimas modalidades** y los **3 últimos ángulos** publicados (transversal a paradigma — un hero minimalista cuenta).
   - Filtrar pool de 6 modalidades por compatibilidad con `categoria-tonal` (mapeo del catálogo § Modalidades visuales § Mapeo categoría tonal).
   - Excluir las 3 últimas modalidades publicadas → pool resultante de candidatos.
   - **Forzado de cobertura modalidad:** si en los primeros 10 heros desde 2026-04-27 una modalidad nunca apareció, bloquear las otras hasta que toque la faltante.
   - Si pool queda vacío por filtros → relajar mapeo tonal (no la anti-repetición); declarar excepción tonal en `PASOS.md § Hero` con motivo.
8. **Selección de ángulo (A1-A5)** — independiente de modalidad: excluir los 3 últimos ángulos publicados; preferir ángulo que case con la acción del `display_title` (ej: A2 cenital para acciones que se leen mejor desde arriba; A3 ángulo bajo para tensión vertical; A1 default lateral si ningún criterio narrativo prevalece).
9. Proponer **3 candidatos completos** a Rafael con razón explícita por candidato: **composición C-XX (familia + referente anglo) + banda + archetype + modalidad M# (paleta + atmósfera) + ángulo A#** + objeto-imposibilidad propuesto. Cada candidato es una combinación distinta de los 4 ejes para maximizar variabilidad. **REGLA DURA — las 3 composiciones C-XX son distintas entre sí** (no 3 variantes de la misma C cambiando solo objeto-imposibilidad / pose / luz secundaria). Verificación: `len(set([c1.C, c2.C, c3.C])) == 3` o regenerar.
10. Tras decisión: rellenar frontmatter `composicion_canon:` + `modalidad_visual:` + `angulo_camara:`. Ensamblar el prompt **sustituyendo el bloque "Composition" del template canónico § 5.bis por el prompt fragment de la composición C-XX elegida** (catálogo `ficcion-hero-composiciones-canon.md § Prompt fragments por composición`), **y reemplazando el bloque `[D]` (luz/paleta/atmósfera) por el prompt fragment de la modalidad M# elegida** (`ficcion-hero-archetypes.md § Prompt fragments por modalidad`). El bloque "Aesthetic" (painterly book cover + Penguin Modern Classics + chiaroscuro Hopper) y los anti-triggers se mantienen intactos en cualquier combinación.

**Validación pre-output (canon § 5.bis + modalidades visuales):**

- [ ] Personaje identificable por rol/oficio en primer plano (no solo silueta abstracta).
- [ ] Acción concreta visible coherente con el verbo del `display_title` declarado.
- [ ] Objeto-imposibilidad materializado físicamente que traduce la paradoja.
- [ ] Fondo del tercio superior matte plain unmarked, sin texto ni caracteres asiáticos. Color del fondo coherente con la **modalidad declarada** (M1 azul noche · M2 cobalto profundo · M3 gris-azulado pálido · M4 violeta-magenta · M5 teal lechoso · M6 cyan-verde frío).
- [ ] **Foco lumínico ÚNICO** mantenido (chiaroscuro de fuente única). Color de la fuente coherente con la modalidad (M1 ámbar cálido · M2 backlight cobalto/cian · M3 norte difusa neutra · M4 sunset magenta-naranja · M5 milky backlight con vapor · M6 fluorescente cenital fría).
- [ ] Test 120px — silueta del personaje + objeto-imposibilidad se distinguen a thumbnail. Las modalidades M3/M5 son las más arriesgadas en thumbnail (menos contraste cromático) — verificar con cuidado.
- [ ] Cero LEDs / glow / paneles luminosos. Cero neones (M2 y M6 son las más arriesgadas — Gemini puede meter neones en M2 ventanas de tormenta o pantallas LED en M6 hospitales).
- [ ] Si banda D: la cara del personaje NO es reconocible como figura concreta. Regen si fallo.
- [ ] **Modalidad y ángulo declarados en frontmatter** (`modalidad_visual:` + `angulo_camara:`) y NO repetidos en los 3 últimos heros publicados (consultar `content/registro-ficciones.md`).
- [ ] **Composición canon declarada** (`composicion_canon: C-XX`) y NO repetida en los 5 últimos publicados. Si las 3 últimas son misma familia (I-V), la nueva está en familia distinta. El render entregado debe leer claramente como la composición declarada (auditoría visual a ojo — declarar C-04 monumental y entregar two-shot íntimo = regen).

#### Paradigma 3 — One-shots/miniseries nuevas con `hero_paradigma: minimalista` (declarativo)

Canon § 5 minimalista existente. Aplica solo cuando el relato tiene un objeto-testigo aislado más fuerte que cualquier personaje en frame (ej: tela ceremonial de *La objeción*, tetrabrik de *El operador nocturno*). El skill **pregunta a Rafael** si hay duda sobre cuál paradigma aplicar; default sin pregunta = paradigma 2 (personaje-acción-imposibilidad).

Detalle completo del canon § 5 minimalista + 15 archetypes en [`ficcion-hero-archetypes.md`](../../assets/branding/ficcion-hero-archetypes.md). Anti-repetición acotada al paradigma minimalista (no contra el paradigma 2).

#### Operativa común a los 3 paradigmas

- **Fallback si Rafael no quiere hero:** usar monograma R sobre fondo ámbar claro como placeholder neutro.
- Añadir la nueva imagen a `asset-catalog.md § 5 · Registro de heros ficción` indicando paradigma + banda (si aplica) + archetype.
- Si hero generado falla cualquier validación → archivar la v en `<slug>/assets/_archive/hero-v<N>-<motivo>-YYYY-MM-DD.png` y regenerar con v+1.

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
9. **Separadores de escena (`---` + `## I. <Título>` del original) → sustituir por** una línea en blanco + *"Parte uno. <Mismo título descriptivo del .md>."* / *"Parte dos. <Mismo título>."* / *"Parte tres. <Mismo título>."* al inicio de cada escena, como párrafo propio. **Los subtítulos descriptivos son los mismos que en el .md fuente** (regla permanente desde 2026-04-24): si el .md dice `## IV. La diapositiva`, el TXT audiolibro dice `Parte cuatro. La diapositiva.`. Los dividers de markdown no se leen.
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

---

## Modo `pitch` — formato canónico de exploración

Cuando se invoca el skill en modo `pitch` (frases trigger: `/ficcion-draft pitch <semilla>`, *"cuéntame más sobre X"*, *"explora el pitch de X"*, *"desarrolla X"*), el skill **NO escribe prosa**. Genera un documento de exploración estructurado para que Rafael elija opciones antes de comprometerse a redactar. Ejecutar solo pasos 0 (detectar modo) + 0.5 (declarar tonal provisional) + este bloque.

**Por qué existe este modo:** brainstorming estructurado sin quemar context window ni tokens en prosa que se va a descartar. Rafael ve las decisiones importantes (personajes, localización, tono, estructura, finales, título) con una opción elegida + variantes, elige, y luego reinvoca `/ficcion-draft one-shot <semilla-refinada>` con la decisión tomada. Separa *qué contar* de *cómo contarlo*.

### Regla de forma — opción elegida + variantes, siempre

Cada bloque que admite variación presenta **una opción elegida (razonada)** y **2-3 variantes descartadas** con media línea sobre qué cambia. Nunca listar opciones equiparables sin marcar cuál recomienda el skill — Rafael pidió decisión con criterio, no un menú neutro. La razón de la elegida es lo que le permite decidir si contraargumentar.

### Template obligatorio — 10 bloques en este orden

**1. El pulso** (2-3 frases).
De qué va **en verdad** el relato (conflicto humano subyacente, no premisa superficial). El robot es MacGuffin que obliga al protagonista a mirar algo. Aquí no hay variantes — es la tesis del relato.

**2. Anclaje canon** (Tchaikovsky + MRU).
- **Left-wall** — restricción tecnológica real e inviolable que hace el relato plausible. Una sola, concreta, con referencia a investigación real (papers, específicos de fabricante, ley, informe). No inventar capacidades.
- **Big-lie** — única licencia creativa por encima del left-wall. Marca explícita: *"Es el único salto que pide el relato; todo lo demás se sostiene solo."*. Máximo una.
- **MRU** — POV (1ª persona de X / 3ª cercana a Y / omnisciente), tiempo verbal (presente / pasado), triángulo autor/personaje/lector (quién sabe qué, dónde está la asimetría dramática).

**3. Geografía y personajes** (con opciones).
- **Localización** — ciudad + barrio concreto. **Elegido: X — razón.** Variantes descartadas: 2-3 alternativas con media línea. El barrio importa (clase social, subtexto).
- **Protagonista** — nombre ES peninsular plausible, edad, oficio, anclaje biográfico en 1 línea. **Elegido: X.** Variantes: 2-3 nombres/perfiles alternativos.
- **Secundarios** — solo los que tienen escena (máx 2-3). Mismo formato.
- **Robot/IA** — nombre propio ficticio del canon ROBOHOGAR (Tico, Hugo, RONDA-3, Eva, MAIA) o propuesta nueva. Si el relato pide robot sin nombre (como en *El partido de los domingos*, donde la ausencia de nombre es el filo), declararlo explícitamente y razonar por qué.

**4. Estructura propuesta** (con longitud).
- **Longitud recomendada** — `flash` (500-800) / `episodio-serie` (1.200-1.800) / `standalone` (2.500-3.500). Razón en media línea. Alternativas brevemente mencionadas si aplica.
- **Esqueleto de escenas** — 2-4 bloques con marcador (Escena 1, Intermedio, Escena 2, etc.) y qué pasa en cada uno. Sin prosa — solo sinopsis.

**5. Por qué funciona** (3 puntos).
- **El villano es humano / doble / ninguno.** Qué problema humano real revela o amplifica el relato (Paint The Villain invertido).
- **Cliffhanger estrictamente emocional.** Qué decisión queda abierta sin resolver. Nunca físico (regla canon).
- **Resonancia con lector ES 30-55.** Por qué el relato tiene tracción emocional en el público objetivo ROBOHOGAR.

**6. Finales posibles** (tabla, 3 opciones).
Tabla de 3 filas con columnas: **Final · Qué pasa · Tono**. Marcar **elegido** con asterisco o negrita y razonar en 2-3 líneas por qué ese es el que recomienda el skill. Los otros dos deben ser finales genuinamente distintos (no variaciones cosméticas del mismo) — cada uno cambia el peso moral del relato.

**7. Datos reales anclables** (bullets).
Lista 3-5 referencias verificables (ley/regulación · paper técnico · estadística INE/Eurostat · spec de fabricante · literatura clínica/psicológica). El relato usará 1 como ancla principal + otros como atmósfera. Si falta dato real obvio → flag: *"buscar verificación en `/research-digest` antes de redactar"*.

**8. Riesgos editoriales** (con antídotos).
Lista 2-4 riesgos: sentimentalidad, calcos anglo, comparación con obra conocida (Her, Black Mirror episodio X), Pixar/redención fácil, antropomorfización. Para cada uno: **antídoto operativo concreto** (qué regla técnica aplicar en la redacción para esquivarlo — ej: cero *thought verbs*, robot no habla en escena, detalle ES peninsular específico).

**9. Título** (con alternativa).
- **Título de trabajo: X** — razón en una línea.
- **Alternativa: Y** — por qué podría ser mejor / peor.
Máximo 2 alternativas. Marcar cuál gana y por qué.

**10. Pregunta de cierre al usuario.**
Lista compacta de qué opciones tiene que decidir Rafael antes de pasar a redacción: final (A/B/C), longitud (flash/episodio-serie/standalone), confirmar o cambiar localización/protagonista/título. Terminar con: *"Si te convence, dime las opciones y lo meto por `/ficcion-draft <modo> <semilla-refinada>`."*.

### Principios de composición del pitch

- **Brevedad con densidad.** Cada bloque debe ser escaneable pero dar meat suficiente para decidir. Sin frases de relleno. Sin *filler* ni resúmenes redundantes entre bloques.
- **Sin prosa del relato.** El pitch describe, no ejecuta. Ni una frase que pueda ir literal en el relato final — si aparece, reescribir o borrar.
- **Voz ROBOHOGAR del skill (no del relato).** El pitch usa voz plural editorial (*"el relato pide"*, *"recomendamos"*) y es analítico/editorial, no narrativo. La voz del narrador del relato se decide en paso 2 (MRU) como opción, no se demuestra.
- **Castellano peninsular directo.** Misma regla que el resto del skill (§§ 3 + 3.bis de `castellano-literario-es.md`). Sin calcos anglo aunque sea análisis editorial.
- **Anti-IA §1 aplica.** Sin *tapiz / entramado / intrincado / matizado*, sin tricolon mecánico, sin em-dashes en cascada decorativa.

### Output del modo pitch

- **Default**: volcar el pitch en el chat con los 10 bloques.
- **Opcional**: si Rafael dice *"guárdalo"* / *"que quede en repo"* → escribir en `content/ficciones/_pitches/<slug>.md` con frontmatter mínimo (`titulo`, `tonal-provisional`, `fecha`, `estado: pitch`). Este archivo NO es el borrador — es solo el documento de exploración. Cuando Rafael decida opciones y reinvoque `/ficcion-draft one-shot <slug>`, el skill lo lee como contexto y ejecuta los pasos 1-9 normales.

### Cuándo NO usar modo `pitch`

- Si Rafael dice *"escribe X"* / *"genera X"* / *"relato sobre X"* directamente — no. Quiere prosa. Ir directo a `one-shot` / `serie`.
- Si el backlog de calendario editorial ya tiene la semilla con gancho + tema humano + formato + dato real → usar `one-shot`, no `pitch` (el pitch equivalente ya está en el backlog).
- Si Rafael repite modo `pitch` sobre la misma semilla — preguntar qué sigue sin cerrar (quizá faltan opciones de personaje o final que no consideramos).

**Incidente origen:** 2026-04-24, Rafael pidió "cuéntame más" sobre una premisa (#10 *El partido de los domingos*) durante brainstorming. El skill respondió con un documento exploratorio estructurado (pulso, anclaje canon, personajes, 3 finales con elegido, riesgos, título con alternativa). Rafael pidió canonizar ese formato y añadirlo al pipeline para que se aplique consistentemente en futuras exploraciones. Regla nueva 2026-04-24. Memoria: `feedback_ficcion_modo_pitch.md`.

<!-- created by wwai-integration 2026-04-17 -->
