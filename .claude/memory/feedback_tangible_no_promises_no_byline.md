---
name: Tangibles ROBOHOGAR — ninguna promesa futura ni byline personal
description: PDFs tangibles de ROBOHOGAR no contienen (a) lista de próximos tangibles, (b) fechas de revisión/actualización prometidas, (c) byline personal "Rafael de ROBOHOGAR". Son documentos del medio.
type: feedback
originSessionId: be1c5a52-ae1a-4d6e-9adc-a2a2cd2570ad
---
Los PDFs tangibles de ROBOHOGAR (Hoja de Compra, Guía primer mes, Glosario, Calendario…) no contienen ninguna de estas 3 formas de "compromiso":

1. **Roadmap de próximos tangibles:** prohibido listar qué otros PDFs/guías existirán. Fórmulas tipo *"Próximos tangibles para suscriptores: Guía de los primeros 30 días · Glosario de 40 términos · Calendario de rebajas ES"* → ❌ bloquear.
2. **Fechas de revisión / promesas de actualización:** prohibido comprometerse a cadencia. Fórmulas tipo *"Esta Hoja la actualizamos cada 6 meses"*, *"Próxima revisión prevista: octubre 2026"*, *"Los suscriptores reciben la v2, v3 automáticamente"* → ❌ bloquear.
3. **Byline personal:** prohibido *"Rafael de ROBOHOGAR"* como firma en el PDF. La firma correcta es simplemente *"ROBOHOGAR"* (+ icon robot si hay firma visual). El PDF es documento editorial del medio, no artículo de opinión personal.

**Why:** Rafael lo estableció en 3 intervenciones consecutivas el 2026-04-18 durante la afinación del v2 de Hoja de Compra:
- *"lo de rafael de robohogar creo que no es necesrio, no es un articulo, basta poner robohogar"* → regla #3.
- *"esto quitalo, nunca pongas algo similar en ningun tangible: Próximos tangibles para suscriptores: Guía de los primeros 30 días · Glosario de 40 términos · Calendario de rebajas ES · Guía del early adopter de humanoides"* → regla #1.
- *"tambien quita Próxima revisión prevista: octubre 2026. o similar, no quiero compromisos"* → regla #2.

Razones objetivas:
- **Compromiso público incómodo:** anunciar roadmap crea deudas editoriales; si un tangible se retrasa queda mal ante el suscriptor.
- **Fragmentación de marca:** listar 4 tangibles futuros diluye el valor del que el lector tiene delante.
- **Commitment público de revisión:** un "actualizamos cada 6 meses" obliga a hacerlo aunque no haya cambios en mercado o no haya tiempo.
- **Byline personal en PDF = inconsistente con el tono editorial del medio.** En artículos la byline humaniza (es opinión, persona). En PDF tangible el documento es producto del medio, no firma de autor.

**How to apply:**

**Sustituir** el bloque "Actualización viva / Próximos tangibles" por un **bloque de invitación a compartir** (cero compromiso, mismo impacto visual):
- Eyebrow: `SI TE HA SERVIDO`
- Título: `Reenvía esta Hoja / Guía a quien esté mirando robots / acabe de comprar su primer robot / etc.`
- Subtítulo: `No hace falta permiso. Lo único que pedimos es que le sirva al siguiente.`

**Sustituir** la firma:
- Antes: `Rafael de ROBOHOGAR · robohogar.com · abril 2026 · vN`
- Después: `ROBOHOGAR · abril 2026 · vN` (con icon robot como firma visual si el layout lo permite).

**Verificación pre-PDF:** antes de generar cualquier PDF tangible, `grep -E "Próximos tangibles|Próxima revisión|actualizamos cada|vamos expandiendo|Rafael de ROBOHOGAR"` en el HTML y el contenido.md. Si matchea, reescribir antes de export.

**Excepción sobre byline:** sí permitido en artículos Beehiiv (sección "Sobre el autor" o byline `Rafael de ROBOHOGAR`). La regla singular está restringida a **PDFs tangibles descargables**. Artículos siguen la regla editorial.md (byline permitido en bio/firma).

**Precedente:** `content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.html` (después del 2026-04-18, post-feedback) — bloque dark con "Si te ha servido → Reenvía esta Hoja" reemplazando "Actualización viva". Firma con solo ROBOHOGAR + icon. Portada sin eyebrow "LEAD MAGNET".
