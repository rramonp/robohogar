# Distribución audiolibro — Pipo

**Generado:** 2026-04-27 por `/audiobook-distribute pipo` (auto-fire desde `/post-publish`).
**Fuente MP3:** `assets/audio/ficciones/pipo.mp3`
**Fuente MP4:** `assets/audio/ficciones/pipo-youtube.mp4` (166 MB · H.264 1280×720 · 18.5 min)

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `hFbU1yVkRuI` |
| URL pública | https://www.youtube.com/watch?v=hFbU1yVkRuI |
| Privacy | public |
| Thumbnail | `covers/pipo-yt-1280x720.png` ✅ |
| Title (81 chars) | `El cazador que apunta a la nieta de chatarra que el robot lleva dos años soldando` |
| Descripción | 580 chars · 19 líneas · capítulos 6 · CTA al post web |
| Coste API | 252 units (100 insert + 50 thumbnail + 1 list playlists + 51 add×2 = 252) |

### Render MP4 (D++ híbrido)

- Background: `covers/pipo-yt-1280x720.png` (full-frame).
- Waveform inferior: `showwaves` ámbar `#F5A623` (1280×120).
- Chyrons capítulo: 6 con `drawtext` + fade in 1s + sostenido 3s + fade out 1s, top 15%.
- Logo: SIN overlay quemado (cubierto por marca de agua del canal YT canal-wide).
- Render: ~18 min CPU (libx264 + filter_complex 2101 chars · 14 nodos vía fichero).

### Capítulos (chunks-index.json)

| # | Título | Inicio |
|---|---|---|
| 1 | Las manos | 00:05 |
| 2 | El altar | 03:36 |
| 3 | El circuito | 06:39 |
| 4 | ¿Jugamos? | 10:37 |
| 5 | La llamada | 12:51 |
| 6 | El termo | 14:56 |

(`¿Jugamos?` con `?` preservado tras el fix del detector 2026-04-27.)

### Playlists asignadas

| Playlist | URL | Estado playlist | Estado vídeo |
|---|---|---|---|
| Ficciones Domésticas | https://www.youtube.com/playlist?list=PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS | existente | añadido |
| Ficciones Domésticas · One-shots | https://www.youtube.com/playlist?list=PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon | existente | añadido |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=hFbU1yVkRuI y pinearlo:

```
¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/pipo
```

→ Abrir el vídeo, comentar, click en 3-dots → Pin.

## RSS Podcast

| Campo | Valor |
|---|---|
| Feed URL | https://feed.robohogar.com/feed.xml |
| GUID episodio | `robohogar-ficciones-pipo` |
| Duración declarada | 00:18:30 |
| MP3 bytes | 17 764 145 (17,3 MB · `<enclosure length>`) |
| Cover episodio | `covers/pipo-podcast-1400x1400.jpg?v=20260427` |
| pub_date | Mon, 27 Apr 2026 09:00:00 +0000 |
| Total episodios en feed | 5 (pipo + la-canguro + la-objecion + el-operador-nocturno + el-que-viene-a-tomar-cafe) |
| Distribuido a | Spotify (~min), Apple (~24-48h), Amazon (~min) |
| Verificación | HTTP 200 ✅ · `Content-Type: application/rss+xml` ✅ |

### Manifest commiteado al repo

`content/podcast/episodes.json` actualizado idempotentemente (preserva GUIDs inmutables). Hace el feed independiente del estado local (chunks-index.json en `.gitignore`).

## Voz audiolibro

- **Voz:** Gabo - Deep, Evocative and Resonant (My Voices ElevenLabs · `o0SveC0zgHFuCsEO3vHR`)
- **Default desde 2026-04-27** — sustituye Luis (`GojDwihhnL1f7RrBuXsJ`).
- Bumpers (intro/outro) siguen en Luis para preservar continuidad sonora con los 3 publicados pre-cambio.
- Velocidad observada: **12.84 cps** (Luis era ~17 cps · Gabo más pausado y evocativo, coherente con tono radical-Cuidados rotos).

## Comandos para regenerar (si algo falla)

```bash
python utilities/generate_youtube_video.py pipo
python utilities/upload_youtube.py pipo
python utilities/add_episode_to_manifest.py pipo
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```

## Verificaciones pre-output ejecutadas

- [✅] MP4 ffprobe: duración 1110.20s ≈ MP3 1110.20s (diff 0s, dentro de tolerancia ±2s).
- [✅] YouTube URL `https://www.youtube.com/watch?v=hFbU1yVkRuI` → HTTP 200.
- [✅] Playlists asignadas: 2 (master + One-shots), ambas con `[AÑADIDO]`.
- [✅] RSS feed `https://feed.robohogar.com/feed.xml` → HTTP 200 · `Content-Type: application/rss+xml`.
- [✅] Anti-IA en descripción YouTube: cero tics tipo *intrincado/tapiz/matizado*, cero hype anglo, voz peninsular cercana.
- [✅] Verbos honestos: la descripción no menciona stack TTS (ElevenLabs/Gabo) — info técnica solo en este snapshot interno.
