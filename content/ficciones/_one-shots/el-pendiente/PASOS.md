# PASOS — El pendiente

**Estado:** borrador validado (anti-IA + anti-calco ES + Capa 2 LLM = READY).
**Generado:** 2026-04-25 vía `/ficcion-draft one-shot flash 600-800` (categoría tonal: mundano).
**Audiolibro:** sin generar (decisión Rafael 2026-04-25 — reproducirlo en ElevenLabs Reader desde Obsidian Mobile).

## Metadata SEO (copy-paste a Beehiiv)

| Campo | Valor |
|---|---|
| Title | El pendiente |
| SEO Title | El pendiente · Ficciones Domésticas |
| Subtitle | Pilar lleva ocho meses sola con su aspirador. Una noche el robot le devuelve algo que su madre perdió antes de morir. |
| Slug | `el-pendiente` |
| Tag Beehiiv | Opinión |
| Tag visual | Ficciones Domésticas |
| Categoría tonal | mundano |
| Hero | pendiente (sin generar; usar fallback monograma R sobre fondo ámbar claro o invocar `/nano-banana` con código visual del relato) |

## Verificaciones aprobadas

- [x] Longitud flash: 670 palabras (audiolibro.txt) · 750 con frontmatter (.md). Dentro de rango 500-800.
- [x] Anti-calco ES Capa 1 (22 greps): 0 matches.
- [x] Anti-calco ES Capa 2 (LLM Agent Explore): READY con 1 fix aplicado (`cámara hacia los álbumes` → `Su cámara no llega a los álbumes`).
- [x] Categoría tonal mundano: cierre descriptivo plano, ≥1 detalle especulativo (papelera ML "cosas pequeñas que parecen importantes").
- [x] Anclaje técnico: 3+ menciones de "aspirador" por sección.
- [x] Sin marcas comerciales reales en narrador (las del frontmatter `dato-real` son metadata interna).
- [x] Subtítulos descriptivos en cada `<h2>`: I. La rutina · II. El pendiente · III. El suelo.
- [x] `left-wall` + `big-lie` declarados en frontmatter Y bloque visible bajo H1.
- [x] Villano humano: el duelo no procesado, no el aspirador.
- [x] POV consistente (3ª cercana Pilar) + tiempo presente coherente.

## Hero pendiente (cuando se quiera publicar)

Código visual sugerido: **domestic warm minimalista** — Pilar (50, contención emocional) + aspirador robot (Tico) en cocina española de Carabanchel. Luz nocturna ámbar de una sola lámpara. Pendiente de perla en mano (foreground), aspirador en background con luz amarilla pulsando. Paleta: marrones cálidos + ámbar puntual. Referencias: After Yang (interior cálido) + Aki Kaurismäki (luz lateral cinematográfica).

Prompt para `/nano-banana` cuando llegue el momento:

```
Domestic warm minimalist still, Madrid 2033 working-class kitchen at 21:30. Spanish woman 50s seated on wooden floor, holding small pearl earring in cupped hand, looking down at it with quiet recognition (no tears, contained emotion). Foreground: small earring catching warm light. Mid-ground: domestic robot vacuum with single soft yellow LED on top, paused at her feet. Background: kitchen with white tile, ceramic dish on entrance shelf, blurred. Single warm amber light source from kitchen ceiling lamp (motivated, not ambient). Palette: deep browns, cream, single amber accent. Cinematic 35mm grain, shallow depth. References: After Yang interior warmth + Aki Kaurismäki side-light + Wong Kar-wai contemplative still. No text, no letters, no Asian characters, no windows to exterior, no decorative LEDs.
```

## Checklist publicación (si se decide publicar)

- [ ] Decidir si publicar este one-shot (relato ad-hoc; no obligatorio del calendario).
- [ ] Si sí: generar hero v1-v3 con `/nano-banana`.
- [ ] Crear borrador HTML Beehiiv desde el `.md` (recibir formato H1/H2 + bloque callout left-wall/big-lie + 3 secciones).
- [ ] Pegar en Beehiiv como `Web only` o `Email and web` según fase newsletter.
- [ ] Tras publicar: `/post-publish <URL>` (12 pasos del skill).

## Audiolibro (si Rafael lo pide más adelante)

- Texto fuente para TTS: `audiolibro.txt` (ya generado, listo para `/audiobook-generate el-pendiente`).
- Coste estimado ElevenLabs: ~$0.40 (4.000 chars · voz Luis Multilingual v2).
- Duración estimada: ~5-6 min.
- Si se genera: encadenar luego `/audiobook-distribute el-pendiente` (auto-fire desde `/post-publish § 13.5`).

## Hooks para futuros relatos (opcional)

- **Pilar como personaje recurrente:** podría ser semilla de mini-serie sobre duelo + tecnología doméstica (3-4 episodios espaciados, marzo a diciembre). Cada episodio sería un objeto que el aspirador encuentra, una capa nueva del luto.
- **La papelera "cosas que parecen importantes":** detalle especulativo reusable como motor de relato. Otra premisa: lo que el aspirador clasifica como "importante" no coincide con lo que el usuario considera importante. Conflicto humano = la frontera entre objeto y memoria.
