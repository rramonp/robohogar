"""
Upload alternativo del feed RSS a Cloudflare R2 vía API REST de Cloudflare.

Uso:
    python utilities/upload_rss_to_r2_via_api.py

Equivalente funcional a `upload_rss_to_r2.py` pero usando el endpoint REST de
Cloudflare (`api.cloudflare.com`) en lugar del endpoint S3-compatible
(`<account>.r2.cloudflarestorage.com`). Útil cuando el rango IP del endpoint
S3 está caído desde la red del laptop pero `api.cloudflare.com` (otro rango
de Cloudflare) sigue alcanzable — incidente 2026-04-25 con outage parcial
en `172.64.66.x`.

Mismo input (`content/podcast/feed.xml`), mismo output observable
(`https://feed.robohogar.com/feed.xml` actualizado), distinto transport.

Requiere una key adicional en `.claude/settings.local.json`:
    "CLOUDFLARE_API_TOKEN": "<token>"

Cómo crear el token (one-time, ~2 min):
  1. https://dash.cloudflare.com/profile/api-tokens → "Create Token".
  2. Custom Token con un solo permiso:
       Account · Workers R2 Storage · Edit
     Account Resources: Include · <tu cuenta>.
     Opcional: TTL 1 año + restricción IP a tu rango.
  3. Copiar el token (solo se muestra una vez) a settings.local.json.

NO requiere las R2 Access Keys S3 (que sí usa el script principal). El
endpoint REST autentica con Bearer token estándar de Cloudflare.

Idempotente: sobrescribe el feed.xml anterior — los `<guid>` de cada item
son inmutables, así que las plataformas no re-procesan episodios viejos.

Dependencias: solo stdlib (json, urllib). Mismo patrón que
`verify_elevenlabs_auth.py` y `generate_audio.py`.
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
FEED_LOCAL = REPO_ROOT / "content" / "podcast" / "feed.xml"

# Key del feed en el bucket. Sirve en `<R2_FEED_PUBLIC_URL>/feed.xml`.
FEED_KEY = "feed.xml"

# Endpoint base de la API REST de Cloudflare. NO depende del account_id en
# el hostname (a diferencia del S3 endpoint). Resuelve a 104.19.x.x — rango
# distinto al S3 endpoint (172.64.x.x), por eso este script funciona cuando
# el otro falla por outage parcial de routing en 172.64.x.x.
CF_API_BASE = "https://api.cloudflare.com/client/v4"


def load_env() -> dict:
    """Carga R2 bucket + Cloudflare API Token desde settings.local.json.

    Diferencia con el script S3: este NO necesita R2_ACCESS_KEY ni
    R2_SECRET_KEY (esas son credenciales S3-compat). Solo R2_ACCOUNT_ID,
    R2_BUCKET, R2_FEED_PUBLIC_URL (el dominio público que sirve el feed)
    y CLOUDFLARE_API_TOKEN (Bearer token con permiso R2 Storage:Edit).
    """
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    required = ["R2_ACCOUNT_ID", "R2_BUCKET", "R2_FEED_PUBLIC_URL", "CLOUDFLARE_API_TOKEN"]
    missing = [k for k in required if not env.get(k) or "REEMPLAZAR" in env.get(k, "")]
    if missing:
        if "CLOUDFLARE_API_TOKEN" in missing:
            sys.exit(
                f"ERROR: falta CLOUDFLARE_API_TOKEN en settings.local.json.\n"
                f"\n"
                f"Crear token (one-time, ~2 min):\n"
                f"  1. https://dash.cloudflare.com/profile/api-tokens -> 'Create Token'.\n"
                f"  2. Custom Token con permiso: Account > Workers R2 Storage > Edit.\n"
                f"  3. Account Resources: Include > tu cuenta.\n"
                f"  4. Copiar el token a settings.local.json:\n"
                f'       "CLOUDFLARE_API_TOKEN": "<token>"\n'
            )
        sys.exit(f"ERROR: faltan en settings.local.json: {', '.join(missing)}")
    return env


def upload_via_rest(env: dict, body: bytes) -> None:
    """PUT del feed.xml al endpoint REST de R2.

    Endpoint: PUT /accounts/{account_id}/r2/buckets/{bucket}/objects/{key}
    Headers:
      - Authorization: Bearer <token>
      - Content-Type: application/rss+xml (estándar IETF para RSS)
      - Cache-Control: max-age=3600 (CDN cachea 1 h; podcast clients
        re-leen cada hora, suficiente)

    Body: bytes del feed.xml. La API REST de R2 acepta el cuerpo binario
    directamente como contenido del objeto — no envuelve en JSON ni
    multipart, distinto a otros endpoints de la API REST de Cloudflare.

    Lanza urllib.error.HTTPError si el upload falla. Cloudflare devuelve
    JSON con `success: true|false` y `errors[]` en el body — lo parseamos
    para dar mensaje claro al usuario.
    """
    url = (
        f"{CF_API_BASE}/accounts/{env['R2_ACCOUNT_ID']}"
        f"/r2/buckets/{env['R2_BUCKET']}/objects/{FEED_KEY}"
    )
    req = urllib.request.Request(
        url,
        data=body,
        method="PUT",
        headers={
            "Authorization": f"Bearer {env['CLOUDFLARE_API_TOKEN']}",
            "Content-Type": "application/rss+xml",
            "Cache-Control": "max-age=3600",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            # 200/201 = ok; cualquier otro código nos lo levanta urllib como HTTPError.
            payload = resp.read().decode("utf-8", errors="replace")
            # La API REST devuelve JSON; nos vale como confirmación de éxito.
            try:
                parsed = json.loads(payload)
                if not parsed.get("success", True):
                    errors = parsed.get("errors", [])
                    sys.exit(f"FAIL upload: API devolvió success=false. Errores: {errors}")
            except json.JSONDecodeError:
                # Algunos endpoints de R2 REST devuelven body vacío en éxito.
                pass
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        sys.exit(
            f"FAIL upload: HTTP {e.code} {e.reason}\n"
            f"Response body: {body_err[:500]}\n"
            f"Causas comunes:\n"
            f"  - 401/403: token inválido o sin permiso 'Workers R2 Storage:Edit'.\n"
            f"  - 404: bucket {env['R2_BUCKET']} no existe en account {env['R2_ACCOUNT_ID']}.\n"
            f"  - 5xx: outage Cloudflare. Reintentar en minutos."
        )
    except urllib.error.URLError as e:
        sys.exit(
            f"FAIL upload: {e.reason}\n"
            f"Si el error es 'connection timed out', el rango de api.cloudflare.com\n"
            f"también está caído desde tu red. Probar con hotspot móvil o esperar."
        )


def main() -> None:
    if not FEED_LOCAL.exists():
        sys.exit(
            f"ERROR: no existe {FEED_LOCAL.relative_to(REPO_ROOT)}\n"
            f"Genera primero: python utilities/generate_podcast_rss.py"
        )

    env = load_env()
    body = FEED_LOCAL.read_bytes()
    public_url = f"{env['R2_FEED_PUBLIC_URL'].rstrip('/')}/{FEED_KEY}"

    print(f"Local feed : {FEED_LOCAL.relative_to(REPO_ROOT)} ({len(body):,} bytes)")
    print(f"Bucket     : {env['R2_BUCKET']}")
    print(f"Key        : {FEED_KEY}")
    print(f"Endpoint   : Cloudflare REST API (api.cloudflare.com)")
    print(f"Public URL : {public_url}")
    print()

    # Pre-step OBLIGATORIO: validar que cada asset referenciado por el feed
    # existe en R2 antes de publicar el feed mismo. Auto-heal sube los que
    # falten desde local (si existen). Si tras heal sigue habiendo huérfanos
    # → SystemExit y el feed NO se publica. Garantiza que las plataformas
    # nunca encuentren 404 al primer fetch (incidente origen 2026-04-25
    # con el-que-viene-a-tomar-cafe).
    from validate_podcast_assets import validate_and_heal
    validate_and_heal(env, FEED_LOCAL, heal=True)
    print()

    print("Subiendo feed.xml vía REST API...")
    upload_via_rest(env, body)
    print(f"  OK -> {public_url}")
    print()
    print("=" * 72)
    print("FEED PUBLICADO (vía REST API)")
    print("=" * 72)
    print(f"URL : {public_url}")
    print()
    print("Verificar:")
    print(f"  curl -sI {public_url} | head -5")
    print(f"  Pegar en https://castfeedvalidator.com")
    print("=" * 72)


if __name__ == "__main__":
    main()
