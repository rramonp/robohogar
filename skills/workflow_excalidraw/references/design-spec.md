# Workflow Excalidraw — Design Specification

Reference: `High Value Reconfirmations Link.excalidraw` (107 elements, March 2026) — adaptado a ROBOHOGAR.

---

## Global Style

- **roughness**: 0 (clean lines, no hand-drawn effect)
- **fillStyle**: solid
- **fontFamily**: 3 (Cascadia / monospace) — ALL text elements
- **roundness**: null (sharp corners) for swimlanes; `{type:3}` for action shapes (rounded)
- **Canvas**: white background. Camera sizes 4:3 (XL=1200x900 typical, XXL=1600x1200 panorama)

## Color Palette by Shape Type

### Action Shapes (rectangles)

| Type | Background | Stroke | Usage |
|---|---|---|---|
| Skill (Claude/auto) | `#a5d8ff` (light blue) | `#4a9eed` | Skill invocations, automated steps |
| Manual (Rafael) | `#d0bfff` (light purple) | `#8b5cf6` | Decisions, edits, manual actions |
| External / publish | `#ffd8a8` (light orange) | `#f59e0b` | Beehiiv, Buffer, plataformas externas |
| Output / storage | `#c3fae8` (light teal) | `#15803d` | Files, registros, vault, plataformas |
| System node | `#038287` (dark teal) | `#ffffff` | Files, databases, unified sources |

All action shapes: strokeWidth=2, opacity=100, roundness `{type:3}`.

### Decisions (diamonds)

| Background | Stroke | Text |
|---|---|---|
| `#fff3bf` (light yellow) | `#1e1e1e` | 16pt, question format ("¿Artículo o ficción?") |

### Start / End (ellipses)

| Type | Background | Stroke | Size |
|---|---|---|---|
| Start | `#22c55e` (green) | `#15803d` | 60x60 |
| End | `#ef4444` (red) | `#dc2626` | 60x60 |

Label "S" or "E" in white, centered. Font size 22pt, fontFamily=3.

### Lanes (opcional, para diagramas con múltiples actores)

| Element | Background | Stroke | Opacity |
|---|---|---|---|
| Lane background | transparent | `#001635` or `#1e1e1e` | 30 |
| Lane header | `#343a40` (dark gray) | `#ffffff` | 100 |

Lane headers: white text, 20pt, bold. Actor name (e.g., "Rafael", "Skill", "Output").

### YES/NO Labels

| Label | Background | Size |
|---|---|---|
| YES (positive path) | `#b2f2bb` (light green) o transparent | 16pt |
| NO (negative/alternate path) | `#a5d8ff` (light blue) o transparent | 16pt |

Position near the diamond branch point.

## Arrows

### Main flow (action to action)

```
strokeColor: #1e1e1e
strokeWidth: 2
strokeStyle: solid
endArrowhead: triangle
startArrowhead: null
```

### System / background links (output dropdowns, optional steps)

```
strokeColor: #868e96
strokeWidth: 1
strokeStyle: dashed
endArrowhead: triangle
```

Use dashed gray arrows for: (a) skill → output dropdowns, (b) optional/conditional steps, (c) dashed-styled action boxes.

## Typography

**ALL text uses fontFamily=3** (Cascadia / monospace).

| Element | Font Size | Color | Notes |
|---|---|---|---|
| Title | 24-28pt | `#1e1e1e` | Top of diagram |
| Subtitle | 15-16pt | `#757575` | Below title |
| Action shape text | 14-16pt | `#1e1e1e` | Centered, max 3 lines |
| Decision text | 14-16pt | `#1e1e1e` | Question format |
| Lane header | 20pt | `#ffffff` | Centered |
| Output text | 13-14pt | `#1e1e1e` | Multi-line OK |
| Start/End label | 22pt | `#ffffff` | "S" or "E", centered |

## Layout Rules

### Single-row horizontal flow (default for ROBOHOGAR pipelines)

Recommended for ≤6 nodes: flow goes LEFT → RIGHT, outputs hang BELOW each skill.

```
S ───► action ───► action ───► action ───► E
        │            │            │
        ▼            ▼            ▼
      output      output      output
```

### Two-row layout (for 7-9 nodes)

Use a U-turn arrow from end of row 1 down to start of row 2.

```
S ───► A ───► B ───► C ───► D ─┐
                                │ (U-turn)
   ┌────────────────────────────┘
   ▼
   E ───► F ───► G ───► End
   │      │      │
   ▼      ▼      ▼
 output output output
```

U-turn arrow points example (start at right edge of last row-1 node):
`points:[[0,0],[30,0],[30,235],[-685,235],[-685,265]]`

### Spacing Guidelines (CRITICAL — shapes must breathe)

- **Action shapes**: 140-180 wide × 90 tall (generous for 14-16pt text, 2-3 lines)
- **Diamonds**: 155×155 minimum
- **Start/End ellipses**: 60×60
- **Horizontal gap** between shapes: 30-50px
- **Vertical gap** between rows: 100-130px
- **Output gap below action**: 40-50px (with dashed gray arrow)

### Connection Points (Excalidraw MCP)

- `fixedPoint: [0.5, 0]` = top center
- `fixedPoint: [1, 0.5]` = right center
- `fixedPoint: [0.5, 1]` = bottom center
- `fixedPoint: [0, 0.5]` = left center

Main flow same-row: right-of-source → left-of-target.
Skill → output: bottom-of-source → top-of-target.
Cross-row: bottom → top via elbowed arrow.

## Excalidraw MCP Workflow

1. Call `Excalidraw:read_me` (once per conversation)
2. Plan elements: title → legend → start ellipse → flow nodes → outputs → end ellipse
3. Build elements array with correct IDs, positions, bindings
4. Call `Excalidraw:create_view` with camera size XL (1200x900) or XXL (1600x1200)
5. Use multiple `cameraUpdate` to animate (zoom into title first, pan out to full diagram)
6. Iterate based on Rafael's feedback
7. (Optional) Save `.excalidraw` file to `docs/` for offline consultation

## Export to excalidraw.com (CRITICAL)

The `label` shorthand on shapes works in MCP `create_view` but does NOT render when exporting JSON to excalidraw.com. For portable diagrams, ALWAYS use explicit text elements with `containerId`:

```json
{"type":"rectangle","id":"box1","x":100,"y":100,"width":185,"height":90,
 "backgroundColor":"#a5d8ff","fillStyle":"solid","strokeColor":"#1e1e1e",
 "strokeWidth":2,"roughness":0,
 "boundElements":[{"id":"box1_t","type":"text"}]},
{"type":"text","id":"box1_t","x":110,"y":120,"width":165,"height":50,
 "text":"Label text\n(line 2)","fontSize":16,"strokeColor":"#1e1e1e",
 "fontFamily":3,"textAlign":"center","verticalAlign":"middle",
 "containerId":"box1"}
```

Every labeled shape needs BOTH:
- The shape with `boundElements: [{"id":"text_id","type":"text"}]`
- A text element with `containerId: "shape_id"`, `textAlign: "center"`, `verticalAlign: "middle"`

## Saving as `.excalidraw` file (offline)

Si Rafael quiere consultarlo offline, guardar como `docs/<nombre>.excalidraw` con esta estructura:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [ ... ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null
  },
  "files": {}
}
```

Cada elemento necesita campos extra para el formato file:
- `seed`, `versionNonce`, `version`, `updated` (números únicos)
- `groupIds: []`, `frameId: null`, `boundElements: []`, `link: null`, `locked: false`, `angle: 0`
- `backgroundColor: "transparent"`, `fillStyle: "solid"`, `strokeWidth`, `strokeStyle`, `opacity: 100`
- Para arrows: `lastCommittedPoint: null`, bindings con `focus: 0, gap: 1`
- Para text: `textAlign`, `verticalAlign`

Rafael puede arrastrar el archivo a excalidraw.com (Open / Ctrl+O) para visualizar y editar.
