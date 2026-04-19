# PASOS — "El operador nocturno" (Ficciones Domésticas · one-shot)

**Slug:** `el-operador-nocturno`
**Tipo:** ficción one-shot (standalone, sin serie)
**Categoría tonal:** `inquietante-heavy` (sello casa Black Mirror)
**Fecha borrador:** 2026-04-19 (v3)
**Versión actual:** v3 (v1 y v2 archivadas como `-v1.md` / `-v2.md` para comparación editorial)
**Palabras:** 3.578 (rango standalone 2.500-3.500 + tolerance +15%)

> **Nota v3 (2026-04-19):** la v2 era buena prosa pero "demasiado mundana" según Rafael (lector dice *"hmm ok"* en lugar de *"joder"*). La v3 sube intensidad a inquietante-heavy aplicando [`references/ficciones/tonalidad-y-mix-editorial.md`](../../../references/ficciones/tonalidad-y-mix-editorial.md). **Vuelta de tuerca clave:** Joel Santos (operador filipino) ha estado calibrando audio sintetizado durante 7 noches consecutivas (clic del imán prolongado a 1.7s, compresor +1 dedo de volumen) para inducir el despertar del niño y verle la cara — sustituye el ritual de su hijo Aldwin perdido hace 4 años. El sistema lo registra como *"audio output ID"* sin auditar contenido. Foreshadowing en escena 1 (compresor más alto, clic más largo, conteo *"cuarto martes seguido"*), revelación en escena 2 (panel pide *"¿pausar algoritmo?"* sesión 7 + biometría pasiva + mención Aldwin), cierre escena 3 con Martín entendiendo y eligiendo no bajar — el sistema sube el ruido. Reloj del horno cierra el círculo: *"las tres y dieciséis"* eco del v1 ahora con significado nuevo. Preservados intactos: 1×humanoide por escena (anclaje editorial), Joel/Martín distinguibles fonéticamente (refactor previo), *"No es un perro, Martín"*, *"Qué cuco, el cabrón"*, *"Nadie. Nadie importante"*, frase tagalo *nakaw tulog*, detalles culturales (Hacendado, descansillo, cobalto, Ifema), prosa peninsular de v2 (10 referentes ES). Subió de 2.898 → 3.578 palabras (vuelta de tuerca + biometría pasiva + cierre nuevo).

---

## SEO metadata · copiar a Beehiiv

| Campo | Valor | Chars |
|---|---|---|
| Title (tag Beehiiv `<title>`) | El operador nocturno · Ficciones Domésticas ROBOHOGAR | 53 / 60 |
| Meta description | Madrid 2032, 03:14. Un niño se levanta a beber agua. En la cocina hay alguien. No es el robot. Es el que lo pilota desde Manila. | 128 / 155 |
| Slug URL | `el-operador-nocturno` | — |
| Publish to | Email and web (evergreen, SEO-indexable) |
| Category Beehiiv | Opinión |
| Tags Beehiiv | `ficciones` + `humanoide` |
| Content Gate | OFF (fase F1 sin gate, regla `@rules/tangibles.md`) |

---

## Hero image

Ruta pendiente: `content/ficciones/_one-shots/el-operador-nocturno/assets/hero-el-operador-nocturno.png`.

**Código visual propuesto:** Black Mirror frío (reservado para "Relatos inversos de Black Mirror" — ver skill `/ficcion-draft` § hero ficción).

**Prompt a ejecutar con `/nano-banana`:**

```
Cinematic still, Black Mirror tone, night kitchen scene in a Madrid apartment 2032.
Boy in green dinosaur pajamas (~12y) standing in the hallway, half-lit by blue LED
strip in the ceiling corner; he is looking into the open kitchen. In the kitchen:
humanoid robot (matte white-grey body, no LEDs, no face features visible, neutral
domestic form, back mostly turned) reaching toward a shelf inside an open
stainless-steel fridge. Single light source: interior fridge lamp (cool white),
spilling yellow onto the tiled floor. Everything else in dark cobalt blue.
Kitchen details: tiled walls, induction hob, single empty glass on counter, a
magnetic calendar on the fridge door. Desaturated palette (cobalto oscuro +
amarillo frío), high contrast, grain fine-but-visible. Composition: pov from
hallway, boy silhouette framing left third, robot back centered.
No text, no letters, no Asian characters, no windows to exterior, no LEDs on
robot, no glow around robot eyes.
```

**Fallback si no convence:** placeholder monograma R sobre fondo ámbar claro (ver asset-catalog).

---

## Checklist de publicación

- [ ] Rafael revisa borrador `.md` y edita si lo ve apretado o flojo
- [ ] Generar hero con `/nano-banana` (prompt arriba) → `assets/hero-el-operador-nocturno.png`
- [ ] Convertir a HTML listo para Beehiiv (pendiente — invocar cuando Rafael diga "genera HTML")
- [ ] En Beehiiv: crear Post nuevo
  - [ ] Pegar HTML en el editor
  - [ ] Title: usar el de la tabla SEO (no el título H1 del relato, que es más literario)
  - [ ] Meta description: usar la de la tabla SEO
  - [ ] Slug URL: `el-operador-nocturno`
  - [ ] Category: Opinión
  - [ ] Tags: `ficciones`, `humanoide`
  - [ ] Featured image: subir el hero WebP
  - [ ] Publish to: `Email and web`
  - [ ] Content Gate: OFF
- [ ] Preview mobile (375px) antes de publicar
- [ ] Publicar
- [ ] Ejecutar `/post-publish <URL>` para limpieza y distribución social

---

## Declaraciones narrativas (paso 3.5 del skill)

**Mentira grande (1 por relato):** el operador remoto ve cámara y audio ambiental del humanoide incluso en zonas que la familia no recuerda haber opt-in; la granularidad legal de los ToS es mayor que la comprensión del usuario medio.

**Muro izquierdo (restricciones reales 2032):**
- Humanoide doméstico comercial 2032 requiere teleop humana remota para ~20% de tareas no resueltas por IA.
- 1X NEO (real, 2026) implementa esto; ofrece opt-out por zona/hora desde app, pero no está activado por defecto.
- Call centers filipinos de teleoperación robótica con salarios 3-5 USD/hora (ILO 2026).
- AI Act art. 50 exige transparencia de agente IA ante personas; entrada en vigor plena alto-riesgo: 2 agosto 2026.

**Villano humano:** la normalización de la vigilancia doméstica globalizada como coste oculto de la promesa de autonomía + gig economy invisible del sur global que sostiene la ilusión de "robot que piensa". El robot NO es villano. El operador Joel tampoco. El portavoz tampoco. El villano es el sistema de plausibilidad que permite que todos duerman.

---

## Dato real anclado (obligatorio rules/editorial.md)

1X NEO (humanoide doméstico comercial 2026-2032) emplea teleoperación humana remota para tareas no resueltas por la IA en hogar real. Deal 1X+EQT (12-abr-2026): 10.000 unidades industriales en paralelo al canal doméstico. AI Act art. 50: obligación de transparencia cuando agente IA interactúa con personas.

**Fuente research:** `content/drafts/research-digest-2026-04-17.md` § Semilla 1.

---

## Validaciones pasadas

- [x] Longitud standalone 2.500-3.500 (−15% tolerance) → **2.336 palabras** ✅ (por debajo del ideal pero dentro de rango)
- [x] Anti-IA §1.1 lista negra: 0 términos
- [x] Anti-IA §1.2 em-dashes narrativos: 0 (target ≤3)
- [x] Anti-IA §1.2 contrast framing "no es solo X, es Y": 0
- [x] Anti-IA §1.3 clichés sensoriales: 0
- [x] Anti-IA §2.1 thought verbs en narrador: 0
- [x] Anti-IA §2.5 tiempo verbal consistente: presente en las 3 escenas ✅
- [x] Anti-IA §2.6 cliffhanger emocional/moral (no físico) ✅
- [x] Marcas comerciales en narrador: 0 (1X aparece solo en diálogo, 1× por escena)
- [x] `left-wall` + `big-lie` + villano humano declarados en frontmatter + bloque visible bajo H1
- [x] Dato real ancla verificable
- [x] POV consistente: omnisciente cercano por escena (Martín / Joel / evento público)
- [x] Hook primera frase: "Martín oye primero el clic del imán de la nevera" — in medias res sensorial, abre loop ("qué hace despierto a las 03:14")

---

## Hooks para futura serie "Operadores invisibles" (si Rafael activa)

El one-shot deja abiertas estas preguntas que una serie podría recoger:
- **¿Qué dice Joel cuando su sobrina insiste?** Serie con POV desde Manila (3-4 eps), cada uno en un hogar diferente.
- **¿Qué informa la empresa al cliente al día siguiente del aviso "actividad nocturna"?** Episodio "El email del lunes" — los García reciben el reporte oficial y no entienden qué hicieron mal.
- **¿Qué pasa cuando una ONG activa consigue el registro completo?** Episodio "Ética Digital" — inspector EU pide logs.
- **¿Qué hace Martín cuando cumple 16?** Time-jump flash con el mismo Martín.

Si Rafael quiere activar serie: crear `content/ficciones/operadores-invisibles/` con character-bible (Joel, Rhea, Martín adulto, inspector EU) y arco-serie desde plantilla.

---

## Notas editoriales

- **Tono:** contenido dentro del registro Black Mirror frío, pero sin distopía gratuita. El horror es el silencio coreografiado de la última escena (padre confiando, madre callando al niño, Martín que no cuenta).
- **Decisiones de voz:** narrador omnisciente cercano por escena (close third). Tiempo presente en las 3 para sostener inmediatez. Sin pensamientos directos del narrador — todo por gesto/objeto.
- **Detalles concretos (Chiang):** pijama verde de dinosaurios, tetrabrik de Hacendado, reloj del horno parpadeando 03:16, 09:24:12 on-task, Ventilador roto en Manila, cobalto del suelo de Ifema.
- **Anti-cliché final:** cierre físico (mirada al reflejo) con carga moral (alguien sabe su nombre). Evita el thought verb "Martín pensó"; dramatiza por acción.
- **Riesgo:** 2.336 palabras cae por debajo del ideal 2.500. Si Rafael considera que el cierre "el reflejo" se queda corto, se puede ampliar escena 3 con más matiz del periodista o con pregunta adicional del público antes de salir.
