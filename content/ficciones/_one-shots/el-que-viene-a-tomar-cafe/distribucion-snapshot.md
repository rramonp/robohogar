# Distribución audiolibro — El que viene a tomar café

**Generado:** 2026-04-25 por `/audiobook-distribute el-que-viene-a-tomar-cafe`.
**Fuente MP3:** `assets/audio/ficciones/el-que-viene-a-tomar-cafe.mp3` (también en R2: `https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/el-que-viene-a-tomar-cafe.mp3`)
**Fuente MP4:** `assets/audio/ficciones/el-que-viene-a-tomar-cafe-youtube.mp4`

> **Contexto histórico:** este audiolibro se generó en FASE 1 piloto (commit `95a2d07`, 2026-04-22) ANTES de que `generate_audio.py` produjera `chunks-index.json`. El MP3 quedó en R2 pero los assets locales (chunks-index, covers) no se persistieron. La distribución 2026-04-25 reconstruyó el `chunks-index.json` post-hoc (script one-shot en `utilities/_archive/rebuild_chunks_index_for_pilot.py`) usando el `audiolibro.txt` + ffprobe del MP3 final + bumpers FASE 1 (silencio after intro 2.0s, sin silencio before outro). Los timestamps de capítulos tienen velocidad uniforme (cps 14.01) — error ±2-3 s aceptable para chyrons YouTube.

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `rQsqXqj-Uyw` |
| URL pública | https://www.youtube.com/watch?v=rQsqXqj-Uyw |
| Privacy | public |
| Título | `El que viene a tomar café — Ficciones Domésticas` (48 chars) |
| Thumbnail | `covers/el-que-viene-a-tomar-cafe-yt-1280x720.png` (✅ aplicada vía API) |
| Coste API | 150 units (100 insert + 50 thumbnail) |
| Capítulos en descripción | 3 (00:06 La cocina a las ocho · 07:42 La hermana · 15:01 El menú) |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=rQsqXqj-Uyw y pinearlo:

```
¿Te ha enganchado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/el-que-viene-a-tomar-cafe
```

## RSS Podcast

| Campo | Valor |
|---|---|
| Feed URL | https://feed.robohogar.com/feed.xml |
| GUID episodio | `robohogar-ficciones-el-que-viene-a-tomar-cafe` |
| Total episodios en feed | 2 (la-objecion + el-que-viene-a-tomar-cafe) |
| Endpoint usado para subir | Cloudflare REST API (`api.cloudflare.com`) |
| Detección estimada | Spotify ~5-10 min · Apple ~24-48 h · Amazon ~5-10 min |

### Nota sobre el upload

El upload S3 estándar (`upload_rss_to_r2.py`) falló por outage parcial de routing al rango `172.64.66.x` de Cloudflare desde este AS (timeout en endpoint `*.r2.cloudflarestorage.com`, fija + móvil + tras reboot). El feed se subió finalmente vía REST API (`utilities/upload_rss_to_r2_via_api.py`, endpoint `api.cloudflare.com` que sirve por rango `104.19.x.x` que sí responde).

Cuando Cloudflare repare el routing 172.64, el script S3 original vuelve a ser válido. Mantener ambos: S3 como default (más barato en quota), REST como fallback documentado para outages parciales.

## Comandos para regenerar (si algo falla)

```bash
python utilities/_archive/rebuild_chunks_index_for_pilot.py   # solo este slug, one-shot
python utilities/generate_youtube_video.py el-que-viene-a-tomar-cafe
python utilities/upload_youtube.py el-que-viene-a-tomar-cafe
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py   # ⚠️ requiere VPN HBX OFF
```
