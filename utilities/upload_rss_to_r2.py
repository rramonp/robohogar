"""
Sube el feed RSS del podcast a Cloudflare R2 con Content-Type correcto.

Uso:
    python utilities/upload_rss_to_r2.py

Lee `content/podcast/feed.xml` (generado por generate_podcast_rss.py) y lo
sube a R2 con key `feed.xml` y Content-Type `application/rss+xml`. El
custom domain `feed.robohogar.com` (configurado en el Bloque 2 de la guía)
sirve este archivo en `https://feed.robohogar.com/feed.xml`.

Idempotente: sobrescribe el feed.xml anterior — es estado actual del
catálogo, no histórico (los `<guid>` de cada item son inmutables, así
que las plataformas no re-procesan episodios viejos).

Las plataformas (Spotify, Apple, Amazon) re-leen el feed cada hora aprox
y detectan automáticamente el nuevo `<item>` por su `<guid>` único. No
hace falta notificarlas — el RSS es pull, no push.

Cuándo invocar:
  - Tras `generate_podcast_rss.py` que regeneró el XML local.
  - Encadenado automáticamente por `/audiobook-distribute` paso 5.
"""

import json
import sys
from pathlib import Path

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
FEED_LOCAL = REPO_ROOT / "content" / "podcast" / "feed.xml"

# Key del feed en el bucket. Sirve en `<R2_FEED_PUBLIC_URL>/feed.xml`.
# Si en el futuro queremos varios feeds (ej. Ficciones vs Reviews), añadir
# parámetro `--key` opcional.
FEED_KEY = "feed.xml"


def load_env() -> dict:
    """Carga R2 credentials + bucket. Mismo patrón que verify_r2_auth.py."""
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    required = ["R2_ACCOUNT_ID", "R2_ACCESS_KEY", "R2_SECRET_KEY", "R2_BUCKET", "R2_FEED_PUBLIC_URL"]
    missing = [k for k in required if not env.get(k) or "REEMPLAZAR" in env.get(k, "")]
    if missing:
        sys.exit(f"ERROR: faltan en settings.local.json: {', '.join(missing)}")
    return env


def main() -> None:
    if not FEED_LOCAL.exists():
        sys.exit(
            f"ERROR: no existe {FEED_LOCAL.relative_to(REPO_ROOT)}\n"
            f"Genera primero: python utilities/generate_podcast_rss.py"
        )

    env = load_env()
    print(f"Local feed : {FEED_LOCAL.relative_to(REPO_ROOT)} ({FEED_LOCAL.stat().st_size:,} bytes)")
    print(f"Bucket     : {env['R2_BUCKET']}")
    print(f"Key        : {FEED_KEY}")
    print(f"Public URL : {env['R2_FEED_PUBLIC_URL'].rstrip('/')}/{FEED_KEY}")
    print()

    s3 = boto3.client(
        "s3",
        endpoint_url=f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
        aws_access_key_id=env["R2_ACCESS_KEY"],
        aws_secret_access_key=env["R2_SECRET_KEY"],
        region_name="auto",
        config=Config(signature_version="s3v4"),
    )

    print("Subiendo feed.xml...")
    try:
        s3.upload_file(
            Filename=str(FEED_LOCAL),
            Bucket=env["R2_BUCKET"],
            Key=FEED_KEY,
            # Content-Type application/rss+xml es el estándar IETF para feeds RSS.
            # CacheControl max-age=3600: que CDN cachee 1h — los podcast clients
            # re-leen cada hora aprox, no hace falta menor.
            ExtraArgs={
                "ContentType": "application/rss+xml",
                "CacheControl": "max-age=3600",
            },
        )
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code", "?")
        sys.exit(f"FAIL upload: {code} -- revisa credenciales/permisos R2")

    public_url = f"{env['R2_FEED_PUBLIC_URL'].rstrip('/')}/{FEED_KEY}"
    print(f"  OK -> {public_url}")
    print()
    print("=" * 72)
    print(f"FEED PUBLICADO")
    print("=" * 72)
    print(f"URL : {public_url}")
    print()
    print("Verificar:")
    print(f"  curl -sI {public_url} | head -5")
    print(f"  Pegar en https://castfeedvalidator.com")
    print("=" * 72)


if __name__ == "__main__":
    main()
