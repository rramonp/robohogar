"""
Sube un MP4 de audiolibro a YouTube vía Data API v3 + asigna thumbnail custom.

Modos:
    python utilities/upload_youtube.py --auth
        Corre el primer OAuth flow: abre navegador, consent, guarda
        `youtube_token.json` en YOUTUBE_OAUTH_TOKEN_PATH (gitignored).
        Solo se hace una vez por dispositivo.

    python utilities/upload_youtube.py <slug>
        Lee MP4 + thumbnail + metadata derivada del relato (frontmatter +
        chunks-index.json) y publica en YouTube. Imprime videoId + URL.

    python utilities/upload_youtube.py <slug> --private
        Igual pero con privacyStatus="private" — útil para test sin exponer
        el vídeo al feed del canal.

Inputs implícitos (según el slug):
  - `assets/audio/ficciones/<slug>-youtube*.mp4` (la versión más reciente)
  - `assets/audio/ficciones/<slug>-chunks-index.json` (capítulos timestamped)
  - `assets/audio/ficciones/covers/<slug>-yt-1280x720.png` (thumbnail)
  - `content/ficciones/**/<slug>/*.md` (frontmatter para título + dek)

Coste API: `videos.insert` = 100 units. `thumbnails.set` = 50 units. Total
150 units por episodio. Quota daily YouTube = 10.000 → ~66 uploads/día holgados.

OAuth scope `youtube.upload` + `youtube.force-ssl` (los 2 son necesarios para
videos.insert con auto-publish + thumbnails.set).
"""

import json
import re
import sys
from pathlib import Path


# Defensive UTF-8 stdout para no romper en consolas Windows cp1252.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


REPO_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_FILE = REPO_ROOT / ".claude" / "settings.local.json"
AUDIO_DIR = REPO_ROOT / "assets" / "audio" / "ficciones"
COVERS_DIR = AUDIO_DIR / "covers"
FICTIONS_ROOT = REPO_ROOT / "content" / "ficciones"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

# CategoryId 22 = "People & Blogs", 24 = "Entertainment". Para audiolibros
# de ficción `24` encaja mejor que `22` que es más vlog/personal. YouTube
# usa esto como pista weak para recomendaciones.
DEFAULT_CATEGORY_ID = "24"

# Mapping serie-slug → nombre legible para el título de YouTube. Las series con
# acrónimos o nombres compuestos no se derivan bien por Title-case automático,
# así que mantenemos un mapping explícito. Añadir entrada cuando se cree serie nueva.
SERIES_DISPLAY_NAMES = {
    "cartas-a-maia": "Cartas a MAIA",
    "la-casa-de-amparo": "La Casa de Amparo",
    "cronicas-ronda-3": "Crónicas RONDA-3",
}


def build_youtube_title(frontmatter: dict) -> str:
    """Construye el título YouTube según el patrón canónico de Ficciones Domésticas.

    Reglas (decisión Rafael 2026-04-25):
      - **Plural OBLIGATORIO**: "Ficciones Domésticas", NO "Ficción Doméstica".
        Razones: (1) coincide con el nombre canónico de la serie en CLAUDE.md +
        bible + descripción del canal; (2) algoritmo YouTube agrupa contenido
        por strings repetidos en títulos — todos los relatos comparten esa
        cola y YouTube los ofrece como "siguiente vídeo" entre ellos.
      - **Hook primero, etiqueta después**: el título del relato va al inicio
        para crear curiosity gap (Mobile YouTube corta a ~60 chars; el hook
        debe estar a salvo en los primeros chars).
      - **Em-dash con espacios** (` — `) entre hook y serie. Permitido en
        títulos de YouTube (regla `editorial.md` solo prohíbe em-dash en
        trust-lines ≤15 palabras).

    3 patrones según el contexto del relato:

    | Caso | Patrón | Detección |
    |---|---|---|
    | Standalone | `{title} — Ficciones Domésticas` | `frontmatter.serie == "_one-shots"` o no definido |
    | Episodio serie | `{title} · {SerieDisplay} #{N} — Ficciones Domésticas` | `frontmatter.serie != "_one-shots"` y `frontmatter.episodio` numérico |
    | Piloto serie nueva | `{title} — Ficciones Domésticas · Piloto` | `frontmatter.tipo == "piloto"` (opt-in explícito) |

    Cap defensivo: 100 chars (límite YouTube). Si el título compuesto excede,
    truncar el hook (no la cola "Ficciones Domésticas") para preservar la
    palabra-marca al final.
    """
    relato_title = frontmatter.get("title", "Sin título").strip()
    serie = (frontmatter.get("serie") or "").strip()
    episodio = frontmatter.get("episodio")
    tipo = (frontmatter.get("tipo") or "").strip().lower()

    # Caso piloto (opt-in): frontmatter explícito tipo: piloto.
    if tipo == "piloto":
        suffix = " — Ficciones Domésticas · Piloto"
    # Caso episodio de serie con bible (slug de serie + episodio numérico).
    elif serie and serie != "_one-shots" and episodio is not None:
        serie_display = SERIES_DISPLAY_NAMES.get(serie, serie.replace("-", " ").title())
        suffix = f" · {serie_display} #{episodio} — Ficciones Domésticas"
    # Caso standalone (default — _one-shots o frontmatter sin serie).
    else:
        suffix = " — Ficciones Domésticas"

    title = relato_title + suffix
    if len(title) > 100:
        # Truncar el hook conservando la cola "Ficciones Domésticas".
        # Reservamos los chars del suffix + 1 elipsis "…" + corte del título.
        max_relato = 100 - len(suffix) - 1
        title = relato_title[:max_relato].rstrip() + "…" + suffix
    return title


# Tags por defecto que aplican a TODO audiolibro de Ficciones Domésticas.
# YouTube tags pesan menos que en 2015 pero siguen ayudando a discovery
# en búsqueda interna y en la categorización del algoritmo.
DEFAULT_TAGS = [
    "ficciones domésticas",
    "audiolibro",
    "ciencia ficción",
    "robótica",
    "robots domésticos",
    "ROBOHOGAR",
    "narrativa especulativa",
    "audiolibro español",
]


def load_env() -> dict:
    """Lee settings.local.json y valida las keys necesarias."""
    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: no existe {SETTINGS_FILE}")
    data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    env = data.get("env", {})
    required = ["YOUTUBE_OAUTH_CLIENT_SECRET_PATH", "YOUTUBE_OAUTH_TOKEN_PATH"]
    missing = [k for k in required if not env.get(k) or "REEMPLAZAR" in env.get(k, "")]
    if missing:
        sys.exit(
            f"ERROR: faltan en settings.local.json: {', '.join(missing)}\n"
            "Ver Docs/Guia Distribucion Audiolibros.md § Bloque 1.4."
        )
    return env


def import_google_libs():
    """Lazy import con mensaje amigable si las libs Google no están instaladas."""
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        from googleapiclient.http import MediaFileUpload
        return Credentials, Request, InstalledAppFlow, build, HttpError, MediaFileUpload
    except ImportError:
        sys.exit(
            "ERROR: faltan dependencias Google. Instala con:\n"
            "  pip install google-auth google-auth-oauthlib google-api-python-client"
        )


# ══════════════════════════════════════════════════════════════════════════
# OAuth flows
# ══════════════════════════════════════════════════════════════════════════

def run_initial_auth(env: dict) -> None:
    """Corre el OAuth flow manual la primera vez.

    Abre navegador del usuario, este consent → guarda token con refresh long-lived
    en el path configurado. Tras esto, el resto de invocaciones cargan y refrescan
    el token sin requerir interacción humana.

    Importante: el OAuth consent screen del proyecto Google Cloud DEBE estar
    en "In production", no "Testing", para que el refresh token no caduque a
    los 7 días — ver Docs/Guia Distribucion Audiolibros.md § Bloque 1.3.
    """
    Credentials, Request, InstalledAppFlow, build, HttpError, _ = import_google_libs()

    client_secret = Path(env["YOUTUBE_OAUTH_CLIENT_SECRET_PATH"])
    token_path = Path(env["YOUTUBE_OAUTH_TOKEN_PATH"])

    if not client_secret.exists():
        sys.exit(
            f"ERROR: no existe el client_secret en {client_secret}\n"
            "Descarga el JSON del OAuth client desde Google Cloud Console "
            "(Bloque 1.4 de la guia) y guardalo en esa ruta."
        )

    print(f"Cargando client_secret desde {client_secret}...")
    flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
    print("Abriendo navegador para autorizar... (consent screen Google)")
    # run_local_server arranca un servidor local efimero en localhost:8080,
    # Google redirige el OAuth callback ahí, captura el code y lo intercambia
    # por refresh+access tokens. Se cierra solo al terminar.
    creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")

    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(creds.to_json(), encoding="utf-8")
    print(f"  Token guardado en {token_path}")

    # Verificación inmediata: ping channels.list para confirmar que
    # autoriza correctamente.
    try:
        youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)
        resp = youtube.channels().list(part="snippet", mine=True).execute()
        title = resp["items"][0]["snippet"]["title"]
        print(f"  Canal autorizado: '{title}'")
    except HttpError as e:
        print(f"  WARNING: el token se guardo pero la verificacion fallo: {e}")
        print(f"  Corre `python utilities/verify_youtube_auth.py` para diagnosticar.")
    print()
    print("OAuth flow completado. Ya puedes usar `python utilities/upload_youtube.py <slug>`.")


def load_credentials(env: dict):
    """Carga el token persistido. Refresca si está expirado."""
    Credentials, Request, _, _, _, _ = import_google_libs()

    token_path = Path(env["YOUTUBE_OAUTH_TOKEN_PATH"])
    if not token_path.exists():
        sys.exit(
            f"ERROR: no existe token en {token_path}\n"
            "Corre primero: python utilities/upload_youtube.py --auth"
        )
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if creds.valid:
        return creds
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        token_path.write_text(creds.to_json(), encoding="utf-8")
        return creds
    sys.exit(
        "ERROR: credenciales invalidas. Re-autoriza:\n"
        "  python utilities/upload_youtube.py --auth"
    )


# ══════════════════════════════════════════════════════════════════════════
# Lectura del frontmatter del relato
# ══════════════════════════════════════════════════════════════════════════

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def find_relato_md(slug: str) -> Path:
    """Busca el .md fuente del relato en `content/ficciones/**/<slug>/`."""
    matches = list(FICTIONS_ROOT.glob(f"**/{slug}/*-{slug}.md"))
    if not matches:
        # Fallback: cualquier .md en el directorio del slug.
        matches = list(FICTIONS_ROOT.glob(f"**/{slug}/*.md"))
        # Filtrar fuera PASOS.md y otros markdown auxiliares.
        matches = [m for m in matches if m.stem.lower() not in {"pasos", "pasosgenerales", "readme"}]
    if not matches:
        sys.exit(f"ERROR: no se encontro markdown del relato para slug '{slug}' en {FICTIONS_ROOT}/")
    return matches[0]


def parse_frontmatter(md_path: Path) -> dict:
    """Parser muy simple de YAML frontmatter — extrae key: value de top-level.

    No usa PyYAML para no añadir dependencia. Asume valores string en una sola
    línea sin nested. Si necesitamos algo más sofisticado en el futuro,
    importar `yaml` opcional con fallback.
    """
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip().strip('"').strip("'")
        fm[key.strip()] = value
    return fm


# ══════════════════════════════════════════════════════════════════════════
# Construcción de metadata YouTube
# ══════════════════════════════════════════════════════════════════════════

def format_timestamp(seconds: float) -> str:
    """Formato MM:SS para chapters de YouTube (HH:MM:SS si pasa de 1h)."""
    s = int(round(seconds))
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def build_description(slug: str, frontmatter: dict, index_data: dict) -> str:
    """Construye la descripción YouTube con CTA newsletter en línea 1 + chapters.

    Patrón validado por research 2026: el link al newsletter va en la
    primera línea visible (~150 chars antes del "Show more"), seguido
    de chapters timestamped (mejoran retention + crean enlaces internos
    compartibles del estilo `youtube.com/watch?v=X&t=312s`).

    YouTube auto-genera chapters si la descripción contiene timestamps
    `MM:SS` con primer timestamp en `00:00` y al menos 3 entries.
    """
    # Hook narrativo del frontmatter (meta_description o subtitle).
    hook = frontmatter.get("meta_description") or frontmatter.get("subtitle") or ""

    # Build chapters block. Primer entry SIEMPRE 00:00 (requisito YouTube).
    intro_dur = index_data.get("intro_duration_seconds", 0)
    # Schema v2 separa silence_after_intro / silence_before_outro; v1 (la-objecion piloto)
    # solo tenía silence_duration_seconds. Compat fallback para no romper distribución del piloto.
    silence_after_intro = index_data.get(
        "silence_after_intro_seconds",
        index_data.get("silence_duration_seconds", 0),
    )
    silence_before_outro = index_data.get("silence_before_outro_seconds", 0)
    total_dur = index_data["total_duration_seconds"]
    outro_dur = index_data.get("outro_duration_seconds", 0)
    outro_start = total_dur - outro_dur if outro_dur > 0 else None

    chapter_lines = ["00:00 Intro"]
    for ch in index_data["chapters"]:
        ts = format_timestamp(ch["start_seconds"])
        chapter_lines.append(f"{ts} {ch['number']}. {ch['title']}")
    if outro_start:
        chapter_lines.append(f"{format_timestamp(outro_start)} Cierre")

    chapters_block = "\n".join(chapter_lines)

    # CTA newsletter: primera línea, link visible antes del Show more.
    cta = f"▶ Lee el relato completo + suscríbete al newsletter: https://robohogar.com/p/{slug}"

    description = f"""{hook}

{cta}

⏱ Capítulos:
{chapters_block}

———
Ficciones Domésticas: relatos de ciencia ficción próxima sobre robótica en el hogar.
Cada semana, junto al newsletter en robohogar.com.

#FiccionesDomesticas #ROBOHOGAR #Audiolibro #CienciaFiccion"""

    # YouTube acepta hasta 5000 chars en descripción. Cap defensivo a 4900.
    if len(description) > 4900:
        description = description[:4900].rstrip() + "..."
    return description


def build_pinned_comment_text(slug: str, frontmatter: dict) -> str:
    """Genera el texto del pinned comment para copy-paste manual.

    YouTube Data API NO permite postear/pinear comments desde una API key
    normal desde 2023 (scope OAuth restringido). El skill devuelve este
    string para que Rafael lo pegue manualmente — ~1 min de trabajo por
    release, aceptable.

    Patrón ganador (research 2026): pregunta o regalo concreto + link.
    Sin "BUY NOW" ni hype.
    """
    hook = frontmatter.get("meta_description", "")
    return f"""¿Te ha gustado el relato? Lee el texto completo (con notas finales del autor) y suscríbete al newsletter en robohogar.com — cada semana mando análisis de robótica doméstica + un relato nuevo de Ficciones Domésticas como este.

🔗 https://robohogar.com/p/{slug}"""


def find_latest_mp4(slug: str) -> Path:
    """Devuelve el MP4 más reciente del slug (-v3 > -v2 > sin versión)."""
    candidates = sorted(AUDIO_DIR.glob(f"{slug}-youtube*.mp4"), reverse=True)
    if not candidates:
        sys.exit(
            f"ERROR: no hay MP4 generado para '{slug}'.\n"
            f"Corre primero: python utilities/generate_youtube_video.py {slug}"
        )
    return candidates[0]


# ══════════════════════════════════════════════════════════════════════════
# Upload
# ══════════════════════════════════════════════════════════════════════════

def upload_video(creds, mp4: Path, thumbnail: Path, title: str,
                 description: str, tags: list[str], privacy: str) -> str:
    """Sube el MP4 + thumbnail. Devuelve videoId."""
    _, _, _, build, HttpError, MediaFileUpload = import_google_libs()

    youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)

    body = {
        "snippet": {
            "title": title[:100],  # YouTube cap 100 chars en title
            "description": description,
            "tags": tags,
            "categoryId": DEFAULT_CATEGORY_ID,
            "defaultLanguage": "es",
            "defaultAudioLanguage": "es",
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
            # license: "youtube" (default standard) o "creativeCommon".
            # ROBOHOGAR mantiene standard porque permite monetización futura
            # y no sacrifica reach del audiolibro.
            "license": "youtube",
            "embeddable": True,
            "publicStatsViewable": True,
        },
    }

    print(f"  Subiendo MP4 ({mp4.stat().st_size / 1024 / 1024:.1f} MB)...")
    media = MediaFileUpload(str(mp4), mimetype="video/mp4", resumable=True, chunksize=8 * 1024 * 1024)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    last_progress = -1
    while response is None:
        status, response = request.next_chunk()
        if status:
            progress = int(status.progress() * 100)
            # Solo imprime cada 10% para no spamear el log.
            if progress >= last_progress + 10:
                print(f"    Subido {progress}%...")
                last_progress = progress

    video_id = response["id"]
    print(f"  videos.insert OK -> videoId={video_id} (cost: 100 units)")

    # Subir thumbnail custom. thumbnails.set requiere youtube.upload scope.
    if thumbnail.exists():
        try:
            thumb_media = MediaFileUpload(str(thumbnail), mimetype="image/png")
            youtube.thumbnails().set(videoId=video_id, media_body=thumb_media).execute()
            print(f"  thumbnails.set OK ({thumbnail.name}, cost: 50 units)")
        except HttpError as e:
            # No abortamos — el vídeo ya está subido. Reportamos y seguimos.
            print(f"  WARNING: thumbnails.set fallo: {e}")
            print(f"  Sube el thumbnail manual desde YouTube Studio.")
    return video_id


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(
            f"Uso:\n"
            f"  python {sys.argv[0]} --auth         # Primer OAuth flow (1 vez)\n"
            f"  python {sys.argv[0]} <slug>         # Sube MP4 a YouTube\n"
            f"  python {sys.argv[0]} <slug> --private  # Sube como private (test)"
        )

    env = load_env()

    if args[0] == "--auth":
        run_initial_auth(env)
        return

    slug = args[0]
    privacy = "private" if "--private" in args else "public"

    print(f"Slug: {slug}")
    print(f"Privacy: {privacy}")
    print()

    # Localizar inputs.
    md = find_relato_md(slug)
    frontmatter = parse_frontmatter(md)
    print(f"Relato MD : {md.relative_to(REPO_ROOT)}")

    chunks_index_path = AUDIO_DIR / f"{slug}-chunks-index.json"
    if not chunks_index_path.exists():
        sys.exit(f"ERROR: falta {chunks_index_path.relative_to(REPO_ROOT)} (correr /audiobook-generate)")
    index_data = json.loads(chunks_index_path.read_text(encoding="utf-8"))

    mp4 = find_latest_mp4(slug)
    print(f"MP4       : {mp4.relative_to(REPO_ROOT)}")
    thumbnail = COVERS_DIR / f"{slug}-yt-1280x720.png"
    print(f"Thumbnail : {thumbnail.relative_to(REPO_ROOT)}")
    print()

    # Construir metadata.
    yt_title = build_youtube_title(frontmatter)
    description = build_description(slug, frontmatter, index_data)
    pinned_comment = build_pinned_comment_text(slug, frontmatter)

    print(f"Título YouTube: {yt_title} ({len(yt_title)} chars)")
    print(f"Descripción   : {len(description)} chars, {description.count(chr(10)) + 1} líneas")
    print()

    # Cargar credenciales y subir.
    creds = load_credentials(env)
    print("Subiendo a YouTube...")
    video_id = upload_video(
        creds, mp4, thumbnail, yt_title, description, DEFAULT_TAGS, privacy,
    )

    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print()
    print("=" * 72)
    print(f"YOUTUBE UPLOAD OK · {slug}")
    print("=" * 72)
    print(f"Video ID    : {video_id}")
    print(f"URL         : {video_url}")
    print(f"Privacy     : {privacy}")
    print(f"Título      : {yt_title}")
    print()
    print("ACCIÓN MANUAL — pegar este pinned comment en YouTube:")
    print("-" * 72)
    print(pinned_comment)
    print("-" * 72)
    print(f"\n  → Abrir {video_url}, comentar, click en 3-dots → Pin.")
    print("=" * 72)


if __name__ == "__main__":
    main()
