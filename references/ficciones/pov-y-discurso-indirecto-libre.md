---
type: reference
tema: punto de vista (POV) y discurso indirecto libre (DIL / free indirect style) — cuándo elegir 1ª persona vs 3ª limitada vs omnisciente, y cómo aplicar DIL como herramienta de voz peninsular literaria contemporánea (Aramburu, Mesa, Adón, Marías) en Ficciones Domésticas ROBOHOGAR
audience: skill /ficcion-draft + Rafael (revisión pre-output)
created: 2026-04-28 PM
incidente-origen: auditoría 2026-04-28 PM — los relatos aplican DIL bien cuando lo aplican (canónicamente Adón, Mesa lo hacen) pero el skill no tiene regla operativa de cuándo usar qué POV, ni catálogo de marcadores DIL para verificación pre-output. Resultado: 4 de 5 relatos en 3ª limitada por defecto, sin aprovechar 1ª persona ni omnisciente cuando habrían dado mejor tirón
---

# POV y discurso indirecto libre — toolkit ROBOHOGAR

> Esta referencia define **qué POV elegir** según tonalidad/intensidad/longitud, y **cómo aplicar discurso indirecto libre** (DIL / free indirect style) — la herramienta que hace la prosa de Aramburu, Mesa, Marías y Adón.
>
> Capa relacionada: voz peninsular literaria (`castellano-literario-es.md`), microtensión §2.8 (`microtension-sentence-level.md`), intensidad narrativa (`intensidad-narrativa.md`).

---

## §1 Tabla decisión — qué POV elegir

POV recomendado según los 3 ejes ROBOHOGAR. La tabla es orientativa — el skill propone, Rafael decide.

| Tonalidad | Intensidad | Longitud | POV recomendado |
|---|---|---|---|
| inquietante | Cinematográfico | corto/episodio | **3ª limitada cercana + DIL** (estándar peninsular: Aramburu, Adón) |
| inquietante | Atmosférico | flash | **3ª limitada cercana** sin DIL fuerte (Mesa) |
| radical | Cinematográfico | corto | **3ª limitada cercana + DIL** (Cristina Morales-style: registro de personaje contamina narración) |
| radical | Dinámico | flash/corto | **1ª persona** (intensidad emocional directa) |
| ambiguo | Atmosférico | flash | **3ª limitada con DIL** (Adón) o **1ª persona** según POV |
| inspirador | Slice | flash | **3ª limitada con DIL suave** (Lara Moreno) |
| mundano | cualquiera | flash/corto | **3ª limitada distante** (Mesa observadora) o omnisciente irónico |
| (POV humanoide) | cualquiera | cualquiera | **3ª limitada IA** o **1ª persona IA** (ver §5) |

**Default si no se elige:** 3ª limitada + DIL. Es el POV más versátil del canon peninsular.

**Catálogo cerrado de valores `pov:` en frontmatter:**
- `1a` — 1ª persona del personaje protagonista.
- `3a-lim` — 3ª limitada cercana sin DIL fuerte.
- `3a-lim-dil` — 3ª limitada cercana con DIL (default).
- `omnisciente` — narrador omnisciente (uso restringido — ver §3).
- `ia-1a` — 1ª persona del humanoide / IA.
- `ia-3a` — 3ª limitada del humanoide / IA.

---

## §2 Discurso indirecto libre (DIL) — definición y 4 marcadores

**DIL / free indirect style** = técnica narrativa en la que el narrador en 3ª persona **filtra la voz interior del personaje** sin marcador explícito (sin *"pensó que"*, sin acotación de pensamiento). El lector lee narración pero le llega como interioridad.

Es la herramienta central de la novela peninsular contemporánea (Aramburu *Patria*, Marías *Corazón tan blanco*, Adón *Las efímeras*). El skill `/ficcion-draft` la trata como recurso primario, no como adorno.

### §2.1 Marcador 1 — Deíctico cercano

Pronombres y demostrativos que solo el personaje usaría desde su posición (no el narrador desde fuera).

**Ejemplo:**
> ❌ *Tres metros más allá, su madre había caído.* (narrador externo)
> ✅ *Aquí, tres metros allá, había caído su madre.* (DIL — *aquí* es deíctico del personaje)

### §2.2 Marcador 2 — Léxico del personaje en narración

Palabras, expresiones o registros que pertenecen al léxico del personaje (su clase, su edad, su jerga) aparecen en la narración tercera.

**Ejemplo canónico** — *La canguro* (Joel, mozo logístico precario):
> *Apagó la pantalla. Y a ver ahora cómo paga la mensual del humanoide a fin de mes.*

La segunda frase es DIL. *"Y a ver ahora cómo paga"* es léxico de Joel, no del narrador omnisciente.

### §2.3 Marcador 3 — Presente histórico mezclado con pretérito narrativo dominante

En narración en pretérito, el DIL puede aparecer en presente puntual marcando interioridad inmediata.

**Ejemplo:**
> *Manuel apoyó el cañón en el muslo. No es esto. No es esto que vio. Levantó la cabeza.*

Las dos frases en presente (*"No es esto. No es esto que vio."*) son DIL — pensamiento interior de Manuel filtrándose en narración pretérita.

### §2.4 Marcador 4 — Exclamación o pregunta interior sin acotación

El personaje formula mentalmente una pregunta o exclamación que el narrador transcribe sin acotar como pensamiento.

**Ejemplo:**
> *Marta dejó la taza en el fregadero. ¿Y si Tata sentía algo todavía?*

La pregunta es DIL — es Marta pensando, no el narrador preguntando al lector. La diferencia está en que NO va precedida de *"se preguntó"* ni de comillas.

---

## §3 5 ejemplos canónicos de DIL en el catálogo ROBOHOGAR

(Extraídos de relatos publicados. Documentar dónde DIL ya funciona — son ejemplos de "lo estamos haciendo bien sin nombrarlo".)

### §3.1 *El que viene a tomar café* — DIL marca duelo no procesado

Pilar (POV) enciende cada mañana al humanoide HOGAR-X5 que simula a su padre fallecido. La narración 3ª limitada se contamina con su interioridad sin marcadores: *"Aquí está. Como cada mañana. Y nadie se entera."* El *"aquí está"* + *"nadie se entera"* son léxico de Pilar, no del narrador.

### §3.2 *Pipo* — DIL marca la decisión antes de articularla

Manuel reconoce la cabeza de Pipo. Narración: *"No es. No es la chatarra que él tiró."* El *"no es"* repetido en presente, sin acotar como pensamiento, es Manuel procesando — DIL marcador §2.3 + §2.4.

### §3.3 *La objeción* — DIL en POV humanoide

VELA-9 (POV humanoide) procesa la cláusula 47. Narración: *"Procede. Procede según patrón. Y luego, ¿qué?"* El *"y luego, ¿qué?"* es DIL — es el humanoide preguntándose sin acotación, no el narrador. Caso especial de §5 (POV IA).

### §3.4 *La canguro* — DIL marca clase y precariedad

Joel (POV) escucha a NIDIA-7 explicar la política de "minimización daño emocional doméstico". Narración: *"Política. Buena palabra para no decirlo claro."* El comentario es DIL — es Joel sin acotar.

### §3.5 *El cristalero* (draft) — DIL en obrero migrante

Wilmer (POV) ve archivar su rosa #31 en el log de CUSTODIA-2. Narración: *"Anomaly visual pattern. Como si dibujar fuera anomalía."* La segunda frase es DIL — es Wilmer pensando, registro suyo, sin acotación.

---

## §4 Anti-patterns

### §4.1 Head-hopping (cabeza saltarina)

Saltar de POV en mitad de escena rompe la inmersión. El lector no sabe a quién pertenece la interioridad.

**Forma prohibida:**
> *Manuel apoyó el cañón. Pipo sintió el frío del aire de noviembre.*

Si el POV está en Manuel (humano), no podemos acceder a la interioridad de Pipo (humanoide) en la misma escena. Solo permitido en bisagra de sección (`---` o `## II.`).

**Excepción documentada:** narrador omnisciente declarado (campo `pov: omnisciente`) puede saltar — pero entonces NO usar DIL fuerte de un solo personaje. Inconsistencia visible.

### §4.2 DIL inconsistente con la voz del personaje

El DIL solo funciona si el léxico que filtra coincide con el registro del personaje. Si Joel (mozo precario) tiene DIL con vocabulario académico, suena falso.

**Verificación:** al detectar DIL en el borrador, leer la frase aislada y preguntar *"¿este léxico es del personaje?"*. Si no → reescribir o eliminar.

### §4.3 Acotar el DIL (suena a doblaje)

Añadir *"pensó"* o comillas al DIL lo destruye. La técnica funciona porque NO está acotada.

| ❌ DIL acotado | ✅ DIL puro |
|---|---|
| *Manuel pensó: "no es esto, no es esto"* | *Manuel apoyó el cañón. No es esto. No es esto.* |

### §4.4 Voice del autor irrumpiendo

Pregunta retórica del narrador hacia el lector (*"¿cómo había llegado hasta aquí?"*) NO es DIL — es el autor entrando. Eliminar siempre.

---

## §5 POV humanoide / IA — convenciones ROBOHOGAR

Caso especial. Cuando el POV es un humanoide o IA (campo `pov: ia-1a` o `pov: ia-3a`), aplicar:

### §5.1 Sin robot-jerga anglo

Prohibido: *"running diagnostic"*, *"processing emotion subroutine"*, *"core protocol"*, *"compliance check"* en interior del humanoide. Sustituir por registro técnico ES + DIL del humanoide.

| ❌ Robot-jerga anglo | ✅ Registro ES + DIL |
|---|---|
| *Running emotion subroutine.* | *Detectó el patrón. Lo asignó a la cesta de cuidado.* |
| *Compliance check 47 returned positive.* | *Cláusula 47 procede.* |
| *Processing fatigue level: 78%.* | *Servomotor del codo derecho a 78. Tres horas de margen.* |

### §5.2 Conciencia humanoide — pulso lento, observación corporal

El humanoide observa el cuerpo humano con precisión técnica (temperatura, frecuencia cardíaca, micro-expresión) pero **no nombra** el sentimiento humano correspondiente. Lo registra y lo asigna.

**Ejemplo canónico** — *La objeción*: VELA-9 registra la dilatación de pupila de Lourdes + el ritmo de la respiración + la tensión del trapecio. Asigna *"alerta"* sin decir *"miedo"*. El lector hace la inferencia.

### §5.3 Léxico institucional ROBOHOGAR

Conviene anclar el humanoide a una institución ficticia del canon (Doméstica Ibérica, Toyminds Barcelona, Rondas3 SAE) con su propio registro corporativo. Eso da textura sin caer en jerga anglo.

### §5.4 DIL humanoide — pregunta interior

El humanoide puede formular pregunta interior sin acotar (DIL §2.4) pero el contenido tiene que ser **operativo o ético**, no emocional directo. Ejemplos canon:

| ✅ DIL humanoide |
|---|
| *Procede. Procede según patrón. Y luego, ¿qué?* |
| *Anomaly. Pero la anomalía no figura en la lista.* |
| *Si actúa ahora, contraviene el manual. Si no actúa, contraviene la cláusula 47.* |

### §5.5 Excepción declarada — humanoide con conciencia poética

En relatos que deliberadamente dan al humanoide voz literaria (línea Cartas a MAIA), se relaja §5.1-§5.4 — el humanoide puede acceder a registro emocional directo. Declararlo en `arco-serie.md` y en `PASOS.md` del relato. Sin declaración → aplica §5.1-§5.4.

---

## §6 POV en flash 500-800 vs corto 1.200-1.800

| Longitud | Cambios de POV permitidos |
|---|---|
| Flash | **0 cambios.** POV único toda la pieza. Si la idea exige cambio, mejor reescribir como corto. |
| Corto | **0-1 cambios** entre secciones (`---` o `## II.`). Nunca en mitad de escena. |
| Mini-serie episodio | **0-2 cambios** entre secciones. Solo si la serie tiene declarado `pov-rotativo: true` en `arco-serie.md`. |

**Regla del POV inicial:** la primera frase del relato debe instalar inequívocamente el POV. Si el lector no sabe en la frase 1 quién mira, hemos fallado el hook.

---

## §7 Cómo se aplica al skill `/ficcion-draft`

1. **Carga obligatoria** en paso 6 — `pov-y-discurso-indirecto-libre.md § 1` (tabla decisión) siempre. §§ 2-5 si el POV elegido es `3a-lim-dil`, `ia-1a` o `ia-3a`.
2. **Declaración en paso 7 nuevo** (POV + estructura de loops):
   - Elegir POV de la tabla §1 + justificación 1 línea.
   - Si `3a-lim-dil` → declarar 2-3 marcadores DIL planeados.
   - Si `ia-1a` o `ia-3a` → declarar institución ficticia del humanoide + lista de léxico técnico-ES-no-anglo.
3. **Verificación pre-output** en paso 8.x:
   - Grep robot-jerga anglo (`running|processing|core protocol|compliance check`) si POV humanoide. Match → reescribir.
   - Grep DIL acotado (`pensó:|"pensó`) — match → reescribir como DIL puro.
   - Lectura manual: cambios de POV en mitad de escena → bloqueo (head-hopping).
4. **Frontmatter** `pov:` (uno de los 6 valores). Auto-balanceo: el catálogo lee qué POVs están saturados.

---

## §8 Auditoría inversa de los 5 relatos publicados

| Relato | POV declarado | DIL detectado | Observación |
|---|---|---|---|
| Pipo | 3a-lim (Manuel) | ✅ §2.3, §2.4 (presente intercalado, pregunta interior) | Canónico — modelo a replicar |
| La objeción | ia-3a (VELA-9) | ✅ §5.4 (DIL humanoide ético) | Canónico — modelo a replicar |
| Papá desde Singapur | 3a-lim (Andrés) | ⚠️ DIL débil — la narración se queda en 3ª distante en partes | Podría reforzarse con DIL clase ejecutiva |
| Setenta y dos horas | 3a-lim (Marta) | ⚠️ DIL débil — silencio interior puro, sin filtrarse a narración | Podría haber DIL en sección del contador |
| La maratonista | omnisciente | ✅ DIL ligero (madre) | Coherente con flash atmosférico |

**Diagnóstico:** los relatos saben hacer DIL cuando lo hacen (Pipo, La objeción son casos canónicos). Pero el skill no obligaba a declarar POV ni a planear marcadores DIL. La regla nueva canon (declarar POV en paso 7 + verificar marcadores en paso 8.x) lo refuerza.

---

## §9 Mantenimiento

Archivo vivo. Cuando se identifique un 5º marcador DIL útil, añadir a §2.5. Cuando se detecte un nuevo robot-jerga anglo recurrente, añadir a §5.1. Cuando se sature un POV en el catálogo (>3 de los últimos 5 en `3a-lim-dil`), proponer rotación a `1a` o `omnisciente` en el siguiente relato.

**Referentes externos** (consulta opcional):
- Dorrit Cohn — *Transparent Minds* (1978) cap. "Free Indirect Style".
- Monika Fludernik — *The Fictions of Language and the Languages of Fiction* (1993).
- Para ES peninsular: Aramburu (*Patria*), Marías (*Corazón tan blanco*), Adón (*Las efímeras*) — manuales DIL contemporáneos.
