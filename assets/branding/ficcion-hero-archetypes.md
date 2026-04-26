# Hero de ficción — catálogo de archetypes compositivos

Catálogo canónico de variaciones compositivas para heros de Ficciones Domésticas. Nace 2026-04-24 tras feedback de Rafael: los primeros 4 one-shots cayeron en la misma receta mecánica (mesa + mano humanoide entrando por la derecha + objeto central-izquierda + luz cálida de lámpara lateral). El canon "portada minimalista · objeto-testigo" de [`asset-catalog.md § 5`](asset-catalog.md) es el **ADN fijo de la serie**; este archivo define **las 15 composiciones distintas** que pueden habitar ese ADN sin romperlo.

## Principio editorial — serie vs relato

La **serie** (Ficciones Domésticas) se reconoce por el ADN fijo: fondo azul noche `#1E2A3A` + superficie doméstica + luz cálida lateral + objeto-testigo + toque sintético sutil + cero texto/neón/asiático. Ese ADN vive entre todos los heros — es el sello Fitzcarraldo adaptado.

El **relato** se distingue por la composición: geometría del encuadre, estado del objeto, presencia o ausencia de figura humanoide, tipo de luz. Dos heros consecutivos que comparten objeto-testigo distinto pero MISMA composición (mesa + mano derecha) dan impresión de "mismo libro con dos etiquetas" en thumbnail. Dos heros consecutivos con objetos-testigo distintos y composiciones distintas dan impresión de "serie con variedad" — que es lo que queremos.

La dirección de arte es eso: conservar el sello, romper la repetición.

## Anatomía del hero — lo fijo, lo variable

| Elemento | Fijo (igual en toda la serie) | Variable (cambia por archetype) |
|---|---|---|
| Fondo | Pared matte `#1E2A3A` completamente bare/unmarked | Cantidad de pared visible; puede cortarse por otros planos |
| Superficie doméstica | Siempre alguna (encimera, parquet, mesilla, cama, suelo, estante) | Tipo, material, textura, ángulo, cantidad en el frame |
| Paleta | Azul noche + ámbar cálido como único color-luz | Intensidad y dirección del ámbar (lateral, cenital, backlight, ausente) |
| Objeto-testigo | 1 por relato (Chekhov's gun) | Escala, posición, estado (entero/roto/envuelto/caído/reflejado), tratamiento |
| Toque sintético | **Siempre presente** (no opcional) · matte cream-white · sin LEDs ni glow · justificado narrativamente | Tipo (mano / fragmento / silueta / ausencia / sombra), posición |
| Texto / neón / caracteres asiáticos | Nunca | Nunca |
| Profundidad | Macro o shallow DOF sobre elemento principal | Qué elemento está en foco cambia por archetype |

### Regla dura "cotidiano + sci-fi" (ADN irrenunciable)

> **La miniatura de un relato es SIEMPRE imagen cotidiana del día a día con un toque de ciencia ficción o robótica humanoide que rompa la tendencia que se esperaba de algo cotidiano.** Sin excepción. Regla canonizada por Rafael 2026-04-24, pedida dos veces. Ver memoria [`feedback_ficcion_hero_cotidiano_mas_scifi`](../../../RRP-DEV/.claude/memory/feedback_ficcion_hero_cotidiano_mas_scifi.md).

Consecuencia sobre el catálogo: **la familia C (presencia humanoide) NO es opcional**. Todo hero lleva al menos un fragmento de C — C1, C2, C3, C4 o C5. El toque puede ser **explícito** (mano / silueta / fragmento corporal) o **indirecto** (percha vacía con forma de uniforme humanoide, cable de carga matte, tarjeta ID, sombra humanoide proyectada) — nunca ausente.

Un archetype con **solo objeto + solo luz** (p. ej. A2·B1·D.i puro, o A5·B1·D.i puro) se rechaza antes de generar. Si el archetype "natural" del relato es solo objeto, se le suma C5 (ausencia marcada) como toque indirecto.

## Las 4 familias + 15 archetypes

Cada archetype combina una variable de **Encuadre (A)**, una de **Sujeto principal (B objeto / C humanoide)** y una de **Luz (D)**. El ADN fijo nunca se toca.

### Familia A — Encuadre (5 variantes de cámara)

**A1 · Lateral eye-level**  
Cámara a la altura de la mesa/superficie. Plano horizontal. Canon por defecto — el que usan actualmente Café, Operador, La objeción v1/v2.  
**Firma visual a thumbnail:** pared arriba + superficie abajo cortando horizontal, sujeto en línea media.  
**Rango tonal:** inquietante, mundano, ambiguo.

**A2 · Cenital / top-down**  
Cámara perpendicular al suelo mirando abajo. El objeto se lee como composición geométrica plana. El toque sintético entra normalmente como dedo único / cable / sombra desde un borde del frame (no mano entera).  
**Firma visual:** lectura de mapa, objeto flotando sobre fondo de color plano.  
**Rango tonal:** radical, inspirador, ambiguo — ritual, ceremonial, contemplativo.

**A3 · Ángulo bajo desde el suelo**  
Cámara a 5-15 cm del suelo mirando arriba. El horizonte queda alto en el frame: mesilla, borde de mesa, esquina del sofá corta por arriba. La superficie ocupa la diagonal, no el tercio inferior.  
**Firma visual:** perspectiva infantil / animal / humanoide caído. Dramática, poco doméstica.  
**Rango tonal:** radical, inquietante — historias de desajuste de poder, miedo, caída.

**A4 · A través de marco**  
La escena se ve a través de una puerta entreabierta, un umbral, una ventana interior, un cristal de vitrina. La habitación real queda pequeña, rodeada por la oscuridad del "marco".  
**Firma visual:** matryoshka espacial, sensación de espiar o de descubrir.  
**Rango tonal:** inquietante, ambiguo — secretos, espionaje, puntos de vista no autorizados.

**A5 · Extreme macro**  
Detalle obsceno del objeto o del elemento sintético. Rosca del tetrabrik, tejido del mantel, tornillo de una articulación, veta de madera. El fondo azul apenas aparece fuera de foco.  
**Firma visual:** textura pura, fondo azul bokeh sin geometría definida.  
**Rango tonal:** mundano, inquietante — el detalle que revela todo.

### Familia B — Estado del objeto (5 variantes del objeto-testigo)

**B1 · Objeto único completo**  
El objeto-testigo entero, en reposo sobre la superficie. Canon por defecto.  
**Firma visual:** silueta limpia, legible al instante.

**B2 · Ausencia / huella**  
El objeto NO está en el hero — pero su ausencia sí. Percha vacía donde había un uniforme, hueco en el estante, marca cuadrada clara sobre pared por un cuadro descolgado, silla vacía frente a mesa puesta, impresión del cuerpo en un cojín. El toque sintético puede estar o no.  
**Firma visual:** el peso dramático lo lleva el vacío. Pregunta mental del espectador: "¿qué había aquí?".  
**Rango tonal:** inspirador (serenidad de despedida), inquietante (desaparición), radical (sacrificio consumado).

**B3 · Roto / dividido / desmontado**  
El objeto partido, desmontado en dos o tres partes, despiezado sobre la superficie como autopsia. Una pieza sintética puede estar presente como herramienta o como responsable.  
**Firma visual:** simetría rota o serie ordenada de piezas.  
**Rango tonal:** radical, inquietante — violencia contenida, diagnóstico, duelo.

**B4 · Envuelto / cubierto / oculto**  
El objeto parcialmente tapado (tela, papel, bolsa, funda, periódico), solo se adivina la forma. Silueta por contorno, no por detalle.  
**Firma visual:** misterio, algo que se esconde o se protege.  
**Rango tonal:** ambiguo, inquietante.

**B5 · Reflejado / duplicado**  
El objeto se refleja en una superficie (café, cristal, pantalla apagada, espejo de tocador, bandeja de acero) y el reflejo muestra algo que no debería: una mano humanoide ausente, una figura al fondo que no está en el primer plano, una sombra de más.  
**Firma visual:** dos objetos, uno real, uno imposible.  
**Rango tonal:** radical, ambiguo — realidades que no encajan.

### Familia C — Presencia humanoide (5 variantes del toque sintético)

**C1 · Mano lateral entrando por el borde**  
Mano sintética matte cream-white entra por un lado (derecha canónico, izquierda aceptable) del frame. Solo hasta el antebrazo. Palma abajo o en gesto concreto (tocando / suspendida / agarrando). Canon por defecto de los primeros one-shots.  
**Firma visual:** intrusión puntual, elemento sintético pequeño respecto al objeto.  
**Rango tonal:** inquietante, ambiguo.  
⚠ **No usar 2 relatos consecutivos con C1.** Es el archetype que causó el incidente de "heros idénticos".

**C2 · Silueta encogida al fondo**  
El humanoide completo, en plano medio desenfocado al fondo de la habitación, sentado en rincón o de pie apoyado en pared, actitud de abandono / espera / reposo. Canon ya en uso (Setenta y dos horas v3).  
**Firma visual:** figura humana secundaria pero inquietante; regla de tercios compuesta.  
**Rango tonal:** inquietante, radical, mundano.

**C3 · Silueta de espaldas al viewer**  
Humanoide cream-white sentado o de pie **de espaldas** al espectador, ocupando 1/3 - 1/2 del frame sin cara visible. Mira el objeto-testigo, una ventana, la pared, una silla. No podemos leer su expresión.  
**Firma visual:** masa humana sin identidad; silueta anónima grande.  
**Rango tonal:** ambiguo, inspirador, radical — la humanidad sin cara.

**C4 · Fragmento corporal aislado**  
Solo una parte del humanoide: un pie matte sobre parquet, una rodilla, una placa torácica desmontada sobre la mesa, un brazo colgando del borde del sofá, una pieza de cable-tendón suelto junto al objeto.  
**Firma visual:** sinécdoque — la parte por el todo, con peso narrativo de lo que no vemos.  
**Rango tonal:** inquietante, radical, mundano.

**C5 · Ausencia / sombra / eco**  
El humanoide no está en el frame. Su presencia se siente por: una sombra proyectada sobre el objeto desde off-frame, una silla de cargador vacía, un cable de carga suelto sobre el parquet, una huella de talón matte en el polvo, una tarjeta ID colgando de un gancho en la pared.  
**Firma visual:** solo objeto + indicio de humanoide que se ha ido o está por llegar.  
**Rango tonal:** inspirador, ambiguo, radical — aplicable a finales catárticos o en los que el humanoide es memoria.

### Familia D — Luz (5 moduladores tonales)

**D.i · Lateral cálida ámbar (default)**  
Lámpara doméstica off-frame superior izquierda. Ámbar cálido solo sobre objeto + patch estrecho de superficie. Sombras alargadas a la derecha. Canon por defecto.

**D.ii · Backlight / contraluz**  
Fuente de luz detrás del sujeto. Objeto y humanoide aparecen silhouetted contra la pared azul con un halo ámbar fino de rim light. Apenas detalle en las caras frontales.  
**Uso:** tono radical, revelación, gravedad. Reduce carga figurativa, aumenta carga simbólica.

**D.iii · Luz desde abajo**  
Pantalla apagada, hornilla, LED de base. La luz cálida o blanquecina viene desde el suelo o desde el propio objeto. Sombras de abajo-arriba invertidas.  
**Uso:** inquietante, radical — ritualidad extraña, fuego de hoguera doméstica.

**D.iv · Luna fría plateada**  
Reemplaza el ámbar cálido por luz blanca-plateada de luna desde una ventana off-frame. La pared azul aparece más saturada. No hay fuente doméstica de calor.  
**Uso:** radical, inquietante, onírico — historias de insomnio, fantasma, vigilia.  
⚠ **Solo si el relato lo pide explícitamente.** Rompe el patrón ámbar que cohesiona la serie; usar con moderación.

**D.v · Luz textura / celosía / cortina**  
La luz atraviesa una celosía, una persiana entreabierta, una cortina, una lámpara con pantalla rajada, una reja de ventilación — y proyecta un patrón rítmico sobre el objeto y la superficie. Sigue siendo ámbar cálido.  
**Uso:** ambiguo, mundano con tensión — escena de verano, siesta cargada, interrogatorio.

## Los 15 archetypes canónicos (combinaciones ya validadas)

Cada archetype es una combinación predefinida **A × (B o C) × D**. Son las 15 plantillas listas para usar. Si un relato pide una combinación fuera de estas, el skill la construye ad-hoc y la añade aquí si funciona.

| # | Nombre corto | A · encuadre | B/C · sujeto | D · luz | Tonalidad sugerida | Ejemplo-diferencial |
|---|---|---|---|---|---|---|
| 01 | **Mesa · mano lateral** | A1 | C1 | D.i | inquietante, mundano | Café v3, La objeción v2 (canon default) |
| 02 | **Mesa · objeto con indicio sintético** | A1 | B1 + **C5** (tarjeta ID, cable carga, sombra, percha) | D.i | mundano, inquietante | Operador v6 (tetrabrik + tarjeta ID) |
| 03 | **Mesa · roto** | A1 | B3 | D.i | radical, inquietante | Autopsia, duelo |
| 04 | **Mesa · reflejo imposible** | A1 | B5 | D.i | radical, ambiguo | Café con mano reflejada que no está |
| 05 | **Cenital ritual** | A2 | B1 o B4 + **C1-cenital / C4 / C5** | D.i o D.ii | radical, inspirador | Bandera/tela plegada top-down + mano entrando desde borde superior o tarjeta ID depositada |
| 06 | **Cenital autopsia** | A2 | B3 + **C4** (pieza mecánica entre los fragmentos) | D.ii | radical | Piezas desmontadas en mesa de acero + fragmento humanoide |
| 07 | **Parquet bajo · humanoide encogido** | A1 | C2 | D.i | radical, inquietante | Setenta y dos horas v3 |
| 08 | **Silueta de espaldas** | A1 | C3 | D.i o D.ii | ambiguo, inspirador | Humanoide mirando ventana o objeto |
| 09 | **Ausencia · percha vacía** | A1 | C5 (con B2) | D.i | inspirador, inquietante | Percha sin uniforme, objeto solo |
| 10 | **Umbral · vista por puerta** | A4 | B1 + C2 o solo B1 | D.i | inquietante, ambiguo | Habitación al fondo enmarcada |
| 11 | **Ángulo bajo · pies** | A3 | C4 (pies/tobillos) | D.i | radical, inquietante | Pies matte desde suelo, objeto alto |
| 12 | **Macro textura** | A5 | B1 (detalle) + **C4 o C5** | D.i o D.v | mundano, inquietante | Tejido, rosca, veta extrema + cable matte / sombra / fragmento |
| 13 | **Celosía ámbar** | A1 o A3 | B1 | D.v | ambiguo, mundano tenso | Siesta, interrogatorio, verano |
| 14 | **Contraluz silueta** | A1 | B1 o C3 | D.ii | radical, inspirador | Objeto perfilado contra pared |
| 15 | **Luna fría** | A1 | B1 o C3 | D.iv | radical, onírico | Insomnio, fantasma, vigilia |

## Algoritmo de selección por tonalidad

El skill `/ficcion-draft` asigna tonalidad al relato (canon 40/15/25/10/10: inquietante · radical · ambiguo · inspirador · mundano). `/nano-banana` en modo ficción usa esa tonalidad como filtro primario sobre los 15 archetypes:

| Tonalidad del relato | Archetypes recomendados |
|---|---|
| **Inquietante** (40%) | 01, 02, 04, 07, 10, 11, 12 |
| **Radical** (15%) | 03, 05, 06, 07, 11, 14, 15 |
| **Ambiguo** (25%) | 04, 08, 10, 13 |
| **Inspirador** (10%) | 05, 08, 09, 14 |
| **Mundano** (10%) | 02, 07, 12, 13 |

## Regla dura anti-repetición

**Ningún archetype puede aparecer en 2 heros consecutivos del mismo grupo** (one-shots y cada serie cuentan como grupo independiente). El skill verifica antes de generar:

1. Leer `asset-catalog.md § 5 · Registro de heros ficción` y ver la columna `Archetype #` del último hero del mismo grupo.
2. Excluir ese número del pool de archetypes candidatos para el nuevo hero.
3. Si el relato encaja tonal y narrativamente solo en un archetype ya usado, forzar modulación — cambiar la luz (D) o el elemento secundario del archetype para que la silueta a thumbnail 120px se distinga claramente del anterior.

Meta de variedad: en los primeros 10 heros publicados, deben aparecer al menos 6 archetypes distintos. Si se llegan a 10 heros con 3 archetypes o menos, se revisa el algoritmo.

## Prompt fragments por archetype

Fragmentos en inglés listos para componer el prompt. Se ensamblan sobre el esqueleto canónico de [`asset-catalog.md § 5 · Prompt template canónico`](asset-catalog.md#prompt-template-canonico) — reemplazando las partes marcadas con `[...]`. El fondo, la luz base y los anti-triggers (sign-guard, no-LEDs, no-text) se mantienen SIEMPRE.

Guía de uso: el agente lee el archetype, copia el **fragmento de encuadre (A)** + el **fragmento de sujeto (B o C)** + el **fragmento de luz (D)** y los integra en el template canónico respetando el orden. Si hay conflicto (p. ej. A2 cenital + C1 mano lateral no casa físicamente), se resuelve por la lógica espacial: la mano entra desde un borde del frame cenital, no lateral.

### Encuadre (A)

```
# A1 · lateral eye-level
Camera at table height, horizontal frame, horizon line dividing frame in thirds.

# A2 · cenital / top-down
Camera directly overhead looking straight down at the [SUPERFICIE], objects read as a flat graphic composition on the dark blue-gray painted surface.

# A3 · ángulo bajo desde el suelo
Camera placed at floor level looking slightly upward, the edge of the [MESILLA/MESA/SOFÁ] cutting high in the frame, the dark blue-gray wall filling the top half.

# A4 · a través de marco
The entire scene is framed by a partially open doorway / interior window / glass cabinet seen from an adjacent darker room, the actual scene appears small in the center surrounded by the dark frame of the foreground opening.

# A5 · extreme macro
Extreme macro close-up of [DETALLE ESPECÍFICO DEL OBJETO], shallow depth of field rendering the dark blue-gray wall as a smooth bokeh background, almost no geometric detail visible beyond the detail itself.
```

### Objeto (B)

```
# B1 · objeto único completo
[OBJETO-TESTIGO] resting whole on the [SUPERFICIE], placed slightly off-center according to rule of thirds, clean silhouette.

# B2 · ausencia / huella
[HUECO CONCRETO] where [OBJETO] used to be: for example, an empty wooden coat hanger mounted on the dark blue-gray wall keeping the exact shape of a uniform that is no longer there; or a rectangular patch of slightly cleaner paint on the wall where a framed picture hung for years; or the deep impression of a head on a pillow nobody currently occupies. The object itself is absent from the scene.

# B3 · roto / dividido
[OBJETO-TESTIGO] broken into two or three distinct pieces laid out on the [SUPERFICIE] as if in an autopsy, the fragments arranged in a deliberate line or triangle, a small metallic tool (not a hand) resting between them.

# B4 · envuelto / cubierto
[OBJETO-TESTIGO] partially wrapped in [MATERIAL: linen cloth, brown paper, newspaper, fabric sleeve], only the silhouette and a small hint of its surface visible through the covering.

# B5 · reflejado / duplicado
[OBJETO-TESTIGO] resting on the [SUPERFICIE REFLECTANTE: stainless steel counter, dark coffee surface, polished wood, turned-off tv screen, vanity mirror], and its reflection in that surface shows a [ELEMENTO SINTÉTICO IMPOSIBLE: a matte cream-white humanoid hand, a seated figure in the corner] that is not present in the primary scene above.
```

### Humanoide (C)

```
# C1 · mano lateral por un borde
A single matte white prosthetic humanoid hand entering from the [LADO: right / left] side of the frame, only the hand and part of the forearm visible, plain matte cream-white with subtle articulated segments at the knuckles and wrist, no glowing parts, no LEDs, no lights, no panels, no colored accents.

# C2 · silueta encogida al fondo
In the blurred out-of-focus background: the silhouette of a matte cream-white humanoid figure seated crumpled on the floor against a corner of the dark blue-gray wall, knees drawn up, head tilted forward as if powered off, completely still, no glowing parts, no LEDs, plain matte surface.

# C3 · silueta de espaldas
A matte cream-white humanoid figure seated or standing with its back fully turned to the camera, occupying about one third of the frame vertically and roughly half of its width, the back of the head and shoulders visible but no face, attention directed at [OBJETO o PARED], plain matte cream-white surface, subtle articulated joints, no glowing parts, no LEDs.

# C4 · fragmento corporal aislado
A single [PART: matte cream-white humanoid foot / forearm / disassembled torso plate / loose cable-tendon] resting on the [SUPERFICIE] near the [OBJETO-TESTIGO], plain matte cream-white surface, subtle articulated detail at the joints, no glowing parts, no LEDs.

# C5 · ausencia / sombra / eco
No humanoid figure is visible. Instead, [INDICIO ESPECÍFICO: a humanoid-shaped shadow projected across the object from off-frame left / an empty charging dock on the floor with the cable coiled neatly / a blank plastic ID card hanging from a hook on the wall / a single matte cream-white heel print in a patch of fine dust on the floor].
```

### Luz (D)

```
# D.i · lateral cálida ámbar (default)
Warm domestic lamp light from the upper left, off-frame, casting a narrow amber highlight only on [SUJETO PRINCIPAL] and a narrow patch of [SUPERFICIE], long soft shadows extending to the right.

# D.ii · backlight / contraluz
Warm backlight from behind the subject, rendering [OBJETO / HUMANOIDE] as a silhouette against the dark blue-gray wall with only a thin amber rim light outlining the top edge, very little frontal detail.

# D.iii · luz desde abajo
Warm light coming from below, originating from [FUENTE: a stove flame just out of frame / an open laptop screen on the surface / a nightlight on the floor], casting upward shadows across the objects and the lower portion of the wall, creating an inverted lighting pattern.

# D.iv · luna fría plateada
Cool pale silvery-white moonlight entering from an off-frame window, no warm amber present, the dark blue-gray wall reads slightly more saturated, no domestic lamp active.

# D.v · luz textura / celosía
Warm amber light filtered through a slatted blind / a lace curtain / a lamp shade with irregular holes, projecting a rhythmic pattern of bright bars and shadows across [OBJETO] and [SUPERFICIE].
```

## Integración con skills

- **`/nano-banana` modo ficción:** antes de generar, leer este archivo y el registro de heros en `asset-catalog.md § 5`. Elegir archetype según (a) tonalidad del relato, (b) regla anti-repetición vs último hero del grupo, (c) compatibilidad espacial entre fragmentos A/B/C/D. Ensamblar prompt desde el esqueleto canónico + los 3 fragments elegidos.
- **`/ficcion-draft`:** al cerrar el draft, en `PASOS.md § Hero` anotar qué archetype propone (A·B/C·D) y por qué, para que `/nano-banana` lo recoja sin reinterpretación.
- **`asset-catalog.md § 5 · Registro de heros ficción`:** añadir columna "Archetype" (número 01-15 o combinación A·B/C·D si es ad-hoc) para hacer cumplir la regla anti-repetición.

## Grupo `personaje-acción-imposibilidad` — canon paralelo 2026-04-26 PM

> **Catálogo nuevo paralelo a los 15 archetypes minimalistas de arriba.** Ese sigue siendo válido (paradigma `minimalista` · canon § 5 de [`asset-catalog.md`](asset-catalog.md)). Lo que sigue es el paradigma `personaje-acción-imposibilidad` (canon § 5.bis) que se convierte en **default** desde 2026-04-26 PM para one-shots y miniseries futuras. Las series activas con código declarado (Amparo, Ronda 3, MAIA) no usan este grupo — mantienen su código existente. El paradigma `minimalista` queda como opción declarativa cuando un relato tiene un objeto-testigo aislado más fuerte que cualquier personaje en frame (ej: *La objeción* tela ceremonial).

**Por qué grupo paralelo y no extender los 15 archetypes:** los 15 archetypes minimalistas tienen ADN específico (objeto-testigo aislado, fondo azul 2/3 superior, regla "cotidiano + sci-fi sutil" sin personaje en primer plano). El nuevo paradigma rompe ese ADN compositivo (personaje en primer plano, fondo azul 1/3 superior, objeto-imposibilidad **materializado** no sutil). Mezclarlos en una misma tabla destruiría la lógica de anti-repetición. Solución: **dos grupos independientes** que comparten paleta + estilo fotográfico + dimensiones + anti-sign-guard pero no comparten composición.

### ADN del paradigma personaje-acción-imposibilidad (recordatorio canon § 5.bis)

| Elemento | Especificación |
|---|---|
| **Personaje** | Identificable por rol/oficio/atrezzo en primer plano · pose dinámica (no contemplativa) |
| **Acción visible** | Verbo del `display_title` traducido visualmente (forjando · cosiendo · ajustando · firmando · vigilando) |
| **Objeto-imposibilidad** | Materializado físicamente (humo de color · líquido luminoso · partículas que escriben · luz que escapa · humanoide en gesto incoherente) |
| **Composición** | Personaje en una zona, objeto-imposibilidad a contrapunto, foco lumínico ámbar diagonal sobre la unión |
| **Fondo** | Azul `#1E2A3A` matte plain unmarked en tercio superior (reducido vs minimalista 2/3) |
| **Look fotográfico** | Still-life cinematográfico (After Yang / Hammershoi / Wenders) — **NO** oil painting / digital painting / cartoon |
| **Identidad de figuras públicas (banda D)** | Por rol y atrezzo solamente · **nunca cara reconocible de figura real** · regen si Gemini la mete |

### Las 5 bandas de personaje

El paradigma se subdivide en 5 bandas según el universo del personaje. La banda determina (a) el atrezzo identificador, (b) el escenario doméstico/laboral, (c) la convención de identidad real (banda D especialmente).

#### Banda A — Oficios domésticos / familia / cotidiano

Personajes del entorno familiar y del hogar. Atrezzo: delantal, mandil de cocina, bata casera, gafas de leer, pijama, pantuflas, herramienta doméstica (sartén, tenedor, paño). Escenario: cocina, salón, dormitorio, pasillo de piso, cuarto infantil. Edad: cualquiera.

| Banda A # | Archetype concreto | Atrezzo / pose | Objeto-imposibilidad |
|---|---|---|---|
| A-01 | Cuidador/a en cocina hirviendo caldo | Mandil + cucharón en mano + cabeza ladeada hacia humanoide encogido | Caldo del que sale humo en forma de palabras o frases |
| A-02 | Niño/a en cuarto frente a aspirador | Pijama + linterna en mano + arrodillado frente a aspirador domóstico | Aspirador trazando con su sensor la sombra de un perro o gato ausente |
| A-03 | Anciano/a en sillón frente a humanoide vigilante | Bata + libro abierto + humanoide cream-white sentado al lado en posición vigilancia | Objeto cotidiano (taza, gafas) levitando entre ambos como si dudara de a quién pertenecer |
| A-04 | Yaya/yayo en mesa con humanoide pidiendo comida | Mantel de hule + cuchara llena de cuchareada hacia humanoide + plato vacío en centro | Humanoide imitando el gesto de comer con la boca abierta sin nada que llevarse |
| A-05 | Nieta/o reprogramando humanoide dormido | Pijama de adolescente + portátil + cable conectado a humanoide cream-white tendido en cama | Letras de código saliendo del cable como humo dorado |

#### Banda B — Trabajadores reconocibles del día a día ES

Personajes de oficios cotidianos del paisaje laboral español, identificables por uniforme/atrezzo. Atrezzo: chaleco de cajera, mochila isotérmica de rider, bata de tienda, pijama sanitario, mono industrial, llaves de portería, mandil de papelería. Escenario: súper, portal, finca, aula, taller, oficina pequeña. Edad: típicamente 25-55.

| Banda B # | Archetype concreto | Atrezzo / pose | Objeto-imposibilidad |
|---|---|---|---|
| B-01 | Cajera de súper escaneando humanoide cliente | Chaleco corporativo + mano sobre lector de barras + humanoide cream-white frente al mostrador | Ticket impreso saliendo del lector que se hace cada vez más largo, palabras visibles en serpentina |
| B-02 | Rider de delivery en portal frente a humanoide vecino | Mochila isotérmica al hombro + bolsa en mano + humanoide cream-white abriendo desde el otro lado | Bolsa que pesa progresivamente más al subir el peldaño |
| B-03 | Conserje de finca frente a buzonera con humanoide haciendo cola | Bata azul de conserje + bolígrafo en mano + humanoide cream-white delante de la cola | Cartas en la buzonera con remitentes que ya no existen (fallecidos) |
| B-04 | Profesora de instituto frente a tablet de alumno | Camisa+chaqueta + tiza en mano + tablet de alumno mostrando voz humanoide en pantalla | Tiza que escribe sola en la pizarra mientras la profesora la sostiene quieta |
| B-05 | Operario/a de mantenimiento frente a humanoide desmontado | Mono industrial naranja + destornillador en mano + humanoide cream-white abierto sobre banco | Tornillos flotando en arco ámbar entre las dos manos del operario |
| B-06 | Teleoperador/a en penumbra frente a holograma | Auriculares + cabeza inclinada + sala oscura + holograma de cuerpo humano lejano | Reloj detrás del operador con manecillas que avanzan al revés |
| B-07 | Técnica del SAS frente a humanoide en consulta | Pijama sanitario azul + estetoscopio + humanoide cream-white en camilla | Estetoscopio escuchando sonido de oleaje en lugar de latido |

#### Banda C — Funcionarios y oficios públicos

Personajes con función pública o administrativa. Atrezzo: corbata sobria, americana, sello, ventanilla, expediente abierto, número de turno, chaleco fluorescente municipal. Escenario: ventanilla administrativa, despacho municipal, sala registral, mostrador SEPE, oficina de Hacienda, calle pública con vehículo de servicio. Edad: 30-60.

| Banda C # | Archetype concreto | Atrezzo / pose | Objeto-imposibilidad |
|---|---|---|---|
| C-01 | Interventora municipal firmando expediente con humanoide | Americana + bolígrafo en mano + humanoide cream-white sentado frente a la mesa | Papel del expediente cuyo número en la cabecera cambia cada vez que se firma |
| C-02 | Agente SS frente a humanoide cuidador a punto de jubilarse | Camisa institucional + carpeta abierta + humanoide cream-white de pie con hoja de servicios | Carpeta que al abrir muestra solo páginas en blanco |
| C-03 | Técnica de Hacienda frente a humanoide declarando | Americana + sello en mano + humanoide cream-white sentado con tablet | Sello que se gasta hasta hacerse transparente sin marcar el papel |
| C-04 | Subinspectora SEPE frente a humanoide en cola | Chaqueta gris + pantalla con número de turno + humanoide cream-white esperando | Pantalla cuyo número de turno retrocede en lugar de avanzar |
| C-05 | Registradora civil frente a humanoide pidiendo nombre | Bata oscura + pluma estilográfica + humanoide cream-white inclinado frente al mostrador | Pluma escribiendo en una lengua extinta o glifos desconocidos |
| C-06 | Trabajador municipal con chaleco fluor frente a humanoide en calle | Chaleco fluorescente naranja + escoba o cono de obra + humanoide cream-white retirado a un lado de la calzada | Farola que se enciende sola sin pulsador, ámbar en pleno día |

#### Banda D — Figuras públicas por rol

Personajes con función política, jurídica, sindical o diplomática reconocible **por rol y atrezzo**, no por cara real. Atrezzo: chaqueta de protocolo, atril institucional, escudo abstracto, micrófono de pleno, corbata con pin abstracto, martillo de juez, pancarta sindical. Escenario: sala de pleno, sala de protocolo, juzgado, asamblea sindical, sala diplomática. Edad: 40-70 típicamente.

**Regla dura de identidad:** la cara del personaje **no debe parecerse a figura pública concreta**. Si Gemini genera cara reconocible (Sánchez, Feijóo, Díaz, Abascal, Ayuso, Belarra, etc.) → regenerar. Atrezzo institucional sí permitido (escudo abstracto del Congreso, atril sin logos identificables, micrófono institucional sin marca). El `display_title` correspondiente NO menciona nombre propio real.

| Banda D # | Archetype concreto | Atrezzo / pose | Objeto-imposibilidad |
|---|---|---|---|
| D-01 | Ministra/o en sala vacía de Congreso cargando humanoide | Chaqueta de protocolo + cable de carga conectado a enchufe institucional + humanoide cream-white de pie | Atril que multiplica la voz del personaje aunque no esté hablando |
| D-02 | Alcalde/sa en pleno municipal con humanoide tomando acta | Pin solapa abstracto + bolígrafo + humanoide cream-white sentado al lado tomando notas | Acta cuyas líneas se reescriben solas mientras el alcalde habla |
| D-03 | Sindicalista en asamblea con humanoide entre compañeros | Chaqueta vaquera + megáfono + humanoide cream-white sentado entre obreros humanos | Pancarta cuyo texto cambia cada vez que la cámara la mira |
| D-04 | Juez/a en sala con humanoide testigo | Toga negra + martillo levantado + humanoide cream-white de pie en el estrado | Martillo que pesa cada vez más, brazo del juez tembloroso por el peso |
| D-05 | Embajador/a en sala protocolaria con humanoide traduciendo | Chaqueta de protocolo + copa en mano + humanoide cream-white inclinado hacia oído de visita | Cáliz que vierte luz dorada en lugar de líquido |

#### Banda E — Cultura pop / mediática

Personajes del ecosistema mediático y de cultura pop reconocibles por entorno y atrezzo (set, anillo de luz, vestuario deportivo, partitura, micrófono). Atrezzo: anillo de luz de streamer, sudadera con merch, equipación deportiva genérica (sin colores de equipo real), partitura, micrófono de podcast, gafas de presentadora. Escenario: setup de streaming, vestuario deportivo, plató de tertulia, estudio de podcast, backstage de concierto. Edad: 18-50.

**Regla complementaria:** equipación deportiva **sin colores ni escudo de equipo real** (azul/blanco genérico, no Real Madrid; rojo/azul genérico, no Barça). Camisetas de selección genérica sin números reales de jugadores actuales.

| Banda E # | Archetype concreto | Atrezzo / pose | Objeto-imposibilidad |
|---|---|---|---|
| E-01 | Influencer streamer en setup con anillo de luz y humanoide | Sudadera + auriculares + anillo de luz redondo + humanoide cream-white sentado al lado imitando reacción al chat | Pantalla con métrica de viewers subiendo en vacío (sin viewers visibles, solo número creciente) |
| E-02 | Futbolista en vestuario con humanoide masajista | Equipación genérica azul/blanca + bota en mano + humanoide cream-white masajeando otra pierna | Bota que late con luz interna como si tuviera corazón |
| E-03 | Presentadora de tertulia con humanoide tertuliano | Vestido de plató + auricular invisible + humanoide cream-white sentado en silla giratoria de mesa | Reloj del programa que adelanta saltando minutos |
| E-04 | Podcaster económico en estudio con humanoide invitado | Camisa abierta + micrófono de pie + humanoide cream-white frente a otro micrófono | Micrófono que sigue grabando descolgado de cualquier soporte, suspendido en aire |
| E-05 | Cantante en backstage con humanoide vocalista de respaldo | Vestuario de gira + partitura en mano + humanoide cream-white de pie con micrófono auxiliar | Partitura cuyas notas se borran de la página cada vez que el cantante intenta leerlas |
| E-06 | Periodista de pie de calle con humanoide entrevistado | Plumífero corporativo + micrófono + humanoide cream-white respondiendo en plaza pública | Cable del micrófono que gira sobre sí mismo formando bucles imposibles |

### Algoritmo de selección por categoría tonal + display title

El skill `/ficcion-draft § 8.x Hero` (paradigma personaje-acción-imposibilidad) sigue este algoritmo:

1. Leer del frontmatter: `categoria-tonal:` + `display_title:` + `display_title_family:` + `Perfil POV` (de tabla del registro).
2. Filtrar bandas por compatibilidad con el `Perfil POV` y con el rol/oficio que sugiere el `display_title`.
3. Cruzar con la categoría tonal para acotar archetypes:
   - **Inquietante** (40%): A-01, A-03, B-03, B-06, C-04, C-05, D-01, D-04, E-01, E-04
   - **Radical** (15%): A-04, B-05, C-02, C-06, D-02, D-04, E-05
   - **Ambiguo** (25%): A-02, A-05, B-01, B-04, C-03, D-05, E-02, E-06
   - **Inspirador** (10%): A-04, B-07, C-01
   - **Mundano** (10%): A-05, B-04, C-03, E-03
4. Aplicar regla anti-repetición acotada al paradigma personaje-acción-imposibilidad:
   - Excluir archetypes presentes en últimos 5 heros del paradigma.
   - Verificar que la banda candidata no haya dominado los últimos 3 (no encadenar 3 relatos en misma banda).
5. Proponer 3 candidatos a Rafael con razón explícita (banda + archetype + objeto-imposibilidad propuesto).
6. Tras decisión, ensamblar el prompt usando el template canónico § 5.bis de [`asset-catalog.md`](asset-catalog.md) sustituyendo `[PERSONAJE]`, `[ACCIÓN VISIBLE]`, `[OBJETO-IMPOSIBILIDAD]`, `[SUPERFICIE/ESCENARIO]`.

### Anti-repetición acotada al grupo

**Regla dura 1 — archetype:** ningún archetype concreto (A-01, B-03, etc.) puede aparecer en 2 heros consecutivos del paradigma personaje-acción-imposibilidad. Excepción documentada en `arco-serie.md` solo si una serie tiene un archetype como sello editorial declarado.

**Regla dura 2 — banda:** no encadenar 3 relatos seguidos en la misma banda. Si los últimos 2 fueron banda A, el siguiente debe rotar a B/C/D/E. Si los últimos 2 fueron de bandas distintas, libertad total para el siguiente. Excepción documentada igual que arriba.

**Meta de diversidad:** en los primeros 10 heros del paradigma personaje-acción-imposibilidad, deben aparecer las 5 bandas al menos una vez cada una. Si tras 10 heros una banda nunca ha aparecido, el skill bloquea las otras bandas hasta que el siguiente relato corresponda a la banda faltante (forzado de cobertura).

### Prompt fragments por banda

Fragmentos canónicos por banda para ensamblar en el template § 5.bis. Reemplazan placeholders `[PERSONAJE]`, `[ACCIÓN VISIBLE]`, `[OBJETO-IMPOSIBILIDAD]`, `[SUPERFICIE/ESCENARIO]`.

```
# Banda A — Oficios domésticos / familia
Foreground: A [woman / man / elder / child] in their [40s / 60s / 80s / under 12], wearing [domestic kitchen apron / robe / pyjamas with slippers / cardigan] visible from torso up, [actively stirring a pot / kneeling next to a vacuum / sitting in armchair tilted toward humanoid / spoon-feeding humanoid], face partially visible in soft amber light, expression of [worry / wonder / acceptance / curiosity].
Setting: a Spanish home interior — modest [kitchen with tiled splashback / living room with TV cabinet and family photos / bedroom with wooden frame / child's room with stuffed animals], plain dark blue-gray paint visible at the upper third of the frame.

# Banda B — Trabajadores reconocibles del día a día ES
Foreground: A [woman / man] in their [25-55], wearing [supermarket cashier vest with name tag / delivery insulated backpack and helmet / building concierge blue jacket / teacher's blouse and cardigan / industrial overall in orange / sanitary pyjamas in light blue / nurse's tunic], face partially visible in soft amber light, [scanning at a barcode reader / handing a delivery bag / sorting mail at building lobby / writing on a small chalkboard / disassembling a humanoid on a workbench / wearing headphones in a dark teleoperation booth / examining a humanoid on a clinic bed].
Setting: a [small Spanish supermarket counter / building entrance hall with mailboxes / classroom corner / mechanic workshop bench / dim teleoperator booth / SAS clinic exam room], plain dark blue-gray paint visible at the upper third of the frame.

# Banda C — Funcionarios y oficios públicos
Foreground: A [woman / man] in their [35-60], wearing [civil servant blazer with discreet pin / SS social services collared shirt / Hacienda tax office formal jacket / SEPE employment office gray cardigan / civil registrar dark robe / municipal worker fluorescent vest], face partially visible in soft amber light, [signing a file with a fountain pen / holding an open folder / pressing an ink stamp / facing a number-display screen / writing in a registry book with a calligraphy pen / standing next to a streetlight].
Setting: a [public administrative office counter / SS service window / Hacienda desk with computer monitor / SEPE waiting hall / civil registry room with heavy wooden ledger / Spanish urban street at dusk], plain dark blue-gray paint visible at the upper third of the frame.
The character's face must NOT resemble any real Spanish public official.

# Banda D — Figuras públicas por rol
Foreground: A [woman / man] in their [45-70], wearing [protocol jacket with abstract lapel pin / formal blazer with discreet pin / vintage worker jacket with union pin / black judicial robe / diplomatic protocol suit], face partially visible in soft amber light — face anonymous, NOT resembling any real political or public figure — [adjusting microphone at podium / signing minutes in plenary chamber / addressing crowd from union assembly stage / raising a gavel in courtroom / receiving a guest in protocol hall].
Setting: an [empty Congress chamber with rows of seats / municipal plenary hall with semicircular tables / union assembly gymnasium with chairs in rows / wood-paneled courtroom / formal diplomatic reception hall], institutional shield kept abstract (no recognizable national flags or party logos), plain dark blue-gray paint visible at the upper third of the frame.
The character's face must NOT resemble any real public figure, politician, judge, or diplomat. Generic Mediterranean adult features only.

# Banda E — Cultura pop / mediática
Foreground: A [woman / man] in their [22-50], wearing [oversized merch hoodie with abstract design / generic blue-and-white sports kit without team crest or sponsor / tertulia panel set dress / open-collar podcast shirt / on-tour stage outfit / TV reporter weatherproof jacket], face partially visible in soft amber light, [adjusting ring light at streaming desk / sitting in locker room with boot in hand / hosting at panel table / speaking into a podcast microphone / reading sheet music backstage / holding microphone on a public square].
Setting: a [streamer setup with circular ring light and double monitor / generic sports locker room with metal lockers / TV tertulia round table set / podcast studio with acoustic foam / concert backstage with cases and cables / Spanish urban square at night with streetlights], plain dark blue-gray paint visible at the upper third of the frame.
Sports kit colors must NOT match any real Spanish football team. Generic colors only.
```

```
# Plantilla de objeto-imposibilidad (rellenar según display_title)
And on the [SUPERFICIE / next to the character / suspended above the surface]: [OBJETO-IMPOSIBILIDAD: smoke rising in colored tendrils that shape into letters / liquid that emits its own warm amber light from inside / particles writing words in mid-air / a household object releasing a beam of dawn-like golden light from inside / a humanoid figure in cream-white matte performing a gesture incoherent with its supposed function — eating from an empty plate, praying, taking notes on a blank notebook, masturbating an empty hand, breastfeeding a non-existent infant — pose deliberately wrong, eerie but not horror], slightly out of focus to create an oneiric effect distinct from the sharply focused character. The impossibility-object is the visual translation of the paradox in the story's display title.
```

## Revisión futura del catálogo

- Si en las próximas 10 generaciones aparecen composiciones no cubiertas por los 15 archetypes, canonizar el nuevo archetype como 16, 17, etc. con su fila en la tabla.
- Si un archetype se revela difícil para Gemini (genera reiteradamente text / neon / asian characters pese a las anti-triggers), documentarlo aquí como "prohibido por modelo" hasta que cambie.
- Si Rafael validará una composición totalmente fuera del canon (rompiendo ADN fijo), ese hero NO se canoniza aquí; se trata como excepción editorial puntual y se documenta como tal en `asset-catalog.md`.
- Lo mismo aplica al grupo `personaje-acción-imposibilidad`: si en las próximas 10 generaciones aparecen archetypes nuevos por banda, canonizar como A-06, B-08, C-07, etc. en la tabla correspondiente.
