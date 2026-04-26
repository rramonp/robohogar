---
name: Ficciones Domésticas — hook de apertura obligatorio + variedad obligatoria
description: Todo relato Ficciones Domésticas abre con gancho fuerte estilo cold open HBO/teaser YouTube; 24 hooks canónicos en taxonomía; no repetir mismo hook en últimos 5 relatos
type: feedback
originSessionId: 1363f11e-911b-47a2-a370-a214bfc70430
---
Toda Ficción Doméstica de ROBOHOGAR (one-shot, episodio-serie, episode-0, piloto, tie-in, sin excepción de longitud) abre con un **gancho fuerte** en el primer párrafo (idealmente la primera frase) que provoque al lector la necesidad de seguir hasta el final para saber qué ha pasado, cómo se ha llegado ahí o qué decisión se va a tomar. Estilo objetivo: **cold open de piloto HBO · teaser de YouTube · primer párrafo de cuento literario peninsular**, no apertura ambiental neutra ni resumen biográfico. **Variedad de hooks entre relatos obligatoria**: no repetir el mismo tipo concreto en los últimos 5 relatos publicados (combinando one-shots y episodios de serie).

**Why:** Rafael lo pidió como prioridad máxima 2026-04-26 con palabras literales: *"quiero que nuestros relatos tengan siempre un gancho inicial, que ocurra algo que haga que el lector quiera leerlo entero para saber qué ocurre al final, ya sea un evento impactante, una gran pregunta, un presente al que queremos saber cómo se ha llegado, etc. Estilo hook de YouTube o piloto de serie de HBO. Reitera sobre esto, quiero muchas posibilidades con una regla fija para el futuro, no quiero que siempre se repitan las mismas situaciones, esto es primordial."* — el énfasis en "primordial" y "regla fija" y "no se repitan las mismas situaciones" son lo que la convierte en regla dura, no en preferencia. ROBOHOGAR ya repite sello tonal (40% inquietante), voz peninsular literaria, villano humano y ancla 2030-2040; si encima repite tipo de hook, el lector recurrente baja la guardia. La variedad de hooks es lo que mantiene el músculo de "esto va a engancharme aunque ya conozca la marca". Auditoría retroactiva al canonizar la regla: 8 relatos publicados/draft con 5 tipos de hook distintos pero ya con dos repeticiones dentro de la ventana de 5 (B3 en #2 y #5 separados por 2 relatos; C3 en #3 y draft *La llave inglesa* separados por 4 relatos) — exactamente el patrón que la regla nueva evita.

**How to apply:**

1. **Catálogo canon de 24 hooks en 6 familias** (A Evento detonante · B Pregunta-enigma · C Estructura temporal · D Voz-forma · E Personaje · F Atmósfera-mundo) en [`references/ficciones/hooks-taxonomia.md`](../../references/ficciones/hooks-taxonomia.md). Cada hook lleva descripción, lógica narrativa, ejemplo canónico (sin marcas comerciales reales) y tabla de encaje por categoría tonal. Lista cerrada de **8 anti-patterns prohibidos** como apertura en § 5 (apertura ambiental sin tensión, resumen biográfico, filosofía declarativa, *"Todo empezó cuando…"*, primera frase explicativa del universo, pregunta retórica al lector, presentación con adjetivos, descripción del robot como decorado).
2. **Frontmatter obligatorio:** `hook_type: <Letra><Número> <Nombre canónico>` (ej: `A4 Ruptura mínima de rutina`). Sin él, el output del skill se bloquea.
3. **Skill `/ficcion-draft § 5.7`:** paso nuevo entre outline (5.5 Arquitectura lectora) y prosa (6 MRUs). Lee taxonomía + lee últimas 5 filas de `content/registro-ficciones.md` columna `Hook` → propone 3 candidatos no usados recientemente con razón explícita → Rafael elige o sobrescribe → registra en frontmatter.
4. **Regla de variedad — DURA:** no repetir mismo hook concreto en los últimos 5. Excepción documentada en `arco-serie.md` (sello de serie declarado) o `PASOS.md` (tie-in con artículo). Sin justificación → cambiar.
5. **Validación pre-output (`§ 9`):** (a) `hook_type` declarado; (b) hook concreto fuera de los últimos 5 o excepción documentada; (c) primera frase / primer párrafo coincide con el hook declarado y no cae en anti-pattern del § 5 (lectura manual obligatoria).
6. **Registro como single source of truth:** `content/registro-ficciones.md` lleva columna `Hook` (publicados + drafts pre-pub). El skill consulta esa tabla, no lleva tracker propio.
7. **Archivo vivo:** si tras feedback editorial Rafael identifica un patrón de apertura que engancha y no encaja en ninguno de los 24 actuales, se añade como G1/G2/… o se amplía la familia más cercana, documentando origen y ejemplo canónico.

**Diferencia con regla preexistente:** antes había bullet "Hook de primera frase" en `ficcion-draft.md § 6` y validación "el primer período debe provocar 'una más'" en § 9. Era textura, no regla dura: 6 hooks en `writewithai/07 § 5` sin tracking de variedad ni catálogo canon, ningún anti-pattern explícito, ninguna obligación de declarar tipo en frontmatter. La regla nueva (a) amplía a 24 tipos con familias semánticas, (b) hace obligatorio declarar tipo concreto en frontmatter, (c) prohíbe explícitamente 8 anti-patterns y (d) instituye tracking de no-repetición vía registro.

**Relación con cliffhanger:** hook de apertura + cliffhanger emocional de cierre (`@references/ficciones/serialized-newsletter-patterns.md § 3.4` + `editorial.md § Narrativa especulativa § Cliffhanger`) son las **dos puntas del mismo contrato con el lector**. El hook lo engancha, el cliffhanger lo deja con peso para el relato siguiente. Reglas hermanas, no redundantes.

**Pipeline canonizado 2026-04-26:**
- `references/ficciones/hooks-taxonomia.md` (creado, 24 hooks canon)
- `.claude/rules/editorial.md § Narrativa especulativa` (regla dura añadida)
- `.claude/commands/ficcion-draft.md § 5.7 + § 6 (Hook de apertura) + § 9 (Validaciones finales)` (3 puntos actualizados)
- `content/registro-ficciones.md` (columna Hook + backfill 8 relatos)
