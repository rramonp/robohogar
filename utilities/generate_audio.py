"""
Generate audiobook MP3 for a Ficciones Domésticas relato.

Pipeline end-to-end:
  1. Lee `audiolibro.txt` TTS-optimizado del relato.
  2. Divide en chunks por párrafos respetando el límite ~4500 chars/request
     del plan Starter ElevenLabs.
  3. Llama `/v1/text-to-speech/{voice_id}` por cada chunk con voz Luis
     (GojDwihhnL1f7RrBuXsJ) y modelo Multilingual v2. Pasa previous_text /
     next_text para mantener prosodia coherente entre chunks.
  4. Concatena con ffmpeg: intro + 2s silencio + chunks narración + outro,
     recodificando todo a 44.1kHz mono 128kbps MP3 consistente.
  5. Sube el MP3 final a Cloudflare R2 bucket (ContentType audio/mpeg)
     y devuelve la URL pública.

Uso:
    python utilities/generate_audio.py <audiolibro.txt> <slug>

Ejemplo:
    python utilities/generate_audio.py \
        content/ficciones/_one-shots/el-que-viene-a-tomar-cafe/audiolibro.txt \
        el-que-viene-a-tomar-cafe

Requisitos:
  - `.claude/settings.local.json` con ELEVENLABS_API_KEY + R2_* (5 vars).
  - `boto3` instalado (pip install boto3).
  - ffmpeg accesible vía PATH o WinGet install path Gyan.FFmpeg*.
  - `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` pregenerados.

Idempotencia: los chunks temporales se guardan en
`assets/audio/ficciones/_chunks-<slug>/` — sirven para debug si el audio
sale raro, y se pueden borrar a mano al confirmar que el MP3 final va bien.
"""

import glob
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

import boto3
from botocore.client import Config


# Decisiones canon del plan audiolibros (docs/plan-audiolibros-ficciones.md).
VOICE_ID = "GojDwihhnL1f7RrBuXsJ"  # Luis — Polished, Mature and Credible
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
            # similarity_boost 0.75: mantiene tono de la voz Luis sin perder
            # naturalidad (1.0 suena robótico en narrativa larga)
            "similarity_boost": 0.75,
            # style 0.0: narración natural, sin exagerar tono emocional
            "style": 0.0,
            # speaker_boost True: refuerza identidad de Luis entre chunks
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
# Concatenación y subida
# ══════════════════════════════════════════════════════════════════════════

def concat_with_ffmpeg(
    ffmpeg: str,
    intro: Path,
    silence_sec: float,
    chunk_files: list[Path],
    outro: Path,
    output: Path,
) -> None:
    """Concatena todas las piezas en un MP3 final consistente.

    Usa el concat filter (no el concat demuxer) porque permite recodificar
    todo a un sample rate / bitrate uniforme — evita el glitch de pops o
    variaciones de loudness entre secciones con bitrates distintos.

    Pipeline de streams:
      intro -> [0:a]
      silencio 2s -> [1:a]
      chunk1 -> [2:a]
      chunk2 -> [3:a]
      ...
      outro -> [N:a]
    """
    inputs: list[str] = ["-i", str(intro), "-f", "lavfi",
                          "-t", str(silence_sec),
                          "-i", "anullsrc=r=44100:cl=mono"]
    for cf in chunk_files:
        inputs.extend(["-i", str(cf)])
    inputs.extend(["-i", str(outro)])

    # n_total = intro (1) + silencio (1) + chunks (N) + outro (1)
    n_total = 2 + len(chunk_files) + 1
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
    if len(sys.argv) != 3:
        sys.exit(
            f"Uso: python {sys.argv[0]} <path/audiolibro.txt> <slug>\n"
            f"Ejemplo: python utilities/generate_audio.py "
            f"content/ficciones/_one-shots/<slug>/audiolibro.txt <slug>"
        )
    input_file = Path(sys.argv[1])
    slug = sys.argv[2]
    if not input_file.exists():
        sys.exit(f"ERROR: no existe {input_file}")
    if not INTRO_MP3.exists():
        sys.exit(f"ERROR: falta {INTRO_MP3}")
    if not OUTRO_MP3.exists():
        sys.exit(f"ERROR: falta {OUTRO_MP3}")

    env = load_env()
    ffmpeg = find_ffmpeg()

    # Carga y chunking
    text = input_file.read_text(encoding="utf-8").strip()
    chunks = chunk_text(text)
    total_chars = sum(len(c) for c in chunks)
    print(f"Texto: {len(text):,} chars totales ({total_chars:,} en chunks).")
    print(f"Dividido en {len(chunks)} chunk(s):")
    for i, c in enumerate(chunks):
        preview = c.replace("\n", " ")[:60]
        print(f"  chunk {i+1}: {len(c):,} chars | '{preview}...'")
    print()

    # Cost estimate — orientativo, asumimos overage rate
    cost_usd = total_chars / 1000 * 0.10
    print(f"Estimación coste: ${cost_usd:.2f} (en cuota Starter: ~{total_chars/60000*100:.1f}% del mes)")
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

    # Concatenación con intro + 2s silencio + chunks + outro.
    final_dir = REPO_ROOT / "assets" / "audio" / "ficciones"
    final_dir.mkdir(parents=True, exist_ok=True)
    final_mp3 = final_dir / f"{slug}.mp3"
    concat_with_ffmpeg(
        ffmpeg, INTRO_MP3, SILENCE_AFTER_INTRO_SEC, chunk_files, OUTRO_MP3, final_mp3,
    )
    duration = probe_duration(ffmpeg, final_mp3)
    print(f"  -> {final_mp3.name}: {final_mp3.stat().st_size / 1024:,.0f} KB, "
          f"duración {duration / 60:.1f} min ({duration:.1f}s)")
    print()

    # Subida a R2 → URL pública.
    public_url = upload_to_r2(env, final_mp3, f"{slug}.mp3")

    print()
    print("=" * 72)
    print(f"AUDIOLIBRO GENERADO · {slug}")
    print("=" * 72)
    print(f"MP3 local : {final_mp3}")
    print(f"URL pública: {public_url}")
    print(f"Duración  : {duration / 60:.1f} min")
    print(f"Chunks    : {len(chunks)} (temp en {tmp_dir.relative_to(REPO_ROOT)})")
    print("=" * 72)


if __name__ == "__main__":
    main()
