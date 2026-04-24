---
name: Componer ES directo en ficción ROBOHOGAR, no traducir del inglés (Calcos 13-22)
description: Regla estructural para /ficcion-draft — escribir castellano peninsular literario desde el primer token, no traducir. Incidente canónico 2026-04-20 con 5 calcos + ampliación 2026-04-24 con calco 22 (frase relativa descriptiva ↔ adjetivo ES).
type: feedback
originSessionId: e9873eca-e420-4e4a-8520-aa5fe0ef3c72
---
**Regla principal:** el skill `/ficcion-draft` compone prosa de ficción **en castellano peninsular literario desde el primer token**. Prohibido pensar una frase en inglés y traducirla. Prohibido usar plantillas narrativas anglosajonas traducidas.

**Why:** incidente editorial 2026-04-20. El relato `el-que-viene-a-tomar-cafe` v2 pasó las 25 validaciones ✅ del skill (incluidas las 5 verificaciones sintácticas anti-calco: posesivos redundantes, "de repente", adverbios -mente, pasiva ser+participio, conectores anglo). Rafael detectó leyendo **dos frases básicas sin sentido** que no caían en ninguna categoría cubierta:

- *"El centro de demostración fue en septiembre"* — calco léxico de *demo center / demonstration center*.
- *"vio la escena en boca de una actriz contratada para hacer de abuela"* — *"en boca de"* es expresión verbal ES aplicada a contexto visual/performativo.

Auditoría posterior detectó ~10 casos más del mismo tenor: voz técnica de manual en narrador doméstico (*"configurado cero"*, *"ha cruzado con las fotos"*, *"lanzó la actualización"*), colocaciones idiomáticas forzadas (*"vigilando de medio lado"* vs ES canónico *"de reojo"*), microcopy anglo en app ficticia (*"No, gracias"* vs ES *"Ahora no"*). La raíz no era falta de validación sino **método de composición**: se traducía del inglés en vez de componer directamente en ES.

Rafael literal: *"no deberías de estar traduciendo del inglés al castellano. Deberías tener el knowledge necesario aplicado en tu repositorio para saber cómo escribir en español directamente, no traduciendo todo el tiempo"*.

**How to apply:**

- **Antes de escribir** la primera frase del paso 6 (prosa) del skill: releer [`references/ficciones/castellano-literario-es.md §§ 3, 3.bis, 4`](../../../robohogar/references/ficciones/castellano-literario-es.md) (17 calcos a evitar + 5 casos canon + 12 recursos ES positivos). Activar como guía de composición, no como checklist a posteriori.
- **Durante la redacción:** si una frase suena a traducción (se releeería dos veces, tiene sabor a "elegante pero raro"), DESCARTAR LA FRASE entera y reescribirla desde cero con sintaxis ES nativa. No parchear calco por calco — reestructurar.
- **Antes del output:** correr los 17 greps de `/ficcion-draft § 8.3` (ya incluye los nuevos 13-17). Si algún grep devuelve match ambiguo (calcos 14, 15 y 17 dependen del contexto), LEER LA FRASE EN VOZ ALTA — el oído peninsular es el filtro definitivo.
- **Excepciones legítimas del calco 15 (voz técnica):** si el texto CITA el manual/la app/un comunicado corporativo (fricción de registros Morales §1.3 del knowledge ES), la voz técnica es correcta y buscada. Lo prohibido es que el narrador cercano al personaje la adopte sin ironía.

**Los 5 calcos nuevos (13-17) quedan canonizados en el knowledge:**

- Calco 13 · Sustantivos compuestos anglo *"X center/facility"* → omitir u nativizar.
- Calco 14 · Expresiones *"en [órgano] de [persona]"* en contexto no-verbal → verbo específico.
- Calco 15 · Voz técnica de manual en narrador doméstico → verbo doméstico ES.
- Calco 16 · Colocaciones idiomáticas forzadas → idiomática ES canónica (*"de reojo"* no *"de medio lado"*).
- Calco 17 · Microcopy UI anglo en ficción especulativa → microcopy ES realista (*"Ahora no"* no *"No, gracias"*).

La expansión de 12 a 21 es definitiva (v3 · 2026-04-20 tarde). El protocolo permanente (documentado en `castellano-literario-es.md § 3.bis`) establece que si se detecta una frase con "olor a traducción" no cubierta por los 21, se añade como caso canónico 6+ y se genera calco 22+ si procede.

**v4 · Self-learning activado** (2026-04-20 tarde). El validador `/validate-prose-es` ahora incluye **Fase 4 · Auto-catalogación**: cuando la Capa 2 (LLM) detecta un hallazgo no cubierto por los 21 calcos, automáticamente propone regex Unicode-safe + entry §3 + caso §3.bis + checklist §8.1 + grep skill §8.3. Auto-testea la regex contra el fixture canónico y el borrador validado. Si pasa los 3 tests, presenta a Rafael para OK/skip. Si Rafael aprueba, aplica los edits a los 4 archivos canónicos. Log permanente en `validator-reports/`.

**v5 · Calco 22 añadido** (2026-04-24). Origen: subtítulo SEO de *La objeción* contenía *"Tiene veintitrés días y un botón que no hace ruido"* — calco anglo `the X that doesn't [verb]` (descripción funcional vía relativa) cuando ES tiene adjetivo idiomático más conciso (*silencioso*, *mudo*, *perpetuo*). Detectado por Rafael leyendo el dek tras publicación; el validador v4 no lo cogió porque el patrón no estaba documentado. Fix aplicado: *"una alarma silenciosa"*. Calco 22 catalogado vía Fase 4 (no auto-propuesto por Capa 2 esta vez — propuesta editorial directa de Rafael; aplicado el mismo flujo de documentación: §3 grep + §3.bis caso 6 + skills updates). Tabla de equivalencias canónicas en `castellano-literario-es.md § 3.bis caso 6` (botón→silencioso, luz→perpetua, teléfono→mudo, puerta→cerrada, reloj→incansable, mano→inerte, ojo→fijo). Excepción legítima: relativa deliberadamente literaria/poética (*"el dios que no responde"*) — defender por intención.

Rationale del cambio (feedback Rafael 2026-04-20 tarde): el protocolo v3 decía *"cada fallo del validador que Rafael detecte se añade manualmente al knowledge"* — cuello de botella. Si Rafael no tiene tiempo o se le olvida, el grep queda estático. Self-learning elimina la dependencia del trabajo manual editorial. El LLM que detecta el fallo también documenta el patrón para el futuro. Safeguards: aprobación humana obligatoria + auto-test antes de proponer + máximo 1 propuesta por sesión (evita fatiga de aprobación).

**No duplicar aquí lo que está en el knowledge.** Esta memoria es el pointer + contexto del incidente. La fuente de verdad es [`references/ficciones/castellano-literario-es.md`](../../../robohogar/references/ficciones/castellano-literario-es.md) (§§ 3, 3.bis, 8.1) y la meta-instrucción en [`.claude/commands/ficcion-draft.md`](../../../robohogar/.claude/commands/ficcion-draft.md) (cabecera Workflow).
