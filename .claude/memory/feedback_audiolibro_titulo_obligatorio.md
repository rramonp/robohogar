---
name: Audiolibro · frontispicio sonoro obligatorio (intro → título → cuerpo → outro)
description: Todo audiolibro Ficciones Domésticas inserta el `title:` corto leído por Gabo entre el bumper Luis y el cuerpo, con prosodia de anuncio especial
type: feedback
---

Regla dura establecida 2026-04-28 PM. Aplica a TODO audiolibro generado por `/audiobook-generate` para Ficciones Domésticas — one-shots, miniseries, episodios de serie, sin excepción.

**La regla:** la composición canon del MP3 final pasa de `intro Luis + 2s + cuerpo Gabo + 3s + outro Luis` a `intro Luis + 2s + ANUNCIO DEL TÍTULO Gabo + 2s + cuerpo Gabo + 3s + outro Luis`. El bloque nuevo es el "frontispicio sonoro" — equivalente sonoro del Snippet 2.5 HTML que Rafael pega en Beehiiv (página título interior estilo Anagrama / Penguin Modern Classics).

**Why:**

Rafael reprodujo `el-cristalero.mp3` v1 generado con la composición previa y detectó al instante que faltaba anclar la pieza con su nombre. El bumper Luis cerraba con *"Una Ficción Doméstica de ROBOHOGAR"* y Gabo arrancaba directamente con *"Treinta y un turnos. Mauricio le dio la hoja…"* sin decir nunca cuál era el relato. Cita literal: *"acabo de reproducir el MP3 y he visto que dice en la intro 'Ficciones de RoboHogar' y luego directamente empieza por parte 1 sin decir el título del relato. En este caso sería 'El Cristalero'."* Sensación: "te cuento una historia cualquiera" en lugar de "abre el libro X y léelo". Rompía el paralelismo con el HTML Beehiiv (que sí lleva el frontispicio Snippet 2.5 entre el reproductor y el cuerpo).

**How to apply:**

- **Texto leído:** el `title:` corto del frontmatter del relato (ej: *"El cristalero"*, *"La objeción"*, *"Pipo"*), idéntico letra por letra al frontispicio HTML del Snippet 2.5. **Nunca** el `display_title:` declarativo largo — eso es para subject de email, H1 web y OG card; 15 palabras leídas como tarjeta de título suenan a sinopsis, no a frontispicio. El script añade automáticamente punto final si falta (idempotente).

- **Voz:** Gabo (mismo locutor del cuerpo). Razón: el narrador del libro lee su propio frontispicio, patrón Penguin / Anagrama del audiolibro impreso. Luis se mantiene exclusivamente como bumper de marca (intro + outro). Cambiar a Luis para el título rompería la metáfora "abro el libro y empiezo a leer".

- **Parámetros prosódicos especiales del TTS** (críticos: con defaults, frases ≤3 palabras se leen como inicio de oración incompleta — el modelo Multilingual v2 asume continuación):
  - `previous_text="Una Ficción Doméstica de ROBO, OGAR."` (cierre simulado del bumper Luis canónico). Sin esto, el modelo no sabe que viene tras una sentencia cerrada y aplica entonación de continuación. Validado A/B con Rafael 2026-04-28 PM: la primera versión (sin estos parámetros) sonaba a frase incompleta; la segunda (con previous_text + style/stability) suena como tarjeta de título limpia.
  - `voice_settings.style = 0.5` (cuerpo: 0.0). Da expresividad de presentación, no de narración íntima.
  - `voice_settings.stability = 0.4` (cuerpo: 0.5). Suficiente variación para que el cierre del título caiga en pitch como final declarativo.
  - `next_text` ausente. Evita que el modelo encadene con el cuerpo sin pausa.

- **Implementación:** `utilities/generate_audio.py § synthesize_title_announce` desde 2026-04-28 PM. CLI nuevo (3er arg obligatorio): `python utilities/generate_audio.py <audiolibro.txt> <slug> "<title corto>"`. Sin él, abort con mensaje claro.

- **`chunks-index.json` schema_version = 3:** añade `title_text`, `title_duration_seconds`, `silence_after_title_seconds`. Los `chapters[].start_seconds` se calculan con offset = `intro + sil_after_intro + título + sil_after_title` (la narración empieza tras el frontispicio sonoro). Implicación downstream: timestamps de capítulos del MP4 YouTube + chapters de descripción RSS se desplazan ~3-4s respecto al canon previo.

- **MP4 YouTube hereda automáticamente.** `/audiobook-distribute` compone el MP4 con el MP3 final como pista de audio + waveform + chyrons. El título leído ya está horneado en el MP3 → aparece en el MP4 sin trabajo extra. Los chapters de la descripción YouTube usan los offsets nuevos del `chunks-index.json` v3.

- **Aplicación retroactiva:** los 5 audiolibros publicados pre-2026-04-28 PM (`el-que-viene-a-tomar-cafe`, `la-canguro`, `la-objecion`, `papa-desde-singapur`, `pipo`) **NO se regeneran** — coste TTS de regenerar 5 cuerpos enteros ~60K créditos (50% cuota mensual Creator). Aplica desde el siguiente relato. `el-cristalero` ya en R2 con título intercalado vía one-shot `utilities/_archive/intercalate_title_el_cristalero_2026_04_28*.py` (ahorro: solo se regeneró el chunk del título, no los 12.5K chars del cuerpo).

- **Coste por relato:** ~10-30 chars adicionales TTS por título (~10-30 créditos ElevenLabs, despreciable frente a los 12-15K del cuerpo medio).

**Incidente origen + validación A/B:**

2026-04-28 PM — Rafael reprodujo `el-cristalero.mp3` v1 (composición sin título), detectó el problema, pidió arreglo + canonización. Yo propuse 3 caminos (A: trick prosódico Gabo; B: voz Luis bumper; C: alargar texto leído). Rafael eligió A. Generé v2 con `previous_text=BUMPER_LUIS_CLOSE_TEXT + style=0.5 + stability=0.4`. Veredicto Rafael literal: *"mucho mejor"*. Canon aplicado: regla en `editorial.md § Composición canon del audiolibro` + cambio estructural en `generate_audio.py` (3er arg obligatorio + función `synthesize_title_announce` + `concat_with_ffmpeg` con título intercalado + `build_chunks_index` schema v3) + skill `audiobook-generate.md` actualizado + esta memoria.

**Verificación pre-output del skill `/audiobook-generate`:** el `title:` corto del frontmatter del relato debe existir y no estar vacío. Si falta, abort con mensaje claro (la regla canon del frontispicio HTML Snippet 2.5 desde 2026-04-26 ya garantizaba que `title:` existe — esta regla solo añade que también vive como anuncio sonoro).

**Referencias cruzadas:**

- Regla canon: [`@.claude/rules/editorial.md § Composición canon del audiolibro`](../rules/editorial.md).
- Implementación: [`utilities/generate_audio.py § synthesize_title_announce`](../../utilities/generate_audio.py) + `§ concat_with_ffmpeg` + `§ build_chunks_index` schema v3.
- Skill: [`@.claude/commands/audiobook-generate.md § 4. Generar el audio`](../commands/audiobook-generate.md).
- One-shots históricos del fix `el-cristalero`: `utilities/_archive/intercalate_title_el_cristalero_2026_04_28.py` (v1 — sin parámetros prosódicos especiales; rechazado) + `utilities/_archive/intercalate_title_el_cristalero_2026_04_28_v2.py` (v2 — con prosodia de anuncio; aprobado).
- Memoria hermana sobre voz Gabo default cuerpo: `feedback_audiobook_voz_default_gabo.md`.
- Memoria sobre snippet HTML 2.5 frontispicio: `feedback_ficcion_frontispicio_titulo_corto.md`.
