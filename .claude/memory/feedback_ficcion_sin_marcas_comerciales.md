---
name: Ficción ROBOHOGAR sin marcas comerciales de robótica en narrador
description: Rafael rechazó explícitamente mezclar modelos comerciales reales (Dreame X50, Roborock Qrevo Curv 2, Ecovacs X8 Pro Omni, etc.) dentro de relatos. Es promo glorificada, no ficción; rompe "Black Mirror invertido" y suena creepy. Caracterización humana (móvil viejo, TV) sigue permitida.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
**Regla dura.** En la prosa del narrador de cualquier relato ROBOHOGAR (Ficciones Domésticas: La Casa de Amparo, Crónicas de RONDA-3, Cartas a MAIA, futuras series, one-shots) **NUNCA** aparecen nombres de modelo comerciales reales de robótica doméstica. Alcance exacto:

**Categorías vetadas en narrador**: aspiradores-robot, humanoides domésticos, cortacéspedes-robot, fregasuelos, limpia-cristales, mascotas robot, drones domésticos, brazos robóticos de cocina. Marcas concretas:
- Aspiración: `Dreame | Roborock | Ecovacs | Cecotec | Xiaomi | iRobot | Roomba | Mova | Eufy | Dyson | Neato | Samsung (Bespoke Jet Bot) | LG (CordZero) | Philips (Homerun)`.
- Humanoides: `Unitree | 1X | Figure | Agility | Apptronik | Neura | Sanctuary | Kawasaki | Tesla Optimus`.
- Compañía: `Aibo | Loona | LOOI`.

**Permitido en narrador**:
- Robots genéricos: *"el aspirador doméstico"*, *"el humanoide de cuidados"*, *"el cortacésped del patio"*.
- Ficticios canon ROBOHOGAR: Tico (aspirador IA), Hugo (humanoide Casa de Amparo), RONDA-3 (utility), Eva (humanoide familia Cortés), MAIA (IA epistolar).
- Marcas ficticias canon (series-bible-maestra): HOGAR-X de Doméstica Ibérica, KIKI de Toyminds Barcelona, ReboteTech, Cuídame Iberia, Ronda Municipal.
- Marcas inventadas nuevas si se canonizan en la bible de la serie antes de aparecer (ej: "SVA-12").

**Permitido en diálogo**: un personaje puede mencionar una marca real de robótica **una sola vez por escena** si es verosímil en su boca (un yayo diciendo *"yo el Roomba de toda la vida"*). Nunca en cadena, nunca en narrador.

**NO aplica a caracterización humana no-robótica**: móvil viejo de un personaje (Samsung A13 de Amparo), lavadora de siempre, TV marca tal — es prosa cotidiana ES, no promo. Validado 2026-04-19.

**Why:** Rafael verbatim 2026-04-19: *"mezclar Dreame X50 con historias reales = creepy. Quiero buenas novelas cortas con temática inversión de Black Mirror, no una promo glorificada que no me da ningún rédito"*. La ficción ROBOHOGAR tiene que funcionar como literatura — si el lector siente que está leyendo una review disfrazada, rompe el pacto editorial. La tesis "Black Mirror invertido" (villano humano · robot instrumento neutro · soledad/burnout/brecha como conflicto) exige que el robot sea un arquetipo narrativo, no un producto identificable con URL de afiliado.

**Incidente de origen.** Al integrar la regla curse of knowledge (Pinker) el 2026-04-19, Claude metió en `/ficcion-draft § 8.2` el ejemplo *"el Qrevo Curv 2"* → *"el Qrevo Curv 2, el aspirador nuevo de la cocina"*. Rafael lo rechazó en cuanto lo vio. También se detectó regla antigua contradictoria en `series-bible-maestra.md` línea 48 que permitía "modelos reales de aspiradoras cuando sea relevante" — reescrita para alinear.

**Refuerzo 2026-04-19 — nombres propios de robots/IA siempre ficticios**. Rafael verbatim: *"si los robots tienen nombres deben ser ficticios, no de productos reales"*. Prohibidos como nombre de robot protagonista o secundario del relato: `Alexa | Siri | Cortana | Bixby | Google Assistant | ChatGPT | Claude | Gemini | Copilot | Grok | Llama | Mistral | Perplexity | Aibo | Loona | LOOI | Atlas | NAO | Pepper | Ameca | Digit`. Excepción en diálogo: 1 mención por escena verosímil (*"le pregunto a Alexa"*), nunca como nombre del robot del relato.

**How to apply:**
- `/ficcion-draft § 8.2` tiene checklist explícito con regex de marcas vetadas.
- `rules/editorial.md § Narrativa especulativa` lista las categorías y marcas bloqueadas.
- `series-bible-maestra.md § Marcas ficticias compartidas` reescrita para prohibir modelos reales en narrador.
- Verificación pre-output ficción: grep sobre prosa del narrador (excluyendo líneas entre comillas/guiones de diálogo) de las marcas listadas → 0 matches. Reescribir si matchea.

**Relación con otras reglas**:
- Complementa `anti-ia-checklist.md § 2 Ficción` (especificidad Chiang — puede haber marca inventada, nunca real).
- Complementa `editorial.md § Narrativa especulativa` (villano humano, robot neutro, dato real anclado).
- Curse of knowledge (Pinker 2026-04-19) aplica a artículos con marcas reales + ficción con categorías genéricas o ficticias.
