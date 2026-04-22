"""
Verificar autenticación y permisos de la API key de ElevenLabs.

Uso:
    python utilities/verify_elevenlabs_auth.py

Lee ELEVENLABS_API_KEY desde .claude/settings.local.json (gitignored) y
hace GET /v1/voices (endpoint de metadata, zero coste en créditos) para
confirmar que:
  1. La key autentica correctamente (HTTP 200, no 401).
  2. El permiso "Voices: Read" está activo (no 403).
  3. Hay voces ES disponibles para elegir el voice_id del narrador en FASE 0
     del plan audiolibros (docs/plan-audiolibros-ficciones.md).

Cuándo invocar este script:
  - Tras crear/rotar una API key (smoke test inmediato).
  - Tras configurar una máquina nueva (laptop/desktop) con su settings.local.json.
  - Si /audiobook-generate falla con error 401/403, para aislar si el problema
    es la key o el código.

Dependencias: solo stdlib (json, urllib). No requiere pip install.
"""

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path


# Ruta absoluta al archivo local (gitignored) que contiene la key.
# Se localiza relativo al root del repo, asumiendo que este script vive en utilities/.
SETTINGS_FILE = Path(__file__).resolve().parent.parent / ".claude" / "settings.local.json"

# Endpoint de metadata — devuelve el catálogo de voces accesibles para la cuenta.
# No consume créditos de caracteres (solo /v1/text-to-speech/* los consume).
VOICES_URL = "https://api.elevenlabs.io/v1/voices"


def load_api_key() -> str:
    """Lee la API key del JSON local. Aborta con mensaje claro si falta o es placeholder."""
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}. Crear con env.ELEVENLABS_API_KEY.")
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: {SETTINGS_FILE} no es JSON válido: {e}")
    key = data.get("env", {}).get("ELEVENLABS_API_KEY", "")
    # Detectamos placeholder explícito para evitar enviar texto basura como Bearer.
    if not key or key.startswith("REEMPLAZAR"):
        sys.exit("ERROR: ELEVENLABS_API_KEY vacía o placeholder sin reemplazar.")
    return key


def probe_voices(api_key: str):
    """GET /v1/voices con la key. Devuelve (status_code, body_dict_o_texto_error)."""
    req = urllib.request.Request(
        VOICES_URL,
        headers={"xi-api-key": api_key, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        # Truncamos a 500 chars por si la API devuelve HTML largo en errores raros.
        return e.code, e.read().decode("utf-8", errors="replace")[:500]
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def main() -> None:
    api_key = load_api_key()
    # NO imprimimos la key entera — solo prefijo + longitud para confirmar que cargó algo
    # plausible (las keys de ElevenLabs empiezan por "sk_" y rondan los 50 chars).
    print(f"Key cargada: {api_key[:7]}... ({len(api_key)} chars)")
    print(f"Probando: {VOICES_URL}")
    print()

    status, body = probe_voices(api_key)

    if status == 200:
        voices = body.get("voices", []) if isinstance(body, dict) else []
        print(f"AUTH OK -- HTTP 200, {len(voices)} voces accesibles\n")
        # Filtramos voces que tienen ES en su language label (case-insensitive).
        # ElevenLabs marca el idioma en labels.language o labels.accent dependiendo de la voz.
        spanish_voices = []
        for v in voices:
            labels = v.get("labels", {}) or {}
            lang = (labels.get("language") or "").lower()
            accent = (labels.get("accent") or "").lower()
            if "es" == lang or "spanish" in lang or "spanish" in accent or "spain" in accent:
                spanish_voices.append(v)

        if spanish_voices:
            print(f"Voces ES detectadas ({len(spanish_voices)}, primeras 10):")
            for v in spanish_voices[:10]:
                labels = v.get("labels", {}) or {}
                print(
                    f"  - {(v.get('name') or '?'):28s}  "
                    f"id={(v.get('voice_id') or '?')[:10]}...  "
                    f"accent={(labels.get('accent') or '?'):10s}  "
                    f"gender={labels.get('gender') or '?'}"
                )
        else:
            print("(Sin voces con label ES directo en el set por defecto)")
            print("Para ver el catálogo ES completo, ir al dashboard ElevenLabs >")
            print("Voices > Library > filtro Language: Spanish.")

        print(f"\nPrimeras 5 voces del catálogo (any language):")
        for v in voices[:5]:
            labels = v.get("labels", {}) or {}
            print(
                f"  - {(v.get('name') or '?'):28s}  "
                f"id={(v.get('voice_id') or '?')[:10]}...  "
                f"category={v.get('category') or '?'}"
            )

    elif status == 401:
        print(f"AUTH FAIL -- HTTP 401: key invalida o revocada")
        print(f"Respuesta: {body}")
        sys.exit(1)
    elif status == 403:
        print(f"PERMISOS FAIL -- HTTP 403: key valida pero sin permiso Voices=Read")
        print(f"Dashboard > API Keys > robohogar-audiobook > Voices = Read")
        print(f"Respuesta: {body}")
        sys.exit(1)
    else:
        print(f"STATUS inesperado: {status}")
        print(f"Respuesta: {body}")
        sys.exit(1)


if __name__ == "__main__":
    main()
