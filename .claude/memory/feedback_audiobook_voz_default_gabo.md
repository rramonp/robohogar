---
name: Voz audiobooks canon híbrido Luis+Gabo + auto-encadenado /audiobook-generate desde /ficcion-draft
description: Canon 2026-04-28 — híbrido bumpers Luis + cuerpo Gabo. Cuerpo del relato narrado con Gabo (`o0SveC0zgHFuCsEO3vHR`, default desde 2026-04-27); bumpers intro/outro mantienen voz Luis (`GojDwihhnL1f7RrBuXsJ`) para continuidad sonora y separación marca/narrador. Revierte el experimento "100% Gabo" del 2026-04-27 PM tarde. Y `/ficcion-draft` encadena automáticamente `/audiobook-generate` para que el `beehiiv-paste.html` salga con los 8 snippets canónicos (incluidos los MP3 email/web). Cambia la regla anterior "manual only".
type: feedback
---

Dos cambios canon establecidos por Rafael 2026-04-27 PM tras el primer relato `pipo` (que se generó sin audio):

## 1. Voz canon híbrido — bumpers Luis + cuerpo Gabo

**Regla (canon 2026-04-28):** todo audiolibro nuevo de Ficciones Domésticas se genera con voz **Gabo** (`o0SveC0zgHFuCsEO3vHR` — Gabo - Deep, Evocative and Resonant) en el **cuerpo del relato**, y voz **Luis** (`GojDwihhnL1f7RrBuXsJ` — Luis - Polished, Mature and Credible) en los **bumpers intro/outro de marca**. Las dos voces conviven dentro del mismo MP3: el oyente arranca y cierra con Luis (sello sonoro de marca ROBOHOGAR) y escucha la prosa narrativa con Gabo.

**Why:** Rafael quiere voz Gabo (más grave, evocativa, resonante) para la prosa peninsular literaria del catálogo (radical-Cuidados rotos, inquietante-Hogar uncanny, etc.) — el peso moral del cuerpo gana con un tono más profundo. Pero los bumpers funcionan como **sello sonoro de marca**, no como prosa narrativa: la voz Luis (más pulida, profesional, "creíble") encaja mejor con el rol de presentador de marca y mantiene continuidad con los 3 relatos publicados pre-cambio (la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe). El contraste tonal Luis→Gabo→Luis ancla además al lector entre marca y ficción.

Decisión tomada el 2026-04-28 tras un día con bumpers 100% Gabo. Cita literal: *"cambio de opinion para los audiolibros y su distribucion nos quedamos con intro y outro voz de Luis y voz del relato Gabo"*. Aplica desde el siguiente relato.

**How to apply:**
- `utilities/generate_audio.py`: `VOICE_ID = "o0SveC0zgHFuCsEO3vHR"` (Gabo) sigue en el cuerpo del relato (línea 68). Los bumpers son archivos pregrabados — el script no los regenera, los concatena vía ffmpeg desde `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` (que ahora son Luis otra vez).
- `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` = **voz Luis** (canónicos desde 2026-04-28). Duraciones: intro 2.53s · outro 11.89s. Bumpers Gabo del 2026-04-27 versionados como `intro-ficciones-gabo-v1.mp3` y `outro-ficciones-gabo-v1.mp3` (regla never overwrite). Bumpers Luis previos siguen como `intro-ficciones-luis-v1.mp3` y `outro-ficciones-luis-v1.mp3` (idénticos a los canónicos actuales — backup histórico).
- `.claude/commands/audiobook-generate.md`: descripción del skill + paso 4 + pre-requisito mencionan canon híbrido (ya cambiado).
- **Histórico mantenido sin cambios:** los 3 relatos pre-cambio voz cuerpo (la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe) quedan publicados con voz Luis 100%. Pipo (2026-04-27 AM) ya se publicó con Luis bumpers + Gabo cuerpo — coincide exactamente con el canon híbrido restaurado, no requiere reproceso. Ningún audiolibro publicado se regenera retroactivamente.
- **Excepción explícita de relato:** Rafael puede pedir voz distinta del cuerpo para un relato concreto (`/audiobook-generate <slug> --voice luis`) — el script lo soporta via override, pero el default del cuerpo es Gabo y los bumpers son Luis siempre.

### Histórico de la decisión (para sesiones futuras que pregunten qué pasó con "100% Gabo")

1. **2026-04-22:** FASE 0 cierra con voz Luis 100% (bumpers Luis + cuerpo Luis). 3 relatos publicados.
2. **2026-04-27 AM:** prueba A/B en `pipo` con cuerpo Gabo (Luis bumpers + Gabo cuerpo). Rafael valida la voz Gabo para cuerpo.
3. **2026-04-27 PM tarde:** Rafael decide *"100% Gabo desde el siguiente relato"*. Bumpers regenerados a Gabo (script puntual: `utilities/_archive/generate_bumpers_gabo_2026_04_27.py`). Duraciones Gabo: intro 2.83s · outro 8.68s. Coste regeneración: ~107 créditos ElevenLabs.
4. **2026-04-28:** Rafael revierte. Canon final = híbrido bumpers Luis + cuerpo Gabo. Bumpers Luis restaurados como canónicos. Pipo resulta ser el primer y único relato pre-2026-04-28 con la fórmula híbrida ya activa accidentalmente.

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
