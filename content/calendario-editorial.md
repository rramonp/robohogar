# Calendario Editorial — ROBOHOGAR

> Consultar antes de elegir temas. Actualizar tras cada publicación.

---

## Cadencia (fase 0-100 suscriptores)

| Qué | Frecuencia | Publish to | Prioridad |
|-----|-----------|-----------|-----------|
| **Artículo web** | ~1/semana (objetivo) | `Email and web` | Alta — genera SEO y trae suscriptores |
| **Ficciones Domésticas** | 1 cada 3-4 semanas | `Email and web` (tag: Ficciones Domésticas) | Media — pilar experimental ~10% del mix |
| **Newsletter** | Activar cuando haya 30-50 suscriptores | `Email only` | Baja hasta tener audiencia |
| **Research digest** | Bajo demanda (antes de escribir) | No se publica | Ejecutar si no hay digest reciente |

**Flujo:** digest (si falta) → artículo → publicar → post-publish. Sin día fijo — cuando Rafael tenga tiempo.

### Slot Ficciones Domésticas

Relatos cortos de ciencia ficción doméstica (2030-2040) con personajes recurrentes. Pilar experimental, cadencia separada del artículo semanal.

- **Cadencia objetivo:** 1 relato cada 3-4 semanas (no cada semana — la ficción satura más rápido)
- **Formato:** flash 500-1.000 · relato corto 1.500-3.000 · mini-serie por episodios
- **Skill:** `/ficcion-draft {semilla, personajes, longitud}`
- **Output:** `content/ficciones/<serie>/YYYY-MM-DD-<slug>.md` + PASOS.md
- **Publicación en Beehiiv:** `Email and web` con tag dedicado "Ficciones Domésticas"
- **Piloto recomendado antes de mini-serie:** 3 flash fictions de 800 palabras en 3 semanas consecutivas. Si engagement sube >10% → comprometer mini-serie. Si neutral → mantener rotativa. Si negativo → archivar.
- Fechas concretas: Rafael las decide. El slot está reservado en el calendario, no programado.
- Detalle: `@content/ficciones/README.md` · Voz: `@.claude/rules/editorial.md` § Narrativa especulativa

---

## Backlog de temas

> Temas candidatos para artículos futuros. Priorizar por SEO + viralidad + actualidad.
> `/research-digest` añade temas aquí automáticamente con señal de viralidad.
> 🔥 = poco debate / 🔥🔥 = varios medios + foros / 🔥🔥🔥 = cobertura masiva + mainstream

| Prioridad | Tema | Tipo | Keyword SEO | 🔥 | Notas |
|-----------|------|------|-------------|---|-------|
| ~~Alta~~ | ~~Roborock Saros Z70: review del brazo robot~~ | ~~Review~~ | ~~roborock saros z70 review~~ | ~~🔥🔥🔥~~ | ✅ Publicado 2026-04-16 |
| Alta | Robots aspirador que suben escaleras (3 enfoques) | Editorial | robot aspirador escaleras | 🔥🔥🔥 | Saros Rover + Dreame Cyber X + eufy MarsWalker |
| Alta | Humanoides domésticos 2026: los 5 que puedes comprar | Comparativa | robot humanoide comprar 2026 | 🔥🔥🔥 | NEO, R1, Memo, Onero H1, Panther |
| Alta | Sunday Memo: el anti-humanoide de $1.150M | Editorial | sunday robotics memo | 🔥🔥🔥 | Bloomberg+TechCrunch. Ruedas>piernas |
| Alta | Apple entra en robótica doméstica | Editorial | apple home robot 2026 | 🔥🔥🔥 | Hub 2026, robot 2027. Mainstream masivo |
| Alta | Mejor robot aspirador 2026 | Review/Comparativa | robot aspirador | 🔥🔥 | Evergreen, alto volumen SEO |
| Alta | Robot cortacésped: guía de compra | Guía | robot cortacésped | 🔥🔥 | Temporada primavera/verano |
| Media | MOVA V70 Ultra: submarca de Dreame llega a España | Review | mova v70 ultra | 🔥🔥 | 1.399€ mayo 2026, 40.000 Pa |
| Media | SwitchBot Onero H1: humanoide por <$10K | Review | switchbot onero h1 | 🔥🔥 | El más barato y práctico |
| Media | Roborock: "humanoides no son eficientes para casa" | Editorial | robot humanoide hogar | 🔥🔥 | Entrevista española, contrapunto |
| Media | Roborock cortacéspedes: RockMow X1 LiDAR | Review | roborock cortacésped | 🔥🔥 | AWD, sin cables, IA. España 2026 |
| Media | Ecovacs LilMilo: tu marca de aspiradores vende un perro | Editorial | ecovacs lilmilo robot mascota | 🔥🔥 | TechRadar "me hizo llorar" |
| Media | Dreame vs Roborock vs Ecovacs: guerra 2026 | Comparativa | dreame vs roborock 2026 | 🔥🔥 | Datos frescos digest 2026-04-16 |
| Baja | Xiaomi Miloco: tu casa se convierte en robot | Editorial | xiaomi hogar inteligente ia | 🔥 | MWC 2026, concepto no producto |
| Baja | Historia de la robótica doméstica | Editorial | robótica doméstica | 🔥 | Pilar SEO |

---

## Backlog Ficciones Domésticas

> Semillas narrativas candidatas para relatos futuros. Rafael elige cuándo y en qué serie encajan.
> `/research-digest` añade semillas aquí automáticamente (paso 8b del skill) extrayendo tensión narrativa de las noticias reales. `/ficcion-draft` las consume (paso 0 del skill).
> Placeholders — ninguna es canon hasta que se publica el episodio.

| Prioridad | Semilla de trabajo | Formato | Serie sugerida | Tema humano | Dato real ancla | Notas |
|-----------|--------------------|---------|----------------|-------------|-----------------|-------|
| — | _(pendiente — `/research-digest` rellenará tras primera ejecución post-integración)_ | | | | | |

## Temas usados (no repetir)

| Fecha | Tipo | Tema | Slug |
|-------|------|------|------|
| 2026-04-14 | Review/Comparativa | Robots de escritorio con IA | mejor-robot-asistente-ia-2026 |
| 2026-04-15 | Editorial/Opinión | Humanoides en casa | humanoides-en-casa-cuanto-falta |
| 2026-04-16 | Editorial/Opinión | Roborock Saros Z70 brazo mecánico | roborock-saros-z70-review |
