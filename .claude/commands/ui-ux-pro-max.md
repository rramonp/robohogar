# UI/UX Pro Max — Design Intelligence

External skill for UI/UX design decisions. BM25 search across 15+ databases.

## When to activate

- "design system", "color palette", "typography", "font pairing"
- "UX review", "accessibility check", "design recommendation"
- Visual design decisions for landing page, newsletter template, social cards

## Location

Scripts in RRP-DEV: `$HOME/RRP-DEV/skills/external/ui_ux_pro_max/`

## Usage

### Generate Design System

```bash
python $HOME/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "home robotics newsletter editorial" --design-system -p "ROBOHOGAR"
```

### Domain Search

```bash
python $HOME/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "editorial magazine clean" --domain style
python $HOME/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "newsletter signup" --domain landing
python $HOME/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "tech blog modern" --domain typography
```

### Available Domains

style, color, typography, google-fonts, chart, ux, product, landing, icons, react, web

## ROBOHOGAR Design Context

- Palette: fondo `#FFFFFF`, acento ámbar `#F5A623`, negro `#0C0C0C`, gris `#F2F2F2`
- Typography: Jost (títulos) + DM Sans (cuerpo)
- Style: editorial cálido, magazine-style, generous whitespace
- Inspiration: Newsletter Operator, Morning Brew, The Hustle
- Platform: Beehiiv (free plan)
