"""
skills.pdf_brand — Skill ROBOHOGAR para generar tangibles (lead magnets) en PDF con marca.

API pública:
    render_cheatsheet(data, output_dir=None, force=False, skip_pdf=False)
        Renderiza la variante `cheatsheet` (2-páginas de items + portada + backcover).
        Variante más común: preguntas-antes-de-comprar, dossiers "N datos clave",
        cheatsheets de 5-7 minutos.

    validate_html(html_content) / validate_html_or_raise(html_path)
        Runs the hard-rule check contra `@rules/tangibles.md`.
        Lanzan ValidationError si el HTML viola prohibiciones (roadmap futuro,
        fechas de revisión, byline personal).

Variantes futuras (F4C expansion):
    render_comparativa(data)  — tablas standalone de benchmark
    render_guia(data)         — guías step-by-step (primeros 30 días, glosarios)
    render_relato(data)       — ficciones ilustradas (dossier Ficciones Domésticas)

Fuente de verdad del diseño: el v2 validado de `content/lead-magnets/hoja-compra/`
(2026-04-18). Cualquier ajuste visual al template debe propagarse a todos los
tangibles generados con una re-ejecución del skill.
"""

from .render import render_cheatsheet
from .validators import (
    ValidationError,
    ValidationIssue,
    validate_html,
    validate_html_or_raise,
)

__all__ = [
    "render_cheatsheet",
    "validate_html",
    "validate_html_or_raise",
    "ValidationError",
    "ValidationIssue",
]
