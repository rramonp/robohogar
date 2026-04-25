# Audiobook Distribute — distribución multi-plataforma del audiolibro

Distribuye un audiolibro de Ficciones Domésticas (MP3 ya generado por `/audiobook-generate` y subido a Cloudflare R2) a YouTube + Spotify/Apple Podcasts/Amazon Music vía RSS feed propio. Cero edición manual semanal — solo pegar el pinned comment de YouTube al final.

**INVOCACIÓN AUTO-FIRE desde `/post-publish`** cuando detecta que el slug es ficción + tiene MP3 + chunks-index.json + covers generados. También invocable manual: `/audiobook-distribute <slug>` para piloto/test/re-distribución.

## When to activate

- Encadenado por `/post-publish § paso 13.5` cuando publicas un relato Ficciones Domésticas con audiolibro disponible.
- "distribuye el audiolibro de `<slug>`" / "publica `<slug>` en YouTube y podcast"
- "retomamos plan distribución audiolibros — distribuye `<slug>`"
- "manda `<slug>` a YouTube y RSS"

**NO activar por:** publicar un relato sin audiolibro (no hay MP3), publicar un artículo no-ficción (no hay relato narrado), ni invocaciones de `/audiobook-generate` (la regla del plan separa generación de distribución para no acoplar fallos).

## Sintaxis

```
/audiobook-distribute <slug> [--private] [--skip-rss] [--skip-youtube]
```

- **slug** (obligatorio): nombre del directorio del relato dentro de `content/ficciones/**/<slug>/`. Ej: `papa-desde-singapur`, `el-que-viene-a-tomar-cafe`.
- **--private** (opcional): sube el vídeo YouTube como `privacyStatus=private` en lugar de `public`. Útil para pruebas sin exponer al feed del canal. El RSS feed sigue público (Spotify/Apple lo recogen).
- **--skip-rss** (opcional): solo sube YouTube, no toca el RSS. Útil si Apple aún tiene el feed en review y no queremos invalidar el GUID.
- **--skip-youtube** (opcional): solo regenera RSS, no sube YouTube. Útil para correcciones de show notes podcast sin re-quemar quota YouTube.

## Pre-requisitos

Antes de invocar, Claude debe verificar:

- [ ] **Setup manual completado** (Bloques 1-3 de `Docs/Guia Distribucion Audiolibros.md` en Obsidian). Sin esto el skill falla en pre-check.
- [ ] **Credenciales en `.claude/settings.local.json`**:
    - `R2_ACCOUNT_ID`, `R2_ACCESS_KEY`, `R2_SECRET_KEY`, `R2_BUCKET`, `R2_PUBLIC_URL` (heredadas de `/audiobook-generate`).
    - `R2_FEED_PUBLIC_URL` (custom domain del feed, ej. `https://feed.robohogar.com`).
    - `YOUTUBE_OAUTH_CLIENT_SECRET_PATH` (path absoluto al `client_secret.json`).
    - `YOUTUBE_OAUTH_TOKEN_PATH` (path al `youtube_token.json` con refresh token long-lived).
    - `PODCAST_OWNER_EMAIL` (email del owner Apple-verified).
- [ ] **Tokens OAuth válidos**: correr `python utilities/verify_youtube_auth.py` antes del primer paso. Si falla → STOP, pedir re-auth manual con `python utilities/upload_youtube.py --auth`.
- [ ] **Inputs por slug**:
    - `assets/audio/ficciones/<slug>.mp3` existe y subido a R2 (verificable con `curl -sI <R2_PUBLIC_URL>/<slug>.mp3` → 200).
    - `assets/audio/ficciones/<slug>-chunks-index.json` existe.
    - `assets/audio/ficciones/covers/<slug>-yt-1280x720.png` existe.
    - `assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg` existe.
    - `assets/branding/logo-robohogar-200x200.png` existe.
- [ ] **Relato fuente**: `content/ficciones/**/<slug>/<fecha>-<slug>.md` con frontmatter completo (`title`, `meta_description`, `date`).
- [ ] **Canal podcast configurado**: `content/podcast/canal-metadata.md` con email + artwork URL reales (no placeholders).
- [ ] **Dependencias Python**: `pip install google-auth google-auth-oauthlib google-api-python-client pillow` (boto3 ya viene de `/audiobook-generate`).
- [ ] **ffmpeg con libx264 + libmp3lame + showwaves**: ya verificado en setup de `/audiobook-generate`. Sin acción adicional.

Si falta cualquier pre-requisito → STOP y reportar el fix concreto. NO empezar el pipeline a medias.

## Workflow

### 1. Pre-check completo (failsafe pre-quota)

Ejecutar las verificaciones en orden, parar al primer fallo:

```bash
# (a) Credenciales YouTube válidas (cost: 1 unit del quota)
python utilities/verify_youtube_auth.py

# (b) MP3 público accesible (sin gastar quota)
curl -sI -A "Mozilla/5.0 ..." "$R2_PUBLIC_URL/<slug>.mp3" | head -1
# Esperado: HTTP/2 200 + Content-Type: audio/mpeg

# (c) chunks-index.json + covers existen (Glob local)
ls assets/audio/ficciones/<slug>-chunks-index.json
ls assets/audio/ficciones/covers/<slug>-yt-1280x720.png
ls assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg

# (d) Si ya existe distribucion-snapshot.md con videoId → confirmar re-distribución
ls content/ficciones/**/<slug>/distribucion-snapshot.md
```

**Re-distribución** (snapshot ya existe): preguntar a Rafael *"Ya hay un upload anterior con videoId X. ¿Re-publicar (gasta 150 units quota + crea segundo vídeo en el canal)? Para corregir solo metadata, mejor editar manual desde YouTube Studio."*. Si confirma → continuar. Si no → STOP.

**Si todo OK → continuar al paso 2.**

### 2. Generar MP4 YouTube (opción D++ híbrido)

```bash
python utilities/generate_youtube_video.py <slug>
```

El script compone con ffmpeg:
- Background full-frame: `covers/<slug>-yt-1280x720.png`.
- Waveform inferior animado: `showwaves` ámbar `#F5A623` 1280×120.
- Chyrons de capítulo: un `drawtext` por capítulo de `chunks-index.json` con fade in 1 s + sostenido 3 s + fade out 1 s, centrado horizontal arriba 15%.
- Logo overlay esquina inferior derecha: `assets/branding/logo-robohogar-200x200.png`, permanente.

Output: `assets/audio/ficciones/<slug>-youtube.mp4` (versionado `-v2`, `-v3`... si ya existe — regla `feedback_never_overwrite_images.md`).

Render: 1-4 min para 15 min de audio en CPU portátil moderna. Verifica al final que `ffprobe duración MP4 ≈ duración MP3 ± 2 s`.

**Si falla:** revisar `result.stderr` del ffmpeg en consola — el problema más común es un `drawtext` con caracteres mal escapados (apostrofes, colons en títulos). Solución: el script usa `escape_drawtext_text()` que sustituye `'` por `’` (typographic) y escapa `:`/`,` — si pese a eso falla, simplificar el título del capítulo en el frontmatter.

### 3. Construir descripción YouTube + pinned comment

Plantillas en `utilities/upload_youtube.py § build_description` y `§ build_pinned_comment_text`. Salidas se computan ANTES del upload para que Rafael las vea en el chat:

**Descripción YouTube** (5000 chars cap, ROBOHOGAR cap defensivo 4900):

```
{primera frase del meta_description del relato}

▶ Lee el relato completo + suscríbete al newsletter: https://robohogar.com/p/<slug>

⏱ Capítulos:
00:00 Intro
{MM:SS} 1. {Título Capítulo I}
{MM:SS} 2. {Título Capítulo II}
...
{MM:SS} Cierre

———
Ficciones Domésticas: relatos de ciencia ficción próxima sobre robótica en el hogar.
Cada semana, junto al newsletter en robohogar.com.

Audiolibro narrado con voz Luis (ElevenLabs Multilingual v2).

#FiccionesDomesticas #ROBOHOGAR #Audiolibro #CienciaFiccion
```

**Pinned comment** (Rafael lo pega manual a posteriori — la API no lo permite desde 2023):

```
¿Te ha enganchado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/<slug>
```

### 4. Upload YouTube (videos.insert + thumbnails.set)

```bash
python utilities/upload_youtube.py <slug>
# o con --private para test
```

Subida resumable por chunks de 8 MB con progress logging cada 10 %. Coste: 100 units `videos.insert` + 50 units `thumbnails.set` = 150 units (de los 10.000/día disponibles).

Metadata seteada vía API:
- `title`: `<Título relato> — Ficción Doméstica` (cap 100 chars).
- `description`: la del paso 3.
- `tags`: lista canónica `["ficciones domésticas", "audiolibro", "ciencia ficción", "robótica", "robots domésticos", "ROBOHOGAR", "narrativa especulativa", "audiolibro español"]`.
- `categoryId`: `24` (Entertainment).
- `defaultLanguage` + `defaultAudioLanguage`: `es`.
- `privacyStatus`: `public` (o `private` si `--private`).
- `thumbnail`: `covers/<slug>-yt-1280x720.png`.

Captura `videoId` y URL pública `https://www.youtube.com/watch?v=<videoId>`.

### 5. Regenerar y subir RSS feed

```bash
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
```

Re-escanea `assets/audio/ficciones/*-chunks-index.json` (el del slug nuevo + todos los anteriores) y reconstruye `content/podcast/feed.xml` con todos los `<item>` ordenados por pubDate descendente.

Cada `<item>` lleva:
- `<title>`: `frontmatter.title` del relato.
- `<itunes:summary>`: `meta_description` del frontmatter.
- `<description>`: HTML CDATA con hook + CTA al newsletter (`<a href>` al post web).
- `<enclosure url="...mp3" length="..." type="audio/mpeg" />`.
- `<guid isPermaLink="false">robohogar-ficciones-<slug></guid>` — inmutable, identificador único del episodio para las plataformas.
- `<pubDate>` en RFC 2822 (parseado del frontmatter `date` o filename `YYYY-MM-DD-<slug>.md`).
- `<itunes:duration>`, `<itunes:image>`, `<itunes:episodeType>`, `<itunes:explicit>`.

Sube a R2 con `Content-Type: application/rss+xml` + `Cache-Control: max-age=3600`. Las plataformas re-leen el feed cada hora — el episodio nuevo aparece en Spotify/Amazon en minutos, en Apple en 24-48 h (review humana inicial; auto-update tras la primera).

### 6. Persistir snapshot en repo + reportar

Escribir `content/ficciones/**/<slug>/distribucion-snapshot.md` con todo lo necesario para que Rafael lo recupere en sesiones futuras sin volver a invocar el skill:

```markdown
# Distribución audiolibro — <Título del relato>

**Generado:** YYYY-MM-DD por `/audiobook-distribute <slug>`.
**Fuente MP3:** `assets/audio/ficciones/<slug>.mp3`
**Fuente MP4:** `assets/audio/ficciones/<slug>-youtube.mp4`

## YouTube

| Campo | Valor |
|---|---|
| Video ID | `<videoId>` |
| URL pública | https://www.youtube.com/watch?v=<videoId> |
| Privacy | public |
| Thumbnail | `covers/<slug>-yt-1280x720.png` |
| Coste API | 150 units (100 insert + 50 thumbnail) |

### ⚠️ Acción manual pendiente — Pinned comment

Pegar este comment en https://www.youtube.com/watch?v=<videoId> y pinearlo:

```
<texto literal del pinned comment del paso 3>
```

## RSS Podcast

| Campo | Valor |
|---|---|
| Feed URL | https://feed.robohogar.com/feed.xml |
| GUID episodio | `robohogar-ficciones-<slug>` |
| Total episodios en feed | <N> |
| Distribuido a | Spotify (~min), Apple (~24-48h), Amazon (~min) |

## Comandos para regenerar (si algo falla)

\`\`\`bash
python utilities/generate_youtube_video.py <slug>
python utilities/upload_youtube.py <slug>
python utilities/generate_podcast_rss.py
python utilities/upload_rss_to_r2.py
\`\`\`
```

**Resumen al chat** (breve, accionable):

```
✅ DISTRIBUCIÓN COMPLETADA · <slug>

🎬 YouTube: https://www.youtube.com/watch?v=<videoId>
📡 RSS: https://feed.robohogar.com/feed.xml (N episodios totales)

⚠️ ACCIÓN MANUAL — pegar pinned comment en YouTube:
─────────────────────────────────────────────
<texto literal del pinned comment>
─────────────────────────────────────────────
   → Abrir el vídeo, comentar, click en 3-dots → Pin.

Snapshot persistido: content/ficciones/**/<slug>/distribucion-snapshot.md
```

## Verificación pre-output

Antes de devolver el resumen final, Claude debe:

- [ ] **MP4 verificado**: `ffprobe` confirma duración ≈ MP3 ± 2 s + codec H.264 + container MP4.
- [ ] **YouTube URL accesible**: `curl -sI https://www.youtube.com/watch?v=<videoId>` devuelve 200.
- [ ] **RSS feed válido**: `curl -sI https://feed.robohogar.com/feed.xml` devuelve 200 + `Content-Type: application/rss+xml`. Recordar a Rafael que valide con [Cast Feed Validator](https://castfeedvalidator.com) si es la primera distribución del setup.
- [ ] **Snapshot persistido** en el directorio del relato.
- [ ] **Anti-IA en descripción YouTube y show notes RSS**: revisar que no haya tics tipo *intrincado/tapiz/matizado/entramado*, em-dashes en cascada, ni hype anglosajón. Regla `editorial.md § Anti-IA checklist § §1 Universal`.
- [ ] **Verbos honestos**: la descripción dice *"audiolibro narrado con voz Luis (ElevenLabs)"*, no *"audiolibro producido por nosotros"*. Regla `editorial.md § Honestidad de primera persona`.

## Reglas y safety

- **Versionar MP4, nunca sobrescribir** (regla `feedback_never_overwrite_images.md`): si ya hay `<slug>-youtube.mp4`, generar `-v2.mp4`. R2 también con sufijo de versión si re-subimos.
- **RSS sí se sobrescribe**: es estado actual del catálogo, no histórico. Los `<guid>` son inmutables, así que las plataformas no re-procesan episodios viejos.
- **Pre-check antes de gastar quota**: si snapshot existe con videoId → confirmar re-publicación. Cero uploads silenciosos duplicados.
- **OAuth tokens NUNCA en repo**: `content/podcast/_oauth-tokens/` debe estar en `.gitignore`.
- **Cero verbos de acción no realizada en metadata** (regla editorial heredada): "audiolibro narrado" sí, "audiolibro producido por nosotros" no, "test del producto" no.
- **Pronunciación canónica ROBOHOGAR**: en TTS = `ROBO, OGAR` (ver memoria `feedback_robohogar_tts_pronunciation.md`). En metadata escrita visible al lector (descripción YouTube, show notes RSS) = `ROBOHOGAR` sin coma.
- **Si Apple Podcasts rechaza el primer feed por feed vacío** (no hay `<item>` aún): distribuir el primer relato real ANTES de dar de alta en Apple. Spotify y Amazon aceptan feeds vacíos.

## Output final esperado

```
✅ DISTRIBUCIÓN COMPLETADA · <slug>

🎬 YouTube: https://www.youtube.com/watch?v=<videoId>
   • Render: <X> min
   • Tamaño MP4: <Y> MB
   • Privacy: public
   • Thumbnail: ✅
   • Chapters: <N> en descripción

📡 RSS Podcast: https://feed.robohogar.com/feed.xml
   • Episodios totales: <N>
   • Nuevo GUID: robohogar-ficciones-<slug>
   • Detección estimada: Spotify ~min · Apple ~24-48h · Amazon ~min

📁 Snapshot persistido: content/ficciones/**/<slug>/distribucion-snapshot.md

⚠️ ACCIÓN MANUAL — pegar este pinned comment:
─────────────────────────────────────────────
<texto literal>
─────────────────────────────────────────────
   → https://www.youtube.com/watch?v=<videoId> · Comentar · Pin.

💰 Coste API esta sesión: 150 units YouTube (de 10.000/día). $0.
```

## Coste en régimen

- **YouTube Data API v3:** 150 units/episodio × 4 ep/mes = 600 units/mes (de 300.000 mensuales). Coste: $0.
- **Cloudflare R2:** feed.xml ~30-100 KB; covers ~150-700 KB; MP4 ~50-200 MB → bajo el free tier 10 GB durante años. Coste: $0.
- **YouTube Storage:** ilimitado para vídeos públicos. Coste: $0.
- **Spotify / Apple / Amazon:** gratis, indefinido.
- **ffmpeg compute local:** 1-4 min CPU/episodio. Coste: $0.

**Coste agregado nuevo:** $0 sobre el setup actual de ElevenLabs Starter ($5/mes).

## Troubleshooting

### Token YouTube caducado mid-pipeline

`upload_youtube.py` falla con `invalid_grant` o `Token has been expired or revoked`. Causa: app quedó en "Testing mode" (consent screen) o credenciales revocadas manualmente.

**Fix:** borrar `content/podcast/_oauth-tokens/youtube_token.json` y correr `python utilities/upload_youtube.py --auth`. Tras esto, re-invocar `/audiobook-distribute <slug>`.

### MP4 no pasa upload a YouTube por codec

Causa rara — el ffmpeg del script ya usa libx264 + AAC + yuv420p (perfil universal). Si pese a eso falla: subir manual desde YouTube Studio para diagnóstico.

### Apple Podcasts: "Feed contains no episodes"

Apple no acepta feeds vacíos en el review inicial. Solución: distribuir el primer relato (que añade el primer `<item>`) ANTES de dar de alta en Apple. Spotify y Amazon sí aceptan setup con feed vacío.

### Spotify: episodio nuevo no aparece tras 1 hora

Lo normal. Spotify dice "instantáneo" pero re-lee el feed cada 60-90 min. Si tras 2 h sigue sin aparecer: verificar feed con [Cast Feed Validator](https://castfeedvalidator.com), `<guid>` único del episodio nuevo, y `<pubDate>` válido.

### YouTube: aparece copyright claim falso por la voz Luis

Reportar dispute desde Studio. La voz Luis es voz humana sintetizada bajo licencia comercial ElevenLabs Starter — no coincide con ningún catálogo de copyright. Si recurre el claim, verificar que ningún chunk del audio incluyó música externa por error (revisar `_chunks-<slug>/`).

### El chyron de un capítulo aparece en el momento equivocado

Causa: error de timestamping del `chunks-index.json`. Velocidad uniforme tiene error ±5%, en chapters de 5+ min puede ser 1-3 s. Si el offset es notorio (>10 s), regenerar el audiolibro con el texto exacto que se usó (puede haber drift entre `audiolibro.txt` y los chunks reales si Rafael editó el .txt entre runs).

## Referencias cruzadas

- Plan completo: [`docs/plan-audiolibros-ficciones.md`](../../docs/plan-audiolibros-ficciones.md) (FASE 3 de este plan).
- Skill upstream: [`audiobook-generate.md`](audiobook-generate.md) (genera MP3 + chunks-index.json + covers).
- Skill que dispara: [`post-publish.md § paso 13.5`](post-publish.md) (auto-fire si detecta audiolibro).
- Guía operativa setup manual: vault Obsidian → `Docs/Guia Distribucion Audiolibros.md` (3 bloques: YouTube, R2 custom domain, RSS + plataformas).
- Utilidades Python invocadas:
  - [`utilities/verify_youtube_auth.py`](../../utilities/verify_youtube_auth.py)
  - [`utilities/generate_audiobook_covers.py`](../../utilities/generate_audiobook_covers.py)
  - [`utilities/generate_youtube_video.py`](../../utilities/generate_youtube_video.py)
  - [`utilities/upload_youtube.py`](../../utilities/upload_youtube.py)
  - [`utilities/generate_podcast_rss.py`](../../utilities/generate_podcast_rss.py)
  - [`utilities/upload_rss_to_r2.py`](../../utilities/upload_rss_to_r2.py)
- Memoria pronunciación marca: [`feedback_robohogar_tts_pronunciation.md`](../../../RRP-DEV/.claude/memory/feedback_robohogar_tts_pronunciation.md).
- Memoria versionado: [`feedback_never_overwrite_images.md`](../../../RRP-DEV/.claude/memory/feedback_never_overwrite_images.md).
- Regla automation pipeline: [`@rules/automation.md § Pipeline de contenido`](../rules/automation.md).
