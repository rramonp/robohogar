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

## Revisión futura del catálogo

- Si en las próximas 10 generaciones aparecen composiciones no cubiertas por los 15 archetypes, canonizar el nuevo archetype como 16, 17, etc. con su fila en la tabla.
- Si un archetype se revela difícil para Gemini (genera reiteradamente text / neon / asian characters pese a las anti-triggers), documentarlo aquí como "prohibido por modelo" hasta que cambie.
- Si Rafael validará una composición totalmente fuera del canon (rompiendo ADN fijo), ese hero NO se canoniza aquí; se trata como excepción editorial puntual y se documenta como tal en `asset-catalog.md`.
