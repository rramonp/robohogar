---
name: ROBOHOGAR archive snippet — deeplink desde URL externa NO viable en Beehiiv
description: 3 vías probadas y rechazadas para pre-filtrar el archive desde URL externa. Conclusión: filtro funciona solo con click manual; deeplinks requieren posts dedicados o migración fuera de Beehiiv.
type: feedback
---

El fichero `content/templates/beehiiv-archive-snippet.html` mantiene desde 2026-04-27 el sistema **v1 con `<input type="radio">` + `<label>` + `:checked`** para filtrar las cards. **Solo funciona por click manual del usuario en los chips, no admite deeplinks desde URL externa.** Tres alternativas se probaron y descartaron.

**Why (incidente origen 2026-04-27):**

Rafael pidió poder linkear desde otras partes (banners en artículos, CTAs en email, posts sociales) directamente al archive con un filtro de categoría pre-aplicado, ej. `/archive#ficciones` o `/archive?cat=ficciones`. Tras 3 iteraciones todas verificadas en producción con playwright, ninguna técnica CSS/HTML pura funcionó dentro del Custom HTML block de Beehiiv.

**Tres approaches probados y por qué fallan:**

1. **`<script>` que lee `?cat=<slug>` y marca `<input>.checked`.** Beehiiv strippea TODO `<script>` del Custom HTML block (sanitizer anti-XSS). Verificado: `document.querySelectorAll('script').filter(s => s.textContent.includes('rbh-f-')).length === 0` aunque el snippet pegado contenía el bloque. Los scripts no sobreviven el paste.

2. **CSS `:target` sobre anchors `<a id="<slug>">` con URLs `archive#<slug>`.** El browser no asocia los anchors con el `:target` matcher porque Beehiiv (Next.js + React Server Components — el container del Custom HTML lleva `id="_R_<hash>_"` típico de RSC) inyecta el HTML del bloque CLIENT-SIDE tras hidration. Verificación: con URL `https://robohogar.com/archive#ficciones`, `document.getElementById('ficciones').matches(':target') === false` aunque el anchor está en el DOM y es único. La regla CSS `#ficciones:target ~ ...` nunca se aplica.

3. **Forzar re-trigger de `:target` desde JS** (`window.location.hash = ''` luego `= 'ficciones'`, click manual sobre `<a href="#ficciones">`, `scrollIntoView` del anchor). Ninguno hace que `:target` matchee. Bug del matcher en SPA hydrated content — Chrome y Firefox no re-evalúan `:target` cuando elementos con `id` matching aparecen tras hidration; solo los del HTML SSR inicial.

**Conclusión operativa:**

- Filtro DENTRO del archive (click manual del usuario en chips) funciona perfectamente con `:checked` y persiste a través del hydration de React. Mantener v1.
- **Deeplink desde URL externa con CSS/HTML puro NO es viable en este Beehiiv.** Cualquier intento futuro debe partir de esta evidencia.

**Opciones para deeplinking si Rafael lo pide en el futuro:**

a) **Aceptar 1 click extra** — linkear externos a `https://robohogar.com/archive` (sin filtro) y dejar que el lector pulse el chip. Friction mínima, cero mantenimiento.

b) **Posts dedicados por categoría** — crear un post Beehiiv por cada categoría (`/p/ficciones-archivo`, `/p/aspiradores-archivo`, etc.) cuyo Custom HTML block contenga solo las cards de ESA categoría hardcodeadas. URLs bonitas, SEO mejor, sin dependencias técnicas. Coste: cada `/post-publish` debe actualizar tanto el archive central como el post de su categoría (2 snippets a re-pegar). Viable si Rafael lo prioriza.

c) **Migrar archive fuera de Beehiiv** — montar `archive.robohogar.com` o `robohogar.com/archivo` en un subdominio Cloudflare Pages con HTML estático generado por `/post-publish`. Sin sanitizer, scripts y `:target` funcionan nativamente. Pendiente F2+ cuando Rafael decida si el archive merece infra propia.

**Hallazgos permanentes Beehiiv (aplican más allá de este snippet):**

- Beehiiv Custom HTML blocks **strippean `<script>`** (todas las páginas: archive, posts, landings).
- Beehiiv (Next.js + RSC) **rompe `:target` para elementos inyectados client-side**. Cualquier técnica CSS-only que dependa de URL fragments para filtrar/togglear no es fiable.
- Lo que SÍ funciona en Custom HTML de Beehiiv: estructura HTML+CSS estática (cards, banners, CTAs), `:checked` con `<input>` + `<label>` para tabs/accordions/filtros con click humano, `:hover` para tooltips/dropdowns, `<details>`/`<summary>` para colapsables, iframes whitelist (Twitter/YouTube/Spotify), CSS `:has()` y `@media`.
- iFrames de redirect/`<meta refresh>` también se strippean en posts standard.

**Regla operativa para `/post-publish § 5.7`:** la lógica de inserción de cards al inicio del grid no cambia. Mantener el comentario de cabecera "DEEPLINK DESDE URL EXTERNA — NO ES VIABLE EN BEEHIIV" como advertencia perenne para no volver a perder horas con esto.

Verificación pre-entrega del snippet:

```bash
# (a) v1 limpia: 5 inputs radios + 5 labels chip + 0 :target en CSS + 0 <script>
grep -cE 'input type="radio"' content/templates/beehiiv-archive-snippet.html  # esperado: ≥5
grep -cE '<label class="rbh-arc-chip' content/templates/beehiiv-archive-snippet.html  # esperado: 5
grep -cE '^\s*#[a-z-]+:target' content/templates/beehiiv-archive-snippet.html  # esperado: 0 (en CSS, no comments)
grep -cE '^\s*<script' content/templates/beehiiv-archive-snippet.html  # esperado: 0

# (b) Comentario de advertencia presente
grep -c "DEEPLINK DESDE URL EXTERNA — NO ES VIABLE" content/templates/beehiiv-archive-snippet.html  # esperado: 1
```

Si (a) no devuelve los valores esperados → restos de v2 fallido, restaurar v1 antes de entregar. Si (b) devuelve 0 → falta el aviso, restaurar.
