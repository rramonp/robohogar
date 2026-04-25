"""
Reconstruye chunks-index.json para 'el-que-viene-a-tomar-cafe' (piloto FASE 1).

Uso one-shot. El piloto se generó con generate_audio.py 22-abr (commit 95a2d07),
antes de FASE 3 que introdujo chunks-index.json. Como el MP3 final está en R2
y no tenemos los chunks individuales, reconstruimos el index midiendo el MP3
final + bumpers + asumiendo velocidad uniforme de narración.

Diferencia con la versión actual: el piloto usaba solo SILENCE_AFTER_INTRO_SEC=2.0,
sin SILENCE_BEFORE_OUTRO_SEC. Por eso este script hardcodea silence_before=0.0.

Tras correrlo, archivar a utilities/_archive/ (one-shot, no recurrente).
"""

import json
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SLUG = "el-que-viene-a-tomar-cafe"

# Constantes de la FASE 1 piloto (ver git show 95a2d07:utilities/generate_audio.py).
SILENCE_AFTER_INTRO_SEC = 2.0
SILENCE_BEFORE_OUTRO_SEC = 0.0  # piloto NO tenía este silencio.

# Mismo regex de detección de capítulos que utilities/generate_audio.py.
SPANISH_ORDINALS = {
    "Uno": 1, "Dos": 2, "Tres": 3, "Cuatro": 4, "Cinco": 5,
    "Seis": 6, "Siete": 7, "Ocho": 8, "Nueve": 9, "Diez": 10,
    "Once": 11, "Doce": 12,
}
MAX_CHAPTER_TITLE_CHARS = 60
CHAPTER_HEADING_RE = re.compile(
    r"^(?:Parte\s+)?({ordinals})\.\s+([^,;:\n]{{1,{maxlen}}}?)\.\s*$".format(
        ordinals="|".join(SPANISH_ORDINALS.keys()),
        maxlen=MAX_CHAPTER_TITLE_CHARS,
    ),
    re.MULTILINE | re.IGNORECASE,
)


def probe_duration(ffmpeg_cmd: str, mp3: Path) -> float:
    """ffprobe vía ffmpeg -hide_banner -i, parseando 'Duration: hh:mm:ss.cc'."""
    res = subprocess.run(
        [ffmpeg_cmd, "-hide_banner", "-i", str(mp3)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    # ffmpeg sin -f null escribe a stderr y retorna 1, pero la duración aparece igual.
    out = res.stderr
    m = re.search(r"Duration:\s+(\d+):(\d+):(\d+\.\d+)", out)
    if not m:
        sys.exit(f"ERROR: no pude leer duración de {mp3}\n{out[:500]}")
    h, mn, s = int(m.group(1)), int(m.group(2)), float(m.group(3))
    return h * 3600 + mn * 60 + s


def find_ffmpeg() -> str:
    """Busca ffmpeg en PATH primero, luego en winget install location."""
    from shutil import which
    p = which("ffmpeg")
    if p:
        return p
    # Fallback Windows winget.
    candidates = list((Path.home() / "AppData/Local/Microsoft/WinGet/Packages").rglob("ffmpeg.exe"))
    if candidates:
        return str(candidates[0])
    sys.exit("ERROR: ffmpeg no encontrado en PATH ni en winget location")


def detect_chapters(text: str) -> list[dict]:
    raw = []
    for m in CHAPTER_HEADING_RE.finditer(text):
        ordinal_key = m.group(1).capitalize()
        raw.append({
            "number": SPANISH_ORDINALS[ordinal_key],
            "title": m.group(2).strip(),
            "char_position": m.start(),
        })
    chapters = []
    for i, ch in enumerate(raw):
        if ch["number"] == i + 1:
            chapters.append(ch)
        else:
            break
    return chapters


def main() -> None:
    ffmpeg = find_ffmpeg()

    # Inputs.
    audiolibro_txt = REPO_ROOT / "content" / "ficciones" / "_one-shots" / SLUG / "audiolibro.txt"
    mp3_final = REPO_ROOT / "assets" / "audio" / "ficciones" / f"{SLUG}.mp3"
    intro_mp3 = REPO_ROOT / "assets" / "audio" / "intro-ficciones.mp3"
    outro_mp3 = REPO_ROOT / "assets" / "audio" / "outro-ficciones.mp3"

    for f in (audiolibro_txt, mp3_final, intro_mp3, outro_mp3):
        if not f.exists():
            sys.exit(f"ERROR: falta {f}")

    text = audiolibro_txt.read_text(encoding="utf-8").strip()

    # Mediciones.
    total_dur = probe_duration(ffmpeg, mp3_final)
    intro_dur = probe_duration(ffmpeg, intro_mp3)
    outro_dur = probe_duration(ffmpeg, outro_mp3)
    narration_dur = (
        total_dur - intro_dur - SILENCE_AFTER_INTRO_SEC
        - SILENCE_BEFORE_OUTRO_SEC - outro_dur
    )

    narration_chars = len(text)
    cps = narration_chars / narration_dur if narration_dur > 0 else 17.0
    narration_start = intro_dur + SILENCE_AFTER_INTRO_SEC

    # Capítulos.
    chapters_raw = detect_chapters(text)
    chapters = [
        {
            "number": ch["number"],
            "title": ch["title"],
            "start_seconds": round(narration_start + ch["char_position"] / cps, 2),
        }
        for ch in chapters_raw
    ]
    if not chapters:
        chapters = [{"number": 1, "title": "Relato", "start_seconds": round(narration_start, 2)}]

    # Build index. chunks[] sintético: 1 entrada que cubre toda la narración,
    # ya que no preservamos chunks individuales del piloto. Downstream
    # (generate_youtube_video.py) solo lee chapters[], no chunks[].
    index = {
        "schema_version": 2,
        "slug": SLUG,
        "total_duration_seconds": round(total_dur, 2),
        "intro_duration_seconds": round(intro_dur, 2),
        "silence_after_intro_seconds": round(SILENCE_AFTER_INTRO_SEC, 2),
        "silence_before_outro_seconds": round(SILENCE_BEFORE_OUTRO_SEC, 2),
        "outro_duration_seconds": round(outro_dur, 2),
        "narration_duration_seconds": round(narration_dur, 2),
        "narration_chars": narration_chars,
        "narration_chars_per_second": round(cps, 2),
        "chunks": [
            {
                "index": 1,
                "file_relative": f"assets/audio/ficciones/{SLUG}.mp3",
                "duration_seconds": round(narration_dur, 2),
                "char_count": narration_chars,
                "_note": "chunks individuales no preservados — piloto FASE 1 reconstruido post-hoc",
            }
        ],
        "chapters": chapters,
    }

    out_path = REPO_ROOT / "assets" / "audio" / "ficciones" / f"{SLUG}-chunks-index.json"
    out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK -> {out_path}")
    print(f"  total: {total_dur:.1f}s · narration: {narration_dur:.1f}s · cps: {cps:.2f}")
    print(f"  capítulos detectados: {len(chapters)}")
    for ch in chapters:
        m, s = divmod(int(ch["start_seconds"]), 60)
        print(f"    {m:02d}:{s:02d} · {ch['number']}. {ch['title']}")


if __name__ == "__main__":
    main()
