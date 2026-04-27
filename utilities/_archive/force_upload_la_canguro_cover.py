"""Sube el cover podcast 1400x1400 de la-canguro a R2 (one-shot 2026-04-27)."""

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

key = "covers/la-canguro-podcast-1400x1400.jpg"
local = REPO_ROOT / "assets/audio/ficciones/covers/la-canguro-podcast-1400x1400.jpg"

if not local.exists():
    sys.exit(f"FAIL: archivo local no existe: {local}")

print(f"Subiendo {local.name} ({local.stat().st_size // 1024} KB) -> r2:{key}")
s3.upload_file(
    str(local),
    env["R2_BUCKET"],
    key,
    ExtraArgs={"ContentType": "image/jpeg", "CacheControl": "public, max-age=86400"},
)
print(f"OK -> https://feed.robohogar.com/{key}")
