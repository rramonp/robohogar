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
- [ ] **Canal YouTube verificado por SMS** (CRÍTICO antes del PRIMER upload de cada canal). Sin verify, YouTube limita uploads a **15 minutos máximo** y rechaza vídeos más largos con `failureReason: "El vídeo es demasiado largo"` Y bloquea `thumbnails.set` con HTTP 403. Comprobar visitando https://www.youtube.com/verify — debe mostrar "Tu canal está verificado". Si no, hacer verify SMS antes de seguir (one-time, gratis, ~30s). **Sin esta verificación, el vídeo se rechaza incluso si tiene OAuth + scopes válidos.** Incidente origen: 2026-04-25 sesión "la-objecion".
- [ ] **Credenciales en `.claude/settings.local.json`**:
    - `R2_ACCOUNT_ID`, `R2_ACCESS_KEY`, `R2_SECRET_KEY`, `R2_BUCKET`, `R2_PUBLIC_URL` (heredadas de `/audiobook-generate`).
    - `R2_FEED_PUBLIC_URL` (custom domain del feed, ej. `https://feed.robohogar.com`).
    - `YOUTUBE_OAUTH_CLIENT_SECRET_PATH` (path absoluto al `client_secret.json`).
    - `YOUTUBE_OAUTH_TOKEN_PATH` (path al `youtube_token.json` con refresh token long-lived).
    - `PODCAST_OWNER_EMAIL` (email del owner Apple-verified) — **solo necesario si NO se usa `--skip-rss`**.
- [ ] **Tokens OAuth válidos**: correr `python utilities/verify_youtube_auth.py` antes del primer paso. Si falla → STOP, pedir re-auth manual con `python utilities/upload_youtube.py --auth`.
- [ ] **Inputs por slug**:
    - `assets/audio/ficciones/<slug>.mp3` existe y subido a R2 (verificable con `curl -sI <R2_PUBLIC_URL>/<slug>.mp3` → 200).
    - `assets/audio/ficciones/<slug>-chunks-index.json` existe **y los capítulos detectados coinciden con la estructura real del relato** (ver Pre-check paso 1.e abajo — bug 2026-04-25 con regex `Parte X.`).
    - `assets/audio/ficciones/covers/<slug>-yt-1280x720.png` existe.
    - `assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg` existe.
    - `assets/branding/logo-robohogar-200x200.png` existe (solo si se invoca `generate_youtube_video.py` con flag `--logo` — el modo default no usa overlay quemado).
    - `assets/fonts/arialbd.ttf` existe (font local del repo, NO `C:/Windows/Fonts/...` — los `:` del path Windows rompen el filter_complex de ffmpeg, ver Troubleshooting).
- [ ] **Marca de agua del canal en YouTube Studio configurada** (one-time, vale para todos los vídeos futuros): Studio → Customisation → Branding → Watermark → subir `assets/branding/logo-robohogar-200x200.png` (con transparencia real — alpha range `(0, 255)`) + Display time = "Whole video" (recomendado) o "End of video" si prefieres menos invasivo. Sustituye al overlay quemado del MP4 con la ventaja añadida de ser **clickable → suscribirse**. Verificar en cualquier vídeo del canal que aparece la marca de agua. Sin esta configuración, los vídeos saldrán sin branding.
- [ ] **Relato fuente**: `content/ficciones/**/<slug>/<fecha>-<slug>.md` con frontmatter completo (`title`, `meta_description`, `date`).
- [ ] **Canal podcast configurado** (solo si NO `--skip-rss`): `content/podcast/canal-metadata.md` con email + artwork URL reales (no placeholders `REEMPLAZAR_CON_*`). Si tiene placeholders → ejecutar `--skip-rss` automáticamente sin preguntar y dejar nota en el snapshot, **NO bloquear la distribución a YouTube por esto**.
- [ ] **Dependencias Python**: `pip install google-auth google-auth-oauthlib google-api-python-client pillow` (boto3 ya viene de `/audiobook-generate`).
- [ ] **ffmpeg con libx264 + libmp3lame + showwaves**: ya verificado en setup de `/audiobook-generate`. Sin acción adicional.

Si falta cualquier pre-requisito **bloqueante** (verify SMS, OAuth, MP3, chunks-index, covers, font, relato MD) → STOP y reportar el fix concreto. NO empezar el pipeline a medias.

**Pre-requisitos no-bloqueantes** (canal-metadata con placeholders, PODCAST_OWNER_EMAIL faltante): activar `--skip-rss` automáticamente, distribuir solo a YouTube, dejar nota en el snapshot del relato y en el reporte final indicando "Bloque 3 RSS pendiente". El usuario completará Bloque 3 después y re-invocará `--skip-youtube` para añadir el episodio al feed sin re-subir el vídeo.

## Workflow

### 1. Pre-check completo (failsafe pre-quota)

Ejecutar las verificaciones en orden, parar al primer fallo:

```bash
# (a) Credenciales YouTube válidas (cost: 1 unit del quota)
python utilities/verify_youtube_auth.py

# (b) MP3 público accesible (sin gastar quota)
curl -sI -A "Mozilla/5.0 ..." "$R2_PUBLIC_URL/<slug>.mp3" | head -1
# Esperado: HTTP/2 200 + Content-Type: audio/mpeg

# (c) chunks-index.json + covers + font local existen (Glob local)
ls assets/audio/ficciones/<slug>-chunks-index.json
ls assets/audio/ficciones/covers/<slug>-yt-1280x720.png
ls assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg
ls assets/fonts/arialbd.ttf
ls assets/branding/logo-robohogar-200x200.png

# (d) Si ya existe distribucion-snapshot.md con videoId → confirmar re-distribución
ls content/ficciones/**/<slug>/distribucion-snapshot.md

# (e) Validar que chunks-index detectó capítulos REALES del relato (no falsos positivos)
python -c "
import json, re
from pathlib import Path
slug = '<slug>'
idx = json.loads(Path(f'assets/audio/ficciones/{slug}-chunks-index.json').read_text(encoding='utf-8'))
# Buscar el audiolibro.txt en cualquier subcarpeta de content/ficciones/
txts = list(Path('content/ficciones').rglob(f'{slug}/audiolibro.txt'))
if not txts:
    print(f'WARN: no se encontró audiolibro.txt para {slug}')
else:
    txt = txts[0].read_text(encoding='utf-8')
    parte_count = len(re.findall(r'^Parte (uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\.', txt, re.MULTILINE | re.IGNORECASE))
    uno_count = len(re.findall(r'^(Uno|Dos|Tres|Cuatro|Cinco|Seis|Siete|Ocho|Nueve|Diez|Once|Doce)\.', txt, re.MULTILINE))
    detected = len(idx['chapters'])
    real = max(parte_count, uno_count)
    print(f'Capítulos detectados en index: {detected} | esperados según .txt: {real}')
    if detected != real:
        print(f'WARN: discrepancia. Reconstruir chunks-index.json antes de generar el MP4.')
    if any(len(c['title']) > 80 for c in idx['chapters']):
        print(f'WARN: títulos de capítulo muy largos (>80 chars). Posible falso positivo en el regex.')
"

# (f) Validar duración MP3 vs límite YouTube canal sin verificar (15 min)
python -c "
import json
from pathlib import Path
idx = json.loads(Path('assets/audio/ficciones/<slug>-chunks-index.json').read_text(encoding='utf-8'))
dur_min = idx['total_duration_seconds'] / 60
print(f'Duración MP3: {dur_min:.1f} min')
if dur_min > 15:
    print(f'INFO: vídeo >15 min — el canal YouTube DEBE estar verificado por SMS o YouTube rechazará el upload con failureReason=\"El vídeo es demasiado largo\". Verificar en https://www.youtube.com/verify antes del primer upload.')
"
```

**Re-distribución** (snapshot ya existe): preguntar a Rafael *"Ya hay un upload anterior con videoId X. ¿Re-publicar (gasta 150 units quota + crea segundo vídeo en el canal)? Para corregir solo metadata, mejor editar manual desde YouTube Studio."*. Si confirma → continuar. Si no → STOP.

**Discrepancia de capítulos en (e):** STOP automático antes de generar MP4. Mostrar a Rafael:
- Capítulos detectados (con sus títulos)
- Capítulos reales esperados según el regex sobre `audiolibro.txt`
- Reconstrucción manual del `chunks-index.json` con la heurística siguiente:
  ```python
  # Para cada match de "Parte X." en el .txt, calcular start_seconds:
  # silence_after_intro = idx.get('silence_after_intro_seconds', idx.get('silence_duration_seconds', 0))  # v2 con fallback v1
  # start_seconds = intro_duration_seconds + silence_after_intro
  #               + (char_offset_en_txt / total_chars_txt) * narration_duration_seconds
  ```
- Sobreescribir el JSON. Continuar.

**Caveat sobre WARN en (e) — títulos >80 chars:** indica que el regex agarró un párrafo entero como título (típico falso positivo donde "Uno." aparece en mitad del texto narrativo). Síntoma del bug origen 2026-04-25. Reconstruir antes de proceder.

**Si todo OK → continuar al paso 2.**

### 2. Generar MP4 YouTube (opción D++ híbrido)

```bash
python utilities/generate_youtube_video.py <slug>
```

El script compone con ffmpeg:
- Background full-frame: `covers/<slug>-yt-1280x720.png`.
- Waveform inferior animado: `showwaves` ámbar `#F5A623` 1280×120.
- Chyrons de capítulo: un `drawtext` por capítulo de `chunks-index.json` con fade in 1 s + sostenido 3 s + fade out 1 s, centrado horizontal arriba 15%.
- **SIN logo overlay quemado** (default). El branding del canal en YouTube se cubre con la **marca de agua del canal** configurada en YouTube Studio → Customisation → Branding → Watermark. Esa marca de agua es **clickable** (lleva a "Suscribirse" — UX superior al overlay quemado), su timing es configurable ("Whole video" recomendado), y aparece en TODOS los vídeos del canal automáticamente. Decisión 2026-04-25 tras detectar duplicación visual del logo (overlay quemado del MP4 + marca de agua YT) en el vídeo `BFliK-JcwGc` de "la-objecion".

Si en algún caso especial se quiere reusar el MP4 fuera de YouTube (donde no hay marca de agua del canal), invocar el script con flag `--logo` para incluir el overlay quemado y conservar branding standalone:

```bash
python utilities/generate_youtube_video.py <slug> --logo
```

Output: `assets/audio/ficciones/<slug>-youtube.mp4` (versionado `-v2`, `-v3`... si ya existe — regla `feedback_never_overwrite_images.md`).

Render: 1-4 min para 15 min de audio en CPU portátil moderna. Verifica al final que `ffprobe duración MP4 ≈ duración MP3 ± 2 s`.

**Si falla:** revisar `result.stderr` del ffmpeg en consola. Problemas conocidos del script (todos resueltos en runs posteriores 2026-04-25 — el script ya los maneja, pero documentar por si reaparece variante):

- **`Invalid argument` con filter complex >2000 chars** (típico con ≥6 capítulos): el script usa `-/filter_complex <file>` con fichero temporal en lugar de pasar el filter inline para evitar el límite de longitud de línea de comando Windows. Si el script falla con `Invalid argument` y filter <2000 chars, revisar otra causa.
- **`No option name near '/Windows/...'`**: el filter contiene un path Windows con `:` sin escapar correctamente. El script ya usa `assets/fonts/arialbd.ttf` (path relativo del repo, sin `:`) en lugar de `C:/Windows/Fonts/arialbd.ttf`. Si pese a eso aparece, revisar que el font del repo existe (`ls assets/fonts/arialbd.ttf`).
- **`drawtext` con apostrofes/colons en títulos de capítulo**: el script usa `escape_drawtext_text()` que sustituye `'` por `’` (typographic) y escapa `:`/`,` — si pese a eso falla, simplificar el título del capítulo en el `chunks-index.json`.

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

#FiccionesDomesticas #ROBOHOGAR #Audiolibro #CienciaFiccion
```

**Pinned comment** (Rafael lo pega manual a posteriori — la API no lo permite desde 2023):

```
¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/<slug>
```

### 4. Upload YouTube (videos.insert + thumbnails.set)

```bash
python utilities/upload_youtube.py <slug>
# o con --private para test
```

Subida resumable por chunks de 8 MB con progress logging cada 10 %. Coste: 100 units `videos.insert` + 50 units `thumbnails.set` = 150 units (de los 10.000/día disponibles).

Metadata seteada vía API:
- `title`: construido por `build_youtube_title(frontmatter)` según 3 patrones canónicos (decisión Rafael 2026-04-25 — siempre **plural "Ficciones Domésticas"**, nunca "Ficción Doméstica" singular). Cap 100 chars con truncado defensivo del hook (preserva la cola "Ficciones Domésticas"):

| Caso | Patrón | Detección frontmatter |
|---|---|---|
| **Standalone** | `{title} — Ficciones Domésticas` | `serie: _one-shots` o sin definir |
| **Episodio serie** | `{title} · {SerieDisplay} #{N} — Ficciones Domésticas` | `serie: <slug-serie>` + `episodio: <N>` numérico |
| **Piloto serie nueva** | `{title} — Ficciones Domésticas · Piloto` | `tipo: piloto` (opt-in explícito en frontmatter) |

Razones del patrón:
- **Plural "Ficciones Domésticas"** coincide con: nombre canónico de la serie en `CLAUDE.md` + `references/ficciones/series-bible-maestra.md` + character bibles + descripción del canal. Algoritmo YouTube agrupa contenido por strings repetidos en títulos → todos los relatos comparten esa cola y YouTube los ofrece como "siguiente vídeo" entre ellos.
- **Hook primero, etiqueta después**: 80% del descubrimiento YouTube es por search/recomendación (no por canal). El gancho del título vende; la etiqueta de serie clasifica. Mobile YouTube corta a ~60 chars → el hook está a salvo en los primeros chars.
- **Em-dash con espacios** (` — `) entre hook y serie. Permitido en títulos (regla `editorial.md` solo prohíbe em-dash en trust-lines ≤15 palabras).
- **Middot `·`** para subseparadores internos (entre hook y serie, o tras "Ficciones Domésticas" para etiqueta de tipo).

**Mapping de nombres legibles de serie** (en `utilities/upload_youtube.py § SERIES_DISPLAY_NAMES`): añadir entrada explícita cuando se cree serie nueva con acrónimos o nombres compuestos (ej: `cartas-a-maia` → `Cartas a MAIA`). Sin entrada, fallback a Title-case automático del slug (`serie-nueva` → `Serie Nueva`) — funciona pero menos pulido.

Ejemplos generados:
- `La objeción — Ficciones Domésticas` (standalone)
- `El cumpleaños · Cartas a MAIA #3 — Ficciones Domésticas` (episodio serie)
- `El primer humanoide — Ficciones Domésticas · Piloto` (piloto opt-in)
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
- [ ] **Verbos honestos**: la descripción NO contiene *"audiolibro producido por nosotros"*, *"hemos grabado"*, *"hemos producido"* ni similares (regla `editorial.md § Honestidad de primera persona`). El tooling TTS específico (ElevenLabs, voz Luis, etc.) **NO se menciona en la descripción YouTube** (decisión 2026-04-25 de Rafael — el lector externo no necesita saber el stack técnico). Sí permitido en notas internas (snapshot, troubleshooting, debug copyright claim).

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

### Vídeo rechazado: "El vídeo es demasiado largo" / `Procesamiento interrumpido`

**Causa:** canal YouTube **no verificado por SMS** → límite 15 min/upload por defecto. Cualquier MP4 más largo (típico para audiolibros standalone de 18-25 min) se rechaza tras subir el bytes completos.

**Síntoma:** YouTube Studio muestra el vídeo en estado "Procesamiento interrumpido" con mensaje "El vídeo es demasiado largo. Más información". `videos.list` API devuelve `failureReason: "El vídeo es demasiado largo"`.

**Fix:**
1. Verificar canal en https://www.youtube.com/verify (cuenta Google del canal ROBOHOGAR) → introducir móvil → SMS → código. ~30 segundos. One-time, vale para siempre.
2. Borrar el vídeo broken desde Studio (o vía `youtube.videos().delete(id='...')` API).
3. Re-invocar `/audiobook-distribute <slug>` — el segundo upload pasará limpio.

**Coste del fallo:** 100 units API extra (re-insert) + ~10 min de tiempo. **Prevención:** verify SMS antes del primer upload (añadido al pre-check 1.f del workflow). Incidente origen: 2026-04-25 sesión "la-objecion".

### `thumbnails.set` HTTP 403: "user doesn't have permissions to upload custom thumbnails"

**Causa:** misma raíz que el bug anterior — canal no verificado SMS. La verify SMS desbloquea **a la vez** los uploads >15 min y los thumbnails custom.

**Síntoma:** `videos.insert` funciona pero `thumbnails.set` falla con HTTP 403. Vídeo aparece en YouTube con thumbnail auto-generado del primer frame.

**Fix:**
1. Verify SMS si no está hecho.
2. Subir thumbnail vía API directa al video existente (NO re-uploadear MP4):
   ```python
   from googleapiclient.discovery import build
   from googleapiclient.http import MediaFileUpload
   from google.oauth2.credentials import Credentials
   creds = Credentials.from_authorized_user_file('<token_path>')
   youtube = build('youtube', 'v3', credentials=creds)
   media = MediaFileUpload('<thumbnail_path>', mimetype='image/png')
   youtube.thumbnails().set(videoId='<videoId>', media_body=media).execute()
   ```
   Coste: 50 units (frente a 150 del re-upload completo).

### Discrepancia capítulos en `chunks-index.json` (falsos positivos)

**Causa:** el regex de `utilities/generate_audio.py` solo matchea headings `Uno. / Dos. / Tres. / ... / Doce.` aislados al inicio de línea. Relatos que usan `Parte uno. / Parte dos. / ...` (convención alternativa) no se detectan correctamente — y palabras como "Uno." en mitad del cuerpo (cardinal numérico narrativo) generan falsos positivos.

**Síntoma:** `chunks-index.json` con `chapters` de menos número del real, títulos extraños (párrafos enteros), o `start_seconds` cerca del final del audio.

**Fix manual** (script Python ad-hoc para reconstruir el index sin re-generar el MP3 ni gastar cuota ElevenLabs):

```python
import re, json
from pathlib import Path

slug = '<slug>'
idx_path = Path(f'assets/audio/ficciones/{slug}-chunks-index.json')
idx = json.loads(idx_path.read_text(encoding='utf-8'))
txt_path = next(Path('content/ficciones').rglob(f'{slug}/audiolibro.txt'))
text = txt_path.read_text(encoding='utf-8')

intro_s = idx['intro_duration_seconds']
# v2 (canónico) tiene silence_after_intro / silence_before_outro separados.
# v1 (la-objecion piloto) tiene un único silence_duration_seconds. Fallback compat.
silence_s = idx.get('silence_after_intro_seconds', idx.get('silence_duration_seconds', 0))
narration_s = idx['narration_duration_seconds']
total_chars = len(text)
chars_per_second = total_chars / narration_s

ordinal_map = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5,
               'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9, 'diez': 10,
               'once': 11, 'doce': 12}
# Probar primero "Parte uno." (más específico), si no hay matches caer a "Uno." aislado
pattern = re.compile(r'^Parte (uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\.\s*([^\n]*)$',
                     re.MULTILINE | re.IGNORECASE)
chapters = []
for m in pattern.finditer(text):
    char_pos = m.start()
    ordinal = m.group(1).lower()
    title = m.group(2).rstrip('.').strip() or f'Parte {ordinal}'
    start_s = intro_s + silence_s + (char_pos / chars_per_second)
    chapters.append({'number': ordinal_map[ordinal], 'title': title,
                     'start_seconds': round(start_s, 2)})
idx['chapters'] = chapters
idx_path.write_text(json.dumps(idx, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'OK reconstruido: {len(chapters)} capítulos')
```

**Fix permanente pendiente:** extender el regex en `utilities/generate_audio.py` para soportar también `Parte X.`. Hasta entonces, el pre-check (e) del workflow detecta la discrepancia y pide reconstruir antes de generar el MP4.

### Token YouTube caducado mid-pipeline

`upload_youtube.py` falla con `invalid_grant` o `Token has been expired or revoked`. Causa: app quedó en "Testing mode" (consent screen) o credenciales revocadas manualmente.

**Fix:** borrar `content/podcast/_oauth-tokens/youtube_token.json` y correr `python utilities/upload_youtube.py --auth`. Tras esto, re-invocar `/audiobook-distribute <slug>`.

### `generate_youtube_video.py` falla con `Invalid argument` antes de empezar a renderizar

**Causa:** filter_complex de ffmpeg muy largo (típico con ≥6 capítulos → ~2900 chars) excede el límite de longitud de línea de comando en Windows.

**Fix permanente aplicado (2026-04-25):** el script ahora escribe el filter_complex a un fichero temporal `<slug>-filter.tmp` y usa `-/filter_complex <file>` en lugar de pasarlo inline. Cleanup en `finally`. Si volviera a aparecer, verificar que el patch sigue en el script (función `main()`, sección "Pasamos el filter_complex via fichero").

### `generate_youtube_video.py` falla con `No option name near '/Windows/Fonts/...'`

**Causa:** filter_complex contiene un path Windows con `:` (típicamente `fontfile=C:/Windows/Fonts/arialbd.ttf`). El parser de filtros de ffmpeg interpreta los `:` como separadores de opciones (`opt1=val1:opt2=val2`); las comillas simples NO protegen el path cuando el filter va por fichero.

**Fix permanente aplicado (2026-04-25):** font copiado a `assets/fonts/arialbd.ttf` (path relativo del repo, sin `:`). `FONT_FILE` en `utilities/generate_youtube_video.py` apunta ahí. Si volviera a aparecer, verificar `ls assets/fonts/arialbd.ttf` y que la constante FONT_FILE no se haya cambiado a path absoluto.

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
