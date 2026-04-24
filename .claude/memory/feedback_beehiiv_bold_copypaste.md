---
name: Beehiiv bold copy-paste — usar <strong>, no <span class="bold">
description: Incidente Rafael 2026-04-19. Los borradores ROBOHOGAR usaban <span class="bold"> con CSS .bold{font-weight:bold}. Al copy-paste a Beehiiv, el editor arrastra el inline style y duplica el peso (bold visible "más grueso"). Solución: usar <strong> semántico, sin class CSS.
type: feedback
originSessionId: 383a134e-9380-44b2-9a0b-a7aef3bbdef3
---
**Problema detectado 2026-04-19.** Rafael publica haciendo copy-paste desde `borrador.html` al editor rich text de Beehiiv. En los borradores ROBOHOGAR las negritas de párrafo usaban `<span class="bold">palabra</span>` con una clase CSS `.bold { font-weight: bold; }` definida en el `<style>` del borrador. Al copiar del preview del navegador (Chrome), el clipboard captura el estilo computado y Beehiiv al pegar lo traduce a `<span style="font-weight: bold">palabra</span>` inline. Beehiiv aplica entonces SU propio bold encima → peso visible "más grueso" de lo que debería. Cuando Rafael selecciona la palabra en Beehiiv y pulsa B, el editor sustituye por `<strong>` semántico limpio y el peso se normaliza — pero hacerlo palabra por palabra en un artículo de 2.000 palabras es engorroso.

**Regla dura ROBOHOGAR** (editorial.md § Formato técnico Beehiiv § Política de negritas):

1. **Usar siempre `<strong>`** para negritas de párrafo. Nunca `<span class="bold">`, nunca `style="font-weight"` inline, nunca `<b>`. HTML semántico = mapping 1:1 con el Bold nativo de Beehiiv al pegar.
2. **NO incluir `.bold { font-weight: bold; }`** en el `<style>` del borrador. Sin la clase, no hay nada que arrastre al clipboard.
3. **NUNCA bold dentro de `<h1>` `<h2>` `<h3>` `<h4>`** (el heading ya tiene `font-weight` global de Beehiiv · DM Sans Bold · cualquier `<strong>` dentro duplica peso).
4. **NUNCA bold dentro de `<thead>`** ni dentro de `<div class="checklist">` callout crema.

**How to apply** (pre-output obligatorio):
- Verificación 1: `grep -c 'class="bold"' borrador.html` → 0.
- Verificación 2: `grep -nE '<h[1-4][^>]*>[^<]{0,80}<(strong|b)\b' borrador.html` → 0 matches.
- Verificación 3: `grep -nE '<thead[^>]*>.*<(strong|b)\b' borrador.html` → 0 matches.
- Migración automática de residuales: `sed -i -E 's|<span class="bold">([^<]*)</span>|<strong>\1</strong>|g' borrador.html` + `sed -i '/\.bold { font-weight: bold;/d' borrador.html`.

**Migración aplicada 2026-04-19 a 11 archivos**: master template · 4 borradores con `class="bold"` residual (mejor-robot-aspirador-2026, humanoides-en-casa-cuanto-falta, roborock-saros-z70-review, samsung-jet-bot-steam-ultra-review) · sus 4 published equivalentes.

**Consecuencia operativa**: los artículos YA publicados en Beehiiv antes del fix siguen con el problema en la web pública. Rafael puede arreglarlos manualmente seleccionando las negritas y pulsando B en cada post (tedioso pero único camino — Beehiiv no tiene bulk-fix). Alternativa: dejarlos como están hasta el próximo re-edit. Los borradores locales y published/ en el repo SÍ están limpios tras la migración — si Rafael re-pega un post se aplicará el bold correcto.

**Referencias**:
- `@.claude/rules/editorial.md § Formato técnico (Beehiiv) § Política de negritas`
- `@.claude/commands/content-draft.md § 8.6 Formato técnico Beehiiv`
- Issue de origen: Rafael mensaje chat 2026-04-19 *"el BOLD que pones en el paragraph normal, si hago copy y paste en beehiiv sale como más bold o weight de lo que debería"*.
