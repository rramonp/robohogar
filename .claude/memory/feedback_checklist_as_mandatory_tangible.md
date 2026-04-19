---
name: ROBOHOGAR checklist accionable = tangible mínimo obligatorio + promoción en subtítulo
description: Todo artículo ROBOHOGAR incluye una checklist de 3-7 ítems como tangible mínimo y lo menciona con cifra en subtítulo + meta_description
type: feedback
---
Todo artículo ROBOHOGAR (review, comparativa, guía, editorial, tutorial, newsletter) debe incluir **una checklist accionable de 3-7 ítems concretos** antes del veredicto/cierre, y **promocionarla en el subtítulo + meta_description** con cifra concreta. Es el tangible mínimo obligatorio — no hay artículo que se publique sin él.

**Why:** Rafael lo validó el 2026-04-18 al revisar `mejor-robot-aspirador-2026`. Observación literal: *"me gusta la tabla que hiciste en el anterior artículo con las preguntas que debe de hacerse cualquiera antes de comprar un aspirador robot, eso es tangible, podríamos siempre poner algo similar en los artículos como mínimo, y promocionarlo en el subtítulo del artículo que sale en la miniatura"*. Razones objetivas:

1. **ROI máximo por tiempo editorial:** una checklist son 5-7 líneas, 10 min de trabajo, y crea un "producto" reconocible en el artículo.
2. **OG card competitiva:** el subtítulo que aparece en la miniatura (landing, OG card de Twitter/LinkedIn, SERP de Google) es el primer contacto del lector. *"La guía honesta, sin hype"* compite peor que *"checklist de 5 preguntas que te ahorra 600 €"*. Cifra + tangible > adjetivos.
3. **Fase F1 (0-50 subs):** en pre-audiencia, cada OG card cuenta.
4. **Coherencia con pivote Cole 2026:** el tangible es el producto; la checklist es el tangible más barato y repetible. Ver `@rules/tangibles.md` § Reglas operativas.

**How to apply:**

1. **En el skill `/content-draft`:** paso 8.7 obligatorio. Checklist embebida con `<div class="checklist">` + H2 que empiece por `Checklist —` (ej: `Checklist — 5 preguntas antes de comprar`). Si el tema no admite checklist natural, sustituir por decision tree mini (4-6 bifurcaciones), dossier "3 datos clave" o cuadro "qué hacer / qué no hacer" — nunca omitir.
2. **Subtítulo obligado:** fórmula `<qué entrega el artículo> + <tangible con número>`.
3. **`meta_description` (≤155 chars):** replicar la promesa del subtítulo reformulada para SEO.
4. **`seo_title` (≤60 chars):** incorporar `+ checklist` si la keyword deja margen.
5. **Rechazo automático:** si un borrador sale sin checklist/tangible accionable o con subtítulo/meta_description genéricos → bloquear y reescribir antes de entregar.

**Precedente fundador:** `samsung-jet-bot-steam-ultra-review` § "Antes de comprar cualquier aspirador con vapor, comprueba estas 5 cosas".
