# Configuration

## Rutas del proyecto — NUNCA confundir

| Ruta | Qué es | Cuándo usar |
|---|---|---|
| Repo Git (desktop) | `c:\Users\cri-c\robohogar\` | Desarrollo, commits, scripts |
| Repo Git (laptop) | `c:\Users\bakal\robohogar\` | Desarrollo, commits, scripts |
| **Vault Obsidian** | resolver vía `python utilities/get_vault_path.py` (autodetect bakal/cri-c) | Notas, wiki, templates, calendario editorial |
| Mirror RRP-DEV | `$HOME/RRP-DEV/projects/robohogar/` | Solo referencia cruzada desde RRP-DEV |

**REGLAS:**
- Archivos `.md` de consulta/wiki/templates → Obsidian vault
- Archivos de código, assets, config, docs técnicos → Repo Git
- NUNCA crear carpetas ni archivos .md en rutas incorrectas
- **NUNCA usar literal `$HBX_VAULT` en bash** — la variable no está exportada al shell de Claude Code. Usar siempre `VAULT=$(python utilities/get_vault_path.py)`. El helper autodetecta laptop/desktop sin depender de variables externas. Detalle: `@.claude/commands/obsidian-robohogar.md § Vault Path`.
- El vault está SIEMPRE accesible (sincronizado vía OneDrive HBX Group + Syncthing entre laptop bakal y desktop cri-c). Si el helper falla, hay un problema de configuración, no de "vault desconectado" — investigar antes de saltar el sync.

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
