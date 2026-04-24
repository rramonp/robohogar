---
name: Mobile-first obligatorio en copy de interfaz
description: Copy/diseño para landings/email/social/cards debe validarse mentalmente a 375px ANTES de proponer; bullets ≤40 chars, sin em-dashes en headlines
type: feedback
originSessionId: a977eacc-2dad-43a7-9ff4-a44f39625a58
---
Cuando propongo copy o diseño para landing pages, emails, posts en redes, cards o cualquier interfaz que el usuario consume en pantalla, debo pensar en MÓVIL PRIMERO, no como afterthought.

**Why:** Rafael me corrigió en sesión 2026-04-17 trabajando en la sección "¿Qué recibirás?" de robohogar.com. Le propuse 4 bullets con descripciones largas y emdashes (—) que rompían el layout en desktop y eran inviables en móvil. Su feedback literal: *"has dado textos muy largos que hacen que las cards tengan dos líneas, incluso para escritorios. Imagínate para correo o para teléfono móvil; tengo entendido que un porcentaje muy elevado de mis lectores utilizarán teléfono móvil."* Además me dijo que mi recomendación era superficial — debí cuestionar si la sección debía existir y rediseñar el layout (3-column vs 4 stacked cards), no solo cambiar texto.

**How to apply:**

Para landing pages, emails, social posts, copy de marketing, formularios, cards:

1. **Bullets/headlines máximo 40 chars** — si necesitas más, está mal estructurado. Reescribir más corto, no añadir sub-texto largo
2. **Em-dashes (`—`) prohibidos en headlines/bullets cortos** — el navegador rompe en sitios feos en móvil. Usar `:` `·` `()` o reescribir
3. **Sub-textos siempre opcionales** — el bullet primario debe entenderse sin contexto extra
4. **Validación mental obligatoria a 375px** — antes de proponer texto que vaya a interfaz, visualizarlo en pantalla móvil estrecha. Si tiene wrap raro, está mal
5. **Layouts: 3-column horizontal > 4 stacked cards** — siempre que sea posible. En móvil ambos colapsan a vertical pero el 3-up tiene jerarquía visual y menos scroll
6. **Imágenes optimizadas** — WebP <200KB email, <500KB web
7. **Cuando el usuario pide "actualiza esta sección"**: cuestionar primero si la sección debe existir, después diseñar layout, después escribir copy. NO empezar por el texto

**Excepciones:** Documentación técnica interna, planes, scripts, código, prompts de skill. NO aplica a contenido editorial largo (artículos), donde el cuerpo se lee en desktop o reader-mode con su propio formato.

**Aplica a:** ROBOHOGAR (landing Beehiiv, social posts, email broadcasts), futuros proyectos personales/profesionales con landings o newsletters, cualquier interfaz que el usuario final consume en pantalla. NO solo este proyecto.
