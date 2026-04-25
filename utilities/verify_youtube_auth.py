"""
Verificar credenciales OAuth de YouTube Data API v3 + accesibilidad del canal.

Uso:
    python utilities/verify_youtube_auth.py

Lee el token OAuth persistido (gitignored) en la ruta configurada por
`YOUTUBE_OAUTH_TOKEN_PATH` de `.claude/settings.local.json`. Si el token
está expirado pero hay refresh_token válido, lo refresca y persiste el
nuevo. Luego llama a `channels.list(part='snippet,statistics', mine=True)`
(cuesta 1 unit del quota, irrelevante) y muestra info del canal.

Cuándo invocar:
  - Tras el setup inicial (Bloque 1 de la guía de distribución) — confirmar
    que el primer auth flow generó token válido.
  - Como pre-check del paso 13.5 de `/post-publish` antes de invocar
    `/audiobook-distribute` — si el token caducó, falla aquí en lugar de
    fallar a mitad del upload.
  - Cuando `/audiobook-distribute` reporta error de auth — diagnostica si
    el problema es token o cuota.

Patrón heredado de `verify_r2_auth.py` y `verify_elevenlabs_auth.py`:
modular, mensajes de error amigables apuntando al fix concreto de la guía,
salidas con exit codes claros.
"""

import json
import sys
from pathlib import Path


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


SETTINGS_FILE = Path(__file__).resolve().parent.parent / ".claude" / "settings.local.json"

# Scopes necesarios para upload + manage de YouTube. Los 3 deben estar
# presentes en el OAuth consent screen Y en el token generado — si el
# token tiene menos scopes que los requeridos por el upload posterior,
# la API devuelve insufficient permissions sin reauth.
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

REQUIRED_KEYS = [
    "YOUTUBE_OAUTH_CLIENT_SECRET_PATH",
    "YOUTUBE_OAUTH_TOKEN_PATH",
]


def load_env() -> dict:
    """Lee .claude/settings.local.json y devuelve el dict env validado.

    Falla con mensaje claro y exit code 1 si falta alguna key. El usuario
    sabe inmediatamente qué configurar — no se ve un AttributeError
    después de varias capas.
    """
    if not SETTINGS_FILE.exists():
        sys.exit(
            f"ERROR: no existe {SETTINGS_FILE}\n"
            "Crea el archivo con las env vars YouTube — ver "
            "Docs/Guia Distribucion Audiolibros.md § Bloque 1.4."
        )
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: {SETTINGS_FILE} no es JSON valido: {e}")

    env = data.get("env", {})
    missing = [k for k in REQUIRED_KEYS if not env.get(k) or "REEMPLAZAR" in env.get(k, "")]
    if missing:
        sys.exit(
            f"ERROR: faltan en settings.local.json: {', '.join(missing)}\n"
            "Ver Docs/Guia Distribucion Audiolibros.md § Bloque 1.4 para los valores correctos."
        )
    return env


def import_google_libs():
    """Import lazy de las libs Google con mensaje amigable si faltan.

    Hacemos import lazy (no a nivel de módulo) para que `--help` o errores
    de configuración no requieran tener los packages instalados — útil
    durante el setup cuando aún no se ha hecho `pip install`.
    """
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        return Credentials, Request, build, HttpError
    except ImportError:
        sys.exit(
            "ERROR: faltan dependencias Google. Instala con:\n"
            "  pip install google-auth google-auth-oauthlib google-api-python-client"
        )


def load_credentials(token_path: Path):
    """Carga el token OAuth persistido y refresca si está expirado.

    Estrategia:
      1. Si no existe token → mensaje claro pidiendo correr --auth flow.
      2. Si existe pero inválido sin refresh → mensaje pidiendo re-auth.
      3. Si existe pero expirado con refresh → refresca, persiste, sigue.
      4. Si existe y válido → usa directamente.

    Persistir el token refrescado evita tener que refrescar en cada
    invocación — el token nuevo dura ~1 h y entonces se vuelve a refrescar
    automáticamente en la siguiente call.
    """
    Credentials, Request, _, _ = import_google_libs()

    if not token_path.exists():
        sys.exit(
            f"ERROR: no existe el token en {token_path}\n"
            "Corre primero el auth flow:\n"
            "  python utilities/upload_youtube.py --auth\n"
            "Luego repite este verifier."
        )

    try:
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    except Exception as e:
        sys.exit(f"ERROR: token corrupto o con scopes incorrectos: {e}\n"
                 "Borra el token y re-autoriza con `python utilities/upload_youtube.py --auth`.")

    if creds.valid:
        print("  [1/2] Token cargado y valido (sin refresh necesario).")
        return creds

    if creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            # Persistir el token refrescado para no tener que refrescar
            # en la siguiente invocación.
            token_path.write_text(creds.to_json(), encoding="utf-8")
            print("  [1/2] Token expirado, refrescado y persistido OK.")
            return creds
        except Exception as e:
            sys.exit(
                f"ERROR refrescando token: {e}\n"
                "Posibles causas: refresh token caduco (consent screen en Testing mode?),\n"
                "credenciales revocadas, o password de Google cambiada.\n"
                "Fix: borra el token y re-autoriza con `python utilities/upload_youtube.py --auth`."
            )

    sys.exit(
        "ERROR: credenciales invalidas y sin refresh token utilizable.\n"
        "Re-autoriza con `python utilities/upload_youtube.py --auth`."
    )


def fetch_channel_info(creds) -> dict:
    """Llama a channels.list(mine=True) — cuesta 1 unit del quota."""
    _, _, build, HttpError = import_google_libs()

    try:
        youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)
        response = youtube.channels().list(
            part="snippet,statistics,contentDetails",
            mine=True,
        ).execute()
    except HttpError as e:
        sys.exit(f"  [2/2] FAIL channels.list HTTP {e.resp.status}: {e}\n"
                 "Verifica que YouTube Data API v3 esta enabled en Google Cloud Console.")

    items = response.get("items", [])
    if not items:
        sys.exit("  [2/2] FAIL: el OAuth no tiene canal asociado.\n"
                 "Crea el canal YouTube primero (Bloque 1.1 de la guia) y reauth.")
    return items[0]


def main() -> None:
    env = load_env()
    print(f"Settings cargados desde {SETTINGS_FILE.relative_to(SETTINGS_FILE.parent.parent)}.")
    token_path = Path(env["YOUTUBE_OAUTH_TOKEN_PATH"])
    print(f"Token path: {token_path}")
    print()

    print("Smoke test YouTube OAuth (load token -> channels.list mine):")
    creds = load_credentials(token_path)
    channel = fetch_channel_info(creds)

    snippet = channel.get("snippet", {})
    stats = channel.get("statistics", {})
    print(f"  [2/2] channels.list OK (cost: 1 unit).")
    print()
    print("=" * 72)
    print(f"YOUTUBE AUTH OK")
    print("=" * 72)
    print(f"Channel name : {snippet.get('title', '?')}")
    print(f"Channel ID   : {channel.get('id', '?')}")
    print(f"Subscribers  : {stats.get('subscriberCount', '?')}")
    print(f"Videos       : {stats.get('videoCount', '?')}")
    print(f"Total views  : {stats.get('viewCount', '?')}")
    print(f"Country      : {snippet.get('country', 'no especificado')}")
    print("=" * 72)
    print()
    expected_id = env.get("YOUTUBE_CHANNEL_ID", "")
    if expected_id and expected_id != channel.get("id"):
        print(f"WARNING: YOUTUBE_CHANNEL_ID en settings ({expected_id}) no coincide")
        print(f"         con el canal autorizado ({channel.get('id')}).")
        print(f"         Actualiza settings.local.json con el ID correcto.")
    elif not expected_id:
        print(f"NOTA: YOUTUBE_CHANNEL_ID no esta en settings.local.json.")
        print(f"      Anadelo: \"YOUTUBE_CHANNEL_ID\": \"{channel.get('id')}\"")


if __name__ == "__main__":
    main()
