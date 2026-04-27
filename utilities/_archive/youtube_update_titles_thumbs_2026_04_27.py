"""
Actualiza title + thumbnail de los 3 vídeos YouTube ya publicados de Ficciones
Domésticas (la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe).

Decisión 2026-04-27 con Rafael:
  - Title nuevo = display_title largo del frontmatter (sin sufijo). Refleja
    canon § 5.bis YouTube-style desde 2026-04-26 PM.
  - Thumbnail nuevo = cover yt-1280x720 painterly chiaroscuro (heros v9/v7/v6
    nuevos). Sin chyron overlay.

Idempotente: re-ejecutar no rompe nada (YouTube acepta el mismo title/thumbnail).

Coste API: por video, 50 units (videos.update con part=snippet) + 50 units
(thumbnails.set) = 100 units. Total 3 videos = 300 units / 10.000 daily quota.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "utilities"))

# Reusamos load_credentials/import_google_libs de upload_youtube.py.
from upload_youtube import load_credentials, import_google_libs  # noqa: E402

env = json.loads((REPO_ROOT / ".claude" / "settings.local.json").read_text(encoding="utf-8"))["env"]

# 3 entradas: (videoId, display_title nuevo, ruta thumbnail local)
UPDATES = [
    (
        "BFliK-JcwGc",
        "El humanoide que activó una alarma silenciosa contra el ministro al que sirve la cena",
        REPO_ROOT / "assets/audio/ficciones/covers/la-objecion-yt-1280x720.png",
    ),
    (
        "OgWaX-rcVfU",
        "El operador en Manila que afina el ruido del robot para que el niño se despierte",
        REPO_ROOT / "assets/audio/ficciones/covers/el-operador-nocturno-yt-1280x720.png",
    ),
    (
        "rQsqXqj-Uyw",
        "La hija que cada mañana programa al humanoide para que sea el padre muerto de su madre",
        REPO_ROOT / "assets/audio/ficciones/covers/el-que-viene-a-tomar-cafe-yt-1280x720.png",
    ),
]


def main() -> None:
    creds = load_credentials(env)
    _Cred, _Req, _Flow, build, _HttpErr, MediaFileUpload = import_google_libs()
    youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)

    for video_id, new_title, thumb_path in UPDATES:
        if not thumb_path.exists():
            sys.exit(f"FAIL: thumbnail no existe: {thumb_path}")

        # Paso 1: leer snippet existente (necesario porque videos.update con
        # part=snippet exige enviar TODO el snippet — si mandas solo title,
        # YouTube vacía description/tags/categoryId).
        resp = youtube.videos().list(part="snippet", id=video_id).execute()
        items = resp.get("items", [])
        if not items:
            sys.exit(f"FAIL: video no encontrado: {video_id}")
        snippet = items[0]["snippet"]
        old_title = snippet.get("title", "")

        # Mutación local: solo title cambia.
        snippet["title"] = new_title

        # Paso 2: update title.
        print(f"\n[{video_id}]")
        print(f"  Old title: {old_title}")
        print(f"  New title: {new_title}")
        youtube.videos().update(
            part="snippet",
            body={"id": video_id, "snippet": snippet},
        ).execute()
        print(f"  ✓ title actualizado ({len(new_title)} chars)")

        # Paso 3: thumbnail set.
        media = MediaFileUpload(str(thumb_path), mimetype="image/png", resumable=False)
        youtube.thumbnails().set(videoId=video_id, media_body=media).execute()
        print(f"  ✓ thumbnail subida ({thumb_path.stat().st_size // 1024} KB)")

    print("\n✅ 3 vídeos actualizados (title + thumbnail). Coste API ~300 units.")


if __name__ == "__main__":
    main()
