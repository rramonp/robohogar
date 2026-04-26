# Distribución audiolibro — El operador nocturno

**Generado:** 2026-04-26 por `/audiobook-distribute el-operador-nocturno` (auto-fire desde `/post-publish § paso 13.5`).
**Fuente MP3:** `assets/audio/ficciones/el-operador-nocturno.mp3`
**Fuente MP4:** `assets/audio/ficciones/el-operador-nocturno-youtube.mp4`

## YouTube

| Campo | Valor |
|---|---|
| **Video ID** | `OgWaX-rcVfU` |
| **URL pública** | https://www.youtube.com/watch?v=OgWaX-rcVfU |
| **Título** | El operador nocturno — Ficciones Domésticas (43 chars · patrón standalone) |
| **Privacy** | public |
| **Thumbnail** | `assets/audio/ficciones/covers/el-operador-nocturno-yt-1280x720.png` ✅ |
| **MP4** | 64,9 MB (68.056.446 bytes) · 1280×720 · H.264 + AAC · 23:05 (1385,17s) |
| **Bitrate MP4** | ~393 kbps |
| **Coste API** | 150 units (100 `videos.insert` + 50 `thumbnails.set`) de los 10.000/día |
| **Capítulos en descripción** | 3 (Madrid madrugada · Manila mañana · Madrid sábado) |
| **Marca de agua canal** | configurada en YouTube Studio (clickable → suscribirse) — no hay overlay quemado en el MP4 |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=OgWaX-rcVfU y pinearlo:

```
¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/el-operador-nocturno
```

Pasos: abrir el vídeo · "Comentar" · pegar · publicar · click en los 3 puntos del propio comment → **Pin**.

## RSS Podcast

| Campo | Valor |
|---|---|
| **Feed URL** | https://feed.robohogar.com/feed.xml |
| **HTTP** | 200 OK · Content-Type: `application/rss+xml` ✅ |
| **GUID episodio** | `robohogar-ficciones-el-operador-nocturno` |
| **Total episodios en feed** | 3 (la-objecion · el-operador-nocturno · el-que-viene-a-tomar-cafe — orden cronológico descendente por pubDate) |
| **Distribución estimada** | Spotify ~min · Apple ~24-48h (re-fetch desde catálogo) · Amazon ~min |
| **Cover podcast subido** | `covers/el-operador-nocturno-podcast-1400x1400.jpg` reparado a R2 (1 referencia que faltaba, healed por `validate_podcast_assets.py`) |

## Capítulos (chunks-index.json)

| # | Inicio | Título |
|---|---|---|
| 1 | 00:06 | Madrid, un martes a las tres y catorce |
| 2 | 04:57 | Manila, el mismo martes, las nueve y catorce |
| 3 | 15:36 | Madrid, sábado, doce y seis del mediodía |

## Comandos para regenerar (si algo falla)

```bash
python utilities/generate_youtube_video.py el-operador-nocturno
python utilities/upload_youtube.py el-operador-nocturno
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```

## Verificaciones pre-output ✅

- MP4: ffprobe duración 1385,17s ≈ MP3 1385,17s (delta 0s) · H.264 + AAC + yuv420p · 1280×720
- YouTube: `videos.insert` + `thumbnails.set` ambos OK (logs upload `OgWaX-rcVfU`)
- RSS: HTTP 200 + Content-Type correcto + 3 items + cover episodio en R2
- Snapshot persistido aquí
- Anti-IA + verbos honestos: descripción YouTube no menciona ElevenLabs/voz Luis (decisión 2026-04-25)

## Coste API agregado de la sesión

- ElevenLabs (TTS audiolibro · `/audiobook-generate`): ~15.566 créditos del plan Creator (saldo restante 92.763 / 121.880)
- YouTube Data API v3 (`/audiobook-distribute`): 150 units de los 10.000 disponibles hoy
- Cloudflare R2 (MP3 + cover podcast + feed): bajo free tier 10 GB
- ffmpeg compute local: ~3-4 min CPU

## Actualización 2026-04-26 — Playlists asignadas

Backfill via `python utilities/backfill_youtube_playlists.py` tras decisión Rafael 2026-04-26 (master + específica con middot). Idempotente: re-correr el backfill no duplica.

| Playlist | URL | Estado playlist | Estado vídeo |
|---|---|---|---|
| Ficciones Domésticas | https://www.youtube.com/playlist?list=PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS | CREADA en este backfill | añadido |
| Ficciones Domésticas · One-shots | https://www.youtube.com/playlist?list=PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon | CREADA en este backfill | añadido |

Coste extra: ~150 units API (1 list + 50 create master + 50 create One-shots + 51 insert master + ~50 insert One-shots con retry post-create). Total acumulado este relato: 300 units de los 10.000/día. $0.
