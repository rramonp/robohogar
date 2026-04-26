"""
Constantes compartidas entre los scripts de distribución de audiolibros.

Vive aquí (módulo independiente) para que `upload_youtube.py` y
`youtube_playlists.py` puedan importarlas sin ciclo. Mantener este archivo
fino — solo constantes de mapping/naming, no funciones con side effects.

Cuándo se actualiza:
  - Cada vez que se canoniza una serie nueva de Ficciones Domésticas con
    bible propia → añadir entrada al `SERIES_DISPLAY_NAMES` con su nombre
    legible (mayúsculas, acentos, acrónimos correctos). Sin entrada, el
    fallback hace title-case del slug — funciona pero menos pulido.
"""

# Mapping serie-slug → nombre legible. Usado en:
#   - utilities/upload_youtube.py § build_youtube_title (título del vídeo)
#   - utilities/youtube_playlists.py § assign_video_to_playlists (nombre de playlist)
# Las series con acrónimos o nombres compuestos no se derivan bien por
# title-case automático, así que mantenemos un mapping explícito.
SERIES_DISPLAY_NAMES = {
    "cartas-a-maia": "Cartas a MAIA",
    "la-casa-de-amparo": "La Casa de Amparo",
    "cronicas-ronda-3": "Crónicas RONDA-3",
}


# Convenciones de naming de playlists YouTube.
# Decisiones canónicas (Rafael 2026-04-26):
#   (a) Playlist master "Ficciones Domésticas" agrega TODOS los relatos
#       (cronológica por orden de inserción = orden de publicación).
#   (b) Separador middot ` · ` para coherencia con la convención de títulos
#       del skill (que usa middot entre hook y serie en el título YouTube).
#   (c) Orden por defecto = orden de inserción al añadir vídeo. Sin
#       reordenamientos automáticos.
#
# Estructura resultante por relato:
#   - Standalone (one-shot): master + "Ficciones Domésticas · One-shots"
#   - Episodio de serie    : master + "Ficciones Domésticas · <SerieDisplay>"
#   - Piloto de serie nueva: master + playlist de la serie (si tiene `serie`)
#                            o master + One-shots (si solo `tipo: piloto`)

# Playlist que contiene TODOS los relatos publicados como audiolibro.
# Discovery primario del catálogo entero — apuntar desde landing/about del canal.
PLAYLIST_MASTER_TITLE = "Ficciones Domésticas"
PLAYLIST_MASTER_DESCRIPTION = (
    "Audiolibros de Ficciones Domésticas — relatos de ciencia ficción próxima "
    "sobre robótica en el hogar. Catálogo completo en orden cronológico de "
    "publicación. Cada semana, junto al newsletter en robohogar.com."
)

# Playlist específica de standalones (one-shots, sin serie).
PLAYLIST_ONESHOTS_TITLE = "Ficciones Domésticas · One-shots"
PLAYLIST_ONESHOTS_DESCRIPTION = (
    "Relatos standalone de Ficciones Domésticas — historias autoconclusivas "
    "que no forman parte de ninguna serie. Cada audiolibro completo, narrado, "
    "con notas finales del autor en robohogar.com."
)

# Prefijo para playlists de series (concat con el SERIES_DISPLAY_NAMES).
# Ej: "Ficciones Domésticas · Cartas a MAIA"
PLAYLIST_SERIE_PREFIX = "Ficciones Domésticas · "


def playlist_title_for_serie(serie_slug: str) -> str:
    """Devuelve el título canónico de la playlist YouTube para una serie.

    Args:
        serie_slug: slug de la serie (ej: "cartas-a-maia").

    Returns:
        Título canónico (ej: "Ficciones Domésticas · Cartas a MAIA").
        Si la serie no está en SERIES_DISPLAY_NAMES, fallback a title-case
        del slug — funciona pero menos pulido.
    """
    serie_display = SERIES_DISPLAY_NAMES.get(
        serie_slug, serie_slug.replace("-", " ").title()
    )
    return f"{PLAYLIST_SERIE_PREFIX}{serie_display}"


def playlist_description_for_serie(serie_slug: str) -> str:
    """Descripción canónica de la playlist para una serie."""
    serie_display = SERIES_DISPLAY_NAMES.get(
        serie_slug, serie_slug.replace("-", " ").title()
    )
    return (
        f"Audiolibros de la serie {serie_display} — Ficciones Domésticas. "
        f"Episodios completos en orden cronológico. Cada audiolibro narrado, "
        f"con notas finales del autor en robohogar.com."
    )
