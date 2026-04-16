# ROBOHOGAR — Claude Project Instructions

## Proyecto

Newsletter + blog en español sobre robótica doméstica y humanoides. Hobby personal de Rafael (3-5 hrs/semana). Dominio: robohogar.com. Plataforma: Beehiiv (free plan, 2.500 subs). Mercado objetivo: España/Europa hispanohablante + LATAM. Posicionamiento: robots que YA llegan al hogar (70% práctico) + visión del hogar robotizado del futuro (30% editorial).

## Scope

**ALWAYS work within the robohogar repository** unless Rafael explicitly specifies an external path.

## Language & Communication

- Respond in **Spanish** unless Rafael explicitly asks for English
- Content (artículos, newsletter) SIEMPRE en español
- Be concise and direct — no filler

## Verification First

Before starting any task, state how you will verify the result. Every deliverable must have a verification method — whether it's running a script, checking output visually, comparing against a reference, or testing in browser. No work without a defined verification step.

## Code — ALWAYS Commented

ALL code (Python, HTML, JS, CSS) must be commented. No exceptions. Comments explain "why" and "how", not "what". A file without comments is an incomplete file. See `@rules/literate-code.md` for density and format requirements.

## Work Efficiency

- **Batch over one-by-one:** when bulk-processing (scraping, API calls, repetitive ops), generate a batch script — never execute one-by-one
- **Token-conscious:** if an operation repeats >5 times identically, write a loop/script first

## Anti-Duplication

Each concept has ONE owner. If something is defined in a rule file, commands reference it with `@rules/` instead of copying. Never duplicate definitions across files — if you find a duplicate, replace it with a reference to the source of truth.

## File Naming

- Rules/commands: `kebab-case.md`
- Python directories: `underscore_case/`
- Filenames: max 60 chars, descriptive
- Drafts with date: `YYYY-MM-DD-slug.md`
- Images: `kebab-case-descriptive.png`

## Utilities Lifecycle

Scripts in `utilities/` are active tools. After a one-shot script is used and no longer needed, move it to `utilities/_archive/`. Only active scripts live in the root of `utilities/`.

## Output Validation

Before generating any final output (publishing an article, generating a definitive image, sending a newsletter): validate content first. Never skip validation. For images: check the asset catalog. For articles: proofread + SEO check. For scripts: syntax + test run.

## Key Directories

| Path | Purpose |
|---|---|
| `content/drafts/` | Borradores de artículos |
| `content/articulos/<slug>/` | Artículos (borrador.html + assets/ por artículo) |
| `content/published/` | Artículos publicados (backup) |
| `assets/branding/master/` | Mascota 2K — assets definitivos |
| `assets/branding/flash-1K/` | Mascota 1K — borradores |
| `assets/branding/con-fondo/` | Mascota en contexto hogar |
| `assets/images/` | Templates genéricos (newsletter header, social card) |
| `docs/brand-voice.md` | **Voz de marca — consultar SIEMPRE para contenido** |
| `docs/` | Planes y estrategia |
| `references/` | Investigación de mercado |
| `utilities/` | Scripts (research aggregator, etc.) |

## Commits

```
Short descriptive title

Changes: <brief summary>

Co-Authored-By: Claude <model> <noreply@anthropic.com>
```

Stage files by name (NOT `git add -A`). Do NOT auto-push unless Rafael asks.

---

@rules/editorial.md
@rules/seo.md
@rules/design.md
@rules/automation.md
@rules/config.md
@rules/literate-code.md
@rules/newsletter.md
