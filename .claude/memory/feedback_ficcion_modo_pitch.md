---
name: /ficcion-draft modo pitch — formato canónico de exploración pre-escritura
description: Desde 2026-04-24 /ficcion-draft tiene modo `pitch` que genera documento de exploración estructurado (10 bloques, cada uno con opción elegida + variantes) antes de comprometerse a redactar. Rafael elige, reinvoca con semilla refinada.
type: feedback
originSessionId: 7a46d40c-fa61-4722-9cd1-c0d5e5642bda
---
Desde 2026-04-24 el skill `/ficcion-draft` admite modo `pitch` — un formato canónico de exploración pre-escritura que se activa con `/ficcion-draft pitch <semilla>` o con frases naturales tipo *"cuéntame más sobre X"* / *"explora el pitch de X"* / *"desarrolla X"*.

**Why:** Rafael hace brainstorming de relatos en sesiones espaciadas. Necesita ver decisiones importantes (personajes, localización, tono, estructura, finales, título) con **opción elegida + variantes razonadas** antes de quemar tokens en prosa. Separa *qué contar* de *cómo contarlo* y evita regenerar relatos completos cuando no le convence un personaje o un final. Patrón validado 2026-04-24 sobre la premisa #10 *El partido de los domingos*: Rafael pidió "cuéntame más", el skill respondió con 10 bloques estructurados, Rafael pidió canonizar el formato como paso del pipeline.

**How to apply:**

- **Trigger:** `/ficcion-draft pitch <semilla>` o cualquier variante natural de exploración pre-escritura ("cuéntame más", "explora X", "desarrolla X"). Si Rafael dice "escribe X" o "genera X" → NO es pitch, es redacción directa.
- **Template fijo — 10 bloques en orden:**
  1. El pulso (2-3 frases · tesis del relato · sin variantes)
  2. Anclaje canon (left-wall · big-lie · MRU con POV + tiempo verbal + triángulo asimetría)
  3. Geografía y personajes (localización + protagonista + secundarios + robot — cada uno con **elegido + 2-3 variantes**)
  4. Estructura propuesta (longitud + esqueleto de escenas, sin prosa)
  5. Por qué funciona (villano humano + cliffhanger emocional + resonancia lector ES 30-55)
  6. Finales posibles (tabla de 3 con elegido marcado + razón)
  7. Datos reales anclables (3-5 bullets verificables)
  8. Riesgos editoriales con antídotos operativos
  9. Título (elegido + 1 alternativa)
  10. Pregunta de cierre al usuario (qué decidir antes de reinvocar modo prosa)
- **Regla de forma:** cada bloque con variación presenta **opción elegida razonada + variantes descartadas** con media línea cada una. Nunca menú neutro — Rafael pidió decisión con criterio.
- **El skill NO escribe prosa en modo pitch.** Ni una frase que pueda ir literal en el relato final. El pitch describe, no ejecuta.
- **Output:** default = volcar en chat. Si Rafael pide *"guárdalo"* → escribir en `content/ficciones/_pitches/<slug>.md` con frontmatter `estado: pitch`. Al reinvocar `/ficcion-draft one-shot <slug>` el skill lee el pitch como contexto.
- **Ejecutar solo pasos 0 + 0.5 del workflow.** Saltar pasos 2-9 (character bible, framework, prosa, anti-IA, castellano-es grep, audiolibro, output). Esos se ejecutan en la reinvocación posterior con modo de redacción.
- **Anti-IA §1 + castellano peninsular §§ 3 + 3.bis** aplican al propio pitch. El skill habla en voz plural editorial ROBOHOGAR, no en voz narrativa del relato.

**Incidente origen:** 2026-04-24, brainstorming de 10 temáticas → Rafael elige #10 *El partido de los domingos* → pide "cuéntame más" → skill genera exploración estructurada (pulso + anclaje canon + 3 finales con elegido + riesgos + título alternativo) → Rafael pide canonizar ese formato y meterlo al pipeline. Documento canónico en `.claude/commands/ficcion-draft.md § Modo pitch — formato canónico de exploración`.
