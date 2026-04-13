# Configuration

## Rutas del proyecto — NUNCA confundir

| Ruta | Qué es | Cuándo usar |
|---|---|---|
| `c:\Users\bakal\robohogar\` | **Repo Git** — código, docs, assets | Desarrollo, commits, scripts |
| `C:\Users\bakal\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter\` | **Vault Obsidian** — sección ROBOHOGAR | Notas, wiki, templates, calendario editorial |
| `C:\Users\bakal\RRP-DEV\projects\robohogar\` | **Mirror RRP-DEV** — docs espejo | Solo referencia cruzada desde RRP-DEV |

**REGLAS:**
- Archivos `.md` de consulta/wiki/templates → Obsidian vault
- Archivos de código, assets, config, docs técnicos → Repo Git
- NUNCA crear carpetas ni archivos .md en rutas incorrectas
- NUNCA buscar el vault — la ruta es la de arriba, siempre

## Project files

| File | Purpose |
|---|---|
| `.mcp.json` | MCP servers (Firecrawl + Playwright) |
| `.claude/rules/*.md` | Project rules |
| `.claude/commands/*.md` | Skills/commands |
| `.claude/memory/` | Persistent memory |
| `CLAUDE.md` | Main project instructions |

## API Keys & Secrets

Secrets go in environment variables or `.claude/settings.local.json` (gitignored). NEVER commit API keys.

Required keys:
- `GEMINI_API_KEY` — image generation (Nano Banana)
- `FIRECRAWL_API_KEY` — web scraping
- Future: `ANTHROPIC_API_KEY` (for research aggregator)

## MCP Servers

- **Playwright** — browser automation, testing landing pages
- **Firecrawl** — web scraping for research aggregation
