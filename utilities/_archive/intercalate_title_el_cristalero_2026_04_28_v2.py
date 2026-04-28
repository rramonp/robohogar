"""
One-shot v2: regenera SOLO el chunk de título con parámetros prosódicos
ajustados para evitar entonación de "frase incompleta" en TTS muy corto.

Cambios vs v1 (intercalate_title_el_cristalero_2026_04_28.py):
  - previous_text="Ficciones de ROBO, OGAR." simulando el cierre real del
    bumper Luis. Sin esto, el modelo Multilingual v2 lee "El cristalero."
    como si fuera el inicio de una frase que continúa.
  - voice_settings.style = 0.5 (default 0.0): más expresividad de anuncio.
  - voice_settings.stability = 0.4 (default 0.5): más variación prosódica
    para que el cierre de "cristalero." baje en pitch como un título.

Reutiliza:
  - intro_part.mp3 ya cortado en c:\\tmp\\cristalero-title-fix (4.53s,
    intro Luis + 2s silencio).
  - body_part.mp3 ya cortado (1369.63s, cuerpo + 3s + outro).

Solo regenera title.mp3 + concat final + upload R2.
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generate_audio import (  # noqa: E402
    VOICE_ID,
    MODEL_ID,
    OUTPUT_FORMAT,
    REPO_ROOT,
    load_env,
    find_ffmpeg,
    upload_to_r2,
    probe_duration,
    detect_chapters,
)
from elevenlabs_balance import pre_check, record_usage  # noqa: E402

# Reusa el script v1 para concat_with_ffmpeg / cut helpers.
from intercalate_title_el_cristalero_2026_04_28 import ffmpeg_concat  # noqa: E402


SLUG = "el-cristalero"
TITLE_TEXT = "El cristalero."
SILENCE_AFTER_TITLE_SEC = 2.0
R2_KEY = f"{SLUG}.mp3"
TMP_DIR = Path("c:/tmp/cristalero-title-fix")

# Cierre del bumper Luis canónico: "Una Ficción Doméstica de ROBO, OGAR."
# Esto le dice al modelo: lo que sigue NO es continuación; viene tras un
# punto declarativo. La marca con coma sigue la convención TTS canon.
PREV_TEXT_BUMPER_CLOSE = "Una Ficción Doméstica de ROBO, OGAR."


def call_tts_announce(api_key: str, text: str, prev_text: str) -> bytes:
    """TTS con voice_settings ajustados para entonación de anuncio.

    style 0.5 vs 0.0 (default narración íntima) → da expresividad de
    presentación: el modelo aplica patrón "tarjeta de título" en lugar de
    "frase narrativa neutra".

    stability 0.4 vs 0.5 → suficiente variación para que la prosodia caiga
    al final del título como cierre, en lugar de quedar suspendida.

    similarity_boost y use_speaker_boost se mantienen idénticos al cuerpo
    (queremos la misma identidad vocal Gabo, solo cambia el "modo" expresivo).
    """
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
        "previous_text": prev_text,
        # Sin next_text — queremos que el cierre prosódico del título baje
        # como final declarativo. Si pusiéramos next_text="Parte uno..." el
        # modelo encadenaría sin pausa.
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
    print(f"  TTS announce ({len(text)} chars, prev='{prev_text[:30]}...', "
          f"style=0.5 stability=0.4)...", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            audio = resp.read()
        print(f"    -> {len(audio):,} bytes", flush=True)
        return audio
    except urllib.error.HTTPError as e:
        body_snip = e.read().decode("utf-8", errors="replace")[:300]
        sys.exit(f"  FAIL HTTP {e.code}: {body_snip}")


def main() -> None:
    print(f"Regenerando título '{TITLE_TEXT}' con prosodia de anuncio...")
    print()

    env = load_env()
    ffmpeg = find_ffmpeg()

    intro_part = TMP_DIR / "intro_part.mp3"
    body_part = TMP_DIR / "body_part.mp3"
    if not intro_part.exists() or not body_part.exists():
        sys.exit(f"ERROR: faltan {intro_part} o {body_part}. Corre v1 primero.")

    # TTS del título con prosodia de anuncio.
    chars = len(TITLE_TEXT)
    ok, msg = pre_check(chars=chars)
    print(f"Saldo: {msg}")
    if not ok:
        sys.exit("Saldo insuficiente.")

    title_bytes = call_tts_announce(
        env["ELEVENLABS_API_KEY"],
        TITLE_TEXT,
        prev_text=PREV_TEXT_BUMPER_CLOSE,
    )
    title_mp3 = TMP_DIR / "title_v2.mp3"
    title_mp3.write_bytes(title_bytes)
    title_dur = probe_duration(ffmpeg, title_mp3)
    print(f"  title_v2.mp3: {title_dur:.2f}s")
    print()

    # Concat final.
    final_mp3 = TMP_DIR / "el-cristalero-final-v2.mp3"
    ffmpeg_concat(
        ffmpeg,
        parts=[intro_part, title_mp3, body_part],
        silence_durations={1: SILENCE_AFTER_TITLE_SEC},
        dest=final_mp3,
    )
    final_dur = probe_duration(ffmpeg, final_mp3)
    print(f"  final v2: {final_dur:.2f}s ({final_dur/60:.1f} min)")
    print()

    # Subir a R2 (sobrescribe).
    print("Subiendo a R2 (sobrescribe el-cristalero.mp3)...")
    public_url = upload_to_r2(env, final_mp3, R2_KEY)
    print(f"  -> {public_url}")
    print()

    # Recalcular chunks-index.json (mismo cálculo que v1 pero con title_dur nuevo).
    intro_mp3 = REPO_ROOT / "assets" / "audio" / "intro-ficciones.mp3"
    outro_mp3 = REPO_ROOT / "assets" / "audio" / "outro-ficciones.mp3"
    intro_dur = probe_duration(ffmpeg, intro_mp3)
    outro_dur = probe_duration(ffmpeg, outro_mp3)
    sil_after_intro = 2.0
    sil_before_outro = 3.0

    audiolibro_txt = (REPO_ROOT / "content" / "ficciones" / "_one-shots"
                      / SLUG / "audiolibro.txt")
    text = audiolibro_txt.read_text(encoding="utf-8").strip()
    chapters_raw = detect_chapters(text)

    narration_dur = (final_dur - intro_dur - sil_after_intro - title_dur
                     - SILENCE_AFTER_TITLE_SEC - sil_before_outro - outro_dur)
    narration_chars = len(text)
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
        "chunks": [],
        "chapters": chapters,
    }

    index_file = (REPO_ROOT / "assets" / "audio" / "ficciones"
                  / f"{SLUG}-chunks-index.json")
    index_file.write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8",
    )
    print(f"chunks-index.json actualizado:")
    for ch in chapters:
        m, s = divmod(int(ch["start_seconds"]), 60)
        print(f"    {m:02d}:{s:02d} · {ch['number']}. {ch['title']}")
    print()

    record_usage(slug=f"{SLUG}-title-v2", chars=chars)
    print("=" * 72)
    print(f"OK · título regenerado con prosodia de anuncio")
    print(f"R2 URL: {public_url}")
    print("=" * 72)


if __name__ == "__main__":
    main()
