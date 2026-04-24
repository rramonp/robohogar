---
name: content-draft inline images must be downloaded, never deferred
description: En /content-draft paso 7, nunca marcar imágenes inline como "descarga manual pendiente" — son ejecutables y obligatorias dentro del mismo turno
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
En el skill `/content-draft` paso 7 ("Descargar imágenes inline de fuentes"), las imágenes inline de productos/prensa son **OBLIGATORIAS** y se descargan en el mismo turno usando WebSearch → WebFetch → curl → Pillow (resize/compress). Nunca marcar como "⚠️ descargar manualmente" o "pendiente de Rafael" ni diferir al editor humano.

**Why:** Rafael lo señaló explícitamente el 2026-04-18 en el borrador de `mejor-robot-aspirador-2026`. Caí en un atajo "auto mode-style" justificado como cuidado editorial ("que Rafael verifique la fuente"), pero el skill ya garantiza fuentes oficiales (fabricantes + prensa) y las herramientas disponibles cubren todo el flujo:
1. `WebSearch` encuentra la página oficial del producto
2. `WebFetch` con prompt "extract main product hero image URL" devuelve el `<img src>` directo
3. `curl -fsSL -o <filename>` descarga
4. Pillow redimensiona a ≤1400px ancho + JPG quality 82 → baja de MB a <100 KB

El coste es 3 llamadas WebFetch paralelas + 1 bash de compresión. Es barato. Diferir a manual rompe el pacto del skill ("borrador listo para editar") y carga a Rafael con trabajo que el agente puede hacer.

**How to apply:**
- Vale para CUALQUIER skill cuyos pasos estén descritos con verbos ejecutables ("descargar", "descargar con curl", "generar", "comprimir") y cuyas herramientas estén disponibles (WebSearch, WebFetch, curl, Python/Pillow, image.py de nano-banana). Si puedes ejecutar el paso con el tooling que tienes, ejecútalo — no lo conviertas en TODO para el humano.
- Excepción genuina: el tooling falla (HTTP 404 tras 2 intentos, paywall duro, IP geobloqueado). En ese caso sí documentar como TODO con la URL intentada y el motivo del fallo.
- Patrón operativo para imágenes inline en `/content-draft`:
  1. Por cada modelo/producto referenciado en `<img>` del HTML, ejecutar `WebSearch` en paralelo con query "<marca> <modelo> official product image" (una búsqueda por imagen).
  2. Para cada resultado, ejecutar `WebFetch` sobre la página oficial con prompt "Return the full URL of the main product hero image, nothing else".
  3. `curl -fsSL -o assets/<filename> "<url>"` en bash (escapar `$` en URLs con `\$`).
  4. Pipe a Pillow: resize si width >1400, save JPG quality 82 optimize=True, borrar original si formato distinto.
  5. Validar peso: objetivo <300 KB/imagen web, <200 KB/imagen email. Total <800 KB.
  6. En `PASOS.md`, registrar fuente + peso + status ✅ descargada. No dejar la tabla con `[rellenar]` ni `⚠️ descargar`.
- Extensión a otros skills: aplica igual a `/nano-banana` (ya se ejecuta inline), `/research-digest` (scraping con Firecrawl ejecutable), `/social-content` (generación de assets), etc. Cualquier paso con verbo ejecutable + tool disponible → se ejecuta, no se difiere.
