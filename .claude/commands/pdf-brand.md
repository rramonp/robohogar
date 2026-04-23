# PDF Brand — Generador de tangibles PDF con marca ROBOHOGAR

Genera PDFs descargables (lead magnets, cheatsheets, guías, dossiers) a partir de un `contenido.md` estructurado. Aplica el patrón visual validado del v2 de Hoja de Compra: portada ámbar + icon robot, páginas internas 2-col con callouts, backcover con bloque dark de invitación a compartir + firma ROBOHOGAR + icon.

## When to activate

- "genera el PDF del <tangible>"
- "hazme el PDF de <slug>"
- "convierte contenido.md a PDF"
- "itera el PDF del <tangible> a vN"
- `/pdf-brand cheatsheet <slug>`
- `/pdf-brand cheatsheet <slug> v<N>` (para versionar iteraciones)

## Sintaxis

```
/pdf-brand <variante> <slug> [version]
```

- **variante:** `cheatsheet` (única en F4C-v1; `comparativa`, `guia`, `relato` pendientes de construir — ver roadmap).
- **slug:** nombre del directorio del tangible dentro de `content/lead-magnets/<slug>/`.
- **version** (opcional): `v1`, `v2`, `v3`… Si se omite, Claude lee la última versión existente del dir y crea la siguiente (v1 si no hay nada).

## Workflow que Claude ejecuta

### 1. Validar inputs

- Confirmar que `content/lead-magnets/<slug>/contenido.md` existe. Si no, error.
- Confirmar que la variante está soportada (hoy solo `cheatsheet`).
- Determinar la versión objetivo:
  - Si el usuario pasó `vN`, usarla.
  - Si no, buscar la última `<slug>-robohogar-v*.pdf` existente, incrementar el número. Si no hay ninguno, usar `v1`.

### 2. Leer y parsear `contenido.md`

El `contenido.md` de cada tangible tiene secciones con **convenciones semánticas**:

| Sección del markdown | Dónde va en el PDF | Campo `data` del render |
|---|---|---|
| Título principal (la primera `#`) | H1 portada (puede partirse en `title_big` + `title_small` si son 2 líneas) | `title_big`, `title_small` |
| `**Subtítulo:**` | Subtítulo portada | `subtitle` |
| `**Descriptor:**` | Callout descriptor portada | `descriptor` |
| `**Dato gancho:**` (opcional) | Número decorativo grande + bloque callout | `decorative_number` |
| `## INTRODUCCIÓN` | Intro callout portada (multi-párrafo) | `intro_paragraphs` |
| `## LAS N PREGUNTAS` / `## LA LISTA` / `## LOS N ÍTEMS` | Lista items distribuidos 5/página | `items[]` |
| Cada `### N. Texto pregunta` | Una card del grid de items | `{num, title, body, bullets, callout}` |
| `## ANEXO` (opcional) | Bloque ámbar backcover | `anexo.title`, `anexo.items[]` |
| `## CIERRE` / bloque dark con eyebrow "SI TE HA SERVIDO" | Bloque dark backcover | `close_hook.{eyebrow, title, subtitle}` |
| `**Más recursos:**` | Bloque resources backcover | `resources[]` |
| `**Disclaimer (pie):**` | Disclaimer italic backcover | `disclaimer` |

Claude extrae estos campos del markdown y monta el dict `data`.

**Reglas de parseo importantes:**
- Negritas `**texto**` dentro de bullets van como `{label: "texto", text: "resto"}`.
- Tablas Markdown dentro de un item se convierten a HTML crudo en el campo body.
- Los callouts por pregunta se detectan por bloque que empieza con `> **TRAMPA:** …` o similar.
- El "¿?" inicial de preguntas se preserva tal cual.
- Todo contenido entre `<!-- -->` del markdown se ignora.

### 3. Aplicar reglas de tangibles.md antes de generar

Antes de invocar el skill, Claude debe:

- [ ] **Verificar que NO hay texto prohibido** en los campos extraídos:
  - Listas de "próximos tangibles" / roadmap de futuros PDFs.
  - Fechas de revisión prometidas ("Próxima revisión octubre 2026", "actualizamos cada 6 meses").
  - Byline "Rafael de ROBOHOGAR" (la firma es solo `ROBOHOGAR`).
- [ ] **Título corto** (≤60 chars combinando big+small).
- [ ] **Subtítulo con cifra o promesa concreta** (regla tangibles.md § promoción en subtítulo).
- [ ] **Todos los items** tienen callout propio (patrón del v2 validado).

Si encuentra violaciones → **NO llama al skill**, reporta a Rafael y pide corregir el `contenido.md` primero. (El validator del skill también bloquea pre-PDF por si Claude falla, pero mejor catch temprano.)

### 3 bis. Second reader externo · `/validate-prose-es` — OBLIGATORIO antes de invocar el skill (añadido 2026-04-23)

Los validators Python del skill (`skills/pdf_brand/validators.py`) cubren las 3 prohibiciones duras (roadmap futuros / fechas revisión / byline personal) + anti-IA §1 + microcopy de conversión + anti-anglicismos ES + jerga `tangible` filtrada. Pero NO cogen: calcos sintácticos EN→ES (21 patterns del knowledge ES), colocaciones ambiguas no documentadas, registros mezclados, frases que requieren releer — los mismos vicios que `/content-draft § 8.5 quater` y `/ficcion-draft § 8.4` defienden vía `/validate-prose-es`.

**Invocación obligatoria y autónoma:** tras pasar las verificaciones del paso 3 con 0 violaciones, invocar `/validate-prose-es content/lead-magnets/<slug>/contenido.md` (la fuente de prosa del PDF, antes de que el skill Python la transforme en HTML/PDF). **El skill se ejecuta sin pedir autorización a Rafael** — es paso del pipeline.

- **READY** → proceder al paso 4 (invocar skill Python).
- **PENDING_FIXES** → aplicar fixes directamente al `contenido.md`. Re-invocar una vez. Si sigue PENDING, mostrar reporte a Rafael antes de generar PDF.
- **MAJOR_REWRITE** → BLOQUEAR generación PDF. Volver a reescritura de `contenido.md`.

**Por qué validar aquí y no solo en el PDF renderizado:** el PDF es artefacto final difícil de iterar (regenerarlo cuesta ~5 min de compute + incrementar versión del filename). La prosa fuente en markdown es el lugar natural para auditar — si el validador pide cambios, se tocan 3 líneas en `contenido.md` y se relanza. Atajar calcos aquí evita PDFs v2/v3/v4 por iteración editorial.

Log en `content/lead-magnets/<slug>/validator-reports/YYYY-MM-DD-report.md`.

**Ámbito:** aplica a cualquier variante de `/pdf-brand` que genere prosa significativa — cheatsheet (activo), guia (futuro), comparativa (futuro), relato (futuro). La ficha Beehiiv Digital Product generada en paso 6 hereda esta validación porque su contenido deriva del mismo `contenido.md`.

### 4. Invocar el skill programáticamente

```python
import sys
sys.path.insert(0, "c:/Users/bakal/robohogar")
from skills.pdf_brand import render_cheatsheet

data = {...}  # extraído del contenido.md
html_path, pdf_path = render_cheatsheet(data, force=False)
```

Si `force=False` y la versión ya existe, levanta `FileExistsError` → Claude incrementa versión y reintenta (o avisa a Rafael).

### 5. Generar previews PNG para verificación visual

Tras generar el PDF, Claude produce PNG previews de cada página (igual que para la v2 manual):

```bash
uv run --with playwright --with pillow python -c "
from playwright.sync_api import sync_playwright
# ... render full-page screenshot, split en 4 páginas, guardar en _preview_<version>/
"
```

Previews van a `content/lead-magnets/<slug>/_preview_<version>/page-N.png`.

### 6. Generar ficha Beehiiv Digital Product (OBLIGATORIO)

Todo tangible necesita además una `beehiiv-ficha.md` en `content/lead-magnets/<slug>/` con los 10 campos de configuración del Digital Product de Beehiiv. Claude genera esta ficha automáticamente tras el PDF, usando el template canónico [`content/templates/beehiiv-digital-product-template.md`](../../content/templates/beehiiv-digital-product-template.md) y extrayendo:

- **File** (auto): `<slug>-robohogar-<version>.pdf`
- **Product name** (auto): derivado de `title_big + title_small + " · " + descriptor-corto` del data.py
- **Description** (auto): `subtitle` del data.py (mantener ≤200 chars)
- **Product details** (auto): 6 bloques estructurados (Qué es · Qué cubre · Para quién es · Para quién no es · Qué incluye · Qué pasa al descargarlo) construidos a partir de `descriptor + intro_paragraphs + items (como lista de puntos) + close_hook + welcome flow info`
- **Call-to-action copy** (default fijo): `Descargar gratis`
- **Post-purchase redirect** (default fijo): `(vacío)`
- **Survey** (default fijo): `No survey`
- **Product page URL** (sugerencia a Rafael): slug corto de 2-4 palabras, Claude propone uno pero Rafael lo valida
- **Send review request emails** (default fijo): `❌ OFF`
- **Images** (nota): usar portada PDF a 1280×720

Los **4 defaults fijos** (CTA copy, redirect, survey, review emails) se aplican sin preguntar — son reglas sistémicas del repo para fase F1-F2 (0-500 subs). Documentadas en [`rules/tangibles.md`](../rules/tangibles.md) § Reglas operativas.

La ficha debe pasar los mismos **validators** que el PDF:
- Sin lista de "próximos tangibles" o roadmap futuro.
- Sin promesas de fechas de revisión.
- Sin byline personal "Rafael de ROBOHOGAR".
- Voz plural editorial.
- Anti-IA §1 Universal (0 palabras tóxicas).
- **Microcopy de conversión (`@rules/tangibles.md § Microcopy de conversión`).** El campo "Product details → Qué pasa al descargarlo" y cualquier trust-line debajo de un CTA (botón Beehiiv, email post-purchase) cumple el default canónico `PDF gratis con tu suscripción semanal. Cancela cuando quieras.` o variante que respete las 3 reglas (≥2 elementos obligatorios · 0 promesas prohibidas · ≤80 chars). Prohibidas: `15 segundos`, `llega al email en`, `instantáneo`, `sin publicidad`, `sin promociones`, `sin letra pequeña`, hype anglosajón (`Join N+ readers`, `Don't miss out`).
- **Anti-anglicismos ES (`@rules/editorial.md § Apertura y cierre del cuerpo del email`).** Validator bloquea saludos anglo (`Hola X`, `Querido lector`, `Hey`, `espero que estés bien`) y uso de `tangible` como jerga determinada al lector (`el/este/nuestro tangible`). Los nombres de marca reales (`TangibleFuture`) y comentarios HTML no disparan — regex acotado.

Si el Product details violara alguna regla → Claude debe reescribir antes de entregar, nunca entregar una ficha con violaciones.

### 7. Reportar a Rafael

Formato de respuesta:

```
✓ Generado <slug>-robohogar-<version>.pdf (<size> KB, <N> páginas)

Archivos:
- HTML source: content/lead-magnets/<slug>/<slug>-robohogar-<version>.html
- PDF: content/lead-magnets/<slug>/<slug>-robohogar-<version>.pdf
- Previews: content/lead-magnets/<slug>/_preview_<version>/page-{1..N}.png
- Ficha Beehiiv: content/lead-magnets/<slug>/beehiiv-ficha.md

Checks validados (PDF + ficha Beehiiv):
  ✓ No roadmap de próximos tangibles
  ✓ No promesas de fechas de revisión
  ✓ Firma = solo "ROBOHOGAR" (sin byline personal)
  ✓ Todos los ítems tienen callout propio
  ✓ Subtítulo con cifra concreta
  ✓ Defaults Beehiiv aplicados (CTA "Descargar gratis" · sin redirect · sin survey · review OFF)

Abre el PDF y dime qué iterar. Cuando valides el PDF, usa beehiiv-ficha.md para
configurar el Digital Product en Beehiiv (5 min copy-paste).
```

## Ejemplos de invocación

### Ejemplo 1 — Regenerar Hoja de Compra como v3 (validación del skill)

**Rafael:** `/pdf-brand cheatsheet hoja-compra v3`

**Claude:**
1. Lee `content/lead-magnets/hoja-compra/contenido.md`.
2. Extrae el dict data con 10 items + portada + backcover.
3. Valida que no hay prohibiciones (hay una nota del propio contenido.md al final que menciona "Prohibido en PDFs tangibles..." — esa sección NO se parsea como contenido, es guía editorial).
4. Llama `render_cheatsheet(data, force=False)`.
5. Skill genera HTML + PDF + valida y devuelve paths.
6. Claude genera previews PNG de las 4 páginas.
7. Reporta a Rafael con paths y checks.

### Ejemplo 2 — Primer PDF del tangible "Guía primer mes"

**Rafael:** `/pdf-brand cheatsheet guia-primer-mes-aspirador` (sin versión → usa v1)

**Claude:**
- Detecta que no existen PDFs previos → versión = v1.
- Procesa el contenido.md (más largo que Hoja de Compra, posiblemente 3 páginas de items + anexo de troubleshooting + tabla de consumibles).
- **Ajuste de items_per_page:** este tangible tiene 4 bloques grandes (Semana 1, Semanas 2-3, Día 30, Troubleshooting + Consumibles) en vez de 10 preguntas. Claude decide si cada sección es un item (4 items en 1 página, alta densidad) o si subdivide en sub-items.
- Genera.

### Ejemplo 3 — Iteración tras feedback

**Rafael:** "en el v3 de Hoja de Compra, cambia el callout de la pregunta 3 por X y regenera"

**Claude:**
1. Edita `contenido.md` aplicando el cambio.
2. Invoca `/pdf-brand cheatsheet hoja-compra` → Claude detecta que v3 ya existe y propone v4.
3. Genera v4 preservando v3 (regla no-sobrescritura de `feedback_never_overwrite_images.md`).

## Variantes futuras (roadmap)

| Variante | Layout | Status |
|---|---|---|
| `cheatsheet` | Portada + 2pp items 2-col + backcover | ✅ v1 disponible |
| `comparativa` | Portada + tabla benchmark full-width + veredicto + backcover | 🔜 cuando toque primer tangible "Calendario rebajas" |
| `guia` | Portada + N pp step-by-step (día/semana) + troubleshooting | 🔜 cuando toque "Guía primer mes aspirador" si cheatsheet no encaja |
| `relato` | Portada ilustrada + relato tipografía editorial + character card | 🔜 cuando toque "Dossier Ficciones Domésticas" |

Cada variante nueva reusa `brand.css` + validators + export PDF y solo cambia el template Jinja2.

## Paso final — Actualizar tablero vivo en guia-implementacion.md

Tras generar el PDF + ficha Beehiiv + previews PNG y reportar paths, actualizar [`docs/guia-implementacion.md`](../../docs/guia-implementacion.md) en 2 lugares (reglas: `§ 🗓 Schedule semanal fijo § Regla de oro`):

**(a) `§ 📍 Dónde estoy hoy`** — actualizar la línea **"Último tangible publicado:"** al final de la sección con el slug + versión recién generados: *"<slug> v<N> (YYYY-MM-DD) → `content/lead-magnets/<slug>/`"*.

**(b) `§ 🎯 Roadmap actual § Prioridad 3 — SISTEMA DE TANGIBLES § Primer tangible activo`** — bumpear el contador si es un tangible nuevo (no una regeneración del mismo). Si es regeneración (ej. Hoja de Compra v3 tras v2), añadir el bump de versión: *"Hoja de Compra ROBOHOGAR (PDF 4pp, v3 validada YYYY-MM-DD)"*.

**(c) `§ 📍 Dónde estoy hoy § 📌 Próximos 3 next steps`** — si el tangible recién generado corresponde a uno de los bullets activos, marcarlo `- [x]` y tirar del siguiente del backlog (`@rules/tangibles.md § Mapeo momento del funnel` + `content/calendario-editorial.md`).

## Rules

- **NO sobreescribir versiones existentes sin `force=True`** (regla no-sobrescritura).
- **Validator duro de tangibles** (sin bypass): si el HTML matchea una prohibición → error, Rafael corrige.
- **Siempre genera preview PNGs** tras el PDF para que Rafael pueda revisar visualmente sin abrir el PDF.
- **El `contenido.md` es fuente de verdad**: si el PDF necesita cambios, editar el markdown primero, regenerar después.
- **Tablero vivo obligatorio:** el paso "Actualizar tablero vivo en guia-implementacion.md" es parte del skill, no opcional.

## Fuentes y referencias

- Reglas editoriales: [`@rules/tangibles.md`](../rules/tangibles.md) § Reglas operativas
- Memoria feedback: `feedback_tangible_no_promises_no_byline.md`, `feedback_checklist_as_mandatory_tangible.md`, `feedback_never_overwrite_images.md`
- Precedente fundador: `content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.html` (v2 validado post-feedback 2026-04-18)
- Skill code: [`skills/pdf_brand/`](../../skills/pdf_brand/)
