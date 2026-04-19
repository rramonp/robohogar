# Ficha Beehiiv Digital Product — template canónico

> Template que todo tangible ROBOHOGAR (lead magnet PDF) debe tener documentado en `content/lead-magnets/<slug>/beehiiv-ficha.md` **ANTES** de subirlo a Beehiiv. El objetivo: que Rafael solo tenga que copy-paste los valores sin pensar decisiones por cada tangible, y que los defaults sean consistentes entre todos los tangibles del repo.
>
> Destilado de la configuración del primer Digital Product (Hoja de Compra, 2026-04-18) tras la sesión de setup en Beehiiv.

---

## Flujo donde encaja esta ficha

1. Skill `/pdf-brand cheatsheet <slug>` genera el PDF + HTML + `beehiiv-ficha.md` precargada con los defaults.
2. Rafael abre la ficha y revisa los campos específicos del tangible (product name, description, product details, slug URL).
3. Rafael sube a Beehiiv → Monetize → Digital Products → New Product y pega los valores directamente de la ficha.
4. Si hay duda sobre un campo, la ficha ya trae default documentado con "por qué este default" abajo.

---

## Plantilla (copiar por cada tangible nuevo)

```markdown
# Ficha Beehiiv Digital Product — <Nombre del Tangible>

> Valores para configurar `<Nombre del Tangible>` en Beehiiv → Monetize → Digital Products → New Product.
> PDF fuente: `content/lead-magnets/<slug>/<slug>-robohogar-<version>.pdf`.

## Campos obligatorios

### File/Download for purchase
Subir: `<slug>-robohogar-<version>.pdf` (ruta: `content/lead-magnets/<slug>/`)

### Product name (*)
```
<Nombre del tangible · descriptor corto>
```
Ej. Hoja de Compra ROBOHOGAR · 10 preguntas antes de comprar

### Description (*)
1-2 frases, 150-200 chars máximo. Debe replicar la `meta_description` del SEO del artículo promotor, adaptada.
```
<qué es + cifra + promesa + formato>
```
Ej. PDF 2 páginas. 10 preguntas que te ahorran 600 € antes de comprar tu robot doméstico.

### Product details (*) — editor rich text (B/I/U/link/list)

Estructura obligatoria en 5 bloques con **bold en los encabezados** de cada bloque:

**Qué es**
<1-2 frases que definen el tangible y su formato>

**Qué cubre**
<scope concreto: qué categorías de producto entran. Si excluye algo relevante — humanoides, ficciones — decirlo aquí como "queda fuera: ...">

**Para quién es**
<3 bullets, cada uno describe un perfil del lector objetivo>
- <primer perfil>
- <segundo perfil>
- <tercer perfil>

**Para quién no es**
<2 bullets honestos de cuándo este tangible NO aplica>
- <caso 1>
- <caso 2>

**Qué incluye**
<lista con las secciones/preguntas/contenidos del tangible; ~10 líneas>
- <sección 1>
- <sección 2>
- ...

**Qué pasa al descargarlo**
<flow exacto: doble opt-in → PDF en email 1 + pregunta → email 2 con 2 artículos + cadencia semanal>

### Call-to-action copy
```
Descargar gratis
```
Default fijo para todos los tangibles ROBOHOGAR (match exacto con el CTA del banner del artículo que trae al suscriptor — coherencia canal a canal).

### Post-purchase redirect
```
(vacío)
```
Default fijo en F1-F2 (0-500 subs): dejar la thank-you page default de Beehiiv. Activar redirect custom cuando haya ≥100 descargas y quieras orientar tráfico post-descarga a un artículo concreto.

### Survey
```
No survey
```
Default fijo. Razón: feedback cualitativo se captura vía reply al Email 1 del welcome flow (señal Gmail + research real). Un survey en post-descarga añade fricción innecesaria.

### Product page URL
```
<slug-corto-tangible>
```
Formato: kebab-case, 2-4 palabras máximo. No "slug-del-tangible-completo-con-descriptor-largo"; sí "hoja-de-compra", "glosario-robohogar", "calendario-rebajas-2026". La URL del product se usa dentro del Email 1 del welcome (link al PDF), no es URL pública viral.

### Send review request emails
```
❌ OFF (toggle desactivado)
```
Default fijo en F1-F2 (0-500 subs). Razón: pedir review a primeros suscriptores con cero trust es cringe y rompe la voz editorial. Activar cuando haya ≥100 descargas reales y quieras prueba social genuina.

### Images
Primary: **imagen 1280×720 (16:9) diseñada específicamente** para el product card de Beehiiv. **NO usar directamente la portada del PDF** — es A4 vertical y Beehiiv la recorta/desborda mal.

Diseño canónico: layout horizontal con lado izquierdo (texto: brand header + título + subtítulo + descriptor + meta "GRATIS · robohogar.com") + lado derecho con bloque ámbar + número decorativo del tangible. Mismos elementos visuales del PDF reorganizados para horizontal.

**Generación automatizable:** crear `assets/thumbnail-1280x720.html` derivado del template [`content/lead-magnets/hoja-compra/assets/thumbnail-1280x720.html`](../lead-magnets/hoja-compra/assets/thumbnail-1280x720.html) (precedente fundador 2026-04-18). Renderizar con Playwright a PNG+JPG:

```bash
uv run --with playwright --with pillow python -c "
from playwright.sync_api import sync_playwright
from PIL import Image
from pathlib import Path
html = Path('content/lead-magnets/<slug>/assets/thumbnail-1280x720.html').resolve().as_uri()
out = Path('content/lead-magnets/<slug>/assets')
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 1280, 'height': 720}, device_scale_factor=1)
    pg = ctx.new_page(); pg.goto(html, wait_until='networkidle')
    pg.screenshot(path=str(out / f'thumbnail-<slug>-1280x720.png'), clip={'x':0,'y':0,'width':1280,'height':720})
    b.close()
Image.open(out / f'thumbnail-<slug>-1280x720.png').convert('RGB').save(out / f'thumbnail-<slug>-1280x720.jpg', 'JPEG', quality=88, optimize=True)
"
```

Peso objetivo: ~40-80 KB JPG (Hoja de Compra: 47 KB).

Secondary (opcional): backcover del PDF (bloque dark "Si te ha servido") — solo si quieres prueba visual extra, no prioridad.

## Resumen para pegar en 5 minutos

| Campo | Valor |
|---|---|
| File | `<slug>-robohogar-<version>.pdf` |
| Product name | `<Nombre · descriptor corto>` |
| Description | `<1-2 frases con cifra y promesa>` |
| Product details | (rich text — ver bloques arriba) |
| Call-to-action copy | `Descargar gratis` |
| Post-purchase redirect | (vacío) |
| Survey | `No survey` |
| Product page URL | `<slug-corto>` |
| Send review request emails | ❌ OFF |
| Images | Primary = portada PDF 1280×720 |
```

---

## Reglas duras (no negociables)

Aplica al Product details igual que al copy del PDF (ver `@rules/tangibles.md § Reglas operativas`):

1. **No listar próximos tangibles** en el Product details. Si el scope excluye humanoides (u otra categoría), decirlo como "queda fuera" (scope), no como "tendremos un documento específico de humanoides próximamente" (roadmap prohibido).
2. **No prometer fechas de revisión** ("actualizamos cada 6 meses", "próxima revisión octubre 2026"). La Product details page es público y permanente — si el tangible pasa 8 meses sin tocar, esa promesa te hace quedar mal.
3. **No byline personal** ("Rafael de ROBOHOGAR"). La voz de la ficha es ROBOHOGAR como medio, no Rafael como autor.
4. **Voz plural editorial** ("nos hacemos", "recibirás", "publicamos") — regla editorial.md § Voz.
5. **Anti-IA §1 Universal** aplica también al copy del Product details. No tapiz/entramado/intrincado/matizado/etc.

---

## Integración con el skill `/pdf-brand`

Cuando ejecutes `/pdf-brand cheatsheet <slug>`, el skill genera en `content/lead-magnets/<slug>/`:

- `<slug>-robohogar-<version>.html` (source HTML)
- `<slug>-robohogar-<version>.pdf` (PDF final)
- `data.py` (estructura de datos que alimenta el template)
- **`beehiiv-ficha.md` (ESTA ficha, con los campos pre-rellenados desde `data.py`)**
- `_preview_<version>/page-{1..N}.png` (previews)

Claude rellena automáticamente desde `data.py` los siguientes campos de la ficha:
- Product name (viene de `title_big + title_small` del data)
- Description (viene de `subtitle` del data)
- Product details (se construye desde `descriptor + intro_paragraphs + items + close_hook`)
- File path (auto-calculado)

Los valores **default fijos** (CTA copy, redirect, survey, review toggle) los rellena Claude con los valores canónicos de este template sin preguntar.

El único campo que Claude NO rellena es el **Product page URL** — ese lo decide Rafael cuando sube el tangible a Beehiiv (short slug diferente del slug interno).

---

## Ejemplo aplicado

Ver `content/lead-magnets/hoja-compra/beehiiv-ficha.md` — ficha completa del primer tangible usando este template. Sirve de referencia concreta al redactar fichas para los próximos tangibles.
