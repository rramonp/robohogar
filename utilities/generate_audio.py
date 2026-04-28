"""
Generate audiobook MP3 for a Ficciones Domésticas relato.

Pipeline end-to-end:
  1. Lee `audiolibro.txt` TTS-optimizado del relato.
  2. Divide en chunks por párrafos respetando el límite ~4500 chars/request
     del plan Starter ElevenLabs.
  3. Llama `/v1/text-to-speech/{voice_id}` por cada chunk con voz Gabo
     (o0SveC0zgHFuCsEO3vHR — default desde 2026-04-27, sustituye Luis para
     el cuerpo del relato) y modelo Multilingual v2. Pasa previous_text /
     next_text para mantener prosodia coherente entre chunks.
  4. Sintetiza un chunk extra de "anuncio del título" con la misma voz Gabo
     pero parámetros prosódicos especiales (style=0.5, stability=0.4 +
     previous_text artificial simulando cierre del bumper Luis) — sin estos
     parámetros, una frase tan corta como "El cristalero." se lee con
     entonación de "frase incompleta". Canon obligatorio desde 2026-04-28
     PM (regla `editorial.md § Composición canon del audiolibro`).
  5. Concatena con ffmpeg: intro Luis + 2s silencio + ANUNCIO DEL TÍTULO
     Gabo + 2s silencio + chunks narración Gabo + 3s silencio + outro Luis,
     recodificando todo a 44.1kHz mono 128kbps MP3 consistente. El silencio
     de 3s antes del outro es respiro narrativo entre el FIN del relato y
     la CTA final de marca (decisión 2026-04-25). Canon híbrido bumpers
     Luis + cuerpo Gabo restaurado 2026-04-28 tras revertir el experimento
     "100% Gabo" del 2026-04-27 PM.
  6. Sube el MP3 final a Cloudflare R2 bucket (ContentType audio/mpeg)
     y devuelve la URL pública.

Uso:
    python utilities/generate_audio.py <audiolibro.txt> <slug> <title>

El <title> es el `title:` corto del frontmatter del relato (ej: "El cristalero",
NO el `display_title:` declarativo largo). El script le añade automáticamente
un punto final si falta — el frontispicio HTML del Snippet 2.5 y el anuncio
TTS deben coincidir letra por letra.

Ejemplo:
    python utilities/generate_audio.py \
        content/ficciones/_one-shots/el-cristalero/audiolibro.txt \
        el-cristalero \
        "El cristalero"

Requisitos:
  - `.claude/settings.local.json` con ELEVENLABS_API_KEY + R2_* (5 vars).
  - `boto3` instalado (pip install boto3).
  - ffmpeg accesible vía PATH o WinGet install path Gyan.FFmpeg*.
  - `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` pregenerados
    (voz Luis — son los bumpers de marca, distintos de la voz del cuerpo).

Idempotencia: los chunks temporales se guardan en
`assets/audio/ficciones/_chunks-<slug>/` — sirven para debug si el audio
sale raro, y se pueden borrar a mano al confirmar que el MP3 final va bien.
"""

import glob
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

import boto3
from botocore.client import Config

# Contador local de saldo ElevenLabs. Necesario porque la API key actual no
# tiene permiso user_read y /v1/user/subscription devuelve 401 — sin esto
# no podemos saber si quedan créditos antes de lanzar TTS y los chunks
# parciales no son recuperables si la cuota se agota mid-pipeline.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from elevenlabs_balance import pre_check, record_usage  # noqa: E402


# Defensive: fuerza UTF-8 en stdout para no romper en consolas Windows que
# usan cp1252 por defecto (Python 3.14 + cmd.exe/PS5 sin chcp 65001). En
# bash MINGW o PowerShell 7+ ya es UTF-8 así que el reconfigure es no-op.
# `errors="replace"` evita crashes si algún glyph no existe en la consola.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# Decisiones canon del plan audiolibros (docs/plan-audiolibros-ficciones.md).
VOICE_ID = "o0SveC0zgHFuCsEO3vHR"  # Gabo — Deep, Evocative and Resonant (default cuerpo desde 2026-04-27, sustituye Luis GojDwihhnL1f7RrBuXsJ que se mantiene en intro/outro como bumpers de marca)
MODEL_ID = "eleven_multilingual_v2"
# mp3_44100_128 coincide con intro-ficciones.mp3 (44.1kHz mono 128kbps).
OUTPUT_FORMAT = "mp3_44100_128"

# Límite seguro bajo el cap ~5000 chars/request de Multilingual v2 en Starter.
# Dejo margen para no llegar al límite duro y para encajar párrafos completos.
MAX_CHUNK_CHARS = 4500

# Silencio entre outro del intro y primera frase de narración.
# La regla original del plan pedía 2s baked en el intro; lo inyectamos aquí
# para mantener el intro asset limpio y reutilizable.
SILENCE_AFTER_INTRO_SEC = 2.0

# Silencio entre el anuncio del título y el primer "Parte uno" del cuerpo.
# 2s suficiente para marcar la frontera entre frontispicio sonoro y el
# arranque narrativo, sin que se note como una pausa muerta.
SILENCE_AFTER_TITLE_SEC = 2.0

# Cierre del bumper Luis canónico (asset assets/audio/intro-ficciones.mp3).
# Lo pasamos como `previous_text` al TTS del título para que Multilingual v2
# asuma que viene tras una frase ya cerrada y aplique entonación inicial
# limpia. Sin esto, "El cristalero." (≤3 palabras) se lee como inicio de
# frase incompleta. Documentado en feedback_audiolibro_titulo_obligatorio.md.
BUMPER_LUIS_CLOSE_TEXT = "Una Ficción Doméstica de ROBO, OGAR."

# Silencio entre la última palabra de la narración (FIN del relato) y la
# CTA final de marca (outro-ficciones.mp3). Default 3s para dar respiro
# narrativo al lector — más largo que el silencio de entrada porque el
# contraste tonal es mayor (de prosa íntima a voz de marca corporativa).
# Decisión 2026-04-25 tras feedback Rafael: el outro arrancaba inmediato
# tras el FIN y rompía el respiro emocional del cierre del relato.
SILENCE_BEFORE_OUTRO_SEC = 3.0

# Paths relativos al root del repo (este script vive en utilities/).
REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
INTRO_MP3 = REPO_ROOT / "assets" / "audio" / "intro-ficciones.mp3"
OUTRO_MP3 = REPO_ROOT / "assets" / "audio" / "outro-ficciones.mp3"


# ══════════════════════════════════════════════════════════════════════════
# Carga de entorno y utilidades de sistema
# ══════════════════════════════════════════════════════════════════════════

def load_env() -> dict:
    """Carga las 6 env vars requeridas desde settings.local.json.

    Aborta con mensaje claro si alguna falta o sigue como placeholder — evita
    errores crípticos al hacer HTTP/S3 calls con strings basura.
    """
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    required = [
        "ELEVENLABS_API_KEY",
        "R2_ACCOUNT_ID",
        "R2_ACCESS_KEY",
        "R2_SECRET_KEY",
        "R2_BUCKET",
        "R2_PUBLIC_URL",
    ]
    for k in required:
        v = env.get(k, "")
        if not v or v.startswith(("REEMPLAZAR", "PEGAR")):
            sys.exit(f"ERROR: env var {k} no configurada en settings.local.json")
    return env


def find_ffmpeg() -> str:
    """Localiza el ejecutable de ffmpeg.

    Orden de búsqueda:
      1. PATH del sistema (normal tras reiniciar la shell post-install).
      2. WinGet install location de Gyan.FFmpeg (fallback Windows).

    Razón del fallback: cuando winget instala ffmpeg modifica el PATH del
    registro pero las shells ya abiertas no lo ven hasta reiniciar. Este
    script debe funcionar aunque se ejecute en la misma sesión que hizo
    el install.
    """
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    pattern = os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\**\ffmpeg.exe"
    )
    matches = glob.glob(pattern, recursive=True)
    if matches:
        return matches[0]
    sys.exit("ERROR: ffmpeg no encontrado ni en PATH ni en WinGet install")


# ══════════════════════════════════════════════════════════════════════════
# Normalización de marca para TTS
# ══════════════════════════════════════════════════════════════════════════

# Pattern que captura todas las variantes históricas y futuras de la marca
# en el texto TTS. Cubre: ROBOHOGAR, ROBO OGAR, ROBO  OGAR (doble espacio),
# ROBO,OGAR (sin espacio post-coma), ROBO, OGAR (canónica). Case-sensitive
# a propósito: solo normalizamos cuando la marca aparece en uppercase como
# asset de marca; "robohogar" en lowercase dentro del cuerpo de un relato
# se respeta tal cual (decisión editorial del autor).
BRAND_PATTERN = re.compile(r"\bROBO\s*,?\s*H?OGAR\b")
BRAND_CANONICAL = "ROBO, OGAR"


def apply_tts_brand_substitutions(text: str) -> str:
    """Normaliza menciones de la marca ROBOHOGAR para TTS → 'ROBO, OGAR'.

    Por qué la coma: el motor Multilingual v2 de ElevenLabs puede aspirar
    la H estilo inglés cuando ve "ROBOHOGAR" como token contiguo, sonando
    "RoboJOgar" al oído castellano peninsular (donde la H es muda). La
    convención previa "ROBO OGAR" (espacio simple) tampoco garantizaba
    pausa: el motor en ciertos contextos empalmaba las dos palabras.

    La coma fuerza una pausa prosódica de ~150-300 ms que el espacio
    simple no garantiza, suficiente para separar las dos sílabas sin
    que suene a final de frase (eso lo haría el punto). Decisión
    canonizada 2026-04-25 — ver `feedback_robohogar_tts_pronunciation.md`
    + `docs/plan-audiolibros-ficciones.md § Decisiones cerradas`.

    Idempotente: aplicar 2 veces produce el mismo resultado. Migra
    automáticamente la convención antigua "ROBO OGAR" presente en
    relatos generados con la versión previa del pipeline.
    """
    matches = BRAND_PATTERN.findall(text)
    if matches:
        # Solo informamos si había variantes no-canónicas — evita ruido
        # cuando el texto ya viene normalizado.
        non_canonical = [m for m in matches if m != BRAND_CANONICAL]
        if non_canonical:
            print(
                f"  Normalizadas {len(non_canonical)} mención(es) de marca "
                f"a '{BRAND_CANONICAL}' (pronunciación TTS canónica)",
                flush=True,
            )
    return BRAND_PATTERN.sub(BRAND_CANONICAL, text)


# ══════════════════════════════════════════════════════════════════════════
# Chunking del texto
# ══════════════════════════════════════════════════════════════════════════

def chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Divide el texto en chunks respetando párrafos completos.

    Estrategia: partir por doble-newline (párrafos) y acumular hasta que
    añadir el siguiente supere max_chars — entonces cierra el chunk actual
    y abre uno nuevo. Garantiza que nunca se corta un párrafo a la mitad,
    lo que preservaría el ritmo narrativo al narrarlo.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    current = ""
    for p in paragraphs:
        candidate = f"{current}\n\n{p}" if current else p
        # Si el candidato excede el límite Y ya tenemos algo acumulado,
        # cerramos el chunk actual y empezamos uno nuevo con este párrafo.
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = p
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


# ══════════════════════════════════════════════════════════════════════════
# Llamada a ElevenLabs TTS
# ══════════════════════════════════════════════════════════════════════════

def call_elevenlabs_tts(
    api_key: str,
    text: str,
    chunk_index: int,
    total_chunks: int,
    prev_text: str = "",
    next_text: str = "",
) -> bytes:
    """Llama al endpoint /v1/text-to-speech/{voice_id} y devuelve bytes MP3.

    previous_text / next_text dan contexto adyacente al modelo para mantener
    prosodia y entonación coherentes entre chunks — es la forma oficial que
    recomienda ElevenLabs para narraciones largas chunked. Usamos los 500
    últimos chars del chunk anterior y los 500 primeros del siguiente.
    """
    url = (
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        f"?output_format={OUTPUT_FORMAT}"
    )
    body = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            # stability 0.5: balance entre consistencia y variación expresiva
            "stability": 0.5,
            # similarity_boost 0.75: mantiene tono de la voz del cuerpo
            # (Gabo) sin perder naturalidad (1.0 suena robótico en
            # narrativa larga)
            "similarity_boost": 0.75,
            # style 0.0: narración natural, sin exagerar tono emocional
            "style": 0.0,
            # speaker_boost True: refuerza identidad del narrador entre chunks
            "use_speaker_boost": True,
        },
    }
    if prev_text:
        body["previous_text"] = prev_text[-500:]
    if next_text:
        body["next_text"] = next_text[:500]

    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    label = f"[{chunk_index + 1}/{total_chunks}]"
    print(f"  {label} TTS call ({len(text):,} chars)...", flush=True)
    try:
        # Timeout generoso — Multilingual v2 tarda ~10-30s por chunk.
        with urllib.request.urlopen(req, timeout=180) as resp:
            audio = resp.read()
        print(f"    -> recibidos {len(audio):,} bytes MP3", flush=True)
        return audio
    except urllib.error.HTTPError as e:
        body_snip = e.read().decode("utf-8", errors="replace")[:300]
        sys.exit(f"  {label} FAIL HTTP {e.code}: {body_snip}")


# ══════════════════════════════════════════════════════════════════════════
# TTS especial del anuncio de título (frontispicio sonoro)
# ══════════════════════════════════════════════════════════════════════════

def synthesize_title_announce(api_key: str, title_text: str) -> bytes:
    """TTS de la tarjeta de título con voz Gabo y prosodia de anuncio.

    Devuelve los bytes MP3 del título leído entre intro Luis y cuerpo
    narrativo. Es el equivalente sonoro del frontispicio HTML del Snippet
    2.5 (Anagrama / Penguin Modern Classics) — el oyente acaba de oír el
    bumper de marca, escucha 2s de silencio y entonces el narrador del
    relato dice el título antes de empezar el cuerpo.

    Por qué parámetros distintos a los del cuerpo:
      - `previous_text=BUMPER_LUIS_CLOSE_TEXT`: Multilingual v2 lee frases
        muy cortas sin contexto previo como si fueran inicio de oración
        incompleta. Pasarle un cierre simulado del bumper Luis le indica
        que viene tras una frase declarativa cerrada → entonación inicial
        natural en lugar de prosodia "frase a medias".
      - `style=0.5` (cuerpo: 0.0): expresividad de presentación, no de
        narración íntima — sube ligeramente el énfasis del título.
      - `stability=0.4` (cuerpo: 0.5): permite suficiente variación para
        que el cierre del título caiga en pitch como final declarativo.
      - `next_text=""` (no se pasa): queremos que el título cierre con
        prosodia descendente. Si pasáramos el primer párrafo del cuerpo,
        Gabo encadenaría sin pausa.

    Validado 2026-04-28 con `el-cristalero` (`title:` "El cristalero", 14
    chars) — sonaba a frase incompleta con defaults; con estos parámetros
    suena como tarjeta de título limpia. Detalle en
    `feedback_audiolibro_titulo_obligatorio.md`.
    """
    # Normalización defensiva: el título debe terminar con punto para que
    # el modelo aplique cierre prosódico. Si el frontmatter trae
    # "El cristalero" sin punto, lo añadimos. Idempotente.
    text = title_text.strip()
    if not text.endswith((".", "?", "!")):
        text = text + "."

    url = (
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        f"?output_format={OUTPUT_FORMAT}"
    )
    body = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75,
            "style": 0.5,
            "use_speaker_boost": True,
        },
        "previous_text": BUMPER_LUIS_CLOSE_TEXT,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    print(f"  [título] TTS announce ({len(text)} chars: '{text}')...", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            audio = resp.read()
        print(f"    -> recibidos {len(audio):,} bytes MP3", flush=True)
        return audio
    except urllib.error.HTTPError as e:
        body_snip = e.read().decode("utf-8", errors="replace")[:300]
        sys.exit(f"  [título] FAIL HTTP {e.code}: {body_snip}")


# ══════════════════════════════════════════════════════════════════════════
# Concatenación y subida
# ══════════════════════════════════════════════════════════════════════════

def concat_with_ffmpeg(
    ffmpeg: str,
    intro: Path,
    silence_after_intro_sec: float,
    title_file: Path,
    silence_after_title_sec: float,
    chunk_files: list[Path],
    silence_before_outro_sec: float,
    outro: Path,
    output: Path,
) -> None:
    """Concatena todas las piezas en un MP3 final consistente.

    Usa el concat filter (no el concat demuxer) porque permite recodificar
    todo a un sample rate / bitrate uniforme — evita el glitch de pops o
    variaciones de loudness entre secciones con bitrates distintos.

    Pipeline de streams (canon desde 2026-04-28 PM con título intercalado):
      intro Luis            -> [0:a]
      silencio after_intro  -> [1:a]
      título Gabo (anuncio) -> [2:a]
      silencio after_title  -> [3:a]
      chunk1                -> [4:a]
      chunk2                -> [5:a]
      ...
      chunkN                -> [N+3:a]
      silencio before_outro -> [N+4:a]
      outro Luis            -> [N+5:a]
    """
    inputs: list[str] = [
        "-i", str(intro),
        "-f", "lavfi", "-t", str(silence_after_intro_sec),
        "-i", "anullsrc=r=44100:cl=mono",
        "-i", str(title_file),
        "-f", "lavfi", "-t", str(silence_after_title_sec),
        "-i", "anullsrc=r=44100:cl=mono",
    ]
    for cf in chunk_files:
        inputs.extend(["-i", str(cf)])
    inputs.extend(["-f", "lavfi",
                   "-t", str(silence_before_outro_sec),
                   "-i", "anullsrc=r=44100:cl=mono"])
    inputs.extend(["-i", str(outro)])

    # n_total = intro (1) + sil_after_intro (1) + título (1) + sil_after_title (1)
    #         + chunks (N) + sil_before_outro (1) + outro (1)
    n_total = 4 + len(chunk_files) + 2
    stream_labels = "".join(f"[{i}:a]" for i in range(n_total))
    filter_str = f"{stream_labels}concat=n={n_total}:v=0:a=1[out]"

    cmd = [
        ffmpeg, "-y",
        *inputs,
        "-filter_complex", filter_str,
        "-map", "[out]",
        # libmp3lame con 128kbps = coherente con intro, suficiente para voz.
        "-codec:a", "libmp3lame",
        "-b:a", "128k",
        "-ar", "44100",
        "-ac", "1",
        str(output),
    ]
    print("  Concatenando con ffmpeg (recodificación coherente)...", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        # Mostramos solo los últimos 500 chars del stderr — el verbose de
        # ffmpeg es muy largo pero el error real suele estar al final.
        sys.exit(f"ffmpeg FAIL:\n{result.stderr[-500:]}")


def probe_duration(ffmpeg: str, mp3: Path) -> float:
    """Pregunta a ffprobe la duración del MP3 para reportarla al final.

    Deriva la ruta de ffprobe a partir de la de ffmpeg cambiando SOLO el
    basename del ejecutable (no todas las apariciones del string "ffmpeg"
    en la ruta — las carpetas instaladas por winget contienen "ffmpeg" y
    un replace global corrompe la ruta).
    """
    p = Path(ffmpeg)
    ffprobe_name = p.name.replace("ffmpeg", "ffprobe")
    ffprobe = str(p.with_name(ffprobe_name))
    if not Path(ffprobe).exists():
        # Fallback silencioso — la duración es info nice-to-have, no crítica.
        return 0.0
    result = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3)],
        capture_output=True, text=True,
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


# ══════════════════════════════════════════════════════════════════════════
# Indexado de capítulos para distribución downstream
# ══════════════════════════════════════════════════════════════════════════

# Ordinales en español que se usan como heading de capítulo en audiolibro.txt
# (convención TTS § paso 2 del skill audiobook-generate.md). Mapeo a número
# arábigo para que el JSON downstream pueda ordenar/iterar fácilmente.
SPANISH_ORDINALS = {
    "Uno": 1, "Dos": 2, "Tres": 3, "Cuatro": 4, "Cinco": 5,
    "Seis": 6, "Siete": 7, "Ocho": 8, "Nueve": 9, "Diez": 10,
    "Once": 11, "Doce": 12,
}

# Heading de capítulo: dos convenciones soportadas (ambas detectables sin
# colisión porque el prefijo `Parte ` es específico):
#   1. `Uno. La cocina.`  — convención canónica corta.
#   2. `Parte uno. El botón.` — convención larga (case insensitive en el ordinal).
# Restricciones para evitar falsos positivos:
#   - Anclado a inicio de línea (re.MULTILINE).
#   - El título (grupo 2) limitado a max 60 chars (`{1,60}`) — un heading real
#     siempre es corto. Párrafos narrativos completos que empiezan por
#     "Tres meses antes..." o "Uno por uno..." no matchean porque el `.` final
#     del párrafo queda muchos chars más adelante.
#   - El título no puede contener `;` ni `:` — separadores fuertes de prosa
#     narrativa. La coma SÍ se permite porque algunos relatos usan headings
#     con location + tiempo separados por coma (ej: "Madrid, un martes a las
#     tres y catorce." en `el-operador-nocturno`). El filtro post-regex de
#     orden secuencial (más abajo) descarta cualquier falso positivo que pase.
# Bug origen 2026-04-25 (slug "la-objecion"): regex antiguo solo aceptaba
# `Uno./Dos./...` y agarró 2 falsos positivos al final del texto. Bug
# secundario detectado en testing post-fix (slug "papa-desde-singapur"):
# regex SIN límite de título capturaba párrafos enteros que empiezan por
# `Tres meses antes` / `Las últimas dos semanas`. Fix terciario 2026-04-26
# (slug "el-operador-nocturno"): regex con `[^,;:\n]` rechazaba 3 headings
# legítimos por contener coma → 0 capítulos detectados, fallback "Relato".
# Fix cuaternario 2026-04-27 (slug "pipo"): regex exigía `\.\s*$` y heading
# `Parte cuatro. ¿Jugamos?` falló por terminar en `?`. El filtro post-regex
# hizo break al saltar el 4 y perdimos también 5 y 6 → solo 3/6 detectados.
# Fix: aceptar `[.?!]\s*$` como terminador (interrogación y exclamación son
# headings literarios legítimos en relatos con preguntas como título).
MAX_CHAPTER_TITLE_CHARS = 60
CHAPTER_HEADING_RE = re.compile(
    r"^(?:Parte\s+)?({ordinals})\.\s+([^;:\n]{{1,{maxlen}}}?)([.?!])\s*$".format(
        ordinals="|".join(SPANISH_ORDINALS.keys()),
        maxlen=MAX_CHAPTER_TITLE_CHARS,
    ),
    re.MULTILINE | re.IGNORECASE,
)


# Regex LAXO de detección de capítulos — sirve sólo como red de seguridad
# contra que el regex estricto se quede corto ante una convención nueva
# (heading con `?`/`!`, comas, etc.). NO se usa para construir capítulos
# reales (no captura terminador). Empareja cualquier línea que empieza con
# un ordinal canónico seguido de punto + algo de texto, sea cual sea su
# terminador. Si laxo > estricto, hay headings legítimos que el estricto
# se está saltando — abort con mensaje claro listándolos.
LAX_CHAPTER_HEADING_RE = re.compile(
    r"^(?:Parte\s+)?({ordinals})\.[ \t]+[^\n]+$".format(
        ordinals="|".join(SPANISH_ORDINALS.keys()),
    ),
    re.MULTILINE | re.IGNORECASE,
)


def assert_no_chapters_lost(text: str) -> None:
    """Aborta si el regex estricto detecta menos headings que el laxo.

    Defensa contra bugs futuros del CHAPTER_HEADING_RE. Cuando aparece
    una convención nueva (heading con `?` 2026-04-27 pipo, heading con
    coma 2026-04-26 el-operador-nocturno, etc.) el regex estricto se queda
    corto silenciosamente — el script genera el MP3 y solo al ver el
    chunks-index.json se nota que faltan capítulos. Para entonces ya
    hemos gastado los créditos.

    Esta función corre ANTES del TTS. Si laxo encuentra `Parte cuatro. ¿Jugamos?`
    pero el estricto no lo captura, abort listando los headings perdidos
    + sugerencia de revisar `CHAPTER_HEADING_RE` antes de consumir cuota.
    """
    lax_lines = [m.group(0).strip() for m in LAX_CHAPTER_HEADING_RE.finditer(text)]
    strict_chapters = detect_chapters(text)
    if len(lax_lines) <= len(strict_chapters):
        return  # OK: el estricto cubre todo lo que el laxo ve.

    # Diff: qué líneas laxas no están en los chapters estrictos.
    strict_chartexts = {ch["char_text"] for ch in strict_chapters}
    lost = [line for line in lax_lines if line not in strict_chartexts]
    msg = (
        "\n[ABORT pre-TTS] El detector estricto se ha saltado headings que el "
        f"detector laxo SÍ ve. Encontrados {len(lax_lines)} headings laxos vs "
        f"{len(strict_chapters)} estrictos. Headings perdidos:\n"
        + "\n".join(f"  - {line!r}" for line in lost)
        + "\n\nProbable causa: convención de heading nueva (terminador `?`/`!`, "
        "ordinal compuesto, etc.). Revisa CHAPTER_HEADING_RE en este archivo "
        "antes de gastar créditos ElevenLabs. Si los headings perdidos son "
        "legítimos, amplía el regex y añade un caso de regresión a "
        "utilities/tests/test_chapter_detection.py."
    )
    raise SystemExit(msg)


def detect_chapters(text: str) -> list[dict]:
    """Detecta headings de capítulo en el texto TTS.

    Soporta dos convenciones (ver `CHAPTER_HEADING_RE`):
      - `Uno. La cocina.` (canónica corta)
      - `Parte uno. El botón.` (alternativa larga)

    Devuelve lista ordenada de capítulos con su posición de char absoluta:
    `[{number: 1, title: "La cocina", char_position: 0, char_text: "Uno. La cocina."}, ...]`.

    El char_position se usa después para mapear a tiempo del MP3 final
    asumiendo velocidad de narración uniforme — error ±5% aceptable para
    YouTube chapters (donde el oyente tolera offset de 1-2 s).

    Filtro post-regex: además del límite de longitud del título a nivel regex,
    descartamos capítulos numerados fuera de orden (ej: si encuentra "5" sin
    haber encontrado "1, 2, 3, 4" antes, es falso positivo). Eso bloquea el
    último vestigio de matches espurios cuando un relato menciona "Tres" o
    "Cinco" como sustantivo aislado en su propia línea.
    """
    raw = []
    for m in CHAPTER_HEADING_RE.finditer(text):
        ordinal_key = m.group(1).capitalize()
        title = m.group(2).strip()
        terminator = m.group(3)
        # `.` no aporta información al título limpio (el lector lo lee como
        # ruido visual: "El altar." → "El altar"). `?` y `!` SÍ son parte
        # semántica del heading literario (`¿Jugamos?` / `¡Vámonos!`) y
        # deben sobrevivir al render del chyron y a los YouTube chapters.
        if terminator in ("?", "!"):
            title = f"{title}{terminator}"
        raw.append({
            "number": SPANISH_ORDINALS[ordinal_key],
            "title": title,
            "char_position": m.start(),
            "char_text": m.group(0).strip(),
        })

    # Filtro de orden: el número de capítulo debe ser igual al índice+1 (1, 2, 3, ...).
    # Si encontramos "5" cuando esperábamos "3", ese match es spurio (palabra suelta).
    # Recortamos en el primer capítulo que rompa la secuencia.
    chapters = []
    for i, ch in enumerate(raw):
        if ch["number"] == i + 1:
            chapters.append(ch)
        else:
            break
    return chapters


def build_chunks_index(
    slug: str,
    text: str,
    chunks: list[str],
    chunk_files: list[Path],
    ffmpeg: str,
    intro_duration: float,
    silence_after_intro: float,
    title_text: str,
    title_duration: float,
    silence_after_title: float,
    silence_before_outro: float,
    outro_duration: float,
    total_duration: float,
) -> dict:
    """Construye el dict serializable que se vuelca a chunks-index.json.

    El JSON es la fuente de verdad downstream para `/audiobook-distribute`:
      - YouTube chapters de la descripción (con timestamps por capítulo).
      - Composición del MP4 con chyrons cambiantes (cada capítulo su drawtext).
      - Show notes RSS con sección "capítulos" si quisiéramos en futuro.

    Estrategia de timestamping de capítulos: velocidad uniforme global.
      Calculamos chars/segundo sobre la narración total (excluyendo intro,
      silencio y outro) y mapeamos cada char_position a un offset relativo.
      Para Gabo ES Multilingual v2 sale ~12-14 cps (más pausado que Luis
      ~16-20 cps), suficientemente uniforme entre chunks para que el error
      sea de 1-3 s, dentro de tolerancia.
    """
    # Duraciones reales de cada chunk (medidas con ffprobe, no estimadas).
    # Sirven para que downstream pueda ofrecer timestamps muy precisos por
    # chunk individual aunque el chapters_index use velocidad uniforme.
    chunk_durations = [probe_duration(ffmpeg, cf) for cf in chunk_files]

    # Total chars de narración (excluye outro/intro porque no son chunks).
    narration_chars = sum(len(c) for c in chunks)
    narration_duration = sum(chunk_durations)

    # Velocidad de narración chars/segundo. Fallback razonable si ffprobe
    # falló (devolvió 0.0): ~13 cps que es la media empírica de Gabo ES
    # (default desde 2026-04-27; Luis era ~17 cps, más rápido).
    cps = narration_chars / narration_duration if narration_duration > 0 else 13.0

    # Detectar capítulos sobre el texto narrativo.
    chapters_raw = detect_chapters(text)
    # Offset = intro + sil_after_intro + título + sil_after_title (canon
    # 2026-04-28 PM: la narración empieza tras el frontispicio sonoro).
    narration_start = (intro_duration + silence_after_intro
                       + title_duration + silence_after_title)
    chapters = [
        {
            "number": ch["number"],
            "title": ch["title"],
            "start_seconds": round(narration_start + ch["char_position"] / cps, 2),
        }
        for ch in chapters_raw
    ]

    # Si no se detectó ningún capítulo (relato sin "Uno. Dos. Tres."),
    # generamos un único chapter sintético "Relato" para que YouTube
    # tenga al menos 1 entry de chapters válida (requiere ≥3 entries
    # para auto-generar chapters reales — pero un solo entry no rompe).
    if not chapters:
        chapters = [{
            "number": 1,
            "title": "Relato",
            "start_seconds": round(narration_start, 2),
        }]

    # Estructura JSON final. Versionada por si downstream cambia
    # parsing y necesita compatibilidad hacia atrás.
    return {
        "schema_version": 3,  # bump: añade title_* fields desde 2026-04-28 PM
        "slug": slug,
        "total_duration_seconds": round(total_duration, 2),
        "intro_duration_seconds": round(intro_duration, 2),
        "silence_after_intro_seconds": round(silence_after_intro, 2),
        "title_text": title_text,
        "title_duration_seconds": round(title_duration, 2),
        "silence_after_title_seconds": round(silence_after_title, 2),
        "silence_before_outro_seconds": round(silence_before_outro, 2),
        "outro_duration_seconds": round(outro_duration, 2),
        "narration_duration_seconds": round(narration_duration, 2),
        "narration_chars": narration_chars,
        "narration_chars_per_second": round(cps, 2),
        "chunks": [
            {
                "index": i + 1,
                "file_relative": str(cf.relative_to(REPO_ROOT)).replace("\\", "/"),
                "duration_seconds": round(chunk_durations[i], 2),
                "char_count": len(chunks[i]),
            }
            for i, cf in enumerate(chunk_files)
        ],
        "chapters": chapters,
    }


def upload_to_r2(env: dict, local_path: Path, key: str) -> str:
    """Sube el MP3 a Cloudflare R2. Devuelve la URL pública."""
    s3 = boto3.client(
        "s3",
        endpoint_url=f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
        aws_access_key_id=env["R2_ACCESS_KEY"],
        aws_secret_access_key=env["R2_SECRET_KEY"],
        region_name="auto",
        config=Config(signature_version="s3v4"),
    )
    print(f"  Subiendo a R2: s3://{env['R2_BUCKET']}/{key}...", flush=True)
    s3.upload_file(
        Filename=str(local_path),
        Bucket=env["R2_BUCKET"],
        Key=key,
        # ContentType audio/mpeg es crucial para que el <audio> HTML5 lo
        # reconozca como MP3 y no caiga en octet-stream (que algunos
        # navegadores rechazan para streaming).
        ExtraArgs={"ContentType": "audio/mpeg"},
    )
    return f"{env['R2_PUBLIC_URL'].rstrip('/')}/{key}"


# ══════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════

def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(
            f"Uso: python {sys.argv[0]} <path/audiolibro.txt> <slug> <title>\n"
            f"Ejemplo: python utilities/generate_audio.py "
            f"content/ficciones/_one-shots/el-cristalero/audiolibro.txt "
            f"el-cristalero \"El cristalero\"\n\n"
            f"<title> = `title:` corto del frontmatter del relato (ej: "
            f"\"El cristalero\"). Se lee como tarjeta de título entre el "
            f"bumper Luis y el cuerpo del relato. NO usar `display_title:` "
            f"declarativo largo. Canon obligatorio desde 2026-04-28 PM."
        )
    input_file = Path(sys.argv[1])
    slug = sys.argv[2]
    title_text = sys.argv[3].strip()
    if not input_file.exists():
        sys.exit(f"ERROR: no existe {input_file}")
    if not INTRO_MP3.exists():
        sys.exit(f"ERROR: falta {INTRO_MP3}")
    if not OUTRO_MP3.exists():
        sys.exit(f"ERROR: falta {OUTRO_MP3}")
    if not title_text:
        sys.exit("ERROR: <title> vacío. Pasa el `title:` corto del frontmatter.")

    env = load_env()
    ffmpeg = find_ffmpeg()

    # Carga y chunking
    text = input_file.read_text(encoding="utf-8").strip()
    # Safety-net: normaliza marca a 'ROBO, OGAR' antes del TTS aunque el
    # skill /audiobook-generate ya debería haberlo aplicado al construir
    # audiolibro.txt. Idempotente.
    text = apply_tts_brand_substitutions(text)

    # Guardia de detección de capítulos ANTES del TTS — si el regex estricto
    # se ha quedado corto ante una convención nueva (`¿Jugamos?` con `?`,
    # `Madrid, un martes a las...` con coma, etc.) abort aquí y no gastamos
    # créditos. Imprime los headings perdidos para debugging inmediato.
    # Origen 2026-04-27 tras el bug pipo (3/6 capítulos detectados sin aviso).
    assert_no_chapters_lost(text)

    chunks = chunk_text(text)
    # total_chars incluye el título (frontispicio sonoro extra) — el TTS del
    # anuncio cuesta créditos también. Despreciable (~10-30 chars) pero
    # correcto para que pre_check / cost_estimate / record_usage no mientan.
    body_chars = sum(len(c) for c in chunks)
    total_chars = body_chars + len(title_text) + 1  # +1 por punto final auto-añadido
    print(f"Texto: {len(text):,} chars totales (body {body_chars:,} + título "
          f"~{total_chars - body_chars}).")
    print(f"Dividido en {len(chunks)} chunk(s):")
    for i, c in enumerate(chunks):
        preview = c.replace("\n", " ")[:60]
        print(f"  chunk {i+1}: {len(c):,} chars | '{preview}...'")
    print()

    # Cost estimate — orientativo, asumimos overage rate
    cost_usd = total_chars / 1000 * 0.10
    print(f"Estimación coste: ${cost_usd:.2f} (en cuota Starter: ~{total_chars/60000*100:.1f}% del mes)")
    print()

    # Pre-check del contador local de saldo ElevenLabs. Si el contador
    # detecta saldo insuficiente para los total_chars del relato, abortamos
    # ANTES de gastar el primer chunk (los chunks parciales no son
    # recuperables si la cuota se agota mid-pipeline — incidente origen
    # 2026-04-25 con la-objecion).
    # `--force` (env var ROBOHOGAR_ELEVENLABS_FORCE=1) salta el bloqueo si
    # Rafael acaba de pagar overage y el contador aún no lo refleja.
    force = os.environ.get("ROBOHOGAR_ELEVENLABS_FORCE", "").strip() in ("1", "true", "yes")
    ok, msg = pre_check(chars=total_chars)
    print(f"Contador saldo: {msg}")
    if not ok and not force:
        sys.exit(
            "\n[ABORT] Saldo insuficiente según contador local. "
            "Si has pagado overage o quieres ignorar el bloqueo, re-ejecuta con "
            "ROBOHOGAR_ELEVENLABS_FORCE=1. Si es error del contador, actualízalo "
            "con `python utilities/elevenlabs_balance.py set --credits N`."
        )
    print()

    # Directorio temp para chunks — persistente entre runs para facilitar debug.
    tmp_dir = REPO_ROOT / "assets" / "audio" / "ficciones" / f"_chunks-{slug}"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    # TTS por chunk con contexto adyacente para prosodia coherente.
    chunk_files: list[Path] = []
    print("Generando narración chunk a chunk:")
    for i, chunk in enumerate(chunks):
        prev = chunks[i - 1] if i > 0 else ""
        nxt = chunks[i + 1] if i < len(chunks) - 1 else ""
        audio_bytes = call_elevenlabs_tts(
            env["ELEVENLABS_API_KEY"], chunk, i, len(chunks),
            prev_text=prev, next_text=nxt,
        )
        chunk_file = tmp_dir / f"chunk-{i + 1:02d}.mp3"
        chunk_file.write_bytes(audio_bytes)
        chunk_files.append(chunk_file)
    print()

    # TTS extra del anuncio del título (frontispicio sonoro). Coste mínimo
    # (~10-30 chars adicionales) y obligatorio desde 2026-04-28 PM. Voice
    # settings y previous_text simulado los maneja synthesize_title_announce.
    print(f"Generando anuncio del título: '{title_text}'")
    title_bytes = synthesize_title_announce(env["ELEVENLABS_API_KEY"], title_text)
    title_file = tmp_dir / "_title_announce.mp3"
    title_file.write_bytes(title_bytes)
    print()

    # Concatenación: intro + sil_after_intro + título + sil_after_title +
    # chunks cuerpo + sil_before_outro + outro.
    final_dir = REPO_ROOT / "assets" / "audio" / "ficciones"
    final_dir.mkdir(parents=True, exist_ok=True)
    final_mp3 = final_dir / f"{slug}.mp3"
    concat_with_ffmpeg(
        ffmpeg,
        INTRO_MP3, SILENCE_AFTER_INTRO_SEC,
        title_file, SILENCE_AFTER_TITLE_SEC,
        chunk_files,
        SILENCE_BEFORE_OUTRO_SEC, OUTRO_MP3,
        final_mp3,
    )
    duration = probe_duration(ffmpeg, final_mp3)
    print(f"  -> {final_mp3.name}: {final_mp3.stat().st_size / 1024:,.0f} KB, "
          f"duración {duration / 60:.1f} min ({duration:.1f}s)")
    print()

    # Construcción del chunks-index.json con timestamps de capítulos
    # mapeados a segundos del MP3 final. Lo consume `/audiobook-distribute`
    # para componer chyrons del MP4 YouTube + chapters de descripción +
    # show notes RSS. Se escribe antes del upload R2 — si falla el upload,
    # el JSON queda disponible para reintentar la subida sin regenerar.
    intro_dur = probe_duration(ffmpeg, INTRO_MP3)
    outro_dur = probe_duration(ffmpeg, OUTRO_MP3)
    title_dur = probe_duration(ffmpeg, title_file)
    index_data = build_chunks_index(
        slug=slug, text=text, chunks=chunks, chunk_files=chunk_files,
        ffmpeg=ffmpeg,
        intro_duration=intro_dur,
        silence_after_intro=SILENCE_AFTER_INTRO_SEC,
        title_text=title_text,
        title_duration=title_dur,
        silence_after_title=SILENCE_AFTER_TITLE_SEC,
        silence_before_outro=SILENCE_BEFORE_OUTRO_SEC,
        outro_duration=outro_dur,
        total_duration=duration,
    )
    index_file = final_dir / f"{slug}-chunks-index.json"
    index_file.write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    n_chapters = len(index_data["chapters"])
    print(f"  -> chunks-index.json escrito ({n_chapters} capítulo(s) detectado(s)):")
    for ch in index_data["chapters"]:
        m, s = divmod(int(ch["start_seconds"]), 60)
        print(f"     {m:02d}:{s:02d} · {ch['number']}. {ch['title']}")
    print()

    # Subida a R2 → URL pública.
    public_url = upload_to_r2(env, final_mp3, f"{slug}.mp3")

    # Registrar consumo en el contador local. Llegamos aquí solo si TTS +
    # concat + upload pasaron — así no contabilizamos generaciones que
    # fallaron a mitad. El balance se decrementa por chars * ratio configurado.
    usage_event = record_usage(slug=slug, chars=total_chars)
    print(f"Saldo ElevenLabs tras generación: {usage_event['credits_after']:,} "
          f"créditos (decrementado en {usage_event['credits_estimated']:,}).")

    print()
    print("=" * 72)
    print(f"AUDIOLIBRO GENERADO · {slug}")
    print("=" * 72)
    print(f"MP3 local      : {final_mp3}")
    print(f"URL pública    : {public_url}")
    print(f"Duración       : {duration / 60:.1f} min")
    print(f"Chunks         : {len(chunks)} (temp en {tmp_dir.relative_to(REPO_ROOT)})")
    print(f"Chapters index : {index_file.relative_to(REPO_ROOT)}")
    print(f"Capítulos      : {n_chapters} detectado(s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
