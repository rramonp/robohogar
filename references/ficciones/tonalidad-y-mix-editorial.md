---
type: reference
tema: sistema tonal canon Ficciones Domésticas ROBOHOGAR
audience: skill /ficcion-draft + Rafael (decisión editorial)
created: 2026-04-19
incidente-origen: feedback Rafael 2026-04-19 tras leer "El operador nocturno v2" — relato bien escrito pero "demasiado mundano, espero algo más impactante o incluso inquietante. El estilo habitual quiero que sea Black Mirror, ahí las historias son inolvidables"
---

# Tonalidad y mix editorial — Ficciones Domésticas

> Este archivo define el **sistema tonal canon** de las ficciones ROBOHOGAR: qué % del catálogo va a cada categoría, qué define cada categoría operativamente, qué la valida y qué la invalida, y cómo el skill `/ficcion-draft` auto-balancea el mix.
>
> Knowledge complementario: la voz literaria peninsular se rige por [`castellano-literario-es.md`](castellano-literario-es.md); los frameworks narrativos universales (Pixar, MRUs, Paint The Villain) por [`../writewithai/07-ficcion-y-narrativa-serializada.md`](../writewithai/07-ficcion-y-narrativa-serializada.md); los patrones serialized newsletter por [`serialized-newsletter-patterns.md`](serialized-newsletter-patterns.md); el canon de series y personajes recurrentes por [`series-bible-maestra.md`](series-bible-maestra.md). Este archivo NO duplica esos contenidos: aporta solo el sistema tonal por encima.

---

## §1 Matriz tonal canon

| Categoría | % objetivo | Sello en una frase | Black Mirror-adjacent |
|---|---|---|---|
| 🩻 **Inquietante** | **40%** | El final deja un nudo en el estómago | Sí (sello casa) |
| 🪤 **Radical / disruptivo** | **15%** | Cierre que da que hablar en una cena | Sí (extremo) |
| 🤔 **Ambiguo moral** | **25%** | El lector dudaría en votar quién tiene razón | Sí (cuando tira a oscuro) |
| 💚 **Inspirador / positivo** | **10%** | El lector sonríe (no llora) | No |
| 🍵 **Mundano / cotidiano** | **10%** | El lector arquea la ceja: *"ok, curioso"* | No |

**Lectura macro:** Black Mirror-adjacent = **80% del catálogo** (40 + 15 + 25, asumiendo que el ambiguo tira a oscuro la mayoría del tiempo). Inspirador + mundano = **20%** para que la marca tenga rango emocional y el lector no acabe fatigado.

**Cómo se aplica esta matriz:**
- Es un **objetivo macro del catálogo**, no una regla por relato individual.
- El skill `/ficcion-draft` cuenta el catálogo histórico (relatos publicados por categoría) y, si Rafael no especifica tonal en la invocación, propone la categoría más infrarrepresentada respecto al objetivo.
- Rafael puede sobrescribir con `--tono=X`. Si lo hace 3 veces seguidas hacia la misma categoría, el skill avisa que el mix se está desviando.
- Un relato puntual puede romper la categoría si el ángulo lo justifica, pero se documenta en su PASOS.md.

---

## §2 Categoría a categoría — definición operativa

### §2.1 🩻 Inquietante (40%) — sello casa

**Qué busca:** que el lector cierre el relato y necesite 30 segundos para asimilar antes de pasar a otra cosa. La tecnología es espejo deformante de lo humano. El cliffhanger emocional/moral ya documentado en `serialized-newsletter-patterns.md § 3.4` es el motor.

**Subcategoría — inquietante heavy:** dentro del 40%, una porción debe ser *heavy* (más cerca de radical sin llegar). Característica: la situación llega a territorio incómodo (manipulación íntima, voyeurismo coordinado, coerción suave por dark patterns, dependencia emocional inducida) sin cruzar a violencia explícita. Es lo que separa Black Mirror clásico de Black Mirror flojo.

**Verificación pre-output:**
- [ ] El lector cierra el relato con sensación física (nudo, escalofrío, peso).
- [ ] El final deja al menos 1 pregunta abierta que el lector se sigue haciendo.
- [ ] El robot/IA es instrumento, no villano (el villano es humano: empresa, familia, sistema).
- [ ] La situación no se resuelve a favor de nadie — alguien acepta algo silenciosamente.

**Antipatrón — el "hmm ok":**
- Situación curiosa pero sin consecuencia emocional para los personajes.
- El narrador explica el mecanismo tecnológico pero no toca lo humano.
- Cliffhanger débil tipo "alguien mira el suelo y se va a comer".
- *El operador nocturno v2* cayó parcialmente aquí (Rafael 2026-04-19); la v3 corrige con vuelta de tuerca.

**Referentes literarios:**
- **Charlie Brooker** (*Black Mirror* — *Be Right Back, Hated in the Nation, Smithereens*): la tecnología revela algo del humano que estaba latente.
- **Mariana Enríquez** (*Las cosas que perdimos en el fuego*): horror cotidiano sin gore explícito.
- **Pilar Adón** (*Las efímeras*, *De bestias y aves*): amenaza contenida, prosa que sostiene la inquietud sin nombrarla.
- **Layla Martínez** (*Carcoma*): el horror estaba en las paredes desde antes.

**Patrón canónico:**
- Hook in medias res (escena ya empezada).
- Acto 2 incluye revelación parcial — el lector sospecha algo antes que el personaje.
- Cliffhanger emocional con elisión: alguien decide callar / borrar / no contar.
- Densidad sensorial alta; detalles concretos que el cuerpo reconoce.

### §2.2 🪤 Radical / disruptivo (15%)

**Qué busca:** territorio extremo que se queda con el lector durante días. Si el relato se contara en una cena, generaría debate fuerte ("qué heavy" / "no me parece bien" / "yo también lo habría hecho").

**Temas válidos:** asesinato, manipulación severa, perversión moral (no sexual gratuita), traición irreversible, decisión que cruza una línea ética sin vuelta atrás. Los robots y la IA son testigos, instrumentos o coartadas — nunca actores morales primarios.

**Verificación pre-output:**
- [ ] El cierre es irreversible: alguien hace algo que no se puede deshacer.
- [ ] La empatía del lector queda dividida o suspendida.
- [ ] Hay un dato real ancla que hace plausible la situación extrema (ToS leído, hueco regulatorio, gig economy invisible).
- [ ] No hay villano de cartón; los implicados tienen razones humanas creíbles (no necesariamente justificables).

**Antipatrón:**
- Gore gratuito sin tesis humana detrás.
- Shock por shock, sin que la tecnología revele algo del sistema.
- Resolución tipo "la policía lo descubre" (cierra demasiado, anula la incomodidad).

**Referentes literarios:**
- **Charlie Brooker** (*Black Mirror* extremo: *White Bear, Shut Up and Dance, USS Callister*): violencia ética/emocional sostenida.
- **Fernanda Melchor** (*Temporada de huracanes*): violencia social sin redención.
- **Samanta Schweblin** (*Distancia de rescate*, *Pájaros en la boca*): cuerpo y horror.

**Patrón canónico:**
- Apertura engañosamente cotidiana.
- Escalación rápida en acto 2.
- Cierre con un acto irreversible + alguien siguiendo con su vida como si nada (más perturbador que el acto en sí).

### §2.3 🤔 Ambiguo moral (25%) — categoría favorita Rafael

**Qué busca:** que el lector dude en votar quién tiene razón. No hay villano claro. Dos verdades igualmente válidas chocan. El lector cierra preguntándose: *"¿yo qué habría hecho?"*

**Verificación pre-output:**
- [ ] Si el relato lo leyeran 10 personas, al menos 4 defenderían cada lado.
- [ ] Ningún personaje tiene la razón absoluta; ninguno está totalmente equivocado.
- [ ] El cliffhanger no resuelve — deja la decisión moral abierta.
- [ ] No hay narrador omnisciente moralista; la voz no juzga.

**Antipatrón:**
- Falsa ambigüedad: el narrador finge equilibrio pero el desenlace deja claro quién tenía razón.
- Mensaje obvio disfrazado de duda.
- "Equilibrio" entre una opción razonable y una claramente monstruosa (no es ambiguo, es mala fe).

**Referentes literarios:**
- **Ted Chiang** (*The Truth of Fact, the Truth of Feeling*; *The Lifecycle of Software Objects*): dilemas éticos sin solución.
- **Ursula K. Le Guin** (*The Ones Who Walk Away from Omelas*): el lector se queda con la pregunta.
- **Adrian Tchaikovsky** (*Service Model*): asistencia robótica vs autonomía humana, sin villano.

**Patrón canónico:**
- Apertura desde el POV del que va a tomar la decisión.
- Acto 2: escena que muestra el daño potencial de la opción A; escena que muestra el daño de la opción B.
- Cliffhanger: el personaje toma la decisión pero el narrador no juzga el resultado.

### §2.4 💚 Inspirador / positivo (10%) — criterio NO-triste reforzado

**Qué busca:** mensaje esperanzador o redentor sin ñoñería ni tragedia subyacente. La tecnología abre posibilidad humana real. El lector sonríe (no llora) y sale con energía.

**Verificación pre-output:**
- [ ] El lector cierra el relato con energía positiva, no con pena.
- [ ] No hay muerte, enfermedad terminal, duelo no resuelto, huérfano, exilio.
- [ ] La tecnología cataliza un acto humano valioso (reencuentro, perdón, descubrimiento, alegría).
- [ ] El cierre es concreto y suave, no platillo emocional.

**Antipatrón crítico (incidente Rafael 2026-04-19):**
- **Inspirador-triste** tipo *"el niño huérfano cuya madre programó el cortacésped"* — eso NO es inspirador. Es inquietante con disfraz emocional. Rafael lo rechazó explícitamente: *"demasiado triste"*.
- Si la inspiración requiere muerte previa, duelo o pérdida irreversible para llegar al "buen final", la categoría real es inquietante o ambiguo, no inspirador.
- Inspirador NO significa happy ending. Significa que el lector sale con energía, no con peso.

**Referentes:**
- **Kazuo Ishiguro** (*Klara and the Sun*): ternura sostenida sin ñoñería.
- **Kogonada** (*After Yang*): luz suave, duelo trabajado pero con belleza dominante.
- **Spike Jonze** (*Her*): la conexión humana asistida por IA que no se reduce a la IA.
- **Lara Moreno** (*La menuda*): la observadora externa que ama a los humanos sin despreciarlos.

**Patrón canónico:**
- Apertura tranquila, casi sin tensión.
- Acto 2: pequeño descubrimiento o gesto que abre una posibilidad nueva.
- Cliffhanger emocional positivo: dos personas hablando, una decisión que abre futuro, un gesto compartido. Nunca cierre con muerte ni pérdida.

### §2.5 🍵 Mundano / cotidiano (10%)

**Qué busca:** slice of life especulativo, observación tranquila sin gran giro. Funciona como respiro entre las categorías fuertes. El lector arquea la ceja: *"ok, curioso"*.

**Verificación pre-output:**
- [ ] La situación es plausible y reconocible.
- [ ] Hay al menos 1 detalle especulativo que la sitúa en 2030-2040 (sin él, no es ROBOHOGAR — es slice of life genérico).
- [ ] El cierre es descriptivo, sin promesa.
- [ ] El relato es corto (flash 500-800 idealmente; un mundano largo es aburrido).

**Antipatrón:**
- Mundano sin ningún detalle especulativo (cualquier escena cotidiana sin tecnología distintiva).
- Mundano que pretende ser inquietante pero no llega — entonces es solo flojo.
- Mundano largo (>1.500 palabras) — el formato no aguanta sin gancho.

**Referentes:**
- **Sara Mesa** (*Cara de pan*): observación contenida.
- **Lara Moreno** (*Por si se va la luz* — escenas de cotidianidad): la cocina, el patio, la espera.
- **Ali Smith** (*Seasons*): pequeñas escenas urbanas.

**Patrón canónico:**
- Apertura descriptiva.
- Acto 2: una observación o pequeño suceso (encuentro entre dos robots, malentendido lingüístico, rutina rota suavemente).
- Cierre descriptivo plano sin giro. La gracia está en el detalle especulativo, no en la trama.

---

## §3 Auto-balanceo del catálogo

El skill `/ficcion-draft` mantiene el mix gracias a este algoritmo de auto-balanceo:

1. **Lectura del catálogo histórico:** al invocarse sin tonal explícito, lee `content/registro-ficciones.md` (catálogo de relatos publicados con su `categoria-tonal` registrada en frontmatter).
2. **Cálculo del % real:** cuenta cuántos relatos publicados hay por categoría sobre el total.
3. **Comparación con objetivo:** identifica la categoría más infrarrepresentada respecto a la matriz §1 (la que tiene mayor déficit en puntos porcentuales).
4. **Propuesta:** sugiere a Rafael la categoría más infrarrepresentada como default para la próxima ficción. Rafael puede aceptar o sobrescribir con `--tono=X`.
5. **Aviso de desviación:** si Rafael fuerza la misma categoría 3 veces seguidas, el skill avisa: *"el mix está desviado: categoría X lleva N% del catálogo, objetivo Y%. ¿Seguimos o equilibramos?"*

**Ejemplo (estado hipotético del catálogo en mes 6):**
- 12 relatos publicados: 8 inquietante (67%) · 1 radical (8%) · 1 ambiguo (8%) · 2 mundano (17%) · 0 inspirador (0%).
- Mayor déficit: inspirador (objetivo 10%, real 0% → -10pp). Segundo: ambiguo (objetivo 25%, real 8% → -17pp).
- Skill sugiere: *"próxima ficción default = ambiguo (mayor déficit absoluto -17pp). Si quieres respiro positivo, default = inspirador (-10pp)."*

**Ventana de cómputo:** los últimos 12 relatos publicados (no todo el catálogo histórico) — así un sesgo viejo no domina indefinidamente.

---

## §4 Combinación tonal × frameworks narrativos

Cada categoría tonal sugiere (no impone) un framework de los del KB universal:

| Categoría | Framework Pixar Story Spine adaptado | Tipo cliffhanger | Densidad sensorial |
|---|---|---|---|
| 🩻 Inquietante | Spine completo + foreshadowing en acto 1 + revelación parcial en acto 2 | Emocional con elisión (alguien calla / borra / no cuenta) | Alta — detalles concretos del cuerpo y el espacio |
| 🪤 Radical | Spine acelerado + apertura cotidiana engañosa | Acto irreversible + alguien sigue como si nada | Media — la trama lleva el peso |
| 🤔 Ambiguo | Spine bifurcado: dos posiciones igual de defendibles en acto 2 | Decisión tomada sin juicio narrativo | Media-baja — la cabeza del lector lleva el peso |
| 💚 Inspirador | Spine suave + descubrimiento gradual | Gesto compartido o decisión que abre futuro | Alta — luz, gestos, pequeños actos |
| 🍵 Mundano | 5-Sentence Story para flash | Cierre descriptivo plano | Alta concentrada en 1-2 detalles especulativos |

---

## §5 Cross-references obligatorios

- **Voz literaria peninsular** (cómo se escribe la prosa): [`castellano-literario-es.md`](castellano-literario-es.md). Independiente de la categoría tonal — toda ficción ROBOHOGAR pasa por ese knowledge.
- **Frameworks universales** (Pixar, MRUs, Paint The Villain): [`../writewithai/07-ficcion-y-narrativa-serializada.md`](../writewithai/07-ficcion-y-narrativa-serializada.md).
- **Patrones serialized newsletter** (longitud, hook, cliffhanger emocional, left-wall + big-lie): [`serialized-newsletter-patterns.md`](serialized-newsletter-patterns.md).
- **Canon de series y personajes** (qué series existen, qué personajes son canon): [`series-bible-maestra.md`](series-bible-maestra.md).
- **Anti-IA checklist** (universal + ficción): [`../anti-ia-checklist.md`](../anti-ia-checklist.md).
- **Voz editorial baseline** (excepciones para ficción): [`../../.claude/rules/editorial.md § Narrativa especulativa`](../../.claude/rules/editorial.md).

---

## §6 Changelog

- **2026-04-19** — creación. Origen: feedback Rafael sobre *El operador nocturno v2* + validación de 20 historias-tipo + matriz tonal aprobada (40/15/25/10/10) con criterio NO-triste reforzado para inspirador.
