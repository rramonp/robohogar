---
name: Ficciones Domésticas — sistema multinivel anti-auto-plagio (variabilidad inter-relatos)
description: Bloqueo duro de repetición en 4 ejes (POV/Setting/Conflicto/Cliffhanger) + tropos quemados + grep cruzado pre-output, instaurado tras detectar copy-paste literal de párrafo entre relatos
type: feedback
originSessionId: 1363f11e-911b-47a2-a370-a214bfc70430
---
Cada relato Ficciones Domésticas debe diversificar contra los últimos 5 publicados en CUATRO ejes estructurales (Perfil POV, Setting triple, Conflicto humano, Cliffhanger tipo) más la lista de tropos quemados (figuras retóricas, gestos, símiles, frases-fórmula). Si cualquier eje se repite o un tropo 🔴 QUEMADO aparece en el outline, el skill `/ficcion-draft` BLOQUEA el output antes de prosa. Validación grep cruzada `utilities/check_self_plagiarism.py` final detecta n-gramas ≥6 palabras coincidentes con relatos previos como blindaje adicional.

**Why:** Rafael lo pidió como prioridad máxima 2026-04-26 PM con palabras literales: *"Se han utilizado recursos literarios repetidos idénticos que en anteriores relatos… No digo la forma o la composición, sino directamente copy-paste. Esto es inviable. Quiero que podamos hacer una gran biblioteca de relatos de ciencia ficción y quiero que sean variables entre sí. No pueden tener copy-paste de figuras literarias o expresiones directamente idénticas o relatos que son estructuras prácticamente idénticas que solo cambian los nombres."* Su énfasis: *"que esto no vuelva nunca a ocurrir y se tenga en cuenta a la hora de escribir un nuevo relato."*

**Diagnóstico empírico** (auditoría 2026-04-26 con 3 Explore agents sobre 9 relatos):
- **Copy-paste literal** del párrafo "cafetera italiana + gluglú + geranios sin florecer + luz que no calienta" entre `el-que-viene-a-tomar-cafe.md` líneas 40-41 y `el-chaval.md` línea 56 (solo cambian nombres y mes).
- **Gesto pelusa-codo-dos-dedos** idéntico en 3 relatos.
- **Símil "humanoide = abrigo colgado en percha grande"** idéntico en 2.
- **Bata azul abrochada al revés** idéntica entre Soledad (#2) y Concha (#9).
- **Nombre Pilar** como protagonista en 2 relatos.
- 66% del catálogo en mismo conflicto humano (duelo+demencia+soledad-cuidadora) · 77% en mismo POV · 67% en misma postura humanoide · 78% en mismo arco narrativo.

**Causa raíz:** el knowledge base solo trackeaba 2 dimensiones de variedad (hooks de apertura — canonizada misma mañana — y categoría tonal). POV/setting/conflicto/cliffhanger/figuras retóricas estaban invisibles. El skill `/ficcion-draft` (924 líneas de prescripción + 10 referentes peninsulares contemplativos en `castellano-literario-es.md`) convergía defensivamente al molde validado anterior. Variabilidad superficial (nombre, ciudad), identidad estructural y léxica profunda.

**How to apply:**

1. **Tracking estructural** en [`content/registro-ficciones.md`](../../content/registro-ficciones.md): 4 columnas nuevas (`Perfil POV`, `Setting`, `Conflicto humano`, `Cliffhanger tipo`) con backfill de los 9 relatos. El skill consulta esa tabla en el nuevo paso `§ 5.6 Variability gate` antes de outline.
2. **Tropos quemados** en [`references/ficciones/tropos-quemados.md`](../../references/ficciones/tropos-quemados.md): registro vivo con 4 estados (🟢 LIBRE · 🟡 VIGILAR · 🔴 QUEMADO · ⚫ JUBILADO). Lista cerrada inicial 14 tropos saturados de la auditoría. Ventana de enfriamiento 5 relatos. Cada relato actualiza al cerrar añadiendo 5-10 figuras dominantes detectadas.
3. **Regla dura** en [`@.claude/rules/editorial.md § Variabilidad inter-relatos`](../rules/editorial.md): bloqueo duro en los 4 ejes. Excepción única documentada: sello de serie declarado en `arco-serie.md`.
4. **Skill `/ficcion-draft § 5.6 Variability gate`**: paso obligatorio entre arquitectura lectora (5.5) y hook (5.7). Calcula ejes saturados, valida outline, bloquea si repite.
5. **Skill `/ficcion-draft § 9` validaciones finales**: añadidos 3 checks (variabilidad 4 ejes · tropos quemados · grep cruzado) + actualización obligatoria del registro al cerrar.
6. **Script `utilities/check_self_plagiarism.py`**: detecta n-gramas ≥6 palabras (BLOQUEO) y 4-5 palabras (WARNING) entre el candidato y los M relatos previos. Stdlib only. UTF-8 output forzado para Windows. Confirmado funcional sobre el caso real (detecta los 37 matches del párrafo cafetera+geranios+luz).
7. **Diversificación voces ES** en [`castellano-literario-es.md § 1.bis`](../../references/ficciones/castellano-literario-es.md): 7 referentes adicionales (Manuel Vilas oral cómico-trágico · Almudena Grandes popular madrileño · Eduardo Mendoza comicidad seca · Mariana Enriquez terror doméstico · Fernando Aramburu coral moral · Patricio Pron prosa intelectualizada · Rafael Chirbes cinismo moral). Tabla de aplicación rápida por categoría tonal + POV.
8. **Reescritura quirúrgica de `El chaval` v2**: 6 zonas reescritas (cafetera+geranios+luz, pelusa-codo, bata-azul, postura-catálogo, gesto-servirse-café, fórmulas temporales) + cierre cambiado (ya no termina con "Carmen cierra los ojos" — tropo quemado). 2.754 palabras finales. Pasa el script grep cruzado con cero matches ≥6 palabras.

**Decisiones cerradas con Rafael 2026-04-26 PM:**
- Reescritura quirúrgica > descartar y rehacer.
- Ejecución todo de golpe (A+B+C) en una sola tanda.
- Bloqueo duro en los 4 ejes (no aviso blando).
- Los 7 referentes ES propuestos completos.

**Plan de origen:** [`C:/Users/bakal/.claude/plans/se-han-utilizado-recursos-scalable-duckling.md`](../../../.claude/plans/se-han-utilizado-recursos-scalable-duckling.md).

**Relación con regla hermana:** la regla de hooks de variedad (canonizada misma mañana 2026-04-26 en [`hooks-taxonomia.md`](../../references/ficciones/hooks-taxonomia.md)) es el primer eje de variabilidad. Esta regla añade los 4 ejes restantes (POV, Setting, Conflicto, Cliffhanger) + tropos quemados + grep cruzado. Juntas forman el sistema completo de "variabilidad inter-relatos" — 5 ejes estructurales + tropos + n-gramas.

**Uso para futuro escalado:** el sistema está pensado para soportar el catálogo de 15-20-50 relatos sin que la convergencia al molde reaparezca. Si Rafael detecta nueva forma de auto-plagio no cubierta, ampliar:
- El catálogo de tropos quemados (`tropos-quemados.md` es archivo vivo).
- Los 4 ejes estructurales (añadir 5º o 6º eje) con la misma forma de regla.
- Los referentes ES (`castellano-literario-es.md § 1.bis` admite añadir más voces).

**Audit retroactivo del catálogo** (visible en `content/registro-ficciones.md`):
- Repeticiones pre-regla detectadas: B3 hook en relatos #2 y #5 + C3 en #3 y draft `la-llave-inglesa` + nombre Pilar como protagonista en #2 y #8 + acto-irreversible-suspendido en #2, #4 y #6. Documentadas con ⚠️ en notas de la tabla. Esos relatos ya están publicados; las reglas aplican a futuros (excepto El chaval que se reescribió).

---

## Capa adicional 2026-04-26 PM tarde — Saturación de catálogo de voces

Tras canonizar el sistema anti-auto-plagio (4 ejes + tropos + grep cruzado), Rafael pidió validación complementaria: *"si te das cuenta de que se está quedando corto el número de autores españoles que hay dentro de Castellano literario es, sugiéreme aumentar el registro en más autores."* Es la misma lógica anti-saturación aplicada al **eje voz** (referente literario) que antes no estaba trackeado.

**Implementación** (todo dentro del sistema ya existente):

1. **Frontmatter de cada relato** declara `referente-principal: <Nombre>` (autor cuya voz literaria se ha tomado como guía dominante) + opcional `referente-secundario`. Backfill aproximado de los 9 relatos por inferencia documentado en `registro-ficciones.md` con marca `[inferido]`. A partir del relato 10, declaración explícita pre-prosa.
2. **Columna `Referente principal`** añadida a `content/registro-ficciones.md` (publicados + drafts).
3. **Heurística de detección** en [`castellano-literario-es.md § 2.bis.1`](../../references/ficciones/castellano-literario-es.md): 🔴 SATURACIÓN CRÍTICA si ≤2 referentes distintos en últimos 5 · 🔴 RACHA SATURANTE si mismo referente 3 consecutivos · 🟡 LEVE si <6 referentes en últimos 10 · 🟢 SANO si ≥8 distintos en últimos 10.
4. **Banco curado §2.bis.2** con 12 candidatos pre-analizados listos para activarse cuando se dispare saturación: 5 voces ES jóvenes/contemporáneas (Andrea Abreu · Sara Torres · Marta Jiménez Serrano · Almudena Sánchez · Edurne Portela), 5 voces ES canónicas mayores (Antonio Muñoz Molina · Javier Marías · Enrique Vila-Matas · Belén Gopegui · Marta Sanz), 2 voces latinoamericanas como excepción documentada (Samanta Schweblin · Mariana Travacio). Cada candidato con descripción de registro + qué aporta + cuándo activarlo + NO usar para. Banco vivo: amplía Rafael cuando descubra autores nuevos.
5. **Lista §2.bis.4 de descartados con razón documentada**: Carmen Martín Gaite (cubierto por Moreno/Mesa), Ana María Matute (registro mítico fuera de foco), Manuel Rivas (lírico-ensoñador choca con realismo duro), Camilo José Cela (anacrónico), Eduardo Halfon (fuera de foco temático), Pola Oloixarac (ya cubierto por Pron). El descarte es reversible si Rafael cambia de opinión.
6. **Skill `/ficcion-draft § 5.6.bis Saturación de catálogo`**: sub-paso del Variability gate (entre § 5.6 y § 5.7). Si SANO → silencio. Si LEVE → línea informativa sin bloquear. Si CRÍTICA o RACHA → INTERRUMPE flujo + reporta distribución + propone candidatos + da 4 opciones a Rafael (activar candidato del banco · activar referente del catálogo §1.bis no usado · seguir con el referente propuesto · ampliar banco con autor nuevo).
7. **Validación regresiva**: si Rafael acepta ampliar el banco con un autor nuevo, el skill lo añade automáticamente a §2.bis.2 con formato canónico. Si lo descarta, entra a §2.bis.4 como descarte documentado.
8. **Aviso de banco corto**: si el banco §2.bis.2 tiene ≤2 candidatos sin promover (porque otros pasaron a §1.tris), el skill avisa a Rafael — la regla es recursiva: la propia detección de saturación se aplica al banco también.

**Niveles de activación de un candidato del banco**:
- **Nivel A puntual**: el skill lo carga como referente dominante de un solo relato. Frontmatter + registro lo recogen. NO se mueve al catálogo activo.
- **Nivel B promoción**: tras 2-3 relatos puntuales validados, Rafael promueve el candidato a §1.tris (nueva sección con análisis literario completo: concepto + patrón + adoptar para ROBOHOGAR + NO usar para, formato §1.bis). Decisión editorial siempre de Rafael.

**Diagnóstico retroactivo del catálogo histórico (2026-04-26 PM)**:
- **Adón aparece como referente principal o secundario en 7 de 9 relatos (78%)** → muy por encima del umbral 🔴 SATURACIÓN CRÍTICA.
- Mesa en 4 de 9 (44%) · Urraca en 3 de 9 (33%).
- Solo 6 referentes distintos usados en los 9 relatos (sobre 17 disponibles en §1+§1.bis).
- 0 candidatos del banco §2.bis.2 activados todavía.
- Cuando se publique el relato 10, si vuelve a usar Adón → se cumple 🔴 RACHA SATURANTE (Adón en 4 de los últimos 5).

**Recomendación operativa para el siguiente relato (relato 10)**: ROTAR fuera de Adón/Urraca/Mesa. Buenos candidatos del banco según semilla:
- POV joven/adolescente → **Andrea Abreu** (canaria, voz oral popular)
- Conflicto político-laboral → **Belén Gopegui**
- POV mujer mayor con conciencia del cuerpo → **Marta Sanz**
- Humanoide cerebralmente raro → **Samanta Schweblin** (*Kentukis* es lectura obligatoria — escribió específicamente sobre cuasi-humanoides domésticos)
- Coral con focalización rotativa para Reset Libro 1 → **Aramburu** (ya en §1.bis pero solo usado en relato #1) o **Antonio Muñoz Molina** (banco)

**Recursividad del sistema**: la regla anti-saturación aplica a 5 dimensiones ahora — hooks (canonizado mañana 2026-04-26) · perfil POV · setting · conflicto humano · cliffhanger · **+ voz/referente literario** (canonizado tarde 2026-04-26). Si Rafael detecta una sexta dimensión que produzca convergencia en futuro, se añade siguiendo el mismo patrón: tracking en registro + heurística + banco curado + interrupción del skill al detectar.

---

## Capa adicional 2026-04-26 PM tarde-noche — Intensidad narrativa cinematográfica por defecto

Tras canonizar las dos capas anteriores (anti-self-plagio + saturación de voces), Rafael leyó *El chaval v2* y rechazó el resultado por motivo distinto a auto-plagio: **demasiado convencional, demasiado sutil**. Cita literal: *"todos los relatos parecen iguales… aquí no ha ocurrido nada y siempre parece que aquí no ha pasado nada. Necesito que pasen cosas en los relatos. Audionovelas en un newsletter de gente que está acostumbrada a vídeos de YouTube, etcétera. Por defecto quiero que ocurran más cosas."*

Es una capa **distinta** a la voz literaria — la voz peninsular contemplativa estaba bien escrita, pero la **estructura** (cuántos eventos, qué ritmo) se quedaba corta para audiencia que también consume YouTube/TikTok.

**Implementación** (todo dentro del marco del sistema ya existente):

1. **Nuevo archivo** [`references/ficciones/intensidad-narrativa.md`](../../references/ficciones/intensidad-narrativa.md) — matriz canon de 4 categorías (🎬 Cinematográfico 40% default · ⚡ Dinámico 35% · 🌫️ Atmosférico 20% · 🍵 Slice of life 5%) con definición operativa de "evento significativo" + tests + protocolo de aplicación.
2. **Frontmatter de cada relato** declara `intensidad-narrativa: <categoría>`. Sin él, output bloqueado.
3. **Columna `Intensidad`** añadida a `content/registro-ficciones.md` con backfill retroactivo de los 9 relatos. Diagnóstico histórico: 0% Cinematográfico · 44% Dinámico · 44% Atmosférico · 11% Slice — inversión necesaria respecto al target nuevo.
4. **Banco §2.bis.2 ampliado** con 4 referentes de género (Pierre Lemaitre, Don Winslow, Daniel Suarez, Eva García Sáenz de Urturi) específicamente para combinar con voz literaria peninsular cuando el relato sea Cinematográfico/Dinámico.
5. **Skill `/ficcion-draft § 5.6.tris Intensidad narrativa`**: paso obligatorio entre saturación de catálogo (§5.6.bis) y hook (§5.7). Calcula auto-balanceo del catálogo, propone categoría infrarrepresentada (default = Cinematográfico salvo override), valida que el outline tenga eventos suficientes para la categoría declarada antes de pasar a prosa. Si Cinematográfico declarado y solo hay 3 eventos → BLOQUEO.
6. **`/ficcion-draft § 9` validaciones finales**: añadidos checks de `intensidad-narrativa` declarada en frontmatter + lista de eventos en `PASOS.md § Eventos del relato` + (si Cinematográfico/Dinámico) las 4 condiciones específicas (decisión moral concreta + intervención del humanoide fuera de patrón + cliffhanger fuerte + ratio acción/atmósfera ≥75/25).
7. **Regla dura en `editorial.md § Narrativa especulativa`** con **default Cinematográfico** explícito.

**Reescritura de `El chaval v2` → `La Unidad v3`** (2026-04-26 PM tarde-noche):
- Cambio de nombre del humanoide: "el chaval" → **VELA-9 / "La Unidad"** (registro frío-administrativo, alias "Ribera" del técnico solo al final del relato como momento de bisagra emocional).
- Nuevo slug: `la-unidad`. Nuevo archivo `content/ficciones/el-gran-reset/2026-04-26-la-unidad.md`. v2 archivada en `_descartados/_DESCARTADO-2026-04-26-el-chaval-v2.md`.
- Estructura cinematográfica con **6 eventos significativos**: portero don Marcial con noticias urgentes · pelea + caída del Sr. Morales en el bordillo · ayuda a la víctima + Carmen vuelve con sangre en los nudillos · llamada Beatriz desde Berlín cortada por caída de redes 4G/5G · apagón + tres golpes en la puerta del 4ºB con Vega forzada como cebo + tercer hombre escondido revelado por la luz dirigida del humanoide · grito desde la séptima planta + La Unidad mira al techo.
- Hook A1 In medias res físico (apertura con Carmen subiendo escaleras de tres en tres con sangre en los nudillos, no es suya).
- Voz: Eva García Sáenz de Urturi (primaria, thriller peninsular accesible) + Don Winslow (secundaria, estructura de género escena breve y alternancia rápida) — primera vez que se activa banco §2.bis.2.
- 2.584 palabras (15-17 min TTS). Pasa script anti-plagio con cero matches ≥6 palabras tras mover v2 a `_descartados/`.
- Audiolibro v3 generado en vault Obsidian, v2 borrada del vault.

**Recursividad final del sistema (2026-04-26 cierre del día):** la regla anti-saturación + variabilidad ahora aplica a 6 dimensiones — (1) hooks, (2) perfil POV, (3) setting, (4) conflicto humano, (5) cliffhanger, (6) voz/referente literario. La regla de **intensidad narrativa** es la 7ª dimensión pero opera distinto: no es regla de no-repetición (todas las categorías son válidas) sino de auto-balanceo + default fuerte (Cinematográfico). Su sistema es matriz porcentual como el tono — no ventana de últimos 5 como las dimensiones 1-6.

**Lección operativa para el agente** (yo): cuando escriba un relato Cinematográfico/Dinámico, debo:
- Listar eventos significativos del outline ANTES de prosa (no improvisar).
- Pensar en la audiencia: oyente de audiolibro que también ve YouTube/TikTok, no lector literario.
- Mantener voz literaria peninsular cuidada PERO con estructura de género (escenas breves, alternancia rápida, cliffhanger fuerte, decisión moral del personaje, intervención del humanoide fuera de patrón).
- NO confundir "literario" con "atmosférico". Eva García Sáenz de Urturi es literaria. Lo es Lemaitre. Lo es Daniel Suarez. La voz cuidada NO está reñida con el ritmo cinematográfico — es lo que separa Audible americana pulp de un audiolibro ROBOHOGAR.
