"""
One-shot 2026-04-27: regenera intro-ficciones.mp3 + outro-ficciones.mp3
con voz Gabo (default canon desde 2026-04-27).

Ejecución:
    python utilities/_archive/generate_bumpers_gabo_2026_04_27.py

Sustituye los Luis previos (versionados como -luis-v1) tras la decisión
"100% Gabo desde el siguiente relato" de Rafael 2026-04-27.

Texto canon de bumpers en docs/plan-audiolibros-ficciones.md § 109-113.
Aplica regla TTS de pronunciación marca: ROBOHOGAR → ROBO, OGAR (memoria
feedback_robohogar_tts_pronunciation.md).
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

VOICE_ID_GABO = "o0SveC0zgHFuCsEO3vHR"  # Gabo - Deep, Evocative and Resonant
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"

INTRO_TEXT = "Ficciones Domésticas, de ROBO, OGAR."
OUTRO_TEXT = (
    "Has escuchado una Ficción Doméstica de ROBO, OGAR. "
    "Más relatos y newsletter en ROBO, OGAR punto com."
)


def load_api_key() -> str:
    """Lee ELEVENLABS_API_KEY de settings.local.json buscando recursivamente."""
    settings = json.loads(
        (REPO_ROOT / ".claude" / "settings.local.json").read_text(encoding="utf-8")
    )

    def find(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k == "ELEVENLABS_API_KEY":
                    return v
                r = find(v)
                if r:
                    return r
        return None

    key = find(settings) or os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ERROR: ELEVENLABS_API_KEY no encontrado.")
    return key


def tts(api_key: str, text: str, output_path: Path) -> None:
    """Llama TTS ElevenLabs con voz Gabo y escribe MP3 al path indicado."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID_GABO}?output_format={OUTPUT_FORMAT}"
    body = json.dumps(
        {
            "text": text,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.0,
                "use_speaker_boost": True,
            },
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        audio_bytes = resp.read()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(audio_bytes)
    print(f"  -> {output_path.name}: {len(audio_bytes):,} bytes")


def main() -> None:
    print(f"Voz: Gabo ({VOICE_ID_GABO}) · modelo {MODEL_ID}\n")

    api_key = load_api_key()

    print(f'Generando intro: "{INTRO_TEXT}"')
    tts(api_key, INTRO_TEXT, REPO_ROOT / "assets" / "audio" / "intro-ficciones.mp3")

    print(f'\nGenerando outro: "{OUTRO_TEXT}"')
    tts(api_key, OUTRO_TEXT, REPO_ROOT / "assets" / "audio" / "outro-ficciones.mp3")

    chars = len(INTRO_TEXT) + len(OUTRO_TEXT)
    print(f"\nTotal chars facturados: ~{chars} (~{int(chars * 0.79)} créditos a 0.79 chars/créd)")
    print("\n✅ Bumpers Gabo generados. Próximos relatos los usarán automáticamente.")


if __name__ == "__main__":
    main()
