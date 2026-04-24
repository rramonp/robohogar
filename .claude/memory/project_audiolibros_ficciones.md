---
name: project_audiolibros_ficciones
description: ROBOHOGAR — plan audiolibros Ficciones Domésticas catalogado, decisiones de coste/licencia/arquitectura cerradas 2026-04-22, pendiente activación FASE 0
type: project
originSessionId: 454369cd-5a0b-432e-9fc2-cdbadf13fcaf
---
ROBOHOGAR tiene un plan catalogado (no activo todavía) para añadir reproductor de audio + descarga MP3 a cada relato de Ficciones Domésticas publicado en Beehiiv. Plan completo en `docs/plan-audiolibros-ficciones.md`.

**Decisiones cerradas 2026-04-19:**
- Reproductor HTML5 nativo `<audio controls>` + botón descarga, ambos embebidos in-page en el post Beehiiv vía `/html` Custom HTML.
- Estructura MP3: intro marca (5-8s) + narración + outro marca (10-15s). Sin mid-roll (rompe inmersión premium).
- Voz narrador única para sello sonoro reconocible.
- Input TTS ya existe: `02-Drafts/Ficciones/<slug>-audiolibro.md` del vault, generado auto por `/ficcion-draft` (memoria `feedback_ficcion_audiolibro_copy.md`).

**Decisiones cerradas 2026-04-22** (esta sesión):
- **Plan ElevenLabs:** Starter yearly $5/mes ($60/año) — commercial license explícita en el banner del plan. Descartado pay-as-you-go (ambigüedad sobre commercial license) y Creator $11-22/mes (overkill hasta que haya Professional Voice Clone).
- **Modelo TTS:** Multilingual v2/v3 (obligatorio para ficción literaria ES con matiz emocional). Flash/Turbo descartado (optimizado para chatbots).
- **Voz narrador — política:** voz pre-hecha del marketplace ES de ElevenLabs (gratis en Starter). Upgrade a Instant Voice Clone / Professional Voice Clone diferido a fase posterior con señal de audiencia real. Voice_id concreto se fija en FASE 0 probando 2-3 candidatos.
- **Invocación del skill — dura:** `/audiobook-generate` se invoca SIEMPRE manualmente sobre texto final aprobado. NUNCA se encadena automáticamente desde `/ficcion-draft` ni `/post-publish`. Razón: cada iteración de borrador que Rafael edita (voz, cliffhanger, anti-IA, castellano literario) quemaría ~9k chars de API inútilmente.
- **Media Session API:** el snippet HTML v2 incluye `<script>` con `navigator.mediaSession.metadata` para mostrar título + portada en lockscreen móvil (iOS Control Center / Android notificación) al reproducir. Fallback a atributo `onplay` si Beehiiv sanea `<script>` inline (a validar en FASE 1 piloto).
- **Capacidad Starter:** ~60.000 chars Multilingual v2/mes = ~4 relatos/mes con regeneraciones. Cubre cadencia ficción actual (1 cada 1-2 semanas condicionada a evergreen-first). Umbral upgrade a Creator $11/mes solo si se cruzan 60k chars/mes tres meses seguidos (improbable con pivote SEO-first).
- **Persistencia de snippets Beehiiv (regla dura 2026-04-22 tarde):** `/audiobook-generate` escribe SIEMPRE `content/ficciones/**/<slug>/beehiiv-audiolibro-snippets.md` como paso 6 obligatorio del pipeline, con URL R2, duración, tamaño, bitrate, coste real, los 4 strings (título 🎧 + subtítulo + HTML email-only + HTML web-only) con substituciones aplicadas, y las instrucciones de pegado. El chat muestra además los strings para copy-paste inmediato, pero la fuente de verdad persistente es el `.md` del repo. Razón: Rafael trabaja en sesiones espaciadas (3-5 h/semana); si cierra la conversación y vuelve días después a publicar, tiene que poder encontrar todo sin pedir regeneración. Incidente origen: 2026-04-22 `papa-desde-singapur` — el skill en v1 solo mostraba los strings en chat, Rafael tuvo que pedir que se persistieran.

**Pendientes de decisión antes de arrancar FASE 0:** host del MP3 (candidatos ordenados: Cloudflare R2 > GitHub Releases > Backblaze B2; descartados GitHub Pages y Beehiiv media library) y voice_id concreto del marketplace ES.

**Why:** Rafael quiere diferenciación premium para el pilar ficción (~10% del content mix) sin romper el pipeline actual. Starter $5/mes da commercial license explícita (vs ambigüedad pay-as-you-go) y cubre holgado el volumen real. Arquitectura manual-only protege presupuesto API y separa concerns (texto vs audio).

**How to apply:** cuando Rafael diga "Retomamos plan audiolibros — empezamos piloto manual con <slug>" o "Retomamos plan audiolibros — monta /audiobook-generate", leer `docs/plan-audiolibros-ficciones.md`, revisar checkboxes de cada fase y retomar en el primer paso pendiente. NO proponer encadenar `/audiobook-generate` desde `/ficcion-draft` ni desde `/post-publish` — es decisión cerrada por economía de API. NO proponer pay-as-you-go como alternativa a Starter — descartada por tema commercial license. No arrancar FASE 0 sin trigger explícito de Rafael.
