"""sync_catalogs.py — auditoría de sincronización entre filesystem y catálogos.

Compara la realidad del repo (qué hay en `content/articulos/`, `content/published/`,
`content/ficciones/`, `assets/audio/ficciones/`) contra los 3 catálogos editoriales
(`registro-articulos.md`, `registro-ficciones.md`, `calendario-editorial.md`) y
emite un reporte de deltas en `content/pipeline-debug-reports/sync-catalogs-YYYY-MM-DD.md`.

Sin auto-fix: solo reporta. Rafael decide qué corregir.

Uso:
    python utilities/sync_catalogs.py
    python utilities/sync_catalogs.py --quiet   # solo reporta deltas, no narra los OK

Invocado opcionalmente desde `/pipeline-debug`. También útil como check rápido
antes de un commit grande o tras una sesión larga de publicación.

Dependencias: solo stdlib. No toca red. No escribe nada salvo el .md de reporte.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Windows default console encoding (cp1252) no soporta los emojis del reporte.
# Forzamos utf-8 en stdout/stderr para que el script funcione igual en Git Bash,
# PowerShell y CMD sin importar la configuración regional.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# ════════════════════════════════════════════════════════════════════════════
# Configuración: rutas raíz del repo y carpetas que se inspeccionan.
# ════════════════════════════════════════════════════════════════════════════

# El script vive en utilities/ — el repo root es el padre.
REPO_ROOT = Path(__file__).resolve().parent.parent

ARTICULOS_DIR = REPO_ROOT / "content" / "articulos"
PUBLISHED_DIR = REPO_ROOT / "content" / "published"
FICCIONES_DIR = REPO_ROOT / "content" / "ficciones"
LEAD_MAGNETS_DIR = REPO_ROOT / "content" / "lead-magnets"
AUDIO_DIR = REPO_ROOT / "assets" / "audio" / "ficciones"

REGISTRO_ARTICULOS = REPO_ROOT / "content" / "registro-articulos.md"
REGISTRO_FICCIONES = REPO_ROOT / "content" / "registro-ficciones.md"
CALENDARIO = REPO_ROOT / "content" / "calendario-editorial.md"

REPORTS_DIR = REPO_ROOT / "content" / "pipeline-debug-reports"

# Slugs de ficciones que viven explícitamente como drafts experimentales —
# no son "incompletos", son intencionalmente pre-publicación. Se leen del
# propio registro-ficciones.md (sección "Drafts experimentales") en runtime.


# ════════════════════════════════════════════════════════════════════════════
# Modelo del reporte: agrupamos hallazgos por severidad para que Rafael
# distinga lo que necesita acción inmediata de lo informativo.
# ════════════════════════════════════════════════════════════════════════════

@dataclass
class Report:
    """Acumula deltas detectados por el auditor."""

    # Cosas que parecen estar mal y bloquean / confunden el pipeline.
    deltas: list[str] = field(default_factory=list)
    # Cosas raras pero no urgentes (huérfanos, drafts viejos).
    warnings: list[str] = field(default_factory=list)
    # Verificaciones que pasaron, útiles para confirmar el estado sano.
    ok: list[str] = field(default_factory=list)

    def is_clean(self) -> bool:
        return not self.deltas and not self.warnings


# ════════════════════════════════════════════════════════════════════════════
# Lectura de los catálogos: extraemos los slugs canónicos para comparar.
# ════════════════════════════════════════════════════════════════════════════

# Patrón para slugs de URL: typically https://robohogar.com/p/<slug>
URL_SLUG_RE = re.compile(r"https?://robohogar\.com/p/([a-z0-9][a-z0-9-]+)")

# Patrón para fila de tabla con slug en columna independiente.
SLUG_CELL_RE = re.compile(r"\|\s*([a-z0-9][a-z0-9-]{3,})\s*\|")


def _read(path: Path) -> str:
    """Lee un archivo en utf-8; devuelve string vacío si no existe."""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def slugs_from_registro_articulos() -> set[str]:
    """Slugs publicados según el catálogo de artículos."""
    text = _read(REGISTRO_ARTICULOS)
    return set(URL_SLUG_RE.findall(text))


def slugs_from_registro_ficciones() -> tuple[set[str], set[str]]:
    """Devuelve (publicados, drafts_experimentales) según registro-ficciones.md.

    Los drafts experimentales viven en una sección dedicada del archivo y NO
    se consideran deuda — el pipeline puede generar audiolibros sobre ellos
    sin marcarlos como incompletos.
    """
    text = _read(REGISTRO_FICCIONES)
    if not text:
        return set(), set()

    publicados: set[str] = set()
    drafts: set[str] = set()

    # Heurística: dividimos por la sección "Drafts experimentales".
    parts = re.split(r"^##\s+Drafts experimentales", text, maxsplit=1, flags=re.MULTILINE)
    main_section = parts[0]
    drafts_section = parts[1] if len(parts) > 1 else ""

    publicados.update(URL_SLUG_RE.findall(main_section))
    # En la sección drafts no hay URL real (aún no publicado), buscamos el slug
    # como celda de tabla.
    for line in drafts_section.splitlines():
        if "|" not in line or line.lstrip().startswith("|---"):
            continue
        cells = [c.strip() for c in line.split("|") if c.strip()]
        # Estructura esperada: fecha | título | slug | audiolibro | veredicto | notas
        if len(cells) >= 3 and re.match(r"^[a-z0-9][a-z0-9-]{3,}$", cells[2]):
            drafts.add(cells[2])

    return publicados, drafts


# ════════════════════════════════════════════════════════════════════════════
# Lectura del filesystem: qué hay realmente en disco.
# ════════════════════════════════════════════════════════════════════════════

def slugs_in_articulos_dir() -> set[str]:
    """Carpetas de borrador de artículos en content/articulos/<slug>/."""
    if not ARTICULOS_DIR.exists():
        return set()
    return {
        p.name for p in ARTICULOS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith("_") and (p / "borrador.html").exists()
    }


def slugs_in_published_dir() -> set[str]:
    """Slugs publicados deducidos del nombre `YYYY-MM-DD-<slug>.html`."""
    if not PUBLISHED_DIR.exists():
        return set()
    out: set[str] = set()
    for f in PUBLISHED_DIR.glob("*.html"):
        # Quitar prefijo de fecha si lo tiene.
        m = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.html$", f.name)
        if m:
            out.add(m.group(1))
        else:
            out.add(f.stem)
    return out


def slugs_in_ficciones_dir() -> set[str]:
    """Carpetas de relato en content/ficciones/_one-shots/ y series."""
    if not FICCIONES_DIR.exists():
        return set()
    out: set[str] = set()
    # _one-shots/<slug>/
    one_shots = FICCIONES_DIR / "_one-shots"
    if one_shots.exists():
        out.update(p.name for p in one_shots.iterdir() if p.is_dir() and not p.name.startswith("_"))
    # Series: content/ficciones/<serie>/episodios/<slug>.md (heurística laxa)
    for serie_dir in FICCIONES_DIR.iterdir():
        if not serie_dir.is_dir() or serie_dir.name.startswith("_"):
            continue
        for episodio in serie_dir.glob("**/2*.md"):
            m = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.md$", episodio.name)
            if m:
                out.add(m.group(1))
    return out


def slugs_with_audio() -> set[str]:
    """Ficciones con MP3 ya generado en assets/audio/ficciones/."""
    if not AUDIO_DIR.exists():
        return set()
    return {f.stem for f in AUDIO_DIR.glob("*.mp3")}


def lead_magnet_dirs() -> set[str]:
    """Directorios de lead magnets activos."""
    if not LEAD_MAGNETS_DIR.exists():
        return set()
    return {
        p.name for p in LEAD_MAGNETS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith("_")
    }


def lead_magnets_referenced() -> set[str]:
    """Lead magnets referenciados desde algún artículo (borrador o published)."""
    referenced: set[str] = set()
    for source in (ARTICULOS_DIR, PUBLISHED_DIR):
        if not source.exists():
            continue
        for html in source.rglob("*.html"):
            text = _read(html)
            for lm in lead_magnet_dirs():
                if lm in text:
                    referenced.add(lm)
    return referenced


# ════════════════════════════════════════════════════════════════════════════
# Auditoría: comparar conjuntos y poblar el Report.
# ════════════════════════════════════════════════════════════════════════════

def audit_articulos(report: Report) -> None:
    """Compara registro-articulos.md vs filesystem (drafts y publicados)."""
    registro = slugs_from_registro_articulos()
    drafts = slugs_in_articulos_dir()
    published_fs = slugs_in_published_dir()

    # Slugs en published/ pero no en registro: artículo publicado sin entrada.
    missing_in_registro = published_fs - registro
    for slug in sorted(missing_in_registro):
        report.deltas.append(
            f"Artículo publicado en `content/published/` sin entrada en `registro-articulos.md`: `{slug}`"
        )

    # Slugs en registro pero sin published/: backup local ausente (riesgo).
    missing_published_backup = registro - published_fs
    for slug in sorted(missing_published_backup):
        report.warnings.append(
            f"Artículo en `registro-articulos.md` sin backup en `content/published/`: `{slug}`"
        )

    # Drafts en articulos/ que ya están publicados pero el folder sigue ahí: OK informativo.
    drafts_done = drafts & registro
    if drafts_done:
        report.ok.append(
            f"{len(drafts_done)} drafts en `content/articulos/` con artículo ya publicado (carpeta de trabajo retenida)."
        )

    # Drafts en articulos/ no publicados: posibles huérfanos si llevan tiempo.
    pending_drafts = drafts - registro
    for slug in sorted(pending_drafts):
        report.warnings.append(
            f"Draft en `content/articulos/{slug}/` sin entrada en registro (work-in-progress o huérfano)."
        )

    if not missing_in_registro:
        report.ok.append(f"`registro-articulos.md` ↔ `content/published/`: sincronizado ({len(registro)} entradas).")


def audit_ficciones(report: Report) -> None:
    """Compara registro-ficciones.md vs filesystem (one-shots, series, audio)."""
    publicadas, drafts_exp = slugs_from_registro_ficciones()
    en_fs = slugs_in_ficciones_dir()
    con_audio = slugs_with_audio()

    # En filesystem pero no en ningún sitio del registro → gap.
    huerfanos = en_fs - publicadas - drafts_exp
    for slug in sorted(huerfanos):
        report.deltas.append(
            f"Ficción en `content/ficciones/` sin entrada en `registro-ficciones.md` "
            f"(ni publicada ni en drafts experimentales): `{slug}`"
        )

    # En registro publicadas pero no en disco → ficción borrada pero registrada.
    publicadas_sin_fs = publicadas - en_fs
    for slug in sorted(publicadas_sin_fs):
        report.warnings.append(
            f"Ficción en `registro-ficciones.md` sin carpeta en `content/ficciones/`: `{slug}`"
        )

    # MP3 sin ficción → archivo huérfano.
    audio_sin_ficcion = con_audio - en_fs
    for slug in sorted(audio_sin_ficcion):
        report.warnings.append(
            f"MP3 en `assets/audio/ficciones/{slug}.mp3` sin ficción en `content/ficciones/`."
        )

    if drafts_exp:
        report.ok.append(
            f"{len(drafts_exp)} draft(s) experimental(es) detectado(s): {', '.join(sorted(drafts_exp))} (intencionalmente pre-publicación)."
        )
    if publicadas and not huerfanos and not publicadas_sin_fs:
        report.ok.append(f"`registro-ficciones.md` ↔ `content/ficciones/`: sincronizado ({len(publicadas)} publicadas).")


def audit_calendario(report: Report) -> None:
    """Cruza slugs de calendario con registro-articulos para detectar publicaciones no marcadas."""
    text = _read(CALENDARIO)
    if not text:
        report.warnings.append("`calendario-editorial.md` no existe.")
        return

    registro = slugs_from_registro_articulos()
    # En el calendario buscamos slugs con backticks (`mejor-...`) en filas de backlog
    # que NO estén tachadas (~~). Si un slug aparece en backlog activo Y está en
    # registro publicado → desfase.
    not_struck = re.findall(r"`([a-z0-9][a-z0-9-]{4,})`", text)
    # Filtramos los que están dentro de líneas tachadas con ~~slug~~.
    striked = set(re.findall(r"~~([a-z0-9][a-z0-9-]{4,})~~", text))
    candidates = (set(not_struck) - striked) & registro

    for slug in sorted(candidates):
        # Doble check: el slug puede aparecer también en URL de "Temas usados"
        # (que es informativo, no backlog activo). Lo aceptamos como OK si la
        # línea contiene "Temas usados" cerca o ya hay un ✅.
        idx = text.find(f"`{slug}`")
        if idx == -1:
            continue
        line_start = text.rfind("\n", 0, idx) + 1
        line_end = text.find("\n", idx)
        line = text[line_start:line_end if line_end != -1 else None]
        if "✅" in line or "publicado" in line.lower() or "Publicado" in line:
            continue
        # Saltamos si la línea es del bloque "Temas usados" (al final del archivo).
        if "Temas usados" in text[max(0, idx - 4000):idx]:
            continue
        report.deltas.append(
            f"Tema `{slug}` aparece como pendiente en `calendario-editorial.md` "
            f"pero ya está publicado según `registro-articulos.md`."
        )

    if not candidates:
        report.ok.append("`calendario-editorial.md` ↔ `registro-articulos.md`: sin contradicciones.")


def audit_lead_magnets(report: Report) -> None:
    """Lead magnets sin ningún artículo que los referencie."""
    existing = lead_magnet_dirs()
    referenced = lead_magnets_referenced()
    huerfanos = existing - referenced
    for lm in sorted(huerfanos):
        report.warnings.append(
            f"Lead magnet `content/lead-magnets/{lm}/` existe pero ningún artículo lo referencia."
        )
    if existing and not huerfanos:
        report.ok.append(f"Lead magnets: {len(existing)} existentes, todos referenciados desde al menos un artículo.")


# ════════════════════════════════════════════════════════════════════════════
# Render del reporte: markdown legible + escritura a disco.
# ════════════════════════════════════════════════════════════════════════════

def render_report(report: Report, quiet: bool) -> str:
    today = _dt.date.today().isoformat()
    lines = [
        f"# Sync Catalogs · {today}",
        "",
        "Auditoría automática de sincronización entre filesystem y catálogos editoriales.",
        f"Generado por `utilities/sync_catalogs.py`. Sin auto-fix.",
        "",
    ]

    if report.is_clean():
        lines.append("**Resultado: ✅ sincronizado.** No se detectaron deltas ni warnings.")
    else:
        if report.deltas:
            lines.append(f"## Deltas ({len(report.deltas)})")
            lines.append("")
            lines.append("Bloquean o confunden el pipeline. Acción recomendada: corregir antes del próximo publish.")
            lines.append("")
            for d in report.deltas:
                lines.append(f"- ⚠️ {d}")
            lines.append("")
        if report.warnings:
            lines.append(f"## Warnings ({len(report.warnings)})")
            lines.append("")
            lines.append("No urgentes. Revisar cuando haya tiempo.")
            lines.append("")
            for w in report.warnings:
                lines.append(f"- 💭 {w}")
            lines.append("")

    if not quiet and report.ok:
        lines.append(f"## OK ({len(report.ok)})")
        lines.append("")
        for o in report.ok:
            lines.append(f"- ✅ {o}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_report(content: str) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    today = _dt.date.today().isoformat()
    out = REPORTS_DIR / f"sync-catalogs-{today}.md"
    out.write_text(content, encoding="utf-8")
    return out


# ════════════════════════════════════════════════════════════════════════════
# Entry point: orquesta todas las auditorías y emite el reporte.
# ════════════════════════════════════════════════════════════════════════════

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audita sincronización catálogos ↔ filesystem ROBOHOGAR.")
    parser.add_argument("--quiet", action="store_true", help="Omite la sección 'OK' del reporte.")
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="No escribe el .md de reporte (solo imprime a stdout). Útil en CI.",
    )
    args = parser.parse_args(argv)

    report = Report()
    audit_articulos(report)
    audit_ficciones(report)
    audit_calendario(report)
    audit_lead_magnets(report)

    rendered = render_report(report, quiet=args.quiet)
    print(rendered)

    if not args.no_write:
        out = write_report(rendered)
        print(f"Reporte guardado en {out.relative_to(REPO_ROOT)}", file=sys.stderr)

    # Exit code 1 si hay deltas (útil para CI futuro). Warnings no rompen.
    return 1 if report.deltas else 0


if __name__ == "__main__":
    sys.exit(main())
