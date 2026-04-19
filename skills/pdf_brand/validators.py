"""
validators.py — Checks pre-export sobre el HTML generado para tangibles ROBOHOGAR.

Implementa las reglas duras de `@rules/tangibles.md` § Reglas operativas +
§ Microcopy de conversión y de las memorias:
  - feedback_tangible_no_promises_no_byline.md
  - feedback_microcopy_trust_lines.md

Prohibiciones en PDFs tangibles + fichas Beehiiv Digital Product:
  1. Listas de próximos tangibles ("Próximos tangibles para suscriptores...").
  2. Promesas de fechas de revisión ("Próxima revisión octubre 2026",
     "actualizamos cada 6 meses", "Los suscriptores reciben la v2, v3...").
  3. Byline personal "Rafael de ROBOHOGAR" (permitido en artículos, no en PDF).
  4. Microcopy de conversión — trust-lines bajo CTA (nuevo 2026-04-19):
     - Promesas de velocidad de entrega ("15 segundos", "llega al email en",
       "instantáneo", "al momento") — no controlamos la entrega Beehiiv.
     - Promesas de ausencia futura de publicidad ("sin publicidad",
       "sin promociones") — inconsistente con modelo (afiliados eventuales).
     - Copy vago ("sin letra pequeña", "sin trucos") — huele a marketer.
     - Hype anglosajón traducido ("Join N+ readers", "Don't miss out",
       "Apúntate ya") — incumple CTA no-spammy de Write With AI.

Si cualquier patrón matchea → `ValidationError` y bloquea la generación del PDF.
Rafael lo corrige y re-ejecuta; sin bypass.

Fuente de las reglas:
  - Rafael 2026-04-18 durante afinación de Hoja de Compra v2 (§ 1-3).
  - Rafael 2026-04-19 tras pedir best practices certificadas de microcopy (§ 4).
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
    # ── Microcopy de conversión (trust-lines bajo CTA) — 2026-04-19 ──
    # Prohibiciones heredadas de `@rules/tangibles.md § Microcopy de conversión`.
    # Aplican al HTML del PDF (si hay CTA embebido) Y a la ficha Beehiiv Digital Product.
    (
        "microcopy_velocidad_entrega",
        # Matches "15 segundos", "llega al email en X segundos", "instantáneo", "al momento".
        re.compile(r"\b(\d+\s*segundos|llega\s+al\s+email\s+en|instant[aá]neo|al\s+momento)\b", re.IGNORECASE),
        'Eliminar promesa de velocidad de entrega. No controlamos el tiempo de delivery de Beehiiv (30-90s reales + riesgo filtro Promotions). Reemplazar por trust-line canónica: "PDF gratis con tu suscripción semanal. Cancela cuando quieras.".',
    ),
    (
        "microcopy_sin_publicidad",
        # Matches "sin publicidad", "sin promociones", "sin spam comercial".
        re.compile(r"sin\s+(publicidad|promociones|spam\s+comercial)\b", re.IGNORECASE),
        'Eliminar promesa de ausencia futura de publicidad/promociones. Inconsistente con modelo ROBOHOGAR (afiliados eventuales en F2+).',
    ),
    (
        "microcopy_vago",
        # "sin letra pequeña", "sin trucos", "sin compromiso" genéricos.
        re.compile(r"sin\s+(letra\s+peque[ñn]a|trucos|compromiso)\b", re.IGNORECASE),
        'Copy vago. Sustituir por claim concreto (formato del tangible, baja fricción de salida, transparencia del vínculo).',
    ),
    (
        "microcopy_hype_anglo",
        # "Join N+ readers", "Don't miss out", "Apúntate ya!".
        re.compile(r"(join\s+\d[\d,\.k]*\+?\s*(readers|subscribers)|don.?t\s+miss\s+out|ap[uú]ntate\s+ya)", re.IGNORECASE),
        'Hype anglosajón / imperativo agresivo. Incumple CTA no-spammy de Write With AI. Reemplazar por trust-line editorial.',
    ),
    # ── Anti-anglicismos de apertura/cierre — 2026-04-19 ──
    # Validado contra 20 newsletters ES (Kloshletter, Suma Positiva, Xataka, EOM,
    # elDiario, etc.) — 0 apariciones de estos patterns.
    # Regla en `@rules/editorial.md § Apertura y cierre del cuerpo del email`.
    (
        "saludo_anglo_hola_nombre",
        # "Hola X," al inicio de línea — tic de traducción "Hi X,".
        # Excluye "Hola," suelto sin nombre (puede ser legítimo en ficción diálogo).
        re.compile(r"^\s*Hola\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s*[,!]", re.MULTILINE),
        'Saludo "Hola X," es tic anglo ("Hi X,"). Ningún newsletter ES auditado lo usa. Reemplazar por entrada directa al tema o "Buenos días." + primera frase.',
    ),
    (
        "saludo_anglo_espero_bien",
        # "Espero que estés bien" / "espero que te encuentres bien".
        re.compile(r"espero que (est[eé]s|te encuentres) bien", re.IGNORECASE),
        'Calco directo de "hope you\'re well". Ausente del 100% de newsletters ES auditados. Eliminar sin sustituir — el lector prefiere entrada directa.',
    ),
    (
        "saludo_anglo_querido_lector",
        # "Querido/a lector/a", "Queridos amigos".
        re.compile(r"Querid[oa]s?\s+(lector|lectora|amig[oa]s?)", re.IGNORECASE),
        'Registro de carta formal / "Dear reader". Newsletters ES usan apertura directa o "Buenos días." Prohibido en copy publicable.',
    ),
    (
        "saludo_anglo_hey",
        # "Hey," al inicio de párrafo/línea.
        re.compile(r"^\s*Hey\s*[,!]", re.MULTILINE | re.IGNORECASE),
        'Anglicismo puro sin traducir. No aparece en newsletters ES editoriales. Eliminar.',
    ),
    (
        "jerga_tangible_al_lector",
        # "el tangible", "este tangible", "nuestro tangible", etc. — determinante + "tangible".
        # NO bloquea nombres de marca ("TangibleFuture"), ni comentarios HTML, ni "tangibles" en plural
        # genérico del tipo "los tangibles PDF" (docs internos).
        re.compile(r"\b(este|esta|ese|esa|nuestro|nuestra|el|la|un|una)\s+tangible\b(?!\w)", re.IGNORECASE),
        '"Tangible" es jerga interna del pipeline ROBOHOGAR. El lector ES no la reconoce como categoría (0/20 newsletters auditados la usan en copy público). Sustituir por "PDF gratis", "guía gratis", "descargable" o el formato concreto ("checklist", "tabla").',
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
