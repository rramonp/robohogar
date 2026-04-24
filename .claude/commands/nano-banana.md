# Nano Banana — Image Generation

Generate images using Google's Gemini image models.

## When to activate

- "genera una imagen", "create an image", "nano banana"
- Any request to generate hero de artículo, hero de ficción, social card, banner, o variante de logo

## Script

Located in RRP-DEV: `$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py`
Invoked via `uv run`.

## Style Reference (MANDATORY)

**Before generating ANY image**, read `assets/branding/asset-catalog.md`. Es la fuente única de verdad para:
- Los 2 logos oficiales (monograma R + icon robot en `social/final/`)
- Cuándo usar cada logo (monograma = espacio; icon = densidad)
- Estilo product-hero cinematográfico para artículos
- Estilo still cinematográfico para ficción
- Registro de heros ya generados (evitar duplicados)

Para **heros de artículos** además leer **SIEMPRE** `assets/branding/nano-banana-prompt-base.md` — decision tree + suffix compilado anti-neones + palabras prohibidas.

## Invocation

```bash
uv run "$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py" \
  --prompt "<description>" \
  --output "<output_path>.png" \
  [--model flash|2|pro] \
  [--aspect square|landscape|portrait|16:9|4:3|9:16|21:9|...] \
  [--size 512|1K|2K|4K]
```

**NO usar `--reference`** para heros (artículos ni ficción) — contamina el estilo fotográfico con ilustración/artefactos.

## Defaults for ROBOHOGAR

| Param | Default | Notes |
|---|---|---|
| `--model` | `flash` | Rápido, calidad suficiente para heros |
| `--aspect` | `landscape` | Heros 1200×630 |
| `--size` | `1K` | Web-optimized |
| `--output` | `content/articulos/<slug>/assets/hero-<slug>-v<N>.png` | Heros de artículo |

## Output paths

| Type | Output to |
|---|---|
| **Hero de artículo** | **`content/articulos/<slug>/assets/hero-<slug>-v<N>.png`** |
| **Hero de ficción** | **`content/ficciones/<serie>/assets/hero-<slug>-v<N>.png`** |
| Variantes de logo / social pack | `assets/branding/social/` |
| Templates sociales genéricos | `assets/images/` |

## Dos modos de generación

### Modo 1: Hero de artículo (product-hero cinematográfico)

- **LEER SIEMPRE PRIMERO:** `assets/branding/nano-banana-prompt-base.md` — decision tree + suffix compilado anti-neones + palabras prohibidas
- Secundariamente: `assets/branding/asset-catalog.md` § "Heros de artículos" para prompts exactos por tipo de artículo
- **NO usar `--reference`**
- Modelo: `flash`. Aspect: `landscape`. Size: `1K`
- Output: `content/articulos/<slug>/assets/hero-<slug>-v<N>.png` (versionar desde v1)

**Composición del prompt (obligatorio):**
```
<prompt específico del artículo, siguiendo decision tree de prompt-base.md>
+ suffix compilado (copiar literal desde prompt-base.md § "Suffix compilado")
```

El suffix evita los 3 fallos recurrentes de Gemini: paneles luminosos en cuerpos de robots, neones en paredes, y caracteres asiáticos en fondos. Iteraciones esperadas: 2-3 por hero.

**Validar tras generación:** checklist en `prompt-base.md` § "Validación rápida post-generación". Si falla → mover a `assets/_archive/` y regenerar.

**Invocado automáticamente por `/content-draft`** como paso del pipeline de creación de artículos.

### Modo 2: Hero de ficción (portada minimalista · objeto-testigo)

**Regla irrenunciable — "cotidiano + sci-fi siempre mezclados":** toda miniatura de Ficciones Domésticas es imagen cotidiana del día a día con un toque de ciencia ficción o robótica humanoide que rompa la tendencia cotidiana. La familia C del catálogo de archetypes (presencia humanoide) NO es opcional — aparece explícita (mano/silueta/fragmento) o indirecta (percha con forma de uniforme, cable de carga, tarjeta ID, sombra humanoide proyectada). Cualquier prompt que haya eliminado C se rechaza antes de enviarlo a Gemini. Fuente: memoria `feedback_ficcion_hero_cotidiano_mas_scifi`.

- **LEER SIEMPRE PRIMERO (los dos archivos, en este orden):**
  1. `assets/branding/asset-catalog.md § 5` — ADN fijo de la serie (fondo, luz base, paleta, anti-triggers)
  2. `assets/branding/ficcion-hero-archetypes.md` — catálogo de 15 archetypes compositivos + algoritmo de selección por tonalidad + regla anti-repetición
- **Elegir archetype ANTES de componer el prompt:**
  1. Leer tonalidad del relato (inquietante / radical / ambiguo / inspirador / mundano) desde el `PASOS.md` o el frontmatter del borrador
  2. Filtrar los 15 archetypes por la matriz tonal del catálogo
  3. Excluir el archetype del último hero del mismo grupo (one-shot / serie) — leer columna `Archetype` de `asset-catalog.md § 5 · Registro de heros ficción`
  4. Si hay varios candidatos, preferir el que más se diferencie a thumbnail 120px por silueta / ángulo / presencia humanoide
- **Componer el prompt:** partir del esqueleto canónico de `asset-catalog.md § 5 · Prompt template canónico` y sustituir las partes variables por los fragments del archetype elegido en `ficcion-hero-archetypes.md § Prompt fragments por archetype` (A · B/C · D).
- NO usar `--reference`
- Modelo: `2`. Aspect: `16:9`. Size: `2K` (usar `--model 2 --aspect 16:9 --size 2K`, luego crop Pillow a 1200×630 si hace falta — el bug `--model flash` cae a 1024×1024, no usar)
- Output: `content/ficciones/<serie-o-_one-shots>/<slug>/assets/hero-<slug>-v<N>.png`
- **Post-generación:** ejecutar la checklist de 8 puntos de `asset-catalog.md § 5 · Validación pre-output`. Si falla → archivar v en `<slug>/assets/_archive/hero-v<N>-<motivo>-YYYY-MM-DD.png` y regenerar con v+1. Al aceptar una v, actualizar el registro con el archetype usado.

## Workflow

1. **Read `assets/branding/asset-catalog.md`** — check what already exists, avoid duplicates
2. Determinar modo: ¿hero de artículo o hero de ficción?
3. Leer la sección correspondiente del catálogo (y `prompt-base.md` si es artículo)
4. Crear carpeta del artículo/relato si no existe
5. Run the script via `uv run`
6. Confirm output path to user
7. **NEVER overwrite** existing images — use versioned filenames (-v2, -v3)
8. **Update `assets/branding/asset-catalog.md`** — añadir nueva fila en tabla de registro correspondiente

## Post-generación: fondo blanco y recorte (OBLIGATORIO para assets de logo/social pack)

Toda variante de logo o social pack que genere Nano Banana debe entregarse con:

1. **Fondo blanco puro (255,255,255)** — nunca transparente, nunca checkerboard horneado
2. **Recortada al contenido** — sin espacio blanco sobrante, solo ~15px padding
3. **Formato JPG** además de PNG — para uso en email/Beehiiv donde la transparencia da problemas
4. Si Gemini genera checkerboard horneado en los píxeles (grises ~204-240 alternando), limpiar con script antes de entregar

```python
# Limpiar checker + recortar + exportar JPG
from PIL import Image
img = Image.open(path).convert('RGB')
pixels = img.load()
w, h = img.size
for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        if r > 230 and g > 230 and b > 230:
            pixels[x, y] = (255, 255, 255)
# Crop to content bbox + pad
# Save as JPG quality=95 + PNG
```

Los heros de artículo/ficción NO pasan por este paso — son imágenes fotográficas, no branding.

## Requirements

- `uv` in PATH
- `GEMINI_API_KEY` set in environment
