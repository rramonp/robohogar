# Composiciones canónicas para heros de Ficciones Domésticas

Catálogo de **19 patrones compositivos macro** (C-01..C-19) extraídos del canal "Domestic Fictions" de YouTube y aprobados por Rafael 2026-04-27 (C-01..C-12) y 2026-04-28 (C-13..C-19) como referente visual de variabilidad. Cada composición es un patrón **gramatical de frame** distinto: encuadre, profundidad, relación entre planos, atmósfera. Aplica a **todos los paradigmas** de hero ficción (minimalista § 5 + personaje-acción-imposibilidad § 5.bis).

Eje **ortogonal** a:
- **Modalidad visual** M1-M6 (paleta + color de la fuente lumínica única).
- **Ángulo de cámara** A1-A5 (eye-level / cenital / bajo / marco / macro).
- **Banda** A-E (rol del personaje, solo paradigma personaje).
- **Hook display_title** (verbo + paradoja).

## Por qué un catálogo macro de composiciones

Las 9 miniaturas test del 2026-04-27 (3 por relato: 72h, Papá, Llave) salieron correctas en estilo painterly y modalidad cromática, pero las 9 compartían exactamente la misma gramática compositiva: objeto-en-superficie con presencia humanoide secundaria. Rafael detectó que aunque las modalidades cambian la luz, las composiciones siguen mecánicas. Solución: forzar rotación a nivel de **patrón compositivo**, no solo a nivel de paleta.

## Reglas duras

1. **Frontmatter `composicion_canon: C-01..C-19` obligatorio** desde 2026-04-28. Sin él, output del skill bloqueado.
2. **Anti-repetición:** no repetir misma composición en los **últimos 5 heros publicados** (transversal a paradigma). Skill consulta `content/registro-ficciones.md` columna `Comp.`.
3. **Selección aleatoria + filtro de compatibilidad:** el skill `/ficcion-draft § 8.x Hero` filtra el pool de 19 por compatibilidad con `categoria-tonal` (mapeo más abajo) + `Perfil POV` + composición coherente con `display_title`, excluye las 5 últimas, y propone **3 candidatos aleatorios** del pool resultante. Rafael valida o pide alternativa.
3.bis. **Regla dura — los 3 candidatos son SIEMPRE 3 composiciones C-XX totalmente distintas** (canonizado 2026-04-28 PM tras feedback Rafael en la generación de Pipo: *"cuando me das tres opciones, quiero tres opciones con composiciones totalmente distintas, no tres prácticamente idénticas con pequeñas diferencias muy sutiles"*). Prohibido proponer 3 variantes de la misma C-XX cambiando solo el objeto-imposibilidad / pose / luz secundaria. Si el skill cree que una C-XX concreta encaja perfecto, igualmente debe proponer 2 más de C-XX distintas para que Rafael decida con contraste real — el valor del paso es exploratorio, no confirmatorio. **Ideal:** las 3 vienen además de **familias distintas** (I/II/III/IV/V) cuando el pool lo permita, para máximo contraste compositivo macro. **Verificación pre-output:** `len(set([c1.C, c2.C, c3.C])) == 3` o resamplear; `len(set([c1.fam, c2.fam, c3.fam])) == 3` ideal o declarar motivo si el pool no lo permite. Aplica también al skill `/nano-banana` cuando se invoca en modo ficción.
4. **Anti-cuadricula compositiva:** si las últimas 3 composiciones publicadas pertenecen a la misma familia (I-V), forzar familia distinta para la siguiente.
5. **ADN visual y regla "cotidiano + sci-fi mezclados" se mantienen** en todas las composiciones — humanoide siempre presente (explícito o como sombra/silueta/objeto sintético), painterly book cover obligatorio, chiaroscuro con foco único, anti-sign-guard activo.
6. **Meta de cobertura inicial:** en los próximos 19 heros desde 2026-04-28, deben aparecer **al menos 12 de las 19 composiciones**. Si tras 19 una composición nunca apareció, el skill bloquea las otras hasta que toque la faltante.

## Catálogo

### Familia I — Íntima emocional (close-up + two-shot)

#### C-01 · Two-shot lateral íntimo

Dos figuras en perfil cara-a-cara o paralelas, distancia próxima, tensión emocional concreta visible. Una figura es humano (con cara legible y expresión fuerte), la otra humanoide cream-white o tech-elemento. Foco lumínico único cae sobre el punto de contacto entre ellas (manos cogidas, cucharón al borde de la boca, gesto de alimentación, mano sobre hombro).

- **Gancho compositivo:** la mirada del lector entra por la cara emocional y salta al humanoide en cuestión de milisegundos.
- **Tonalidades preferentes:** ambiguo · inspirador · mundano · radical (cuando el contacto es invasivo).
- **Inspirado en:** *Sensory robot mimicking deceased chef · Companion bot simulating aging · Antique restoration robot replacing heirlooms · Smart cradle mimicking heartbeat.*

#### C-02 · Primerísimo primer plano emocional

Cara humana ocupando 60-80% del frame, expresión emocional unmistakable a thumbnail (shock, vergüenza, complicidad, descubrimiento, miedo). El humanoide o tech-elemento entra como detalle parcial (mano sintética en el borde, reflejo en el ojo, pixel de pantalla en la pupila).

- **Gancho compositivo:** la cara emocional llena el frame y el "imposible" entra por un borde — el lector primero siente, luego entiende.
- **Tonalidades preferentes:** radical · inquietante · ambiguo.
- **Inspirado en:** *Humanoid influencer sabotaging its own face · A maintenance droid deleting memories (en variante close-up paciente).*

#### C-03 · Detalle obsesivo con manos

Detalle macro o medium-macro de manos trabajando un objeto + atrezzo identificador del oficio + segundo plano fuera de foco con personaje y/o humanoide. La acción es minuciosa, ritual: coser, ajustar, medir, escribir, sellar, calibrar, restaurar, cocinar.

- **Gancho compositivo:** las manos hacen un trabajo concreto y el "imposible" se materializa entre los dedos (humo escribiendo, líquido luminoso, partículas, herramienta que no debería estar ahí).
- **Tonalidades preferentes:** inquietante · mundano · radical.
- **Inspirado en:** *Robotic tailor stitching microscopic trackers · Antique restoration robot.*

#### C-13 · Three-shot teatral horizontal con oficio

Tres figuras alineadas horizontalmente en un mismo plano de un taller / consulta / atelier / estudio: artesano-personaje a un extremo trabajando un objeto central, objeto/maniquí/destinatario en el centro como pivot, y receptor/cliente/observador al otro extremo. Suelen tener distinta profundidad pero tridelimitan el frame en tercios verticales. Foco lumínico cálido único cae sobre el objeto central que conecta a los tres.

- **Gancho compositivo:** la composición teatral en tercios fuerza al lector a leer una **transacción ritualizada de oficio** — quién hace, sobre qué, para quién. Los tres roles quedan claros a thumbnail.
- **Tonalidades preferentes:** ambiguo · inspirador · radical (cuando el receptor es coercionado).
- **Inspirado en:** *The tailor who sews sensors into wedding dresses to detect a groom's mechanical heart.*

#### C-18 · Detalle de manos con altar / fondo ceremonial simétrico

Híbrido C-03 + C-05. Detalle medium-macro de manos en primer plano trabajando un objeto-imposibilidad delicado, **mientras el fondo es un altar / atril / retablo / mecanismo monumental rigurosamente simétrico** con elementos flanqueantes (velas, columnas, vitrales, engranajes gigantes, símbolos religiosos o gremiales). El gesto íntimo del oficio se inscribe en una arquitectura ceremonial.

- **Gancho compositivo:** la fricción entre el gesto íntimo (manos) y la solemnidad del fondo (altar) declara visualmente que **lo que se hace aquí es ritual**, no rutina. Carga moral fuerte.
- **Tonalidades preferentes:** inquietante · radical · ambiguo.
- **Inspirado en:** *An antique clockmaker who replaces mechanical gears with synthetic humanoid heart valves.*

### Familia II — Plano arquitectónico monumental

#### C-04 · Espacio institucional con perspectiva profunda

Catedral, tribunal, sala de pleno, hangar, hospital, archivo, ferrocarril, biblioteca, cripta, garaje. Una perspectiva fuerte de un solo punto de fuga. Arquitectura monumental ocupa 60-70% del frame. Figura(s) pequeña/s en el espacio (silueta o plano medio), aisladas por la escala. El humanoide aparece como figura cream-white pequeña en alguna de las naves laterales o al fondo.

- **Gancho compositivo:** la escala sola produce inquietud; la figura pequeña en ella amplifica el conflicto humano.
- **Tonalidades preferentes:** radical · inquietante.
- **Inspirado en:** *Robot priest grants absolution · Robotic organist · Automated lawyer losing cases · Robotic judge sentencing carbon · Automated pilot crashing plane.*

#### C-05 · Eje simétrico altar / atril

Composición central absoluta. Figura(s) en eje vertical + simetría horizontal estricta. Adversario o multitud al fondo en filas paralelas. El humanoide u objeto-imposibilidad ocupa el eje exacto. Frame casi mandálico.

- **Gancho compositivo:** la simetría produce gravedad ceremonial — confrontación ritual, juicio, juramento.
- **Tonalidades preferentes:** radical.
- **Inspirado en:** *Robotic judge calculating sentences · The robot priest absolution · The robotic organist congregation.*

#### C-14 · Contrapicado de escala asimétrica humano↔máquina

Cámara contrapicada baja (a la altura del tobillo / suelo). Figura humana **pequeña** en primer plano (niño, anciano frágil, persona sentada o agachada) con máquina / humanoide / dron militar **enorme** en el mismo encuadre, dominando el frame por encima. Ambas figuras en el mismo plano de profundidad — no es perspectiva monumental al estilo C-04, es **contraste físico de cuerpos** en la misma estancia/calle/sala.

- **Gancho compositivo:** el contrapicado convierte al humano en silueta vulnerable y a la máquina en presencia totémica. El lector lee desnivel de poder antes de leer la escena.
- **Tonalidades preferentes:** inquietante · radical · ambiguo.
- **Inspirado en:** *An orphan who tricks the patrol robot into playing hide and seek forever.*

#### C-15 · Bóveda / cúpula con reunión circular ritual

Geometría arqueada del fondo (sótano abovedado, cripta, refugio subterráneo, cisterna, hangar arqueado, capilla, observatorio cupular). Figura central (o pareja central) sentada / de pie en el eje, **rodeada por una audiencia dispuesta en círculo** (niños, ancianos, fieles, supervivientes, alumnos). Profundidad mantenida por la curva del techo. Pantallas o iconos colgantes pueden reforzar la geometría arqueada.

- **Gancho compositivo:** la geometría circular sugiere ritual de comunidad clandestina — narración oral, ceremonia, asamblea. Distinta de la perspectiva monumental rígida (C-04) y del eje altar simétrico (C-05).
- **Tonalidades preferentes:** ambiguo · inspirador · radical.
- **Inspirado en:** *An insomniac teacher who uses discarded robot voices to narrate forgotten history to orphans.*

### Familia III — Frame dentro de frame

#### C-06 · Pantalla / holograma central

Una segunda escena dentro del frame principal vía pantalla, holograma, monitor, proyección, tablet, espejo digital, cristal de cabina. La pantalla muestra paradoja o información imposible (un ser querido fallecido, un cuerpo holográfico, métricas vacías, video de seguridad alterado). El personaje observa la pantalla; el humanoide participa o presencia.

- **Gancho compositivo:** el lector ve dos escenas — la real y la mediada por la pantalla — y la fricción entre ellas es el hook.
- **Tonalidades preferentes:** inquietante · ambiguo · radical.
- **Inspirado en:** *Digital butler leaking security footage · Automated therapist swap identities · Domestic robot translating baby cries.*

#### C-07 · Ventana / umbral al exterior

Una ventana, puerta, cristal de balcón o puerta entreabierta muestra una segunda escena exterior (mansión iluminada al fondo, paisaje nocturno, calle, jardín, cielo de tormenta). El interior está en penumbra; la ventana es el único punto de fuga lumínico. Personaje al lado de la ventana, mirándola o de espaldas.

- **Gancho compositivo:** el contraste interior-exterior crea pregunta inmediata: ¿qué espera el personaje? ¿qué viene del fuera?
- **Tonalidades preferentes:** ambiguo · inquietante · inspirador.
- **Inspirado en:** *Smart cradle mimicking heartbeat · Navigation droid blind billionaire · Gardening drone invasive species (variante con casa al fondo) · Automated pilot crashing plane.*

#### C-19 · Cabina cerrada con ventana a exterior radical

Variante extrema de C-07. El interior es **claustrofóbico y técnico** (cabina de avión, escotilla espacial, búnker, observatorio, submarino, ascensor minero, sala de control). El exterior visto por la ventana NO es doméstico ni reconocible: es **cosmos estrellado, dunas marcianas, mar abierto en tormenta, tundra ártica, cráter de impacto, ciudad bombardeada al fondo, cielo de tormenta extraterrestre**. El personaje está sentado o de pie con auriculares / casco / monitor en mano, **el humanoide o dron exterior comparte la composición** (visto pequeño contra el exterior radical).

- **Gancho compositivo:** la fricción interior-cerrado / exterior-abismal coloca al personaje en posición de soledad técnica frente a algo demasiado grande. Distinto del C-07 (donde el exterior es legible y cercano).
- **Tonalidades preferentes:** inquietante · ambiguo · radical.
- **Inspirado en:** *The pilot who teaches a cargo drone how to recognize constellations during long flights.*

### Familia IV — Frontal teatral / over-the-shoulder

#### C-08 · Frontal teatral con atrezzo simbólico

Figura (humano o humanoide) encarando la cámara directamente, pose teatral consciente, atrezzo o objeto simbólico claramente visible (cucharón, sello, expediente, pancarta, micrófono, llave inglesa, herramienta, bandera, boletín). Fondo en penumbra absoluta o sombra deep blue-gray. La figura es el único elemento iluminado completo.

- **Gancho compositivo:** la pose teatral y el atrezzo declaran el conflicto al instante — el lector lee "esto es lo que hace este personaje, y lo que hace es paradójico".
- **Tonalidades preferentes:** radical · inquietante (figuras públicas).
- **Inspirado en:** *Domestic robot translating baby cries · Robotic judge with globe · Automated florist toxic flowers · The robotic organist solo · Humanoid life coach.*

#### C-09 · Over-the-shoulder voyeur

Espalda de figura en primer plano (humano o humanoide), ocupando 30-40% del frame por un lado, dejando ver la escena al fondo en plano medio. La figura observa lo que el lector observa con ella. Tensión voyeurística o complicidad silenciosa.

- **Gancho compositivo:** el lector se convierte en el observador — comparte ángulo de visión con el personaje, comparte la transgresión.
- **Tonalidades preferentes:** inquietante · radical.
- **Inspirado en:** *Cleaning droid documenting household waste · Automated lawyer losing cases (variante backshot) · The librarian droid burning books (variante silueta + fuego al fondo).*

#### C-16 · Foco lumínico cenital extremo (quirúrgico / teatral)

Tight bust shot (cabeza + manos + atrezzo) con **luz cenital absoluta** cayendo en pico desde arriba. Sombras duras debajo de cejas, nariz, mentón, hombros. Atmósfera de quirófano / mesa de autopsia / escenario teatral con un solo spotlight / interrogatorio. El humanoide o tech-elemento entra como **objeto en las manos del personaje** (un dedo robótico de juguete, una placa de circuito, un órgano sintético) recibiendo también el rayo cenital.

- **Gancho compositivo:** la luz cenital teatraliza el momento como ritual técnico bajo escrutinio. El gesto de las manos sostiene el peso narrativo. Distinto del C-02 close-up emocional (lateral diagonal) — aquí la luz **cae desde arriba** y produce dramatismo de mesa de operaciones.
- **Tonalidades preferentes:** inquietante · radical.
- **Inspirado en:** *The surgeon who replaces his trembling hands with the precise fingers of a toy · The judge who asks a household robot to testify (variante con luz divina cenital sobre el robot testigo).*

### Familia V — Atmósfera ambiental + color-pop

#### C-10 · Exterior nocturno con foco icónico distante

Exterior nocturno: edificio iluminado al fondo (casa rural, mansión, faro, antena, hoguera, subestación), figura(s) silueta en primer plano de espaldas o de perfil. La distancia entre la figura y el foco icónico es protagonista. Cielo nocturno o de tormenta arriba.

- **Gancho compositivo:** la silueta apunta al foco lejano y el lector pregunta: ¿va hacia él? ¿viene de él? ¿qué pasó allí?
- **Tonalidades preferentes:** inquietante · ambiguo · mundano · radical.
- **Inspirado en:** *Navigation droid leading blind billionaire · Gardening drone invasive species · Librarian droid burning books · La llave inglesa (canon ROBOHOGAR — Ayllón en blackout).*

#### C-11 · Interior decadencia / caos

Habitación con elementos rotos, mobiliario desorganizado, objetos amontonados, evidencias de abandono o destrucción. Figura aislada en el caos (sentada, de pie, derrumbada). El humanoide cream-white aparece como contraste limpio en medio del desorden.

- **Gancho compositivo:** la habitación cuenta una historia anterior al frame — algo pasó aquí. La figura sostiene el peso de lo ocurrido.
- **Tonalidades preferentes:** radical · ambiguo · inquietante.
- **Inspirado en:** *Humanoid life coach convincing client to give away possessions · librarian droid (variante interior post-quema).*

#### C-12 · Color-pop saturado single-zone

Paleta general sobria/painterly canónica + UNA zona con acento cromático saturado fuerte (flores fucsia, pantalla turquesa, fuego naranja, neón violeta puntual, líquido verde fluorescente, humo magenta). El color-pop ocupa 15-25% del frame y es el segundo elemento visual más fuerte tras la cara/figura principal.

- **Gancho compositivo:** el choque cromático rompe la sobriedad y declara visualmente "aquí hay algo que no debería estar".
- **Tonalidades preferentes:** radical · inquietante.
- **Inspirado en:** *Automated florist arranging toxic flowers · Humanoid influencer sabotaging face · The librarian droid burning books (color-pop fuego) · Digital butler holograma turquesa.*

#### C-17 · Ritual outdoor con horizonte desolado / apocalíptico

Exterior amplio bajo cielo crepuscular o post-tormenta. Personaje en primer plano realizando **gesto ritual concreto** (arrodillado en absolución, alzando objeto, encendiendo vela, depositando ofrenda, cubriendo cuerpo, cavando, bendiciendo) sobre objeto-imposibilidad (cuerpo de robot caído, placa de circuito iluminada, órgano sintético, máquina rota, drone destruido). Detrás, el horizonte se extiende en **capas de paisaje desolado**: vertedero, llano post-industrial, ciudad bombardeada, cementerio de chatarra, dunas, ladera quemada, cráter, basurero electrónico. Cielo magenta-naranja-óxido o gris plomizo dramático.

- **Gancho compositivo:** el contraste entre el gesto de cuidado/ritual íntimo y el paisaje de desastre amplifica la carga moral. Distinto del C-10 (foco icónico distante puntual) — aquí no hay punto de luz lejano, hay **paisaje desolado completo en capas**.
- **Tonalidades preferentes:** radical · inquietante · ambiguo (cuando hay esperanza posible) · inspirador (cuando el ritual es de cuidado).
- **Inspirado en:** *A priest who performs last rites for robots discarded in the city landfill.*

## Mapeo composición → tonalidades preferentes (resumen)

| Tonalidad | Composiciones preferentes (no exclusivo) |
|---|---|
| inquietante (40%) | C-02 · C-03 · C-04 · C-06 · C-07 · C-09 · C-10 · C-11 · C-12 · C-14 · C-16 · C-17 · C-18 · C-19 |
| radical (15%) | C-02 · C-04 · C-05 · C-08 · C-09 · C-11 · C-12 · C-13 · C-14 · C-15 · C-16 · C-17 · C-18 · C-19 |
| ambiguo (25%) | C-01 · C-02 · C-06 · C-07 · C-10 · C-11 · C-13 · C-14 · C-15 · C-17 · C-18 · C-19 |
| inspirador (10%) | C-01 · C-07 · C-13 · C-15 · C-17 |
| mundano (10%) | C-01 · C-03 · C-10 · C-13 |

## Compatibilidades especiales con bandas (paradigma personaje)

- **Banda A (oficios domésticos):** mejor con C-01 · C-03 · C-07 · C-08 · C-12 · C-13 · C-16 · C-18.
- **Banda B (trabajadores ES día a día):** mejor con C-03 · C-08 · C-09 · C-11 · C-13 · C-16 · C-19.
- **Banda C (funcionarios públicos):** mejor con C-04 · C-05 · C-06 · C-08 · C-15 · C-16 · C-19.
- **Banda D (figuras públicas por rol):** mejor con C-04 · C-05 · C-08 · C-15 · C-16 (atrezzo institucional).
- **Banda E (cultura pop / mediática):** mejor con C-02 · C-06 · C-08 · C-12 · C-14 · C-16.

Las composiciones cross-banda (C-09 over-the-shoulder, C-10 exterior nocturno, C-11 caos, **C-14 contrapicado escala**, **C-17 ritual outdoor desolado**, **C-19 cabina exterior radical**) sirven a cualquier banda — son las **comodín** para forzar variedad cuando una banda lleva 2 relatos consecutivos en composición C-08 frontal teatral.

## Algoritmo de selección aleatoria con anti-repetición

```
1. Cargar pool completo: C-01..C-19.
2. Filtrar por mapeo tonal (composiciones preferentes para la categoría tonal del relato).
3. Excluir las 5 últimas composiciones publicadas (consultar registro-ficciones.md columna Comp.).
4. Excluir composición que coincida con familia (I-V) si las últimas 3 publicadas son de la misma familia.
5. Si pool resultante < 3, relajar filtro (a) tonal — permitir composiciones no preferentes que cumplan anti-repetición.
6. Si pool resultante = 0, error: ampliar catálogo o documentar excepción.
7. Random.choice de 3 candidatos del pool resultante.
8. Skill propone los 3 a Rafael con razón explícita (composición + por qué encaja con tonal/POV/display_title + ejemplo del referente anglo).
9. Rafael valida o pide rotación.
10. Tras decisión: rellenar frontmatter `composicion_canon: C-XX`. Componer prompt usando el patrón compositivo elegido + modalidad + ángulo + banda.
```

## Prompt fragments por composición

Cada fragment va en el bloque "Composition" del template canónico § 5.bis (`asset-catalog.md`). Sustituye el bloque "Foreground" + descripción de la escena. Mantiene el ADN painterly + chiaroscuro intactos.

```
# C-01 · Two-shot lateral íntimo
Composition: a tight two-shot in perfect side profile, two figures facing each other or sharing a parallel direction at very short distance, the moment of intimate contact between them filling the central third of the frame. Foreground left: [PERSONAJE HUMANO with role attire and emotionally readable face — expression of <emoción concreta>]. Foreground right (or beside): a matte cream-white humanoid in profile, plain matte surface, subtle articulated joints, no glowing parts, no LEDs. The point of contact between them — [hands clasped / spoon at mouth / hand on shoulder / gesture of feeding / token being passed] — receives the focal light. Background falls into deep painted shadow.

# C-02 · Primerísimo primer plano emocional
Composition: extreme close-up of a single human face filling 60 to 80 percent of the frame, painterly volumes on the cheekbone, eye, and lip, expression of <emoción concreta — shock, shame, complicity, discovery, fear> rendered unmistakably and legible at 120 pixel thumbnail scale. The humanoid presence enters the frame only as a small fragment at the edge — [a matte cream-white synthetic finger, a reflection in the iris, a single mechanical line at the corner of the lips, a sliver of cream-white shoulder]. Hard focal light cuts diagonally across the cheek and eye. Background of the frame falls into deep painted shadow.

# C-03 · Detalle obsesivo con manos
Composition: a medium-macro of a pair of human hands working a small object with concentrated attention, the role atrezzo (ring, glove, tool, lens) clearly identifying the trade, painterly volumes on the knuckles, fingernails, and tool. Object-impossibility materialized between the fingers — [smoke writing letters / luminous liquid glow / impossible particles / synthetic component that should not be there]. Out of focus in the background: the personaje's torso and partial face, plus the matte cream-white silhouette of a humanoid figure observing or participating, plain matte surface, no glowing parts. Hard focal light raking across the hands and the impossible object.

# C-04 · Espacio institucional con perspectiva profunda
Composition: a strong one-point-perspective view of a monumental institutional interior — [cathedral nave / courthouse hall / parliament chamber / hospital corridor / archive aisle / hangar bay / library stacks / crypt]. Architectural volume occupies the upper two thirds of the frame. The vanishing point pulls the eye toward the far end. A small human figure stands in the lower third near the foreground (silhouette or medium plane), dwarfed by the architecture. In a side aisle or far corner, a matte cream-white humanoid figure stands or kneels, plain matte surface, no glowing parts, presence-as-absence. Hard focal light enters from a clerestory window or skylight and falls on a single zone of the architecture and on the human figure.

# C-05 · Eje simétrico altar / atril
Composition: strict central symmetry in the frame — vertical axis through the middle, horizontal symmetry of background elements (rows of seats, flanking columns, parallel pews, mirrored audience). The personaje is positioned on the axis, frontal pose, atrezzo of authority or surrender clearly displayed. The object-impossibility floats or rests exactly on the axis as a second focal point. The matte cream-white humanoid stands behind or beside the personaje, also on the axis or in mirrored position. Symmetric audience or adversaries fill the background in deep painted shadow. Hard focal light from above or behind the personaje creates a vertical wedge of illumination along the axis.

# C-06 · Pantalla / holograma central
Composition: a screen, hologram, monitor, projection, tablet, glass dome, or digital mirror occupies the central third of the frame, projecting a second scene that contradicts or completes the primary scene. The personaje stands or sits beside the screen observing it, partial profile, painterly emotion legible on the face. The matte cream-white humanoid participates — either projecting the screen content, holding the device, or standing on the other side of the screen. Hard focal light comes from the screen itself, casting a colored glow on the personaje's face and hands. Background room falls into deep painted shadow.

# C-07 · Ventana / umbral al exterior
Composition: an interior corner with a single window, doorway, or balcony glass dominating one third of the frame, looking out onto a second scene at exterior — [illuminated mansion at distance / nocturnal landscape / urban street / garden / storm sky / rural square]. The interior is in deep painted shadow, the window the only major lit zone. The personaje stands beside the window, looking out or with back turned, painterly silhouette. The matte cream-white humanoid stands at the opposite side of the room or close to the window with the personaje, plain matte surface, presence-as-absence. Hard focal light enters from the window.

# C-08 · Frontal teatral con atrezzo simbólico
Composition: a single figure facing the camera directly, theatrical staged pose at chest height, atrezzo or symbolic object clearly held in hand or worn (spoon, stamp, wrench, microphone, pamphlet, key, tool, badge, flag, gavel, clipboard). The figure occupies the central column of the frame. Background falls into total deep painted shadow except for a sliver of context that identifies the setting (institutional column, kitchen tile, workshop wall). The matte cream-white humanoid stands one step behind the figure or beside, in deep shadow with only edge light catching the outline. Hard focal light from above-left drops a wedge on the figure's face, hands, and atrezzo.

# C-09 · Over-the-shoulder voyeur
Composition: the back and shoulder of a figure (human or humanoid) in the foreground occupies 30 to 40 percent of one side of the frame, head partially visible. Beyond the shoulder, the observed scene unfolds in medium plane: another personaje doing something private, a humanoid intervening, a screen, a transgressive moment. The reader shares the foreground figure's vantage. Hard focal light is on the observed scene; the foreground figure is in deep shadow, only edge light catching the outline of the shoulder.

# C-10 · Exterior nocturno con foco icónico distante
Composition: night exterior, deep painted blue-gray sky and ground. Far in the background: a single illuminated icon — [a rural Spanish house with windows lit / a mansion / a lighthouse / a transmission antenna / a bonfire / an electrical substation / a church spire]. Foreground: one or two figures in silhouette, back turned or in profile, looking toward the distant icon. The matte cream-white humanoid is one of the foreground figures or stands beside the personaje, plain matte surface. Hard focal light comes from the distant illuminated icon — the only major lit zone of the frame.

# C-11 · Interior decadencia / caos
Composition: an interior room in disarray — [furniture broken / objects piled in heaps / broken glass on floor / clothes strewn / collapsed bookshelves / scattered documents / debris]. Painterly volumes on the disorder. The personaje is alone in the chaos — [seated in the only intact chair / standing with hand on a wall / kneeling among debris / looking at one specific broken object]. Painterly emotion legible on the face. The matte cream-white humanoid stands as the only clean vertical element in the chaos, contrast of order amid disorder, plain matte surface. Hard focal light from a single source (window, lamp, fire) on the personaje and one zone of debris.

# C-12 · Color-pop saturado single-zone
Composition: the overall scene rendered in muted painterly palette dominated by deep blue-gray shadow + the modality's main hue, EXCEPT one specific zone occupying 15 to 25 percent of the frame where saturated color erupts — [magenta flowers in a vase / fuchsia hologram / orange fire on hearth / violet neon tube / fluorescent green liquid in beaker / pink dress on a body / amber smoke writing words]. The color-pop is the second strongest visual element after the personaje's face. The matte cream-white humanoid is positioned beside or interacting with the color-pop zone. Hard focal light cuts across the personaje's face and the color-pop zone, fusing them into a single emotional unit.

# C-13 · Three-shot teatral horizontal con oficio
Composition: a horizontal three-shot in a workshop / atelier / consulting room / studio, three figures arranged across the frame in vertical thirds. Left third: the personaje-artisan working with concentrated attention, role attire and trade tool clearly visible, painterly emotion legible on the face. Center third: the object central of the trade — [mannequin / dress / device / specimen / instrument] receiving the artisan's labor, occupying the visual pivot of the frame. Right third: the receiver — a client / patient / observer / commissioner — facing the center, painterly waiting expression. The matte cream-white humanoid is one of the three figures (artisan, object, or receiver) or stands as a fourth witness in deep shadow. Hard focal light from above-left lands on the central object, knitting all three roles into a single ritual transaction.

# C-14 · Contrapicado de escala asimétrica humano↔máquina
Composition: low-angle camera positioned near the floor (ankle height), looking up. Foreground: a small vulnerable human figure (child, elderly, seated, crouched) occupying the lower third of the frame, painterly emotion legible on the face. Looming above and behind, a massive humanoid / patrol robot / surveillance drone / industrial machine, painterly volumes on its plates and joints, dominating the upper two thirds of the frame. Both figures share the same physical space (alleyway, hallway, room, stairwell) — not architectural perspective. Hard focal light comes from above the machine, casting the human into deep shadow except for face and hands. Strong vertical contrast of scale.

# C-15 · Bóveda / cúpula con reunión circular ritual
Composition: an arched / vaulted / cupolated interior — [underground basement / crypt / shelter / cistern / arched hangar / chapel / observatory dome]. The vault's curved ceiling occupies the upper third of the frame, framing the scene. A central figure (or pair) is seated or standing on the vertical axis, surrounded by a circular audience of figures (children, elders, faithful, students, survivors) arranged radially around the center. Suspended screens, lanterns, or icons may reinforce the arch. The matte cream-white humanoid stands among the audience or beside the central figure, plain matte surface. Hard focal light from above (skylight, hanging lamp, central candle) drops a vertical wedge on the central figure, with the audience falling into deep painted shadow toward the periphery.

# C-16 · Foco lumínico cenital extremo (quirúrgico / teatral)
Composition: a tight bust-shot of the personaje (head, shoulders, hands holding an object), framed at chest height. Lighting comes from a single source directly overhead (surgical lamp / theatrical spotlight / interrogation light / autopsy ceiling lamp), casting hard shadows under brows, nose, chin, shoulders. Atmosphere of operating room / autopsy table / theatrical stage with single spotlight / interrogation chamber. The personaje's hands hold the object-impossibility (synthetic finger, circuit board, organ, prosthetic component) — the object also receives the vertical light beam. Background falls into total deep painted shadow. The matte cream-white humanoid presence is suggested by the object in hand or by a sliver of cream-white fabric at the edge.

# C-17 · Ritual outdoor con horizonte desolado / apocalíptico
Composition: wide outdoor exterior under crepuscular or post-storm sky (magenta-orange-rust or plumb-gray dramatic gradient). Foreground: the personaje performing a concrete ritual gesture — [kneeling in absolution / lifting an object skyward / lighting a candle / depositing an offering / covering a body / digging / blessing / closing eyelids] — over the object-impossibility (fallen humanoid body, glowing circuit board, synthetic organ, broken machine, crushed drone, electronic remains). Background: layered desolate landscape extending to the horizon — [city landfill / post-industrial plain / bombed cityscape / electronic-waste cemetery / dunes / scorched hillside / impact crater / bone-yard of machinery]. The matte cream-white humanoid is the object of the ritual or stands as silent witness behind the personaje. Hard focal light from low sun raking across the foreground figure and the object.

# C-18 · Detalle de manos con altar / fondo ceremonial simétrico
Composition: medium-macro of human hands in foreground working a delicate object-impossibility (synthetic heart valve, mechanical gear with organic tissue, glowing element, miniature humanoid component) — painterly volumes on knuckles and tool. The background is a strictly symmetrical altar / atrium / retable / monumental clockwork / shrine / guild seal, with flanking ceremonial elements (candles, columns, gears, stained glass, religious or guild symbols, mirrored sconces). The vertical axis of the altar runs straight up from between the hands. Painterly volumes on the altar fall into chiaroscuro. The matte cream-white humanoid presence is implied by the object in hand or by a partial silhouette in the symmetric background. Hard focal light from above (altar source) lands on the hands and the object, the symmetric background falling into reverent shadow.

# C-19 · Cabina cerrada con ventana a exterior radical
Composition: a tight, claustrophobic technical interior — [aircraft cockpit / spacecraft hatch / bunker control room / submarine cabin / mining elevator / observatory station] — occupying the foreground and middle ground. A window, viewport, or porthole on one side opens onto an exterior that is NOT domestic or urban but radically alien: cosmic starfield, Martian dunes, stormy open sea, arctic tundra, impact crater landscape, bombed city skyline at horizon, alien storm sky. The personaje is seated or standing inside the cabin, headphones / helmet / instrument in hand, painterly profile or three-quarter pose, looking toward the window or at a tool. The matte cream-white humanoid (or external drone) appears small against the radical exterior, visible through the window. Hard focal light from inside (instrument panel glow) on the personaje's face; cold ambient light from the radical exterior on the window frame. Hard contrast warm-interior / cold-exterior.
```

## Verificación pre-output (composición)

- [ ] Frontmatter `composicion_canon:` declarado y entre C-01..C-19 (bloqueo si falta).
- [ ] Composición no aparece en las 5 últimas publicadas (consultar `registro-ficciones.md`).
- [ ] Composición compatible con `categoria-tonal` declarada (consultar mapeo) — si no, motivo declarado en `PASOS.md § Hero`.
- [ ] Si las últimas 3 son de la misma familia (I-V), la nueva está en otra familia.
- [ ] El render entregado lee como la composición declarada (auditoría visual a ojo) — si declaras C-04 monumental pero el frame es un two-shot, regen.
- [ ] Composición + modalidad coherentes (ej: C-10 exterior nocturno NO se hace con M3 diurno plomizo; C-04 institucional rara vez con M5 amanecer brumoso).

## Backfill retroactivo de los 9 publicados + drafts

Todos los 9 publicados se backfillean con la composición que mejor describe su hero existente (best-fit, no perfecto):

| Relato | Hero existente (descripción mínima) | Composición backfill |
|---|---|---|
| El operador nocturno (v7) | Niño con linterna mirando humo gris desde aspirador con humanoide al fondo | **C-09** Over-the-shoulder voyeur (backfill) |
| El que viene a tomar café (v6) | Dos figuras en cocina con humanoide visible · two-shot | **C-01** Two-shot lateral íntimo |
| La maratonista y su sombra | Madre + hija + TV con récord humanoide | **C-07** Ventana / umbral al exterior (TV como umbral) |
| Setenta y dos horas (v3) | Yoyó rojo + humanoide encogido en rincón parquet | **C-11** Interior decadencia / caos (variante leve — no caos completo, pero presence-as-absence en piso semivacío) |
| Papá desde Singapur | (sin hero) | — |
| La objeción (v9) | Humanoide vestido como mayordomo sirviendo con humo de letras | **C-08** Frontal teatral con atrezzo simbólico |
| La llave inglesa | (sin hero) | — |
| El pendiente | (sin hero) | — |
| La canguro (v4) | Padre con linterna sobre laptop con palabras saliendo en humo | **C-03** Detalle obsesivo con manos |

Esto es backfill aproximado para empezar el contador de anti-repetición — no implica rerender. Los heros existentes se mantienen.

## Cross-references

- Catálogo de archetypes minimalistas + paradigma personaje: [`ficcion-hero-archetypes.md`](ficcion-hero-archetypes.md)
- Catálogo de modalidades visuales M1-M6: [`ficcion-hero-archetypes.md § Modalidades visuales`](ficcion-hero-archetypes.md)
- Template canónico v2 painterly: [`asset-catalog.md § 5.bis`](asset-catalog.md)
- Skill que implementa el algoritmo: [`.claude/commands/ficcion-draft.md § Hero`](../../.claude/commands/ficcion-draft.md)
- Tracking en registro: [`content/registro-ficciones.md`](../../content/registro-ficciones.md) columna `Comp.`
- Memoria del cambio: [`.claude/memory/feedback_ficcion_composiciones_canon.md`](../../.claude/memory/feedback_ficcion_composiciones_canon.md)
