"""
generate_pasos.py — Generador automático de PASOS.md para artículos ROBOHOGAR.

Uso:
    uv run python utilities/generate_pasos.py <slug>

Lee:
    - content/articulos/<slug>/borrador.html (frontmatter YAML dentro del <!-- --> inicial)
    - content/templates/PASOS-template.md (template con placeholders {VAR})

Escribe:
    - content/articulos/<slug>/PASOS.md (pre-rellenado con datos del frontmatter)

Qué rellena automáticamente:
    - SEO metadata (title, meta_description, slug, tags)
    - Char counts para title y description (validación Beehiiv)
    - Publish to según frontmatter `status` y si audiencia <30 subs (hardcoded hoy)
    - Links genéricos al slug publicado

Qué queda como placeholder para rellenar a mano:
    - Conceptos de hero v1/v2/v3 (solo Rafael/agente sabe qué generó)
    - Imágenes inline (depende del artículo)
    - Mapa visual ASCII
    - Datos a validar, fuentes, notas editoriales (depende del contenido)

Razón: PASOS.md tiene ~60% estructura repetible y ~40% específico del artículo.
Este script automatiza el 60% para que Rafael solo edite los bloques específicos.
"""

import re
import sys
from pathlib import Path


# ──────────────────────────────────────────────────────────────
# Parseo de frontmatter YAML dentro de un comentario HTML
# ──────────────────────────────────────────────────────────────

def extract_frontmatter(html_path: Path) -> dict:
    """
    Lee borrador.html y extrae el frontmatter YAML que vive dentro del
    primer bloque <!-- --> del archivo. Formato esperado:

        <!--
        ---
        title: "..."
        slug: "..."
        tags: ["..."]
        ...
        ---
        -->

    Devuelve un dict con los campos parseados. No usa PyYAML (no dependencia):
    parser manual simple porque el frontmatter siempre es plano.
    """
    text = html_path.read_text(encoding="utf-8")
    # Buscar el bloque entre los dos '---' dentro del comentario HTML
    match = re.search(r"<!--\s*---\s*(.+?)\s*---", text, re.DOTALL)
    if not match:
        raise ValueError(f"No se encontró frontmatter en {html_path}")
    body = match.group(1)

    data = {}
    for line in body.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        # Dividir solo en el primer ':' para que valores con ':' funcionen
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        # Quitar comillas dobles o simples si las hay
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        # Parsear listas tipo ["a", "b"]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            value = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
        data[key] = value
    return data


# ──────────────────────────────────────────────────────────────
# Resolver campos derivados (char counts, publish_to, tags, etc.)
# ──────────────────────────────────────────────────────────────

def build_replacements(frontmatter: dict, slug: str, articulo_num: int = None) -> dict:
    """
    Convierte los datos del frontmatter a los placeholders del template.
    Aplica reglas del repo (p.ej. fase pre-audiencia → Web only).
    """
    # Título SEO: preferir seo_title si existe, si no title. Char count estricto.
    seo_title = frontmatter.get("seo_title") or frontmatter.get("title", "")
    meta_desc = frontmatter.get("meta_description", "")
    title = frontmatter.get("title", "")

    tags_raw = frontmatter.get("tags", [])
    if isinstance(tags_raw, str):
        tags_raw = [tags_raw]
    # Tags formato backtick: `Humanoides`, `Comparativa`
    tags_formatted = ", ".join(f"`{t}`" for t in tags_raw)

    # Fase pre-audiencia (regla rules/newsletter.md): artículos van Web only.
    # Cuando audiencia ≥30 subs, cambiar default a "Email and web".
    # Por ahora hardcoded Web only + nota explicativa.
    publish_to = "Web only"
    publish_note = "(fase pre-audiencia, reserva envío hasta que haya ≥30 subs)"

    # Content Gate por defecto NO para reviews/editoriales evergreen
    content_gate = "❌ NO activar (foco SEO, artículo evergreen)"

    return {
        "ARTICULO_NUM": str(articulo_num) if articulo_num is not None else "?",
        "TITULO": title,
        "SUBTITULO_O_PROMESA": f"Artículo tipo {frontmatter.get('type', '?')}. Rellenar una frase con la promesa concreta al lector.",
        "META_TITLE": seo_title,
        "META_TITLE_CHARS": str(len(seo_title)),
        "META_DESCRIPTION": meta_desc,
        "META_DESC_CHARS": str(len(meta_desc)),
        "SLUG": slug,
        "TAGS": tags_formatted,
        "PUBLISH_TO": publish_to,
        "PUBLISH_NOTE": publish_note,
        "CONTENT_GATE": content_gate,
        "HERO_V1_CONCEPTO": "[rellenar: concepto de v1]",
        "HERO_V2_CONCEPTO": "[rellenar: concepto de v2]",
        "HERO_V3_CONCEPTO": "[rellenar: concepto de v3]",
        "HERO_RECOMENDACION": "[rellenar: v1/v2/v3 y por qué]",
        "INLINE_IMAGES_TABLE": "| Archivo | Ubicación en artículo | Fuente |\n|---|---|---|\n| [rellenar] | [rellenar sección] | [rellenar fuente] |",
        "MAPA_VISUAL_ASCII": "[rellenar: diagrama ASCII del layout del artículo con H1/H2/imágenes/CTAs]",
        "DATOS_A_VALIDAR": "- [ ] [rellenar: cada precio, fecha y dato específico que pueda haber cambiado desde el research]",
        "TEMPLATE_BASE_SLUG": "[rellenar: slug del artículo Beehiiv a duplicar — ej mejor-robot-asistente-ia-2026 para comparativas]",
        "FUENTES_TABLE": "| Dato | Fuente | Cómo verificar |\n|---|---|---|\n| [rellenar] | [rellenar] | [rellenar] |",
        "INTERNAL_LINKS": "- [rellenar: URLs de otros artículos del registro que se enlazan en el texto]",
        "NOTAS_EDITORIALES": "- [rellenar: notas de tono, ángulo, decisiones editoriales importantes]",
    }


# ──────────────────────────────────────────────────────────────
# Render del template
# ──────────────────────────────────────────────────────────────

def render(template: str, replacements: dict) -> str:
    """
    Reemplaza {VAR} por valores. Si falta algún placeholder, lo deja tal cual
    con marca visible para que Rafael lo vea y rellene a mano.
    """
    for key, value in replacements.items():
        template = template.replace("{" + key + "}", str(value))
    # Marcar placeholders no resueltos (quedarán como {VAR_NO_RESUELTA})
    unresolved = re.findall(r"\{([A-Z_]+)\}", template)
    if unresolved:
        print(f"⚠️  Placeholders sin resolver (rellenar a mano): {set(unresolved)}", file=sys.stderr)
    return template


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: uv run python utilities/generate_pasos.py <slug> [<articulo_num>]", file=sys.stderr)
        sys.exit(1)

    slug = sys.argv[1]
    articulo_num = int(sys.argv[2]) if len(sys.argv) > 2 else None

    # Resolver paths relativos al repo root (asumimos que se ejecuta desde ahí)
    repo_root = Path.cwd()
    article_dir = repo_root / "content" / "articulos" / slug
    html_path = article_dir / "borrador.html"
    template_path = repo_root / "content" / "templates" / "PASOS-template.md"
    output_path = article_dir / "PASOS.md"

    if not html_path.exists():
        print(f"❌ No existe: {html_path}", file=sys.stderr)
        sys.exit(1)
    if not template_path.exists():
        print(f"❌ No existe: {template_path}", file=sys.stderr)
        sys.exit(1)
    if output_path.exists():
        print(f"⚠️  PASOS.md ya existe: {output_path}. Sobrescribir? [y/N] ", end="", flush=True)
        answer = input().strip().lower()
        if answer != "y":
            print("Cancelado.")
            sys.exit(0)

    # Pipeline: leer frontmatter → resolver placeholders → render template → escribir
    frontmatter = extract_frontmatter(html_path)
    replacements = build_replacements(frontmatter, slug, articulo_num)
    template = template_path.read_text(encoding="utf-8")
    rendered = render(template, replacements)
    output_path.write_text(rendered, encoding="utf-8")

    print(f"✅ Generado: {output_path}")
    print(f"   SEO: title={len(replacements['META_TITLE'])} chars, desc={len(replacements['META_DESCRIPTION'])} chars")
    print(f"   Tags: {replacements['TAGS']}")
    print()
    print("Revisar y rellenar a mano los bloques marcados [rellenar: ...]:")
    print("  - Conceptos de hero v1/v2/v3 + recomendación")
    print("  - Tabla de imágenes inline")
    print("  - Mapa visual ASCII")
    print("  - Datos a validar, fuentes, notas editoriales, links internos")


if __name__ == "__main__":
    main()
