"""
Helper de gestión de playlists YouTube para audiolibros de Ficciones Domésticas.

Tres responsabilidades:
  1. `ensure_playlist()` — busca por título exacto en el canal del usuario;
     si existe, devuelve su id. Si no, la crea con `playlists.insert`.
     Idempotente — re-llamarlo no duplica.
  2. `add_video_to_playlist()` — añade un vídeo a una playlist solo si no
     está ya en ella. Idempotente vía `playlistItems.list` filtrado por
     videoId + playlistId antes de insertar.
  3. `assign_video_to_playlists()` — orquesta lo anterior según el frontmatter
     del relato:
       - SIEMPRE añade a la master "Ficciones Domésticas".
       - Si frontmatter.serie != "_one-shots" → añade a la playlist de la serie.
       - Else → añade a "Ficciones Domésticas · One-shots".

Coste API (irrelevante vs los 10.000 units/día):
  - playlists.list:        1 unit
  - playlists.insert:      50 units (solo primera vez por playlist)
  - playlistItems.list:    1 unit
  - playlistItems.insert:  50 units (cada vídeo añadido)

  Por relato nuevo en régimen estable:
    1 (list playlists) + 1*2 (list items en master + one-shots/serie)
    + 50*2 (insert items) = ~102 units. Trivial.

  Setup inicial con backfill de N vídeos existentes:
    50*K (crear K playlists nuevas) + 50*N*2 (insertar cada vídeo en master
    + su específica) ≈ 350-500 units para canal pequeño.

Decisiones canónicas en `utilities/audiobook_constants.py`:
  (a) Master playlist activa.
  (b) Separador middot.
  (c) Orden por defecto = orden de inserción.

Privacy: todas las playlists se crean con `privacyStatus="public"`. Si en
el futuro se quiere usar para drafts/internas, pasar privacy explícito.

Uso programático:

    from googleapiclient.discovery import build
    from utilities.youtube_playlists import assign_video_to_playlists

    youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)
    result = assign_video_to_playlists(
        youtube,
        video_id="OgWaX-rcVfU",
        frontmatter={"serie": "_one-shots", ...},
    )
    # result = {
    #     "Ficciones Domésticas":          {"playlist_id": "PL...", "playlist_was_created": False, "video_was_added": True},
    #     "Ficciones Domésticas · One-shots": {"playlist_id": "PL...", "playlist_was_created": False, "video_was_added": True},
    # }

Llamado desde:
  - utilities/upload_youtube.py § main (paso post-thumbnail).
  - utilities/backfill_youtube_playlists.py (script de mantenimiento).
"""

import sys
import time
from typing import Optional

from audiobook_constants import (
    PLAYLIST_MASTER_TITLE,
    PLAYLIST_MASTER_DESCRIPTION,
    PLAYLIST_ONESHOTS_TITLE,
    PLAYLIST_ONESHOTS_DESCRIPTION,
    playlist_title_for_serie,
    playlist_description_for_serie,
)


# Privacy default para playlists nuevas. ROBOHOGAR usa siempre public — los
# audiolibros son contenido público para discovery. Si en el futuro se
# necesitan playlists privadas (drafts internos, listas de testing), pasar
# privacy="private" o "unlisted" explícito a ensure_playlist().
DEFAULT_PRIVACY_STATUS = "public"

# Idioma por defecto del canal — coincide con el del vídeo y la descripción.
DEFAULT_LANGUAGE = "es"


# ══════════════════════════════════════════════════════════════════════════
# Listado de playlists del canal con paginación
# ══════════════════════════════════════════════════════════════════════════


def list_my_playlists(youtube) -> list[dict]:
    """Lista TODAS las playlists del canal autenticado, paginando si hace falta.

    Cada item devuelto contiene:
      - id: playlist ID (PL...)
      - snippet: título, descripción, channelId, etc.
      - status: privacyStatus
      - contentDetails: itemCount

    Uso típico: buscar por título exacto antes de crear.
    Coste: 1 unit por página (50 playlists/página). Canal pequeño = 1 unit.
    """
    playlists = []
    page_token = None
    while True:
        request = youtube.playlists().list(
            part="snippet,status,contentDetails",
            mine=True,
            maxResults=50,
            pageToken=page_token,
        )
        response = request.execute()
        playlists.extend(response.get("items", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return playlists


# ══════════════════════════════════════════════════════════════════════════
# Ensure playlist (idempotente: busca por título exacto, crea si no existe)
# ══════════════════════════════════════════════════════════════════════════


def ensure_playlist(
    youtube,
    title: str,
    description: str = "",
    privacy: str = DEFAULT_PRIVACY_STATUS,
) -> tuple[str, bool]:
    """Devuelve `(playlist_id, was_created)` para una playlist con el título dado.

    Si ya existe en el canal una playlist con `snippet.title == title` (match
    exacto, case-sensitive, con espacios y middot literales), devuelve su
    id y `was_created=False`. Si no existe, la crea con `playlists.insert`
    y devuelve el id nuevo + `was_created=True`.

    El match es por título porque YouTube no permite filtrar `playlists.list`
    por título — hay que listar todas y comparar. Para canales con <50
    playlists es 1 unit total. Si en algún momento Rafael crea cientos de
    playlists, considerar cache local del id por título.

    Idempotente: re-llamadas con el mismo título no duplican.
    """
    existing = list_my_playlists(youtube)
    for pl in existing:
        if pl["snippet"]["title"] == title:
            return pl["id"], False

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "defaultLanguage": DEFAULT_LANGUAGE,
        },
        "status": {
            "privacyStatus": privacy,
        },
    }
    request = youtube.playlists().insert(part="snippet,status", body=body)
    response = request.execute()
    return response["id"], True


# ══════════════════════════════════════════════════════════════════════════
# Add video to playlist (idempotente: skip si el vídeo ya está dentro)
# ══════════════════════════════════════════════════════════════════════════


def find_video_in_playlist(youtube, playlist_id: str, video_id: str) -> Optional[str]:
    """Devuelve el `playlistItem.id` si el vídeo ya está en la playlist; si no, None.

    `playlistItems.list` con `playlistId=...` + `videoId=...` filtra
    server-side a la combinación exacta — devuelve 0 o 1 items. Coste: 1 unit.
    """
    response = youtube.playlistItems().list(
        part="id,snippet",
        playlistId=playlist_id,
        videoId=video_id,
        maxResults=1,
    ).execute()
    items = response.get("items", [])
    if items:
        return items[0]["id"]
    return None


def _raw_insert_video(youtube, playlist_id: str, video_id: str) -> str:
    """`playlistItems.insert` raw, sin chequeo previo de existencia.

    Uso interno: se llama cuando ya sabemos que el vídeo no está en la
    playlist (porque la acabamos de crear, o porque el find ya devolvió None).
    Devuelve el `playlistItem.id` del item nuevo. 50 units.
    """
    body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": video_id,
            },
        },
    }
    request = youtube.playlistItems().insert(part="snippet", body=body)
    response = request.execute()
    return response["id"]


def _insert_with_retry_on_404(
    youtube,
    playlist_id: str,
    video_id: str,
    max_attempts: int = 4,
    base_delay: float = 1.5,
) -> str:
    """Insert con retry exponencial cuando YouTube devuelve 404 transitorio.

    Tras `playlists.insert`, YouTube tarda ~1-3 s en hacer la playlist
    findable por las APIs de `playlistItems`. En ese intervalo cualquier
    operación devuelve `404 playlistNotFound` aunque la playlist exista.
    Reintentamos con delay creciente — todos los intentos tras el primero
    suelen ser instantáneos a partir del segundo 3.

    Si el 404 persiste tras `max_attempts`, propagamos el error: no es un
    problema de propagación, es algo más serio (playlist borrada manualmente
    entre llamadas, scopes incorrectos, etc.).
    """
    # Lazy import para evitar dependencia hard si solo se usa el módulo
    # para naming y routing puros.
    from googleapiclient.errors import HttpError

    last_err = None
    for attempt in range(max_attempts):
        try:
            return _raw_insert_video(youtube, playlist_id, video_id)
        except HttpError as e:
            if e.resp.status != 404:
                # Error real: scopes, vídeo inválido, etc. No reintentar.
                raise
            last_err = e
            delay = base_delay * (attempt + 1)
            print(f"    (404 transitorio post-create, esperando {delay:.1f}s y reintentando...)")
            time.sleep(delay)
    # Si llegamos aquí los retries no resolvieron el 404.
    raise last_err  # type: ignore[misc]


def add_video_to_playlist(
    youtube,
    playlist_id: str,
    video_id: str,
    skip_existence_check: bool = False,
) -> tuple[str, bool]:
    """Añade `video_id` a `playlist_id`. Idempotente.

    Devuelve `(playlist_item_id, was_added)`:
      - Si el vídeo ya estaba en la playlist → devuelve su playlistItem.id
        existente con `was_added=False` (no consume insert quota).
      - Si no estaba → `playlistItems.insert` y devuelve el id nuevo con
        `was_added=True`.

    Costes:
      - Skip path: 1 unit (find_video_in_playlist).
      - Insert path: 1 + 50 = 51 units.

    `skip_existence_check=True` salta el `find_video_in_playlist` y va
    directo al insert. Útil cuando el caller sabe que la playlist está
    vacía (recién creada). Ahorra 1 unit y evita el bug de propagación
    de YouTube post-create (ver `_insert_with_retry_on_404`).
    """
    if not skip_existence_check:
        existing_item_id = find_video_in_playlist(youtube, playlist_id, video_id)
        if existing_item_id:
            return existing_item_id, False

    new_item_id = _insert_with_retry_on_404(youtube, playlist_id, video_id)
    return new_item_id, True


# ══════════════════════════════════════════════════════════════════════════
# Routing por frontmatter (la pieza que pega todo)
# ══════════════════════════════════════════════════════════════════════════


def _normalized_serie(frontmatter: dict) -> str:
    """Devuelve el slug de serie normalizado, o cadena vacía si es one-shot.

    YAML acepta varios placeholders para "sin valor": `null`, `~`, `None`, o
    el campo entero ausente. Además convivimos con `_one-shots` explícito.
    Todos esos casos se tratan como equivalentes a "no es de ninguna serie".
    """
    raw = (frontmatter.get("serie") or "").strip()
    if raw.lower() in ("", "_one-shots", "null", "none", "~"):
        return ""
    return raw


def determine_target_playlists(frontmatter: dict) -> list[tuple[str, str]]:
    """Decide a qué playlists debe añadirse este relato.

    Reglas (decisión Rafael 2026-04-26):
      - SIEMPRE: master "Ficciones Domésticas" (todos los relatos).
      - Si frontmatter declara serie con slug real (no placeholder):
           → playlist específica de la serie.
      - Else (one-shot, placeholder YAML `null`/`~`/`None`, o `_one-shots`):
           → "Ficciones Domésticas · One-shots".

    Devuelve lista de tuplas `(playlist_title, playlist_description)`.

    Casos edge:
      - `tipo: piloto` con serie definida → entra a la playlist de la serie
        (es el primer episodio, encaja en el universo).
      - `tipo: piloto` sin serie definida → entra a One-shots (es un
        standalone que podría convertirse en serie, pero hoy no lo es).
    """
    serie = _normalized_serie(frontmatter)

    targets = [(PLAYLIST_MASTER_TITLE, PLAYLIST_MASTER_DESCRIPTION)]

    if serie:
        targets.append((
            playlist_title_for_serie(serie),
            playlist_description_for_serie(serie),
        ))
    else:
        targets.append((PLAYLIST_ONESHOTS_TITLE, PLAYLIST_ONESHOTS_DESCRIPTION))

    return targets


def assign_video_to_playlists(
    youtube,
    video_id: str,
    frontmatter: dict,
    verbose: bool = True,
) -> dict[str, dict]:
    """Asigna un vídeo a TODAS las playlists que le tocan según su frontmatter.

    Args:
        youtube: cliente youtube ya autenticado (build("youtube", "v3", credentials=...)).
        video_id: id del vídeo recién subido (o existente para backfill).
        frontmatter: dict del frontmatter del .md del relato. Solo necesita
            `serie` (string opcional). Sin él, asume one-shot.
        verbose: imprime progreso a stdout (default True).

    Returns:
        dict {playlist_title: {playlist_id, playlist_was_created, video_was_added}}
        para cada playlist tocada. Útil para el snapshot de distribución.

    Idempotente: re-llamarlo con el mismo video_id no duplica nada — las
    playlists existentes se reutilizan, y los items ya presentes se
    detectan vía `find_video_in_playlist` antes de insertar.
    """
    targets = determine_target_playlists(frontmatter)
    result = {}

    for title, description in targets:
        if verbose:
            print(f"  Playlist: {title}")
        playlist_id, was_created = ensure_playlist(youtube, title, description)
        if verbose:
            tag = "CREADA" if was_created else "existente"
            print(f"    [{tag}] id={playlist_id}")

        # Si la playlist se acaba de crear sabemos que está vacía → saltamos
        # el find (ahorra 1 unit y evita el 404 transitorio post-create de
        # YouTube). El insert directo se protege con retry exponencial vía
        # `_insert_with_retry_on_404` para cubrir la ventana de propagación.
        item_id, was_added = add_video_to_playlist(
            youtube, playlist_id, video_id,
            skip_existence_check=was_created,
        )
        if verbose:
            tag = "AÑADIDO" if was_added else "ya estaba"
            print(f"    [{tag}] item_id={item_id}")

        result[title] = {
            "playlist_id": playlist_id,
            "playlist_was_created": was_created,
            "video_was_added": was_added,
            "item_id": item_id,
        }

    return result


# ══════════════════════════════════════════════════════════════════════════
# Helpers de URL pública (para reportar al chat)
# ══════════════════════════════════════════════════════════════════════════


def playlist_public_url(playlist_id: str) -> str:
    """URL pública de una playlist YouTube."""
    return f"https://www.youtube.com/playlist?list={playlist_id}"


# ══════════════════════════════════════════════════════════════════════════
# CLI standalone (debug / smoke test manual)
# ══════════════════════════════════════════════════════════════════════════


def _cli_smoke_test():
    """Smoke test manual: lista playlists del canal autenticado.

    Uso: `python utilities/youtube_playlists.py`. Requiere OAuth ya hecho
    (`python utilities/upload_youtube.py --auth` corrido previamente).
    """
    # Defensive UTF-8 stdout (consolas Windows cp1252).
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    # Lazy import: evitar dependencia hard cuando se importa el módulo
    # solo para usar funciones puras (sin networking).
    from googleapiclient.discovery import build
    from upload_youtube import load_credentials, load_env

    env = load_env()
    creds = load_credentials(env)
    youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)

    print("Playlists del canal:")
    playlists = list_my_playlists(youtube)
    if not playlists:
        print("  (ninguna)")
        return
    for pl in playlists:
        title = pl["snippet"]["title"]
        item_count = pl["contentDetails"]["itemCount"]
        privacy = pl["status"]["privacyStatus"]
        print(f"  - {title} · {item_count} items · {privacy} · {pl['id']}")


if __name__ == "__main__":
    _cli_smoke_test()
