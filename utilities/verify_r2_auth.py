"""
Verificar credenciales y accesibilidad pública de Cloudflare R2.

Uso:
    python utilities/verify_r2_auth.py

Lee las 5 env vars de R2 desde .claude/settings.local.json (gitignored) y
ejecuta un ciclo completo upload → read-public → delete con un archivo de
prueba minúsculo (1 KB, `test-connection-<timestamp>.txt`). Con esto se
confirma en una sola pasada:

  1. Las credenciales S3-compatible autentican (HeadBucket OK).
  2. El token tiene permiso Object Write (upload OK).
  3. El bucket está expuesto por R2 Public Development URL (GET público OK).
  4. El token tiene permiso Object Delete (cleanup OK).

Cuándo invocar este script:
  - Tras configurar R2 por primera vez (smoke test antes de confiar en el host).
  - Tras rotar credenciales o el token.
  - Si /audiobook-generate falla con errores de autenticación S3 o 404 del
    MP3 público, para aislar si el problema es R2 o el código del skill.

Dependencias: boto3 (para S3 API), urllib (stdlib, para comprobar URL pública).
El archivo de prueba se borra automáticamente al final — no deja residuo.

No consume cuota de ElevenLabs ni créditos de caracteres (solo R2).
"""

import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError, EndpointConnectionError


# Ruta absoluta al archivo gitignored con los secretos.
SETTINGS_FILE = Path(__file__).resolve().parent.parent / ".claude" / "settings.local.json"

# Lista canónica de env vars que este verificador necesita. Cualquier ausencia
# o placeholder (REEMPLAZAR, PEGAR) se trata como error de configuración.
REQUIRED_KEYS = [
    "R2_ACCOUNT_ID",
    "R2_ACCESS_KEY",
    "R2_SECRET_KEY",
    "R2_BUCKET",
    "R2_PUBLIC_URL",
]


def load_env() -> dict:
    """Lee el JSON y devuelve el dict env. Aborta si falta cualquier key requerida."""
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: {SETTINGS_FILE} no es JSON valido: {e}")

    env = data.get("env", {})
    missing = []
    for k in REQUIRED_KEYS:
        v = env.get(k, "")
        # Detectamos placeholders obvios para evitar fallos crípticos más adelante.
        if not v or "REEMPLAZAR" in v or "PEGAR" in v:
            missing.append(k)
    if missing:
        sys.exit(f"ERROR: faltan en settings.local.json: {', '.join(missing)}")
    return env


def build_s3_client(env: dict):
    """Crea cliente boto3 apuntando al endpoint S3 de R2.

    R2 requiere signature_version s3v4 (obligatorio) y region 'auto' porque
    los buckets R2 no tienen región clásica como S3. Endpoint es el de R2:
    https://<account_id>.r2.cloudflarestorage.com
    """
    endpoint = f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com"
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=env["R2_ACCESS_KEY"],
        aws_secret_access_key=env["R2_SECRET_KEY"],
        region_name="auto",
        config=Config(signature_version="s3v4"),
    )


def check_bucket_exists(s3, bucket: str) -> None:
    """HeadBucket — confirma credenciales + bucket accesible. Aborta si falla."""
    try:
        s3.head_bucket(Bucket=bucket)
        print(f"  [1/4] HEAD bucket '{bucket}' OK (credenciales autentican)")
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "?")
        sys.exit(f"  [1/4] FAIL HeadBucket: {code} — revisa R2_ACCOUNT_ID / credenciales / R2_BUCKET")
    except EndpointConnectionError as e:
        sys.exit(f"  [1/4] FAIL endpoint: {e} — revisa que R2_ACCOUNT_ID es correcto")


def upload_test_object(s3, bucket: str, key: str, body: bytes) -> None:
    """PutObject — confirma permiso Object Write."""
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=body, ContentType="text/plain")
        print(f"  [2/4] PUT '{key}' ({len(body)} bytes) OK")
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "?")
        sys.exit(f"  [2/4] FAIL PutObject: {code} — token sin permiso Object Write?")


def fetch_via_public_url(public_url: str, key: str, expected_body: bytes) -> None:
    """HTTP GET al R2.dev subdomain — confirma Public Development URL habilitada.

    Importante: Cloudflare R2.dev devuelve 403 para User-Agents no-navegador
    (python-urllib/... rechazado como bot). Por eso enviamos un UA de navegador
    real. Esto no afecta al uso final (el <audio> en Beehiiv usa UA nativo del
    navegador del lector — sin problemas); solo afecta a clientes programáticos.
    """
    url = f"{public_url.rstrip('/')}/{key}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            got = resp.read()
        if got == expected_body:
            print(f"  [3/4] GET publico '{url}' OK (contenido coincide, {len(got)} bytes)")
        else:
            sys.exit(f"  [3/4] FAIL contenido distinto: {len(got)} bytes vs {len(expected_body)} esperados")
    except urllib.error.HTTPError as e:
        sys.exit(f"  [3/4] FAIL HTTP {e.code}: {e.reason} — revisa que Public Development URL este Enabled")
    except Exception as e:
        sys.exit(f"  [3/4] FAIL {type(e).__name__}: {e}")


def delete_test_object(s3, bucket: str, key: str) -> None:
    """DeleteObject — cleanup + confirma permiso Object Delete (viene con Object R/W)."""
    try:
        s3.delete_object(Bucket=bucket, Key=key)
        print(f"  [4/4] DELETE '{key}' OK (cleanup)")
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "?")
        # No abortamos aquí — el test principal ya pasó; solo warning.
        print(f"  [4/4] WARNING DeleteObject fallo: {code} — borra '{key}' manual desde dashboard")


def main() -> None:
    env = load_env()
    print("Env cargado desde settings.local.json:")
    print(f"  R2_ACCOUNT_ID: {env['R2_ACCOUNT_ID'][:8]}...")
    print(f"  R2_BUCKET:     {env['R2_BUCKET']}")
    print(f"  R2_PUBLIC_URL: {env['R2_PUBLIC_URL']}")
    print()

    s3 = build_s3_client(env)

    # Archivo de prueba con timestamp para que no colisione si se ejecuta varias veces seguidas.
    # Contenido deliberadamente pequeño — no consume cuota notable.
    ts = int(time.time())
    test_key = f"test-connection-{ts}.txt"
    test_body = f"ROBOHOGAR R2 smoke test at {ts}. Safe to delete.\n".encode("utf-8")

    print(f"Smoke test R2 (upload -> public GET -> delete):")
    check_bucket_exists(s3, env["R2_BUCKET"])
    upload_test_object(s3, env["R2_BUCKET"], test_key, test_body)
    fetch_via_public_url(env["R2_PUBLIC_URL"], test_key, test_body)
    delete_test_object(s3, env["R2_BUCKET"], test_key)

    print()
    print("AUTH OK -- R2 listo para uso. Credenciales, permisos y URL publica verificados.")


if __name__ == "__main__":
    main()
