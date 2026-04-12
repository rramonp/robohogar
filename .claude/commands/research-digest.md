# Research Digest — Content Aggregation

Fetch, categorize, and summarize robotics news for newsletter prep.

## When to activate

- "research digest", "agrega noticias", "prepara el digest", "busca noticias de robots"

## Script

`utilities/research_aggregator.py` (TODO: implementar)

## Manual workflow (hasta que el script esté listo)

1. Use Firecrawl MCP to scrape key sources:
   - IEEE Spectrum Robotics, The Robot Report, TechCrunch Robotics
   - Xataka (robotics/smart home), ComputerHoy domótica
   - r/RobotVacuums, newsrooms iRobot/Roborock/Ecovacs/Dreame

2. Filter last 14 days, deduplicate similar stories

3. Categorize each story:
   - Categories: Consumer Robots, Robot Vacuums, Lawn Robots, Humanoids, AI/Software, Industry, Reviews
   - Relevance score 1-5 for Spanish home robotics audience

4. Output to `content/drafts/research-digest-YYYY-MM-DD.md`:
   ```markdown
   # Research Digest — YYYY-MM-DD

   ## Top Stories (relevance 4-5)
   - **[Title]** — Source — 1-line summary
     - Ángulo ROBOHOGAR: [por qué importa a nuestra audiencia]

   ## Notable (relevance 3)
   - ...

   ## Monitoring (relevance 1-2)
   - ...
   ```

5. Rafael picks 3-5 stories, adds his angle, and drafts the newsletter
