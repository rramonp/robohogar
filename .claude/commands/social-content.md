# Social Content — Generador de posts para redes sociales

Genera contenido para redes sociales desde artículos o newsletters de ROBOHOGAR.
Output listo para copiar/pegar en cada plataforma.

## When to activate

- "genera social", "posts sociales", "crea reels", "social media"
- "post de linkedin", "tweets", "contenido instagram"
- "whatsapp channel", "mensaje whatsapp"
- "promociona el artículo", "comparte en redes"

## Workflow

### 1. Identificar fuente

- Leer el artículo/newsletter más reciente de `content/published/` o `content/drafts/`
- Si Rafael especifica uno concreto, usar ese
- Extraer: título, hook, datos clave, opinión principal, link a Beehiiv
- **Leer flag `Evergreen`** del artículo en `content/registro-articulos.md` (o del frontmatter si es artículo nuevo):
  - `true` → generar posts normalmente + añadir cabecera `evergreen: true` al YAML del `.md` social
  - `false` → generar posts igual pero marcar cabecera `evergreen: false` + añadir nota **"⚠️ Post reactivo sobre noticia con fecha — NO reutilizar en redes después de 2026-MM-DD (fecha_publicación + 3 meses). Publicar solo en su ventana de relevancia."**

## Uso del flag en planificación

- **Pre-audiencia (<30 subs, hoy):** los posts se generan y se archivan en `content/social/` como banco. NO programar en Buffer mientras no haya presencia activa en el canal (ver regla en `rules/newsletter.md` fase pre-audiencia)
- **FASE 4B+ (con audiencia):** construir calendario social mezclando (a) 1 post del artículo nuevo de la semana + (b) 1 post evergreen del backlog de semanas previas. Los posts `evergreen: false` NO entran en el backlog de reutilización — solo se publican en su ventana de relevancia o se descartan

### 2. Generar contenido por plataforma

Aplicar tono de `rules/editorial.md`: cercano, informado, humor sutil, opiniones propias.

**Primera persona plural obligatoria** en todos los posts (ver `rules/editorial.md`).

**LinkedIn (1 post):**
```
[Hook en 1 línea — dato sorprendente o pregunta]

[3-4 párrafos cortos con el insight principal del artículo]

[Opinión personal fuerte — tomar partido]

[CTA suave: "Si te interesa la robótica doméstica, cada semana publicamos un newsletter con lo que importa."]

// Link en primer comentario, NO en el post (LinkedIn penaliza links en post)
```

**X/Twitter (3 posts):**
```
Post 1 (tweet principal):
[Dato sorprendente o hot take en <280 chars]
🤖 [hashtag relevante]

Post 2 (contexto):
[Desarrollo del punto + dato extra]

Post 3 (CTA):
[Si te interesa → link al artículo en robohogar.com]
```

**Instagram (caption para Reel o post):**
```
[Hook: primera línea que engancha — aparece antes del "más"]

[2-3 párrafos cortos con emojis relevantes]

[CTA: "¿Qué robot tienes en casa? Cuéntame 👇"]

[5-10 hashtags: #robotaspirador #roboticadomestica #robohogar #tecnologia #hogarinteligente]
```

**WhatsApp Channel (mensaje):**
```
🤖 ROBOHOGAR #XX — [Título del issue/artículo]

[Resumen en 2-3 líneas — lo esencial]

👉 Lee el artículo completo: [link a robohogar.com]
```

### 3. Ideas para Reels (si aplica)

Generar 1-2 ideas de Reel basadas en el contenido:
- Formato: "3 cosas que no sabías de [robot]" (7-15s)
- Formato: "Comparativa rápida [Robot A] vs [Robot B]" (15-30s)
- Formato: "Dato curioso sobre [tema]" (7s)
- Hook en primeros 3 segundos (60%+ hold rate target)

### 4. Output

- **Repo:** `content/social/YYYY-MM-DD-social.md`
- Formato: cada plataforma en una sección separada con copy listo para copiar

### 5. Programación recomendada

| Plataforma | Cuándo publicar | Frecuencia |
|---|---|---|
| LinkedIn | Martes/Miércoles 9:00 CET | 1/semana |
| X/Twitter | Lunes-Viernes 14:00 CET | 3-5/semana |
| Instagram Reel | Martes/Jueves 12:00 CET | 2-3/semana |
| WhatsApp Channel | Día de envío del newsletter | Semanal |

## Formato del .md

El output debe ser visualmente escaneable en Obsidian/VS Code para copiar rápido a Buffer:

- **Negrita** para datos duros (cifras, precios, scores, nombres de producto)
- *Cursiva* para matices, coloquialismos, nombres de medios, citas
- Cada plataforma con `## H2` y cada post con `### H3`
- Hashtags en bloques de código inline para distinguirlos del copy

## Rules

- NUNCA publicar automáticamente — Rafael revisa y aprueba antes
- LinkedIn: link en PRIMER COMENTARIO, no en el post (algoritmo penaliza)
- Instagram: NO reutilizar contenido con watermarks de otras plataformas
- WhatsApp: mensajes cortos, no más de 5 líneas
- Referencia `rules/editorial.md` para tono en todo el contenido
