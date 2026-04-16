# Research Digest — Content & Competitive Intelligence

Two modes: news aggregation (semanal) and competitive website intelligence (on demand).

## When to activate

- "research digest", "agrega noticias", "prepara el digest", "busca noticias de robots"
- "website intelligence", "competitive analysis", "analiza la competencia", "scrape competitors"
- "5 questions", "website brief", "analiza estos sitios"

## Tools

- **Firecrawl MCP** (preferred): `mcp__firecrawl__scrape`, `mcp__firecrawl__map`, `mcp__firecrawl__search`
- **WebFetch** (fallback): if Firecrawl is not connected, use WebFetch for individual page scraping
- **WebSearch**: for finding competitors and trending topics

If Firecrawl MCP is not connected, notify Rafael and fall back to WebFetch + WebSearch.

## Script

`utilities/research_aggregator.py` — pendiente FASE 10. El skill usa Firecrawl/WebSearch directamente.

---

## MODE 1: News Digest (semanal)

### Sources to scrape

**Tier 1 (always):**
- IEEE Spectrum Robotics, The Robot Report, TechCrunch Robotics, The Verge

**Tier 2 (home robotics):**
- r/RobotVacuums, newsrooms iRobot/Roborock/Ecovacs/Dreame
- Xataka (robotics/smart home), ComputerHoy domótica

**Tier 3 (monitoring):**
- Humanoid Press, Robotics 24/7, integrarobot.com

### Workflow

1. Scrape key sources (Firecrawl `scrape` or WebFetch)
2. Filter last 7 days, deduplicate similar stories
3. Categorize each story:
   - Categories: Consumer Robots, Robot Vacuums, Lawn Robots, Humanoids, AI/Software, Industry, Reviews
   - Relevance score 1-5 for Spanish home robotics audience
4. Output DUAL:
   - Repo: `content/drafts/research-digest-YYYY-MM-DD.md`
   - Vault Obsidian: `$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Research/Research Digest YYYY-MM-DD.md`
   (usar template del vault: `Templates/Template Research Digest.md`)

### Output format

```markdown
# Research Digest — YYYY-MM-DD

## Top Stories (relevance 4-5)
- **[Title]** — Source — 1-line summary
  - Ángulo ROBOHOGAR: [por qué importa a nuestra audiencia]
  - 📷 Imagen: [URL de imagen editorial/prensa si existe]

## Notable (relevance 3)
- ...

## Monitoring (relevance 1-2)
- ...

## Imágenes recopiladas
| Imagen | URL fuente | Uso sugerido |
|--------|-----------|--------------|
| [descripción] | [URL directa] | [qué sección del artículo] |
```

**Recopilar imágenes durante el research:** Para cada Top Story (relevance 4-5), buscar al menos 1 imagen editorial/prensa de la fuente oficial (blog del fabricante, nota de prensa, medio tech). Priorizar fotos reales de producto/evento sobre renders genéricos. Estas imágenes se descargarán en el paso de `/content-draft` para colocarlas en el HTML.

5. **Wiki update**: para cada robot/empresa mencionado en el digest:
   - Si NO existe nota en `Wiki/Robots/` o `Wiki/Empresas/` → crear desde template
   - Si existe → añadir bullet con la noticia + fecha + fuente
   - Ruta vault Wiki: `$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Wiki/`
6. **Actualizar backlog** en `content/calendario-editorial.md` — añadir temas candidatos del digest al backlog con prioridad y keyword SEO
7. Rafael picks 3-5 stories, adds his angle, and drafts the newsletter

---

## MODE 2: Website / Competitive Intelligence

Research-driven analysis of competitor websites for design, content, and conversion strategy.

### Step 1 — Find competitors

Use Firecrawl `search` or WebSearch to find top 10 sites in the target niche.
Score each against these criteria (1-10):

| Criterion | What to look for |
|---|---|
| Search visibility | Page 1 rankings for key industry terms? |
| Review quality | Google reviews, Trustpilot, G2 — 4.5+ stars? |
| Visual design | Modern, professional, not template-looking? |
| Mobile responsive | Clean on mobile, not just "it works"? |
| Content depth | Real copy or placeholder garbage? |
| Social proof | Testimonials, logos, case studies visible? |
| CTA strategy | Clear next step for the visitor? |
| Page speed | Fast load, no layout shift? |

### Step 2 — Deep scrape top 5

For each of the top 5 scoring sites, scrape and extract:

- **Visual identity** — colors (hex), typography, photography style, design aesthetic
- **Content strategy** — headline formula, CTA copy, value prop structure
- **Site architecture** — number of pages, nav structure, depth
- **Conversion strategy** — primary CTA, lead capture method, social proof placement

### Step 3 — Identify patterns

What do ALL top sites do that the bottom ones don't? Find the 3-5 patterns that separate elite from average.

### Step 4 — Brand extraction (if client site exists)

Scrape client's current site and extract: logo, brand colors (from CSS), fonts, tone of voice, key messaging, site structure.

### Output

Save research outputs to `docs/`:
- `docs/competitive-analysis.md` — Full competitor breakdown with comparison table
- `docs/website-brief.md` — 5 Questions answered + consolidated prompt for builder

### 5 Questions Framework

Every website brief must answer:

1. **Who is this website for?** — The visitor, not the business
2. **What's the ONE action?** — Single primary CTA
3. **What objections does the visitor have?** — Maps to sections needed
4. **What's the vibe?** — Feeds design direction
5. **Do you have existing brand assets?** — What exists vs what to create

---

## Rules

- ALWAYS save research outputs as files — every phase is a deliverable
- NEVER start design/build without answering the 5 Questions first
- Cite sources with URLs when using specific data
- Firecrawl credits are limited (500/month free) — be efficient, don't scrape entire sites when a homepage suffices
