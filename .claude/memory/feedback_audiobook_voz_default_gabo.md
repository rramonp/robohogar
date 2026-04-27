---
name: Voz default audiobooks Gabo + auto-encadenado /audiobook-generate desde /ficcion-draft
description: Canon 2026-04-27 — Gabo (`o0SveC0zgHFuCsEO3vHR`) sustituye a Luis como voz default ElevenLabs para todo audiolibro nuevo de Ficciones. Y `/ficcion-draft` encadena automáticamente `/audiobook-generate` para que el `beehiiv-paste.html` salga con los 8 snippets canónicos (incluidos los MP3 email/web). Cambia la regla anterior "manual only".
type: feedback
---

Dos cambios canon establecidos por Rafael 2026-04-27 PM tras el primer relato `pipo` (que se generó sin audio):

## 1. Voz default Gabo

**Regla:** todo audiolibro nuevo de Ficciones Domésticas se genera con voz **Gabo** (`o0SveC0zgHFuCsEO3vHR` — Gabo - Deep, Evocative and Resonant, My Voices ElevenLabs). Sustituye a Luis (`GojDwihhnL1f7RrBuXsJ`) como voz por defecto.

**Why:** Rafael quiere voz más grave, evocativa y resonante para los relatos de Ficciones Domésticas — el peso moral y la prosa peninsular literaria del catálogo (radical-Cuidados rotos, inquietante-Hogar uncanny, etc.) gana con un tono más profundo que Luis. Decisión tras escuchar la prueba A/B con `pipo` (relato radical-Cuidados rotos). Aplica desde el siguiente relato.

**How to apply:**
- `utilities/generate_audio.py` línea 68: `VOICE_ID = "o0SveC0zgHFuCsEO3vHR"  # Gabo` (ya cambiado).
- `.claude/commands/audiobook-generate.md`: descripción del skill + paso 4 + tabla TTS-friendly mencionan Gabo como default (ya cambiado).
- **Histórico mantenido sin cambios:** `la-objecion`, `el-operador-nocturno`, `el-que-viene-a-tomar-cafe` quedan publicados con voz Luis. No se regeneran salvo que Rafael lo pida explícitamente. La columna "Voz" del registro de ficciones (si se añade) refleja el histórico.
- **Bumpers de marca (intro-ficciones.mp3 + outro-ficciones.mp3)** siguen en voz Luis. No se regeneran al cambiar la voz default — preservan continuidad sonora entre los 3 publicados pre-cambio y los nuevos. Regenerar bumpers solo si Rafael lo pide tras escuchar varios relatos con Gabo.
- **Excepción explícita de relato:** Rafael puede pedir voz distinta para un relato concreto (`/audiobook-generate <slug> --voice luis`) — el script lo soporta via override, pero el default fijo es Gabo.

## 2. Auto-encadenado `/audiobook-generate` desde `/ficcion-draft`

**Regla:** cuando Rafael pide generar el artículo de un relato de Ficciones Domésticas vía `/ficcion-draft` (o lo equivalente conversacional), el flujo se encadena automáticamente con `/audiobook-generate <slug>` ANTES de cerrar el output del relato. El `beehiiv-paste.html` final entregado a Rafael lleva los **8 snippets canónicos** (Meta A/B/C + Snippet 1=audio email + Snippet 2=audio web + Snippet 2.5=Frontispicio + Snippet 3=Lo real + Snippet 4=CTA), no los 6 del estado "sin audio".

**Why:** Rafael publica los relatos en el newsletter Beehiiv y quiere que el lector pueda escuchar el audiolibro desde el email o desde la web sin tener que esperar un segundo paso manual. Cita literal 2026-04-27: *"para el futuro, si pido que me generes el artículo de un relato de ficcion también quiero que me generes el mp3 y lo subas ya que quiero los snippets html para escucharlo desde el newsletter"*. El audio es parte del producto editorial, no add-on opcional.

**Cambia la regla canon previa** ([`feedback_robohogar_audiobook_economia_api.md` y CLAUDE.md § Skills del pipeline]) que decía: *"Invocación SIEMPRE MANUAL sobre texto final aprobado, NUNCA encadenado desde `/ficcion-draft` ni `/post-publish` (economía de API)"*. La economía de API se gestionará por verificación pre-flight de saldo (`utilities/elevenlabs_balance.py`) y por opción explícita de skip si Rafael lo pide (`/ficcion-draft <slug> --no-audio`), no por bloqueo manual default.

**How to apply:**

- `/ficcion-draft` paso final de Output (post `§ 9 Validaciones finales`): tras cerrar el `.md`, generar `audiolibro.txt` aplicando las reglas TTS canon (`§ Copia audiolibro paso 9`), llamar al pipeline `python utilities/generate_audio.py <audiolibro.txt> <slug>`, esperar finalización (mostrar URL R2 + duración tras concat), y luego invocar el paso 6.4 de `/audiobook-generate` que reescribe el `beehiiv-paste.html` a 8 snippets.
- **Pre-flight de saldo obligatorio:** antes de llamar a la API de ElevenLabs, correr `pre_check(audiolibro.txt)` desde `elevenlabs_balance`. Si saldo insuficiente → bloquear con mensaje claro a Rafael ("Saldo ElevenLabs insuficiente: X créditos disponibles, Y necesarios. ¿Esperar a reset día 25 o subir plan?"). Cero invocaciones a ciegas.
- **Opción de override `--no-audio`:** Rafael puede pedir explícitamente *"genérame el relato pero sin audio"* y el flujo cierra con 6 snippets canónicos sin tocar ElevenLabs. Útil cuando hay testing intensivo de prosa o cuando saldo está bajo.
- **Idempotencia:** si el `<slug>.mp3` ya existe en R2 al invocar `/audiobook-generate`, el skill debe ofrecer `regenerar / saltar`. Default = saltar y solo añadir snippets al `beehiiv-paste.html`.
- **Pipeline downstream:** `/audiobook-distribute` sigue siendo MANUAL (auto-fire desde `/post-publish § 13.5` ya existe). El encadenado nuevo solo cubre `/ficcion-draft → /audiobook-generate`, NO llega a YouTube/RSS hasta publicar el post en Beehiiv.

**Coste por relato (Creator plan, ~14.5K chars promedio standalone):** ~11.500 créditos (0.79 chars/créd · ratio observado). Plan Creator = 121.880 créditos/mes → margen para ~10 relatos/mes con audio + reservas para regeneración. Factible con cadencia semanal de 1 relato.

**Aplicación retroactiva al canon de skill:**
- `.claude/commands/ficcion-draft.md` § Output gana paso "Generar audiolibro" antes de "PASOS.md del relato" (pendiente de implementar).
- `.claude/commands/audiobook-generate.md` "Invocación SIEMPRE MANUAL" se sustituye por "Invocación encadenada desde `/ficcion-draft` (default) o manual sobre `<slug>` ya redactado".
- `CLAUDE.md § Skills del pipeline` actualiza la nota "(MANUAL-ONLY)" del audiolibro a "(default desde `/ficcion-draft`, override `--no-audio` disponible)".

**Diferencia clave para sesiones futuras:** si Rafael pide *"hazme un relato de X"*, el output esperado incluye MP3 subido a R2 + `beehiiv-paste.html` con 8 snippets, NO solo el `.md`. El relato sin audio es la excepción (override explícito), no el default.
