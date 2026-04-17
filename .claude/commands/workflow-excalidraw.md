---
description: Genera diagramas de flujo y proceso vía Excalidraw MCP siguiendo el estilo visual ROBOHOGAR
---

# Workflow Excalidraw — Generador de diagramas de flujo

Genera flowcharts de proceso usando Excalidraw MCP, siguiendo el estilo visual establecido en `docs/pipeline-skills.excalidraw`.

## Cuándo activar

- "diagrama de flujo", "flowchart", "workflow", "proceso", "mapa de proceso"
- "visualiza el flujo", "cómo funciona el proceso", "genera el diagrama"
- Cualquier descripción de un proceso multi-paso con actores, decisiones o handoffs
- Visualizar pipelines de skills (research → draft → publish → social)

## Antes de construir

1. **Lee** `skills/workflow_excalidraw/references/design-spec.md` — paleta completa, shape types, tipografía, reglas de flechas
2. **Llama** `Excalidraw:read_me` (OBLIGATORIO, una vez por conversación) para cargar el formato MCP
3. **Planifica** la estructura con Rafael: actores/lanes, fases, pasos, decisiones, conexiones
4. **Construye** array de elements siguiendo el design spec
5. **Llama** `Excalidraw:create_view` para renderizar
6. **Guarda** el `.excalidraw` en `docs/` si Rafael lo quiere consultar offline

## Modos de output

### Modo 1 — Renderizado interactivo (default)
Usa Excalidraw MCP directamente. Resultado: diagrama interactivo en la conversación.

### Modo 2 — Archivo `.excalidraw` portable
Guarda en `docs/<nombre>.excalidraw` para que Rafael lo abra/edite en excalidraw.com vía Open (Ctrl+O) o drag-drop. Estructura del archivo en `design-spec.md` sección "Saving as .excalidraw file".

### Modo 3 — Export a URL excalidraw.com
Llama `Excalidraw:export_to_excalidraw` con el JSON enriquecido (seed/version/updated/etc) — devuelve URL compartible. Si falla, usa Modo 2.

## Principios de diseño

- **Estilo limpio, plano** — `roughness=0`, sin sombras, sin efecto hand-drawn
- **Color-coding pastel** — cada tipo de shape tiene un color asignado (ver `design-spec.md`)
- **Single-row horizontal** preferido para pipelines ≤6 nodos
- **Two-row con U-turn** para 7-9 nodos
- **Lanes** solo para >9 nodos o múltiples actores con flujos paralelos
- **Outputs cuelgan debajo** de cada skill con flecha gris dashed
- **Decoración mínima** — sin iconos, sin gradientes, sin elementos innecesarios

## Reglas críticas

- **SIEMPRE leer `design-spec.md`** antes de construir
- **SIEMPRE llamar `Excalidraw:read_me`** primero
- **fontFamily=3** (Cascadia/monospace) en TODOS los textos
- **roughness=0** en TODOS los elementos
- **Shapes deben respirar**: rectángulos 140-180×90 mín, gaps 30-50px horizontal, 100-130px vertical
- **strokeWidth=2** en action shapes, **strokeWidth=1** en lanes y system links
- Decisiones = **diamantes amarillo claro `#fff3bf`**
- Start = **green `#22c55e`** 60×60, End = **red `#ef4444`** 60×60
- Skills (Claude) = **azul claro `#a5d8ff`** + stroke `#4a9eed`
- Manual (Rafael) = **morado claro `#d0bfff`** + stroke `#8b5cf6`
- Outputs = **teal claro `#c3fae8`** + stroke `#15803d`
- Externo (Beehiiv, Buffer) = **naranja claro `#ffd8a8`** + stroke `#f59e0b`
- Flechas main: dark `#1e1e1e`, sólidas, triangle head. System links: gray `#868e96`, dashed
- **Idioma**: español por defecto (audiencia ROBOHOGAR)
- **Camera 4:3 obligatorio**: XL=1200x900 (default), XXL=1600x1200 (panorama). NUNCA otros ratios

## Regla de export (CRÍTICO)

Cuando exportas vía `Excalidraw:export_to_excalidraw`, el shorthand `label` NO renderiza. SIEMPRE usar text elements explícitos con `containerId` binding al shape padre. Ver `design-spec.md` sección "Export to excalidraw.com".

## Ejemplo de referencia

`docs/pipeline-skills.excalidraw` — pipeline ROBOHOGAR de skills (research-digest → content-draft → publish → post-publish → social-content). Two-row layout con U-turn, color-coded por actor, outputs colgando debajo. Usar como template para futuros diagramas de pipeline.
