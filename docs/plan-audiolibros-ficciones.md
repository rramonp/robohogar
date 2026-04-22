# Plan — Audiolibros para Ficciones Domésticas

**Estado:** Catalogado, pendiente activación.
**Fecha catálogo:** 2026-04-19.
**Decisión de arranque:** cuando Rafael publique el próximo relato de Ficciones Domésticas.

## 📌 Frases trigger para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Arrancar el piloto | **"Retomamos plan audiolibros — empezamos piloto manual con \<slug-relato\>"** |
| Montar el skill automatizado | **"Retomamos plan audiolibros — monta `/audiobook-generate`"** |
| Ver estado del plan | **"¿En qué fase del plan audiolibros estamos?"** |

Con esas frases, Claude debe:
1. Leer este archivo.
2. Revisar los checkboxes de cada fase.
3. Retomar en el primer paso pendiente.

## Objetivo

Ofrecer en cada relato de Ficciones Domésticas publicado en Beehiiv (`robohogar.com/p/<slug>`) un reproductor de audio embebido **in-page** + botón de descarga MP3, con el mismo MP3 hosteado externamente y embebido vía Custom HTML en el post.

## Decisiones cerradas en conversación 2026-04-19

- **Reproducción:** `<audio controls>` HTML5 nativo, streaming in-page dentro del propio post Beehiiv (no página custom; Beehiiv ya da URL única por relato).
- **Descarga:** botón explícito `<a href download>` además del reproductor, pensado para "escuchar en el coche".
- **Intro de marca (5-8s) — texto TTS:** *"Ficciones Domésticas, de ROBO OGAR."* + 2s silencio. (Visual de marca sigue siendo "ROBOHOGAR" — el texto TTS separa en 2 palabras y **elimina la H** para que el Multilingual v2 no aspire la H estilo inglés, que al oído peninsular suena cercano a "robojogar". La H es muda en español, por lo que al oyente el resultado es indistinguible de "ROBOHOGAR" escrito. Convención validada por Rafael 2026-04-22 tras probar en ElevenLabs Studio con la voz Luis.)
- **Outro de marca (10-15s) — texto TTS:** *"Has escuchado una Ficción Doméstica de ROBO OGAR. Si te ha gustado, puedes leer más relatos y suscribirte al newsletter en ROBO OGAR punto com."* (URL: "ROBO OGAR punto com" en la misma convención de la marca + "punto com" explícito en vez de `.com` para forzar lectura correcta).
- **Mid-roll:** descartado. Rompe inmersión y contradice el posicionamiento premium del pilar ficción. Excepción permitida: bumper de 3s "ROBOHOGAR" entre episodios de mini-serie como sello sonoro.
- **Voz narrador:** única y consistente para todos los relatos (sello sonoro reconocible = tipografía sonora). Voice_id ElevenLabs pendiente elegir.
- **Motor TTS:** ElevenLabs API (ya validado por Rafael como herramienta de uso personal en ElevenLabs Reader).
- **Plan ElevenLabs:** **Starter, yearly billing ($5/mes, ~$60/año)** con commercial license explícita incluida (verificado 2026-04-22 en el banner del plan en [elevenlabs.io/pricing](https://elevenlabs.io/pricing)). Razón descarte de pay-as-you-go y Creator: pay-as-you-go deja ambigüedad sobre commercial license que no se resuelve sin soporte; Creator $11-22/mes es overkill hasta que haya Professional Voice Clone (fase posterior). Starter cubre holgado el volumen ROBOHOGAR (~60.000 chars Multilingual v2/mes = ~4 relatos/mes con regeneraciones).
- **Modelo TTS:** **Multilingual v2/v3** ($0,10/1.000 chars en overage). Obligatorio para ficción literaria ES con matiz emocional. Flash/Turbo descartado (optimizado para chatbots, perdería textura narrativa).
- **Voz narrador — política:** voz del marketplace ES de ElevenLabs (gratis, disponible en Starter). Upgrade a Instant Voice Clone o Professional Voice Clone propia diferido a fase posterior con señal de audiencia real.
- **Voz narrador — decisión cerrada 2026-04-22:** **Luis — Polished, Mature and Credible** (`voice_id = GojDwihhnL1f7RrBuXsJ`). Categoría `professional`, use_case `narrative_story`, accent `peninsular`, language `es`, age `old` (62 según descripción propia). Razones: (a) fit perfecto con arquetipo narrador ROBOHOGAR editorial (warm, mature, credible, no flashy); (b) accent peninsular sin traslado a ES neutro latino que descartaría el registro target del medio; (c) optimizada para `narrative_story` por el propio proveedor de la voz, no voz genérica conversacional; (d) validada por Rafael tras uso previo en ElevenLabs Reader como lector personal. Descartada David Martin — también peninsular y confident, pero más general-purpose, menos especializada en narrativa larga.
- **Invocación del skill — política dura:** `/audiobook-generate` se invoca **SIEMPRE manualmente**, NUNCA inline dentro de `/ficcion-draft`. Razón de economía: cada iteración de borrador que Rafael edita (voz, cliffhanger, anti-IA, castellano literario) quema ~9.000 chars de API. Dos revisiones = 27k chars tirados porque el audio de v1 no vale cuando publicas v2. El audio se genera **solo sobre texto final aprobado**.
- **Input TTS:** `02-Drafts/Ficciones/<slug>-audiolibro.md` generado automáticamente por `/ficcion-draft` (memoria `feedback_ficcion_audiolibro_copy.md`: prosa TTS-optimizada, números a palabras, sin cursivas, sin siglas duras).

## Decisiones cerradas adicionales 2026-04-22

- **Host del MP3 — Cloudflare R2.** Razón: proyecto personal, R2 es la elección preferida por Rafael por gusto/coherencia con el resto de su stack web. 0 € hasta 10 GB (volumen ROBOHOGAR cabrá durante años: 50 relatos × ~10 MB ≈ 500 MB). URL pública vía `pub-<hash>.r2.dev/<filename>` para FASE 0/1 piloto; subdominio custom `audio.robohogar.com` diferido a FASE 3. Descartado GitHub Releases (URL fea, sin CDN, lock-in a GitHub) y Backblaze (más servicios sin ventaja real para este volumen).

- **Canon editorial para Ficciones Domésticas con audiolibro** (cerrado tras piloto *El que viene a tomar café* 2026-04-22). Arquitectura de 4 capas lógicas, con la capa 3 desdoblada en 2 bloques Beehiiv (email + web) por incompatibilidad de `<script>`/`<audio>` en clientes de email:

  1. **Título (Beehiiv post title):** `🎧 Ficción · <Título del relato>`. El 🎧 al inicio es signal visual instantáneo que se propaga a landing + OG card + email subject. `Ficción ·` mantiene marca de pilar (vs reviews/guías). Middle dot coherente con design system ROBOHOGAR. Cabe en ≤45 chars (límite subject line) para títulos de relato ≤30 chars.
  2. **Subtítulo/dek (Beehiiv subtitle field):** **el gancho narrativo puro, SIN meta-información del formato**. Es lo que aparece en landing preview + OG description + email preview — aquí compite el relato por la atención del lector. Meter "Audiolibro X min" aquí sería malgastar el espacio de enganche. Ejemplo piloto: *"Vallecas, 2032. Una hija cuida a su madre con demencia y cada mañana enciende al humanoide para que sea su padre muerto. Hasta que llega la hermana."*
  3. **Par de bloques Custom HTML consecutivos** (inmediatamente tras el dek), con visibility toggles de Beehiiv por canal:

     - **3a. Bloque email-only** (hide from web). HTML simple con fuentes universales Arial/Helvetica, solo inline styles seguros para Gmail/Outlook/Apple Mail/Yahoo. Contiene: emoji 🎧 + label `Audiolibro disponible · X min` + 2 links (al post web y al MP3 directo). No usa `<script>` ni `<audio>` porque todos los clientes email strippean scripts y renderizan `<audio>` inconsistentemente.

     - **3b. Bloque web-only** (hide from email). El snippet canónico completo con `<audio controls preload="none">` + `<script>` Media Session API para lockscreen móvil. La etiqueta del player (`🎧 Escuchar · X min`) comunica formato al lector que ya está dentro.

  4. **Cuerpo del relato:** H2 `I. La cocina...` empieza la narrativa inmediatamente después de los 2 bloques email/web.

  **Configuración Beehiiv por bloque:**

  | Bloque | Hide from web | Hide from email | Canal visible |
  |---|---|---|---|
  | 3a (texto con links) | ☑ | ☐ | Solo email |
  | 3b (player con `<audio>` + script) | ☐ | ☑ | Solo web |

  **Decisión del par email+web 2026-04-22** (post piloto): primera iteración del canon asumía un único snippet Custom HTML funcionando en los 2 canales. Rafael detectó el riesgo al preguntar por el comportamiento en email. Realidad: `<script>` lo strippean 100% de clientes email por seguridad; `<audio>` HTML5 solo renderiza en Apple Mail, muy inconsistente en Gmail Web/Android/Outlook/Yahoo. Estimación: ~70-80% de aperturas por email no verían el player. Solución: bloque 3a garantiza que el suscriptor de email recibe links accesibles (al post web o descarga MP3 directo) y el bloque 3b conserva la experiencia óptima para lectores web.

  **Decisión de simplificación intra-web 2026-04-22:** versión temprana del canon incluía una 5ª capa con línea "Audiolibro X min disponible al inicio. Léelo o escúchalo." entre el dek y el player. Eliminada tras feedback de Rafael: el widget self-explain (🎧 + "Escuchar" + duración + play button) la hace redundante. Principio UX: si un componente visual comunica algo, la descripción textual duplicada añade ruido sin señal.

  **Razón del orden 1→2 (dek narrativo sin marker de formato):** detectado al pegar el piloto — si meta-información del formato (duración, "audiolibro") va en el dek, roba el espacio de enganche visible en landing/OG a la narrativa. El 🎧 del título ya hace el trabajo de "hay audio" en todos los previews externos.

  **Aplicación en `/audiobook-generate` (FASE 2):** el skill imprime al terminar los 4 strings listos para copy-paste directo en Beehiiv: (a) título con 🎧, (b) dek narrativo del frontmatter, (c) HTML del bloque 3a email-only, (d) HTML del bloque 3b web-only. Rafael solo configura los toggles de visibilidad por bloque tras pegar.

## Decisiones pendientes

- **Nombre final del skill**: propuesta `/audiobook-generate <slug>`.
- **Compatibilidad de `<script>` inline en Custom HTML block de Beehiiv** — Media Session API (ver snippet v2 abajo) requiere JS inline. Si Beehiiv sanea `<script>` → fallback a atributo `onplay` inline. Se valida en FASE 1 piloto.

## Arquitectura técnica propuesta

### Flujo end-to-end

```
1. /ficcion-draft <args>
   ├─ Genera content/ficciones/<slug>/borrador.md (relato editorial)
   └─ Genera 02-Drafts/Ficciones/<slug>-audiolibro.md (prosa TTS-optimizada)

2. Rafael revisa, edita y valida el texto final del relato.
   (NUNCA se genera audio desde un borrador sin validar — quemaría API en cada iteración)

3. /audiobook-generate <slug>   ← INVOCACIÓN MANUAL, explícita, sobre texto cerrado
   ├─ Lee <slug>-audiolibro.md del vault
   ├─ Llama ElevenLabs API → narracion.mp3
   ├─ ffmpeg concat: intro.mp3 + narracion.mp3 + outro.mp3 → <slug>.mp3
   ├─ Sube <slug>.mp3 al host (R2 / GH Releases)
   ├─ Obtiene URL pública
   └─ Inserta snippet HTML con reproductor + botón descarga
      directamente en content/ficciones/<slug>/borrador.html

4. Rafael copia borrador.html a Beehiiv como hace hoy.
   El bloque <audio> va vía /html Custom HTML block.
```

**Regla arquitectónica dura.** `/audiobook-generate` vive como skill **independiente y manual**, nunca encadenado automáticamente desde `/ficcion-draft` ni desde `/post-publish`. Razones:

1. **Economía de API.** El borrador pasa por iteraciones editoriales (voz, cliffhanger, anti-IA, castellano literario, tonal balance). Generar audio en cada iteración tira dinero y consume cuota Starter inútilmente.
2. **Control de calidad del audio.** El MP3 es bien de marca — igual que el hero. Merece su propio check de Rafael antes de quemar los minutos de API, no delegarlo a un trigger automático.
3. **Separación de concerns.** `/ficcion-draft` = texto. `/audiobook-generate` = audio. Encadenarlos acopla fallos (si falla la subida a R2, rompe todo el pipeline de ficción).

### Assets fijos (una sola vez)

- `assets/audio/intro-ficciones.mp3` — intro genérico de marca (5-8s).
  - Texto: *"Ficciones Domésticas, de ROBOHOGAR."* + 2s silencio.
  - O variante con título parametrizable si ElevenLabs permite edición parcial (explorar).
- `assets/audio/outro-ficciones.mp3` — outro genérico de marca (10-15s).
  - Texto: *"Has escuchado una Ficción Doméstica de ROBOHOGAR. Más relatos y newsletter en robohogar.com."*
- `assets/audio/bumper-robohogar.mp3` — 3s sello sonoro para separar episodios de mini-serie.

### Snippet HTML canónico (propuesta v2 — con Media Session API)

Va dentro del `.snippet-block` de `/html` Beehiiv (regla `design.md § Bloques de código para snippets HTML inline en borradores`). Incluye bloque `<script>` que activa Media Session API → en móvil con pantalla bloqueada sale título del relato + portada en los controles de reproducción (iOS Control Center / Android notificación persistente) en vez de la URL cruda `audio.robohogar.com`.

```html
<div class="audio-player-robohogar">
  <p class="audio-label">🎧 Escuchar · <span class="audio-duration">12 min</span></p>
  <audio id="audio-<slug>" controls preload="none" src="https://audio.robohogar.com/<slug>.mp3"></audio>
  <a href="https://audio.robohogar.com/<slug>.mp3" download class="audio-download">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  // Media Session API — muestra título + portada en lockscreen móvil al reproducir.
  // Los navegadores que no soportan la API ignoran el bloque sin romper nada.
  (function() {
    var audio = document.getElementById('audio-<slug>');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: '<TITULO_RELATO>',
        artist: 'ROBOHOGAR · Ficciones Domésticas',
        artwork: [
          { src: 'https://audio.robohogar.com/covers/<slug>-512.webp', sizes: '512x512', type: 'image/webp' },
          { src: 'https://audio.robohogar.com/covers/<slug>-1024.webp', sizes: '1024x1024', type: 'image/webp' }
        ]
      });
    });
  })();
</script>
```

**Placeholders que `/audiobook-generate` sustituye:**
- `<slug>` — slug del relato (ej: `operador-nocturno`).
- `<TITULO_RELATO>` — título visible del relato.
- `audio.robohogar.com/covers/<slug>-{512,1024}.webp` — portadas derivadas del hero del relato (crop cuadrado de `hero-<slug>-1K.webp`), subidas al mismo host al generar el MP3.

**Fallback si Beehiiv sanea `<script>` inline** (a validar en FASE 1 piloto): usar atributo `onplay` en el `<audio>` con la llamada a MediaMetadata serializada. Menos limpio pero no depende de `<script>`. Si ni siquiera eso pasa el saneado, la Media Session API se degrada a controles genéricos del navegador — el audio con pantalla apagada sigue funcionando igual (es comportamiento nativo), solo pierdes la metadata bonita en la lockscreen.

CSS canónico pendiente definir (paleta ámbar `#F5A623`, tipografía DM Sans, mobile-first 375px).

### Script Python — `utilities/generate_audio.py`

Comentado (regla `literate-code.md`), idempotente, batch-ready. Dependencias:
- `elevenlabs` (SDK oficial)
- `boto3` (para R2, S3-compatible) o `PyGithub` (si GH Releases)
- `ffmpeg-python` o llamada a `ffmpeg` vía subprocess

Variables de entorno requeridas en `.claude/settings.local.json`:
- `ELEVENLABS_API_KEY` — API key ElevenLabs Starter plan (permisos Text to Speech + Voices Read).
- `R2_ACCOUNT_ID` — ID de cuenta Cloudflare (se ve en el endpoint URL de R2 o en el dashboard).
- `R2_ACCESS_KEY` — Access Key ID del API token de R2.
- `R2_SECRET_KEY` — Secret Access Key del API token de R2.
- `R2_BUCKET` — nombre del bucket (`robohogar-audio`).
- `R2_PUBLIC_URL` — URL base pública del bucket para servir los MP3 (en FASE 0/1: `https://pub-<hash>.r2.dev`; tras FASE 3: `https://audio.robohogar.com`).

### Skill `/audiobook-generate` (propuesta)

Ubicación: `.claude/commands/audiobook-generate.md`.

Inputs:
- `<slug>` (obligatorio): slug del relato. Ej: `operador-nocturno`.

Outputs:
- `assets/audio/ficciones/<slug>.mp3` (copia local versionada, `-v2`, `-v3` si se regenera — regla `feedback_never_overwrite_images.md`).
- URL pública del MP3 en el host elegido.
- Snippet HTML insertado automáticamente en `content/ficciones/<slug>/borrador.html` en la posición correcta (justo tras el H1 del relato, antes del cuerpo).

Verificación:
- Reproducir el MP3 localmente antes de subir.
- Chequear que la URL es pública y accesible (curl HEAD 200).
- Validar que el snippet quedó pegado en el borrador y renderiza en preview del navegador.

## Fases de activación

### FASE 0 — Prerrequisitos (cuando Rafael dé el OK)

- [ ] **Suscribirse a ElevenLabs Starter plan (yearly billing, $5/mes)** en [elevenlabs.io/pricing](https://elevenlabs.io/pricing).
- [ ] Verificar en el dashboard que aparece "Commercial License: included" y cuota ~60.000 chars Multilingual v2/mes.
- [ ] Generar `ELEVENLABS_API_KEY` en dashboard → API Keys → Create API Key.
- [ ] Guardar `ELEVENLABS_API_KEY` en `.claude/settings.local.json` (gitignored).
- [x] **Voz narrador elegida:** Luis — Polished, Mature and Credible. `voice_id = GojDwihhnL1f7RrBuXsJ`. Cerrada 2026-04-22 (ver sección "Decisiones cerradas").
- [x] **Host elegido: Cloudflare R2** (decisión cerrada 2026-04-22 — preferencia personal de Rafael).
- [x] **Bucket `robohogar-audio` creado en R2** + Public Development URL habilitada (`https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev`) + API token `robohogar-audiobook-uploader` creado con permiso Object Read & Write scoped a ese bucket.
- [x] **5 env vars R2 guardadas en `.claude/settings.local.json`** (desktop) + Chrome Password Manager. Smoke test `utilities/verify_r2_auth.py` 4/4 OK 2026-04-22 (HEAD + PUT + GET público + DELETE).
- [ ] **Gotcha operativo documentado:** el GET público a `*.r2.dev` requiere User-Agent de navegador (Cloudflare rechaza UAs tipo `python-urllib/...` con 403 como protección anti-bot). Sin impacto en producción (el `<audio>` en Beehiiv usa UA del navegador del lector), solo afecta a scripts programáticos que hagan GET directo. `verify_r2_auth.py` envía UA de Chrome para esquivarlo.
- [ ] **Laptop pendiente:** crear `C:\Users\bakal\robohogar\.claude\settings.local.json` con los 6 env vars (ElevenLabs + 5 R2), copiados desde Chrome Password Manager. `pip install boto3` también. Ejecutar `python utilities/verify_r2_auth.py` en laptop para confirmar.
- [x] **`intro-ficciones.mp3` (2.53s) + `outro-ficciones.mp3` (11.89s) generados** en ElevenLabs Studio con voz Luis 2026-04-22. Guardados en `assets/audio/`. Ambos MP3 44.1kHz mono, calidad adecuada para voz. Convención `ROBO OGAR` validada en ambos bumpers.
- [x] **Nota de silencio:** el intro no incluye los 2s de silencio finales que especificaba el plan original. El silencio se inyectará **dinámicamente en la concatenación** de `/audiobook-generate` vía `ffmpeg -af "apad=pad_dur=2"`. Más flexible que bakearlo en el asset — permite ajustar la pausa por relato si hace falta.
- [x] **ffmpeg 8.1 full build instalado** vía `winget install Gyan.FFmpeg` (2026-04-22). Binario en `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_.../ffmpeg-8.1-full_build/bin/ffmpeg.exe`, alias en PATH vía WindowsApps. Incluye `libmp3lame` (codec MP3 necesario para concat intro+narración+outro).
- [ ] **Addendum snippet v2:** documentar en el skill cómo derivar las portadas `covers/<slug>-{512,1024}.webp` desde el hero del relato (crop cuadrado + resize), y cómo subirlas al mismo bucket que el MP3.

### FASE 1 — Piloto manual con un relato

- [ ] Elegir relato ya publicado como piloto (candidatos: `la-casa-de-amparo` · `operador-nocturno-v2` · otro).
- [ ] Generar MP3 manual en ElevenLabs Studio desde `<slug>-audiolibro.md` del vault.
- [ ] Concatenar intro + narración + outro con `ffmpeg` (comando documentado en este plan).
- [ ] Subir al host elegido → obtener URL.
- [ ] Crear snippet HTML a mano con la URL real.
- [ ] Pegar en el post Beehiiv del relato piloto vía `/html`.
- [ ] Validar reproducción en desktop + móvil (375px).
- [ ] Validar botón descarga funciona en Safari/Chrome/Firefox.
- [ ] Rafael decide si el formato convence antes de automatizar.

### FASE 2 — Automatización (si FASE 1 convence)

- [x] **`utilities/generate_audio.py` operativo** (FASE 1 piloto lo creó y validó con *El que viene a tomar café*). Pipeline: chunking por párrafos ≤4500 chars → TTS con voz Luis + `previous_text`/`next_text` → ffmpeg concat (intro + 2s silencio + chunks + outro, recodificación uniforme 44.1kHz mono 128kbps) → upload a R2. Detecta ffmpeg vía PATH o WinGet install location.
- [x] **Skill `.claude/commands/audiobook-generate.md` creado** 2026-04-22 tras piloto. Workflow de 6 pasos: localizar relato → construir/validar `audiolibro.txt` con Rafael → correr `generate_audio.py` → imprimir 4 strings copy-paste para Beehiiv (título 🎧 + dek + bloque HTML email-only + bloque HTML web-only). Incluye pre-requisitos, transformaciones TTS detalladas, y regla dura de invocación manual-only.
- [x] **Entrada en `CLAUDE.md § Skills del pipeline`** (Skills secundarios, junto a `/ficcion-draft`) marcando explícitamente invocación manual sobre texto final aprobado, nunca encadenado.
- [x] **Actualizada `docs/guia-implementacion.md`** con el paso 4 "Audiolibro (opcional)" en el workflow Ficciones Domésticas, entre "Editar" y "Publicar". Incluye frase trigger, los 4 strings que devuelve el skill, regla dura de invocación manual, y estimación de coste por tipo de relato.
- [x] **Coste real documentado en régimen Starter** ($5/mes yearly, ~60k chars Multilingual v2/mes ≈ ~3-4 relatos standalone/mes con regeneraciones). Piloto *El que viene a tomar café* consumió 18.5k chars = ~31% cuota. Umbral upgrade a Creator ($11/mes yearly, 121k credits) si se cruzan 60k chars/mes tres meses seguidos.

### FASE 3 — Mejoras opcionales (post-validación)

- [ ] Subdominio `audio.robohogar.com` en Cloudflare apuntando al bucket R2.
- [ ] Player custom con diseño ROBOHOGAR (superar el look nativo del navegador) — solo si Rafael lo pide.
- [ ] Feed RSS podcast auto-generado desde los relatos con audio → publicable en Spotify/Apple Podcasts como canal "Ficciones Domésticas ROBOHOGAR". Evaluar solo con ≥5 relatos en audio.
- [ ] Transcripción sincronizada (karaoke-style) si alguna vez Rafael quiere un formato premium.

## Coste estimado en régimen

- **ElevenLabs Starter (yearly):** **$5/mes ≈ $60/año** = ~60.000 chars Multilingual v2/mes ≈ ~4 relatos/mes con regeneraciones. Tope suficiente para cadencia ficción actual (1 cada 1-2 semanas condicionada a evergreen-first, regla `editorial.md § Ficciones Domésticas`). Licencia comercial incluida explícita. Verificado 2026-04-22 en el banner del plan.
- **Umbral de upgrade a Creator (yearly $11/mes):** si el consumo mensual cruza los 60k chars tres meses seguidos. Escenario poco probable con el pivote SEO-first que prioriza evergreens sobre ficción.
- **Coste overage pay-as-you-go** (si superas Starter sin haber subido a Creator): $0,10/1.000 chars Multilingual v2.
- **Cloudflare R2:** 0 € realistas (bajo los 10 GB gratis) incluso con 50+ relatos.
- **GitHub Releases:** 0 €.
- **Compute Claude:** despreciable — ~2 min por relato.

Total régimen actual: **~$5/mes = ~$60/año** = coste del plan Starter ElevenLabs. Cero infra extra.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| ElevenLabs cambia pricing | Arquitectura modular: el skill puede apuntar a OpenAI TTS / Google TTS cambiando 1 función |
| Host cae o cambia TOS | MP3 versionados también en `assets/audio/ficciones/` local + repo git → re-subida trivial |
| Voz suena robótica en frases largas | Ya mitigado por `feedback_ficcion_audiolibro_copy.md` (prosa TTS-optimizada) |
| Coste de API escala mal si pilar ficción crece | Cadencia real (editorial-es + SEO-first) ≤4 relatos/mes × ~9k chars × factor regeneración ≈ 36-50k chars/mes → entra en Starter 60k. Upgrade a Creator $11/mes solo si se cruza el umbral tres meses seguidos |
| Rafael no está cómodo con su voz narrando | ElevenLabs tiene catálogo amplio de voces ES premium; no hace falta clonar la suya |

## Referencias cruzadas

- Regla editorial ficción: `.claude/rules/editorial.md § Narrativa especulativa`.
- Skill fuente: `.claude/commands/ficcion-draft.md` (paso que genera audiolibro.md).
- Memoria audiolibro: `.claude/memory/feedback_ficcion_audiolibro_copy.md`.
- Patrón versionado: `.claude/memory/feedback_never_overwrite_images.md`.
- Patrón snippet HTML: `.claude/rules/design.md § Bloques de código para snippets HTML`.
- Guía operativa: `docs/guia-implementacion.md` (actualizar en FASE 2).
