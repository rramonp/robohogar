# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "playwright",
# ]
# ///
"""
pdf_export.py — Exporta un HTML a PDF A4 usando Playwright Chromium headless.

Módulo base para la generación de tangibles ROBOHOGAR (lead magnets en PDF).
Prototipo del futuro skill `/pdf-brand` — por ahora se invoca directo con `uv run`.

Uso:
    uv run utilities/pdf_export.py <html_input> <pdf_output>

Ejemplo:
    uv run utilities/pdf_export.py \\
      content/lead-magnets/hoja-compra/hoja-compra-robohogar-v1.html \\
      content/lead-magnets/hoja-compra/hoja-compra-robohogar-v1.pdf

Dependencias:
    - playwright (browser Chromium instalado automáticamente en primer uso)
    - Ejecución offline tras descarga inicial de Chromium (~150 MB)

Config de impresión:
    - A4 portrait
    - Márgenes: gobierna el @page del CSS del HTML (aquí pasamos 0 para no pisarlo)
    - print_background=True para que salga el color ámbar del cover
    - wait_until='networkidle' para esperar carga de fuentes de Google Fonts

Razón de Playwright vs otras opciones:
    - Playwright renderiza con Chromium → misma fidelidad que Chrome/Edge en escritorio.
    - WeasyPrint tiene bugs con web fonts + @page complejos en 2026.
    - ReportLab exige API programática pesada, no reusa CSS del brand existente.
    - Pandoc + LaTeX es otro stack (LaTeX) con currva de aprendizaje.
"""

import subprocess
import sys
from pathlib import Path


# ──────────────────────────────────────────────────────────────
# Chequeo de dependencias: instalar browser Chromium la 1ª vez
# ──────────────────────────────────────────────────────────────

def ensure_chromium_installed():
    """
    Playwright necesita descargar Chromium la primera vez. Esto se hace con
    `playwright install chromium`. Si ya está instalado, el comando sale rápido.
    """
    try:
        # Invocamos como módulo para que use el mismo venv que uv gestiona
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium", "--with-deps"],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError:
        # Si falla `--with-deps` (ej. permisos sudo en Linux), reintentar sin
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
        )


# ──────────────────────────────────────────────────────────────
# Export principal
# ──────────────────────────────────────────────────────────────

def export_html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    """
    Carga el HTML en Chromium headless y exporta a PDF A4.

    Args:
        html_path: ruta absoluta o relativa al .html fuente
        pdf_path: ruta de salida del .pdf
    """
    from playwright.sync_api import sync_playwright  # noqa: import local para no fallar si no hay playwright

    # URI file:// requiere ruta absoluta y forward slashes (también en Windows)
    html_uri = html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Cargar HTML y esperar a que Google Fonts y cualquier asset externo se asiente
        page.goto(html_uri, wait_until="networkidle")

        # Exportar PDF. Márgenes a 0 porque el @page del CSS ya los controla.
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True,
        )

        browser.close()


# ──────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) != 3:
        print("Uso: uv run utilities/pdf_export.py <html_input> <pdf_output>", file=sys.stderr)
        sys.exit(1)

    html_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2])

    if not html_path.exists():
        print(f"ERROR: no existe el HTML: {html_path}", file=sys.stderr)
        sys.exit(1)

    # Asegurar que el directorio de salida existe
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"→ Instalando Chromium si hace falta...")
    ensure_chromium_installed()

    print(f"→ Exportando {html_path.name} a PDF...")
    export_html_to_pdf(html_path, pdf_path)

    size_kb = pdf_path.stat().st_size // 1024
    print(f"✓ Generado: {pdf_path}  ({size_kb} KB)")


if __name__ == "__main__":
    main()
