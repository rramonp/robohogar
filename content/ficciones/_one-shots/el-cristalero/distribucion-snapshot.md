# Distribución audiolibro — El cristalero

**Generado:** 2026-04-28 por `/audiobook-distribute el-cristalero` (auto-fire desde `/post-publish` § paso 13.5).
**Fuente MP3:** `assets/audio/ficciones/el-cristalero.mp3` (22.0 MB · 23.0 min · 1377.3s)
**Fuente MP4:** `assets/audio/ficciones/el-cristalero-youtube.mp4` (207.6 MB)
**chunks-index:** schema_version=3 con frontispicio sonoro (anuncio del título Gabo intercalado entre intro Luis y cuerpo).

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `Dfr5aOQ-S8w` |
| URL pública | https://www.youtube.com/watch?v=Dfr5aOQ-S8w |
| Privacy | public |
| Thumbnail | `covers/el-cristalero-yt-1280x720.png` |
| Coste API | 150 units (100 insert + 50 thumbnail) + ~102 playlists |

### Playlists asignadas

| Playlist | URL | Estado playlist | Estado vídeo |
|---|---|---|---|
| Ficciones Domésticas | https://www.youtube.com/playlist?list=PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS | existente | añadido |
| Ficciones Domésticas · One-shots | https://www.youtube.com/playlist?list=PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon | existente | añadido |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=Dfr5aOQ-S8w y pinearlo:

```
¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/el-cristalero
```

## RSS Podcast

| Campo | Valor |
|---|---|
| Feed URL | https://feed.robohogar.com/feed.xml |
| GUID episodio | `robohogar-ficciones-el-cristalero` |
| Total episodios en feed | 6 |
| Distribuido a | Spotify (~min), Apple (~24-48h), Amazon (~min) |

## Cover podcast

Subido a R2 con Content-Type correcto (`image/jpeg`) tras un primer intento que cargó como `audio/mpeg` (bug del helper `upload_to_r2()` de `generate_audio.py` que fuerza ContentType audio/mpeg para MP3 — al reusarlo para imágenes fuerza tipo erróneo). Corrección aplicada manualmente con boto3 + `ExtraArgs={'ContentType': 'image/jpeg', 'CacheControl': 'public, max-age=86400'}`.

**Pendiente seguimiento técnico:** generalizar `upload_to_r2()` para que infiera ContentType del path (.mp3 → audio/mpeg, .jpg → image/jpeg, .png → image/png, .xml → application/rss+xml). Hasta entonces, los uploads de covers desde el pipeline `/audiobook-distribute` requieren intervención manual o re-upload con boto3.

## Particularidad de este relato

Primer relato canon § Composición canon del audiolibro establecida 2026-04-28 PM:

- Frontispicio sonoro: intro Luis (2.53s) + 2s silencio + ANUNCIO "El cristalero." (Gabo, 1.16s, prosodia de anuncio: `style=0.5` / `stability=0.4` / `previous_text="Una Ficción Doméstica de ROBO, OGAR."`) + 2s silencio + cuerpo Gabo + 3s silencio + outro Luis.
- `chunks-index.json` schema_version=3 (campos nuevos `title_text`, `title_duration_seconds`, `silence_after_title_seconds`).
- Capítulos del MP4 desplazados ~3-4s respecto al canon previo (sin frontispicio): 00:07 / 07:46 / 12:43 / 18:08.
- MP3 R2 actual fue intercalado one-shot con `utilities/_archive/intercalate_title_el_cristalero_2026_04_28_v2.py` (no regenerado desde cero — los chunks del cuerpo ya estaban horneados en el MP3 v1).
- Para relatos siguientes: el canon se aplica directo desde `generate_audio.py` con el 3er arg CLI `<title>`.

## Comandos para regenerar (si algo falla)

```bash
python utilities/generate_youtube_video.py el-cristalero
python utilities/upload_youtube.py el-cristalero
python utilities/add_episode_to_manifest.py el-cristalero
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```
