# Configuration

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
