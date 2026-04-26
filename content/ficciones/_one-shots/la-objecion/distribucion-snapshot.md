# Distribución audiolibro — La objeción

**Generado:** 2026-04-25 por `/audiobook-distribute la-objecion` (piloto FASE 3 — primera distribución completa del pipeline).
**Fuente MP3:** `assets/audio/ficciones/la-objecion.mp3`
**Fuente MP4:** `assets/audio/ficciones/la-objecion-youtube.mp4`

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `BFliK-JcwGc` |
| URL pública | https://www.youtube.com/watch?v=BFliK-JcwGc |
| Privacy | public |
| Título | La objeción — Ficción Doméstica |
| Tamaño MP4 | 64,9 MB |
| Duración | 19,1 min (1143,1s) |
| Códecs | H.264 (vídeo) + AAC (audio) |
| Resolución | 1280×720 (HD ready) |
| Capítulos | 9 chyrons con fade in/out (5s sostenido cada uno) |
| Thumbnail | ✅ Custom subido (cover-yt-1280x720) tras verificación SMS del canal — 2026-04-25 |
| Coste API | 300 units total: 100 (insert vídeo broken pre-SMS) + 50 (thumbnail patch post-SMS) + 100 (re-insert tras delete) + 50 (thumbnail re-upload) |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=BFliK-JcwGc y pinearlo:

```
¿Te ha enganchado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/la-objecion
```

### ✅ Thumbnail custom — RESUELTO 2026-04-25

Verificación SMS del canal completada por Rafael. Thumbnail custom (`la-objecion-yt-1280x720.png`) subido vía API directamente con `youtube.thumbnails().set(videoId='BFliK-JcwGc', media_body=...)` — sin re-uploadear el MP4 (ahorro 100 units API). Próximos `/audiobook-distribute` ya no necesitarán esta acción manual.

## RSS Podcast

⏸ **PENDIENTE — Bloque 3 de la guía no completado.**

El feed RSS no se regeneró en esta distribución porque:
- `PODCAST_OWNER_EMAIL` falta en `.claude/settings.local.json`.
- `content/podcast/canal-metadata.md` tiene placeholders (`REEMPLAZAR_CON_EMAIL_OWNER`, `REEMPLAZAR_CON_URL_PUBLICA_ARTWORK_3000x3000`).
- Spotify/Apple/Amazon NO están dados de alta todavía.

Cuando se complete el Bloque 3 (alta plataformas + canal-metadata real), correr:

```bash
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```

Y este episodio de "La objeción" entrará automáticamente como primer `<item>` del feed.

## Comandos para regenerar (si algo falla)

```bash
# Regenerar el MP4 con chyrons + waveform
python utilities/generate_youtube_video.py la-objecion

# Re-subir el vídeo (NO ejecutar salvo que el primer upload se rompiera —
# crearía un duplicado público en el canal)
python utilities/upload_youtube.py la-objecion

# Cuando Bloque 3 esté hecho:
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```

## Bug adicional descubierto post-upload — límite 15 min sin verificar canal

**Bug:** YouTube rechazó el vídeo del primer upload (ID `4O9QSY9wEsM`) con `failureReason: "El vídeo es demasiado largo"` y status `Procesamiento interrumpido`. Causa: canales sin verificación SMS tienen límite de 15 min/upload por defecto. El vídeo de "La objeción" dura 19 min 4 s.

**Cronología:**
1. Primer `videos.insert` → upload OK pero `thumbnails.set` falló con HTTP 403 (verify SMS pendiente).
2. Rafael completa verify SMS.
3. Thumbnail patch directo via API funciona (50 units).
4. Pero el vídeo ya estaba marcado `Procesamiento interrumpido` por el límite 15 min — la verify NO retroactiva el estado del upload anterior.
5. Rafael borra el vídeo broken desde Studio.
6. Re-upload (`videos.insert` + `thumbnails.set` en el mismo run, post-SMS) → OK limpio. Nuevo ID: `BFliK-JcwGc`.

**Lección:** **verificar SMS del canal SIEMPRE antes del primer `/audiobook-distribute`**, no después. La guía de setup (`Docs/Guia Distribucion Audiolibros.md § Bloque 1`) debería tener un sub-paso explícito para esto entre 1.1 (crear canal) y 1.5 (OAuth flow).

**Coste de no detectarlo upfront:** 150 units API extra (re-insert + re-thumbnail) + ~10 min de tiempo. Cero económico, pequeño ruido en el canal.

## Bugs encontrados durante esta distribución

Lista canónica para evitar que vuelvan a ocurrir en futuras invocaciones de `/audiobook-distribute`. Detalle completo en el chat de la sesión 2026-04-25.

1. **`generate_audio.py` — regex de capítulos demasiado restrictivo.** El skill detectaba solo `Uno. / Dos. / Tres.` aislados, pero relatos como "La objeción" usan `Parte uno. / Parte dos.`. Resultado: 2 falsos positivos (líneas con "Uno." en otro contexto narrativo). Fix manual aplicado al `chunks-index.json`. **Pendiente:** extender regex en `utilities/generate_audio.py` para soportar también `Parte X.`.

2. **`generate_youtube_video.py` — filter_complex CLI demasiado largo.** Con 9 capítulos, el filter llega a ~2900 chars y subprocess en Windows tiene problemas pasándolo como argumento. **Fix aplicado:** escribir el filter a fichero temporal y usar `-/filter_complex <file>`. Modificación queda en el script para todos los runs futuros.

3. **`generate_youtube_video.py` — paths Windows con `:` rompen filter_complex.** El parser de filtros de ffmpeg en Windows interpreta los `:` del path `C:/Windows/...` como separadores de opciones. Las comillas simples NO protegen, ni siquiera con escape `\:`. **Fix aplicado:** copiar font al repo (`assets/fonts/arialbd.ttf`) y usar path relativo sin `:`. El `FONT_FILE` constante en el script ahora apunta al repo. Los próximos canales/máquinas no necesitan font instalado en Windows.

4. **YouTube thumbnail upload — canal sin verificar.** HTTP 403 al subir thumbnail custom. Causa: cuenta YouTube no verificada (SMS). Es one-time. **Acción pendiente:** verificar canal en https://www.youtube.com/verify (ver bloque arriba).

5. **`PODCAST_OWNER_EMAIL` missing en settings.local.json.** Bloque 3 de la guía no completado. RSS no se regenera hasta que esté hecho. No es bloqueante para YouTube.

6. **ElevenLabs cuota Starter agotada (40k chars/mes).** Los 3 audios anteriores ya consumieron ~39k. Regenerar este forzó upgrade a Creator (100k chars/mes, $22). **Anotado en CLAUDE.md / plan audiolibros**: la cadencia mensual ROBOHOGAR de 1-2 audiolibros/mes excede Starter.


## Actualización 2026-04-26 — Playlists asignadas

Backfill via `python utilities/backfill_youtube_playlists.py` tras decisión Rafael 2026-04-26 (master + específica con middot). Idempotente: re-correr el backfill no duplica.

| Playlist | URL | Estado playlist | Estado vídeo |
|---|---|---|---|
| Ficciones Domésticas | https://www.youtube.com/playlist?list=PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS | existente | añadido |
| Ficciones Domésticas · One-shots | https://www.youtube.com/playlist?list=PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon | existente | añadido |

Coste extra: ~102 units API (1 list + 51 insert master + 51 insert One-shots — playlists ya creadas en el backfill por `el-operador-nocturno`). Total acumulado este relato: ~252 units. $0.
