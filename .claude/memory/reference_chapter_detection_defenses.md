---
name: Defensas del detector de capítulos en generate_audio.py
description: Canon 2026-04-27 — dos defensas duraderas contra que el regex CHAPTER_HEADING_RE vuelva a quedarse corto: (1) guard pre-TTS `assert_no_chapters_lost` que aborta antes de gastar créditos, (2) tests de regresión `utilities/tests/test_chapter_detection.py` con todos los bugs históricos. Cuatro fixes del regex registrados; cada bug futuro debe añadir un test antes del fix.
type: reference
---

## Por qué existe este archivo

El detector de capítulos del audiolibro (`CHAPTER_HEADING_RE` + `detect_chapters` en [`utilities/generate_audio.py`](../../utilities/generate_audio.py)) ha tenido **4 bugs en 4 días distintos**, cada uno detectado solo después de gastar créditos ElevenLabs y revisar el `chunks-index.json`:

| Fecha | Slug | Bug | Fix |
|---|---|---|---|
| 2026-04-25 | la-objecion | Regex solo aceptaba `Uno./Dos./...` y agarraba 2 falsos positivos al final del texto | Anclar a `^` + `re.MULTILINE` |
| 2026-04-25 | papa-desde-singapur | Regex sin límite de título capturaba párrafos enteros que empiezan por `Tres meses antes` | Límite `{1,60}` chars en grupo título + filtro post-regex de orden secuencial |
| 2026-04-26 | el-operador-nocturno | Regex con `[^,;:\n]` rechazaba 3 headings legítimos por contener coma → 0 detectados, fallback "Relato" | Pasar a `[^;:\n]` (sí coma, no `;:`) |
| 2026-04-27 | pipo | Regex exigía `\.\s*$` y `Parte cuatro. ¿Jugamos?` falló por terminar en `?` → solo 3/6 detectados (filtro de orden hizo break al saltar el 4) | Terminador ampliado a `[.?!]` y capturado como grupo 3; el `?` y `!` se preservan en el título |

Patrón evidente: cada relato nuevo introduce una convención de heading que el regex no había visto. Sin defensas estructurales, el ciclo se repetirá. Las dos defensas siguientes lo cortan.

## Defensa 1 — Guard pre-TTS `assert_no_chapters_lost`

**Qué hace.** Antes de gastar el primer crédito ElevenLabs, corre dos detectores sobre el mismo texto:

- **`LAX_CHAPTER_HEADING_RE`** — laxo. Solo exige `^(?:Parte\s+)?(ordinal)\.[ \t]+<algo>$` en una línea. NO restringe terminador, longitud, ni caracteres prohibidos en el título.
- **`CHAPTER_HEADING_RE`** — estricto canon. El que se usa para construir capítulos reales.

Si el laxo encuentra **más** headings que el estricto → `SystemExit` con mensaje listando los headings perdidos. Probable causa documentada: convención nueva (terminador `?`/`!`/`…`, ordinal compuesto, etc.).

**Por qué laxo > estricto sin posibilidad inversa.** El laxo es siempre superset del estricto. Cualquier heading que el estricto detecte, el laxo también. Si laxo detecta menos que estricto sería un bug del laxo (imposible mientras el laxo se mantenga genuinamente más permisivo).

**Cuándo se llama.** [`utilities/generate_audio.py § main()`](../../utilities/generate_audio.py) inmediatamente tras `apply_tts_brand_substitutions(text)` y antes del `chunk_text(text)` y `pre_check(saldo)`. Cero créditos gastados si la guardia salta.

**Comportamiento esperado tras un abort:**
1. Inspeccionar el output con la lista de headings perdidos.
2. Si los headings son legítimos pero el regex estricto se queda corto → ampliar `CHAPTER_HEADING_RE` para incluir la convención nueva.
3. Antes de re-fixear, **añadir un test de regresión nuevo** en [`utilities/tests/test_chapter_detection.py`](../../utilities/tests/test_chapter_detection.py) que ejercite el caso. El test FALLA con el regex actual (red), pasa tras el fix (green).
4. Solo después correr `python utilities/generate_audio.py` de nuevo.

## Defensa 2 — Tests de regresión

[`utilities/tests/test_chapter_detection.py`](../../utilities/tests/test_chapter_detection.py) cubre:

- **Cada bug histórico** (la-objecion, papa-desde-singapur, el-operador-nocturno, pipo) con su ejemplo mínimo reproducible.
- **Convenciones canónicas** (`Uno. ...` corto · `Parte uno. ...` largo · headings con coma legítima · terminadores `?` y `!`).
- **Anti-patterns** (párrafos narrativos que empiezan por ordinal NO matchean · ordinales fuera de orden secuencial se descartan).
- **Real audiolibros del repo** — carga los `audiolibro.txt` publicados (pipo, la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe) y verifica el conteo esperado de capítulos. Si alguien edita el regex y rompe los publicados, este test lo detecta sin necesidad de re-ejecutar el TTS.
- **El propio guard** `assert_no_chapters_lost` (caso happy + caso adversarial que debe abortar).

**Ejecutar antes de mergear cualquier cambio al regex:**

```bash
python -m unittest utilities.tests.test_chapter_detection -v
```

Esperado: `Ran 10 tests in <0.05s` · `OK`.

## Disciplina al añadir un fix futuro

Cuando aparezca el bug número 5 (habrá uno, siempre lo hay):

1. Reproducir el caso mínimo. Identificar qué pattern se le escapó al regex.
2. **Escribir el test primero** en `test_chapter_detection.py`. El test debe fallar con el regex actual (red).
3. Editar `CHAPTER_HEADING_RE` (o `LAX_CHAPTER_HEADING_RE` si el bug está en el laxo) hasta que el test pase (green).
4. Verificar que **todos los tests existentes siguen pasando** — el fix no debe romper convenciones anteriores.
5. Añadir línea al historial de bugs (tabla de arriba) + comentario en el regex con la 5ª iteración del fix.
6. Sólo entonces re-correr `python utilities/generate_audio.py` para producción.

Esta disciplina es lo que cierra el ciclo: cada bug se convierte en test permanente, el regex se va haciendo más resistente con el tiempo.

## Archivos canon afectados

- [`utilities/generate_audio.py`](../../utilities/generate_audio.py) — `SPANISH_ORDINALS` · `CHAPTER_HEADING_RE` · `LAX_CHAPTER_HEADING_RE` · `detect_chapters` · `assert_no_chapters_lost` · llamada en `main()`.
- [`utilities/tests/test_chapter_detection.py`](../../utilities/tests/test_chapter_detection.py) — 10 casos de regresión.
- [`assets/audio/ficciones/<slug>-chunks-index.json`](../../assets/audio/ficciones/) — output downstream consumido por `/audiobook-distribute` para YouTube chapters + chyrons MP4 + show notes RSS.
