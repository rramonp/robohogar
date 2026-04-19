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
- **Intro de marca (5-8s):** *"Ficciones Domésticas, de ROBOHOGAR. [Título]. Por [narrador]."* + 2s silencio.
- **Outro de marca (10-15s):** *"Has escuchado [título], una Ficción Doméstica de ROBOHOGAR. Si te ha gustado, puedes leer más relatos y suscribirte al newsletter en robohogar.com."*
- **Mid-roll:** descartado. Rompe inmersión y contradice el posicionamiento premium del pilar ficción. Excepción permitida: bumper de 3s "ROBOHOGAR" entre episodios de mini-serie como sello sonoro.
- **Voz narrador:** única y consistente para todos los relatos (sello sonoro reconocible = tipografía sonora). Voice_id ElevenLabs pendiente elegir.
- **Motor TTS:** ElevenLabs API (ya validado por Rafael como herramienta de uso personal en ElevenLabs Reader).
- **Input TTS:** `02-Drafts/Ficciones/<slug>-audiolibro.md` generado automáticamente por `/ficcion-draft` (memoria `feedback_ficcion_audiolibro_copy.md`: prosa TTS-optimizada, números a palabras, sin cursivas, sin siglas duras).

## Decisiones pendientes

- **Host del MP3** — candidatos ordenados:
  1. **Cloudflare R2** (recomendado): 0€ realistas hasta 10 GB + 0€ egress, pensado para media, CDN global, range requests OK para scrubbing móvil. Setup inicial ~10 min. Permite servir desde `audio.robohogar.com/<slug>.mp3` si `robohogar.com` está en Cloudflare DNS.
  2. **GitHub Releases** (piloto barato): 0€, 2 GB/archivo, tolerado por GitHub para binarios. URLs menos bonitas, sin CDN optimizado. Válido para validar formato antes de invertir en R2.
  3. **Backblaze B2 + Cloudflare**: alternativa clásica a R2, 2 servicios que configurar.
  4. **GitHub Pages**: **descartado**. TOS desaconseja audio/vídeo, range requests poco fiables en móvil → scrubbing falla.
  5. **Beehiiv media library**: **no soporta audio** (verificado 2026), solo imagen.
- **Voice_id ElevenLabs** del narrador.
- **Nombre final del skill**: propuesta `/audiobook-generate <slug>`.

## Arquitectura técnica propuesta

### Flujo end-to-end

```
1. /ficcion-draft <args>
   ├─ Genera content/ficciones/<slug>/borrador.md (relato editorial)
   └─ Genera 02-Drafts/Ficciones/<slug>-audiolibro.md (prosa TTS-optimizada)

2. Rafael revisa y ajusta audiolibro.md si hace falta.

3. /audiobook-generate <slug>
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

### Assets fijos (una sola vez)

- `assets/audio/intro-ficciones.mp3` — intro genérico de marca (5-8s).
  - Texto: *"Ficciones Domésticas, de ROBOHOGAR."* + 2s silencio.
  - O variante con título parametrizable si ElevenLabs permite edición parcial (explorar).
- `assets/audio/outro-ficciones.mp3` — outro genérico de marca (10-15s).
  - Texto: *"Has escuchado una Ficción Doméstica de ROBOHOGAR. Más relatos y newsletter en robohogar.com."*
- `assets/audio/bumper-robohogar.mp3` — 3s sello sonoro para separar episodios de mini-serie.

### Snippet HTML canónico (propuesta v1)

Va dentro del `.snippet-block` de `/html` Beehiiv (regla `design.md § Bloques de código para snippets HTML inline en borradores`):

```html
<div class="audio-player-robohogar">
  <p class="audio-label">🎧 Escuchar · <span class="audio-duration">12 min</span></p>
  <audio controls preload="none" src="https://audio.robohogar.com/<slug>.mp3"></audio>
  <a href="https://audio.robohogar.com/<slug>.mp3" download class="audio-download">
    ⬇ Descargar MP3 (para el coche)
  </a>
</div>
```

CSS canónico pendiente definir (paleta ámbar `#F5A623`, tipografía DM Sans, mobile-first 375px).

### Script Python — `utilities/generate_audio.py`

Comentado (regla `literate-code.md`), idempotente, batch-ready. Dependencias:
- `elevenlabs` (SDK oficial)
- `boto3` (para R2, S3-compatible) o `PyGithub` (si GH Releases)
- `ffmpeg-python` o llamada a `ffmpeg` vía subprocess

Variables de entorno requeridas en `.claude/settings.local.json`:
- `ELEVENLABS_API_KEY`
- Si R2: `R2_ACCOUNT_ID`, `R2_ACCESS_KEY`, `R2_SECRET_KEY`, `R2_BUCKET`
- Si GH Releases: `GITHUB_TOKEN` con scope `contents:write`

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

- [ ] Decidir host (R2 vs GH Releases).
- [ ] Crear cuenta/bucket del host elegido + API token.
- [ ] Elegir `voice_id` ElevenLabs para narrador.
- [ ] Generar `intro-ficciones.mp3` + `outro-ficciones.mp3` con ElevenLabs Studio (manual, una vez).
- [ ] Guardar ambos en `assets/audio/`.
- [ ] Confirmar `ffmpeg` instalado local (`ffmpeg -version`).
- [ ] Guardar `ELEVENLABS_API_KEY` + credenciales host en `.claude/settings.local.json`.

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

- [ ] Escribir `utilities/generate_audio.py` comentado.
- [ ] Escribir skill `.claude/commands/audiobook-generate.md` con pasos, verificación pre-output, y frases trigger.
- [ ] Añadir entrada en `CLAUDE.md § Skills del pipeline` (tabla de skills secundarios, sección junto a `/ficcion-draft`).
- [ ] Integrar llamada opcional desde `/post-publish` o desde `/ficcion-draft` al cerrar relato (decisión: ¿auto o manual?). Por defecto manual para que Rafael valide texto antes de gastar API.
- [ ] Actualizar `docs/guia-implementacion.md` con la nueva fase de producción de audio + frases trigger.
- [ ] Documentar coste mensual estimado ElevenLabs (plan Creator 22$/mes cubre ~10-15 relatos largos).

### FASE 3 — Mejoras opcionales (post-validación)

- [ ] Subdominio `audio.robohogar.com` en Cloudflare apuntando al bucket R2.
- [ ] Player custom con diseño ROBOHOGAR (superar el look nativo del navegador) — solo si Rafael lo pide.
- [ ] Feed RSS podcast auto-generado desde los relatos con audio → publicable en Spotify/Apple Podcasts como canal "Ficciones Domésticas ROBOHOGAR". Evaluar solo con ≥5 relatos en audio.
- [ ] Transcripción sincronizada (karaoke-style) si alguna vez Rafael quiere un formato premium.

## Coste estimado en régimen

- **ElevenLabs Creator:** 22 $/mes = 100.000 chars ≈ 10-15 relatos largos/mes. Tope suficiente para cadencia ficción (1 cada 3-4 semanas, regla `editorial.md § Ficciones Domésticas`).
- **Cloudflare R2:** 0 € realistas (bajo los 10 GB gratis) incluso con 50+ relatos.
- **GitHub Releases:** 0 €.
- **Compute Claude:** despreciable — ~2 min por relato.

Total: **22 $/mes** = coste del plan Creator ElevenLabs. Cero infra extra.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| ElevenLabs cambia pricing | Arquitectura modular: el skill puede apuntar a OpenAI TTS / Google TTS cambiando 1 función |
| Host cae o cambia TOS | MP3 versionados también en `assets/audio/ficciones/` local + repo git → re-subida trivial |
| Voz suena robótica en frases largas | Ya mitigado por `feedback_ficcion_audiolibro_copy.md` (prosa TTS-optimizada) |
| Coste de API escala mal si pilar ficción crece | Cadencia máxima 1 relato/3-4 semanas → tope ~12-18 relatos/año = <30% del cupo Creator |
| Rafael no está cómodo con su voz narrando | ElevenLabs tiene catálogo amplio de voces ES premium; no hace falta clonar la suya |

## Referencias cruzadas

- Regla editorial ficción: `.claude/rules/editorial.md § Narrativa especulativa`.
- Skill fuente: `.claude/commands/ficcion-draft.md` (paso que genera audiolibro.md).
- Memoria audiolibro: `.claude/memory/feedback_ficcion_audiolibro_copy.md`.
- Patrón versionado: `.claude/memory/feedback_never_overwrite_images.md`.
- Patrón snippet HTML: `.claude/rules/design.md § Bloques de código para snippets HTML`.
- Guía operativa: `docs/guia-implementacion.md` (actualizar en FASE 2).
