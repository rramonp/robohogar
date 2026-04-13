# Nano Banana — Image Generation

Generate images using Google's Gemini image models.

## When to activate

- "genera una imagen", "create an image", "nano banana"
- Any request to generate visual assets, mascot variations, social cards, banners

## Script

Located in RRP-DEV: `$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py`
Invoked via `uv run`.

## Style Reference (MANDATORY)

**Before generating ANY image**, read `assets/branding/mascota-prompt.md`. This is the single source of truth for:
- Character description (shape, eyes, apron, antennas, proportions)
- Base prompt template for all variations
- Consistency rules (orange LED eyes, blue checkered apron, kawaii proportions)
- Full pose catalog (11 poses with exact prompts)
- Usage map per newsletter section

When the user asks for mascot images, variations, or "de mi estilo" / "estilo ROBOHOGAR":
1. Read `assets/branding/mascota-prompt.md`
2. Use the **base prompt template** from that file (not free-form)
3. ALWAYS use `--reference` pointing to a master image for style anchoring

## Invocation

```bash
uv run "$HOME/RRP-DEV/skills/external/nano_banana/scripts/image.py" \
  --prompt "<description>" \
  --output "<output_path>.png" \
  [--model flash|2|pro] \
  [--aspect square|landscape|portrait|16:9|4:3|9:16|21:9|...] \
  [--size 512|1K|2K|4K] \
  [--reference assets/branding/master/<file>.png]
```

## Defaults for ROBOHOGAR

| Param | Default | Notes |
|---|---|---|
| `--model` | `2` | Balanced speed + 4K |
| `--aspect` | `square` | Social cards, mascot poses |
| `--size` | `1K` | Web-optimized |
| `--output` | `assets/images/<slug>.png` | Article/general images |
| `--reference` | `assets/branding/master/robohogar-mascot-principal.png` | Mascot consistency anchor |

## Output paths

| Type | Output to |
|---|---|
| Mascot new poses (master quality) | `assets/branding/master/` |
| Mascot drafts/tests | `assets/branding/flash-1K/` |
| Mascot in context/scene | `assets/branding/con-fondo/` |
| **Hero de artículo** | **`content/articulos/<slug>/assets/hero-<slug>.png`** |
| Templates genéricos (newsletter, social card) | `assets/images/` |

## Dos modos de generación

### Modo 1: Mascota (poses, variaciones, social cards)

- Leer `assets/branding/mascota-prompt.md` — prompt base + reglas de consistencia
- Usar `--reference` apuntando a una imagen master para anclar el estilo
- Modelo: `2` o `pro`. Aspect: `square`

### Modo 2: Hero de artículo (thumbnails para blog/newsletter)

**Estilo obligatorio: Product-hero cinematográfico (tipo YouTube thumbnail)**

- Leer `assets/branding/asset-catalog.md` sección "Estilo ROBOHOGAR para heros de artículos"
- Ahí están los prompts exactos por tipo de artículo, las reglas visuales y los parámetros
- **NO usar `--reference`** — contamina el estilo fotográfico con ilustración/texto asiático
- Modelo: `flash`. Aspect: `landscape`. Size: `1K`
- Output: `content/articulos/<slug>/assets/hero-<slug>.png`

Prompt template rápido:
```
Eye-catching editorial hero image for an article about [TEMA].
[PRODUCTO/ROBOT protagonista, dramáticamente iluminado].
[Contexto hogar moderno, desenfocado].
Warm amber lighting, editorial photography style, high contrast, shallow depth of field.
Absolutely NO text, NO letters, NO words, NO signs, NO writing of any kind.
```

**Invocado automáticamente por `/content-draft`** como paso del pipeline de creación de artículos.

## Workflow

1. **Read `assets/branding/asset-catalog.md`** — check what already exists, avoid duplicates
2. Determinar modo: ¿mascota o hero de artículo?
3. Si mascota → read `mascota-prompt.md`, usar prompt base + `--reference`
4. Si hero de artículo → read `asset-catalog.md` sección estilo, usar prompt template SIN `--reference`
5. Crear carpeta del artículo si no existe: `content/articulos/<slug>/assets/`
6. Run the script via `uv run`
7. Confirm output path to user
8. NEVER overwrite existing images — use versioned filenames (-v2, -v3)
9. **Update `assets/branding/asset-catalog.md`** — añadir nueva fila en tabla "Heros de artículos"

## Requirements

- `uv` in PATH
- `GEMINI_API_KEY` set in environment
