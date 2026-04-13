# Automation Rules

## Principio

Automatizar todo EXCEPTO juicio editorial y voz. La opinión y personalidad son manuales siempre.

## Pipeline de contenido

```
RSS feeds → Script Python → Claude API categoriza → Research Digest .md
Rafael elige temas + ángulos → Claude genera borrador → Rafael edita → Publicar en Beehiiv
Publicación → Canva Reels + Buffer → Instagram, LinkedIn, X
```

Detalle completo: `docs/plan-v2.md` sección 4.

## Scripts (utilities/)

- `research_aggregator.py` — fetch RSS, scrape con Firecrawl, categoriza con Claude API
- Futuros: social post generator, newsletter formatter

## Herramientas externas

| Tool | Función | Coste |
|---|---|---|
| Make.com | Orquestación RSS→Claude→Buffer | 9€/mes |
| Buffer | Programación social (LinkedIn, X, Threads) | 6€/mes |
| Firecrawl | Scraping (MCP + API) | Free tier (500 créditos/mes) |
| Claude API | Categorización + generación borradores | ~$0.10/run |

## Reglas de automatización

- NUNCA publicar contenido auto-generado sin revisión manual de Rafael
- Scripts deben ser idempotentes (re-ejecutar no duplica)
- Outputs intermedios van a `content/drafts/` con fecha en filename
- Logs de ejecución a stdout, no a archivos (por ahora)
