---
name: Composiciones canon (C-01..C-19) — eje compositivo macro de heros de Ficciones
description: Catálogo cerrado de 19 patrones gramaticales del frame organizados en 5 familias, extraídos del canal Domestic Fictions YouTube y aprobados por Rafael 2026-04-27 (C-01..C-12) + 2026-04-28 PM tarde (C-13..C-19, ampliación tras nuevas capturas). Selección aleatoria con anti-repetición últimos 5 + bloqueo de familia si las últimas 3 son misma familia. Aplica a todos los paradigmas hero ficción.
type: feedback
---

Regla dura establecida por Rafael 2026-04-27 PM tras revisión del set de 9 miniaturas test (3 relatos × 3 modalidades) generadas con el template painterly v2.

**Toda generación de hero de relato Ficciones Domésticas (one-shots y miniseries futuras, paradigmas minimalista § 5 y personaje-acción-imposibilidad § 5.bis) debe declarar `composicion_canon: C-01..C-19` en frontmatter, junto a `modalidad_visual:` y `angulo_camara:`. La selección es aleatoria del pool tonal-compatible, con anti-repetición de los últimos 5 publicados y bloqueo de familia si las 3 últimas son misma familia.**

**Why:** las 9 miniaturas test painterly v2 (72h M2/M4/M6 · Papá M2/M3/M6 · Llave M3/M4/M5) salieron correctas en estilo (painterly book cover Penguin Modern Classics) y modalidad cromática (paletas distintas), pero las 3 composiciones de los 3 relatos eran demasiado parecidas en gramática del frame: las 3 son objeto-en-superficie con presencia humanoide secundaria (yoyó cenital, niño en cama frente a humanoide arrodillado, llave inglesa cenital). Rafael comparó contra las ~23 miniaturas del canal "Domestic Fictions" de YouTube y detectó que el referente anglo tiene **mucha más variedad gramatical**: two-shots íntimos en perfil, planos arquitectónicos monumentales (catedral, tribunal), frame-in-frame (holograma, ventana), close-ups emocionales, over-the-shoulder voyeur, color-pop saturado, decadencia caos, etc. Cita literal: *"Que montes en el skill, ahora mismo, una funcionalidad para ser mucho más aleatorio a la hora de buscar composiciones, para que sean diferentes entre sí, pero que tengan su gancho y que tengan un cut to action importante y que atraigan."*

**Catálogo cerrado** (canon en [`assets/branding/ficcion-hero-composiciones-canon.md`](../../assets/branding/ficcion-hero-composiciones-canon.md)) — 19 composiciones en 5 familias (C-01..C-12 canonizadas 2026-04-27, C-13..C-19 ampliadas 2026-04-28 PM tarde):

| Familia | Composiciones |
|---|---|
| **I — Íntima emocional** (close-up + two-shot + relacional) | `C-01` Two-shot lateral íntimo · `C-02` Primerísimo plano emocional · `C-03` Detalle obsesivo manos · **`C-13`** Three-shot teatral horizontal con oficio · **`C-18`** Detalle de manos con altar simétrico |
| **II — Plano arquitectónico monumental + escala** | `C-04` Espacio institucional con perspectiva profunda · `C-05` Eje simétrico altar/atril · **`C-14`** Contrapicado de escala asimétrica humano↔máquina · **`C-15`** Bóveda/cúpula con reunión circular ritual |
| **III — Frame dentro de frame** | `C-06` Pantalla/holograma central · `C-07` Ventana/umbral al exterior · **`C-19`** Cabina cerrada con ventana a exterior radical (cósmico/intemperie) |
| **IV — Frontal teatral / over-the-shoulder** | `C-08` Frontal teatral con atrezzo simbólico · `C-09` Over-the-shoulder voyeur · **`C-16`** Foco lumínico cenital extremo (quirúrgico/teatral) |
| **V — Atmósfera ambiental + color-pop** | `C-10` Exterior nocturno con foco icónico · `C-11` Interior decadencia/caos · `C-12` Color-pop saturado single-zone · **`C-17`** Ritual outdoor con horizonte desolado/apocalíptico |

**ADN inmutable que conviven todas las composiciones** (no se toca al cambiar composición): estilo painterly book cover Penguin Modern Classics + chiaroscuro Hopper-Caravaggio con foco lumínico **único** + regla "cotidiano + sci-fi mezclados" (humanoide siempre presente, explícito o como sombra/silueta) + tight legibilidad a thumbnail 120px + anti-sign-guard activo (cero neones, cero caracteres asiáticos, cero LEDs/glow, cero texto salvo letras-fragmento como objeto-imposibilidad narrativo) + dimensiones 1200×630.

**How to apply (regla operativa):**

- **Frontmatter obligatorio en relatos nuevos** (one-shots y miniseries futuras): `composicion_canon: C-XX` declarado. Sin él, output del skill `/ficcion-draft § 8.x Hero` bloqueado.
- **Anti-repetición transversal a paradigma:** ningún `composicion_canon` puede repetirse en los **últimos 5 heros** publicados. Si las **últimas 3** son de la misma familia (I-V), la familia entera queda bloqueada para la siguiente. El skill consulta `content/registro-ficciones.md` columna `Comp.` antes de proponer.
- **Selección aleatoria:** el skill filtra el pool por compatibilidad con `categoria-tonal` (mapeo en el catálogo § Mapeo composición → tonalidades preferentes), excluye las 5 últimas, aplica bloqueo de familia, y propone **3 candidatos aleatorios** del pool resultante. Cada candidato es una combinación distinta de composición + modalidad + ángulo + banda — máxima variabilidad.
- **Mapeo tonalidad → composiciones preferentes** (no exclusivo): inquietante → C-02·C-03·C-04·C-06·C-07·C-09·C-10·C-11·C-12·C-14·C-16·C-17·C-18·C-19 · radical → C-02·C-04·C-05·C-08·C-09·C-11·C-12·C-13·C-14·C-15·C-16·C-17·C-18·C-19 · ambiguo → C-01·C-02·C-06·C-07·C-10·C-11·C-13·C-14·C-15·C-17·C-18·C-19 · inspirador → C-01·C-07·C-13·C-15·C-17 · mundano → C-01·C-03·C-10·C-13. Si pool < 3 candidatos tras filtro, relajar tonal antes de relajar anti-repetición.
- **Compatibilidades especiales con bandas (paradigma personaje):** banda A (oficios domésticos) mejor con C-01·C-03·C-07·C-08·C-12·C-13·C-16·C-18 · banda B (trabajadores ES) con C-03·C-08·C-09·C-11·C-13·C-16·C-19 · banda C (funcionarios) con C-04·C-05·C-06·C-08·C-15·C-16·C-19 · banda D (figuras públicas) con C-04·C-05·C-08·C-15·C-16 · banda E (cultura pop) con C-02·C-06·C-08·C-12·C-14·C-16. Comodín cross-banda: C-09·C-10·C-11·C-14·C-17·C-19.
- **Forzado de cobertura:** en los 19 primeros heros publicados desde 2026-04-28, deben aparecer al menos 12 de las 19 composiciones. Si una nunca apareció tras 19, el skill bloquea las otras hasta que toque la faltante.
- **Series activas con código declarado** (Amparo, Ronda 3, MAIA): NO usan C-01..C-19. Mantienen su código visual fijo.
- **Aplicación retroactiva:** los 6 publicados con hero existente se backfillean con la composición C-01..C-12 que mejor describe su frame (best-fit, no implica rerender). Las 7 nuevas C-13..C-19 NO se aplican retroactivamente — son default desde el siguiente relato. Tabla en el catálogo § Backfill retroactivo.
  - Operador nocturno → C-09 Over-the-shoulder voyeur
  - Café (hija reza) → C-01 Two-shot lateral íntimo
  - Maratonista y su sombra → C-07 Ventana/umbral (TV como umbral)
  - Setenta y dos horas → C-11 Interior decadencia/caos (variante leve)
  - La objeción → C-08 Frontal teatral con atrezzo simbólico
  - La canguro → C-03 Detalle obsesivo con manos
- **Prompt fragments por composición** (inglés, listos para Gemini): catálogo en [`ficcion-hero-composiciones-canon.md § Prompt fragments por composición`](../../assets/branding/ficcion-hero-composiciones-canon.md). Sustituyen el bloque "Composition" del template canónico § 5.bis. C-13..C-19 incorporados al bloque de fragments el 2026-04-28 PM tarde.

**Test inicial — set de 9 miniaturas test 2026-04-27 que motivó la regla:**
- Las 9 v2 painterly están en `assets/branding/_test/modalidades-visuales/`. Estilo correcto, modalidad cromática variada, **composición demasiado uniforme**. Aprobadas como test de modalidad pero rechazadas como muestra de variabilidad compositiva total. La regla nueva resuelve este último gap.

**Ampliación 2026-04-28 PM tarde — 7 composiciones nuevas (C-13..C-19):** Rafael envía 5 capturas adicionales del canal "Domestic Fictions" mostrando 14 miniaturas nuevas. Tras estudio identifico 7 huecos compositivos que C-01..C-12 no cubría: (a) three-shot teatral horizontal con oficio (tailor + dress + groom) → **C-13**; (b) contrapicado de escala asimétrica humano↔máquina (orphan + patrol robot) → **C-14**; (c) bóveda/cúpula con reunión circular ritual (insomniac teacher + orphans) → **C-15**; (d) foco lumínico cenital extremo quirúrgico/teatral (surgeon + toy fingers) → **C-16**; (e) ritual outdoor con horizonte desolado/apocalíptico (priest in landfill) → **C-17**; (f) detalle de manos con altar simétrico ceremonial (antique clockmaker) → **C-18**; (g) cabina cerrada con ventana a exterior radical cósmico/intemperie (pilot + drone constellations) → **C-19**. Todas mantienen el ADN inmutable. Cita literal: *"Quiero que estudies estas composiciones y las añadas a las posibles composiciones para generar imagenes de relatos de ficcion con nano banana, mismo estilo personal pero con estas posibles variantes de composicion, coloreado, planos, zoom, etc"*. Cifra del catálogo "12 patrones" → "19 patrones" actualizada en todas las cross-references del repo.

**Documentación canónica relacionada:**
- Catálogo + reglas + prompt fragments: [`assets/branding/ficcion-hero-composiciones-canon.md`](../../assets/branding/ficcion-hero-composiciones-canon.md).
- ADN visual y reglas duras: [`.claude/rules/editorial.md § Hero de one-shots y miniseries`](../rules/editorial.md).
- Algoritmo del skill (paso 6.bis nuevo): [`.claude/commands/ficcion-draft.md § Paradigma 2 — Algoritmo de selección`](../commands/ficcion-draft.md).
- Tracking en registro: [`content/registro-ficciones.md`](../../content/registro-ficciones.md) columna `Comp.`
- Memoria hermana de modalidades visuales: [`feedback_ficcion_modalidades_visuales.md`](feedback_ficcion_modalidades_visuales.md).
