---
name: Tangibles ROBOHOGAR — ninguna promesa futura ni byline personal
description: PDFs tangibles de ROBOHOGAR no contienen (a) lista de próximos tangibles, (b) fechas de revisión/actualización prometidas, (c) byline personal "Rafael de ROBOHOGAR". Son documentos del medio.
type: feedback
---
Los PDFs tangibles de ROBOHOGAR (Hoja de Compra, Guía primer mes, Glosario, Calendario…) no contienen ninguna de estas 3 formas de "compromiso":

1. **Roadmap de próximos tangibles:** prohibido listar qué otros PDFs/guías existirán.
2. **Fechas de revisión / promesas de actualización:** prohibido comprometerse a cadencia.
3. **Byline personal:** prohibido *"Rafael de ROBOHOGAR"* como firma en el PDF. La firma correcta es simplemente *"ROBOHOGAR"* (+ icon robot si hay firma visual).

**Why:** Rafael lo estableció en 3 intervenciones el 2026-04-18 durante el v2 de Hoja de Compra. Razones objetivas:
- Anunciar roadmap crea deudas editoriales.
- Listar tangibles futuros diluye el valor del que el lector tiene delante.
- Un "actualizamos cada 6 meses" obliga aunque no haya cambios.
- Byline personal en PDF = inconsistente con el tono editorial del medio.

**How to apply:**

**Sustituir** el bloque "Actualización viva / Próximos tangibles" por un **bloque de invitación a compartir**:
- Eyebrow: `SI TE HA SERVIDO`
- Título: `Reenvía esta Hoja / Guía a quien esté mirando robots`
- Subtítulo: `No hace falta permiso. Lo único que pedimos es que le sirva al siguiente.`

**Sustituir** la firma: `ROBOHOGAR · abril 2026 · vN` (con icon robot).

**Verificación pre-PDF:** antes de generar cualquier PDF tangible, `grep -E "Próximos tangibles|Próxima revisión|actualizamos cada|vamos expandiendo|Rafael de ROBOHOGAR"`. Si matchea, reescribir antes de export. El validator de `/pdf-brand` ya bloquea automáticamente.

**Excepción sobre byline:** sí permitido en artículos Beehiiv (sección "Sobre el autor"). La regla singular está restringida a **PDFs tangibles descargables**.

**Precedente:** `content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.html` (post-2026-04-18).
