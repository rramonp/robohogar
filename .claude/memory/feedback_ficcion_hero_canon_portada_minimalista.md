---
name: feedback_ficcion_hero_canon_portada_minimalista
description: ROBOHOGAR heros de ficción — canon "portada minimalista · objeto-testigo" validado 2026-04-20. Fondo azul noche #1E2A3A + luz cálida lateral + un objeto del relato + toque sci-fi sutil. SUSTITUYE el canon anterior "still cinematográfico" para Ficciones Domésticas.
type: feedback
originSessionId: 454369cd-5a0b-432e-9fc2-cdbadf13fcaf
---
Canon visual para heros de Ficciones Domésticas, validado por Rafael 2026-04-20 tras iteración sobre los 3 one-shots iniciales. El canon se canonizó en [`assets/branding/asset-catalog.md § 5`](../../robohogar/assets/branding/asset-catalog.md) con recipe completa + prompt template + anti-sign-guard technique.

**Principio editorial:** la imagen del relato funciona como **portada de ebook minimalista** que lee tanto a thumbnail 120px (landing page, Beehiiv preview cards) como a hero grande 1200×675 al abrir el artículo. No es "still cinematográfico" complejo — es portada de libro.

**ADN visual obligatorio compartido** (los 3 hacen SERIE):
1. Fondo azul noche `#1E2A3A` plano (pared matte dark blue-gray) ocupando 2/3 superiores del frame.
2. Superficie doméstica abajo (encimera, mantel de hule, parquet) en 1/3 inferior.
3. Luz cálida de lámpara lateral izquierda única, amber highlight solo sobre objeto + patch estrecho de superficie.

**Por relato:**
- Un **objeto-testigo** del relato (Chekhov's gun): tetrabrik, taza, yoyó — simboliza el conflicto.
- Un **toque sintético/sci-fi sutil** anclado narrativamente: mano humanoide matte, humanoide encogido desenfocado, tarjeta ID en blanco, pulsera smart, cable fino. NUNCA LEDs, glow, ni paneles luminosos.

**Por qué este canon y no "film still After Yang":** el still complejo no lee en thumbnail 120px; la portada minimalista sí. Referente Fitzcarraldo Editions: **color-firma recurrente** como sello de serie.

**Anti-sign-guard technique (crítico):** el script `nano-banana` auto-inyecta un directive "NO EMPTY SIGNS" que fuerza a Gemini a meter neones + caracteres asiáticos al fondo. NO se puede desactivar. Técnicas que esquivan el bug:
- Frase exacta canonizada: *"solid dark empty wall, plain matte dark blue-gray paint, completely bare and unmarked, filling the top two thirds of the frame"* (describe superficie pintada sólida, no espacio vacío).
- NO usar *"background"*, *"dark space"*, *"midnight blue background"* — Gemini los interpreta como escenarios urbanos con neones.
- NO usar *"sci-fi"*, *"futuristic"*, *"Asian"*.
- Elementos sintéticos siempre con *"plain matte cream-white with no glowing parts, no LEDs, no lights, no panels, no colored accents"*.

**Prompt template canónico:** disponible en `assets/branding/asset-catalog.md § 5` (sección "Prompt template canónico"). `/nano-banana` debe leer ese archivo antes de generar cualquier hero de ficción.

**Why:** el primer set de heros de ficción iba en estilo "still cinematográfico" generic (canon anterior). Rafael pidió 3 one-shot heros para landing page, y el proceso reveló (a) que el thumbnail 120px exige minimalismo radical, (b) que Gemini mete neones por defecto cuando se describe "dark background" sin disciplina, (c) que la mezcla cotidianidad + toque sci-fi ancla la serie como "Black Mirror doméstico" mejor que el still puro. Rafael validó los 3 heros finales (Operador v6 · Café v3 · Setenta v3) y pidió canonizar el patrón para futuros relatos.

**How to apply:**
- Cuando `/ficcion-draft` o `/nano-banana` generen un hero de ficción: **leer obligatoriamente `assets/branding/asset-catalog.md § 5`** antes de componer el prompt.
- Usar el prompt template canónico y adaptar [OBJETO-TESTIGO] + [TOQUE SCI-FI] al relato concreto.
- Correr la checklist de validación pre-output (8 puntos) antes de dar la imagen por válida.
- Si alguna v falla por neones/caracteres asiáticos/texto: archivar en `<slug>/assets/_archive/hero-v<N>-<motivo>-YYYY-MM-DD.png` y regenerar con v+1.

**Cuándo revisar este canon:** si tras N relatos Rafael siente que el fondo azul noche se desgasta, o si surge un subgénero de ficción que no encaja en el canon (por ejemplo, una serie radicalmente distinta que pide otro color-firma), se revisa. La matriz tonal 40/15/25/10/10 de `tonalidad-y-mix-editorial.md` NO cambia el canon visual — inquietante, ambiguo, radical, inspirador, mundano comparten el mismo fondo y luz.
