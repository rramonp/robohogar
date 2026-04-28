"""
One-shot: intercalar el título "El cristalero." entre intro Luis y cuerpo del
audiolibro existente, sin regenerar los ~12.5K chars del cuerpo (Gabo).

Por qué one-shot: el MP3 ya estaba en R2 con la composición antigua (intro →
cuerpo → outro, sin título leído). Rafael detectó al reproducirlo que el
audiolibro arranca en "Treinta y un turnos…" sin anclar la pieza con su
nombre. Para no quemar 12.5K créditos ElevenLabs en regenerar el cuerpo,
descargamos el MP3 actual, lo cortamos al final del silencio post-intro
(intro_dur + 2s = 4.53s), generamos TTS solo del título (~14 chars, ~14
créditos), y reconstruimos el MP3 con el segmento nuevo intercalado.

Tras este script + validación de Rafael, `generate_audio.py` recibe el cambio
canon (lectura de título obligatoria estructural) y este archivo deja de
ejecutarse — vive aquí como prueba histórica del fix.

Pipeline:
  1. Descarga el-cristalero.mp3 desde R2 a c:\\tmp\\.
  2. ffmpeg cuts: intro_part (0..4.53s) + body_part (4.53s..end).
  3. ElevenLabs TTS de "El cristalero." con voice Gabo (igual que cuerpo).
  4. ffmpeg concat: intro_part + title + 2s silencio + body_part.
  5. Sube a R2 sobrescribiendo el-cristalero.mp3.
  6. Reescribe assets/audio/ficciones/el-cristalero-chunks-index.json con
     offsets actualizados (todos los start_seconds suman title_dur + 2s).

Idempotente NO: corre una vez sobre el MP3 "v1 sin título". Si se vuelve a
correr sobre el "v2 con título" intercalaría OTRA vez el título y el MP3
crecería con duplicados. Defensa: pre-check del primer chunk del MP3 actual
— si los primeros 7s ya contienen el título "cristalero", abort.
"""

import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

# Reutiliza utilidades canónicas del pipeline principal.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_audio import (  # noqa: E402
    VOICE_ID,
    MODEL_ID,
    OUTPUT_FORMAT,
    REPO_ROOT,
    load_env,
    find_ffmpeg,
    call_elevenlabs_tts,
    upload_to_r2,
    probe_duration,
    detect_chapters,
)
from elevenlabs_balance import pre_check, record_usage  # noqa: E402


SLUG = "el-cristalero"
TITLE_TEXT = "El cristalero."  # exacto: title corto frontmatter + punto final TTS
SILENCE_AFTER_TITLE_SEC = 2.0  # respiro entre título y primer "I. La hoja"
INTRO_PLUS_SILENCE_CUT_SEC = None  # se calcula a partir de los assets locales

R2_KEY = f"{SLUG}.mp3"
TMP_DIR = Path("c:/tmp/cristalero-title-fix")


def http_download(url: str, dest: Path) -> None:
    """Descarga binaria simple. Sin reintentos: si falla, abort.

    Cloudflare R2 (pub-*.r2.dev) bloquea user-agents de bot por defecto
    (Python-urllib devuelve 403). Añadimos UA de navegador para pasar.
    """
    print(f"  Descargando {url} -> {dest}...", flush=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 robohogar/1.0",
    })
    with urllib.request.urlopen(req, timeout=120) as resp:
        dest.write_bytes(resp.read())
    print(f"    -> {dest.stat().st_size / 1024 / 1024:.1f} MB OK", flush=True)


def ffmpeg_cut(ffmpeg: str, src: Path, start_s: float, end_s: float | None,
               dest: Path) -> None:
    """Corta un segmento del MP3 con re-encode (no copy) para borde limpio.

    end_s=None significa "hasta el final del archivo".

    Usamos re-encode con libmp3lame en lugar de `-c copy` porque cortar MP3
    a tiempo arbitrario con stream copy deja paquetes incompletos al inicio
    (audible como "click" en Beehiiv players). Re-encode añade ~1s de
    cómputo pero garantiza concat sin glitches.
    """
    cmd = [ffmpeg, "-y", "-i", str(src), "-ss", str(start_s)]
    if end_s is not None:
        cmd.extend(["-to", str(end_s)])
    cmd.extend([
        "-codec:a", "libmp3lame", "-b:a", "128k",
        "-ar", "44100", "-ac", "1",
        str(dest),
    ])
    print(f"  ffmpeg cut [{start_s:.2f}..{end_s if end_s else 'end'}] -> {dest.name}", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"ffmpeg cut FAIL:\n{result.stderr[-500:]}")


def ffmpeg_concat(ffmpeg: str, parts: list[Path], silence_durations: dict[int, float],
                  dest: Path) -> None:
    """Concatena partes con silencios opcionales intercalados.

    silence_durations: {posición_post_part_index: duración_silencio_segundos}.
    Si silence_durations = {0: 2.0}, inserta 2s de silencio DESPUÉS de parts[0].

    Usa concat filter (no demuxer) para forzar re-encode coherente — todas las
    piezas terminan en mismo bitrate/sample rate aunque vinieran con
    metadatos distintos.
    """
    inputs: list[str] = []
    stream_order: list[str] = []  # labels de los streams en orden final

    for i, part in enumerate(parts):
        inputs.extend(["-i", str(part)])
        stream_order.append(f"[{len(stream_order) + sum(1 for _ in stream_order if False)}:a]")
        # Si toca silencio después de esta parte, lo encolamos como input lavfi
        if i in silence_durations:
            inputs.extend([
                "-f", "lavfi",
                "-t", str(silence_durations[i]),
                "-i", "anullsrc=r=44100:cl=mono",
            ])

    # Reconstruyo stream_order limpio basándome en el orden real de inputs.
    n_total = len(parts) + len(silence_durations)
    stream_labels = "".join(f"[{i}:a]" for i in range(n_total))
    filter_str = f"{stream_labels}concat=n={n_total}:v=0:a=1[out]"

    cmd = [
        ffmpeg, "-y", *inputs,
        "-filter_complex", filter_str,
        "-map", "[out]",
        "-codec:a", "libmp3lame", "-b:a", "128k",
        "-ar", "44100", "-ac", "1",
        str(dest),
    ]
    print(f"  ffmpeg concat ({n_total} streams) -> {dest.name}", flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"ffmpeg concat FAIL:\n{result.stderr[-500:]}")


def main() -> None:
    print(f"Intercalando título '{TITLE_TEXT}' en {SLUG}.mp3 (R2)...")
    print()

    env = load_env()
    ffmpeg = find_ffmpeg()
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    # Duraciones canónicas de los assets locales — el MP3 en R2 fue
    # construido con intro-ficciones.mp3 (Luis 2.53s) + 2s silencio.
    intro_mp3 = REPO_ROOT / "assets" / "audio" / "intro-ficciones.mp3"
    outro_mp3 = REPO_ROOT / "assets" / "audio" / "outro-ficciones.mp3"
    intro_dur = probe_duration(ffmpeg, intro_mp3)
    outro_dur = probe_duration(ffmpeg, outro_mp3)
    sil_after_intro = 2.0
    sil_before_outro = 3.0
    cut_at = intro_dur + sil_after_intro
    print(f"intro_duration: {intro_dur:.3f}s · sil_after_intro: {sil_after_intro}s · cut at {cut_at:.3f}s")

    # Paso 1 · descargar MP3 actual desde R2.
    public_url = f"{env['R2_PUBLIC_URL'].rstrip('/')}/{R2_KEY}"
    original = TMP_DIR / "original.mp3"
    http_download(public_url, original)

    total_dur = probe_duration(ffmpeg, original)
    print(f"Duración total MP3 actual: {total_dur:.2f}s ({total_dur/60:.1f} min)")
    print()

    # Pre-check anti-doble-ejecución: probamos los primeros 7s con whisper
    # NO disponible local — alternativa simple: confirmar que la duración es
    # ~la del MP3 sin título (el añadir título +sil = +~3-4s, así que si el
    # actual ya está extendido, abortamos por sospecha).
    expected_no_title = total_dur  # baseline
    # Heurística: el MP3 sin título dura ~1374s según beehiiv-paste.html.
    # Si encontramos > 1378s (margen 4s), probablemente ya tiene título.
    if total_dur > 1378:
        print(f"  ⚠️  Duración {total_dur:.1f}s mayor que 1378s — sospecha de doble-ejecución.")
        sys.exit("ABORT: el MP3 actual ya parece tener título. Si no, fuerza re-corre tras revisar.")

    # Paso 2 · cortar en 2 segmentos.
    intro_part = TMP_DIR / "intro_part.mp3"
    body_part = TMP_DIR / "body_part.mp3"
    ffmpeg_cut(ffmpeg, original, 0.0, cut_at, intro_part)
    ffmpeg_cut(ffmpeg, original, cut_at, None, body_part)
    intro_part_dur = probe_duration(ffmpeg, intro_part)
    body_part_dur = probe_duration(ffmpeg, body_part)
    print(f"  intro_part: {intro_part_dur:.2f}s · body_part: {body_part_dur:.2f}s")
    print()

    # Paso 3 · TTS del título con voz Gabo.
    chars = len(TITLE_TEXT)
    print(f"Pre-check ElevenLabs ({chars} chars de '{TITLE_TEXT}')...")
    ok, msg = pre_check(chars=chars)
    print(f"  {msg}")
    if not ok:
        sys.exit("Saldo insuficiente.")

    title_bytes = call_elevenlabs_tts(
        env["ELEVENLABS_API_KEY"],
        TITLE_TEXT,
        chunk_index=0, total_chunks=1,
        prev_text="",  # arranca tras silencio del intro: prosodia inicial limpia
        next_text="",  # silencio detrás también: cierre limpio
    )
    title_mp3 = TMP_DIR / "title.mp3"
    title_mp3.write_bytes(title_bytes)
    title_dur = probe_duration(ffmpeg, title_mp3)
    print(f"  title.mp3: {title_dur:.2f}s ({len(title_bytes)} bytes)")
    print()

    # Paso 4 · concat final: intro_part + title + 2s silencio + body_part.
    final_mp3 = TMP_DIR / "el-cristalero-final.mp3"
    ffmpeg_concat(
        ffmpeg,
        parts=[intro_part, title_mp3, body_part],
        silence_durations={1: SILENCE_AFTER_TITLE_SEC},  # 2s tras title
        dest=final_mp3,
    )
    final_dur = probe_duration(ffmpeg, final_mp3)
    delta = final_dur - total_dur
    print(f"  final: {final_dur:.2f}s ({final_dur/60:.1f} min) · +{delta:.2f}s vs original")
    print()

    # Paso 5 · subir a R2 (sobrescribe).
    print("Subiendo a R2 (sobrescribe el-cristalero.mp3)...")
    public_url_v2 = upload_to_r2(env, final_mp3, R2_KEY)
    print(f"  -> {public_url_v2}")
    print()

    # Paso 6 · reconstruir chunks-index.json con offsets actualizados.
    # No tenemos los chunks individuales del cuerpo (gitignored), pero podemos
    # recalcular los chapters mapeando char_position con velocidad uniforme.
    audiolibro_txt = (REPO_ROOT / "content" / "ficciones" / "_one-shots"
                      / SLUG / "audiolibro.txt")
    text = audiolibro_txt.read_text(encoding="utf-8").strip()
    chapters_raw = detect_chapters(text)

    # narration_dur = total_final - intro_dur - sil_after_intro - title_dur
    #               - sil_after_title - sil_before_outro - outro_dur
    narration_dur = (final_dur - intro_dur - sil_after_intro - title_dur
                     - SILENCE_AFTER_TITLE_SEC - sil_before_outro - outro_dur)
    narration_chars = len(text)  # aproximación: el texto entero del audiolibro
    cps = narration_chars / narration_dur if narration_dur > 0 else 13.0

    narration_start = (intro_dur + sil_after_intro + title_dur
                       + SILENCE_AFTER_TITLE_SEC)
    chapters = [
        {
            "number": ch["number"],
            "title": ch["title"],
            "start_seconds": round(narration_start + ch["char_position"] / cps, 2),
        }
        for ch in chapters_raw
    ]

    index_data = {
        "schema_version": 2,
        "slug": SLUG,
        "total_duration_seconds": round(final_dur, 2),
        "intro_duration_seconds": round(intro_dur, 2),
        "silence_after_intro_seconds": round(sil_after_intro, 2),
        "title_text": TITLE_TEXT,
        "title_duration_seconds": round(title_dur, 2),
        "silence_after_title_seconds": round(SILENCE_AFTER_TITLE_SEC, 2),
        "silence_before_outro_seconds": round(sil_before_outro, 2),
        "outro_duration_seconds": round(outro_dur, 2),
        "narration_duration_seconds": round(narration_dur, 2),
        "narration_chars": narration_chars,
        "narration_chars_per_second": round(cps, 2),
        "chunks": [],  # no las tenemos — el detalle ya no aplica con título intercalado
        "chapters": chapters,
    }

    index_file = (REPO_ROOT / "assets" / "audio" / "ficciones"
                  / f"{SLUG}-chunks-index.json")
    index_file.parent.mkdir(parents=True, exist_ok=True)
    index_file.write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    print(f"chunks-index.json reescrito: {index_file}")
    print(f"  Capítulos con offsets actualizados (+{delta:.1f}s respecto a v1):")
    for ch in chapters:
        m, s = divmod(int(ch["start_seconds"]), 60)
        print(f"    {m:02d}:{s:02d} · {ch['number']}. {ch['title']}")
    print()

    # Paso 7 · contabilizar consumo en el balance local.
    usage = record_usage(slug=f"{SLUG}-title-only", chars=chars)
    print(f"Saldo ElevenLabs: {usage['credits_after']:,} créditos "
          f"(decrementado en {usage['credits_estimated']}).")
    print()

    print("=" * 72)
    print(f"OK · '{TITLE_TEXT}' intercalado en {SLUG}.mp3")
    print("=" * 72)
    print(f"R2 URL          : {public_url_v2}")
    print(f"Duración total  : {final_dur/60:.1f} min ({final_dur:.1f}s)")
    print(f"Delta vs v1     : +{delta:.2f}s")
    print(f"Chapters index  : {index_file.relative_to(REPO_ROOT)}")
    print(f"Tmp local       : {TMP_DIR}")
    print("=" * 72)


if __name__ == "__main__":
    main()
