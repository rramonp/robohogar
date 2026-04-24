---
name: feedback_beehiiv_email_web_dual_block
description: Widgets interactivos en Beehiiv (audio, video, iframe) requieren 2 bloques — email-safe fallback + web-full — con toggles de visibilidad por canal
type: feedback
originSessionId: 2f235af1-f095-49a6-87fc-2ff5941e833c
---
Al embeber cualquier widget interactivo en un post de Beehiiv (reproductor `<audio>`, `<video>`, iframe, script con Media Session API, etc.) NUNCA usar un solo Custom HTML block compartido entre email y web. Siempre desdoblar en 2 bloques consecutivos con visibility toggles de Beehiiv por canal:

- **Bloque email-only** (hide from web): HTML simple con fuentes universales (Arial/Helvetica), inline styles seguros, sin `<script>` ni elementos multimedia activos. Contenido: label del formato + duración + links al recurso (URL del post web y/o URL del asset directo). Garantiza que el suscriptor de email recibe accesibilidad al contenido en su canal.
- **Bloque web-only** (hide from email): el widget completo con interactividad (`<audio>` + `<script>` + Media Session API / `<video>` / iframe embebido / etc.). Conserva la experiencia óptima para lectores web.

**Why:** clientes de email son hostiles a interactividad:
- `<script>` → 100% strippeado por todos los clientes email (seguridad).
- `<audio>` HTML5 → renderiza solo en Apple Mail, muy inconsistente en Gmail Web/Android/Outlook/Yahoo (estimación ~70-80% de aperturas por email rompen el widget).
- `<iframe>` → bloqueado por casi todos.
- CSS avanzado (flexbox, grid, custom properties) → variable.

Si se pega un solo bloque con el widget completo, la mayoría de suscriptores por email verá un hueco vacío o el contenido roto, perdiendo el acceso al recurso.

**How to apply:**
- Al diseñar cualquier feature que emita HTML embebido al post Beehiiv (audiolibro, video embed, widget interactivo, iframe): **generar 2 snippets desde el origen**.
- Configuración Beehiiv: cada bloque tiene iconos de ojo / menú contextual con toggle "Hide from web" / "Hide from email".
- Los skills que generan copy-paste HTML (`/audiobook-generate` en FASE 2, futuros `/video-embed` o similares) deben imprimir los 2 snippets por defecto, documentando claramente cuál va con qué visibility toggle.

**Origen:** decisión tomada durante FASE 1 piloto audiolibro 2026-04-22 con *El que viene a tomar café*. Rafael preguntó si el reproductor se vería en email; al analizar la realidad de los clientes email la respuesta fue negativa. Solución: par de bloques email+web consecutivos con toggles opuestos, validada end-to-end en el piloto. Canon documentado en `docs/plan-audiolibros-ficciones.md § Canon editorial para Ficciones Domésticas con audiolibro`.
