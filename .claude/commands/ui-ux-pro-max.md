# UI/UX Pro Max — Design Intelligence

External skill for UI/UX design decisions. BM25 search across 15+ databases.

## When to activate

- "design system", "color palette", "typography", "font pairing"
- "UX review", "accessibility check", "design recommendation"
- Visual design decisions for landing page, newsletter template, social cards

## Location

Scripts in RRP-DEV: `C:/Users/bakal/RRP-DEV/skills/external/ui_ux_pro_max/`

## Usage

### Generate Design System

```bash
python C:/Users/bakal/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "home robotics newsletter editorial" --design-system -p "ROBOHOGAR"
```

### Domain Search

```bash
python C:/Users/bakal/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "editorial magazine clean" --domain style
python C:/Users/bakal/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "newsletter signup" --domain landing
python C:/Users/bakal/RRP-DEV/skills/external/ui_ux_pro_max/scripts/search.py "tech blog modern" --domain typography
```

### Available Domains

style, color, typography, google-fonts, chart, ux, product, landing, icons, react, web

## ROBOHOGAR Design Context

- Palette: fondo crudo `#F5F3EF`, acento verde lima `#C8FF00`, negro `#0D0D0D`
- Typography: Syne (títulos) + DM Sans (cuerpo)
- Style: editorial magazine, clean, generous whitespace
- Inspiration: MIT Technology Review, The Verge
