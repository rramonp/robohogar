# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "jinja2",
#     "playwright",
# ]
# ///
"""
cli.py — Invocación CLI del skill pdf_brand para generar un tangible desde JSON/Python.

Uso:
    uv run skills/pdf_brand/cli.py cheatsheet <data_file.py>

Donde `data_file.py` es un Python file que define una variable `data: dict` con el
contract de `render_cheatsheet` (ver docstring en `render.py`).

Ejemplo mínimo:
    # data_hoja_compra.py
    data = {
        "slug": "hoja-compra",
        "version": "v3",
        "title_big": "Hoja de",
        "title_small": "Compra",
        "subtitle": "10 preguntas para no pagar de más...",
        "items": [...],
        # resto de campos opcionales
    }

Luego: `uv run skills/pdf_brand/cli.py cheatsheet data_hoja_compra.py`

El modo preferido de uso en el pipeline ROBOHOGAR es NO este CLI, sino la invocación
programática desde Claude vía la command `/pdf-brand cheatsheet <slug>` — Claude lee
el `contenido.md` del tangible, extrae estructura y llama a `render_cheatsheet(data)`
directamente. Este CLI es fallback manual para pruebas.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _load_data_module(py_path: Path) -> dict:
    """Carga un archivo Python por path y devuelve su variable `data`."""
    spec = importlib.util.spec_from_file_location("_tangible_data", py_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar {py_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "data"):
        raise AttributeError(f"{py_path} no define la variable `data`")
    return module.data


def main() -> None:
    if len(sys.argv) != 3:
        print("Uso: uv run skills/pdf_brand/cli.py <variante> <data_file.py>", file=sys.stderr)
        print("  variantes disponibles: cheatsheet", file=sys.stderr)
        sys.exit(1)

    variant = sys.argv[1]
    data_file = Path(sys.argv[2])

    if not data_file.exists():
        print(f"ERROR: no existe {data_file}", file=sys.stderr)
        sys.exit(1)

    # Añadir el repo root al sys.path para que funcione `from skills.pdf_brand import ...`
    _repo_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(_repo_root))

    from skills.pdf_brand import render_cheatsheet, ValidationError

    data = _load_data_module(data_file)

    try:
        if variant == "cheatsheet":
            html_path, pdf_path = render_cheatsheet(data, force=True)
        else:
            print(f"ERROR: variante desconocida '{variant}'. Solo 'cheatsheet' por ahora.", file=sys.stderr)
            sys.exit(1)
    except ValidationError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    print(f"✓ HTML: {html_path}")
    if pdf_path:
        print(f"✓ PDF:  {pdf_path}  ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
