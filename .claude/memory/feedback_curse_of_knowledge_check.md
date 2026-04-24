---
name: Curse of knowledge — check pre-output ROBOHOGAR
description: Regla pre-output basada en Steven Pinker (The Sense of Style, Harvard) integrada en pipeline ROBOHOGAR 2026-04-19. Acrónimos, modelos, jerga y regulaciones con contexto en primera mención. Aplica a artículos y narrador de ficción; se relaja en diálogo.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
**Concepto** — Steven Pinker, *The Sense of Style*: *"the difficulty that we all have in knowing what it's like not to know something that we know"*. El autor experto asume contexto que el lector no tiene; frases obvias para el autor quedan opacas para el lector.

**Regla ROBOHOGAR.** En primera mención dentro de un artículo o prosa narrativa:

- **Acrónimos** expandidos o contextualizados: `LiDAR (sensor láser 360°)`, `AI Act (reglamento europeo de IA)`, `PVP (precio venta recomendado)`, `ToF`, `CE`, `SmartThings`, `Matter`.
- **Modelos** con marca + categoría + año: `"el Dreame X50 Ultra, aspirador gama alta 2026"`, no solo `"el X50"`.
- **Jerga en inglés** traducida: `mopping` → fregado · `auto-wash` → autolavado · `auto-empty` → autovaciado · `edge cleaning` → limpieza de bordes.
- **Conceptos regulatorios/técnicos** con 1 línea de contexto: homologación CE, tarifa PVPC, protocolo Zigbee, banda 2.4 GHz.

En segundas menciones se puede usar abreviado. No es infantilización: es claridad.

**Test operativo.** *"¿Un vecino de 55 años, interesado en tecnología pero no técnico, entiende esta frase al primer pase?"*. Si no → reescribir.

**Excepciones.**
- **Diálogo de ficción** se relaja: un personaje puede hablar con la jerga que le toque, es verosímil. La regla aplica al **narrador**, no a la voz del personaje dentro de comillas/guiones.
- **Segundas menciones** ya contextualizadas no requieren repetir la expansión.

**Why:** ROBOHOGAR se dirige a adultos 30-55 ES interesados en tecnología doméstica pero no técnicos. El pipeline tenía la regla de audiencia definida en `editorial.md` pero sin diagnóstico accionable "qué doy por sabido aquí". Sin check explícito, la voz deriva a "agregador técnico" que asume el vocabulario de Xataka/ReviewsWars. Pinker nombra el problema y da el test accionable.

**How to apply — pre-output obligatorio:**
- `/content-draft § 9 Prohibiciones` incluye checklist curse-of-knowledge (acrónimos · modelos · jerga · conceptos).
- `/ficcion-draft § 8.2` aplica la regla al narrador, no al diálogo.
- `.claude/rules/editorial.md § Curse of knowledge` es la fuente de verdad.

**Descartado del vídeo original** (Steven Pinker, David Perell 2025-06-04, *How to Write*) y no reabrir:
- Read-aloud test como paso obligatorio (riesgo paso muerto si se salta con prisas).
- Test reader humano pre-publish (no aplica en F1 0-50 subs; diferido a F2 cuando haya target reales).
- Rhythm/sibilance/alliteration (pulido anglo no rentable para hobby 3-5h/semana).

**Referencias:**
- Vídeo analizado: https://youtu.be/nBQPnvmaNcE (David Perell · Steven Pinker · 828K views · 43:29)
- Regla aplicada: `@.claude/rules/editorial.md § Curse of knowledge` · `@.claude/commands/content-draft.md § 9` · `@.claude/commands/ficcion-draft.md § 8.2`
