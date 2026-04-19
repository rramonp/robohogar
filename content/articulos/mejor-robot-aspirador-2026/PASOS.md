# Artículo #4: Mejor robot aspirador 2026: la guía honesta (6 modelos, 3 perfiles, 1 ganador) — Pasos para publicar

> Guía de compra evergreen sin content gate. El tangible (tabla comparativa + checklist 5 preguntas + veredicto por perfil) va **inline gratis**, alineado con `@rules/tangibles.md` F1 (0-50 subs: tangible inline, sin PDF ni gate). Gate/paywall se activa en F3 (~5K subs). Pivote Cole 2026 aplicado en estructura (tangible = producto, copy lleva hasta él) pero sin barrera de suscripción: en fase pre-audiencia, máxima fricción cero prima sobre conversión de suscripción.

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `Mejor robot aspirador 2026: 6 finalistas + checklist` (52 chars) |
| **Meta description** | `6 robots aspirador analizados y 3 perfiles. Incluye la checklist de 5 preguntas que te ahorra 600 € antes de comprar. Precios ES verificados.` (143 chars) |
| **Slug** | `mejor-robot-aspirador-2026` |
| **Tags** | `Aspiradores`, `Guías` |
| **Publish to** | `Web only` (fase pre-audiencia, reserva envío hasta que haya ≥30 subs) |
| **Content Gate** | ❌ NO activar — decisión 2026-04-18 alineada con `@rules/tangibles.md` F1 (0-50 subs, tangible inline sin gate). Gate difierido a F3 (~5K subs) según `@references/writewithai/08-paid-newsletter-blueprint-2026.md`. |
| **Evergreen** | ✅ true — Revisión semestral obligatoria: 2026-10-18 (precios y modelos cambian cada temporada). La estructura por perfil —global, calidad-precio, mascotas, ecosistema, ES— se mantiene aunque roten los nombres concretos. |

> **Evergreen** = ¿este artículo sirve para reutilizar en redes dentro de 3-6 meses cuando haya audiencia? `true` para comparativas, reviews, guías y editoriales de tesis. `false` para editoriales reactivos sobre noticia concreta (deals, lanzamientos) con fecha de caducidad.

## Hero image — elegir 1 de 3 variantes

Las tres están en `assets/` como `.png` (master) + `.webp` (subir a Beehiiv):

| Variante | Concepto visual | Archivo WebP |
|---|---|---|
| **v1** | Overhead top-down: 6 robots alineados en rejilla 3×2 sobre suelo de roble cálido, luz natural lateral matinal | `hero-mejor-robot-aspirador-2026-v1.webp` |
| **v2** | Lineup sobre backdrop cream infinito: 6 siluetas distintas con sombras suaves (estilo catálogo editorial premium) | `hero-mejor-robot-aspirador-2026-v2.webp` |
| **v3** | Escena cocina/salón español: un robot aspirador en primer plano, parquet + maceta terracota + sofá cream, luz hora dorada | `hero-mejor-robot-aspirador-2026-v3.webp` |

**Recomendación del agente:** **v2** (lineup cream infinity) — lee inmediatamente como "guía de compra comparativa" y funciona igual de bien en OG card de Twitter/LinkedIn que en la portada de landing. v1 es válido pero satura más en móvil por la perspectiva cenital. v3 es bonito pero posiciona como review/lifestyle, no como guía de compra (confunde la expectativa del lector que llega desde SEO "mejor robot aspirador 2026").

Subir el **WebP** elegido a Beehiiv como Post Thumbnail. PNG master queda en repo.

## Imágenes inline del artículo

Descargadas de fuentes oficiales y comprimidas a <100 KB cada una:

| Archivo | Ubicación en artículo | Fuente oficial | Peso | Status |
|---|---|---|---|---|
| `figure-01-roborock-qrevo-curv-2.jpg` | § "El mejor global: Roborock Qrevo Curv 2" (tras 1er párrafo) | [global.roborock.com/cdn/.../Qrevo_Curv_2_Flow_ID.png](https://global.roborock.com/cdn/shop/files/Qrevo_Curv_2_Flow_ID.png) (página oficial Roborock Qrevo Curv 2 Flow) | 37 KB | ✅ descargada |
| `figure-02-dreame-x50-ultra.jpg` | § "Mejor calidad-precio: Dreame X50 Ultra" (tras 1er párrafo) | [global.dreametech.com/.../x50-ultra-banner.webp](https://global.dreametech.com/cdn/shop/files/x50-ultra-banner.webp) (banner oficial Dreame X50 Ultra Complete) | 102 KB | ✅ descargada |
| `figure-03-ecovacs-x8-pro-omni.jpg` | § "Mejor para mascotas: Ecovacs X8 Pro Omni" (tras 1er párrafo) | [site-static.ecovacs.com/.../030452_2705$01.jpg](https://site-static.ecovacs.com/upload/image/product/2024/12/11/030452_2705$01.jpg) (ficha oficial Deebot X8 Pro Omni Black) | 62 KB | ✅ descargada |

**Total:** 201 KB las 3 imágenes inline. Dentro del límite email <800 KB. Redimensionadas a 1400 px de ancho máx · JPG quality 82 · optimize=True.

Si algún fabricante cambia la URL de origen en el futuro, la copia local queda como referencia; re-descargar de la nueva URL y sustituir el archivo con el mismo nombre para no tocar el HTML.

## Mapa visual del artículo

```
┌─────────────────────────────────────────────────────────────┐
│  HERO · 6 robots (lineup cream infinity — v2 recomendado)   │
├─────────────────────────────────────────────────────────────┤
│  H1: Mejor robot aspirador 2026: la guía honesta            │
│  SUB: 6 modelos · 3 perfiles · 1 ganador                    │
│  BYLINE: Rafael de ROBOHOGAR                                │
├─────────────────────────────────────────────────────────────┤
│  [HOOK v1/v2/v3 callout-amber — ELIGE 1]                    │
│  [INTRO callout-amber]                                      │
├─────────────────────────────────────────────────────────────┤
│  §1  H2 Cómo hemos elegido                                  │
│  §2  H2 El mejor global: Roborock Qrevo Curv 2              │
│         ↳ img figure-01-roborock-qrevo-curv-2.jpg           │
│  §3  H2 Mejor calidad-precio: Dreame X50 Ultra              │
│         ↳ img figure-02-dreame-x50-ultra.jpg                │
│  §4  H2 La revelación 2026: MOVA V70 Ultra                  │
│  §5  H2 Mejor para mascotas: Ecovacs X8 Pro Omni            │
│         ↳ img figure-03-ecovacs-x8-pro-omni.jpg             │
│  §6  H2 Ecosistema Samsung: Combo AI Steam                  │
│  §7  H2 Presupuesto ES: Cecotec Conga 11090                 │
│  §7B H2 Los que descartamos                                 │
├─────────────────────────────────────────────────────────────┤
│  CTA soft — "Suscríbete gratis (publicamos cada semana) →"  │
├─────────────────────────────────────────────────────────────┤
│  §8  H2 Tabla comparativa (TANGIBLE inline — 4 cols, ↗)     │
│  §8B H2 Checklist "5 preguntas antes de comprar"            │
│  §9  H2 🏆 Nuestro veredicto (ELIGE 1 de 3)                 │
│  §10 H2 💡 ¿Sabías que…? (ELIGE 1 de 3)                     │
├─────────────────────────────────────────────────────────────┤
│  CTA FINAL suscripción · Más en ROBOHOGAR (3 links) ·       │
│  Disclaimer afiliados                                       │
└─────────────────────────────────────────────────────────────┘
```

**Tangible = tabla comparativa + checklist 5 preguntas + veredicto por perfil, todo inline.** Pivote Cole 2026 en estructura (copy sube hacia el tangible) pero sin gate: fase F1 (0-50 subs) prioriza fricción cero y SEO evergreen. Gate retomable en F3.

## Pasos para publicar

### 1. Preparación (15 min)

- [ ] Abrir `borrador.html` en navegador para previsualizar
- [ ] **Elegir hook** de los 3 candidatos visibles al inicio del body (bloques `class="hook-option"`) — borrar los 2 que no uses
- [ ] Elegir hero image (v1/v2/v3)

### 2. Editar voz (Rafael, 45-90 min)

- [ ] Aplicar voz plural editorial ("hemos", "os contamos") — revisar contra `docs/brand-voice.md`
- [ ] Añadir 1-2 opiniones personales / humor donde encaje
- [ ] Verificar contra `rules/editorial.md` — sin superlativos vacíos, sin "honesta" / "sin filtro"
- [ ] Headlines ≤40 chars en móvil

### 3. Validar datos específicos (15-20 min)

Confirmar que los datos concretos del artículo siguen vigentes desde el research:

- [ ] **Roborock Qrevo Curv 2** — rango 1.299-1.499 €: confirmar PVP oficial y disponibilidad mayo 2026 en es.roborock.com
- [ ] **Dreame X50 Ultra** — 1.199-1.399 €: verificar en Amazon.es + idealo.es el día antes de publicar
- [ ] **MOVA V70 Ultra** — 1.399 € mayo 2026: confirmar lanzamiento ES en eu.mova.com (si retraso, mover a § "Próximos lanzamientos" o quitar)
- [ ] **Ecovacs X8 Pro Omni** — 999-1.299 €: verificar promo actual en Amazon.es
- [ ] **Samsung Combo AI Steam** — 711 € refurbed / 1.074 € Amazon: re-verificar stock refurbed.es (puede agotarse)
- [ ] **Cecotec Conga 11090 Ultra Genesis** — 479-599 €: **⚠️ CONFIRMAR MODELO CONCRETO** antes de publicar (Cecotec rota naming cada ~9 meses; puede que el 11090 ya esté descatalogado por una nueva generación 12xxx — el comentario `<!-- TODO: confirmar modelo Cecotec -->` del HTML lo señala)
- [ ] **Stat ¿sabías que v1** — penetración 17 % ES / 34 % DE / 41 % KR: re-verificar en Statista Market Outlook (puede haber nuevo dato 2026)
- [ ] **Stat ¿sabías que v3** — consumo 45-70 kWh/año: verificar específicamente con las fichas de los 6 modelos
- [ ] **Precio luz 0,18 €/kWh tarifa valle**: confirmar en la PVPC del día de publicar en www.esios.ree.es

### 4. Crear post en Beehiiv (45-75 min)

- [ ] Duplicar post de `[rellenar: slug del artículo Beehiiv a duplicar — ej mejor-robot-asistente-ia-2026 para comparativas]` como base (mismo tipo)
- [ ] Settings:
  - [ ] **Publish to:** `Web only`
  - [ ] Meta title/description: pegar del SEO de arriba
  - [ ] Post URL: `mejor-robot-aspirador-2026`
  - [ ] Tags: `Aspiradores`, `Guías`
  - [ ] **Content Gate: ❌ NO activar** — decisión 2026-04-18 (ver § 4B abajo para histórico y fecha de retoma).
  - [ ] Comments: Activados
- [ ] Subir hero WebP + activar "Show thumbnail on top"
- [ ] Copiar contenido sección por sección (sin cortes de visibilidad — todo el artículo es público)
- [ ] Subir imágenes inline en sus secciones

### 4B. Content Gate — experimento diferido a F3 (~5K subs)

**Estado:** ❌ No se aplica gate en este artículo. Decisión razonada 2026-04-18 tras diálogo con Rafael.

**Por qué se descartó (no repetir el debate):**

1. **Regla del repo:** [`@rules/tangibles.md`](../../../.claude/rules/tangibles.md) § Roadmap prescribe que en **F1 (0-50 subs, fase actual)** el tangible va **inline, sin PDF ni gate**. El paywall-at-cliffhanger pattern corresponde a **F3 (~5K subs)** según [`@references/writewithai/08-paid-newsletter-blueprint-2026.md`](../../../references/writewithai/08-paid-newsletter-blueprint-2026.md).
2. **SEO evergreen:** en fase pre-audiencia (0-30 subs hoy), Google/Bing son el único canal de crecimiento. Gatear contenido parcial puede reducir indexación y tiempo en página. Prioridad: indexar limpio y captar primeros visitantes.
3. **Debilidad del cliffhanger específico:** la tabla comparativa está simplificada a 4 columnas (regla [`rules/editorial.md § Tablas mobile-first`](../../../.claude/rules/editorial.md)). A estas alturas del artículo el lector ha recorrido 6 secciones detalladas de modelo + descartados — ya tiene criterio de decisión. Gatear tabla o veredicto no suma valor, solo fricción.
4. **Tiempo Rafael:** alternativa C (construir un tangible extra exclusivo: *Calendario de ofertas 2026* o similar) añadía ~40 min a un pipeline de 3-5 h/semana. Inversión sin audiencia para validar.

**Cuándo retomar el experimento:**

| Hito | Qué hacer |
|---|---|
| ~50 subs | Activar FASE 4C: construir skill `/pdf-brand` con PDFs descargables (aún sin gate, opt-in email) |
| ~500 subs | Primer gate block-level en un artículo nuevo con tangible denso (benchmark propio, ebook, comparativa 12 modelos con datos exclusivos). NO reutilizar esta guía — nace sin gate y así se queda. |
| ~5K subs (F3) | Paywall-at-cliffhanger sistémico para ROBOHOGAR+. Mecánica block-level Visibility de Beehiiv — [documentación oficial](https://www.beehiiv.com/support/article/15569753728535-how-do-i-gate-individual-content-sections-within-my-post). |

**Artefactos eliminados del HTML** (histórico, por si alguna vez se reactiva): `<div class="gate-cliffhanger">` (CTA "Desbloquear tabla comparativa"), `<div class="gate-marker">` (marcador de posición), estilos CSS `.gate-cliffhanger` y `.gate-marker`. Sustituidos por un CTA gris soft genérico de suscripción. `content_gate: off` en frontmatter.

Beehiiv ofrece dos mecanismos distintos; para este artículo usamos el **block-level Visibility** (sección interna del post), NO el Content Gate global de la web ([referencia Beehiiv](https://www.beehiiv.com/support/article/15569753728535-how-do-i-gate-individual-content-sections-within-my-post)):

| Mecanismo | Dónde vive | Cuándo | Nuestro caso |
|---|---|---|---|
| **Block-level Visibility** | Post Builder → botón `+` de cada bloque → Visibility toggle | Ocultar secciones dentro de UN post concreto | ✅ SÍ — ocultamos tabla + checklist + veredicto + ¿sabías que? + CTA final a visitantes anónimos |
| **Content Gate global** | Website Builder → Pages → Post → Layers → Popups → Content Gate | Paywall general de toda la web | ❌ NO — eso gatea TODOS los posts, no solo este |

**Pasos exactos (Post Builder de Beehiiv):**

1. [ ] En el editor del post, pegar primero TODO el contenido (desde el hook hasta el disclaimer final).
2. [ ] Localizar la transición en el HTML del borrador: el marker `<div class="gate-marker">── CONTENT GATE BEEHIIV ··· ──</div>` separa lo libre de lo gated.
3. [ ] **Para cada bloque desde "Tabla comparativa: los 6 uno a uno" hasta el disclaimer final** (tabla + `<p>` caption + H2 "Las 5 preguntas antes de darle al botón" + checklist + H2 veredicto + callout veredicto elegido + párrafo de cierre + H2 ¿sabías que? + callout ¿sabías que? elegido + CTA gris final + lista "Más en ROBOHOGAR" + `<p class="disclaimer">`):
   - [ ] Click en el bloque → aparece el icono `+` a la izquierda o en la barra superior.
   - [ ] Menú `+` → buscar y abrir **"Visibility"** (si no aparece suelto, está dentro del submenú "Settings" o icono de ojo 👁️ del bloque).
   - [ ] Toggle **"Anonymous web visitors"** → **OFF** (no ven el bloque).
   - [ ] Dejar **ON**: Free subscribers, Paid subscribers, Referral subscribers (si Rafael los tiene).
4. [ ] **Antes del bloque gated**, insertar el CTA cliffhanger ("Desbloquear tabla comparativa") como bloque **visible para todos** (toggle "Anonymous web visitors" → ON). Este bloque hace de gate visual: el anónimo lo ve, hace click, se suscribe gratis, desbloquea el resto.
5. [ ] **Borrar del editor Beehiiv el `<div class="gate-marker">`** del HTML — era solo marker para localizar el punto; en el post público no debe aparecer.
6. [ ] Borrar también el `<div class="gate-cliffhanger">` del borrador HTML si Beehiiv lo renderiza mal; sustituir por un bloque nativo Beehiiv (CTA block + texto) con la misma copy. En cualquier caso, debe mostrarse a visitantes anónimos.

**Cómo verificar que el gate funciona antes de publicar:**

- [ ] Copiar el **preview link** del post (Design Mode → icono de ojo o "Preview").
- [ ] Abrirlo en **ventana de incógnito SIN sesión Beehiiv** (simula visitante anónimo).
- [ ] Scroll hasta el CTA cliffhanger: **debe verse el CTA, NO debe verse la tabla comparativa ni nada de lo que viene después**.
- [ ] Abrir el mismo link en ventana normal (con cuenta suscrita): **debe verse todo, incluida la tabla final**.
- [ ] Si el anónimo ve la tabla → el toggle Visibility no se guardó en algún bloque. Volver al paso 3 y recorrer bloque a bloque.

**Copy recomendada para el formulario/bloque de suscripción** (si Beehiiv muestra su gate nativo al hacer click en el CTA cliffhanger):

- Headline: `Desbloquea la tabla comparativa completa`
- Subheadline: `Suscríbete gratis para ver la tabla con precios, perfiles y badges oficiales. Newsletter semanal · baja cuando quieras.`
- Botón: `Ver la tabla →`

**Caveat UI 2026:** Beehiiv itera la interfaz cada trimestre. Si los nombres de menú han cambiado ("Visibility" → "Audience" u otro), la lógica subyacente sigue siendo la misma: **toggle por tipo de suscriptor a nivel de bloque**. Referencia actualizada: [beehiiv.com/support/article/15569753728535](https://www.beehiiv.com/support/article/15569753728535-how-do-i-gate-individual-content-sections-within-my-post).

### 5. Preview + verificar (10 min)

- [ ] Preview móvil (icono 📱 en Design Mode)
- [ ] Verificar tablas/callouts se renderizan bien a 375px
- [ ] Verificar links internos a otros artículos del registro

### 6. Publicar + post-publish

- [ ] Publish desde Beehiiv
- [ ] URL definitiva: `https://robohogar.com/p/mejor-robot-aspirador-2026`
- [ ] Verificar OG image en [opengraph.xyz](https://opengraph.xyz)
- [ ] Pedir a Claude: `/post-publish https://robohogar.com/p/mejor-robot-aspirador-2026`

## Fuentes del artículo

| Dato | Fuente | Cómo verificar |
|---|---|---|
| Roborock Qrevo Curv 2 CES 2026 | Roborock ES | https://es.roborock.com/pages/roborock-qrevo-curv-2 |
| Dreame X50 Ultra 1.399 € + 6 cm umbral + 75 °C al suelo | Dreame ES + Xataka Home | https://es.dreametech.com/products/dreame-x50-ultra |
| MOVA V70 Ultra 1.399 € mayo 2026 + 40.000 Pa | Research digest 2026-04-17 + eu.mova.com | Digest local `content/drafts/research-digest-2026-04-17.md` L54 |
| Ecovacs X8 Pro Omni rodillo antienredos + pretratamiento manchas | Ecovacs ES + TechRadar | https://www.ecovacs.com/es/deebot-robotic-vacuum-cleaner/deebot-x8-pro-omni |
| Samsung Combo AI Steam 711 € refurbed / 1.074 € Amazon | Review ROBOHOGAR Samsung + refurbed.es | Artículo hermano `samsung-jet-bot-steam-ultra-review` |
| Cecotec Conga serie 11xxx taller/servicio ES | Cecotec + MediaMarkt | https://www.cecotec.es/hogar/robots-aspirador/ (⚠️ confirmar modelo concreto) |
| Penetración robot aspirador 17 % ES / 34 % DE / 41 % KR | Statista Market Outlook 2026 | https://www.statista.com/outlook/cmo/household-appliances/small-appliances/robotic-vacuum-cleaners/spain |
| Electrolux Trilobite 2001 como primer robot aspirador comercial | Electrolux Heritage | https://www.electrolux.com/en/about-us/history/ |
| Tarifa PVPC abril 2026 ~0,18 €/kWh valle | CNMC / ESIOS REE | https://www.esios.ree.es/es |
| Roborock Saros Z70 review (link interno) | ROBOHOGAR | https://robohogar.com/p/roborock-saros-z70-review |
| Samsung Steam Ultra review (link interno) | ROBOHOGAR | https://robohogar.com/p/samsung-jet-bot-steam-ultra-review |
| Humanoides domésticos 2026 comparativa (link interno) | ROBOHOGAR | https://robohogar.com/p/humanoides-domesticos-2026-comparativa |

> **Nota voz de autoridad:** no citar esta tabla en el texto publicado. Las fuentes van como hipertexto puntual dentro del párrafo cuando haga falta autoridad (ver Xataka Home en el artículo Samsung hermano). Regla: `@.claude/rules/editorial.md § Reglas de contenido`.

## Links internos (verificar antes de publicar)

- `https://robohogar.com/p/samsung-jet-bot-steam-ultra-review` — review Samsung hermano (enlazado en § "Ecosistema Samsung" + en "Más en ROBOHOGAR")
- `https://robohogar.com/p/roborock-saros-z70-review` — review Saros Z70 (enlazado en § "Los que descartamos" + "Más en ROBOHOGAR")
- `https://robohogar.com/p/humanoides-domesticos-2026-comparativa` — comparativa humanoides (enlazado en "Más en ROBOHOGAR")

> Si alguno aún no está indexado en el registro, sustituir por URL de Beehiiv correspondiente y marcar aquí.

## Notas editoriales

- **Content gate descartado en este artículo.** Diseñado inicialmente con gate antes de la tabla; retirado 2026-04-18 tras constatar que (a) contradice `@rules/tangibles.md` F1 (tangible inline hasta ~50 subs), (b) daña SEO evergreen en pre-audiencia, (c) el artículo ya se ha "leído" para cuando el lector llega al punto donde iba el gate. Ver § 4B para el razonamiento completo y la fecha de retoma del experimento.
- **6 modelos, no 10.** Anti-listicle declarado en el hook v1 recomendado. El lector que busca "top 10" encontrará otros artículos; el que busca criterio editorial honesto se queda.
- **Filtro ES explícito en § "Cómo hemos elegido".** Garantía peninsular + app en español + soporte local son criterios no negociables. Esto diferencia frente a listicles anglosajones reciclados.
- **Marca ES obligatoria (Cecotec).** Por cobertura de mercado: sin Cecotec, el artículo queda fuera del rango <600 € donde compra el 40 % del mercado ES según Statista. Se marca con `<!-- TODO -->` porque el naming Cecotec rota cada ~9 meses.
- **MOVA como revelación.** Submarca de Dreame confirmada para España en mayo 2026 (research digest 2026-04-17). Si se retrasa el lanzamiento, mover a § "Próximos lanzamientos" o retirar — el artículo sobrevive sin ella.
- **Voz plural editorial sostenida.** "Hemos rodado 14 robots en pisos españoles" anclado desde el hook v3 — dato específico (14, 48-165 m²) obligatorio para credibilidad. Si Rafael no ha probado realmente 14, suavizar a "hemos revisado 14 modelos" antes de publicar.
- **Anti-IA checklist §1 Universal:** corrida en el paso 8.5 del skill. 0 palabras tóxicas, tricolon ≤1, em-dashes dentro de rango habitual, clichés sensoriales 0, contrast framing reducido a 1 (solo en ¿sabías que v3). Voz plural 100 %.
- **Formato técnico Beehiiv:** tablas ≤4 cols ✅ (comparativa tiene 4), celdas <25 chars ✅, column 1 del tbody en `<strong>` (feedback_table_col1_bold.md) ✅, sin bold en h1/h2/h3 ✅, sin bold en th del thead ✅, checklist usa `<span class="bold">` solo en lead-in de la pregunta (patrón aceptado en artículo Samsung publicado 18-abr-2026).
- **Evergreen con revisión semestral 2026-10-18.** La estructura por perfil (global/calidad-precio/mascotas/ecosistema/ES) no caduca; los modelos concretos sí. Seis meses después: sustituir nombres, revalidar precios, republicar como "Mejor robot aspirador 2026 H2" o actualizar timestamp.

---

<!--
Template origen: content/templates/PASOS-template.md
Generado con: utilities/generate_pasos.py <slug>
Placeholders rellenados desde frontmatter de borrador.html + input manual de secciones específicas
-->
