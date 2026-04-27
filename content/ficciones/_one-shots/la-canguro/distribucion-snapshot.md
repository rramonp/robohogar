# Distribución audiolibro — La canguro

**Generado:** 2026-04-27 por `/audiobook-distribute la-canguro`.
**Fuente MP3:** [`assets/audio/ficciones/la-canguro.mp3`](../../../../assets/audio/ficciones/la-canguro.mp3) (16,8 MB · 17:32)
**Fuente MP4:** `assets/audio/ficciones/la-canguro-youtube.mp4` (108,8 MB · 1280×720 H.264 · 4 chyrons)

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `cOLUVXqKvjc` |
| URL pública | https://www.youtube.com/watch?v=cOLUVXqKvjc |
| Privacy | public |
| Título | El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida |
| Thumbnail | `covers/la-canguro-yt-1280x720.png` (painterly chiaroscuro v4) |
| Capítulos en descripción | 4 (00:05 La cena · 03:43 El correo · 07:36 La pestaña · 12:48 La pregunta) |
| Coste API | 150 units (insert + thumbnail) + ~102 units (playlists) ≈ 252 units |

**Patrón de título aplicado**: display_title YouTube-style 2026-04-27 (display_title pelado sin sufijo " — Ficciones Domésticas"). Aplicado vía patch a `utilities/upload_youtube.py § build_youtube_title`. Primer relato con este patrón nuevo; los 3 retroactivos anteriores se actualizaron manualmente vía script ad-hoc.

### Playlists asignadas

| Playlist | URL | Estado playlist | Estado vídeo |
|---|---|---|---|
| Ficciones Domésticas | https://www.youtube.com/playlist?list=PLNWdNerZ2NVDbG_ZbFwstyVApv8JuIkwS | existente | añadido |
| Ficciones Domésticas · One-shots | https://www.youtube.com/playlist?list=PLNWdNerZ2NVAmgH2_Ybmg5F4C86GECyon | existente | añadido |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=cOLUVXqKvjc y pinearlo:

```
¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/la-canguro
```

→ Abrir el vídeo, comentar, click en 3-dots → Pin.

## RSS Podcast

| Campo | Valor |
|---|---|
| Feed URL | https://feed.robohogar.com/feed.xml |
| GUID episodio | `robohogar-ficciones-la-canguro` |
| Total episodios en feed | 4 (la-canguro · la-objecion · el-operador-nocturno · el-que-viene-a-tomar-cafe) |
| Distribuido a | Spotify (~min) · Apple (~24-48h) · Amazon (~min) |
| pubDate | Mon, 27 Apr 2026 09:00:00 +0000 |
| Cover podcast | `https://feed.robohogar.com/covers/la-canguro-podcast-1400x1400.jpg?v=20260427` |
| `<itunes:subtitle>` | El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida |
| `<itunes:summary>` | Joel paga 79 € al mes para que un humanoide cuide a su hijo de noche. El sábado descubre lo que esa cifra le ha estado comprando. |

### Manifest declarativo (fix arquitectónico aplicado 2026-04-27)

Este episodio fue inicialmente añadido al feed editando `content/podcast/feed.xml` directamente porque el `generate_podcast_rss.py` legacy escaneaba los chunks-index locales (en .gitignore), y los de los 3 retroactivos no estaban presentes en esta máquina — regenerar habría borrado episodios.

Tras detectar el bug en esta sesión, se introdujo el manifest declarativo [`content/podcast/episodes.json`](../../../podcast/episodes.json) commiteado al repo como fuente única de verdad. El refactor de `generate_podcast_rss.py` lee del manifest (no de chunks-index), e [`utilities/add_episode_to_manifest.py`](../../../../utilities/add_episode_to_manifest.py) provee append idempotente desde `/audiobook-distribute § paso 5`. La-canguro fue retroactivamente añadida al manifest tras el refactor para verificar regeneración byte-equivalente. A partir de aquí, el feed se regenera con confianza desde cualquier máquina.

## Comandos para regenerar (si algo falla)

```bash
# MP4 (regenerable desde MP3 + cover + chunks-index)
python utilities/generate_youtube_video.py la-canguro

# Re-upload del vídeo (NO recomendado: gasta 100 units + crea video duplicado en canal)
# Para corregir solo metadata, editar manual en YouTube Studio.

# Re-subida del feed (recordar que regenerar borra los retroactivos sin chunks-index)
# Editar content/podcast/feed.xml a mano + python utilities/upload_rss_to_r2.py
```
