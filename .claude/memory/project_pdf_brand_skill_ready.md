---
name: Skill /pdf-brand cheatsheet operativo desde 2026-04-18
description: ROBOHOGAR tiene skill /pdf-brand cheatsheet funcional para generar lead magnets PDF desde un data.py. Variantes comparativa/guia/relato pendientes.
type: project
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
ROBOHOGAR tiene el skill **`/pdf-brand cheatsheet`** operativo desde 2026-04-18 para generar tangibles PDF con marca. Adelantado del roadmap original (que preveía activarlo ~50 subs) por disponibilidad de plan Beehiiv Scale + validación del primer PDF manual (Hoja de Compra v2).

**Why:** Rafael pidió el 2026-04-18 construir el skill tras validar el v2 manual de Hoja de Compra: *"ok adelante con pdf-brand cheatsheet para generar futuros tangibles"*. Razones:

1. **Amortización real:** tras el v2 manual (~4 h de diseño iterativo), el patrón visual quedó fijado. Construir skill + template ahora sale barato (1 sesión Claude) y cada tangible futuro baja de ~4 h a ~30 min.
2. **Plan Scale ya pagado:** no hay fricción técnica (automations + digital products ya disponibles en Beehiiv).
3. **5 tangibles candidatos inmediatos** del roadmap editorial (Hoja de Compra, Guía primer mes aspirador, Glosario 40 términos, Calendario rebajas ES, Dossier Ficciones) — con skill, los 5 son viables en 1 mes.

**Cómo se invoca:**

```
/pdf-brand cheatsheet <slug> [version]
```

Claude lee `content/lead-magnets/<slug>/contenido.md` + `data.py`, valida prohibiciones, llama a `render_cheatsheet()`, genera HTML+PDF+previews PNG, reporta.

**Arquitectura del skill (code layout):**

```
skills/pdf_brand/
  __init__.py                          ← API pública
  render.py                            ← render_cheatsheet(data, output_dir, force, skip_pdf)
  validators.py                        ← 6 patrones prohibidos (roadmap futuro, fechas, byline)
  cli.py                               ← uv run CLI fallback
  templates/
    cheatsheet.html.jinja2             ← template destilado del v2 validado
  assets/
    icon-robot.png                     ← asset compartido (se copia al output dir de cada tangible)

.claude/commands/
  pdf-brand.md                         ← command para invocación desde Claude
```

**Patrón de generación — cada tangible nuevo:**

1. Crear `content/lead-magnets/<slug>/contenido.md` (fuente humana, editable).
2. Crear `content/lead-magnets/<slug>/data.py` con la variable `data: dict` siguiendo el contract del template (ver `render.py` docstring).
3. Invocar `/pdf-brand cheatsheet <slug>` o `uv run skills/pdf_brand/cli.py cheatsheet <path>/data.py`.
4. Revisar previews PNG en `_preview_<version>/`.
5. Iterar `data.py` o el CSS del template. Cada iteración: incrementar `version` en data.py (nunca sobreescribir v previa — `feedback_never_overwrite_images.md`).

**Validator duro (sin bypass):** 6 patrones prohibidos en el HTML generado:
- `Próximos tangibles` (roadmap)
- `Próxima revisión prevista` (fecha revisión)
- `actualizamos cada N meses` (promesa cadencia)
- `reciben la v2, v3` (versiones futuras)
- `vamos expandiendo` (promesa expansión)
- `Rafael de ROBOHOGAR` (byline personal — permitido en artículos, NO en PDFs)

Si cualquiera matchea → `ValidationError`, Rafael corrige y re-ejecuta. Fuente: `feedback_tangible_no_promises_no_byline.md`.

**Variantes pendientes (F4C expansion según demanda):**

| Variante | Uso | Status |
|---|---|---|
| `cheatsheet` | preguntas-antes-de-comprar, dossiers N datos clave | ✅ v1 operativo |
| `comparativa` | tablas benchmark standalone | 🔜 activar con primer tangible que lo requiera (Calendario rebajas) |
| `guia` | guías step-by-step (primer mes, glosario) | 🔜 activar con Guía primer mes aspirador si cheatsheet no encaja |
| `relato` | ficciones ilustradas (Dossier Ficciones) | 🔜 activar con Dossier Ficciones |

Cada nueva variante reusa `validators.py` + `render.py` lógica de export; solo añade template Jinja2 propio.

**Precedente fundador:** `content/lead-magnets/hoja-compra/` tiene (a) `contenido.md` humano, (b) `data.py` estructurado, (c) `hoja-compra-robohogar-v3.pdf` generado por el skill con paridad 100% vs v2 manual. Usar este directorio como plantilla mental para el próximo tangible.

**No confundir con `utilities/pdf_export.py`** — ese script es una utilidad genérica HTML→PDF (Playwright wrapper). El skill `/pdf-brand` es la capa editorial con template brand + validators + contract data.
