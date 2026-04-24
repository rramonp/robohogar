---
name: Digest recommendation must consolidate live backlog, not just fresh week
description: /research-digest debe mostrar en el bloque de recomendación los candidatos vivos del backlog (digests anteriores + evergreens), no solo lo nuevo de la semana — Rafael lee solo el chat post-invocación, no el markdown
type: feedback
originSessionId: 09ae3fbd-ada2-4254-b68d-e95f2f112aa0
---
ROBOHOGAR — `/research-digest` debe producir un bloque de recomendación **autosuficiente** que cubra tanto lo fresco de la semana como el backlog vivo.

**Why:** Rafael trabaja en sesiones espaciadas (3-5 h/semana) y, tras invocar `/research-digest`, se centra en la respuesta del chat y en el bloque "📌 Recomendación ROBOHOGAR" del markdown. No abre digests antiguos ni el calendario completo. Si la recomendación solo muestra lo fresco, pierde de vista temas virales previos aún no publicados o evergreens pendientes. Confirmado 2026-04-20 tras el digest de esa fecha: Rafael preguntó si borrábamos los anteriores y pidió expresamente que "podría elegir entre lo actual o del anterior, con cosas que no hemos duplicado y que no se mencionan en este".

**How to apply:**
- Cada invocación de `/research-digest` (paso 5.5 del skill) debe leer `content/calendario-editorial.md` y extraer: 5 temas del Backlog de temas (no tachados, sin URL publicada) + 3 semillas del Backlog Ficciones (no `published`).
- Cada candidato del backlog arrastrado lleva etiqueta de **vigencia**: 🟢 vigente · 🟡 en ventana (≤6 semanas, perdiendo frescura) · 🔴 anticuado (>6 sem y cubierto masivamente ES → descartar).
- El bloque "📌 Recomendación ROBOHOGAR" tiene **dos pools** explícitos: **Pool A — Lo más fresco de este digest** y **Pool B — Del backlog vivo (digests anteriores)**. Ambos en el markdown y ambos resumidos en el mensaje del chat (máx 10 líneas en total).
- Regla de decaimiento: si un tema del backlog sigue 🟡 tras 2 digests sin publicarse, bajar automáticamente a prioridad Media. Si está 🔴, tachar en el calendario.
- **Nunca borrar digests anteriores**: son histórico. Solo se marca como publicado/obsoleto el tema en el calendario.

Implementado en `.claude/commands/research-digest.md § paso 5.5` y aplicado retroactivamente al digest 2026-04-20.

**Ampliación 2026-04-20 (paso 5.5 bis) — recomendación razonada obligatoria.** Rafael pidió además que el chat cierre SIEMPRE con una recomendación clara (1 artículo + 1 ficción) y el razonamiento en 3-5 líneas, no solo una lista. Criterios de decisión a aplicar en orden: (1) ventana de viralidad 🔥🔥🔥 ⭐⭐⭐ ≤48 h — gana casi siempre porque caduca en 7-10 días; (2) balance temático — leer `content/registro-articulos.md`, penalizar categoría si hay 3+ seguidos; (3) sinergia internal linking con publicados; (4) ventana SEO estacional; (5) alineación con tangibles activos; (6) dupla artículo+ficción con ángulo editorial compartido gana. El razonamiento debe citar datos concretos, no genéricos.
