"""
validators.py — Checks pre-export sobre el HTML generado para tangibles ROBOHOGAR.

Implementa las reglas duras de `@rules/tangibles.md` § Reglas operativas y
de la memoria `feedback_tangible_no_promises_no_byline.md`:

Prohibiciones en PDFs tangibles:
  1. Listas de próximos tangibles ("Próximos tangibles para suscriptores...").
  2. Promesas de fechas de revisión ("Próxima revisión octubre 2026",
     "actualizamos cada 6 meses", "Los suscriptores reciben la v2, v3...").
  3. Byline personal "Rafael de ROBOHOGAR" (permitido en artículos, no en PDF).

Si cualquier patrón matchea → `ValidationError` y bloquea la generación del PDF.
Rafael lo corrige y re-ejecuta; sin bypass.

Fuente de la regla: Rafael 2026-04-18 durante afinación de Hoja de Compra v2.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


# ──────────────────────────────────────────────────────────────
# Patrones prohibidos — regex compiladas una vez
# ──────────────────────────────────────────────────────────────

# Insensitive + multi-línea. Cada tupla: (nombre_regla, patrón, hint_para_corregir)
_FORBIDDEN_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    (
        "roadmap_proximos_tangibles",
        re.compile(r"Pr[oó]ximos\s+tangibles", re.IGNORECASE),
        'Quitar la lista de "Próximos tangibles para suscriptores..." — sustituir por invitación a compartir.',
    ),
    (
        "promesa_revision_fecha",
        re.compile(r"Pr[oó]xima\s+revisi[oó]n\s+prevista", re.IGNORECASE),
        'Eliminar la promesa de fecha ("Próxima revisión prevista: octubre 2026"). Bloque dark debe ser invitación, no contrato.',
    ),
    (
        "promesa_actualizacion_periodica",
        re.compile(r"actualizamos\s+cada\s+\d+\s+mes", re.IGNORECASE),
        'Eliminar "actualizamos cada N meses" — no prometer cadencia de revisión.',
    ),
    (
        "promesa_versiones_futuras",
        re.compile(r"reciben\s+la\s+v\d+\s*,\s*v\d+", re.IGNORECASE),
        'Eliminar "reciben la v2, v3 automáticamente" — no prometer versiones futuras.',
    ),
    (
        "promesa_expansion",
        re.compile(r"vamos\s+expandiendo", re.IGNORECASE),
        'Eliminar "lo vamos expandiendo" — no prometer expansión futura.',
    ),
    (
        "byline_personal",
        re.compile(r"Rafael\s+de\s+ROBOHOGAR", re.IGNORECASE),
        'Eliminar byline "Rafael de ROBOHOGAR" del PDF. Firma correcta: solo "ROBOHOGAR". (La byline sí permitida en artículos Beehiiv.)',
    ),
]


# ──────────────────────────────────────────────────────────────
# API
# ──────────────────────────────────────────────────────────────

@dataclass
class ValidationIssue:
    """Un incumplimiento encontrado en el HTML."""
    rule: str
    match_snippet: str
    line_hint: int | None
    hint: str

    def format(self) -> str:
        line_txt = f" (línea {self.line_hint})" if self.line_hint else ""
        return f"  • [{self.rule}]{line_txt} → «{self.match_snippet}»\n    Hint: {self.hint}"


class ValidationError(Exception):
    """Lanzada cuando el HTML viola alguna regla dura de tangibles."""
    def __init__(self, issues: list[ValidationIssue]):
        self.issues = issues
        header = f"❌ Validación bloqueada: {len(issues)} regla(s) incumplida(s) en el HTML del tangible.\n"
        body = "\n".join(i.format() for i in issues)
        tail = "\n\nReferencia: @rules/tangibles.md § Reglas operativas + feedback_tangible_no_promises_no_byline.md"
        super().__init__(header + body + tail)


def validate_html(html_content: str) -> list[ValidationIssue]:
    """
    Corre todas las reglas duras contra el HTML.
    Devuelve lista de issues (vacía si todo pasa).
    """
    issues: list[ValidationIssue] = []
    lines = html_content.splitlines()

    for rule_name, pattern, hint in _FORBIDDEN_PATTERNS:
        for i, line in enumerate(lines, start=1):
            m = pattern.search(line)
            if m:
                # Snippet con contexto razonable, recortado
                snippet = line.strip()
                if len(snippet) > 100:
                    # Intentamos centrar el match
                    start = max(0, m.start() - 40)
                    end = min(len(snippet), m.end() + 40)
                    snippet = ("…" if start > 0 else "") + snippet[start:end] + ("…" if end < len(line) else "")
                issues.append(ValidationIssue(
                    rule=rule_name,
                    match_snippet=snippet,
                    line_hint=i,
                    hint=hint,
                ))

    return issues


def validate_html_or_raise(html_path: Path) -> None:
    """Lee el HTML del disk y levanta ValidationError si falla."""
    html = html_path.read_text(encoding="utf-8")
    issues = validate_html(html)
    if issues:
        raise ValidationError(issues)


# ──────────────────────────────────────────────────────────────
# CLI — para invocación manual de validación
# ──────────────────────────────────────────────────────────────

def _main_cli() -> None:
    import sys

    if len(sys.argv) != 2:
        print("Uso: python validators.py <archivo.html>", file=sys.stderr)
        sys.exit(1)

    html_path = Path(sys.argv[1])
    if not html_path.exists():
        print(f"ERROR: no existe {html_path}", file=sys.stderr)
        sys.exit(1)

    try:
        validate_html_or_raise(html_path)
        print(f"✓ {html_path.name} pasa todas las reglas de tangibles.")
    except ValidationError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    _main_cli()
