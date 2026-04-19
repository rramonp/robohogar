# ROBOHOGAR — Claude Project Instructions

## Proyecto

Newsletter + blog en español sobre robótica doméstica y humanoides. Hobby personal de Rafael (3-5 hrs/semana). Dominio: robohogar.com. Plataforma: Beehiiv (**plan Scale** — automations, segmentación por tag, digital products, welcome flows y secuencias disponibles). Mercado objetivo: España/Europa hispanohablante + LATAM. Posicionamiento: robots que YA llegan al hogar (70% práctico) + visión del hogar robotizado del futuro (30% editorial).

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

**Anti-IA checklist OBLIGATORIA para todo contenido publicable** (artículo, review, comparativa, editorial, guía, newsletter, ficción): correr [`@references/anti-ia-checklist.md`](references/anti-ia-checklist.md) antes del output final. §1 Universal aplica a todos; §2 Ficción solo a relatos. Todo skill que genere prosa hereda esta regla (ver integración en `ficcion-draft.md` paso 8 y `content-draft.md` paso 8.5). Razón y detalle: `@rules/editorial.md` § Anti-IA checklist.

## Key Directories

| Path | Purpose |
|---|---|
| `content/drafts/` | Borradores y research digests |
| `content/articulos/<slug>/` | Artículos (borrador.html + assets/ por artículo) |
| `content/published/` | Artículos publicados (backup) |
| `content/calendario-editorial.md` | Cadencia semanal, backlog de temas, planificación |
| `content/registro-articulos.md` | Catálogo de artículos publicados |
| `content/registro-newsletters.md` | Catálogo de newsletters enviados |
| `assets/branding/social/final/` | **Logos oficiales** — Monograma R + Icon robot (única fuente de verdad) |
| `assets/branding/social/` | Social media pack — tamaños derivados para redes + variantes tight |
| `assets/branding/_archive/` | Histórico versionado por cleanup |
| `assets/images/` | Templates sociales genéricos sin branding |
| `docs/brand-voice.md` | **Voz de marca — consultar SIEMPRE para contenido** |
| `docs/` | Planes y estrategia |
| `references/` | Investigación de mercado |
| `utilities/` | Scripts (research aggregator, etc.) |

## Skills del pipeline

Skills invocables (definidos en `.claude/commands/`). Pipeline principal en orden:

| Skill | Propósito | Cuándo invocar |
|---|---|---|
| `/research-digest` | Agrega RSS + Firecrawl, categoriza con Claude, genera digest semanal | Lunes o cuando Rafael pida "genera digest" |
| `/content-draft <tema>` | Borrador HTML + PASOS.md + 3 hero variants + inline images | Tras elegir tema del digest o backlog de calendario |
| `/nano-banana` | Generación de imágenes (hero artículo, hero ficción, social) | Invocado por content-draft; manual para branding |
| `/post-publish <URL>` | Limpieza post-publicación (14 pasos) — published, registro, llms.txt, vault sync, commit | Tras pegar URL definitiva en Beehiiv |
| `/social-content <URL>` | Posts LinkedIn/X/IG/WhatsApp listos para Buffer | Invocado automáticamente por post-publish paso 11 |
| `/obsidian-robohogar` | Sync vault (guía, registro, wiki, calendario) | Invocado automáticamente por post-publish paso 12 |

Skills secundarios:
- `/ficcion-draft` — relatos cortos Ficciones Domésticas (pilar ~10%)
- `/pdf-brand cheatsheet <slug>` — genera **PDF tangible + ficha Beehiiv Digital Product** con marca (lead magnets) desde `content/lead-magnets/<slug>/data.py`. Validators bloquean roadmap futuro / fechas de revisión / byline personal automáticamente. Variantes restantes (comparativa/guia/relato) pendientes activación por demanda. Ver `.claude/commands/pdf-brand.md`.
- `/pipeline-debug [scope]` — auditoría repetible del repo (skills, rules, refs, tangibles, memoria, docs, schedule). Invocar al introducir novedad mayor o cada 4-6 semanas como mantenimiento preventivo. Genera report en `content/pipeline-debug-reports/`.
- `/workflow-excalidraw` — diagramas de flujo (uso ocasional)

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
@rules/tangibles.md
@rules/guide-authoring.md
