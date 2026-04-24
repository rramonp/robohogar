---
name: Byline ROBOHOGAR — sin "Rafael de" en snippets Beehiiv
description: Desde 2026-04-24 el byline de todos los artículos en Beehiiv es "ROBOHOGAR" (todo mayúsculas), sin "Rafael de" delante. Aplica a archive snippets, cards de artículo, social y cualquier output al lector. El avatar-icon se mantiene.
type: feedback
originSessionId: 7a46d40c-fa61-4722-9cd1-c0d5e5642bda
---
Desde 2026-04-24 Rafael cambió el nombre de autor en Beehiiv de "Rafael de ROBOHOGAR" a "ROBOHOGAR" (todo mayúsculas). La foto/icon del autor se mantiene (`profile-icon-1080x1080.png`, mismo user-id `864dc8b9-fd48-414a-ac12-0b53cb770fe9`).

**Why:** decisión editorial — la marca es el medio, no la persona. Consistente con la regla `rules/tangibles.md § Ninguna promesa futura ni byline personal dentro del PDF tangible` (tangibles ya firmaban solo "ROBOHOGAR"). Ahora se extiende a artículos y archive.

**How to apply:**
- Cualquier `<span>...</span>` de byline en snippets Beehiiv (archive snippet, card de artículo, cualquier Custom HTML block futuro) → `<span>ROBOHOGAR</span>`, nunca `Rafael de ROBOHOGAR`.
- El avatar circular 22px (URL Beehiiv `profile-icon-1080x1080.png`) se mantiene igual — solo cambia el texto al lado.
- Aplica al skill `/post-publish` paso 5.7(c) — ya actualizado el template del card en `.claude/commands/post-publish.md`.
- Aplica al template `content/templates/beehiiv-archive-snippet.html` — ya actualizado.
- **NO tocar históricos en bulk** salvo que Rafael lo pida. Hay ~39 archivos con "Rafael de ROBOHOGAR" (borradores antiguos, HTMLs publicados, docs, lead magnets, validators.py, memoria `feedback_tangible_no_promises_no_byline.md`). Solo se han actualizado los 3 snippets Beehiiv activos + template + post-publish. El resto se migra a demanda cuando Rafael lo invoque o cuando se regenere el output.
- **Excepción única:** la bio "Sobre el autor" de Rafael puede seguir en singular con su nombre — es su página personal dentro del medio, no el byline del post.

**Incidente origen:** 2026-04-24, Rafael al revisar el archive snippet post `/la-objecion` v8 pidió cambio del byline en todos los artículos del archive y pidió documentarlo como regla persistente para próximos snippets.
