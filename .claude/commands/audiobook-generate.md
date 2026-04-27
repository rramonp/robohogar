# Audiobook Generate — generador de audiolibros para Ficciones Domésticas

Genera el audiolibro MP3 de un relato de Ficciones Domésticas: lee el texto, construye la versión TTS-optimizada, llama a la API de ElevenLabs con **voz Gabo** (default desde 2026-04-27, sustituye Luis), concatena con intro/outro de marca, sube a Cloudflare R2 y devuelve los 4 strings listos para copy-paste en Beehiiv.

**INVOCACIÓN SIEMPRE MANUAL.** NUNCA se encadena automáticamente desde `/ficcion-draft` ni `/post-publish`. El audio se genera solo sobre texto final aprobado para no quemar cuota API en iteraciones editoriales. Regla dura del plan.

## When to activate

Solo cuando Rafael lo pida explícitamente:

- `/audiobook-generate <slug>`
- "genera el audiolibro de `<slug>`"
- "hazme el MP3 de `<slug>`"
- "retomamos plan audiolibros — piloto con `<slug>`"
- "necesito el audio del relato `<slug>`"

**NO activar por**: publicar un relato (`/post-publish`), terminar un borrador (`/ficcion-draft`), etc. Espera invocación literal.

## Sintaxis

```
/audiobook-generate <slug>
```

- **slug:** nombre del directorio del relato dentro de `content/ficciones/` (puede estar en `_one-shots/<slug>/`, `la-casa-de-amparo/<capitulo>/`, `cronicas-ronda-3/<capitulo>/`, etc.).

## Pre-requisitos

Antes de invocar, Claude debe verificar:

- [ ] `.claude/settings.local.json` tiene las 6 env vars (`ELEVENLABS_API_KEY`, `R2_ACCOUNT_ID`, `R2_ACCESS_KEY`, `R2_SECRET_KEY`, `R2_BUCKET`, `R2_PUBLIC_URL`). Si faltan → ejecutar `python utilities/verify_elevenlabs_auth.py` + `python utilities/verify_r2_auth.py` para diagnosticar.
- [ ] `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` existen (bumpers de marca generados una vez en FASE 0 con voz Luis — no se regeneran al cambiar la voz default a Gabo: el cambio canon de voz aplica a la narración del relato; intro/outro mantienen continuidad sonora con los 3 publicados pre-2026-04-27 y se regenerarán sólo si Rafael lo pide explícitamente).
- [ ] `ffmpeg` accesible vía PATH o WinGet install location. El script `utilities/generate_audio.py` ya detecta ambos.
- [ ] `boto3` instalado (`pip install boto3`).
- [ ] **Cuota ElevenLabs suficiente para el relato** — verificación automática vía contador local [`utilities/elevenlabs_balance.py`](../../utilities/elevenlabs_balance.py). El módulo sincroniza saldo desde el endpoint `/v1/usage/character-stats` (que SÍ funciona con la API key estándar de ROBOHOGAR; el endpoint `/v1/user/subscription` requiere permiso `user_read` que la key no tiene → bloqueado HTTP 401). Verificación:

  ```bash
  # Sincroniza saldo desde la API ElevenLabs (idempotente, lectura pura).
  # Plan + límite + reset day vienen del dashboard ElevenLabs (Subscription page).
  python utilities/elevenlabs_balance.py sync \
      --tier Creator --limit 121880 --reset-day 25 --ratio 0.79

  # Pre-check de margen para los chars del relato.
  python utilities/elevenlabs_balance.py check --chars <chars_del_audiolibro_txt>
  ```

  Salida esperada del `check` con saldo OK: línea verde `✅ Saldo OK. X créditos antes → Y después...`. Si sale `❌ Saldo insuficiente`, abortar antes de TTS — los chunks parciales no son recuperables si la cuota se agota mid-pipeline (incidente origen 2026-04-25 con `la-objecion`: la regeneración falló en el chunk 1 con HTTP 401 quota_exceeded, forzando upgrade de plan a mitad de la sesión).

  **El hook ya está integrado en `generate_audio.py`** — el script llama `pre_check()` antes del primer TTS y aborta si saldo insuficiente, y llama `record_usage()` solo si TTS+concat+upload pasaron. La invocación `python utilities/generate_audio.py …` no requiere acción extra para el contador.

  **Override `ROBOHOGAR_ELEVENLABS_FORCE=1`** salta el bloqueo si Rafael acaba de pagar overage y el contador local aún no lo refleja.

  **Si el contador no está configurado** (estado vacío al iniciar el repo en una máquina nueva), el primer `sync` lo inicializa. Datos a meter — visibles en https://elevenlabs.io/app/subscription:
  - `--tier`: Starter / Creator / Pro / Scale / Business.
  - `--limit`: créditos/mes del plan (Creator base = 100.000, pero la cuenta de Rafael tiene 121.880 por extras — verificar en dashboard "X / Y credits").
  - `--reset-day`: día del mes en que renueva (formato dashboard: "Renews on May 25" → `--reset-day 25`).

  **Opciones si la cuota no llega** (saldo < chars × ratio):
  - Esperar al reset mensual (visible en `status` con campo "Día reset mensual").
  - Pagar overage (~$0,20 / 1k chars) en el dashboard y re-ejecutar `sync` para refrescar.
  - Upgrade de plan (Creator → Pro multiplica cuota ×5).

Si falta algo → reportar al usuario y detener antes de empezar.

## Workflow

### 1. Localizar el relato y decidir si existe `audiolibro.txt`

```bash
find content/ficciones -name "<slug>" -type d
```

El directorio debería contener el `.md` del relato (típicamente `YYYY-MM-DD-<slug>.md`), `borrador.html`, assets, y posiblemente ya un `audiolibro.txt`.

- **Si `<slug>/audiolibro.txt` existe:** saltar al paso 4.
- **Si no existe:** construirlo en pasos 2-3.

### 2. Construir el texto TTS-optimizado

Fuente preferida por orden:
1. **URL publicada del post** (si Rafael la da o está en `content/registro-articulos.md`). Usar WebFetch con prompt específico para extraer solo la prosa narrativa + "Lo real detrás del relato" si existe. Esta es la versión canónica que lee el lector.
2. **Markdown del relato local** (`<slug>/<fecha>-<slug>.md`). Parsear el frontmatter y el cuerpo, ignorando bloques editoriales (`> **Mentira grande:**`, `> **Muro izquierdo:**`), HTML comments y separators `---`.

**Convención de headings de capítulo (importante para chunks-index downstream):** dos formatos válidos, equivalentes:
- **Canónica corta:** `Uno. La cocina.` · `Dos. Hernán.` · ... · `Doce. El final.` (ordinal en Title-case + punto + espacio + título + punto final)
- **Larga:** `Parte uno. La cocina.` · `Parte dos. Hernán.` · ... · `Parte doce. El final.` (prefijo `Parte` case-insensitive)

Cualquiera de las dos se detecta por el regex de `utilities/generate_audio.py § CHAPTER_HEADING_RE`. Mezclar ambas en un mismo relato funciona pero es feo — escoger una y mantenerla. Para relatos que NO tienen capítulos (flash <800 palabras), no hace falta heading: el script genera 1 chapter sintético "Relato" automáticamente.

Aplicar las siguientes transformaciones:

| Qué | De | A |
|---|---|---|
| Romanos de sección | `## I. Título`, `## II.`, `## III.` | `Uno. Título.`, `Dos. Título.`, `Tres. Título.` (como líneas aparte, con punto final) |
| Markdown italics | `*palabra*` | `palabra` (sin asteriscos — al TTS le salen artefactos con ellos) |
| Markdown bold | `**palabra**` | `palabra` (mismo motivo) |
| Middle dots en texto de app/UI | `Ramón García Torres · esposo · fallecido 2027` | `Ramón García Torres, esposo, fallecido dos mil veintisiete` (comas + años a palabras) |
| Modelos ficticios con guión | `HOGAR-X5` | `HOGAR equis cinco` (el guión confunde, la separación forzada evita que el TTS diga "menos" o "guión") |
| Marca ROBOHOGAR (si aparece literal) | `ROBOHOGAR`, `ROBO OGAR`, `ROBO  OGAR`, `ROBO,OGAR` | **`ROBO, OGAR`** (coma + espacio — refuerzo canónico 2026-04-25). La coma fuerza pausa prosódica de ~150-300 ms en Multilingual v2 que el espacio simple **no garantiza**: en ciertos contextos el motor empalmaba "ROBO" con "OGAR" creando una H aspirada parásita estilo inglés ("RoboJOgar"). El símbolo escrito de marca sigue siendo ROBOHOGAR sin coma — la coma vive solo en `audiolibro.txt` y assets TTS, nunca en HTML/banners/metadata visible al lector. Detalle: `feedback_robohogar_tts_pronunciation.md` + `docs/plan-audiolibros-ficciones.md § Decisiones cerradas`. **Safety-net automático:** `utilities/generate_audio.py` aplica esta sustitución idempotente sobre el texto antes del TTS aunque se cuele alguna variante no canónica. |
| Años en italic o prose corta | `2027`, `2024/1689` | `dos mil veintisiete`, eliminar parentéticos con slash (reescribir si son técnicos) |
| Porcentajes | `80%`, `85%` | `ochenta por ciento`, `ochenta y cinco por ciento` |
| Cifras grandes redondas | `900.000 personas` | `novecientas mil personas` |
| Acrónimos expandibles | `SEN` | `la Sociedad Española de Neurología` (primera mención; segunda puede ir abreviada si aparece) |
| Rangos de años técnicos | `(2015-2018)` | `de dos mil quince a dos mil dieciocho` |
| Regulaciones con número | `AI Act (Reglamento UE 2024/1689)` | `el reglamento europeo de inteligencia artificial` (reformular) |
| Separators `---` | `---` | (eliminar — se pierden en TTS) |
| HTML comments | `<!-- ... -->` | (eliminar) |
| Títulos con hash | `# El que viene a tomar café` | `El que viene a tomar café.` (sin hash, con punto final) |

**Lo que NO se toca** (Gabo / Luis los manejan bien):
- Em-dashes `—` (pausas narrativas ES)
- Nombres propios (Pilar, Almudena, Vallecas, Bilbao, Atleti, etc.)
- Acrónimos-palabra cortos (SAMUR, AVE, IMSERSO)
- Ellipses `…`
- Diálogos con `—Frase —dice.`
- Signos de interrogación / exclamación invertidos

Guardar el resultado en `content/ficciones/**/<slug>/audiolibro.txt`.

### 3. Validación del texto con Rafael (STOP obligatorio pre-API)

Presentar a Rafael:
- Ruta del archivo creado
- Stats: `wc -c` chars, aproximación de palabras, duración estimada (~150 palabras/min para narración ES), coste estimado en overage ($0.10/1k chars), % de cuota mensual Starter (60k chars).
- Transformaciones clave aplicadas (tabla resumen).

**Verificación pre-output OBLIGATORIA — pronunciación canónica de marca:**

```bash
# (a) ROBOHOGAR sin separar — debe ser 0
grep -cE '\bROBOHOGAR\b' content/ficciones/**/<slug>/audiolibro.txt

# (b) ROBO OGAR sin coma (convención antigua) — debe ser 0 tras refuerzo 2026-04-25
grep -cE '\bROBO +OGAR\b' content/ficciones/**/<slug>/audiolibro.txt

# (c) ROBO, OGAR canónica — debe ser ≥1 si la marca aparece en el texto
grep -cE '\bROBO, OGAR\b' content/ficciones/**/<slug>/audiolibro.txt
```

Si (a) o (b) devuelven >0 → editar `audiolibro.txt` sustituyendo a `ROBO, OGAR` antes de continuar. El script `utilities/generate_audio.py` aplica un safety-net automático que normaliza estas variantes en runtime (idempotente), pero la fuente local debe quedar limpia para que las regeneraciones futuras y el control de versiones reflejen la convención canónica.

Razón: regla del plan audiolibros § Decisiones cerradas + memoria `feedback_robohogar_tts_pronunciation.md`.

Preguntar: *"¿Procedo a generar el MP3 o quieres tocar algo primero?"*

**NO invocar el script TTS hasta que Rafael dé OK explícito.** Si pide cambios, editar el `audiolibro.txt` y volver a presentar stats.

### 4. Generar el audio

```bash
python utilities/generate_audio.py content/ficciones/**/<slug>/audiolibro.txt <slug>
```

El script (ver [`utilities/generate_audio.py`](../../utilities/generate_audio.py)) hace:
- Chunking por párrafos ≤4500 chars (límite Multilingual v2).
- TTS por chunk con voz **Gabo** (`o0SveC0zgHFuCsEO3vHR`, default desde 2026-04-27 — sustituye Luis `GojDwihhnL1f7RrBuXsJ` que se mantiene como histórico de los 3 publicados pre-cambio), modelo `eleven_multilingual_v2`, formato `mp3_44100_128`, con `previous_text`/`next_text` para prosodia coherente entre chunks.
- Concatenación ffmpeg: intro (2.53s) + 2s silencio + chunks narración + 3s silencio + outro (11.89s), recodificando todo a 44.1kHz mono 128kbps. El silencio de 3s antes del outro (decisión 2026-04-25) da respiro narrativo entre el FIN del relato y la CTA final de marca.
- Upload a R2 bucket `robohogar-audio` con ContentType `audio/mpeg`, key = `<slug>.mp3`.
- Versionado local (`_chunks-<slug>/` persistente para debug o regeneración parcial).

Output del script: URL pública del MP3 + duración final + path local.

### 5. Construir los 4 strings para copy-paste en Beehiiv

Con la URL pública y la duración ya conocidas, generar los siguientes 4 strings listos para que Rafael los pegue (canon del plan `§ Canon editorial para Ficciones Domésticas con audiolibro`):

**(a) Título del post Beehiiv:**

```
🎧 Ficción · <Título del relato>
```

Tomar el `<Título del relato>` del frontmatter (`title` o `seo_title`) del `.md` fuente. Si la suma supera 45 chars, avisar a Rafael (truncará en email subject line).

**(b) Subtítulo / dek del post Beehiiv:**

Tomar literal del `meta_description` del frontmatter del relato. Si no existe, sugerir uno con la regla: gancho narrativo puro, sin meta-información del formato.

**(c) Bloque Custom HTML email-only** (hide from web en Beehiiv):

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · <DURACION> min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/<slug>" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="<URL_R2_MP3>" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
  </p>
</div>
```

Substituir: `<DURACION>` (minutos redondeado del MP3), `<slug>`, `<URL_R2_MP3>` (URL pública R2 devuelta por el script).

**(d) Bloque Custom HTML web-only** (hide from email en Beehiiv):

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;">
    🎧 Escuchar · <span style="color: #6B7280; font-weight: 400;"><DURACION> min</span>
  </p>
  <audio id="audio-<slug>" controls preload="none" style="width: 100%; height: 44px;" src="<URL_R2_MP3>"></audio>
  <a href="<URL_R2_MP3>" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-<slug>');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: '<Título del relato>',
        artist: 'ROBOHOGAR · Ficciones Domésticas',
        artwork: []
      });
    });
  })();
</script>
```

Substituir: `<slug>` (3 veces), `<URL_R2_MP3>` (2 veces), `<DURACION>`, `<Título del relato>` (en el metadata).

### 6. Persistir los 4 strings + metadata en el repo (OBLIGATORIO)

Los 4 strings y la metadata del MP3 **deben quedar guardados en un archivo del repo** junto al relato, para que Rafael los recupere en sesiones futuras sin depender del chat. Rafael trabaja en sesiones espaciadas (3-5 h/semana): si cierra la conversación y vuelve 3 días después a publicar, tiene que poder encontrar todo sin pedir regeneración.

Escribir `content/ficciones/**/<slug>/beehiiv-audiolibro-snippets.md` con esta estructura exacta:

```markdown
# Beehiiv · snippets audiolibro · <Título del relato>

**Generado:** YYYY-MM-DD por `/audiobook-generate <slug>`.
**Relato fuente:** [`<fecha>-<slug>.md`](<fecha>-<slug>.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/<slug>.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | <URL_R2_MP3> |
| **Duración** | <X,Y> min (<Zs>s) |
| **Tamaño** | <N,N> MB (<bytes> bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | <N> · <chars> chars · coste real $<X,YY> (~<Z> % cuota Starter) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK |

---

## (a) Título del post Beehiiv

\`\`\`
🎧 Ficción · <Título del relato>
\`\`\`

*<N> chars — <comentario sobre subject line>.*

---

## (b) Subtítulo / dek

\`\`\`
<meta_description del frontmatter>
\`\`\`

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

\`\`\`html
<bloque HTML (c) con substituciones aplicadas>
\`\`\`

---

## (d) Custom HTML block · web-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from email**.

\`\`\`html
<bloque HTML (d) con substituciones aplicadas>
\`\`\`

---

## Orden de pegado en Beehiiv

1. **(a)** como título del post.
2. **(b)** como subtítulo.
3. **(c)** primer Custom HTML block inmediatamente después del subtítulo → engranaje → **hide from web**.
4. **(d)** segundo Custom HTML block inmediatamente después → engranaje → **hide from email**.
5. El cuerpo del relato (`Uno. / Dos. / …`) va **después** de ambos bloques HTML.
6. Publica con **Email and web**.
7. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

## Regeneración parcial

Si algún chunk suena mal (transición rara, nombre pronunciado torcido):

- Chunks persistidos en `assets/audio/ficciones/_chunks-<slug>/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings` (stability / similarity_boost)
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `<slug>.mp3`)

Ahorra cuota API vs regenerar los N chunks completos.
```

**Regla dura:** este archivo se escribe SIEMPRE al final del pipeline, sin preguntar. Es idempotente (se sobrescribe si se regenera el audiolibro). El chat muestra además los 4 strings para comodidad inmediata, pero la **fuente de verdad persistente es el `.md` del repo** — nunca solo el chat.

### 6.4. Actualizar `beehiiv-paste.html` con los 4 snippets como bloques de código (OBLIGATORIO)

**Regla dura 2026-04-26 (refuerzo Rafael):** todos los snippets que se pegan en Beehiiv vía `/html` → "Custom HTML block" — audiolibro email-only, audiolibro web-only, "Lo real detrás del relato", CTA suscripción ficción — viven en el `beehiiv-paste.html` como **bloques de código copy-paste** (`.snippet-block`), NO como `<div>` renderizados. Razón: Rafael publica haciendo copy-paste desde el archivo al editor Beehiiv. Los Custom HTML blocks requieren el HTML como **texto copiable**, no como elemento ya renderizado. Si los snippets viven como `<div>` inline en el archivo, al copiar desde navegador se copia el texto visible, no el código source.

Esta regla es la aplicación a Ficciones del patrón canónico ya canonizado en [`@rules/design.md § Bloques de código para snippets HTML inline en borradores`](../../.claude/rules/design.md). Aplica a TODO `beehiiv-paste.html` de Ficciones (con o sin audiolibro).

**Estructura obligatoria del `beehiiv-paste.html`** tras `/audiobook-generate` — **8 `.snippet-block`** (3 meta + 5 /html: audio email + audio web + frontispicio + Lo real + CTA) más el cuerpo del relato. **Snippet 2.5 (Frontispicio · título corto)** canonizado 2026-04-27 — funciona como página título interior del libro impreso (patrón Anagrama / Penguin Modern Classics): tras los snippets utilitarios de audio, el lector entra al cuerpo del relato encontrando el **título corto del relato** (`title:` del frontmatter, no `display_title:`) en grande sobre fondo blanco con eyebrow ámbar `Ficciones Domésticas`. Funciona como sello editorial de la pieza, anclando su identidad como obra mientras el `display_title` largo (en el H1 visible del post) hace de hook vendor:

```
<!DOCTYPE html><html><head><style>.snippet-block { ... }</style></head><body>

<!-- INSTRUCCIONES (orden de pegado en Beehiiv) -->

<div class="snippet-block">  <!-- Meta A: Title del post -->
  <p class="snippet-header">📝 Meta A · Title · campo "Title" del editor</p>
  <p class="snippet-hint">No es /html — es el campo de título del post. Pegar tal cual.</p>
  <pre><code>🎧 Ficción · &lt;Título del relato&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Meta B: Subtítulo / dek -->
  <p class="snippet-header">📝 Meta B · Subtítulo · campo "Subtitle" + "Meta description" SEO</p>
  <p class="snippet-hint">No es /html — es el subtítulo / dek del post. Pegar también como meta_description en el SEO panel.</p>
  <pre><code>&lt;meta_description del frontmatter del .md&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Meta C: URL slug -->
  <p class="snippet-header">📝 Meta C · URL slug · campo "URL slug" del editor</p>
  <p class="snippet-hint">No es /html — es el slug del post. Pegar en el campo "URL slug" (panel SEO/Settings). URL pública resultante: https://robohogar.com/p/&lt;slug&gt;.</p>
  <pre><code>&lt;slug&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Snippet 1: audiolibro email-only -->
  <p class="snippet-header">📋 Snippet 1 · Audiolibro email-only · hide from web</p>
  <p class="snippet-hint">/html → Custom HTML block → engranaje → Hide from web.</p>
  <pre><code>&lt;div...&gt;...&lt;/div&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Snippet 2: audiolibro web-only -->
  <p class="snippet-header">📋 Snippet 2 · Audiolibro web-only · hide from email</p>
  <p class="snippet-hint">/html → Custom HTML block → engranaje → Hide from email.</p>
  <pre><code>&lt;div...&gt;...&lt;/div&gt;&lt;script&gt;...&lt;/script&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Snippet 2.5: frontispicio título corto -->
  <p class="snippet-header">📋 Snippet 2.5 · Frontispicio · título corto entre audio y cuerpo</p>
  <p class="snippet-hint">/html → Custom HTML block → pega el código. Va después de Snippet 2 y antes del primer H2 del cuerpo. Lleva el `title:` corto del frontmatter, NO el `display_title:` largo.</p>
  <pre><code>&lt;div style=&quot;margin: 56px 0 40px; padding: 0; text-align: center; font-family: &#x27;DM Sans&#x27;, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;&quot;&gt;
  &lt;div style=&quot;color: #F5A623; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;&quot;&gt;Ficciones Domésticas&lt;/div&gt;
  &lt;div style=&quot;font-family: &#x27;DM Sans&#x27;, sans-serif; font-size: 32px; font-weight: 700; color: #0C0C0C; line-height: 1.15; margin: 0; letter-spacing: -0.3px;&quot;&gt;&lt;TÍTULO CORTO&gt;&lt;/div&gt;
  &lt;div style=&quot;display: inline-block; width: 36px; height: 2px; background: #F5A623; margin: 18px auto 0;&quot;&gt;&lt;/div&gt;
&lt;/div&gt;</code></pre>
</div>

<!-- CUERPO DEL RELATO (texto editor normal en Beehiiv, NO snippet-block) -->
<h2 style="text-align:center;">I. ...</h2>
<p>...</p>
<h2 style="text-align:center;">II. ...</h2>
<p>...</p>
...
<p style="text-align:center;font-style:italic;color:#6B7280;margin-top:32px;">Fin.</p>

<div class="snippet-block">  <!-- Snippet 3: Lo real detrás del relato -->
  <p class="snippet-header">📋 Snippet 3 · Lo real detrás del relato · tras "Fin."</p>
  <p class="snippet-hint">/html → Custom HTML block → pega el código.</p>
  <pre><code>&lt;div...&gt;...&lt;/div&gt;</code></pre>
</div>

<div class="snippet-block">  <!-- Snippet 4: CTA suscripción ficción -->
  <p class="snippet-header">📋 Snippet 4 · CTA suscripción ficción · final del post</p>
  <p class="snippet-hint">/html → Custom HTML block → pega el código.</p>
  <pre><code>&lt;div...&gt;...&lt;/div&gt;</code></pre>
</div>

</body></html>
```

**Reglas Meta A / Meta B / Meta C:**
- **Meta A · Title:** prefijo fijo `🎧 Ficción · ` + título del relato (del frontmatter `title`). Sin escapado HTML — es texto plano.
- **Meta B · Subtítulo:** literal del frontmatter `meta_description` del relato. Sin escapado HTML — es texto plano. Reutilizable como `Meta description` del SEO panel del editor (mismo string).
- **Meta C · URL slug:** literal del frontmatter `slug` del relato. Sin escapado HTML — es texto plano (kebab-case). La URL pública resultante en Beehiiv será `https://robohogar.com/p/<slug>`.

**CSS canónico** del `<style>` (copiar tal cual al `<head>` del `beehiiv-paste.html` — no viaja a Beehiiv, es solo para preview en navegador local):

```css
.snippet-block { background: #F0F0F0; border: 2px dashed #535252; border-radius: 8px; padding: 16px 18px; margin: 32px 0; }
.snippet-block .snippet-header { font-family: 'DM Sans', sans-serif; font-weight: 700; font-size: 14px; color: #283642; margin: 0 0 6px; letter-spacing: 0.5px; text-transform: uppercase; }
.snippet-block .snippet-hint { font-style: italic; font-size: 13px; color: #6B7280; margin: 0 0 12px; }
.snippet-block pre { background: #FFFFFF; border: 1px solid #C0C0C0; border-radius: 4px; padding: 12px 14px; margin: 0; overflow-x: auto; }
.snippet-block code { font-family: 'Courier New', Consolas, Monaco, monospace; font-size: 12px; color: #0C0C0C; white-space: pre-wrap; word-break: break-word; }
```

**Reglas de escapado dentro de `<pre><code>`:**
- `<` → `&lt;`
- `>` → `&gt;`
- `&` → `&amp;` (cuidado con entidades preexistentes como `&mdash;` que se vuelven `&amp;mdash;` y se renderizan como `&mdash;` en Beehiiv tras copy-paste — esto es el comportamiento deseado)
- Comillas dobles dentro de atributos HTML quedan tal cual.

**Verificación pre-output (grep, debe pasar todo):**

```bash
FILE="content/ficciones/**/<slug>/beehiiv-paste.html"

# (a) Ocho .snippet-block (3 Meta A/B/C + 5 /html: audiolibro x2 + frontispicio + Lo real + CTA)
grep -c 'class="snippet-block"' "$FILE"  # esperado: 8

# (a2) Meta A, Meta B y Meta C presentes
grep -cE '📝 Meta [ABC]' "$FILE"  # esperado: 3

# (a3) Snippets 1, 2, 2.5, 3, 4 presentes
grep -cE '📋 Snippet (1|2|2\.5|3|4)' "$FILE"  # esperado: 5

# (a4) Frontispicio con eyebrow Ficciones Domésticas
grep -c 'Ficciones Dom&eacute;sticas\|Ficciones Domésticas' "$FILE"  # esperado: ≥1

# (b) HTML escapado dentro de los <pre><code> de los 4 snippets /html
grep -c '&lt;\|&gt;' "$FILE"  # esperado: >0 (típico ~25-40 según relato)

# (c) Capítulos del cuerpo (h2)
grep -cE '<h2[^>]*>I+[\.I]' "$FILE"  # esperado: número de escenas del relato

# (d) Fin. cierra el cuerpo
grep -c '>Fin\.<' "$FILE"  # esperado: 1

# (e) NO hay <div style="margin:32px 0;padding:24px 28px;background:#FFF9EF"> renderizado
#     (eso es el bloque "Lo real" que DEBE estar dentro de <pre><code>, no inline)
grep -c '<div style="margin:32px 0;padding:24px 28px;background:#FFF9EF' "$FILE"  # esperado: 0

# (f) NO hay reproductor de audio renderizado inline (debe estar dentro de Snippet 2)
grep -cE '<audio id="audio-' "$FILE"  # esperado: 0
```

Si (a) ≠ 7 o (e) > 0 o (f) > 0 → reescribir el `beehiiv-paste.html` antes de entregar a Rafael.

**Aplicación retroactiva:** los `beehiiv-paste.html` previos al refuerzo 2026-04-26 (la-objecion publicada con `<div>` inline, el-pendiente borrador) NO se actualizan retroactivamente salvo petición explícita — la versión publicada en Beehiiv ya está correcta y el archivo del repo es histórico de cómo se pegó. Aplica solo a relatos nuevos desde 2026-04-26 (`el-operador-nocturno` en adelante).

**Ficciones SIN audiolibro:** el `beehiiv-paste.html` lleva 6 `.snippet-block` (Meta A + Meta B + Meta C + Snippet 1 = Frontispicio título corto + Snippet 2 = "Lo real detrás del relato" + Snippet 3 = CTA suscripción ficción), sin los dos del audiolibro. La estructura general se mantiene; el Frontispicio sigue siendo Snippet 1 antes del cuerpo del relato.

### 6.5. chunks-index.json — automático, no requiere acción

`utilities/generate_audio.py` genera automáticamente `assets/audio/ficciones/<slug>-chunks-index.json` al final del run. Lo consume `/audiobook-distribute` (FASE 3) para componer:

- **Chyrons del MP4 YouTube** — un drawtext por capítulo con fade in/out al cruzar `start_seconds` (opción D++ híbrido del plan).
- **Chapters timestamped en la descripción YouTube** — formato `MM:SS Capítulo I — Título` que YouTube auto-renderiza como navegación interna del vídeo.
- **Show notes RSS** (opcional, futuro) — secciones de capítulos en el `<itunes:summary>` del item.

Estructura JSON (schema_version: 2):

```json
{
  "schema_version": 2,
  "slug": "<slug>",
  "total_duration_seconds": ...,
  "intro_duration_seconds": 2.53,
  "silence_after_intro_seconds": 2.0,
  "silence_before_outro_seconds": 3.0,
  "outro_duration_seconds": 11.89,
  "narration_duration_seconds": ...,
  "narration_chars": ...,
  "narration_chars_per_second": ...,
  "chunks": [{"index": 1, "file_relative": "...", "duration_seconds": ..., "char_count": ...}, ...],
  "chapters": [{"number": 1, "title": "La cocina", "start_seconds": 6.1}, ...]
}
```

**Cambio 2026-04-25 — schema v1 → v2.** El campo `silence_duration_seconds` (silencio único después del intro) se sustituye por dos campos separados: `silence_after_intro_seconds` (default 2.0s, inicio narración) y `silence_before_outro_seconds` (default 3.0s, respiro narrativo entre el FIN del relato y la CTA final de marca). El JSON v1 de `la-objecion` (piloto) sigue siendo compatible con `/audiobook-distribute` (lee `silence_duration_seconds` como fallback si v2 no está presente). Audiolibros nuevos van directamente con v2.

**Detección de capítulos:** regex `CHAPTER_HEADING_RE` sobre el `audiolibro.txt` que matchea las dos convenciones soportadas (ver paso 2 § "Convención de headings de capítulo"):
- `Uno. La cocina.` (canónica corta)
- `Parte uno. La cocina.` (alternativa larga, prefijo case-insensitive)

Anclado a inicio de línea (re.MULTILINE) + ordinal case-insensitive + título corto + punto final. Evita falsos positivos de párrafos que contengan "Uno." mid-sentence (cardinales numéricos narrativos).

**Mapping char→tiempo:** velocidad uniforme global. `chars_per_second = narration_chars / narration_duration` calculado tras el TTS. Asume que el narrador (Gabo / Luis) lee a velocidad constante entre chapters — error real ±5% (1-3 s en chapters de 5+ minutos), tolerable para YouTube chapters donde el espectador acepta offset menor.

**Fallback sin capítulos detectados:** si el relato no tiene headings `Uno. Dos. Tres.` ni `Parte uno. Parte dos.` (relatos flash <800 palabras o experimentales), se genera 1 chapter sintético `{"number": 1, "title": "Relato", "start_seconds": <intro+silencio>}` para que YouTube tenga al menos 1 entry válida.

**Verificación post-output OBLIGATORIA del chunks-index** (Claude debe correrla antes de cerrar el skill — evita pasar un index roto a `/audiobook-distribute`):

```bash
python -c "
import json, re
from pathlib import Path
slug = '<slug>'
idx = json.loads(Path(f'assets/audio/ficciones/{slug}-chunks-index.json').read_text(encoding='utf-8'))
txt = next(Path('content/ficciones').rglob(f'{slug}/audiolibro.txt')).read_text(encoding='utf-8')
real = max(
    len(re.findall(r'^Parte (uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)\.', txt, re.MULTILINE | re.IGNORECASE)),
    len(re.findall(r'^(Uno|Dos|Tres|Cuatro|Cinco|Seis|Siete|Ocho|Nueve|Diez|Once|Doce)\.', txt, re.MULTILINE)),
)
detected = len(idx['chapters'])
long_titles = [c for c in idx['chapters'] if len(c['title']) > 80]
print(f'Capítulos detectados: {detected} | esperados según .txt: {real}')
print(f'Títulos largos (>80 chars, posibles falsos positivos): {len(long_titles)}')
ok = (detected == real or (detected == 1 and idx['chapters'][0]['title'] == 'Relato')) and not long_titles
print('OK' if ok else 'FAIL — revisar manualmente antes de /audiobook-distribute')
"
```

Si imprime FAIL → reportar a Rafael con detalle (capítulos detectados vs esperados, títulos sospechosos) y NO continuar con `/audiobook-distribute` hasta arreglar. El fix recomendado es renombrar headings del `audiolibro.txt` a la convención canónica + re-ejecutar el script (NO requiere re-gastar TTS — `chunks-index.json` se regenera barato del .txt). Bug origen 2026-04-25: regex antiguo solo aceptaba `Uno./Dos.`; ahora soporta también `Parte X.` tras fix.

### 6.6. Generar covers derivados (YouTube + podcast)

Tras escribir `chunks-index.json`, invocar:

```bash
python utilities/generate_audiobook_covers.py <slug>
```

Genera 2 outputs idempotentes desde el hero del relato (`content/ficciones/**/<slug>/assets/hero-<slug>-*.png` o variantes):

- `assets/audio/ficciones/covers/<slug>-yt-1280x720.png` — cover YouTube 16:9 PNG. Sin texto overlay (los chyrons los añade ffmpeg en runtime al MP4). Sirve también como thumbnail estático del vídeo antes de play.
- `assets/audio/ficciones/covers/<slug>-podcast-1400x1400.jpg` — cover podcast 1:1 JPEG quality 88. Va al `<itunes:image>` de cada `<item>` del feed RSS y aparece como artwork del episodio en Spotify/Apple/Amazon.

**Si falta el hero del relato:** el script falla amigablemente sugiriendo correr `/nano-banana` para generarlo. Sin hero no hay distribución.

**Estrategia de transformación:** crop al center con aspect ratio target (no letterbox), Lanczos resize. Preserva el sujeto centrado de los heros generados con `/nano-banana` (convención visual ROBOHOGAR).

**Versionado:** las versiones se sobrescriben (idempotente — son derivados, no assets primarios). El hero original sigue versionado como siempre (`hero-<slug>-v2`, `-v3`...).

### 7. Instrucciones de pegado para Rafael

Presentar al final en el chat, tras los 4 strings:

> **Archivo con todo persistido:** `content/ficciones/**/<slug>/beehiiv-audiolibro-snippets.md`
>
> **Posición en Beehiiv** (orden de pegado):
> 1. Pega (a) como título del post.
> 2. Pega (b) como subtítulo.
> 3. Pega (c) como primer Custom HTML block (`/html`) inmediatamente después del subtítulo.
> 4. Pega (d) como segundo Custom HTML block inmediatamente después del anterior.
> 5. **Configurar visibility por bloque:**
>    - Bloque (c) → hide from web (solo email).
>    - Bloque (d) → hide from email (solo web).
> 6. El cuerpo del relato (`Uno. / Dos. / …`) va después de ambos bloques.

## Verificación pre-output

Antes de entregar los 4 strings, Claude debe:

- [ ] Confirmar con `curl -sI -A "Mozilla/5.0 ..."` que la URL pública del MP3 responde HTTP 200 + `Content-Type: audio/mpeg` + `Content-Length` no-cero. (Sin UA de navegador da 403 — es bot protection de Cloudflare, documentado en `verify_r2_auth.py`.)
- [ ] Probar duración real del MP3 con `ffprobe` — reportar a Rafael cualquier diferencia >10% sobre la estimada en paso 3.
- [ ] Comprobar que los 2 bloques HTML están bien formateados (balanced tags, URLs completas, substitutions correctas).

## Output final esperado

Resumen limpio con:
- URL pública R2 del MP3
- Duración final
- Tamaño del archivo
- Los 4 strings (a, b, c, d) listos para copy-paste
- Instrucciones de pegado en Beehiiv (paso 6 arriba)

## Regeneración parcial (si un chunk suena mal)

Si Rafael detecta una transición rara o un nombre mal pronunciado:
- Los chunks individuales están persistidos en `assets/audio/ficciones/_chunks-<slug>/`.
- Se puede regenerar **solo el chunk afectado** llamando a la API con el texto del chunk + ajustes en `voice_settings` (más stability si suena inestable; más similarity_boost si cambia timbre).
- Re-concatenar con ffmpeg usando los mismos chunks + el nuevo.
- Re-subir a R2 (sobreescribe la key `<slug>.mp3`).

No rehacer los 5 chunks si solo 1 es el problema — ahorra cuota API.

## Versionado

El MP3 en R2 se sobreescribe con cada regeneración (`<slug>.mp3` es la key fija). Los chunks locales también se sobreescriben dentro de `_chunks-<slug>/`. Si Rafael quiere conservar una versión anterior antes de regenerar, debe descargarla del R2 manualmente antes.

Para futuras iteraciones: si se quiere versionado tipo `<slug>-v2.mp3`, el script acepta argumento adicional. De momento FASE 2 = una sola versión canónica.

## Coste en régimen

- **Un relato standalone (~3500 palabras, ~20k chars):** ~$2.00 API en overage, ~33% cuota mensual Starter.
- **Un relato episodio-serie (~1500 palabras, ~9k chars):** ~$0.90, ~15% cuota.
- **Un flash (~700 palabras, ~4k chars):** ~$0.40, ~7% cuota.

Starter cubre holgado **~3-4 relatos standalone/mes** o cualquier mezcla equivalente. Si se cruza el umbral 3 meses seguidos → upgrade a Creator $11/mes yearly (121k credits).

## Referencias cruzadas

- Plan completo: [`docs/plan-audiolibros-ficciones.md`](../../docs/plan-audiolibros-ficciones.md).
- Script del pipeline: [`utilities/generate_audio.py`](../../utilities/generate_audio.py).
- Verificadores de credenciales: [`utilities/verify_elevenlabs_auth.py`](../../utilities/verify_elevenlabs_auth.py) + [`utilities/verify_r2_auth.py`](../../utilities/verify_r2_auth.py).
- Regla editorial ficción: [`.claude/rules/editorial.md § Narrativa especulativa`](../rules/editorial.md).
- Convención TTS audiolibro copy: memoria [`feedback_ficcion_audiolibro_copy.md`](../../../RRP-DEV/.claude/memory/feedback_ficcion_audiolibro_copy.md).
- Convención `ROBO OGAR`: plan § Decisiones cerradas 2026-04-22.
- Dual block email+web: memoria [`feedback_beehiiv_email_web_dual_block.md`](../../../RRP-DEV/.claude/memory/feedback_beehiiv_email_web_dual_block.md).
