# Nano Banana — Image Generation

Generate images using Google's Gemini image models.

## When to activate

- "genera una imagen", "create an image", "nano banana"
- Any request to generate visual assets, mascot variations, social cards, banners

## Script

Located in RRP-DEV: `C:/Users/bakal/RRP-DEV/skills/external/nano_banana/scripts/image.py`
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
uv run "C:/Users/bakal/RRP-DEV/skills/external/nano_banana/scripts/image.py" \
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
| Article images, banners, social cards | `assets/images/` |

## Workflow

1. **Read `assets/branding/asset-catalog.md`** — check what already exists, avoid duplicates
2. **Read `assets/branding/mascota-prompt.md`** — character spec, base prompts, pose catalog
3. If mascot variation → use base prompt template + variation text from mascota-prompt.md
4. If general image (not mascot) → build prompt freely but keep ROBOHOGAR visual identity (clean, editorial, warm)
5. Run the script via `uv run`
6. Confirm output path to user
7. NEVER overwrite existing images — use versioned filenames (-v2, -v3)
8. **Update `assets/branding/asset-catalog.md`** — add the new image with file, folder, date, description

## Requirements

- `uv` in PATH
- `GEMINI_API_KEY` set in environment
