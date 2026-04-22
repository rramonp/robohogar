# Audiobook Generate — generador de audiolibros para Ficciones Domésticas

Genera el audiolibro MP3 de un relato de Ficciones Domésticas: lee el texto, construye la versión TTS-optimizada, llama a la API de ElevenLabs con voz Luis, concatena con intro/outro de marca, sube a Cloudflare R2 y devuelve los 4 strings listos para copy-paste en Beehiiv.

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
- [ ] `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` existen (bumpers de marca con voz Luis, generados una vez en FASE 0).
- [ ] `ffmpeg` accesible vía PATH o WinGet install location. El script `utilities/generate_audio.py` ya detecta ambos.
- [ ] `boto3` instalado (`pip install boto3`).

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

Aplicar las siguientes transformaciones:

| Qué | De | A |
|---|---|---|
| Romanos de sección | `## I. Título`, `## II.`, `## III.` | `Uno. Título.`, `Dos. Título.`, `Tres. Título.` (como líneas aparte, con punto final) |
| Markdown italics | `*palabra*` | `palabra` (sin asteriscos — al TTS le salen artefactos con ellos) |
| Markdown bold | `**palabra**` | `palabra` (mismo motivo) |
| Middle dots en texto de app/UI | `Ramón García Torres · esposo · fallecido 2027` | `Ramón García Torres, esposo, fallecido dos mil veintisiete` (comas + años a palabras) |
| Modelos ficticios con guión | `HOGAR-X5` | `HOGAR equis cinco` (el guión confunde, la separación forzada evita que Luis diga "menos" o "guión") |
| Marca ROBOHOGAR (si aparece literal) | `ROBOHOGAR` | `ROBO OGAR` (regla del plan — evita que Multilingual v2 aspire la H a la inglesa) |
| Años en italic o prose corta | `2027`, `2024/1689` | `dos mil veintisiete`, eliminar parentéticos con slash (reescribir si son técnicos) |
| Porcentajes | `80%`, `85%` | `ochenta por ciento`, `ochenta y cinco por ciento` |
| Cifras grandes redondas | `900.000 personas` | `novecientas mil personas` |
| Acrónimos expandibles | `SEN` | `la Sociedad Española de Neurología` (primera mención; segunda puede ir abreviada si aparece) |
| Rangos de años técnicos | `(2015-2018)` | `de dos mil quince a dos mil dieciocho` |
| Regulaciones con número | `AI Act (Reglamento UE 2024/1689)` | `el reglamento europeo de inteligencia artificial` (reformular) |
| Separators `---` | `---` | (eliminar — se pierden en TTS) |
| HTML comments | `<!-- ... -->` | (eliminar) |
| Títulos con hash | `# El que viene a tomar café` | `El que viene a tomar café.` (sin hash, con punto final) |

**Lo que NO se toca** (Luis los maneja bien):
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

Preguntar: *"¿Procedo a generar el MP3 o quieres tocar algo primero?"*

**NO invocar el script TTS hasta que Rafael dé OK explícito.** Si pide cambios, editar el `audiolibro.txt` y volver a presentar stats.

### 4. Generar el audio

```bash
python utilities/generate_audio.py content/ficciones/**/<slug>/audiolibro.txt <slug>
```

El script (ver [`utilities/generate_audio.py`](../../utilities/generate_audio.py)) hace:
- Chunking por párrafos ≤4500 chars (límite Multilingual v2).
- TTS por chunk con voz Luis (`GojDwihhnL1f7RrBuXsJ`), modelo `eleven_multilingual_v2`, formato `mp3_44100_128`, con `previous_text`/`next_text` para prosodia coherente entre chunks.
- Concatenación ffmpeg: intro (2.53s) + 2s silencio + chunks narración + outro (11.89s), recodificando todo a 44.1kHz mono 128kbps.
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
