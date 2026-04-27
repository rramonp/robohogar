"""
Fuerza upload de los 3 covers podcast nuevos a R2 (2026-04-27).

Origen del bug: validate_podcast_assets.py § head_check verifica si una URL
devuelve HTTP 200 antes de subir. Cloudflare R2 ignora el query string
(`?v=20260427`) y devuelve 200 con el archivo VIEJO al hacer HEAD. El validator
asume OK y NO sube. Resultado: el feed referencia URLs con cache-bust pero
el archivo subyacente sigue siendo el viejo.

Este script usa el endpoint S3 de R2 (boto3) — mismo plano que upload_rss_to_r2.py.
"""

import json
import sys
from pathlib import Path

import boto3
from botocore.client import Config

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

env = json.loads((REPO_ROOT / ".claude" / "settings.local.json").read_text(encoding="utf-8"))["env"]

s3 = boto3.client(
    "s3",
    endpoint_url=f"https://{env['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
    aws_access_key_id=env["R2_ACCESS_KEY"],
    aws_secret_access_key=env["R2_SECRET_KEY"],
    config=Config(signature_version="s3v4"),
    region_name="auto",
)

covers = [
    ("covers/la-objecion-podcast-1400x1400.jpg",
     REPO_ROOT / "assets/audio/ficciones/covers/la-objecion-podcast-1400x1400.jpg"),
    ("covers/el-operador-nocturno-podcast-1400x1400.jpg",
     REPO_ROOT / "assets/audio/ficciones/covers/el-operador-nocturno-podcast-1400x1400.jpg"),
    ("covers/el-que-viene-a-tomar-cafe-podcast-1400x1400.jpg",
     REPO_ROOT / "assets/audio/ficciones/covers/el-que-viene-a-tomar-cafe-podcast-1400x1400.jpg"),
]

for key, local in covers:
    if not local.exists():
        sys.exit(f"FAIL: archivo local no existe: {local}")
    size_kb = local.stat().st_size // 1024
    print(f"Subiendo {local.name} ({size_kb} KB) -> r2:{key}")
    s3.upload_file(
        str(local),
        env["R2_BUCKET"],
        key,
        ExtraArgs={"ContentType": "image/jpeg", "CacheControl": "public, max-age=86400"},
    )
    print(f"  OK -> https://feed.robohogar.com/{key}")

print("\n3 covers nuevos subidos a R2 (sobreescribiendo).")
