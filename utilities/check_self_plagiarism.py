"""check_self_plagiarism.py — Validación grep cruzada anti-auto-plagio para Ficciones Domésticas.

Compara n-gramas (frases consecutivas de N palabras) del relato candidato contra
los últimos M relatos publicados/draft de la saga, y reporta los matches que
indican copy-paste literal o casi literal.

Pipeline obligatorio del skill /ficcion-draft § 9 (regla dura 2026-04-26 PM tras
incidente "El chaval" — copy-paste literal de párrafo entero entre relatos).

Estados de match:
  - >=6 palabras consecutivas idénticas → BLOQUEO (auto-plagio literal)
  - 4-5 palabras de fórmula idéntica → WARNING (revisar contra tropos-quemados.md)
  - <4 palabras → ignorado (coincidencias léxicas normales del registro ES)

Uso:
    python utilities/check_self_plagiarism.py <ruta-relato.md> [--window 5]

Salida:
    Exit 0 → procede al output del skill (cero matches >=6 palabras).
    Exit 1 → BLOQUEO. Imprime tabla de matches y archivo origen + línea.
    Exit 2 → WARNING (matches 4-5). Imprime advertencia, no bloquea.

Dependencias:
    Solo stdlib (argparse, pathlib, re, collections, sys). No pip.

Convenciones:
    - El relato candidato puede estar en cualquier carpeta de content/ficciones/.
    - Los relatos de comparación se descubren leyendo content/registro-ficciones.md
      (tabla de relatos publicados + tabla de drafts pre-pub combinadas, ordenadas
      por fecha descendente, los M más recientes se usan).
    - Cada relato se normaliza antes de extraer n-gramas: minúsculas, eliminar
      frontmatter YAML, eliminar comentarios HTML, eliminar bloques de cita
      `> Mentira grande` y `> Muro izquierdo`, eliminar sección "Lo real detrás
      del relato", colapsar whitespace, quitar puntuación menor.
"""

# ════════════════════════════════════════════════════════════════════════════
# Imports y configuración
# ════════════════════════════════════════════════════════════════════════════

import argparse                                              # parseo de CLI
import re                                                    # normalización + extracción
import sys                                                   # exit codes
from collections import defaultdict                          # agrupar matches por archivo origen
from pathlib import Path                                     # rutas portátiles

# Windows cp1252 stdout no soporta emojis (UnicodeEncodeError). Forzar UTF-8 en
# Python 3.7+ vía reconfigure(). Si no se puede (cap. iOS/legacy), seguimos: el
# script funciona, solo que el reporte saldría en ASCII.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass                                                 # no fatal; deja el default


# Constantes operativas — ajustar aquí si cambian umbrales
MIN_NGRAM_BLOCK = 6                                          # ≥ → bloqueo (auto-plagio literal)
MIN_NGRAM_WARN = 4                                           # 4-5 → warning (fórmula reconocible)
DEFAULT_WINDOW = 5                                           # nº de relatos previos a comparar
REPO_ROOT = Path(__file__).resolve().parent.parent           # raíz del repo robohogar/
FICCIONES_ROOT = REPO_ROOT / "content" / "ficciones"         # carpeta canon de relatos
REGISTRO_PATH = REPO_ROOT / "content" / "registro-ficciones.md"  # tabla con orden cronológico


# ════════════════════════════════════════════════════════════════════════════
# Normalización del texto — extrae prosa narrativa pura, descarta meta-bloques
# ════════════════════════════════════════════════════════════════════════════

def normalize_prose(content: str) -> str:
    """Devuelve solo la prosa narrativa del relato, lista para extraer n-gramas.

    Descarta:
      - frontmatter YAML (--- ... ---)
      - bloques `> Mentira grande:` y `> Muro izquierdo:` (declaraciones del skill)
      - sección "Lo real detrás del relato" hasta final
      - comentarios HTML <!-- ... -->
      - subtítulos `## I.`, `## II.`, etc. (no son prosa, son bisagras)
      - puntuación que no aporta significado (—, ·, "", '', cursiva markdown, *, _, comillas)

    Lo que mantiene: prosa de escena, diálogo (raya española respetada como espacio),
    descripciones, narrador. Todo en minúsculas, whitespace colapsado.
    """
    text = content

    # Eliminar frontmatter YAML al inicio
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

    # Eliminar bloque de declaración Mentira/Muro (siempre al inicio del relato tras H1)
    text = re.sub(r"^> \*\*Mentira grande:.*?\*Registradas por.*?\*\n", "", text, flags=re.DOTALL | re.MULTILINE)

    # Eliminar todo desde "## Lo real detrás del relato" hasta el final
    text = re.sub(r"\n## Lo real detrás del relato.*", "", text, flags=re.DOTALL)

    # Eliminar comentarios HTML
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Eliminar el "Fin." aislado
    text = re.sub(r"\n+Fin\.\s*\n", "\n", text)

    # Eliminar líneas de subtítulos `## I. Algo` (bisagras, no prosa)
    text = re.sub(r"^## [IVX]+\..*$", "", text, flags=re.MULTILINE)

    # Eliminar el H1 del título (línea que empieza con `# `)
    text = re.sub(r"^# .*$", "", text, flags=re.MULTILINE)

    # Cursiva markdown *...* y _..._ → quitar marcas pero mantener contenido
    text = re.sub(r"[*_]+", " ", text)

    # Comillas tipográficas, em-dashes, separadores middot — convertir a espacio
    text = re.sub(r"[—–·«»“”‘’\"`]", " ", text)

    # Diálogo: raya española al inicio de párrafo (—Ramón) → quitar la raya
    text = re.sub(r"^—\s*", "", text, flags=re.MULTILINE)

    # Puntuación final de oración + signos auxiliares → espacios (no queremos n-gramas que
    # crucen oraciones distintas, pero tampoco queremos que la puntuación bloquee match)
    text = re.sub(r"[.,;:!?¿¡()…\[\]/]", " ", text)

    # Cifras y dígitos: irrelevantes para detección de plagio léxico — los descartamos
    text = re.sub(r"\d+", " ", text)

    # Whitespace y minúsculas
    text = re.sub(r"\s+", " ", text).strip().lower()

    return text


# ════════════════════════════════════════════════════════════════════════════
# Extracción de n-gramas
# ════════════════════════════════════════════════════════════════════════════

def extract_ngrams(prose: str, n: int) -> set[str]:
    """Devuelve el conjunto de n-gramas (frases de n palabras consecutivas).

    Usa set para tener O(1) en intersecciones. El orden de aparición se reconstruye
    a posteriori si hace falta para reportar al usuario (función find_matches_in_text).
    """
    words = prose.split()                                    # tokenización ingenua suficiente
    if len(words) < n:
        return set()
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def find_match_context(content: str, ngram: str) -> tuple[int, str] | None:
    """Localiza un n-grama (texto normalizado) en el archivo original sin normalizar.

    Devuelve (línea, frase original cercana) o None si no encuentra. Usado solo para
    reportar al usuario — el match ya se confirmó en el conjunto normalizado.

    Heurística: busca las primeras 3 palabras del n-gram en el texto original (case-
    insensitive). No es perfecto, pero suficiente para que Rafael localice la frase.
    """
    first_words = ngram.split()[:3]                          # primeras 3 palabras como ancla
    pattern = re.escape(" ".join(first_words))               # escapar regex special chars
    for line_num, line in enumerate(content.splitlines(), start=1):
        if re.search(pattern, line, flags=re.IGNORECASE):
            return (line_num, line.strip()[:120])
    return None


# ════════════════════════════════════════════════════════════════════════════
# Lectura del registro: descubrir los M relatos previos a comparar
# ════════════════════════════════════════════════════════════════════════════

def read_recent_relatos(window: int, exclude_slug: str) -> list[Path]:
    """Lee content/registro-ficciones.md y devuelve los `window` relatos más recientes.

    Combina las dos tablas (publicados + drafts pre-pub) y ordena por fecha en columna 1
    (campo `Fecha`). Excluye el relato actual (exclude_slug) por si está ya en el registro
    como draft.

    Heurística de path: para cada slug del registro, buscar el archivo .md más reciente en
    content/ficciones/**/<slug>/*.md o content/ficciones/<slug>/*.md.
    """
    if not REGISTRO_PATH.exists():
        return []

    registro_text = REGISTRO_PATH.read_text(encoding="utf-8")

    # Extraer pares (fecha, slug) de cualquier fila de tabla markdown que tenga ambos
    # Patrón: línea con | YYYY-MM-DD | ... | <slug> | (un slug es kebab-case con guiones)
    rows = re.findall(
        r"\|\s*\d+\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|.*?\|\s*([a-z0-9-]+)\s*\|"
        r"|\|\s*(\d{4}-\d{2}-\d{2})\s*\|.*?\|\s*([a-z0-9-]+)\s*\|",
        registro_text,
    )

    # Cada match es (fecha_pub, slug_pub, fecha_draft, slug_draft) — coger el que tenga valor
    pairs: list[tuple[str, str]] = []
    for fp, sp, fd, sd in rows:
        if fp and sp:
            pairs.append((fp, sp))
        elif fd and sd:
            pairs.append((fd, sd))

    # Excluir slug actual y duplicados (mantener el más reciente de cada slug)
    seen_slugs: dict[str, str] = {}
    for fecha, slug in pairs:
        if slug == exclude_slug:
            continue
        # Si ya existe ese slug, mantener la fecha más reciente
        if slug not in seen_slugs or fecha > seen_slugs[slug]:
            seen_slugs[slug] = fecha

    # Ordenar por fecha descendente y tomar los `window` más recientes
    sorted_slugs = sorted(seen_slugs.items(), key=lambda x: x[1], reverse=True)[:window]

    # Resolver cada slug a su path concreto
    # Patrón canónico del relato: YYYY-MM-DD-<slug>.md (frontmatter + prosa).
    # NO el snippets de Beehiiv, NO PASOS.md, NO audiolibro.txt, NO versiones _v1/_v2.
    paths: list[Path] = []
    canonical_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    for slug, _ in sorted_slugs:
        # Solo archivos cuyo NOMBRE coincida con YYYY-MM-DD-<slug>.md
        # (no glob por carpeta — eso pesca snippets, PASOS, audiolibro, etc.)
        candidates = [
            p for p in FICCIONES_ROOT.glob(f"**/*-{slug}.md")
            if canonical_pattern.match(p.name)
            and not p.name.endswith("-v1.md")
            and not p.name.endswith("-v2.md")
        ]
        if candidates:
            # Si hay varios (raro: solo si hay versiones de fechas distintas), el más reciente
            paths.append(max(candidates, key=lambda p: p.stat().st_mtime))

    return paths


# ════════════════════════════════════════════════════════════════════════════
# Lógica principal
# ════════════════════════════════════════════════════════════════════════════

def check(candidate_path: Path, window: int) -> int:
    """Compara candidate_path contra los `window` relatos previos. Devuelve exit code.

    Returns:
        0 → cero matches >=4 palabras → procede al output
        1 → algún match >=6 palabras → BLOQUEO
        2 → solo matches 4-5 palabras → WARNING (no bloquea pero avisa)
    """
    if not candidate_path.exists():
        print(f"❌ Archivo no encontrado: {candidate_path}")
        return 1

    # Derivar slug desde el filename: 2026-04-26-el-chaval.md → el-chaval
    candidate_slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", candidate_path.stem)

    candidate_raw = candidate_path.read_text(encoding="utf-8")
    candidate_prose = normalize_prose(candidate_raw)

    if not candidate_prose:
        print(f"⚠️  Texto vacío tras normalizar: {candidate_path}")
        return 1

    # Conjunto de n-gramas del candidato
    cand_ng_block = extract_ngrams(candidate_prose, MIN_NGRAM_BLOCK)
    cand_ng_warn = extract_ngrams(candidate_prose, MIN_NGRAM_WARN)

    # Descubrir relatos previos
    previos = read_recent_relatos(window, exclude_slug=candidate_slug)

    if not previos:
        print(f"ℹ️  No se encontraron relatos previos en {REGISTRO_PATH}.")
        print(f"    (Es el primer relato del catálogo o el slug {candidate_slug} es ya el más reciente.)")
        print("✅ Sin base contra la que comparar — procede al output.")
        return 0

    print(f"🔍 Comparando {candidate_path.name} contra {len(previos)} relatos previos:")
    for p in previos:
        print(f"   • {p.relative_to(REPO_ROOT)}")
    print()

    # Acumuladores de matches por archivo
    blocks_by_file: dict[Path, list[tuple[str, int, str]]] = defaultdict(list)
    warns_by_file: dict[Path, list[tuple[str, int, str]]] = defaultdict(list)

    for prev_path in previos:
        prev_raw = prev_path.read_text(encoding="utf-8")
        prev_prose = normalize_prose(prev_raw)
        prev_ng_block = extract_ngrams(prev_prose, MIN_NGRAM_BLOCK)
        prev_ng_warn = extract_ngrams(prev_prose, MIN_NGRAM_WARN)

        # Matches >=6 palabras → BLOQUEO
        intersect_block = cand_ng_block & prev_ng_block
        for ng in intersect_block:
            ctx = find_match_context(prev_raw, ng)
            line, snippet = ctx if ctx else (0, ng)
            blocks_by_file[prev_path].append((ng, line, snippet))

        # Matches 4-5 palabras → WARNING (excluir los que ya están cubiertos por block matches)
        intersect_warn_only = (cand_ng_warn & prev_ng_warn) - {
            " ".join(ng.split()[:MIN_NGRAM_WARN])
            for ng in intersect_block
        }
        # Filtrar warns que ya estén dentro de un block match (n-gramas más cortos contenidos)
        intersect_warn_only = {
            ng for ng in intersect_warn_only
            if not any(ng in big for big in intersect_block)
        }
        for ng in intersect_warn_only:
            ctx = find_match_context(prev_raw, ng)
            line, snippet = ctx if ctx else (0, ng)
            warns_by_file[prev_path].append((ng, line, snippet))

    # ──────────────────────────────────────────────────────────────────────
    # Reporte
    # ──────────────────────────────────────────────────────────────────────

    if blocks_by_file:
        print(f"❌ BLOQUEO — {sum(len(v) for v in blocks_by_file.values())} match(es) ≥{MIN_NGRAM_BLOCK} palabras consecutivas:\n")
        for path, matches in blocks_by_file.items():
            print(f"  📄 {path.relative_to(REPO_ROOT)}")
            for ng, line, snippet in sorted(matches, key=lambda m: m[1]):
                print(f"     L{line}: {snippet!r}")
                print(f"        ↳ n-grama: {ng!r}")
            print()
        print("🛑 Reescribir las frases marcadas antes de entregar el output.\n")
        # Reportar también los warns aunque ya hay bloqueo, son útiles
        if warns_by_file:
            print(f"⚠️  Adicionalmente, {sum(len(v) for v in warns_by_file.values())} match(es) {MIN_NGRAM_WARN}-{MIN_NGRAM_BLOCK - 1} palabras (revisar tropos-quemados.md):\n")
            for path, matches in warns_by_file.items():
                # Limitar a los 3 más relevantes por archivo (los matches más largos del rango)
                top = sorted(matches, key=lambda m: -len(m[0].split()))[:3]
                print(f"  📄 {path.relative_to(REPO_ROOT)}")
                for ng, line, snippet in top:
                    print(f"     L{line}: {ng!r}")
                print()
        return 1

    if warns_by_file:
        total_warns = sum(len(v) for v in warns_by_file.values())
        print(f"⚠️  WARNING — {total_warns} match(es) {MIN_NGRAM_WARN}-{MIN_NGRAM_BLOCK - 1} palabras (no bloquea pero revisa):\n")
        for path, matches in warns_by_file.items():
            # Limitar a los 5 más relevantes por archivo (n-gramas más largos)
            top = sorted(matches, key=lambda m: -len(m[0].split()))[:5]
            print(f"  📄 {path.relative_to(REPO_ROOT)}")
            for ng, line, snippet in top:
                print(f"     L{line}: {ng!r}")
            print()
        print("👉 Revisar contra `references/ficciones/tropos-quemados.md` — si la fórmula está marcada 🔴, reescribir.\n")
        return 2

    print("✅ Cero matches ≥4 palabras consecutivas. Procede al output del skill.")
    return 0


# ════════════════════════════════════════════════════════════════════════════
# Entry point
# ════════════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validación grep cruzada anti-auto-plagio para Ficciones Domésticas ROBOHOGAR.",
    )
    parser.add_argument(
        "candidate",
        type=Path,
        help="Ruta al .md del relato candidato (puede ser absoluta o relativa al cwd).",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=DEFAULT_WINDOW,
        help=f"Cuántos relatos previos comparar (por defecto: {DEFAULT_WINDOW}).",
    )
    args = parser.parse_args()

    candidate = args.candidate.resolve()
    return check(candidate, args.window)


if __name__ == "__main__":
    sys.exit(main())
