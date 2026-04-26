"""Hook PreToolUse(Write): bloquea sobrescritura de imágenes versionables.

Lee el evento JSON de stdin, mira tool_input.file_path. Si el path apunta a una
imagen dentro de assets/ o content/articulos/<slug>/assets/ Y el archivo destino
ya existe, devuelve exit code 2 (bloquea) con mensaje en stderr para que el modelo
renombre a -v2, -v3, etc.

En cualquier otro caso devuelve 0 (deja pasar).

Política heredada de feedback_never_overwrite_images.md: nunca sobrescribir hero
images ni assets generados; usar versionado -vN para iteración.
"""

import json
import os
import re
import sys


# Extensiones de imagen que entran en el enforce.
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


# Paths que entran en el enforce (relativos al root del repo). Si el file_path
# matchea uno de estos prefijos, aplicamos la regla anti-overwrite.
WATCHED_PREFIXES = (
    "assets/",
    "content/articulos/",
    "content/ficciones/",
)


def _normalize(path: str) -> str:
    """Normaliza path absoluto Windows a forma relativa con separador /, lowercase."""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", "")
    p = path.replace("\\", "/")
    if project_dir:
        prefix = project_dir.replace("\\", "/").rstrip("/") + "/"
        if p.lower().startswith(prefix.lower()):
            p = p[len(prefix):]
    return p


def _is_watched(rel_path: str) -> bool:
    rel_lower = rel_path.lower()
    if not any(rel_lower.startswith(p) for p in WATCHED_PREFIXES):
        return False
    return os.path.splitext(rel_lower)[1] in IMAGE_EXTS


def _suggest_versioned(path: str) -> str:
    """Sugiere -vN siguiente disponible: foo.png → foo-v2.png; foo-v2.png → foo-v3.png."""
    base, ext = os.path.splitext(path)
    m = re.search(r"-v(\d+)$", base)
    if m:
        next_n = int(m.group(1)) + 1
        candidate = f"{base[:-len(m.group(0))]}-v{next_n}{ext}"
    else:
        candidate = f"{base}-v2{ext}"
    while os.path.exists(candidate):
        m2 = re.search(r"-v(\d+)$", os.path.splitext(candidate)[0])
        next_n = int(m2.group(1)) + 1 if m2 else 2
        b2, e2 = os.path.splitext(candidate)
        candidate = re.sub(r"-v\d+$", f"-v{next_n}", b2) + e2
    return candidate


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # No bloqueamos si el input no es válido JSON.

    tool_input = event.get("tool_input") or {}
    file_path = tool_input.get("file_path") or tool_input.get("path") or ""
    if not file_path:
        return 0

    if not os.path.exists(file_path):
        return 0  # Crear nuevo archivo: OK.

    rel = _normalize(file_path)
    if not _is_watched(rel):
        return 0  # No es imagen vigilada (ej. .md, .py, .html): OK.

    suggested = _suggest_versioned(file_path)
    suggested_rel = _normalize(suggested)
    sys.stderr.write(
        f"BLOQUEADO: el asset '{rel}' ya existe.\n"
        f"Política ROBOHOGAR: no sobrescribir imágenes generadas. Usar versionado -vN.\n"
        f"Renombra el destino a: {suggested_rel}\n"
        f"Si la sobrescritura es intencional (ej. corrección de typo en un placeholder),\n"
        f"borra el archivo antiguo manualmente con git mv y vuelve a intentar.\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
