---
name: Frontispicio · título corto del relato visible entre audio snippets y cuerpo
description: Canon 2026-04-27. Toda Ficción Doméstica lleva un Snippet 2.5 con eyebrow Ficciones Domésticas + título corto del frontmatter en grande + línea ámbar. Patrón Anagrama / Penguin Modern Classics.
type: feedback
---

Canon establecido por Rafael 2026-04-27 sobre el publicado de la-canguro y los 3 publicados retroactivos (la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe).

**Why:** con la adopción del formato YouTube-style canon § 5.bis (display_title largo G-family · 10-15 palabras como Title del post Beehiiv + H1 visible + OG title), el `title:` corto del relato (`La canguro`, `La objeción`, etc.) deja de tener presencia visible para el lector — solo vive en URL slug, filename del repo, `<title>` del feed RSS y registro interno. Rafael preguntó *"entonces en ningún sitio digo el título real?"* y validó la propuesta de un frontispicio interior en el post web, en la posición visual entre los snippets utilitarios de audio y el primer H2 del cuerpo del relato.

**Patrón análogo:** página título interior del libro impreso. Editorial Anagrama, Penguin Modern Classics, Fitzcarraldo Editions: cubierta exterior con hook largo de marketing, página título interior con el nombre real de la obra (centrado, sobrio, sin caja). El display_title vende y descubre; el frontispicio ancla la pieza como obra editorial.

**How to apply:**

- **Posición canon:** entre Snippet 2 (audiolibro web-only) y el primer H2 del cuerpo del relato. Para ficciones SIN audiolibro: justo antes del primer H2 del cuerpo.
- **Tipo de elemento:** `<div>` con styling tipográfico, **NO `<h2>` ni `<h1>`**. Si fuera heading SEO, Beehiiv duplicaría jerarquía con el H1 del display_title y rompería SEO.
- **Contenido del título:** literal del campo `title:` del frontmatter del relato (NO `display_title:` y NO con prefijo `🎧` — el emoji solo va al Title del post Beehiiv y al archive snippet, no aquí).
- **Eyebrow fijo:** `Ficciones Domésticas` en color ámbar `#F5A623`, font-size 11px, weight 700, letter-spacing 2px, uppercase, margin-bottom 14px.
- **Título central:** font-family DM Sans bold, size 32px, color `#0C0C0C`, line-height 1.15, letter-spacing -0.3px, margin 0.
- **Sello bajo el título:** `<div>` inline-block 36px × 2px, background ámbar `#F5A623`, margin-top 18px. Sirve como sello editorial sutil.
- **Container:** `<div>` con margin 56px arriba y 40px abajo (respira como página de libro), text-align center, font-family DM Sans default.

**Snippet canónico ROBOHOGAR (frontispicio · v1 · 2026-04-27):**

```html
<div style="margin: 56px 0 40px; padding: 0; text-align: center; font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <div style="color: #F5A623; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">Ficciones Domésticas</div>
  <div style="font-family: 'DM Sans', sans-serif; font-size: 32px; font-weight: 700; color: #0C0C0C; line-height: 1.15; margin: 0; letter-spacing: -0.3px;"><TÍTULO CORTO></div>
  <div style="display: inline-block; width: 36px; height: 2px; background: #F5A623; margin: 18px auto 0;"></div>
</div>
```

Sustituir `<TÍTULO CORTO>` por el `title:` del frontmatter (ej: `La canguro`, `La objeción`, `El operador nocturno`).

**Aplicación retroactiva 2026-04-27:**

- la-canguro (pre-publicación) — canonizado dentro del `beehiiv-paste.html` como Snippet 2.5.
- 3 publicados (la-objecion, el-operador-nocturno, el-que-viene-a-tomar-cafe) — listados en [`UPDATE-2026-04-27-titulos-y-heros.md`](../../content/ficciones/_one-shots/UPDATE-2026-04-27-titulos-y-heros.md) con paso de pegado vía `/html` → Custom HTML block → entre Snippet 2 y primer H2.

**Skills + canon afectados:**

- `.claude/commands/audiobook-generate.md § 6.4` — patrón ampliado de 7 a 8 `.snippet-block`, Snippet 2.5 documentado con plantilla.
- `content/ficciones/_one-shots/la-canguro/beehiiv-paste.html` — Snippet 2.5 ya insertado con `La canguro` literal.
- (Pendiente) `.claude/commands/ficcion-draft.md` — para ficciones sin audiolibro, asegurar que el `beehiiv-paste.html` lleva Frontispicio antes del cuerpo (Snippet 1 si no hay audio).

**Verificación pre-output (post-build de cualquier `beehiiv-paste.html` de ficción):**

```bash
# (a) El frontispicio existe
grep -c 'Frontispicio · título corto' <archivo>  # esperado: 1

# (b) El título corto literal del frontmatter aparece en el frontispicio
TITLE_CORTO=$(grep -E '^title: ' <md-fuente> | sed 's/title: "\(.*\)"/\1/')
grep -c ">${TITLE_CORTO}</div>" <archivo>  # esperado: ≥1

# (c) NO uso heading SEO (<h1>/<h2>) dentro del frontispicio (rompería jerarquía con display_title)
sed -n '/Frontispicio/,/snippet-block/p' <archivo> | grep -cE '<h[12]'  # esperado: 0
```

Si (a) = 0 → falta el frontispicio, regenerar. Si (b) = 0 → frontispicio existe pero con título incorrecto. Si (c) > 0 → bug de jerarquía SEO, corregir antes de entregar.

**Diferencia clara entre los 3 lugares donde aparece el título del relato:**

| Lugar | Qué se muestra | Ejemplo la-canguro |
|---|---|---|
| **Title del post Beehiiv (Meta A · campo Title)** | Display_title largo con prefijo 🎧 | `🎧 El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida` |
| **Frontispicio interior (Snippet 2.5)** | Título corto literal del frontmatter `title:`, sin emoji | `La canguro` |
| **Archive snippet card** | Display_title largo con prefijo 🎧 (idem Title del post) | `🎧 El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida` |

**Por qué el emoji 🎧 va en Beehiiv Title pero NO en frontispicio:** el 🎧 marca "audiolibro disponible" y vive en lugares de descubrimiento (Title del post, archive cards) donde el lector decide entrar. El frontispicio interior es navegación post-entrada — el lector ya está dentro y los snippets de audio (Snippets 1 y 2) están justo arriba: el emoji sería redundante. Pattern análogo: la portada de un audiolibro Audible lleva el icono de auriculares; la página título interior, no.
