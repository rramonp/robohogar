"""
render.py — Renderiza un tangible cheatsheet a HTML + PDF.

Orquesta:
  1. Toma un dict `data` validado con los campos del template Jinja2.
  2. Calcula páginas automáticamente (portada + N páginas de items + backcover).
  3. Renderiza el template Jinja2.
  4. Corre validator pre-export (prohibiciones duras).
  5. Exporta a PDF vía Playwright Chromium (reusa utilities/pdf_export.py lógica).

Contract del dict `data` — ver `variantes/cheatsheet_schema.md` para referencia
completa. Campos obligatorios mínimos:
  - slug: str                          (ej. "hoja-compra")
  - version: str                       (ej. "v1", "v2", "v3")
  - title_big: str                     (primera línea del H1 portada)
  - subtitle: str                      (subtítulo portada)
  - items: list[dict]                  (lista de ítems/preguntas)

Campos opcionales relevantes:
  - title_small, descriptor, intro_paragraphs, decorative_number
  - backcover_title, backcover_lead, anexo, close_hook, resources, disclaimer
  - items_per_page (default 5), date_label (default auto)

Output:
  - content/lead-magnets/<slug>/<slug>-robohogar-<version>.html
  - content/lead-magnets/<slug>/<slug>-robohogar-<version>.pdf

No sobreescribe versiones: si el archivo existe y force=False, error.
"""

from __future__ import annotations

import math
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .validators import validate_html_or_raise


# ──────────────────────────────────────────────────────────────
# Paths del skill
# ──────────────────────────────────────────────────────────────

_SKILL_ROOT = Path(__file__).parent
_TEMPLATES_DIR = _SKILL_ROOT / "templates"
_ASSETS_DIR = _SKILL_ROOT / "assets"
_REPO_ROOT = _SKILL_ROOT.parent.parent  # skills/pdf_brand/../../ = repo root


# ──────────────────────────────────────────────────────────────
# Mes en español (para date_label automático)
# ──────────────────────────────────────────────────────────────

_MESES_ES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def _date_label_today() -> str:
    t = date.today()
    return f"{_MESES_ES[t.month - 1]} {t.year}"


# ──────────────────────────────────────────────────────────────
# Helpers internos
# ──────────────────────────────────────────────────────────────

def _jinja_env() -> Environment:
    """Entorno Jinja2 con StrictUndefined para fallar al ver typos en el dict data."""
    return Environment(
        loader=FileSystemLoader(_TEMPLATES_DIR),
        undefined=StrictUndefined,
        autoescape=False,  # los strings del cliente pueden contener HTML intencional (links)
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _ensure_chromium_installed() -> None:
    """Playwright necesita Chromium la primera vez."""
    try:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium", "--with-deps"],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError:
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
        )


def _export_html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    """Carga el HTML en Chromium headless y exporta a PDF A4 (igual que utilities/pdf_export.py)."""
    from playwright.sync_api import sync_playwright

    html_uri = html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(html_uri, wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True,
        )
        browser.close()


def _stage_icon_robot(output_dir: Path) -> str:
    """
    Copia el icon-robot.png compartido a `<output_dir>/assets/` si no existe ya,
    y devuelve la ruta relativa al HTML (que vive en output_dir).
    """
    out_assets = output_dir / "assets"
    out_assets.mkdir(parents=True, exist_ok=True)
    dst = out_assets / "icon-robot.png"
    if not dst.exists():
        shutil.copy2(_ASSETS_DIR / "icon-robot.png", dst)
    # Ruta relativa desde el HTML al asset (mismo dir padre del HTML)
    return "assets/icon-robot.png"


def _compute_pagination(num_items: int, items_per_page: int) -> tuple[int, int]:
    """Devuelve (num_content_pages, total_pages = 1 portada + N content + 1 backcover)."""
    content_pages = max(1, math.ceil(num_items / items_per_page))
    total = 1 + content_pages + 1
    return content_pages, total


# ──────────────────────────────────────────────────────────────
# API pública
# ──────────────────────────────────────────────────────────────

def render_cheatsheet(
    data: dict,
    output_dir: Path | str | None = None,
    force: bool = False,
    skip_pdf: bool = False,
) -> tuple[Path, Path | None]:
    """
    Renderiza un tangible variante `cheatsheet` a HTML + PDF.

    Args:
        data: dict con los campos del template (ver contract en docstring del módulo).
        output_dir: directorio destino. Default: `content/lead-magnets/<slug>/`.
        force: si True, sobreescribe archivos existentes.
               Si False y el archivo existe, lanza FileExistsError.
        skip_pdf: si True, solo genera el HTML (útil para iterar CSS sin Playwright).

    Returns:
        (html_path, pdf_path). `pdf_path` es None si skip_pdf=True.

    Raises:
        ValueError: si `data` no cumple el contract.
        ValidationError: si el HTML viola alguna regla de @rules/tangibles.md.
        FileExistsError: si el archivo existe y force=False.
    """
    # ─── Defaults + validación de contract mínimo ──────────────
    required = ["slug", "version", "title_big", "subtitle", "items"]
    missing = [k for k in required if k not in data or data[k] in (None, "", [])]
    if missing:
        raise ValueError(f"Faltan campos obligatorios en data: {missing}")

    slug = data["slug"]
    version = data["version"]
    items = list(data["items"])
    items_per_page = int(data.get("items_per_page", 5))

    # Resolver output_dir
    if output_dir is None:
        output_dir = _REPO_ROOT / "content" / "lead-magnets" / slug
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Calcular paginación
    _, total_pages = _compute_pagination(len(items), items_per_page)

    # Asset icon-robot: copiar al output y devolver ruta relativa para el HTML
    icon_robot_rel = _stage_icon_robot(output_dir)

    # Montar contexto Jinja completando defaults no pasados por el usuario
    context = {
        "slug": slug,
        "version": version,
        "generated_date": date.today().isoformat(),
        "date_label": data.get("date_label") or _date_label_today(),

        # Portada
        "title_big": data["title_big"],
        "title_small": data.get("title_small", ""),
        "subtitle": data["subtitle"],
        "descriptor": data.get("descriptor"),
        "decorative_number": data.get("decorative_number"),
        "intro_paragraphs": data.get("intro_paragraphs", []),

        # Running header de páginas interiores
        "running_header_title": data.get(
            "running_header_title",
            f"{data['title_big']} {data.get('title_small', '')}".strip() + " ROBOHOGAR",
        ),

        # Sección items
        "items": items,
        "items_per_page": items_per_page,
        "items_section_title": data.get("items_section_title", "Lista"),
        "items_section_lead": data.get("items_section_lead"),
        "items_section_lead_cont": data.get("items_section_lead_cont"),

        # Back cover
        "backcover_title": data.get("backcover_title"),
        "backcover_lead": data.get("backcover_lead"),
        "anexo": data.get("anexo"),
        "close_hook": data.get("close_hook"),
        "resources": data.get("resources", []),
        "disclaimer": data.get("disclaimer"),

        # Assets
        "icon_robot_path": icon_robot_rel,

        # Paginación
        "total_pages": total_pages,
    }

    # ─── Render Jinja → HTML ──────────────────────────────────
    env = _jinja_env()
    template = env.get_template("cheatsheet.html.jinja2")
    html_content = template.render(**context)

    # ─── Persistir HTML ───────────────────────────────────────
    html_path = output_dir / f"{slug}-robohogar-{version}.html"
    if html_path.exists() and not force:
        raise FileExistsError(
            f"Ya existe {html_path}. Usa force=True para sobreescribir o incrementa la versión (v{int(version[1:]) + 1 if version.startswith('v') and version[1:].isdigit() else 'N+1'})."
        )
    html_path.write_text(html_content, encoding="utf-8")

    # ─── Validator pre-export (prohibiciones duras) ──────────
    validate_html_or_raise(html_path)

    # ─── Exportar PDF ────────────────────────────────────────
    if skip_pdf:
        return html_path, None

    pdf_path = output_dir / f"{slug}-robohogar-{version}.pdf"
    if pdf_path.exists() and not force:
        raise FileExistsError(
            f"Ya existe {pdf_path}. Usa force=True para sobreescribir o incrementa la versión."
        )

    _ensure_chromium_installed()
    _export_html_to_pdf(html_path, pdf_path)

    return html_path, pdf_path
