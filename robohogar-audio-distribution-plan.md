# Robohogar — Audio Distribution Pipeline

**Plan de implementación: YouTube + podcast multicanal con automatización máxima**

Versión: 1.0 — Abril 2026
Owner: Rafael
Stack base: Claude Code + GitHub (RRP-DEV) + Beehiiv + Cloudflare R2

---

## 0. Contexto y objetivos

### 0.1 Situación actual

El pipeline de Robohogar ya contempla:

1. Planificación de novela/artículo con Claude Code
2. Generación de HTML para Beehiiv (copy-paste)
3. Generación de audiolibro MP3 con intro/outro básicos
4. Preview del audio en reader local
5. Skill de publicación: sube MP3 a Cloudflare R2, añade reproductor en Beehiiv
6. **Skill de post-publish**: recibe URL del artículo ya publicado → validaciones, catalogación, mantenimiento

### 0.2 Objetivos del plan

**Primario:**
- Añadir distribución automática del audiolibro a YouTube + plataformas de podcast
- Trigger: extensión del skill **post-publish** existente (el MP3 y la thumbnail ya existen)
- Coste humano por episodio: **≤ 1 min** (solo confirmación)

**Secundarios:**
- Tráfico al newsletter desde YouTube + podcast (CTA en intro/outro + descripciones)
- Preparar camino para monetización (YouTube ads + posible Premium en newsletter)
- Canal YouTube extensible a otros formatos (shorts tech, reviews) en el futuro

### 0.3 Criterios de éxito

- [ ] Un solo comando (`post-publish <url>`) dispara publicación en todas las plataformas
- [ ] Proceso semi-automático: Claude Code sugiere, Rafael confirma
- [ ] Zero re-encoding manual de MP3 entre plataformas
- [ ] RSS feed único como source-of-truth para todos los agregadores de podcast

---

## 1. Arquitectura high-level

```
┌──────────────────────────────────────────────────────────────────┐
│  PIPELINE EXISTENTE (no se toca)                                 │
│  ─────────────────────────────────                               │
│  Plan → HTML Beehiiv → MP3 (intro+outro+contenido) → R2 upload   │
│  → reproductor Beehiiv → artículo publicado                      │
└──────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│  SKILL post-publish (EXISTENTE, se extiende)                     │
│  ─────────────────────────────────────────                       │
│  Input: URL artículo Beehiiv                                     │
│  Tareas actuales: validaciones, catalogación, registro           │
│  ────────────────────────────────────────────                    │
│  NUEVO submódulo: publish-audio/                                 │
│    1. Detectar si el artículo es ficción (frontmatter/tag)       │
│    2. Extraer metadata (título, descripción, thumbnail, MP3 URL) │
│    3. Sugerir CTA y descripciones → esperar confirmación         │
│    4. Generar MP4 con waveform                                   │
│    5. Subir a YouTube (scheduled 09:00 Madrid siguiente día)     │
│    6. Append item al RSS feed                                    │
│    7. Push RSS a Cloudflare Pages                                │
│    8. Registro en vault + notificación                           │
└──────────────────────────────────────────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
┌──────────────────────┐    ┌─────────────────────────────────────┐
│  YouTube (API v3)    │    │  RSS Feed (Cloudflare Pages)         │
│  ────────────────    │    │  ──────────────────────────          │
│  robohogar.com/yt    │    │  robohogar.com/podcast/feed.xml      │
│  Scheduled publish   │    │                                      │
└──────────────────────┘    │  Agregado por (pull automático):     │
                            │    - Spotify                         │
                            │    - Apple Podcasts                  │
                            │    - Amazon Music                    │
                            │    - iVoox                           │
                            │    - Pocket Casts, Overcast, Castbox │
                            └─────────────────────────────────────┘
```

---

## 2. Decisiones de diseño (confirmadas)

| Decisión | Valor |
|----------|-------|
| MP3 para YouTube | Mismo final (con intro/outro) |
| Intro/outro | **Rediseñar** con CTA newsletter — aplica a todas las plataformas |
| Publicación YouTube | Scheduled: 09:00 Madrid del día siguiente |
| Contenido del RSS | **Solo ficción** (futuro: tier premium con series) |
| Canal YouTube | `Robohogar` (nombre corto, extensible a otros formatos) |
| Nombre del podcast | `Robohogar — Relatos de Ficción` |
| Modo de ejecución | **Semi-automático**: Claude sugiere → Rafael confirma → ejecuta |
| Plataformas podcast | Máximas posibles vía RSS único (gratis) |

---

## 3. Prerequisitos — Setup de plataformas

> **Nota**: Esta sección es one-off. Se hace una sola vez. El checklist siguiente asume que Rafael ejecuta manualmente (no automatizable, requieren KYC / browser login).

### 3.1 Canal de YouTube (Brand Account)

**Por qué Brand Account y no cuenta personal:**
- Se puede transferir ownership sin mover de cuenta Google
- Permite múltiples admins en el futuro
- Separa identidad de marca de la personal
- No pierde seguidores si cambias de email

**Pasos:**

1. Ir a [studio.youtube.com](https://studio.youtube.com)
2. Clic en avatar (esquina superior derecha) → **Cambiar cuenta** → **Añadir cuenta**
3. Clic **Crear un canal** → **Usar un nombre comercial o de empresa**
4. Nombre: `Robohogar`
5. Handle (URL): `@robohogar` (verificar disponibilidad)
6. **Personalizar canal:**
   - Descripción: reutilizar la del newsletter, añadir enlace al newsletter como primer link
   - Banner: 2560×1440, identidad visual Robohogar
   - Foto de perfil: 800×800, logo Robohogar
   - Enlaces: newsletter (primario), web, redes
7. **Configuración → Canal → Información básica:**
   - Palabras clave: `robohogar, robótica doméstica, ficción, audiolibro, hogar inteligente, humanoides, futuro`
   - País: España
   - Idioma del canal: Español
8. **Configuración → Subidas por defecto:**
   - Privacidad: `Pública` (se sobrescribirá por el script a `scheduled`)
   - Categoría: `Ciencia y tecnología` o `Cine y animación` (decidir durante fase 1)
   - Licencia: `Estándar de YouTube`
   - Permitir inserción: `Sí`
   - Notificar a suscriptores: `Sí`
9. **Playlist inicial:**
   - Crear playlist `Relatos de Ficción` — pública, descripción + thumbnail

**Checklist completo:**
- [ ] Canal `Robohogar` creado como Brand Account
- [ ] Handle `@robohogar` asignado
- [ ] Banner, avatar, descripción publicados
- [ ] Verificación de número de teléfono completada (imprescindible para subidas > 15 min)
- [ ] Playlist `Relatos de Ficción` creada

---

### 3.2 YouTube Data API v3 — OAuth

**Objetivo:** obtener `client_id`, `client_secret` y `refresh_token` para que los scripts suban vídeos sin intervención humana.

**Pasos:**

1. Ir a [console.cloud.google.com](https://console.cloud.google.com)
2. Crear proyecto: `robohogar-automation`
3. Menú ☰ → **APIs y servicios** → **Biblioteca**
4. Buscar `YouTube Data API v3` → **Habilitar**
5. Menú → **APIs y servicios** → **Pantalla de consentimiento OAuth**
   - Tipo de usuario: **Externo**
   - Nombre de la app: `Robohogar Publisher`
   - Email de asistencia: tu email
   - Dominio autorizado: `robohogar.com`
   - **Scopes**: añadir `https://www.googleapis.com/auth/youtube.upload` y `https://www.googleapis.com/auth/youtube`
   - **Usuarios de prueba**: añadir tu email propio (mientras la app esté en modo testing)
6. Menú → **APIs y servicios** → **Credenciales** → **Crear credenciales** → **ID de cliente OAuth**
   - Tipo: **Aplicación de escritorio**
   - Nombre: `robohogar-cli`
   - Descargar JSON → guardar en `RRP-DEV/robohogar/secrets/oauth-client.json` (añadir a `.gitignore`)
7. **Obtener refresh token (una sola vez):**
   - Script auxiliar `scripts/get-youtube-refresh-token.mjs` (lo generamos en Fase 4)
   - Abre browser, hace login, captura el authorization code
   - Intercambia por refresh token
   - Guarda en `.env` como `YOUTUBE_REFRESH_TOKEN`

**Cuota API (gratis):**
- 10.000 units/día por defecto
- `videos.insert` consume ~1.600 units
- Margen: ~6 subidas/día (más que suficiente)

**Checklist:**
- [ ] Proyecto `robohogar-automation` creado
- [ ] YouTube Data API v3 habilitada
- [ ] OAuth client ID creado (escritorio)
- [ ] `oauth-client.json` descargado y gitignored
- [ ] Refresh token obtenido y guardado en `.env`

---

### 3.3 RSS Feed — Hosting en Cloudflare Pages

**Decisión:** alojar el RSS en `robohogar.com/podcast/feed.xml` (subdirectorio del dominio principal para mantener SEO y branding).

**Arquitectura:**

```
RRP-DEV/
├── robohogar/
│   ├── podcast/
│   │   ├── feed.xml            ← generado dinámicamente
│   │   ├── episodes.json       ← metadata fuente de verdad
│   │   └── cover-3000.jpg      ← portada del show
│   └── scripts/
│       └── regenerate-rss.mjs
└── .github/
    └── workflows/
        └── deploy-podcast.yml  ← push a Cloudflare Pages
```

**Especificaciones RSS 2.0 + iTunes:**

El XML debe incluir tags iTunes obligatorios para que Apple acepte el feed:
- `<itunes:author>`, `<itunes:category>`, `<itunes:explicit>`, `<itunes:image>`
- `<itunes:owner>` con `<itunes:email>` (usar email dedicado, no personal)
- Por episodio: `<itunes:duration>`, `<itunes:episode>`, `<itunes:title>`

**Portada del show:**
- 3000×3000 px (mínimo 1400×1400 por Apple)
- JPG/PNG, RGB, < 500 KB
- Sin texto extra al nombre del show (reglas Apple)

**Pasos setup:**

1. Crear subdominio/ruta `robohogar.com/podcast/`
2. Diseñar portada 3000×3000 → guardar como `cover-3000.jpg`
3. Crear `episodes.json` vacío: `{ "episodes": [] }`
4. Implementar `regenerate-rss.mjs` (Fase 5) que lee `episodes.json` y escupe `feed.xml`
5. Configurar GitHub Action para publicar a Cloudflare Pages al push en `main`
6. Validar el feed en [podba.se/validate](https://podba.se/validate) y [castfeedvalidator.com](https://castfeedvalidator.com)

**Checklist:**
- [ ] Portada 3000×3000 diseñada
- [ ] Estructura `robohogar.com/podcast/` creada
- [ ] `episodes.json` inicial commited
- [ ] GitHub Action desplegando a Cloudflare Pages
- [ ] `feed.xml` validado en ambos validadores (cero errores)

---

### 3.4 Spotify for Creators

**Antes conocido como Spotify for Podcasters / Anchor.**

1. Ir a [creators.spotify.com](https://creators.spotify.com)
2. Iniciar sesión con cuenta Spotify (usar email dedicado de Robohogar si tienes; si no, personal)
3. **Crear show** → **Tengo un podcast existente** → pegar URL del RSS (`https://robohogar.com/podcast/feed.xml`)
4. Spotify hace fetch del RSS, extrae metadata, valida
5. Completar categorías, país (España), idioma (Español)
6. Subir prueba de propiedad: Spotify envía email de verificación al `<itunes:owner><itunes:email>` del RSS → **imprescindible** usar email que controles
7. Confirmar propiedad
8. Revisar y enviar — aprobación típicamente en minutos

**Checklist:**
- [ ] Show creado desde RSS externo
- [ ] Email de verificación recibido y confirmado
- [ ] Show aprobado y visible en búsqueda de Spotify

---

### 3.5 Apple Podcasts Connect

Requiere **Apple ID** (gratis) — no requiere Apple Developer Program ($99/año).

1. Ir a [podcastsconnect.apple.com](https://podcastsconnect.apple.com)
2. Iniciar sesión con Apple ID
3. Clic **+** → **New Show** → **Add a show with an RSS feed**
4. Pegar URL del RSS
5. Apple hace fetch, valida todos los tags iTunes obligatorios
6. Elegir categorías primaria + secundaria:
   - Primaria: `Fiction` → `Science Fiction`
   - Secundaria: `Technology`
7. Submit → aprobación en 1-5 días (Apple revisa manualmente)

**Checklist:**
- [ ] Show creado desde RSS
- [ ] Categorías asignadas
- [ ] Submitted a review
- [ ] Aprobado y visible en Apple Podcasts

---

### 3.6 Amazon Music for Podcasters

Distribuye también a **Audible**.

1. Ir a [podcasters.amazon.com](https://podcasters.amazon.com)
2. Iniciar sesión con cuenta Amazon
3. **Add a podcast** → pegar URL del RSS
4. Verificación por email al owner del RSS
5. Elegir categoría → submit
6. Aprobación: 1-3 días

**Checklist:**
- [ ] Show creado desde RSS
- [ ] Verificación completada
- [ ] Aprobado y visible

---

### 3.7 iVoox — audiencia hispana

Plataforma española/latinoamericana muy fuerte, no debería faltar.

1. Ir a [ivoox.com](https://www.ivoox.com) → Crear cuenta
2. Menú de usuario → **Subir audios** → **Tengo un podcast**
3. Pegar URL del RSS
4. iVoox importa todo el histórico automáticamente y sincroniza nuevos episodios
5. Completar perfil del show: categoría, tags, descripción extendida
6. Activar monetización de iVoox (opcional, reparto por reproducciones)

**Checklist:**
- [ ] Cuenta creada
- [ ] Podcast añadido vía RSS
- [ ] Perfil completado
- [ ] (Opcional) Monetización activada

---

### 3.8 Plataformas que indexan automáticamente (sin acción requerida)

Una vez que Apple y Spotify aprueben el show, estas plataformas lo listan solas en días:

- **Pocket Casts** — indexa desde Apple
- **Overcast** — indexa desde Apple
- **Castbox** — buscar el show y añadir manualmente acelera la indexación
- **Podcast Addict** — idem
- **Podchaser** — agregador/directorio, útil para SEO

**Opcional** (5 min cada uno): crear el show manualmente en Castbox y Podcast Addict para aparecer antes.

---

## 4. Rediseño intro/outro con CTA newsletter

### 4.1 Guión propuesto (español neutro, tono Spain)

**INTRO — 15s**
> "Bienvenidos a *Robohogar — Relatos de Ficción*. Historias cortas sobre cómo será vivir con máquinas en casa. Si te gusta lo que escuchas, suscríbete al newsletter en **robohogar.com** — cada semana un relato nuevo y análisis sobre robótica doméstica. Empezamos."

**OUTRO — 20s**
> "Has escuchado un relato de Robohogar. Si te ha gustado, compártelo y suscríbete al newsletter en **robohogar.com** para no perderte los siguientes episodios. También puedes escucharnos en Spotify, Apple Podcasts y YouTube — busca *Robohogar*. Hasta el próximo relato."

### 4.2 Consideraciones

- **Consistencia de voz**: generar con el mismo TTS que usas ahora (ElevenLabs / OpenAI TTS / Google). Mantener misma `voice_id` y `settings`.
- **Ambient bed opcional**: fondo sutil (sonido de una habitación futurista, ambient mínimo) que dé identidad sin distraer. Si complica, dejarlo sin fondo.
- **Archivos reutilizables**: generar `intro.mp3` y `outro.mp3` una vez, concatenar con `ffmpeg concat` en cada episodio (NO regenerar con TTS cada vez — malgasta créditos).

### 4.3 Concatenación en pipeline

```bash
# ffmpeg concat sin re-encoding
cat > concat.txt <<EOF
file 'intro.mp3'
file 'content.mp3'
file 'outro.mp3'
EOF

ffmpeg -f concat -safe 0 -i concat.txt -c copy episodio-final.mp3
```

### 4.4 Checklist

- [ ] Validar guión con Rafael (posibles ajustes de tono)
- [ ] Generar `intro.mp3` y `outro.mp3` con TTS
- [ ] Guardar en `robohogar/assets/audio/` (versionar en Git — son < 1 MB cada uno)
- [ ] Modificar el skill de generación de audiolibro para usar estos nuevos archivos
- [ ] Test con 1 relato existente: regenerar versión final con los nuevos intro/outro
- [ ] Validar escucha manual antes de publicar nada

---

## 5. Módulo `publish-audio` del skill post-publish

### 5.1 Estructura de archivos

```
robohogar/
├── skills/
│   └── post-publish/
│       ├── SKILL.md                        ← actualizar: añadir step "publish-audio"
│       └── modules/
│           └── publish-audio/              ← NUEVO
│               ├── README.md
│               ├── index.mjs               ← orchestrator
│               ├── generate-mp4.mjs        ← ffmpeg + waveform
│               ├── upload-youtube.mjs      ← YouTube Data API
│               ├── update-rss.mjs          ← append a episodes.json + regenerate RSS
│               ├── prompts/
│               │   ├── youtube-description.md
│               │   └── episode-metadata.md
│               └── templates/
│                   └── rss-item.xml.tpl
├── assets/
│   └── audio/
│       ├── intro.mp3
│       └── outro.mp3
├── podcast/
│   ├── feed.xml                            ← regenerado
│   ├── episodes.json                       ← source of truth
│   └── cover-3000.jpg
└── secrets/                                ← gitignored
    ├── oauth-client.json
    └── .env
```

### 5.2 Variables de entorno (`.env`)

```bash
# YouTube
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_REFRESH_TOKEN=
YOUTUBE_CHANNEL_ID=
YOUTUBE_FICTION_PLAYLIST_ID=

# Cloudflare R2 (si aún no está en env)
R2_ACCESS_KEY=
R2_SECRET_KEY=
R2_BUCKET=robohogar
R2_PUBLIC_URL=https://cdn.robohogar.com

# Podcast
PODCAST_FEED_URL=https://robohogar.com/podcast/feed.xml
PODCAST_COVER_URL=https://robohogar.com/podcast/cover-3000.jpg
PODCAST_OWNER_EMAIL=podcast@robohogar.com
```

### 5.3 Orchestrator (`index.mjs`) — pseudocódigo

```javascript
export async function publishAudio({ articleUrl, dryRun = false }) {
  // 1. Extraer metadata
  const meta = await extractArticleMetadata(articleUrl);
  // { title, description, thumbnailUrl, mp3Url, isFiction, publishedAt, slug }

  if (!meta.isFiction) {
    console.log('No es ficción, skip publish-audio.');
    return;
  }

  // 2. Generar sugerencias (Claude compone título YT + descripción + tags)
  const suggestions = await generateYouTubeMetadata(meta);
  // { youtubeTitle, youtubeDescription, tags[], podcastEpisodeTitle, podcastDescription }

  // 3. Mostrar al usuario para confirmación
  console.log(renderSuggestions(suggestions));
  const approved = await confirm('¿Publicar con estos metadatos? (s/n/editar)');
  if (!approved) return;

  // 4. Descargar MP3 de R2 a /tmp
  const mp3Path = await downloadMp3(meta.mp3Url);

  // 5. Descargar thumbnail
  const thumbPath = await downloadImage(meta.thumbnailUrl);

  // 6. Generar MP4 con waveform
  const mp4Path = await generateMp4({ mp3Path, thumbPath, outputPath: '/tmp/episode.mp4' });

  // 7. Upload a YouTube (scheduled)
  const publishAt = nextDayAt9amMadrid();
  const youtubeVideoId = await uploadToYouTube({
    mp4Path,
    thumbPath,
    title: suggestions.youtubeTitle,
    description: suggestions.youtubeDescription,
    tags: suggestions.tags,
    playlistId: process.env.YOUTUBE_FICTION_PLAYLIST_ID,
    privacyStatus: 'private',
    publishAt,
  });

  // 8. Append al RSS
  await appendEpisodeToRss({
    title: suggestions.podcastEpisodeTitle,
    description: suggestions.podcastDescription,
    mp3Url: meta.mp3Url,
    publishedAt: meta.publishedAt,
    durationSeconds: await getAudioDuration(mp3Path),
    guid: meta.slug,
  });

  // 9. Git commit + push → GitHub Action despliega a Cloudflare Pages
  await commitAndPush(`feat(podcast): add episode "${suggestions.podcastEpisodeTitle}"`);

  // 10. Registrar en vault y notificar
  await updateVault({ articleUrl, youtubeVideoId, rssGuid: meta.slug });
  return { youtubeVideoId, podcastGuid: meta.slug };
}
```

---

## 6. Flujo end-to-end semi-automático

Flujo que verá Rafael tras ejecutar `post-publish https://robohogar.com/historia-X`:

```
[post-publish] Ejecutando validaciones y catalogación...  ✓
[post-publish] Detectado artículo tipo: ficción
[post-publish] ▶ Lanzando módulo publish-audio

[publish-audio] Metadata del artículo extraída:
  Título:       "El último técnico de Neo-Valencia"
  Duración:     23:47
  Thumbnail:    ✓
  MP3:          ✓

[publish-audio] Metadatos sugeridos para YouTube:

  ┌─────────────────────────────────────────────────────────┐
  │ TÍTULO (YouTube)                                        │
  │ El último técnico de Neo-Valencia | Relato de ficción   │
  │                                                         │
  │ DESCRIPCIÓN                                             │
  │ 📬 Suscríbete al newsletter: https://robohogar.com     │
  │                                                         │
  │ En 2047, los técnicos humanos ya no reparan robots      │
  │ domésticos. Marco es el último…                         │
  │                                                         │
  │ ⏱ Capítulos:                                            │
  │ 00:00 Introducción                                      │
  │ 00:15 El relato                                         │
  │ 23:30 Cierre                                            │
  │                                                         │
  │ 🎧 También en Spotify, Apple Podcasts y iVoox          │
  │                                                         │
  │ TAGS                                                    │
  │ robohogar, ficción, audiolibro, robótica, cyberpunk,    │
  │ relato, hogar inteligente                               │
  │                                                         │
  │ PROGRAMACIÓN                                            │
  │ Publicación: Mañana 25/04/2026 09:00 (Madrid)           │
  └─────────────────────────────────────────────────────────┘

  ¿Publicar? [s]í / [n]o / [e]ditar: _
```

Si confirma → ejecuta los 8 pasos del orchestrator → devuelve:

```
[publish-audio] ✓ MP4 generado (74 MB)
[publish-audio] ✓ YouTube upload completado
                  Video ID: dQw4w9WgXcQ
                  Programado: 25/04/2026 09:00 CEST
                  URL: https://youtu.be/dQw4w9WgXcQ
[publish-audio] ✓ RSS actualizado (14 episodios totales)
[publish-audio] ✓ Git push → Cloudflare Pages desplegando
[publish-audio] ✓ Vault actualizado: episodios/2026-04-24-neo-valencia.md
[publish-audio] ✔ Completado en 2m 34s
```

---

## 7. Plan de implementación por fases

### Fase 1 — Setup plataformas (humano, ~3h total)

Secuencial, cada paso bloquea el siguiente:

1. [ ] Crear canal YouTube Brand Account `Robohogar` (§3.1)
2. [ ] Crear proyecto GCP + habilitar YouTube Data API v3 (§3.2)
3. [ ] Descargar `oauth-client.json`, gitignorear
4. [ ] Diseñar portada podcast 3000×3000 (§3.3)
5. [ ] Crear estructura `robohogar.com/podcast/` + GitHub Action a Cloudflare Pages
6. [ ] Crear email dedicado `podcast@robohogar.com` (necesario para verificación)

> **Nota importante**: los pasos 7-10 esperan a tener el feed publicado (Fase 5) porque validan el RSS antes de aceptar el show.

### Fase 2 — Rediseño intro/outro (~1h)

1. [ ] Validar el guión propuesto (§4.1) — ajustar si Rafael quiere otro tono
2. [ ] Generar `intro.mp3` y `outro.mp3` con TTS actual
3. [ ] Escucha manual: confirmar calidad y duración
4. [ ] Commit a `robohogar/assets/audio/`
5. [ ] Modificar skill de generación de audiolibro: usar `concat.txt` + nuevos archivos
6. [ ] Regenerar 1 relato existente como prueba
7. [ ] Aprobar manualmente

### Fase 3 — Generación MP4 con waveform (~1h)

1. [ ] Script `generate-mp4.mjs` con ffmpeg (§1 del plan anterior)
2. [ ] Test con un MP3 y thumbnail existentes
3. [ ] Ajustar parámetros de waveform (color, tamaño, posición) hasta match con identidad Robohogar
4. [ ] Documentar flags en `modules/publish-audio/README.md`

### Fase 4 — Integración YouTube (~2h)

1. [ ] Script `get-youtube-refresh-token.mjs` (one-off, obtener refresh token)
2. [ ] Ejecutar una vez → guardar token en `.env`
3. [ ] Script `upload-youtube.mjs`:
   - `videos.insert` con `privacyStatus: 'private'` y `publishAt`
   - Set thumbnail con `thumbnails.set`
   - Add to playlist con `playlistItems.insert`
4. [ ] Test con vídeo dummy (programar a mañana, luego borrar)
5. [ ] Verificar: aparece en YouTube Studio como "Scheduled"

### Fase 5 — RSS feed automation (~2h)

1. [ ] Script `regenerate-rss.mjs`: lee `episodes.json` → genera `feed.xml`
2. [ ] Script `update-rss.mjs`: append nuevo episode a `episodes.json` + llama regenerar
3. [ ] Primera versión del `feed.xml` con 0 episodios (válida para Apple/Spotify)
4. [ ] Commit + GitHub Action deploya
5. [ ] Validar en [podba.se/validate](https://podba.se/validate) + [castfeedvalidator.com](https://castfeedvalidator.com)
6. [ ] Arreglar cualquier warning hasta 0 errores

### Fase 6 — Submissions a agregadores (humano, ~1h distribuido)

> Bloqueado por Fase 5. Una vez el RSS está live y validado:

1. [ ] Spotify for Creators (§3.4) — aprobación en minutos
2. [ ] Apple Podcasts Connect (§3.5) — aprobación 1-5 días
3. [ ] Amazon Music (§3.6) — aprobación 1-3 días
4. [ ] iVoox (§3.7) — aprobación rápida
5. [ ] (Opcional) Castbox, Podcast Addict

### Fase 7 — Integración en skill post-publish (~1h)

1. [ ] Actualizar `SKILL.md` de post-publish: añadir sección "publish-audio"
2. [ ] Implementar `orchestrator index.mjs` (§5.3)
3. [ ] Implementar `generateYouTubeMetadata` con Claude (prompt en `prompts/episode-metadata.md`)
4. [ ] Implementar `confirm()` interactivo (readline)
5. [ ] Integrar `updateVault()` con la estructura existente

### Fase 8 — Testing end-to-end (~1h)

1. [ ] Elegir relato existente no publicado en YouTube ni en podcast
2. [ ] Ejecutar `post-publish <url>` en modo `--dry-run` → validar sugerencias
3. [ ] Ejecutar sin dry-run → confirmar
4. [ ] Esperar a las 09:00 del día siguiente
5. [ ] Validar:
   - [ ] YouTube: publicado, thumbnail correcta, en playlist, descripción con CTA
   - [ ] Spotify: episodio visible tras unas horas (Spotify pulls cada 30-60 min)
   - [ ] Apple Podcasts: episodio visible (Apple pulls cada pocas horas)
   - [ ] iVoox: episodio visible
6. [ ] Comprobar CTAs funcionales (clicks en descripciones)
7. [ ] **Go live**: declarar flujo operativo, usar en el próximo episodio real

---

## 8. Monitorización y métricas

### 8.1 Qué medir

**YouTube:**
- Subs ganados por episodio
- CTR miniatura → clic
- Retención (%) — objetivo: >50% con waveform vs ~25% con imagen estática
- Clicks a link del newsletter (tracking con UTM)

**Podcast:**
- Descargas totales por plataforma (Spotify da dashboard; Apple solo a 100+ seguidores)
- Top episodios
- Evolución semanal

**Newsletter (conversión):**
- UTM `?utm_source=youtube&utm_medium=audio&utm_campaign=fiction`
- UTM `?utm_source=spotify&utm_medium=podcast`
- Comparar con tráfico orgánico

### 8.2 Dashboard sugerido

Un HTML dashboard que ya sabes construir, consumiendo:
- YouTube Analytics API
- Spotify for Creators API (lectura)
- Beehiiv subscribers API (conversiones)

No crítico para Fase 1-8. Añadir como Fase 9 cuando haya al menos 10 episodios de datos.

---

## 9. Roadmap futuro (post-MVP)

### 9.1 Series con personajes consistentes → Premium

- Newsletter: tier premium en Beehiiv (ya soporta paid subscriptions)
- Acceso a series completas solo para suscriptores pagos
- **En podcast/YouTube**: publicar SOLO el episodio 1 de cada serie como teaser; episodios 2+ solo en newsletter (miembros pagos)
- CTA: "Para escuchar el siguiente episodio, entra en robohogar.com/premium"

### 9.2 Contenido técnico en YouTube (shorts + largos)

- Reviews de productos de robótica doméstica (Roomba, robots limpieza, humanoides consumer)
- Shorts (60s) sobre noticias de robótica
- Explainers de IA aplicada al hogar
- **Ventaja**: mismo canal, algoritmo YouTube cross-promociona entre tipos de contenido
- **Pipeline diferente**: requeriría skill nuevo `publish-tech-video`

### 9.3 Monetización directa

- YouTube ads cuando se llegue a 1.000 subs + 4.000 horas
- Spotify for Creators monetization (ya disponible)
- iVoox Fans / Patreon / Substack Originals (futuro)
- Sponsorships cuando haya tracción (>5k subs/seguidores)

### 9.4 Transcripciones SEO

- Whisper → transcripción de cada episodio
- Publicar en `robohogar.com/transcripciones/<slug>` como HTML
- Beneficio: SEO enorme, tráfico orgánico a Google

---

## 10. Apéndice

### 10.1 Comando ffmpeg de referencia

```bash
# MP4 con thumbnail fija + waveform animado superpuesto abajo
ffmpeg -loop 1 -i thumb.jpg -i audio.mp3 -filter_complex \
  "[1:a]showwaves=s=1920x300:mode=cline:colors=0xD4638F@0.8:rate=25[wave]; \
   [0:v]scale=1920:1080,setsar=1[bg]; \
   [bg][wave]overlay=0:H-h-60:shortest=1[v]" \
  -map "[v]" -map 1:a \
  -c:v libx264 -preset medium -tune stillimage -crf 23 \
  -c:a aac -b:a 192k \
  -pix_fmt yuv420p -movflags +faststart \
  -shortest output.mp4
```

Flags relevantes:
- `showwaves mode=cline` — línea continua, estético
- `colors=0xD4638F@0.8` — rosa Robohogar con 80% opacidad
- `overlay=0:H-h-60` — waveform a 60px del borde inferior
- `-tune stillimage` — optimiza para fondo estático
- `-movflags +faststart` — streaming-friendly

### 10.2 Estructura mínima de `rss-item.xml.tpl`

```xml
<item>
  <title><![CDATA[{{title}}]]></title>
  <description><![CDATA[{{description}}]]></description>
  <pubDate>{{pubDate}}</pubDate>
  <enclosure url="{{mp3Url}}" length="{{mp3SizeBytes}}" type="audio/mpeg" />
  <guid isPermaLink="false">{{guid}}</guid>
  <itunes:author>Robohogar</itunes:author>
  <itunes:duration>{{durationHHMMSS}}</itunes:duration>
  <itunes:explicit>false</itunes:explicit>
  <itunes:episode>{{episodeNumber}}</itunes:episode>
  <itunes:title>{{title}}</itunes:title>
  <itunes:image href="{{episodeArtworkUrl}}" />
  <link>{{articleUrl}}</link>
</item>
```

### 10.3 Librerías Node recomendadas

```json
{
  "dependencies": {
    "googleapis": "^144.0.0",        // YouTube Data API
    "fluent-ffmpeg": "^2.1.3",        // Wrapper de ffmpeg
    "music-metadata": "^10.0.0",      // Leer duración MP3
    "feed": "^4.2.2",                 // Generar RSS
    "dotenv": "^16.4.5",
    "chalk": "^5.3.0",                // Logs con color
    "@inquirer/prompts": "^5.0.0"     // Prompts interactivos
  }
}
```

### 10.4 Cheatsheet de comandos

```bash
# Obtener refresh token (one-off)
node scripts/get-youtube-refresh-token.mjs

# Regenerar RSS desde episodes.json
node robohogar/podcast/regenerate-rss.mjs

# Validar feed en CLI
npx podcast-validator https://robohogar.com/podcast/feed.xml

# Post-publish full
node skills/post-publish/run.mjs --url https://robohogar.com/articulo

# Post-publish dry-run (solo muestra sugerencias)
node skills/post-publish/run.mjs --url https://robohogar.com/articulo --dry-run

# Solo re-subir audio (saltarse validaciones)
node skills/post-publish/run.mjs --url <url> --only publish-audio
```

---

## 11. Checklist master

Copiar a un issue de GitHub tipo "Milestone: Robohogar audio distribution MVP":

**Fase 1 — Plataformas**
- [ ] Canal YouTube Brand Account
- [ ] GCP + YouTube Data API v3
- [ ] OAuth credentials descargadas
- [ ] Portada podcast diseñada
- [ ] Estructura `/podcast/` + GH Action
- [ ] Email dedicado `podcast@robohogar.com`

**Fase 2 — Intro/outro**
- [ ] Guión aprobado
- [ ] `intro.mp3` generado
- [ ] `outro.mp3` generado
- [ ] Skill audiolibro actualizado
- [ ] Test con relato existente

**Fase 3 — MP4 generation**
- [ ] Script `generate-mp4.mjs`
- [ ] Ajuste visual validado

**Fase 4 — YouTube upload**
- [ ] Refresh token obtenido
- [ ] Script `upload-youtube.mjs`
- [ ] Test con vídeo dummy

**Fase 5 — RSS**
- [ ] `regenerate-rss.mjs`
- [ ] `update-rss.mjs`
- [ ] feed.xml inicial live
- [ ] Validación 0 errores

**Fase 6 — Submissions**
- [ ] Spotify aprobado
- [ ] Apple aprobado
- [ ] Amazon aprobado
- [ ] iVoox aprobado

**Fase 7 — Integración**
- [ ] Orchestrator funcional
- [ ] SKILL.md post-publish actualizado

**Fase 8 — Testing**
- [ ] E2E pasado
- [ ] Primer episodio real publicado

---

**Fin del plan v1.0**
