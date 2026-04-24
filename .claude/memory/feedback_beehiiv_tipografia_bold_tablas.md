---
name: Formato técnico Beehiiv — tipografía + bold + copy-paste + tablas mobile
description: Config tipográfica global Beehiiv (DM Sans Bold headings + Inter Regular body) · política de negritas (dónde sí / dónde no) · bug copy-paste obliga a usar <strong> NUNCA <span class="bold"> · tablas mobile-first (máx 4 cols, cells ≤25 chars).
type: feedback
---

Memoria maestra de formato técnico Beehiiv para ROBOHOGAR. Consolida tipografía, política de negritas, bug de copy-paste y reglas de tablas mobile-first. Incidentes de origen al final.

## 1. Config tipográfica global

- **Headings H1/H2/H3/H4:** DM Sans · **Bold** (aplicado como global setting en el admin de Beehiiv).
- **Body / párrafo:** Inter · Regular.
- La config vive en Beehiiv admin, no en los borradores. Los borradores generan Markdown/HTML semántico plano y Beehiiv aplica el estilo al renderizar.

## 2. Política de negritas — DÓNDE SÍ / DÓNDE NO

**✅ SÍ** (bold cuando aporta énfasis):
- Párrafos de texto corrido (intro, desarrollo, callout simple, nota al pie).
- Listas/bullets de prosa dentro de párrafos.

**❌ NO** (aunque la fuente lo permita):
- **Headings H1/H2/H3/H4** — Beehiiv ya aplica DM Sans Bold global; cualquier `<strong>` / `<b>` / `** **` dentro duplica peso visible.
- **`<thead>` de tablas** — Beehiiv estiliza el header con su propio font-weight. En `<tbody>`: solo la col 1 (ancla de escaneo móvil) puede ir en `<strong>`; col 2+ siempre regular.
- **Callouts `.checklist`** (fondo crema `#FFF9EF` + borde `#F5A623`) — items en peso regular, nunca `<li><strong>`.

## 3. Bug copy-paste — SIEMPRE `<strong>`, NUNCA `<span class="bold">`

**Problema técnico.** Los borradores ROBOHOGAR usaron durante un tiempo `<span class="bold">palabra</span>` con CSS `.bold { font-weight: bold; }` en el `<style>` del borrador. Al hacer copy-paste desde el preview de Chrome al editor rich-text de Beehiiv, el clipboard captura el estilo **computado** y lo traduce a `<span style="font-weight: bold">` inline. Beehiiv aplica entonces SU propio bold encima → **doble peso visible** (bold visiblemente más grueso que el bold normal). Cuando Rafael selecciona la palabra y pulsa B en Beehiiv, el editor sustituye por `<strong>` semántico y el peso se normaliza — pero hacerlo palabra a palabra en un artículo de 2.000 palabras es engorroso.

**Regla dura:**

1. Usar SIEMPRE `<strong>` para negritas de párrafo. Nunca `<span class="bold">`, nunca `style="font-weight"` inline, nunca `<b>`. HTML semántico mapea 1:1 con el Bold nativo de Beehiiv al pegar.
2. NO incluir `.bold { font-weight: bold; }` en el `<style>` del borrador. Sin la clase, no hay nada que arrastre al clipboard.
3. Migración automática de residuales:
   ```bash
   sed -i -E 's|<span class="bold">([^<]*)</span>|<strong>\1</strong>|g' borrador.html
   sed -i '/\.bold { font-weight: bold;/d' borrador.html
   ```

**Verificación pre-output (cada grep debe devolver 0):**

```bash
grep -c 'class="bold"' borrador.html                                       # (a)
grep -nE '<h[1-4][^>]*>[^<]{0,80}<(strong|b)\b' borrador.html              # (b)
grep -nE '<thead[^>]*>.*<(strong|b)\b' borrador.html                       # (c)
grep -nE 'class="checklist"[^>]*>.*<(strong|b)\b' borrador.html            # (d)
grep -nE '^#{1,4} .*\*\*' borrador.html                                    # (e) Markdown equivalent
```

**Migración aplicada 2026-04-19 a 11 archivos:** master template · 4 borradores con `class="bold"` residual (mejor-robot-aspirador-2026 · humanoides-en-casa-cuanto-falta · roborock-saros-z70-review · samsung-jet-bot-steam-ultra-review) · sus 4 published/ equivalentes. Posts ya publicados en Beehiiv antes del fix siguen con el problema en la web pública; Rafael los arregla manualmente (select + B) si los re-edita.

## 4. Tablas — mobile-first (≥50% lectores en móvil · 80% según tráfico real 2026)

- **Máximo 4 columnas.** Si comparativa pide más: (a) recortar a las 4 más críticas y el resto en prosa, o (b) partir en 2 tablas temáticas.
- **Texto corto por celda (≤25 chars orientativo · 2-3 palabras).** Sin paréntesis largos, sin disclaimers en celda — eso al caption o al cuerpo.
- **Nombres de producto cortos:** marca + modelo en 2-3 palabras ("Ecovacs X8 Pro Omni", no "Ecovacs Deebot X8 Pro Omni"). Año entre paréntesis en `<em>` con `<br>` si es imprescindible.
- **Unidades pegadas sin espacio:** `100°C`, `1.399€` (ayuda a evitar wrap feo en 375px).
- **Sin specs secundarias en celdas** (potencias, dimensiones, sensores, disclaimers). Van en prosa.
- **Referencia que renderiza bien:** tabla de `content/articulos/mejor-robot-asistente-ia-2026/borrador.html` (4 cols, cells cortas, OK en 375px).
- **Fallo real documentado:** tabla original de `content/articulos/samsung-jet-bot-steam-ultra-review/borrador.html` tenía 7 columnas con cells largas → ilegible en 375px (abril 2026). Corregida a 4 cols.

## 5. Referencias cruzadas

- `@.claude/rules/editorial.md § Formato técnico (Beehiiv) · Política de negritas · Formato técnico Beehiiv (tablas)`
- `@.claude/rules/design.md § Mobile-first`
- `@.claude/commands/content-draft.md § 8.6 Formato técnico Beehiiv`

## 6. Nota de consistencia con design.md

`rules/design.md` menciona **Jost + DM Sans** como fuentes de referencia para **assets propios** (landing, social cards, PDFs). Eso aplica a diseño de assets. El newsletter/web en Beehiiv usa **DM Sans + Inter** (sección 1). Son stacks distintos y compatibles — no duplicados.

## 7. Incidentes de origen

- **2026-04-19 (a) · bug copy-paste bold.** Rafael mensaje chat: *"el BOLD que pones en el paragraph normal, si hago copy y paste en beehiiv sale como más bold o weight de lo que debería"*. Investigación identificó el arrastre de CSS computado por Chrome → inline style → doble peso en Beehiiv. Regla `<strong>` canonizada y migración automática aplicada.
- **2026-04-19 (b) · tabla de 7 cols ilegible en móvil.** Tabla original de *Samsung Jet Bot Steam Ultra Review* renderizaba bien en desktop pero se desbordaba en viewport 375px. Regla dura ≤4 cols canonizada y aplicada a la versión publicada.
- **2026-04 (c) · bold en headings.** Rafael detectó que artículos con `## **Título**` Markdown producían H2 con peso visiblemente más pesado que el global DM Sans Bold. Regla dura "bold NUNCA en headings" canonizada.
