# Editorial ES — Knowledge base de prosa no-ficción ROBOHOGAR

Referentes peninsulares (80%) + LATAM dosificado (20%) de periodismo tech, columnismo, newsletter y copy editorial ES, con muestras textuales reales verificables. Destilado operativo para que los skills generadores (`/content-draft`, `/social-content`) produzcan prosa con voz personal ES, no LLM traducido del inglés.

## Archivos

| Archivo | Ámbito | Skill que lo carga | Densidad |
|---|---|---|---|
| [`01-articulos-y-columnas.md`](01-articulos-y-columnas.md) | Artículos largos (reviews, comparativas, guías, editoriales) + columnas de opinión | `/content-draft` paso 8.5 | ~2.000 palabras |
| [`02-newsletter-y-emails.md`](02-newsletter-y-emails.md) | **Eje central — voz personal.** Newsletter semanal, welcome emails, secuencias automatizadas | `/content-draft` paso 8.5 (si hay newsletter issue) + emails welcome flow manuales | ~2.800 palabras |
| [`03-microcopy-ctas-meta.md`](03-microcopy-ctas-meta.md) | Banners de lead magnet, CTAs, trust-lines, subject lines, OG/meta descriptions | `/content-draft` paso 8.8 + `/pdf-brand` paso 6 (validator cruzado) | ~1.500 palabras |
| [`04-social-posts.md`](04-social-posts.md) | LinkedIn, X, Instagram, WhatsApp | `/social-content` paso 2 | ~1.000 palabras |

## Qué cubre este KB y qué NO

**Cubre:**
- Referentes ES+LATAM concretos con 1-3 muestras textuales reales (URL verificable) cada uno.
- Patrones transversales que un LLM por defecto NO produce sin instrucción explícita.
- Checklist pre-output operativa por formato.
- Cómo construir el "toque personal" del newsletter ES de éxito en copy, emails y artículos.

**NO cubre (consultar archivo indicado):**
- Tics universales anti-IA (palabras prohibidas, tricolon mecánico, em-dashes en cascada) → [`../anti-ia-checklist.md §1 Universal`](../anti-ia-checklist.md).
- Prosa narrativa de ficción → [`../ficciones/castellano-literario-es.md`](../ficciones/castellano-literario-es.md).
- Voz baseline ROBOHOGAR (1ª persona plural, tú al lector, NO usted/vosotros, sin saludos anglo, anti-anglicismos) → [`../../.claude/rules/editorial.md`](../../.claude/rules/editorial.md) + [`../../docs/brand-voice.md`](../../docs/brand-voice.md).
- Auditoría previa de subject/opener/sign-off en 20 newsletters ES → [`../research-newsletters-es-2026-04-19.md`](../research-newsletters-es-2026-04-19.md) (este KB amplía con cuerpo editorial y aplicación, no duplica la auditoría).
- Mecánicas de email (deliverability, GDPR, timing) → [`../../.claude/rules/newsletter.md`](../../.claude/rules/newsletter.md).
- Reglas microcopy de conversión (trust-lines canónicas, patrones prohibidos con regex) → [`../../.claude/rules/tangibles.md § Microcopy de conversión`](../../.claude/rules/tangibles.md).

## Fuentes del research (2026-04-19)

Notas de research completas con 76 citas literales verificables:
- [`../../content/drafts/2026-04-19-research-editorial-es-newsletters.md`](../../content/drafts/2026-04-19-research-editorial-es-newsletters.md) — 9 newsletters ES con ~22 citas.
- [`../../content/drafts/2026-04-19-research-editorial-es-columnistas.md`](../../content/drafts/2026-04-19-research-editorial-es-columnistas.md) — 7 columnistas ES+LATAM con 11+ citas.
- [`../../content/drafts/2026-04-19-research-editorial-es-periodismo-y-copy.md`](../../content/drafts/2026-04-19-research-editorial-es-periodismo-y-copy.md) — 7 periodistas tech + 6 marcas con 43 citas.

## Patrón estructural

Cada archivo sigue el mismo patrón que [`../ficciones/castellano-literario-es.md`](../ficciones/castellano-literario-es.md):

1. §1-§2 Referentes con muestras textuales (URL + 2 citas + patrón + aplicación ROBOHOGAR)
2. §3+ Patrones transversales destilados y calcos EN→ES específicos del registro
3. §N Checklist operativa pre-output con flags automatizables (grep patterns) cuando aplica

Verificación: cada archivo termina con una sección `## Checklist pre-output`. Si algún skill carga un archivo sin ejecutar esa checklist, falla la disciplina.
