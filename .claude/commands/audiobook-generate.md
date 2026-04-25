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
- [ ] **Cuota ElevenLabs suficiente para el relato** (CRÍTICO antes de invocar — evita fallo mid-pipeline tras gastar TTS de algunos chunks). Estimación rápida: cada relato consume ~80% de los chars del `audiolibro.txt` (algunos chars no van al TTS). Margen recomendado: **chars libres ≥ chars del .txt**. Verificación:

  ```bash
  python -c "
  import requests, json
  from pathlib import Path
  env = json.loads(Path('.claude/settings.local.json').read_text())['env']
  txt_chars = len(Path('content/ficciones/**/<slug>/audiolibro.txt').read_text(encoding='utf-8'))
  # Cuota: la API user/subscription requiere scope user_read; si la API key no lo tiene,
  # el script TTS falla con HTTP 401 quota_exceeded incluyendo info en el error.
  # Workaround pragmático: intentar un chunk dummy de 1 char y leer el header X-Character-Cost
  # vs response, o revisar manualmente el dashboard https://elevenlabs.io/app/usage.
  print(f'Chars del .txt: {txt_chars}')
  print(f'Cuota mensual Starter: 40.000 chars · Creator: 100.000 chars')
  print(f'Si es la primera invocación del mes, sobra. Si ya generaste otros audios este mes,')
  print(f'verificar en https://elevenlabs.io/app/usage que quedan ≥{int(txt_chars * 1.1)} chars libres.')
  "
  ```

  Si la cuota libre es <1.1× los chars del .txt, advertir a Rafael ANTES de empezar TTS:
  - Opción A: esperar al reset mensual (mirar fecha en dashboard).
  - Opción B: upgrade de plan (Starter $5 → Creator $22, multiplica cuota ×2.5).
  - Opción C: comprar pack de créditos extra one-time si Eleven lo ofrece.

  **NO empezar `python utilities/generate_audio.py` si hay riesgo de quota_exceeded a mitad de los chunks** — costaría re-generar todo desde cero al recargar cuota, ya que los chunks parciales no son recuperables. Bug origen 2026-04-25: regeneración de "la-objecion" falló en el chunk 1 con HTTP 401 quota_exceeded (880 créditos restantes vs 3.373 necesarios), forzando upgrade a Creator a mitad de la sesión.

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
| Modelos ficticios con guión | `HOGAR-X5` | `HOGAR equis cinco` (el guión confunde, la separación forzada evita que Luis diga "menos" o "guión") |
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

### 6.5. chunks-index.json — automático, no requiere acción

`utilities/generate_audio.py` genera automáticamente `assets/audio/ficciones/<slug>-chunks-index.json` al final del run. Lo consume `/audiobook-distribute` (FASE 3) para componer:

- **Chyrons del MP4 YouTube** — un drawtext por capítulo con fade in/out al cruzar `start_seconds` (opción D++ híbrido del plan).
- **Chapters timestamped en la descripción YouTube** — formato `MM:SS Capítulo I — Título` que YouTube auto-renderiza como navegación interna del vídeo.
- **Show notes RSS** (opcional, futuro) — secciones de capítulos en el `<itunes:summary>` del item.

Estructura JSON (schema_version: 1):

```json
{
  "schema_version": 1,
  "slug": "<slug>",
  "total_duration_seconds": ...,
  "intro_duration_seconds": 2.53,
  "silence_duration_seconds": 2.0,
  "outro_duration_seconds": 11.89,
  "narration_duration_seconds": ...,
  "narration_chars": ...,
  "narration_chars_per_second": ...,
  "chunks": [{"index": 1, "file_relative": "...", "duration_seconds": ..., "char_count": ...}, ...],
  "chapters": [{"number": 1, "title": "La cocina", "start_seconds": 6.1}, ...]
}
```

**Detección de capítulos:** regex `CHAPTER_HEADING_RE` sobre el `audiolibro.txt` que matchea las dos convenciones soportadas (ver paso 2 § "Convención de headings de capítulo"):
- `Uno. La cocina.` (canónica corta)
- `Parte uno. La cocina.` (alternativa larga, prefijo case-insensitive)

Anclado a inicio de línea (re.MULTILINE) + ordinal case-insensitive + título corto + punto final. Evita falsos positivos de párrafos que contengan "Uno." mid-sentence (cardinales numéricos narrativos).

**Mapping char→tiempo:** velocidad uniforme global. `chars_per_second = narration_chars / narration_duration` calculado tras el TTS. Asume que Luis lee a velocidad constante entre chapters — error real ±5% (1-3 s en chapters de 5+ minutos), tolerable para YouTube chapters donde el espectador acepta offset menor.

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
