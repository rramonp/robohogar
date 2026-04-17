# Ficciones Domésticas — Pilar narrativo ROBOHOGAR

Relatos cortos de ciencia ficción doméstica próxima (2030-2040) ambientados en hogares españoles. Personajes recurrentes, continuidad inter-episodio, y un pie anclado siempre en datos reales (AI Act, INE, specs de robots que ya existen). **~10% del content mix**, compatible con la línea editorial principal de reviews y análisis.

La idea: que el lector pase de "qué robot compro" (artículos) a "qué pasará en esta casa dentro de 8 años" (ficciones). Dos puertas distintas al mismo universo.

---

## Estructura de carpetas

Una carpeta por mini-serie. Cada mini-serie es un arco cerrado con inicio/final claros, personajes consistentes y su propia biblia.

```
content/ficciones/
├── README.md                         ← este archivo
├── _template-character-bible.md      ← plantilla rellenable (copiar a cada serie)
├── _template-arco-serie.md           ← plantilla de arco
│
├── <slug-serie-1>/                   ← ej: familia-cortes/
│   ├── character-bible.md            ← fichas de personajes + canon
│   ├── arco-serie.md                 ← premisa, tema, episodios planeados
│   ├── YYYY-MM-DD-<slug>.md          ← episodio (Markdown con frontmatter)
│   ├── YYYY-MM-DD-<slug>.html        ← versión Beehiiv (tras edición)
│   ├── PASOS.md                      ← checklist publicación de ese episodio
│   └── assets/
│       └── hero-<slug>.png           ← still cinematográfico (opcional)
│
├── <slug-serie-2>/                   ← ej: vecino-analogico/
│   └── ...
│
└── flash/                            ← flash fictions no adscritas a serie
    └── YYYY-MM-DD-<slug>.md
```

**Ejemplos de slugs de serie** (placeholders — Rafael decide):
- `familia-cortes` — familia en Madrid con aspirador IA (Tico) y humanoide (Eva)
- `vecino-analogico` — señor mayor que rechaza la IA doméstica
- `cuidados-2035` — humanoides de cuidados para mayores solos

No hay ninguna serie canon todavía. Los nombres anteriores son ejemplos ilustrativos, no universo establecido.

## Convenciones de naming

| Tipo | Patrón | Ejemplo |
|---|---|---|
| Slug de serie | `kebab-case`, max 25 chars | `familia-cortes` |
| Archivo de episodio | `YYYY-MM-DD-<slug-episodio>.md` | `2026-05-01-ocho-pasos.md` |
| Slug de episodio | `kebab-case`, max 40 chars | `ocho-pasos` |
| Hero image | `hero-<slug-episodio>.png` | `hero-ocho-pasos.png` |
| Flash fiction (sin serie) | ir a `content/ficciones/flash/` | `2026-05-15-la-taza-despintada.md` |

## Qué debe contener cada carpeta de serie

### `character-bible.md` (obligatorio)
Fichas de todos los personajes recurrentes + sección "Canon establecido" (facts inmutables del universo) + "Episodios publicados" (log cronológico) + "Arcos pendientes". Ver plantilla: `_template-character-bible.md`.

### `arco-serie.md` (obligatorio si ≥2 episodios)
Premisa de la serie en 1 frase, tema (qué problema humano real explora), arco emocional global, lista de episodios planeados, cliffhanger entre episodios. Ver plantilla: `_template-arco-serie.md`.

### Episodios
Un archivo `.md` por episodio con frontmatter YAML completo (ver `/ficcion-draft` paso "Output"). La versión `.html` se genera al publicar en Beehiiv.

## Flujo de trabajo

```
0. /research-digest (semanal o bajo demanda)
   → Extrae Top/Notable stories de robótica
   → Genera "Semillas narrativas" en output del digest
   → Alimenta el "Backlog Ficciones Domésticas" en calendario-editorial.md
   → Aporta datos reales anclables (AI Act, INE, specs) que reutilizará el relato
         ↓
1. Rafael elige semilla (del backlog) o propone una nueva
         ↓
2. /ficcion-draft {semilla?, personajes, longitud}
   [paso 0 del skill] → si falta semilla o dato real, lee backlog + último digest
         ↓
3. Skill carga character-bible + arco-serie
         ↓
4. Paint The Villain → validar villano humano (no el robot)
         ↓
5. Pixar Spine o 5-Sentence → outline
         ↓
6. Expansión a prosa con MRUs
         ↓
7. Character Voice Checker → validar continuidad
         ↓
8. Output: borrador .md + PASOS.md (+ hero opcional)
         ↓
9. Rafael edita → publica en Beehiiv (tag "Ficciones Domésticas")
         ↓
10. /post-publish: actualizar character-bible "Episodios publicados" + mover
    episodio a published + registros + /social-content para anuncio en redes
```

**Integración con `/research-digest`:** el digest semanal genera 2-4 semillas narrativas por ejecución, que van automáticamente al "Backlog Ficciones Domésticas" en `calendario-editorial.md`. Así Rafael siempre tiene un banco de semillas ancladas a actualidad real cuando invoca `/ficcion-draft`. Si el backlog está poblado, Rafael puede llamar `/ficcion-draft longitud=flash personajes="Tico, abuela Cortés"` sin pasar semilla — el skill leerá el backlog y propondrá las 3 más relevantes.

**Cadencia**: 1 relato cada 3-4 semanas. No cada semana — la ficción se cansa antes que el análisis.

**Primer episodio de una serie nueva**: obligatorio rellenar `character-bible.md` Y `arco-serie.md` antes de invocar `/ficcion-draft`. El skill se negará a escribir sobre bible vacía sin autorización explícita.

## Longitudes disponibles

| Formato | Palabras | Lectura | Uso |
|---|---|---|---|
| **Flash fiction** | 500-1.000 | 2-4 min | Sección rotativa en newsletter / piloto de universo |
| **Relato corto** | 1.500-3.000 | 6-12 min | Publicación standalone (cada 3-4 semanas) |
| **Mini-serie (episodio)** | 1.500-3.000 | 6-12 min | Arco de 6-12 episodios con inicio/final cerrados |

Piloto recomendado antes de comprometerse a mini-serie: 3 flash fictions de 800 palabras en 3 newsletters consecutivas. Si engagement sube >10% → comprometer mini-serie. Si neutral → mantener rotativa. Si negativo → archivar.

## Voz y reglas editoriales

La ficción **relaja explícitamente** la regla de "primera persona plural" del resto de ROBOHOGAR. En ficción:
- Narrador **omnisciente** (3ª persona) **O** **primera persona del personaje POV**
- Tiempo verbal consistente por escena (presente para inmediatez, pasado para reflexión)
- Anclar siempre en ≥1 dato real (AI Act, INE, spec técnica)
- El villano es el problema humano que el robot revela — nunca el robot

Ver detalle completo en `@.claude/rules/editorial.md` sección "Narrativa especulativa — Ficciones Domésticas".

## Enlaces

- Skill principal: `@.claude/commands/ficcion-draft.md`
- Skill que alimenta el backlog: `@.claude/commands/research-digest.md` (paso 5 + 8b)
- Skill de cierre: `@.claude/commands/post-publish.md`
- Knowledge base: `@references/writewithai/07-ficcion-y-narrativa-serializada.md`
- Calendario editorial (slot + backlog): `@content/calendario-editorial.md`
- Estilo de hero: `@assets/branding/asset-catalog.md` → sección "Heros ficción"

<!-- created by wwai-integration 2026-04-17 -->
