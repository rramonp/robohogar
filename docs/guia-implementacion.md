# ROBOHOGAR — Guía de Implementación (micro-pasos)

> Cada paso es una acción concreta. Si una fase no aplica todavía, sáltala — cada FASE es autocontenida.
> Referencia estratégica: `docs/plan-v2.md` · Referencia visual: `docs/website-brief.md`

---

## 📑 Índice

**Estado actual:** [[#🎯 Roadmap actual (abr 2026)|🎯 Roadmap]] · [[#📍 Dónde estoy hoy — siguiente paso|📍 Siguiente paso HOY]]

**Completado:** [[#FASE 0: Beehiiv Setup (30 min)|FASE 0 Beehiiv ✅]] · [[#FASE 1: Landing Page (1 hora)|FASE 1 Landing ✅]] · [[#FASE 1B: Estética del Blog (formato de artículos en Beehiiv)|FASE 1B Blog ✅]] · [[#FASE 1C: Base de Conocimiento Newsletter & Email|FASE 1C Knowledge ✅]] · [[#FASE 2: Contenido Base (semana 1-2)|FASE 2 Contenido base ✅]] · [[#FASE 3: Obsidian Knowledge Base (✅ COMPLETADA)|FASE 3 Obsidian ✅]]

**En ejecución:** [[#FASE 4: Ciclo de creación de contenido (modo actual)|FASE 4 — Ciclo semanal ⚡]] · [[#FASE 4B: Sprint Evergreen SEO (antes "Distribución activa")|FASE 4B Sprint Evergreen SEO ⚡]] · [[#FASE 4C: Lead Magnet #1 + Sistema de tangibles|FASE 4C Tangibles ⚡]]

**Siguiente:** [[#FASE 4D: Biblioteca pública de tangibles (híbrida)|FASE 4D Biblioteca tangibles ⏳]] (activar al 3er tangible)

**Referencia (no tocar todavía):** [[#FASE 5: Automatización (estado actual)|FASE 5 Automatización]] · [[#FASE 6: Métricas y Revisión|FASE 6 Métricas]] · [[#FASE 7: Post-lanzamiento y mantenimiento con Claude Code|FASE 7 Post-lanzamiento]]

**Futuro:** [[#FASE 8: Crecimiento de suscriptores (cuando haya >50 subs)|FASE 8 >50 subs]] · [[#FASE 9: Optimización Newsletter (cuando haya >200 subs)|FASE 9 >200 subs]] · [[#FASE 10: Pipeline Avanzado (cuando el workflow manual sea el bottleneck)|FASE 10 Pipeline avanzado]]

---

## 🗓 Schedule semanal fijo

> Cadencia inmutable. Si pierdes un día, no se recupera el siguiente: cada ritual tiene su ventana y el siguiente también. Objetivo: que la operativa sobreviva a semanas de poca disponibilidad. Frase trigger = lo que dice Rafael para arrancar el ritual con Claude.

| Día | Hora | Ritual | Skill/Acción | Frase trigger |
|---|---|---|---|---|
| **Lun** | 09:00 | Research digest + rellenar métricas semana previa | `/research-digest` + actualizar [[#FASE 6: Métricas y Revisión\|FASE 6 § tabla semanal]] | *"Ritual lunes — digest + métricas"* |
| **Mar** | 09:00 | Newsletter (si ≥30 subs) · si no → draft artículo | Beehiiv send · `/content-draft <tema>` | *"Ritual martes — newsletter"* · *"Ritual martes — draft"* |
| **Mié** | 09:00 | Continuar artículo + heros | `/content-draft` · `/nano-banana` | *"Ritual miércoles — seguir"* |
| **Jue** | 09:00 | Publicar + post-publish + social | `/post-publish <URL>` · `/social-content <URL>` | *"Ritual jueves — publicar"* |
| **Vie** | 09:00 | Tangible (quincenal) · optim CTR/subs (viernes alterno) | `/pdf-brand <variante> <slug>` · *"Trigger optimización ROBOHOGAR"* | *"Ritual viernes — tangible"* · *"Ritual viernes — optimizar"* |
| **Sáb** | libre | ~~Promo foros/Reddit/Menéame~~ **PAUSADO 2026-04-20** — slot libre para lo que Rafael decida (ficción si evergreen cerrado, research adicional, o descanso) | — | — |
| **Dom** | off | — | — | — |

**Mantenimiento mensual (último viernes del mes):** `/pipeline-debug full` — audit completo del repo (skills, rules, refs, tangibles, memoria, docs, schedule). Genera report en `content/pipeline-debug-reports/<YYYY-MM-DD>-debug.md`. Ver [[#FASE 7: Post-lanzamiento y mantenimiento con Claude Code|FASE 7 § Mantenimiento]].

**Revisión mensual (primer lunes del mes):** *"Review mensual ROBOHOGAR — mes <YYYY-MM>"* → Claude compara KPIs vs SLOs y archiva en `docs/reviews-mensuales/`.

**Regla de oro:** si una pieza nueva (skill, tangible, formato) no tiene su fila en este schedule o en [[#📊 SLOs por fase|FASE 6 § SLOs]], entonces o se integra o se posterga. Piezas sin ritual = drift.

---

## 🎯 Roadmap actual (abr 2026 — pivote SEO-first 2026-04-20)

**Estado (21-abr-2026):**

- ✅ **9 artículos publicados** — catálogo completo en [`content/registro-articulos.md`](../content/registro-articulos.md). Último: [Mejor robot cortacésped 2026: 6 finalistas + checklist de 7 preguntas antes de comprar](https://robohogar.com/p/mejor-robot-cortacesped-2026) (2026-04-21).
- ❌ **0 suscriptores** · newsletter semanal diferida hasta 30-50 subs.
- ❌ **0 Ficciones Domésticas** publicadas (pilar experimental pendiente de arrancar).
- ✅ **Pipeline de skills funcionando** (`/research-digest` · `/content-draft` · `/nano-banana` · `/post-publish` · `/social-content` · `/obsidian-robohogar`).
- ✅ **Knowledge base Write With AI completa** — 9 archivos en [`references/writewithai/`](../references/writewithai/) + banco de 90 preguntas en [calendario-editorial.md § Elements of Value](../content/calendario-editorial.md#banco-de-preguntas--elements-of-value).

### 🔄 Pivote 2026-04-20: de distribución activa → SEO-first evergreen

Sesión 2026-04-20 confirmó que el outreach manual en Reddit/Menéame/Xataka/Forocoches no es viable con 3-5 h/sem y sin cuentas ES con karma previo: Reddit bloquea scraping con captcha, Xataka tiene comentarios desactivados hace años, Forocoches es por invitación, Facebook descartado. **Pivote completo:** el motor de crecimiento pasa a ser **SEO evergreen + tangibles como conversión**. Outreach manual queda en pausa indefinida.

Detalle + razones: memoria `feedback_seo_first_pivote.md`.

### Prioridad 1 — SPRINT EVERGREEN SEO ⚡ (motor de crecimiento)

- **Objetivo:** construir la biblioteca evergreen que atrae tráfico orgánico sostenido (mes 6-18) mediante guías de compra, reviews y comparativas con intención compra clara.
- **Ratio:** 3 evergreens / 1 reactivo por cada 4 artículos publicados. Los reactivos (noticias con caducidad <3 meses) solo si el evergreen de la semana está cerrado.
- **Backlog priorizado:** 14 candidatos E1-E14 en [`content/calendario-editorial.md § Backlog Evergreen SEO`](../content/calendario-editorial.md). Priorizar estacionales en ventana (E1 cortacésped · E12 ROI cortacésped → primavera-verano) + hedge emerging (E13 mascota robot · E14 asistentes IA escritorio).
- **Frase trigger:** *"Retomamos evergreen — siguiente del backlog"* o *"Evergreen E<N>"* para elegir uno concreto.
- **Detalle operativo:** [[#FASE 4B: Sprint Evergreen SEO (antes "Distribución activa")|FASE 4B]].

### Prioridad 2 — TANGIBLES COMO MOTOR DE CONVERSIÓN (FASE 4C ⭐)

- **Principio editorial vigente:** *"tangible = producto, no bonus"* (Cole/Bush 2026). Cada artículo se diseña con el tangible como cliffhanger antes del CTA. Regla: [`tangibles.md`](../.claude/rules/tangibles.md).
- **Skill `/pdf-brand cheatsheet` operativo desde 2026-04-18** — variantes restantes (`comparativa` · `guia` · `relato`) pendientes activación por demanda. Cada evergreen que lo requiera acopla su tangible (ver columna "Tangible acoplado" en E1-E14).
- **Primer tangible activo:** Hoja de Compra ROBOHOGAR (PDF 4pp, v2 validada 2026-04-18) en [`content/lead-magnets/hoja-compra/`](../content/lead-magnets/hoja-compra/). Digital Product: `https://robohogar.com/products/hoja-de-compra`.
- **Banner lead magnet Dark** activo en home + 3 artículos consumer. Snippets: [`content/templates/banner-lead-magnet-snippets.md`](../content/templates/banner-lead-magnet-snippets.md).
- **Welcome flow MVP 2 emails** activo: [`docs/welcome-flow-setup.md`](welcome-flow-setup.md).
- **Frase trigger:** *"Retomamos tangibles — siguiente PDF"*.
- **Detalle operativo:** [[#FASE 4C: Lead Magnet #1 + Sistema de tangibles|FASE 4C]].

### Prioridad 3 — BIBLIOTECA PÚBLICA DE TANGIBLES (FASE 4D futura ⏳)

- **Qué es:** página pública `robohogar.com/recursos` que muestre portada + título + descripción de TODOS los tangibles. CTA por tangible: *"Descargar gratis con la newsletter"* → Digital Product de Beehiiv (sigue con gate de suscripción). Opcional: 1 tangible "sampler" de 1 página sin gate como demo de calidad.
- **Por qué:** aumenta la visibilidad pública del catálogo de tangibles (hoy solo descubribles banner-a-banner) sin romper la conversión del gate. Modelo híbrido validado por Rafael 2026-04-20.
- **Activar cuando:** haya **≥3 tangibles publicados** (hoy 1). Candidatos siguientes: Guía primer mes aspirador + Decision tree cortacésped + Comparativa mascota robot.
- **Frase trigger:** *"Retomamos FASE 4D — biblioteca pública de tangibles"*.
- **Detalle operativo:** [[#FASE 4D: Biblioteca pública de tangibles (híbrida)|FASE 4D]].

### 📊 Indicadores orientativos (sin decisión automática)

> **No son métricas de corte.** Rafael decidió 2026-04-20: *"es un proyecto personal, no vamos a establecer métricas de corte"*. Estos números son solo **marco mental** — qué cabría esperar si el SEO compuesto funciona. La decisión de revisar o pivotar la toma Rafael cuando quiera, no lo dispara un umbral.

| Horizonte | Tráfico orgánico esperado | Subs orgánicos acumulados | Lectura |
|---|---|---|---|
| M3 (jul-2026) | 200-500 visitas/mes | 3-15 | Si >500 y >20: mercado responde. Si <100: contenido no indexa — diagnóstico on-page necesario. |
| M6 (oct-2026) | 1.000-3.000 | 10-90 | Si 1-2 evergreens top-10, empieza la curva. |
| M12 (abr-2027) | 3.000-10.000 | 30-300 | Si 2-3 evergreens top-5, proyecto cumple hipótesis SEO-first. |

> Las fases posteriores (5 automatización · 6 métricas · 7 post-lanzamiento · 8 crecimiento >50 subs · 9 optimización newsletter · 10 pipeline avanzado) siguen ahí pero no son el foco. La FASE 4B original (distribución activa Reddit/Menéame) queda **cerrada indefinidamente** — Rafael confirmó 2026-04-20 que no va a construir cuentas ES con karma previo. Única válvula de aceleración no-manual futura: **Beehiiv Boosts** (pagado), pero solo con cluster SEO maduro (≥10 evergreens + 2-3 tangibles). El motor es SEO orgánico + tangibles, sin plan B de outreach.

---

## 📍 Dónde estoy hoy — siguiente paso

> Última actualización: 21-abr-2026, tras publicar #9 *[Mejor robot cortacésped 2026: 6 finalistas + checklist de 7 preguntas antes de comprar](https://robohogar.com/p/mejor-robot-cortacesped-2026)*.

### 📌 Próximos 3 next steps

> Plantilla viva. `/post-publish` y `/pdf-brand` **deben** actualizar estos 3 bullets al completar tareas (marcar el completado · añadir el siguiente desde backlog de `calendario-editorial.md` · actualizar "Último artículo" / "Último tangible" en [[#🎯 Roadmap actual (abr 2026)\|🎯 Roadmap actual]]). Si los 3 están marcados al abrir una sesión, tirar del backlog de calendario.

- [x] **Next 1 —** ~~Publicar artículo #8 *"Un humanoide bate el récord mundial humano de media maratón"*~~ → Publicado 20-abr-2026. URL: https://robohogar.com/p/humanoide-maraton-pekin-record-mundial
- [x] **Next 2 —** ~~Publicar artículo #9 *"Mejor robot cortacésped 2026 · Guía de compra"* (E1 del backlog evergreen, estacional)~~ → Publicado 21-abr-2026. URL: https://robohogar.com/p/mejor-robot-cortacesped-2026
- [ ] **Next 3 —** Primera flash Ficciones Domésticas *"El operador nocturno"* (ahora que el evergreen de la semana está cerrado · regla evergreen-first cumplida) · frase trigger: *"Retomamos ficciones — arrancar piloto"* · `/ficcion-draft`
- [ ] **Next 4 —** **Evergreen E12 — Robot cortacésped vs tradicional: ROI en 3 años** (estacional mismo pico abr-jul · cluster SEO con E1 vía internal linking) · frase trigger: *"Retomamos evergreen — empezamos E12 ROI cortacésped"* · `/content-draft Robot cortacésped vs cortacésped tradicional: ROI en 3 años` · ver [calendario-editorial.md § Backlog Evergreen SEO](../content/calendario-editorial.md)
- [ ] **Next 5 —** **Evergreen E4 — Mejor robot aspirador para piso pequeño (<60 m²)** (long-tail baja competencia, perfil ES típico, no estacional) · frase trigger: *"Retomamos evergreen — empezamos E4 piso pequeño"* · `/content-draft`

**Último artículo publicado:** #9 *Mejor robot cortacésped 2026: 6 finalistas + checklist de 7 preguntas antes de comprar* (2026-04-21).
**Último tangible publicado:** Hoja de Compra v2 PDF (2026-04-18) → `content/lead-magnets/hoja-compra/`.

### 🌍 Filtro mercado ES — regla base

ROBOHOGAR se enfoca en **España primario + LATAM secundario**. Antes de aceptar un tema, validar distribución ES + keyword ES + cobertura en ≥2 fuentes de [`references/fuentes-es-master.md`](../references/fuentes-es-master.md). Regla completa: [`editorial.md § Filtro mercado ES/LATAM`](../.claude/rules/editorial.md). Los skills `/research-digest` y `/content-draft` ya lo aplican automáticamente.

### 🎯 Sprint concreto #6 → #7 → #8 ✅ COMPLETADO (abril 2026)

> Histórico: sprint original del ciclo #6-#8 ya cerrado (#6 Samsung Jet Bot 18-abr · #7 Mejor aspirador 2026 19-abr · #8 Humanoide maratón Pekín 20-abr). **Tras 20-abr-2026 el sprint activo es el Sprint Evergreen SEO — ver [`Roadmap § Prioridad 1`](#prioridad-1--sprint-evergreen-seo--motor-de-crecimiento) y [`FASE 4B`](#fase-4b-sprint-evergreen-seo-antes-distribución-activa).**

#### Artículo #6 — Samsung Jet Bot Steam Ultra ✅ PUBLICADO 18-abr-2026

- **URL:** https://robohogar.com/p/samsung-jet-bot-steam-ultra-review
- **Ángulo editorial final:** el vapor a 100°C no toca el suelo — toca las mopas en la base. Desmontaje honesto del claim con cita a Xataka Home como autoridad.
- **Variantes elegidas por Rafael:** hook v1 (Belief destruction) · veredicto v3 (Contrarian) · ¿sabías que? v3 (Dato histórico). Las 3 recomendaciones IA.
- **Tangibles inline:** tabla comparativa 5 modelos + checklist "5 preguntas antes de comprar con vapor".
- **Evergreen:** true (próxima revisión de precios: **2026-10-18**).

#### Artículo #7 — Mejor robot aspirador 2026 · Guía de compra CON Content Gate ⭐

Primera aplicación del pivote Cole *"tangible = producto"* con email gating real.

**Estructura:**

- **60% abierto (SEO-indexable):** intro, contexto mercado ES 2026, criterios de elección, análisis individual 4-5 modelos (Roborock / Dreame / Ecovacs / Samsung / Xiaomi — todos con distribución ES), opinión editorial.
- **Content Gate split point:** bloque "Introduce tu email para seguir leyendo — tabla comparativa + checklist".
- **40% gated:** tabla comparativa maestra con ganador por caso de uso, checklist "5 preguntas antes de comprar", veredicto por perfil (piso <70 m² / casa grande / mascota / presupuesto apretado).

**Configuración Beehiiv (free plan — sin upgrade):**

- Post settings → *Advanced email capture* → **Content Gate** ON.
- Split point: justo antes de la tabla comparativa final.
- Subs ya existentes: lectura completa sin gate (default).
- Meta description + OG apuntan a la parte abierta (SEO intacto).

**Comando:** `/content-draft Mejor robot aspirador 2026 guía de compra · estructura con content gate antes de la tabla comparativa final`

#### Artículo #8+ — Abrir FASE 4B (distribución activa)

Con ≥7 artículos publicados, activar [[#FASE 4B: Distribución activa (0-50 subs)|FASE 4B]]: Reddit + Menéame + Beehiiv Boosts (€20 piloto).

**Frase trigger:** *"Retomamos distribución 4B — tócame los hilos Reddit activos"*.

### 📖 Arrancar Ficciones Domésticas (paralelo al sprint evergreen)

El pilar de ficción experimental **aún no está arrancado** como publicación (hay 1 relato aprobado internamente pero no publicado en Beehiiv). Aporta diferenciación de marca y variedad editorial, no tráfico SEO — **cadencia hasta 1 cada 1-2 semanas, condicionada a evergreen-first** (solo sale si el evergreen de la semana está entregado). Actualizado 2026-04-20 al pivote SEO-first.

- **Semilla prioritaria:** 🥇 *"El operador nocturno"* — teleoperación NEO desde Manila + deal EQT (dato real ancla).
- **Comando:** `/ficcion-draft` (sin argumentos → skill lee el backlog y propone 3 opciones).
- **Regla dura:** si el evergreen de la semana no está cerrado, NO publicar ficción esa semana. La ficción no canibaliza el motor de crecimiento.

### 📝 Principio editorial transversal — tangible = producto

Cuando invoques `/content-draft`, **empieza definiendo el tangible** en el `PASOS.md` ANTES del copy. El artículo entero se estructura para llevar al tangible. Regla completa: [`tangibles.md`](../.claude/rules/tangibles.md). En el #6 el tangible es inline (checklist específico vapor); en el #7 es inline + gated (tabla maestra + checklist 5 preguntas).

### 🚫 Qué NO hacer todavía

- ❌ **No hacer outreach manual en Reddit / Menéame / foros ES.** **Cerrado indefinidamente** tras pivote 2026-04-20: Rafael confirmó que no va a construir cuentas ES con karma previo. La vía queda descartada como motor de crecimiento. Si en el futuro Rafael cambia de opinión, será caso-por-caso, no un sprint completo de distribución. Detalle: memoria `feedback_seo_first_pivote.md`.
- ❌ **No activar newsletter semanal** — espera a 30-50 subs. Con `Email and web` los artículos ya se envían a los pocos subs que haya.
- ❌ **No abrir canales sociales propios** con cadencia forzada (IG/LinkedIn/WhatsApp). El motor actual es SEO + tangibles, no social.
- ❌ **No tocar paid tier / paywall de pago / cadencia dual** — diferido a F3 (≥5K subs). Documentado en [`08-paid-newsletter-blueprint-2026.md`](../references/writewithai/08-paid-newsletter-blueprint-2026.md) como *reference*, no como acción. **Content Gate ≠ paywall**.
- ❌ **No publicar ficción si el evergreen de la semana no está cerrado.** Regla dura post-pivote 2026-04-20.
- ❌ **No romper el ratio 3 evergreens / 1 reactivo.** Los reactivos (noticias con caducidad <3m) son atractivos por frescura pero no traen tráfico orgánico sostenido. Solo 1 por cada 3 evergreens cerrados.
- ❌ **No recomendar temas sin pasar el filtro mercado ES** (salvo mainstream Apple/Tesla/Samsung/Google/Xiaomi).

---

## Preparación: Clonar el repo (si estás en otro PC)

Si es la primera vez en este PC o no tienes el repo clonado:

```bash
cd $HOME
git clone https://github.com/rramonp/robohogar.git
cd robohogar
```

Si ya lo tienes clonado, actualiza:

```bash
cd $HOME/robohogar
git pull
```

> [!tip]
> Esta guía también está disponible en Obsidian:
> `05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md`
> Si modificas la guía en el repo, copia la versión actualizada al vault de Obsidian.

---

## FASE 0: Beehiiv Setup (30 min)

### Crear cuenta

- [x] Ir a **https://app.beehiiv.com/signup**
- [x] Rellenar: nombre → `Rafael`, email → tu email personal, contraseña
- [x] Publication Name → `ROBOHOGAR`
- [x] Description → `Tu dosis de robótica doméstica · Cada semana, comparativas, reviews, editoriales y relatos`
- [x] Category → `Technology`
- [x] Frequency → `Weekly`

### Subir branding

- [x] Ir a **Settings → Publication → Branding**
- [x] Logo: subir `assets/branding/master/robohogar-mascot-principal.png`
- [x] Favicon: subir la misma imagen (Beehiiv la recorta)
- [x] Accent color → `#F5A623`
- [x] Background → `#FFFFFF`
- [x] Text color → `#0C0C0C`
- [x] Font: Beehiiv no permite Jost/DM Sans custom en free plan — elegir la sans-serif más limpia disponible (Inter o el default)

### Conectar dominio robohogar.com

- [x] En Beehiiv: ir a **Settings → Publication → Domains → Add Custom Domain**
- [x] Escribir `robohogar.com` y pulsar Continue
- [x] Beehiiv muestra los registros DNS necesarios — déjalos abiertos en una pestaña

**En Namecheap (https://ap.www.namecheap.com → Domain List → robohogar.com → Advanced DNS):**

> [!warning]
> Elimina PRIMERO los registros por defecto que Namecheap pone (parking records, URL redirect, etc.) antes de añadir los de Beehiiv. Si no, habrá conflictos.

Registros DNS que Beehiiv típicamente pide (los valores exactos los da Beehiiv en su panel — copia desde allí):

| # | Tipo | Host | Valor (copiar de Beehiiv) | TTL |
|---|---|---|---|---|
| 1 | CNAME | `www` | apuntando a Beehiiv CDN | Auto |
| 2 | A | `@` | IP de Beehiiv | Auto |
| 3 | CNAME | verificación 1 | valor de Beehiiv | Auto |
| 4 | CNAME | verificación 2 | valor de Beehiiv | Auto |
| 5 | TXT | `@` | verificación SPF | Auto |
| 6 | CNAME | DKIM key 1 | valor de Beehiiv | Auto |
| 7 | CNAME | DKIM key 2 | valor de Beehiiv | Auto |
| 8 | CNAME | DKIM key 3 | valor de Beehiiv | Auto |
| 9 | TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:dmarc@robohogar.com` | Auto |
| 10 | MX | `mail` | valor de Beehiiv | Auto |
| 11 | TXT | `mail` | SPF para subdominio mail | Auto |
| 12 | CNAME | `mail` | valor de Beehiiv (si pide CNAME en vez de MX) | Auto |

- [x] Añadir cada registro en Namecheap: botón **Add New Record** → seleccionar tipo → pegar Host y Value
- [x] Volver a Beehiiv y pulsar **Verify Domain**
- [x] Si dice "Pending" — esperar. Propagación DNS: 15 min a 72h (normalmente <2h)

> [!tip]
> Para comprobar propagación: https://dnschecker.org — busca tu dominio y tipo de registro (CNAME, TXT, etc.)

### Configurar email sender

- [x] En Beehiiv: **Settings → Publication → Sending → Sender Email**
- [x] Configurar como `hola@robohogar.com` o `robot@robohogar.com`
- [x] Sender Name → `Rafael de ROBOHOGAR`
- [x] Reply-to → tu email personal (para recibir respuestas directas)

### DMARC

- [x] Verificar que el registro TXT `_dmarc` está activo en Namecheap (paso #9 arriba)
- [x] En Beehiiv, en la sección de Domain, debe aparecer DMARC como ✅ verificado
- [x] Si no aparece tras 24h, revisar que el Host es exactamente `_dmarc` (sin el dominio, Namecheap añade `.robohogar.com` automáticamente)

---

## FASE 1: Landing Page (1 hora)

### AI Website Builder

> [!warning] PASO CRÍTICO
> Abre `docs/website-brief.md` del repo. Ve a la sección **"Prompt para Beehiiv AI Builder"** (línea ~165). Copia el bloque de código ÍNTEGRO (70+ líneas, desde `Build a newsletter landing page...` hasta el cierre de ```). NO uses un resumen — pega TODO.

- [x] En Beehiiv: ir a **Website → AI Website Builder**
- [x] Si no ves AI Builder: ir a **Website → Design Mode** y construir manualmente siguiendo la tabla de secciones de abajo
- [x] Pegar el prompt completo (70+ líneas) del website-brief.md
- [x] Pulsar **Generate** y esperar a que se genere la página completa
- [x] **Verificar:** comparar cada sección generada con la tabla "Ajustar sección por sección" de abajo. El AI no siempre genera exacto — ajustar en Design Mode lo que falte

### Ajustar sección por sección (Design Mode)

**Hero (above the fold):**

- [x] Headline → `Tu dosis de robótica doméstica`
- [x] Subtítulo → `Cada semana, comparativas, reviews, editoriales y relatos`
- [x] Placeholder del input → `tu@email.com`
- [x] Botón → `Suscríbete gratis` con fondo `#F5A623`, texto `#FFFFFF`
- [x] Sin texto bajo el botón — el trust text (`100% gratis · Sin spam · Cancela cuando quieras`) va SOLO en el footer
- [x] Imagen de la mascota principal con café

**Artículos destacados (justo bajo el hero):**

- [x] En Design Mode: añadir bloque **"Recent Posts"** o **"Featured Posts"**
- [x] Configurar para mostrar 2-3 posts con imagen + título + excerpt
- [x] Título de sección → `Lo último en ROBOHOGAR`

> [!warning]
> Esta sección estará vacía hasta que publiques los primeros artículos (FASE 2). Publica al menos 2 posts ANTES de compartir la landing públicamente.

**Sobre qué escribimos** (3 pilares — formato 3-column horizontal, NO 4 cards apiladas):

- [x] Título → `Sobre qué escribimos`
- [x] 3 columnas (icono grande + headline en bold + sub-línea ≤30 chars):
  - `🤖 **Análisis** · Lo que pasa esta semana`
  - `🔍 **Reviews** · Robots reales, sin filtro`
  - `📖 **Ficciones** · El hogar de 2035`

> Beehiiv: usar el componente "Three Column" / "Features" del template Aurora News. Si no existe, usar bloque de HTML personalizado. NO usar el componente "Card list" actual (4 cards apiladas → mal UX en móvil).

**Sobre el autor:**

- [x] Imagen: subir `assets/branding/master/robohogar-mascot-leyendo.png` *(sección omitida — decisión editorial)*
- [x] Texto → `Soy Rafael. Pruebo robots en casa, investigo lo que viene y te cuento lo que merece la pena — sin comunicados de prensa ni hype vacío.`
> Nota: la bio personal mantiene "te cuento" (singular). El plural "contamos" se usa solo en la voz de marca (tagline, subtítulo).

**FAQ:**

- [x] Pregunta 1: `¿Con qué frecuencia llega?` *(omitida en implementación final — la frecuencia ya se indica en el tagline)*
- [x] Pregunta 2: `¿Es gratis?`
- [x] Pregunta 3: `¿Quién escribe esto?`

**Footer:**

- [x] Segundo CTA: `¿Te lo vas a perder?` + formulario de email
- [x] Trust text bajo el formulario del footer → `100% gratis · Sin spam · Cancela cuando quieras` (única ubicación en toda la landing)
- [x] Links a redes cuando estén creadas (FASE 5)

### Mobile testing

- [x] En Beehiiv Design Mode: usar el icono de preview móvil (📱)
- [x] Verificar: el formulario de email es visible sin scroll
- [x] Verificar: las cards de artículos se apilan verticalmente
- [x] Verificar: el texto es legible (mínimo 16px body)
- [x] Verificar: el botón CTA es fácil de pulsar con el pulgar (mínimo 44px alto)
- [x] Publicar la landing: **Website → Publish**

### Assets necesarios para la landing (generar con nano-banana)

| Asset | Archivo | Dónde se usa | Prioridad |
|---|---|---|---|
| **Hero mascota** | `hero-landing-beehiiv.png` (1200x800) | Hero section, lado derecho | P1 — sin esto la landing queda vacía |
| **OG image** | `og-image-robohogar.png` (1200x630) | Meta tag, compartir en redes | P1 — necesario antes de compartir links |
| **Favicon** | `favicon-robohogar.png` (512x512) | Pestaña del navegador | P1 — credibilidad básica |
| **About mascota** | Reutilizar `mascot-leyendo.png` del master | Sección "Sobre el autor" | Ya existe |

> [!tip]
> Generar los 3 assets P1 con `/nano-banana` ANTES de montar la landing en Beehiiv. Así al configurar solo hay que subir los archivos.

### Referencia visual: cómo se ven los mejores

| Referente | Qué copiar para la landing |
|---|---|
| **Newsletter Operator** | Hero con social proof ("50K+ founders") + email campo con borde naranja. "Featured" articles como cards justo debajo. 3 CTAs por página (hero, mid, footer). |
| **Morning Brew** | Tagline memorable ("Become smarter in 5 minutes"). Segundo CTA con mockup de móvil. Juegos como engagement (futuro). |
| **The Hustle** | Headlines GRANDES (54px). Separación clara entre "News Briefs" (corto) y "Originals" (largo). Lead magnet mid-page. |
| **TLDR** | Subscribe button después de CADA artículo (agresivo pero efectivo). Social proof "1.6M readers" prominente. Layout ultra-minimal. |
| **Milk Road** | Ticker de datos relevantes al nicho (futuro: "Últimos robots lanzados"). Pill buttons modernos. |

---

## FASE 1B: Estética del Blog (formato de artículos en Beehiiv)

El blog son los artículos publicados como web posts en Beehiiv. Es tan importante como la landing — el visitante que llega por SEO aterrizará en un artículo, NO en la landing.

### Configuración global del blog

- [x] En Beehiiv: **Website → Design → Blog Settings**
- [x] Layout de artículos: elegir layout con imagen destacada grande arriba (como The Hustle Originals)
- [x] Mostrar: autor, fecha, tiempo de lectura, categoría
- [x] Activar compartir en redes (botones share al final del artículo)
- [x] Activar comentarios (genera engagement y reply signals)

### Estética de cada artículo (basada en research)

Cada artículo publicado en Beehiiv debe seguir esta estructura visual:

```
[Imagen destacada — 1200x630, mascota + contexto temático]

CATEGORÍA · 5 min de lectura

# Título SEO optimizado (H1)

Subtítulo con hook (1-2 frases que enganchen)

---

Contenido con H2s para cada sección principal.
Párrafos cortos (3-4 líneas máx).
Listas con bullets para datos concretos.
Imágenes inline donde aporten (screenshots, comparativas).

> Callout con opinión personal o dato destacado

[CTA mid-article: "¿Te está sirviendo? Publicamos cada semana →"]

Más contenido...

[Link de afiliado natural dentro del contexto, no banner]

---

**¿Te ha gustado?** Comparte con alguien que tenga un robot en casa.

[Botones: Compartir en Twitter · LinkedIn · WhatsApp]

---

**Más en ROBOHOGAR:**
[Card artículo relacionado 1] [Card artículo relacionado 2]
```

### Assets necesarios para artículos (generar con nano-banana)

**Templates (generar una vez):**

| Asset | Archivo | Uso | Prioridad |
|---|---|---|---|
| **Header newsletter** | `newsletter-header.png` (600x150) | Cabecera de cada email enviado | P1 |
| **Social card template** | `social-card-template-v2.png` (1080x1080) | Compartir artículos en redes | P2 |

**Imágenes por artículo (genera el agente de imágenes automáticamente):**

Cada artículo necesita 1 imagen destacada (1200x630). El agente de imágenes (`/nano-banana`) la genera automáticamente como parte del pipeline de publicación y la cataloga en `assets/branding/asset-catalog.md`.

### Estrategia de imágenes

| Tipo | Origen | Ejemplo |
|---|---|---|
| **Imagen destacada (hero)** | Siempre branded con nano-banana | Mascota + contexto temático, estilo ROBOHOGAR |
| **Imágenes inline (dentro del artículo)** | Originales de la fuente/fabricante | Fotos de producto, screenshots, renders oficiales |

**Por qué branded para el hero:** Las cards en la landing, el OG al compartir y la preview en redes deben tener identidad visual consistente. Si cada artículo usa una foto distinta (Samsung, iRobot, stock), la landing parece un collage.

**Por qué originales inline:** Dentro del artículo el lector quiere ver el producto real, no ilustraciones. Fotos del fabricante + capturas aportan realismo y credibilidad.

> [!warning]
> Cada artículo NECESITA su imagen destacada branded (1200x630) antes de publicar. Sin imagen, las cards en la landing y las previews en redes quedan vacías y la conversión cae. El agente de imágenes se encarga de esto como paso del pipeline.

### Patrones de formato por tipo de contenido

**Review/Comparativa (70% del contenido):**

- Tabla comparativa specs al inicio
- Pros/Contras con iconos ✅/❌
- Veredicto claro: "¿Lo compraría? Sí/No y por qué"
- Link de afiliado al final de cada review individual
- Reference: Newsletter Operator usa inline CTA mid-article con lead magnet

**Editorial/Futuro (30% del contenido):**

- Hook con dato sorprendente o imagen evocadora
- Opinión personal fuerte (no hedging)
- Dato + especulación + consecuencia para el lector
- Sin links de afiliado (este contenido construye marca, no revenue)
- Reference: The Hustle "Originals" — reportajes largos con titulares creativos

**Newsletter semanal:**

- Template fijo de 5 secciones (ver FASE 4)
- Máximo 1.500 palabras
- Email gating en el artículo web más valioso de cada issue
- Reference: TLDR — cada item es link + resumen de 2-3 líneas. Conciso.

### Categorías/Tags en Beehiiv

Configurar estas categorías para organizar el contenido:

- [x] **Aspiradores** — reviews, comparativas, guías de compra
- [x] **Cortacéspedes** — reviews, configuración, mantenimiento
- [x] **Humanoides** — noticias, análisis, opinión
- [x] **Asistentes IA** — robots de escritorio, compañeros IA
- [x] **Robot Mascotas** — robot pets, compañeros emocionales
- [x] **Smart Home** — domótica, integración, ecosistemas
- [x] **Noticias** — última hora, lanzamientos
- [x] **Guías** — tutoriales, configuración, troubleshooting
- [x] **Opinión** — editoriales, futuro, debate

> [!tip]
> Cada artículo web post = 1 categoría + 2-3 tags. Las categorías aparecen como badges en las cards (como TLDR usa "Tech", "AI", "Dev").

---

## FASE 1C: Base de Conocimiento Newsletter & Email

> Antes de crear contenido o templates, instalamos el conocimiento base de email marketing
> que informará todas las decisiones de newsletter, templates y automatización.
> Fuentes: beehiiv-newsletter-advisor (datos de plataforma) + email-marketing-bible (best practices generales).

### Referencia unificada de email marketing

- [x] Clonar temporalmente repos fuente (beehiiv-newsletter-advisor + email-marketing-bible)
- [x] Curar y fusionar contenido relevante por tema (excluir: ecommerce, cold email, case studies)
- [x] Crear `references/newsletter/email-marketing-playbook.md` con 11 secciones:
  - Benchmarks & KPIs (beehiiv 2025 + genéricos)
  - Growth Stack (canales ordenados por impacto)
  - Welcome Series (6 emails adaptados a ROBOHOGAR)
  - Subject Lines & Copywriting (frameworks PAS/BAB/1-3-1)
  - Email Design Patterns (specs + anti-slop + 57 diseños curados)
  - Deliverability (autenticación + Gmail Primary + cambios 2025-2026)
  - Segmentation (5 tiers de engagement)
  - Testing (prioridades)
  - Compliance GDPR (audiencia EU)
  - Creator Milestones (revenue stack, inflexión 10K)
  - Send Timing (martes/miércoles, 9:00 AM)
- [x] Verificar: archivo accesible y referenciado desde `/content-draft`

### Regla compacta de newsletter

- [x] Crear `rules/newsletter.md` (≤40 líneas) — mecánicas de email
- [x] Ownership claro: `editorial.md` = voz/tono, `newsletter.md` = entrega/diseño/optimización
- [x] Añadir `@rules/newsletter.md` a `CLAUDE.md`
- [x] Verificar: ≤40 líneas, sin duplicación con `editorial.md`

### Actualizar skill de contenido

- [x] Añadir tipo "Newsletter" a la tabla de tipos en `.claude/commands/content-draft.md`
- [x] Añadir template en tabla de templates
- [x] Añadir referencia condicional al playbook para tipo Newsletter

### Investigación de templates de referentes ✅ superado

> ~~Investigar qué estructuras usan las newsletters exitosas antes de diseñar los nuestros.~~
> **Descatalogado 18-abr-2026:** superado por parseo completo de Write With AI (Cole/Bush) en [`references/writewithai/`](../references/writewithai/) — 9 archivos con growth playbook, prompts, templates short-form, paid newsletter blueprint 2026 y Content Library Elements of Value. La base de referencia existe y es más actual.

- [x] ~~Scrape 2-3 issues de cada referente con Firecrawl (TLDR, Hustle, Morning Brew, Newsletter Operator, Chartr)~~
- [x] ~~Extraer estructura HTML, tipografía, espaciado~~
- [x] ~~Documentar patrones~~ → vivos en `references/writewithai/02-estructura-articulo-visual.md` + `04-email-newsletter-patterns.md`

### Sistema de templates ROBOHOGAR

**Principios de diseño:**

1. **Automation-ready**: slots claros que `/content-draft` puede rellenar
2. **Mobile-first**: 600px max, 14-16px body, single-column, touch targets 44px
3. **Consistencia visual**: misma estructura = lectores saben qué esperar
4. **Anti-slop**: personalidad > perfección. Voz ROBOHOGAR visible
5. **Escalable**: añadir secciones o tipos sin rediseñar

**Templates a crear/iterar:**

> **Consolidación 2026-04-18:** los templates por tipo de la tabla inferior se han unificado en un único master: `content/templates/articulo-beehiiv-master.html` (exportado desde el review Samsung Jet Bot Steam Ultra, formato y CTAs más actualizados). Sirve para review, comparativa, editorial, guía y futura newsletter — la estructura interna se adapta variando bloques, no el esqueleto. Los templates antiguos (`review-comparativa-beehiiv-export.html`, `editorial-opinion-beehiiv-export.html`, `review-comparativa.md`) se archivaron en `content/templates/_archive/`. La tabla abajo se conserva como histórico de la iteración original.

| Template | Archivo | Tipo | Status |
|---|---|---|---|
| Review/Comparativa | `content/templates/review-comparativa.md` | 70% — productos | ✅ Consolidado en master |
| Newsletter Issue | `content/templates/newsletter-issue.md` | Email semanal | ✅ Cubierto por master |
| Noticias/Roundup | `content/templates/noticias-roundup.md` | Noticias curadas | ✅ Cubierto por master |
| Editorial/Opinión | `content/templates/editorial-opinion.md` | 30% — futuro | ✅ Consolidado en master |

**Proceso por template (7 pasos):**

1. Investigar 3+ ejemplos reales del mismo tipo
2. Diseñar estructura (secciones, headings, slots)
3. Definir frontmatter (campos YAML para `/content-draft`)
4. Crear checklist pre-publicación
5. Probar en Beehiiv (post de prueba + mobile preview)
6. Iterar según cómo se ve publicado
7. Documentar versión final con ejemplos

**Template 1: Review/Comparativa (✅ COMPLETADO — TEMPLATE MAESTRO)**

Este template es la referencia visual para TODOS los demás. Tiene el formato definitivo de Beehiiv: fuentes, colores, espaciado, CTAs, estructura de bloques. Los templates 2-4 se ADAPTAN a partir de este, no se crean de cero.

- [x] Revisar estructura vs patrones de referentes
- [x] Verificar slots de frontmatter para `/content-draft`
- [x] Ajustar tabla comparativa → 4 columnas (Producto/Precio/Lo clave/Nota ⭐)
- [x] Probar en Beehiiv con post de prueba, verificar mobile
- [x] Finalizar checklist (22 puntos)

**Template 2: Newsletter Issue ⏸️ diferido a 30-50 subs**
> Se creará cuando se active la newsletter semanal (FASE 9 baseline). Con 0 subs no hace falta.
- [ ] Crear `content/templates/newsletter-issue.md`
- [ ] Copiar estilos base del template Review/Comparativa (fuentes, colores, CTAs, espaciado)
- [ ] Estructura: 5 secciones + frontmatter + pre-send checklist

**Template 3: Noticias/Roundup ⏸️ diferido / probablemente descatalogado**
> Los editoriales individuales con ángulo ya cubren este formato (ej. artículos #3 NEO y #4 comparativa humanoides). Revisar en FASE 6 si hay demanda real.
- [ ] Crear `content/templates/noticias-roundup.md` (solo si se decide mantenerlo)

**Template 4: Editorial/Opinión ⏸️ diferido**
> Los artículos editoriales publicados (#1, #3) usan el template Review adaptado y funciona. Crear plantilla dedicada solo si la repetición lo justifica.
- [ ] Crear `content/templates/editorial-opinion.md` (si se decide)

### Template visual de email en Beehiiv ⏸️ diferido

> Se configura cuando se active la newsletter semanal (30-50 subs). Con `Email and web` los artículos ya salen con el template visual heredado de Beehiiv.

- [ ] Configurar en **Settings → Email → Default Template**
- [ ] Header: `newsletter-header.png` (ya generado)
- [ ] Colores: fondo #FFFFFF, texto #0C0C0C, CTAs #F5A623
- [ ] Footer: social links + unsubscribe
- [ ] Verificar dark mode y mobile
- [ ] Enviar test email a personal

### Limpiar

- [x] Eliminar repos clonados temporales
- [x] Commit con cambios de conocimiento base

---

## FASE 2: Contenido Base (semana 1-2)

### Crear template Review/Comparativa en Beehiiv

- [x] Template creado directamente en Beehiiv (Design Mode)
- [x] HTML exportado: `content/templates/review-comparativa-beehiiv.html`
- [x] Template .md actualizado: `content/templates/review-comparativa.md`
- [x] Template HTML de output: `content/templates/review-comparativa-output.html`
- [x] Voz de marca documentada: `docs/brand-voice.md`
- [x] Verificado en mobile preview

**Estructura final del template (43 bloques):** ver tabla completa en `review-comparativa.md`

---

### Workflow por artículo (aplica a todos)

1. **Claude** genera research + borrador HTML → `content/articulos/<slug>/borrador.html`
2. **Rafael** copia secciones del HTML a Beehiiv bloque por bloque
3. **Rafael** edita con su voz, añade imágenes de producto (fotos fabricante)
4. **Claude** genera hero image con `/nano-banana` (square o landscape) → sirve para artículo + thumbnail + OG/SEO. Verificar en opengraph.xyz tras publicar
5. **Rafael** configura en Beehiiv (ver settings abajo)
6. **Rafael** revisa checklist pre-publicación (`content/templates/review-comparativa.md`)
7. **Publicar** → actualizar Welcome Email con URL real → mover borrador a `content/published/`

### Settings de publicación en Beehiiv

| Setting | Valor | Notas |
|---------|-------|-------|
| **Publish to** | `Email and web` | Artículos = email + web (SEO + inbox). Newsletter semanal = `Email only` |
| **Post URL** | `<slug>` definido en SEO del artículo | Siempre corto, sin stop words |
| **Post thumbnail** | Subir `thumbnail-<slug>.png` (16:9) | Aparece en landing, cards, OG, Google |
| **Show thumbnail on top** | ✅ Activado | La hero se muestra dentro del artículo |
| **Advanced email capture** | `Content Gate` | Primeros párrafos gratis, luego pide email |
| **Comments** | Activados | Engagement + señales SEO |
| **Meta title** | Copiar del frontmatter del borrador | Max 60 chars |
| **Meta description** | Copiar del frontmatter del borrador | Max 155 chars, con CTA implícito |

---

### Artículo 0: "Robots de escritorio con IA: cuál merece tu dinero (y cuál es humo)"

| Campo | Valor |
|-------|-------|
| SEO Title | `Mejor robot asistente IA escritorio 2026 — Comparativa honesta` |
| Meta description | `Eilik, EMO, LOOI, Loona y Vector: los comparamos sin filtro. Cuál vale la pena, cuál es hype y cuál es tirar el dinero.` |
| Slug | `mejor-robot-asistente-ia-2026` |
| Tags | `Asistentes IA`, `Robot Mascotas` |
| Tipo | Review/Comparativa |
| Borrador | `content/articulos/mejor-robot-asistente-ia-2026/borrador.html` |

**Productos:** Eilik (~140€), LOOI (~160-190€), Loona (~500€). No recomendados: EMO Go Home, Vector 2.0, Miko 3.

- [x] Research completado
- [x] Borrador HTML generado
- [x] Copiar a Beehiiv + editar voz
- [x] Hero image generada
- [x] SEO configurado en Beehiiv
- [x] Publicado → https://robohogar.com/p/mejor-robot-asistente-ia-2026
- [x] Welcome Email configurado y activado (ver sección abajo)

---

### Artículo 1: "Humanoides en casa: ¿cuánto falta de verdad?"

| Campo | Valor |
|-------|-------|
| SEO Title | `Humanoides en casa 2026 — ¿Cuánto falta de verdad?` |
| Meta description | `Ya puedes comprar un robot humanoide por el precio de un coche usado. El problema: no sabe limpiar tu baño. Investigamos todos los de 2026.` |
| Slug | `humanoides-en-casa-cuanto-falta` |
| Tags | `Humanoides`, `Opinión` |
| Tipo | Editorial/Opinión (30% — construye marca) |
| Borrador | `content/articulos/humanoides-en-casa-cuanto-falta/borrador.html` |
| Template | Adaptado de Review/Comparativa (base para template Editorial) |

**Robots cubiertos:** Tesla Optimus, Figure 03, Boston Dynamics Atlas, Xpeng Iron, 1X NEO, Unitree G1.

- [x] Research completado (fuentes actualizadas en fuentes-por-categoria.md)
- [x] Borrador HTML generado
- [x] Rafael edita voz + decide imágenes inline
- [x] Crear template Editorial en Beehiiv basado en este borrador
- [x] Hero image con `/nano-banana` (v10 elegida — "Creación de Adán")
- [x] SEO configurado en Beehiiv
- [x] Publicado → https://robohogar.com/p/humanoides-en-casa-cuanto-falta

---

### Welcome Flow (MVP 2 emails — configurar cuando el primer lead magnet esté listo)

> ⚠️ **Actualizado 2026-04-18:** este bloque está **obsoleto** y se reemplaza por el MVP de 2 emails documentado en **[`welcome-flow-setup.md`](welcome-flow-setup.md)**. Razón: la versión original asumía plan Beehiiv free (1 solo welcome email sin automations); ROBOHOGAR ahora corre en plan Scale (desde 2026-04-18), que permite workflows con delay y segmentación.
>
> **Frase trigger para retomar el setup nuevo:** *"Retomamos welcome-flow — empezamos configuración Beehiiv"*.
>
> El bloque de abajo queda como **referencia histórica** del welcome single-email que se configuró inicialmente. No re-usar.

---

#### 📜 (Histórico) Welcome Email versión Free plan

> El Welcome Email es lo primero que recibe alguien al suscribirse.
> **50-55% de open rate** — el doble que un email normal. Es tu mejor oportunidad de causar buena impresión.
> Según el playbook: pedir reply (señal #1 para Gmail Primary) + pedir mover a bandeja principal.

**Paso 1** — Ir a **Automations** en el menú lateral de Beehiiv

**Paso 2** — Buscar **Welcome Email** (Beehiiv lo tiene como automatización predeterminada). Click en **Edit**

**Paso 3** — Configurar cabeceras:

| Campo | Valor |
|-------|-------|
| Subject | `🤖 Bienvenido/a a ROBOHOGAR` |
| Preview text | `Tu dosis semanal empieza aquí` |
| Sender name | `Rafael de ROBOHOGAR` |
| Reply-to | `hola@robohogar.com` |

> **Por qué este subject:** claridad > curiosity en welcome (open rate ya es ~50% por contexto). El emoji al inicio da reconocimiento de marca en inbox.

**Paso 4** — Pegar este contenido en el editor (copy-paste). Usa negritas/cursivas donde marca `**texto**` / `*texto*`:

```
¡Hola!

Soy Rafael, y esto es **ROBOHOGAR** — tu dosis semanal de robótica doméstica.

Cada martes, en tu bandeja, 3 bloques fijos:

🤖 **Análisis** · Lo que pasa esta semana
🔍 **Reviews** · Robots reales, sin filtro
📖 **Ficciones** · El hogar de 2035

*El bloque de Ficciones aparece cada 3-4 semanas; el resto va cada martes.*

Todo gratis, en español y sin tecnicismos.

---

**Antes de nada:** arrastra este email a tu bandeja "Principal" — así los próximos martes llegan bien y no a Promociones.

---

**Mientras esperas al martes, empieza por aquí:**

→ [Robots de escritorio con IA: cuál merece tu dinero (y cuál es humo)](https://robohogar.com/p/mejor-robot-asistente-ia-2026)

→ [Humanoides en casa: ¿cuánto falta de verdad?](https://robohogar.com/p/humanoides-en-casa-cuanto-falta)

---

Un saludo robótico,
**Rafael**
ROBOHOGAR

*P.D. Si tienes un robot en casa y te apetece contármelo, respóndeme con el modelo. Leo todos los emails — aunque no siempre contesto el mismo día.*
```

**Paso 5** — Verificar:

- [ ] Subject empieza con 🤖 y dice "Bienvenido/a a ROBOHOGAR"
- [ ] Preview text incluye la palabra "semanal"
- [ ] Sender name = "Rafael de ROBOHOGAR"
- [ ] Reply-to apunta a `hola@robohogar.com` (no a bakalap2@gmail.com)
- [ ] Los 2 links a artículos funcionan
- [ ] Los iconos 🤖 🔍 📖 se ven bien en la preview móvil (375px)

**Paso 6** — Pulsar **Save & Activate**

**Paso 7** — Probar: suscríbete con un email alternativo y verifica que llega. Responde con "Roborock" para chequear que el reply entra.

> **⚠️ Nota sobre los 2 enlaces a artículos:** NO uses el bloque **Button** para los artículos — un botón transmite "acción" (comprar, suscribirse), no "lee esto". Usa **una de estas dos opciones**:
>
> **Opción A — Bloque "Embed Link"**
> `+` → **Embed Link** → pega la URL del artículo (`https://robohogar.com/p/slug`). Beehiiv hace auto-unfurl y genera card con hero image + título + meta description (como LinkedIn/Twitter unfurl). Depende de que los meta tags del artículo estén bien configurados.
>
> **Opción B — Estructura magazine-style con bloques nativos** (funciona siempre)
> Construye cada "card" manualmente con los bloques que Beehiiv free tiene:
> ```
> [Heading 5]     📖 ARTÍCULO · 8 min       ← pequeño, gris, uppercase
>
> [Heading 3]     Robots de escritorio con IA:
>                 cuál merece tu dinero (y cuál es humo)
>
> [Párrafo]       Guía honesta de los 5 modelos que ya puedes
>                 comprar y cuál encaja con cada presupuesto.
>
> [Párrafo]       Leer en ROBOHOGAR →       ← texto ámbar + bold, hyperlink
>
> [Content Break]                            ← separador antes del siguiente
> ```
> Más sobrio, estilo editorial. Sin botón, sin card fake.
>
> **Tiempos de lectura:** deben ser realistas y distintos por artículo. Calcula: palabras totales ÷ 200 (≈ lectura media español).

---

### Redes sociales ✅ pivote a FASE 4B (18-abr-2026)

> **Plan original superado.** La cadencia IG + LinkedIn + WhatsApp asumía exposición personal de Rafael y cuentas activas. Hoy el motor de crecimiento inicial son canales sin exposición (Reddit, Menéame, Beehiiv Boosts). Ver [FASE 4B](#fase-4b-distribución-activa-0-50-subs). Los pasos de abajo quedan como referencia por si en FASE 8 (>50 subs) se abre IG/LinkedIn orgánico.

**Instagram ⏸️ diferido a FASE 8**

- [x] ~~Crear cuenta `robohogar_es` · foto de perfil mascota · bio~~

**LinkedIn ⏸️ diferido a FASE 8**

- [x] ~~Añadir headline · publicar post de lanzamiento~~

**WhatsApp Channel ⏸️ diferido a FASE 8**

- [x] ~~Crear Channel ROBOHOGAR 🤖~~

**Buffer ⏸️ diferido a FASE 8**

- [x] ~~Registrarse en buffer.com · conectar IG + LinkedIn · horarios~~

**Canva Brand Kit ⏸️ diferido a FASE 8**

- [x] ~~Registrarse en canva.com · Brand Kit con mascota + colores~~

---

### Monetización y legal (configurar ANTES de crear más contenido)

**Amazon Afiliados España** ⏳ PENDIENTE — registrarse cuando haya tráfico y artículos con enlaces de producto

- [ ] Registrarse en afiliados.amazon.es (necesitas NIF + IBAN personal, no hace falta empresa)
- [ ] Website → `robohogar.com`
- [ ] Categorías → Electrónica, Hogar
- [ ] Insertar tag de afiliado en los links de Amazon de los artículos

> ⚠️ Tienes **180 días** para generar al menos 1 venta. No registrarse sin audiencia. Comisiones: 3-7%. Cookie: 24h (89 días si añade al carrito).

**Páginas legales (obligatorias por ley española para cualquier web)**

Paso a paso en Beehiiv:

1. Ve a **Settings** (rueda dentada) → **Website** → busca la sección **Pages**
2. Pulsa **Add Page** (o **New Page**)
3. Crea cada página rellenando título, slug y contenido como se indica abajo

**Página 1: Aviso Legal**

- [ ] Título: `Aviso Legal`
- [ ] Slug: `aviso-legal` (la URL será robohogar.com/aviso-legal)
- [ ] Contenido a poner:

```
AVISO LEGAL

Titular: Rafael [tu apellido]
NIF: [tu DNI]
Email de contacto: robohogar@gmail.com
Dominio: robohogar.com

Este sitio web es un proyecto personal de divulgación sobre robótica doméstica.
El contenido publicado refleja opiniones personales del autor.
Los enlaces a productos pueden incluir enlaces de afiliado (Amazon Afiliados).
```

**Página 2: Política de Privacidad**

- [ ] Título: `Política de Privacidad`
- [ ] Slug: `privacidad` (la URL será robohogar.com/privacidad)
- [ ] Contenido a poner:

```
POLÍTICA DE PRIVACIDAD

Responsable: Rafael [tu apellido]
Email: robohogar@gmail.com
Finalidad: Envío de newsletter semanal sobre robótica doméstica
Legitimación: Consentimiento del interesado (doble opt-in)
Datos recogidos: Email
Destinatarios: Beehiiv Inc. (proveedor de email marketing, EEUU,
               sujeto a cláusulas contractuales tipo UE)
Conservación: Mientras mantengas tu suscripción activa
Derechos: Puedes acceder, rectificar o eliminar tus datos
          escribiendo a robohogar@gmail.com
          Puedes darte de baja en cualquier momento desde
          el enlace en cada email

Última actualización: abril 2026
```

**Añadir links en el footer**

- [ ] Ve a **Settings** → **Website** → sección de diseño/footer
- [ ] Añade enlaces a `/aviso-legal` y `/privacidad` en el pie de página

**Picos de conversión (marcar en calendario)**

- [ ] Prime Day (julio) → comparativas 1-2 semanas antes
- [ ] Black Friday (noviembre) → actualizar precios día del evento
- [ ] Navidad (diciembre) → "Guía de regalos tech: robots para casa"

---

### Artículo 1: "¿Qué robot aspirador compro en 2026?"

| Campo | Valor |
|-------|-------|
| SEO Title | `Mejor robot aspirador 2026 — Guía de compra honesta` |
| Meta description | `Comparativa de los mejores robots aspiradores de 2026. Sin publi, sin hype — solo cuál merece tu dinero según uso y presupuesto.` |
| Slug | `mejor-robot-aspirador-2026` |
| Tags | `Aspiradores` |
| Tipo | Review/Comparativa |

- [ ] Research
- [ ] Borrador HTML
- [ ] Copiar a Beehiiv + editar
- [ ] Hero image
- [ ] Publicado

### Artículo 2: "5 robots humanoides que llegarán a tu casa" ✅ superado (18-abr-2026)

> **Descatalogado.** Este ángulo editorial ya se cubrió en dos artículos publicados con enfoques más actuales:
> - #1 *[Humanoides en casa: ¿cuánto falta de verdad?](https://robohogar.com/p/humanoides-en-casa-cuanto-falta)* (editorial, 2026-04-15)
> - #4 *[Humanoides domésticos 2026: los 7 que puedes comprar o reservar](https://robohogar.com/p/humanoides-domesticos-2026-comparativa)* (comparativa, 2026-04-17)
>
> Slug original `robots-humanoides-casa-2030` no se usará.

- [x] ~~Research · Borrador · Beehiiv · Hero · Publicado~~

### Artículo 3: "Mi experiencia con robots en casa"

| Campo | Valor |
|-------|-------|
| SEO Title | `Convivir con robots en casa — experiencia real` |
| Meta description | `Llevo años con robots en casa. Te cuento qué funciona, qué no, y qué cambiaría si empezara de cero.` |
| Slug | `experiencia-robots-casa` |
| Tags | `Opinión` |
| Tipo | Personal — sin afiliados, sin gating. Construye confianza |

- [ ] Borrador (Rafael escribe, Claude apoya)
- [ ] Copiar a Beehiiv + editar
- [ ] Hero image
- [ ] Publicado

---

## FASE 3: Obsidian Knowledge Base (✅ COMPLETADA)

> Estructura de carpetas, templates y wiki creados. Claude Code mantiene el vault automáticamente via `/obsidian-robohogar` (wiki-update, sync-published, etc.). No se necesitan plugins de Obsidian — la automatización la hace Claude Code.

### Estado actual

- [x] Carpetas creadas en el vault (Research, Wiki/Robots, Wiki/Empresas, Templates, etc.)
- [x] 2 templates activos (Robot Wiki, Empresa Wiki). Los demás (Research Digest, Article Draft, Editorial Calendar, Issue) se borraron — el workflow real usa HTML exports directamente
- [x] 11 fichas de robots + 11 fichas de empresas creadas
- [x] Guía de implementación sincronizada
- [x] Plugins de Obsidian: **no necesarios** — Claude Code gestiona creación de notas y sincronización

### Notas sobre templates antiguos

Los templates de Research Digest, Article Draft y Editorial Calendar que existían en `05-Templates/` se eliminaron. El workflow real usa los skills de Claude Code:

- **Research digest** → `/research-digest` genera `content/drafts/research-digest-YYYY-MM-DD.md` y lo copia al vault (`Research/Research Digest YYYY-MM-DD.md`) automáticamente
- **Article draft** → `/content-draft` genera `content/articulos/<slug>/borrador.html` directamente (HTML, no markdown)
- **Editorial calendar** → `content/calendario-editorial.md` es fuente de verdad. Se sincroniza a `Calendario Editorial.md` del vault tras cada cambio
- **Robot / Empresa Wiki** → siguen vivos en `Templates/Template Robot Wiki.md` y `Template Empresa Wiki.md`. `/research-digest` crea fichas nuevas automáticamente cuando detecta robots/empresas sin nota

No se necesitan plugins de Obsidian (QuickAdd, Periodic Notes, Templater). Claude Code gestiona creación de notas y sincronización directamente.

---

## FASE 4: Ciclo de creación de contenido (modo actual)

> Estado actual: cadencia objetivo **1 artículo/semana** + **1 Ficción Doméstica cada 3-4 semanas**. La newsletter semanal se activa cuando haya 30-50 suscriptores (ver FASE 9). Mientras, todo el foco va a artículos + ficciones que construyen catálogo SEO y voz.

### Vista general del ciclo

```
  ┌───────────────────────────────┐
  │ LUNES — Digest (opcional)     │  /research-digest
  │ Scraping + semillas narrativas│  → drafts/research-digest-YYYY-MM-DD.md
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ LUNES/MARTES — Decidir tema   │  Backlog en calendario-editorial.md
  │ (leer digest, elegir del      │  - Backlog de artículos
  │ backlog, anotar ángulo)       │  - Backlog Ficciones Domésticas
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ MARTES/MIÉRCOLES — Borrador   │  /content-draft  (artículo)
  │ Genera HTML + hero + inlines  │  /ficcion-draft  (relato)
  │ (45-60 min de Claude)         │  /nano-banana    (hero, ejecuta automático)
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ MIÉRCOLES/JUEVES — Edición    │  Rafael (45-90 min)
  │ Añade voz, humor, opinión     │  Siguiendo rules/editorial.md + brand-voice.md
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ Copy-paste a Beehiiv + SEO    │  Manual (20-30 min)
  │ + hero + publicar             │  Settings según tabla FASE 2
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ POST-PUBLISH — Limpieza       │  /post-publish
  │ 14 pasos automáticos          │  (ver detalle abajo)
  └───────────────────────────────┘
               ↓
  ┌───────────────────────────────┐
  │ Social (cuando IG/LinkedIn    │  /social-content
  │  estén configurados)          │  → programar en Buffer
  └───────────────────────────────┘
```

---

### Paso a paso — Artículo semanal

**1. (Opcional) Actualizar research digest**

- [ ] Si han pasado >5 días desde el último digest → ejecutar `/research-digest`
- [ ] Revisar Top Stories y backlog de artículos actualizado
- [ ] Elegir tema del backlog (priorizar 🔥🔥🔥 o tendencias de temporada)

**2. Generar borrador**

- [ ] Ejecutar `/content-draft` indicando: tema, ángulo, tipo (Review/Editorial/Comparativa/Guía), slug
- [ ] El skill genera:
  - `content/articulos/<slug>/borrador.html` — HTML listo para Beehiiv
  - `content/articulos/<slug>/assets/` — hero (3 variantes: flash / landscape / 1K) + imágenes inline descargadas de fuentes
  - `content/articulos/<slug>/PASOS.md` — checklist específico de ese artículo con mapa visual

**3. Editar voz (Rafael)**

- [ ] Leer borrador completo
- [ ] Aplicar voz: plural editorial ("hemos investigado", "os contamos"), sin superlativos vacíos, opiniones propias
- [ ] Verificar contra `docs/brand-voice.md` y `rules/editorial.md`
- [ ] Ajustar títulos/H2 si hace falta (mobile-first: ≤40 chars en headlines)

**4. Publicar en Beehiiv**

- [ ] Seguir `PASOS.md` del artículo (contiene settings específicos + mapa visual del HTML)
- [ ] Settings según tabla FASE 2 (Publish to `Email and web`, Content Gate activo, etc.)
- [ ] Subir hero `.webp` (no el PNG original — ver FASE 5 rules/seo.md)
- [ ] Preview en mobile (375px) y desktop antes de enviar
- [ ] Publicar → capturar la URL definitiva

**5. Post-publish** (dar URL a Claude)

- [ ] Ejecutar `/post-publish <URL>` — ejecuta 14 pasos:
  1. Fetch URL + verificar OG image en opengraph.xyz
  2. Mover borrador a `content/published/YYYY-MM-DD-<slug>.html`
  3. Limpiar variantes de hero no usadas
  4. Actualizar `docs/guia-implementacion.md` (marcar artículo como publicado)
  5. Actualizar `content/registro-articulos.md` (OBLIGATORIO)
  6. Regenerar `content/llms.txt`
  7. Verificar `references/fuentes-por-categoria.md`
  8. Actualizar `assets/branding/asset-catalog.md`
  9. Actualizar templates HTML si el artículo añadió patrón nuevo
  10. Sugerir actualización del Welcome Email (si el artículo es mejor que los actuales)
  11. Generar contenido social preliminar (opcional)
  12. Sincronizar al vault Obsidian (published + registro)
  13. Commit + push
  14. Reportar resumen final

**6. Social (opcional, cuando redes estén configuradas)**

- [ ] `/social-content` — genera posts adaptados a LinkedIn, X, IG, WhatsApp
- [ ] Revisar y editar tono si hace falta
- [ ] Programar en Buffer

---

### Paso a paso — Ficción Doméstica (cada 3-4 semanas)

> Pilar experimental — ~10% del content mix. Relatos cortos de ciencia ficción doméstica próxima (2030-2040) con personajes recurrentes. Voz narrativa distinta (3ª persona omnisciente o 1ª persona del personaje POV — ver `rules/editorial.md` § Narrativa especulativa).

**1. Elegir semilla**

- [ ] Ver `content/calendario-editorial.md` → sección "Backlog Ficciones Domésticas"
- [ ] `/research-digest` rellena este backlog cada ejecución (paso 8b del skill)
- [ ] Cada semilla tiene: gancho + **dato real ancla** (obligatorio) + **villano humano** + personajes tipo + formato sugerido

**2. Generar borrador**

- [ ] Ejecutar `/ficcion-draft` — si no pasas argumentos, el skill lee el backlog y propone 3 opciones
- [ ] Elegir longitud: `flash` (500-1.000) · `corto` (1.500-3.000) · `mini-serie-episodio` (1.500-3.000 + hooks)
- [ ] El skill usa character bible de `content/ficciones/` para mantener continuidad entre episodios
- [ ] Output: `content/ficciones/<serie>/YYYY-MM-DD-<slug>.md` + PASOS.md

**3. Editar (Rafael)**

- [ ] Revisar voz narrativa (distinta del tono baseline — aquí SÍ permitidos superlativos en diálogo irónico)
- [ ] Verificar dato real ancla sigue presente y visible
- [ ] Confirmar villano humano (no el robot)

**4. Publicar**

- [ ] Beehiiv `Publish to: Email and web` con **tag dedicado "Ficciones Domésticas"**
- [ ] Hero estilo still cinematográfico (NO product-hero)
- [ ] Referencia visual: Black Mirror doméstico, After Yang, Her

**5. Post-publish**

- [ ] `/post-publish <URL>` funciona igual que para artículos (detecta el tipo automáticamente)

> **Piloto recomendado antes de comprometer mini-serie:** 3 flash de 800 palabras en 3 semanas consecutivas. Si engagement sube >10% → comprometer mini-serie. Si neutral → mantener rotativa. Si negativo → archivar la serie.

---

### Artículos pendientes del backlog (prioritarios)

> Fuente de verdad: `content/calendario-editorial.md`. Esta tabla es snapshot — actualizarla manualmente desactualiza el calendario. **Consultar el calendario, no esta tabla.**

Snapshot 2026-04-17 de artículos **🔥🔥🔥 Alta**:

- 1X NEO va a fábricas: contradicción del "robot doméstico" (editorial)
- UniX AI Panther: primer humanoide en hogares reales (editorial)
- Neura 4NE-1 Porsche Design €98k: la respuesta europea (editorial)
- Robots aspirador que suben escaleras (3 enfoques) (editorial)
- Humanoides domésticos 2026: los 7 que puedes comprar/reservar (comparativa)
- Sunday Memo: el anti-humanoide de $1.150M (editorial)
- Apple entra en robótica doméstica (editorial)

### Semillas de Ficciones Domésticas (pendientes)

Snapshot 2026-04-17 — 4 semillas en backlog:

- 🥇 "El operador nocturno" — teleop NEO + deal EQT (corto o mini-serie 3 eps)
- 🥇 "El guante" — Sunday Skill Capture + cuidadora con alzhéimer (corto)
- "Los del 4ºA" — F2 piloto China + brecha robótica en edificio (flash)
- "El manual del inspector" — AI Act inspectora EU (corto o mini-serie procedural)

---

### Newsletter (diferida)

La newsletter semanal se activa cuando haya **30-50 suscriptores** (ver FASE 9). Mientras tanto:

- Cada artículo publicado `Email and web` YA va a los suscriptores actuales como email (no hace falta newsletter aparte)
- El Welcome Email cubre la primera impresión
- El espacio "newsletter semanal curada" se añadirá cuando la masa crítica justifique otra cadencia

---

## FASE 4B: Sprint Evergreen SEO (antes "Distribución activa")

> **Pivote 2026-04-20.** Esta fase se llamaba "Distribución activa (0-50 subs)" y el motor era Reddit + Menéame + Beehiiv Boosts. Tras la sesión de scouting del 2026-04-20 (5 descartes consecutivos en Reddit + Xataka sin comentarios + Forocoches por invitación + sin Facebook) + confirmación de Rafael de que no va a construir cuentas ES con karma, el motor cambia a **SEO evergreen compuesto**: publicar 14 evergreens priorizados durante los próximos ~4 meses, dejar que Google los indexe y que el tráfico llegue entre mes 6 y mes 18. Los tangibles descargables (FASE 4C) capturan la conversión de ese tráfico.
>
> **La FASE 4B antigua ("Reddit + Menéame + Beehiiv Boosts") queda cerrada indefinidamente** (archivada al final de esta sección como referencia histórica). No hay plan B de outreach manual. Única válvula de aceleración no-manual futura: **Beehiiv Boosts** pagado cuando el cluster SEO esté maduro. Detalle del pivote: memoria `feedback_seo_first_pivote.md`.

### 📌 Frases trigger para retomar en futuras sesiones

| Qué quiero retomar | Frase exacta |
|---|---|
| Empezar siguiente evergreen del backlog | **"Retomamos evergreen — siguiente del backlog"** |
| Elegir uno concreto por número | **"Evergreen E1"** / **"Evergreen E13"** (reemplaza el N por el del backlog) |
| Ver estado del sprint evergreen | **"¿Cómo va el sprint evergreen?"** |
| Evaluar si toca ficción esta semana | **"¿Toca ficción? ¿Evergreen de la semana cerrado?"** |

### Activación

**Activada 2026-04-20** tras pivote. Corre en paralelo a FASE 4C (tangibles) y reemplaza el motor de crecimiento de la FASE 4B original.

### Operativa del sprint

#### Ritmo semanal

1. **Lunes:** elegir evergreen del backlog E1-E14 ([calendario-editorial.md § Backlog Evergreen SEO](../content/calendario-editorial.md)). Priorizar estacional-en-ventana (E1 cortacésped, E12 ROI cortacésped en primavera-verano) sobre no-estacional. Si ya cerraste el estacional, ir al siguiente "Alta".
2. **Martes-jueves:** `/content-draft <tema E<N>>`. El skill lee el Elements of Value + fuentes ES + filtros mercado ES y genera el borrador HTML con hero + 3 variantes.
3. **Viernes:** revisión de Rafael + publicar con `Email and web` + `/post-publish <URL>`. Ratio 3:1 garantizado si este flujo se repite 4 semanas seguidas.
4. **Opcional Sábado:** `/ficcion-draft` si el evergreen está entregado. Si no, slot libre.

#### Checklist SEO on-page por evergreen (mínimo obligatorio)

- [ ] Title tag ≤55 chars con keyword primaria al principio
- [ ] Meta description 110-155 chars con tangible mencionado con cifra
- [ ] H1 con keyword primaria, H2/H3 con variaciones semánticas y long-tail
- [ ] URL slug corto con keyword (sin stop words)
- [ ] Mínimo **2-3 enlaces internos** a otros artículos ROBOHOGAR (fuerza el cluster temático — regla clave de autoridad de dominio)
- [ ] Alt text descriptivo en todas las imágenes, con keyword natural
- [ ] Hero image: WebP <500KB, 1200x630 OG-compatible
- [ ] **Tangible acoplado:** banner Hoja de Compra (si aspirador/cortacésped/fregasuelos/limpia-cristales) o tangible específico del evergreen
- [ ] Subtítulo + meta description mencionan el tangible con cifra (regla `tangibles.md`)

Los skills `/content-draft` y `/post-publish` ya aplican la mayoría de estos puntos; este checklist es la verificación manual antes de publicar.

#### Regla del ratio 3:1

Cada 4 artículos publicados deben ser **3 evergreens + 1 reactivo** como máximo. Los reactivos (editoriales sobre noticias con caducidad <3 meses — NEO fábricas, humanoide maratón, AI Act) son tentadores por actualidad pero **no traen tráfico orgánico sostenido**: pico 1-2 semanas, luego cae a 0. Solo se escriben cuando el evergreen de la semana está entregado y hay una noticia fuerte que pide respuesta editorial.

#### Ficción condicionada a evergreen-first

Ficciones Domésticas se publican **hasta 1 cada 1-2 semanas, solo si el evergreen de la semana está cerrado**. Si falta el evergreen, no hay ficción esa semana. Regla dura post-pivote 2026-04-20.

### Qué NO hacer en esta fase

- ❌ **Outreach manual** en Reddit / Menéame / foros / Xataka comments. **Cerrado indefinidamente.** Rafael confirmó 2026-04-20 que no construye cuentas con karma ES — sin ese prerrequisito, cualquier outreach es shadowban garantizado. Esta vía queda descartada como motor; no es una pausa.
- ❌ **Autopromoción con cuentas sin historial** — shadowban garantizado.
- ❌ **Comprar listas de emails** (deliverability destruida en semanas).
- ❌ **Pedir a amigos que se suscriban por compromiso** (open rate → 5%, Gmail manda todo a Promotions).
- ❌ **Romper el ratio 3:1** escribiendo 2 reactivos seguidos porque "hay noticia fuerte". Siempre evergreen primero.
- ❌ **Pagar Beehiiv Boosts ahora** — sin tangible robusto y sin cluster SEO, los subs adquiridos hacen churn. Es la única válvula de aceleración no-manual disponible a futuro, pero reevaluar solo cuando haya ≥10 evergreens publicados + 2-3 tangibles + welcome flow validado.

### Indicadores de salud del sprint (orientativos, NO cortes automáticos)

| Horizonte | Evergreens acumulados | Tráfico orgánico esperado | Subs orgánicos |
|---|---|---|---|
| Semana 1-4 | 2-3 (E1 + E2 o E3) | 0-50 visitas/mes | 0-2 |
| Mes 2-3 | 5-8 | 100-300 | 3-10 |
| Mes 4-6 | 10-14 (backlog cerrado) | 500-2.000 | 15-60 |

Si al final del mes 6 el tráfico está muy por debajo (< 100/mes con 10+ evergreens publicados), diagnóstico: competencia SEO demasiado alta para el dominio (sin backlinks), keywords mal elegidas o contenido sin intención compra suficiente. En ese caso Rafael decide si pivotar el nicho (p.ej. long-tail aún más específico), construir backlinks (difícil sin outreach), o pausar. **Decisión humana, no automática.**

---

### 🗃️ FASE 4B antigua (archivada 2026-04-20, cerrada indefinidamente) — Reddit + Menéame + Beehiiv Boosts

> Queda como referencia histórica. Rafael confirmó 2026-04-20 que no va a construir cuentas ES con karma previo — la playbook original **no se va a reactivar**. Si en el futuro cambia de opinión, será caso-por-caso, no como sprint completo. Mientras tanto, NO seguir esta playbook.

- ~~**4B.1 Reddit:** r/espana, r/AskSpain, r/podemos_ahorrar — buscar hilos de pregunta, responder con valor 80-150 palabras, enlazar como contexto de apoyo. Cadencia 5-10 respuestas/semana.~~ **Pausado:** captcha anti-bot impide scraping; sesión 2026-04-20 con 5 descartes consecutivos (3 LATAM fuera scope, 2 subs EN, 1 bloqueado).
- ~~**4B.2 Foros en español:** foro.xataka, forocoches, forobeta.~~ **Pausado:** Xataka sin comentarios activos, Forocoches por invitación.
- ~~**4B.3 Menéame:** submitear 1 de cada 3-4 artículos como editorial ángulo controversia.~~ **Pausado hasta karma suficiente:** submit de propia web con cuenta nueva = shadowban.
- ~~**4B.4 Beehiiv Boosts:** €20 piloto.~~ **Pospuesto:** sin cluster SEO ni welcome validado, los subs adquiridos no retienen.
- ~~**4B.5 Cross-promo newsletters hermanos.**~~ **Pospuesto:** sin audiencia propia no hay swap recíproco viable.

---

## FASE 4C: Lead Magnet #1 + Sistema de tangibles

> **Principio editorial "Always ship a tangible":** cada pieza de contenido publicada incluye al menos 1 tangible descargable (checklist, tabla, cheatsheet, mini-poster, PDF). Modelo Write With AI aplicado a robótica doméstica — el lector siempre se lleva algo concreto. Plan detallado completo: [`C:/Users/cri-c/.claude/plans/crea-el-plan-sugerido-lazy-castle.md`](../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md)

### 📌 Frases trigger para retomar en futuras sesiones

Cuando Rafael vuelva a Claude Code después de días/semanas y quiera retomar esta fase, basta con decir:

| Qué quiero retomar | Frase exacta |
|---|---|
| Construir el skill `/pdf-brand` (FASE A) | **"Retomamos el plan lazy-castle — construimos el skill `/pdf-brand`"** |
| Generar el Lead Magnet #1 (FASE B, requiere skill construido antes) | **"Retomamos lazy-castle — generamos el lead magnet de 5 preguntas"** |
| Activar Content Gate + integraciones Beehiiv (FASE C) | **"Retomamos lazy-castle — activamos Content Gate y las integraciones Beehiiv"** |
| Ver estado actual del plan | **"¿En qué fase del plan lazy-castle estamos?"** |

Con esas frases, Claude debe:

1. Leer este bloque (FASE 4C) + el plan file [`crea-el-plan-sugerido-lazy-castle.md`](../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md)
2. Revisar qué checkboxes están marcados y cuáles no
3. Retomar en el primer paso pendiente de la fase solicitada

### Estado

Estado actual: **0 suscriptores · 0 lead magnets creados · sistema de tangibles por construir.** Objetivo: primer lead magnet activo + skill reutilizable + principio editorial documentado. Tiempo total: ~9h 30min Claude + ~2h 45min Rafael distribuibles en 2-3 sesiones.

### Catálogo de tangibles por tipo de contenido

Cada artículo/editorial/ficción que publique ROBOHOGAR genera su tangible asociado usando el skill `/pdf-brand` (pendiente de construir — ver FASE 5):

| Contenido | Tangible | +Esfuerzo | Variante skill |
|---|---|---|---|
| Review de producto | Checklist compra + specs 1-pager | +15 min | `cheatsheet` |
| Comparativa | Tabla comparativa PDF standalone | +15 min | `comparativa` |
| Editorial/Opinión | "3 datos clave" mini-dossier | +20 min | `cheatsheet` |
| Guía/How-to | Flowchart o checklist paso a paso | +25 min | `guia` |
| Ficción Doméstica | Mini-poster (ilustración + quote + dato real) | +30 min | `relato` |
| Newsletter (futuro) | Cheatsheet semanal "Lo esencial en 3 min" | +20 min | `cheatsheet` |

Regla de oro: si un tangible tarda >30 min, se simplifica o se omite.

### Cadencia de acumulación prevista

| Horizonte | Tangibles | Milestone |
|---|---|---|
| Mes 1 | 4-5 | Bootstrap (1/artículo + lead magnet inicial) |
| Mes 3 | ~15 | Activar sección pública "Descargas" en landing |
| Mes 6 | ~30 + 1 guía trimestral | Primer bundle temático |
| Mes 12 | ~55 + ebook | Masa crítica para all-access pass |

### Orden de ejecución (3 fases)

#### FASE A — Construir skill `/pdf-brand` (primero) — ~5-6h Claude + ~30 min Rafael

- [ ] Redactar `.claude/commands/pdf-brand.md` (workflow 6 pasos + modos `from-scratch` / `derived` / `bundle`)
- [ ] Diseñar `content/templates/pdf-brand-master.html` (layout maestro, 9 elementos de identidad visual blindada)
- [ ] Crear 4 variantes de template: `pdf-brand-guia.html`, `-comparativa.html`, `-glosario.html`, `-relato.html`
- [ ] Script `utilities/render-pdf.py` (Chrome headless HTML→PDF, literate code)
- [ ] Testing: generar 1 PDF de prueba por tipo (4 PDFs) y validar brand consistency
- [ ] Rafael valida diseño visualmente antes de pasar a FASE B

**Identidad visual blindada — 9 elementos combinados que hacen que el PDF sea inequívocamente de ROBOHOGAR:**

1. Header con monograma R (`assets/branding/master/robohogar-logo-monogram-v11.png`)
2. Mascota firma en esquina inferior derecha
3. Paleta 3-color estricta (#F5A623 · #0C0C0C · #FFFFFF)
4. Tipografía Jost (títulos) + DM Sans (cuerpo)
5. Numeración con "chip" ámbar redondeado — elemento signature
6. Separadores anchos de 2px (estilo editorial)
7. Watermark sutil del monograma al 5% opacity
8. Footer con tagline fija "robohogar.com · Tu dosis semanal de robótica doméstica"
9. Emoji-pilar consistente por tipo (Guía 🤖 · Comparativa 🔍 · Glosario 📖 · Relato 📖✨)

#### FASE B — Lead Magnet #1: "5 preguntas antes de comprar un robot aspirador" — ~1h 30min Claude + ~1h 15min Rafael

Alineado con [plan-v2.md:108](plan-v2.md#L108) (modelo "lazy lead magnets"). Standalone evergreen, 1 página A4.

- [ ] `/pdf-brand guia "5 preguntas antes de comprar un aspirador" 1-pagina guias-compra`
- [ ] Output esperado:
  - `content/lead-magnets/guias-compra/guia-5-preguntas-aspirador/guia.md` (markdown fuente)
  - `content/lead-magnets/guias-compra/guia-5-preguntas-aspirador/guia.html` (render)
  - `content/lead-magnets/guias-compra/guia-5-preguntas-aspirador/PASOS.md` (checklist publicación)
  - `assets/lead-magnets/guia-5-preguntas-aspirador-v1.pdf` (PDF final)
  - `assets/lead-magnets/guia-5-preguntas-aspirador-preview.webp` (social card 1200x630)
- [ ] Rafael edita voz del markdown
- [ ] Re-render PDF
- [ ] Añadir bloque CTA lead magnet en `content/templates/review-comparativa-beehiiv.html` (footer de artículos)
- [ ] Aplicar CTA actualizado a los 2 artículos ya publicados en Beehiiv

**Voz (respetando anti-patterns):**

- ❌ NO "honesta", "sin filtro", "guía definitiva"
- ❌ NO superlativos vacíos ("revolucionario", "increíble", "el mejor")
- ✅ Plural editorial ("hemos visto", "te proponemos")
- ✅ Bullets ≤40 chars, sin em-dashes en headlines
- ✅ Mobile-first (legible en 375px sin zoom)

**Título con beneficio concreto:** "5 preguntas que te ahorran 200 € al comprar un robot aspirador"

#### FASE C — Content Gate + integraciones Beehiiv — ~1h Rafael

- [ ] **Content Gate en Saros Z70** (15 min): Beehiiv → Posts → abrir review → insertar bloque Content Gate tras párrafo 3-4 → copy: título `Sigue leyendo gratis`, sub `Reviews y comparativas cada semana en tu bandeja`, botón `Suscribirse`
- [ ] **NO** gate-ar humanoides (editorial, gate-arlo reduce impacto del pilar 30% construye marca)
- [ ] **Welcome Email update** (15 min): añadir bloque con link al PDF arriba de los 2 artículos existentes
- [ ] **Landing page** (30 min): sección nueva entre hero y "Sobre qué escribimos" con background ámbar — copy: `Descarga gratis · 5 preguntas que te ahorran 200 € al comprar un robot aspirador` + form email + botón
- [ ] Configurar segmento `source:lead_magnet_01` en Beehiiv → Subscribers para tracking

### Métricas de éxito

Benchmark playbook ([email-marketing-playbook.md:68](../references/newsletter/email-marketing-playbook.md#L68)):

- Lead magnets: +384% signups
- Content Gate: 3-10% conversión del tráfico SEO
- CTA "Get my guide" > "Subscribe" (+33%)

Target ROBOHOGAR:

- Semana 1-2: 0 → 10 subs
- Mes 1: 10 → 30 subs
- Mes 3: 30 → 100 subs (milestone para activar newsletter semanal)

Si a las 4 semanas el magnet <1% conversión → iterar titular o probar otro magnet (testear 1/mes según [plan-v2.md:110](plan-v2.md#L110)).

### Bundles temáticos (mes 6+)

Cuando la biblioteca >20 items, empaquetar:

- "Aspiradores 2026" (checklists + comparativas)
- "Humanoides doméstico" (editoriales + glosarios + mini-posters ficción)
- "Cortacésped temporada primavera/verano"
- "Anuario ROBOHOGAR" (resumen + top tangibles del año)

Bundles = puente natural a **paid tier** cuando >2.500 subs (ver FASE 9). Free tier: tangibles individuales. Paid tier: bundles.

---

## FASE 4D: Biblioteca pública de tangibles (híbrida)

> **Principio:** resolver el dilema "gente ve todos los tangibles antes de suscribirse" SIN romper la conversión del gate. Modelo **híbrido** validado por Rafael 2026-04-20: página pública muestra portadas de todos los tangibles; descargar requiere suscripción (gate mantenido); opcional 1 "sampler" de 1 página sin gate como demo de calidad.

### 📌 Frases trigger

| Qué quiero retomar | Frase exacta |
|---|---|
| Empezar la biblioteca pública | **"Retomamos FASE 4D — biblioteca pública de tangibles"** |
| Añadir un tangible al grid | **"Añade <slug-tangible> a la biblioteca pública"** |
| Decidir sampler sin gate | **"Decidimos sampler gratuito de la biblioteca"** |

### Activación

Activar cuando haya **≥3 tangibles publicados**. Hoy (2026-04-20): 1 tangible (Hoja de Compra v2). Candidatos siguientes para alcanzar 3:

- Guía primer mes aspirador (formato "estrenando" del funnel)
- Decision tree cortacésped (acopla evergreen E1)
- Checklist "pelos y rodillos" (acopla evergreen E3 mascotas)

### Estructura híbrida

**1 · Página pública `robohogar.com/recursos`**

Grid con tarjeta por tangible:

```
Recursos ROBOHOGAR
Guías, checklists y comparativas para ayudarte a comprar mejor.

[Grid de cards · 1 por tangible]
 📄 Hoja de Compra — 5 preguntas antes de comprar cualquier robot · 2 páginas
    [Descargar gratis con la newsletter →]
 📊 Comparativa — 6 aspiradores 2026 por perfil · 1 página
    [Descargar gratis con la newsletter →]
 🌱 Decision tree — ¿Robot cortacésped o manual? · 1 página
    [Descargar gratis con la newsletter →]
 ...
```

**2 · Gate híbrido**

- **Por defecto:** cada CTA apunta a la Digital Product de Beehiiv correspondiente → suscripción requerida para descargar. Esto mantiene la conversión intacta.
- **Opcional (decidir cuando se active):** 1 tangible marcado como "sampler" con descarga directa sin gate. Ejemplo candidato: versión de 1 página de la Hoja de Compra. Actúa como demo de calidad.
- **No hacer:** todo sin gate (perderíamos el mecanismo principal de captura) ni todo con gate (perderíamos la utilidad del grid público).

**3 · Copy del CTA**

Usar la trust-line canónica ROBOHOGAR: `PDF gratis con tu suscripción semanal. Cancela cuando quieras.` (ver regla en `tangibles.md § Microcopy de conversión`).

### Implementación técnica

- **Plataforma:** página pública en Beehiiv (no requiere dev) o página HTML custom en `robohogar.com/recursos` si se quiere más control de diseño.
- **Assets reusables:** portadas PDF ya existen como WebP 1280×720 en cada `content/lead-magnets/<slug>/assets/`.
- **UTM por tarjeta:** `?utm_source=recursos&utm_medium=biblioteca&utm_campaign=<slug>` para trackear qué tangible atrae más tráfico.
- **Link en navbar principal:** añadir "Recursos" entre "Blog" y "Suscríbete" cuando se active.

### Bundles (evolución mes 6+)

Cuando la biblioteca >10 items, empaquetar subconjuntos por tema en la misma página con CTA único → ver sub-sección `Bundles temáticos (mes 6+)` arriba en FASE 4C.

---

## FASE 5: Automatización (estado actual)

### Principio

Automatizar TODO excepto juicio editorial y voz. Rafael decide QUÉ contar y CÓMO contarlo. Claude Code + skills hacen el resto.

### Estado del pipeline

```
┌─ SEMIAUTOMÁTICO via skills (operativo HOY) ────────────────────┐
│                                                                │
│  /research-digest   → digest + backlog + semillas narrativas  │
│  /content-draft     → borrador HTML + hero + inlines + PASOS  │
│  /ficcion-draft     → relato + character bible + hooks        │
│  /nano-banana       → imágenes branded (mascota/monograma)    │
│  /social-content    → posts LinkedIn/X/IG/WhatsApp            │
│  /post-publish      → 14 tareas de limpieza post-artículo     │
│  /obsidian-robohogar → sync vault + wiki + calendar + audit   │
│  /commit            → commits con formato estándar            │
│                                                                │
│  Input: Claude Code (CLI local) · Output: repo + vault        │
└────────────────────────────────────────────────────────────────┘
                           ↓
┌─ MANUAL (Rafael) ──────────────────────────────────────────────┐
│  - Elegir tema del backlog (~15 min)                          │
│  - Editar voz del borrador (~45-90 min)                       │
│  - Copy-paste a Beehiiv + configurar SEO (~20-30 min)         │
└────────────────────────────────────────────────────────────────┘
                           ↓
┌─ PENDIENTE de integrar (FASE 10) ──────────────────────────────┐
│  - Research aggregator script (RSS + cron)                    │
│  - Make.com (orquestación)                                    │
│  - Buffer (programación social)                               │
│  - Beehiiv MCP (crear drafts desde Claude)                    │
└────────────────────────────────────────────────────────────────┘
```

---

### Qué NO requiere nada más — ya funciona

| Workflow | Skill | Notas |
|---|---|---|
| Research semanal + backlog dual | `/research-digest` | Web search + WebFetch · escribe en repo + vault · extrae semillas narrativas · actualiza wiki robots/empresas |
| Borrador HTML artículo | `/content-draft` | Genera HTML + 3 variantes hero + imágenes inline descargadas + PASOS.md |
| Borrador ficción | `/ficcion-draft` | Lee backlog semillas · usa character bible · aplica Pixar/MRU/Paint-The-Villain |
| Imágenes branded | `/nano-banana` | Gemini API (Nano Banana) · cataloga en `asset-catalog.md` · nunca sobrescribe (versiona v2/v3) |
| Social posts | `/social-content` | Genera por plataforma desde artículo publicado |
| Post-publish (14 pasos) | `/post-publish` | Limpieza + registros + llms.txt + vault sync + commit |
| Vault management | `/obsidian-robohogar` | Subcomandos: `wiki-update`, `sync-published`, `calendar-update`, `audit`, `archive` |
| Git | `/commit` | Formato estándar + co-author + stage por nombre |

### Skills pendientes de construir

| Skill | Para qué | Prioridad | Detalle |
|---|---|---|---|
| `/pdf-brand` | Generar PDFs branded (guías, comparativas, glosarios, relatos, cheatsheets, ediciones especiales) con identidad ROBOHOGAR blindada | 🔥🔥🔥 Alta | Habilita el sistema de tangibles de FASE 4C. Modos: `from-scratch` · `derived` (desde artículo publicado) · `bundle` (compila varios PDFs). Tiempo construcción: ~5-6h Claude + ~30 min Rafael validación visual. Detalle completo en [plan crea-el-plan-sugerido-lazy-castle.md](../../.claude/plans/crea-el-plan-sugerido-lazy-castle.md) |

### Qué sigue siendo manual (y probablemente deba seguir siéndolo)

- **Juicio editorial:** elegir tema, ángulo, ordenar el backlog
- **Voz:** editar el borrador con humor, opinión, experiencias propias — es el activo de marca
- **Copy-paste a Beehiiv:** Beehiiv no tiene API de drafts en plan free. Todo bloque por bloque
- **Preview mobile/desktop:** validación visual antes de publicar
- **Decisión de hero final:** elegir entre las 3 variantes generadas

### Herramientas y costes actuales

| Herramienta | Función | Coste |
|---|---|---|
| Claude Code (CLI) | Ejecución de skills | — (incluido en plan Claude) |
| Gemini API (Nano Banana) | Generación de imágenes | $GEMINI_API_KEY en `.env` |
| Beehiiv free | Publicación + welcome email | 0€ (plan gratuito hasta 2.500 subs) |
| Namecheap | Dominio robohogar.com | ~10€/año |

**Coste actual:** ~10€/año + Nano Banana pay-per-use (~$0.04/imagen).
**Coste futuro con FASE 10:** +15€/mes (Make.com + Buffer) cuando volumen lo justifique.

---

### Cadencia operativa

**Ritmo actual (fase de construcción de catálogo):**

- 1 artículo/semana (objetivo)
- 1 Ficción Doméstica cada 3-4 semanas
- Digest: bajo demanda (antes de escribir si pasaron >5 días)
- Newsletter semanal: diferida (activar con 30-50 subs)

**Día típico de publicación (martes):**

- Lunes noche: `/research-digest` si no hay uno reciente
- Martes mañana: elegir tema + `/content-draft`
- Martes mediodía: editar voz
- Martes tarde: publicar en Beehiiv
- Martes noche: `/post-publish <URL>` → commit + push
- Miércoles: `/social-content` + programar Buffer (cuando esté conectado)

### Welcome Series (cuando plan de Beehiiv lo permita)

> Plan free de Beehiiv: solo Welcome + Reminder. Serie completa de 6 emails requiere plan Scale ($34/mes). Evaluar en FASE 9.

- [ ] **Email 1** (día 0): Bienvenida + mejor artículo + pedir reply → **✅ YA configurado**
- [ ] **Email 2** (día 1): Pregunta engagement "¿Qué robot tienes?" → **✅ YA configurado**
- [ ] **Email 3** (día 3): Editorial humanoides — construye marca
- [ ] **Email 4** (día 5): Guía de compra — valor práctico
- [ ] **Email 5** (día 10): Experiencia personal con robots — confianza
- [ ] **Email 6** (día 14): Resumen + CTA referral + preferencias
- [ ] Upgrade a Beehiiv Scale cuando revenue justifique el coste

---

## FASE 6: Métricas y Revisión

### 📊 SLOs por fase + trigger de optimización

Servicio mínimo por fase. Si se incumple 2 semanas seguidas → disparar trigger de optimización.

| Fase | Rango subs | SLO semanal | SLO mensual | Señal de escalado |
|---|---|---|---|---|
| **F1** (actual) | 0-50 | 1 artículo publicado · 1 post social si toca | 1 tangible PDF · 1 ficción quincenal | ≥30 subs → activar newsletter semanal |
| **F2** | 50-500 | 1 artículo · 1 newsletter · 3 posts social | 2 tangibles · 1 ficción | ≥200 subs → expandir welcome flow a 4 emails |
| **F3** | 500-5K | 2 artículos · 1 newsletter · 5 posts social | 3 tangibles · 2 ficciones · 1 ebook recopilatorio | ≥5K → activar paywall ROBOHOGAR+ |

#### ⚠️ Trigger de optimización

Si 2 semanas seguidas se incumple el SLO semanal **o** el open rate cae >20% vs baseline de las 4 semanas previas:

Frase trigger: ***"Trigger optimización ROBOHOGAR"***.

Claude corre esta checklist y propone 3 cambios concretos antes de seguir produciendo:

- [ ] Revisar titulares de los últimos 4 artículos (¿hay patrón común que pierda click?) contra `@references/writewithai/01-voz-y-estructura.md`
- [ ] Revisar subject lines de los 4 últimos envíos (¿cortos? ¿curiosos? ¿clickbait?) contra `@rules/newsletter.md § Subject Lines`
- [ ] Revisar CTA del lead-magnet en home + OG cards — ¿cifra en subtítulo? ¿banner visible? Contra `@rules/tangibles.md § Reglas operativas`
- [ ] Revisar distribución — ¿se están tocando los canales de FASE 4B (Reddit + Menéame + Beehiiv Boosts) con la cadencia mínima?
- [ ] Revisar si el último tangible generó sign-ups (Beehiiv Digital Product stats)

**Output:** 3 cambios concretos con frase trigger propia. Rafael decide cuáles aplicar la siguiente semana.

### 📅 Tabla semanal viva (mirror local de Beehiiv)

Rellenar cada lunes (ritual *"Ritual lunes — digest + métricas"*). 2 minutos copiando de Beehiiv Dashboard + Amazon Afiliados.

| Semana | Subs netos | Open rate | CTR | Artículos pub | Tangibles pub | Revenue afiliado | Nota |
|---|---|---|---|---|---|---|---|
| 2026-04-13 a 19 | — | — | — | 2 (#5 humanoides, #6 Samsung vapor) | 1 (Hoja de Compra v1/v2) | — | Sprint tangibles + pivote Cole. Primer PDF vivo. |
| 2026-04-20 a 26 | | | | | | | |
| 2026-04-27 a 03-may | | | | | | | |

### Qué rastrear (referencia)

| Métrica | Dónde | Objetivo mes 3 | Objetivo mes 12 |
|---|---|---|---|
| Suscriptores totales | Beehiiv → Dashboard | 100 | 1.000 |
| Open rate | Beehiiv → Posts → Analytics | >50% | >45% |
| Click-through rate | Beehiiv → Posts → Analytics | >10% | >6% |
| Revenue afiliado | Amazon Afiliados → Reports | €0 | €50+/mes |
| Tráfico web | Google Search Console | — | 3.000 visitas/mes |
| IG seguidores | Instagram → Insights | 100 | 1.500 |

### Google Search Console

- [ ] Ir a **https://search.google.com/search-console**
- [ ] Add Property → URL prefix → `https://robohogar.com`
- [ ] Verificar con DNS: añadir registro TXT en Namecheap
  - Tipo: `TXT`
  - Host: `@`
  - Value: el código que te da Search Console (empieza por `google-site-verification=...`)
  - TTL: Auto
- [ ] Enviar sitemap: en Search Console → Sitemaps → escribir `https://robohogar.com/sitemap.xml` (Beehiiv lo genera automáticamente)
- [ ] Esperar 2-3 días para los primeros datos

### Revisión mensual (template)

Cada primer lunes del mes, dedicar 30 min a esto:

```
## Revisión mensual — [MES YYYY]

### Números
- Subs inicio de mes:
- Subs fin de mes:
- Crecimiento neto:
- Open rate promedio:
- CTR promedio:
- Revenue afiliado:
- Top artículo por tráfico:

### Qué funcionó
- 

### Qué no funcionó
- 

### Acciones para los próximos 30 días
> Al rellenar, escribir la fecha objetivo absoluta (YYYY-MM-DD) en cada check — evitar "esta semana" o "pronto".
- [ ] YYYY-MM-DD —
- [ ] YYYY-MM-DD —
- [ ] YYYY-MM-DD —
```

### Evaluación trimestral

**Próxima evaluación trimestral: 2026-07-18** (cuando leas esta fecha o posterior, ejecuta la revisión y reprograma la siguiente a 3 meses vista). Revisar contra los objetivos de `docs/plan-v2.md`:

- [ ] ¿Estoy en cadencia? (¿He enviado todos los newsletters programados?)
- [ ] ¿Crecimiento de subs está en línea con objetivos?
- [ ] ¿Qué tipo de contenido genera más suscripciones? (reviews vs editorial vs guías)
- [ ] ¿Los artículos SEO están posicionando? (Search Console → Performance)
- [ ] ¿Merece la pena invertir en alguna herramienta de pago?

### Criterio de abandono

> [!warning]
> Si después de 6 meses con cadencia consistente (12 newsletters enviados sin fallar) hay **menos de 100 suscriptores**, el nicho no funciona en español. Opciones: pivotar el posicionamiento o cerrar.

---

## FASE 7: Post-lanzamiento y mantenimiento con Claude Code

### 🛠 Mantenimiento preventivo del repo — `/pipeline-debug`

Skill repetible para auditar el pipeline end-to-end. Invocar último viernes de cada mes (ya programado en [[#🗓 Schedule semanal fijo|§ 🗓 Schedule semanal fijo]]) o cuando se introduzca novedad mayor (nuevo skill, pivote editorial, formato nuevo).

**Frases trigger:**

| Qué quiero | Frase exacta |
|---|---|
| Audit completo del repo | **"/pipeline-debug"** o **"pipeline debug"** |
| Audit limitado a un área | **"/pipeline-debug tangibles"** (o `skills`, `rules`, `refs`, `memory`, `docs`, `schedule`) |
| Audit con foco en cambios recientes | **"/pipeline-debug full since:YYYY-MM-DD"** |

**Output:** report markdown en `content/pipeline-debug-reports/<YYYY-MM-DD>-<scope>-debug.md` con hallazgos priorizados 🔴/🟡/🟢 + propuesta de 3 next steps para pegar en [[#📌 Próximos 3 next steps|§ 📌 Próximos 3 next steps]]. El skill NO edita el repo — sólo reporta.

**Baseline de cobertura:** ejercicio manual fundacional 2026-04-19 en `content/pipeline-debug-reports/2026-04-19-full-debug.md`. Cada ejecución automática posterior se compara contra éste para calibrar la cobertura de los prompts de agentes.

Definición completa: [`.claude/commands/pipeline-debug.md`](../.claude/commands/pipeline-debug.md).

### Workflow semanal (~30-60 min con Claude Code)

**Agentes automáticos (Claude Code ejecuta):**

- [ ] `/research-digest` — digest + backlog dual + semillas narrativas (solo si >5 días del último)
- [ ] `/content-draft` — borrador HTML + hero + imágenes inline + PASOS.md
- [ ] `/ficcion-draft` — relato completo desde semillas del backlog (cada 3-4 semanas)

**Manual (Rafael):**

- [ ] Editar borrador (añadir voz, opinión, humor) — 45-90 min
- [ ] Publicar en Beehiiv (copy-paste + settings + hero + preview mobile)

**Post-publicación (Claude Code ejecuta):**

- [ ] `/post-publish <URL>` — 14 pasos: verifica OG, mueve a `published/`, actualiza registros + llms.txt + fuentes + catálogo + vault + commit
- [ ] `/social-content` — posts para LinkedIn, X, Instagram, WhatsApp (opcional, cuando redes estén listas)
- [ ] Programar posts en Buffer (manual hasta FASE 10)

### Mantenimiento mensual (~15 min)

- [ ] `/obsidian-robohogar calendar-update` — actualizar calendario editorial
- [ ] `/obsidian-robohogar audit` — revisar naming, frontmatter, wikilinks
- [ ] Revisar métricas en Beehiiv (subs, open rate, CTR)
- [ ] Revisar Google Search Console (qué keywords posicionan)
- [ ] Actualizar `Metricas/` en el vault con los datos del mes

### Mantenimiento trimestral (~30 min)

- [ ] `/obsidian-robohogar archive` — archivar digests y borradores viejos
- [ ] Actualizar artículos evergreen (precios, modelos nuevos, links rotos)
- [ ] Revisar y actualizar SEO: meta descriptions, títulos, keywords
- [ ] Evaluar: ¿Qué artículos generan más tráfico? → escribir más de ese tipo
- [ ] Evaluar: ¿Qué lead magnets convierten? → mantener gated o abrir

### Actualizar landing en Beehiiv

**Añadir secciones:**

- En Beehiiv: **Website → Design Mode → Add Section**
- Secciones candidatas: testimonios (cuando haya), contador de suscriptores, vídeo embed de YouTube

**Cambiar imágenes:**

- En Beehiiv: **Design Mode → clic en imagen → Replace**
- Generar nuevas con `/nano-banana` → subir a Beehiiv
- Assets van a `assets/images/` en el repo (backup)

**Añadir vídeos:**

- En Beehiiv: **Design Mode → Add Section → Video/Embed**
- Pegar URL de YouTube — Beehiiv genera el embed automáticamente
- Recomendado: 1 vídeo en la landing cuando haya contenido en YouTube

**Actualizar FAQ:**

- En Beehiiv: **Design Mode → FAQ section → Edit**
- Añadir preguntas nuevas basadas en feedback de suscriptores

**Actualizar social proof:**

- Cuando alcances 100 subs: cambiar "Semanal · 5 min" → "Únete a 100+ lectores"
- Cuando alcances 500: "Únete a 500+ lectores que ya viven con robots"

### Skills de Claude Code disponibles

| Skill | Trigger | Qué hace |
|---|---|---|
| `/research-digest` | "agrega noticias", "digest", "research" | Web search/fetch → digest dual (repo + vault) + backlog artículos + backlog Ficciones + wiki update + semillas narrativas |
| `/content-draft` | "borrador", "nuevo artículo" | Genera HTML completo + 3 variantes hero + imágenes inline descargadas + PASOS.md + mapa visual |
| `/ficcion-draft` | "ficción", "relato", "escribe una historia" | Lee backlog Ficciones, usa character bible, aplica frameworks Pixar/MRU/Paint-The-Villain |
| `/nano-banana` | "genera imagen", "hero" | Gemini API (Nano Banana) · cataloga en `asset-catalog.md` · versiona v2/v3 (nunca sobrescribe) |
| `/social-content` | "genera social", "posts" | Posts adaptados a LinkedIn, X, Instagram, WhatsApp desde artículo publicado |
| `/post-publish` | "ya está publicado", URL de artículo | 14 pasos: verifica OG → published/ → registros → llms.txt → fuentes → catálogo → vault → commit |
| `/obsidian-robohogar` | "sync vault", "wiki update", "calendar update" | Subcomandos: `wiki-update` · `sync-published` · `calendar-update` · `audit` · `archive` |
| `/commit` | "commitea", "haz commit" | Git commit con formato estándar + co-author + stage por nombre |
| `/workflow-excalidraw` | "diagrama", "workflow visual" | Diagramas de flujo/proceso en estilo ROBOHOGAR vía Excalidraw MCP |
| `/ui-ux-pro-max` | "review UI", "diseño landing" | Análisis UI/UX de landing, emails, social cards |

## FASE 8: Crecimiento de suscriptores (cuando haya >50 subs)

Tácticas para aumentar la base una vez superados los primeros 50 suscriptores.

> **Distribución activa 0-50 subs (Reddit, foros ES, Menéame, Beehiiv Boosts) vive en FASE 4B — no aquí.** Esta fase cubre solo palancas que requieren masa crítica previa (engagement flows, referral, exit intent, cross-promo recíproca).

### Content gate ("Subscribe to keep reading")

- Beehiiv permite bloquear el contenido a mitad de artículo con un muro de suscripción gratuita
- El lector ve el inicio del artículo, se engancha, y debe suscribirse para seguir leyendo
- **Cuándo activar:** en artículos largos tipo review o comparativa (>1200 palabras), NO en newsletters
- **Configuración en Beehiiv:** Settings → Content → Content Gate (activar por artículo, no globalmente)
- **Referencia visual:** pantallazo guardado — modal con "Subscribe to keep reading", email input y "Not now"

### Engagement-based emails

- Configurar emails automáticos cuando un lector interactúa (likes, clicks, shares)
- Ejemplo: "Veo que te gustó el artículo de humanoides — te aviso cuando publique la parte 2"
- **En Beehiiv:** Automations → Triggers (disponible en planes de pago, planificar para cuando escale)

### Referral program

- Beehiiv tiene sistema de referidos integrado (Refer a Friend)
- Recompensar con contenido exclusivo o mención en la newsletter
- **Cuándo activar:** cuando haya masa crítica (~200+ subs)

### Otras tácticas pendientes de evaluar

- [x] ~~Lead magnet (PDF "Guía de compra de robots 2026") a cambio de email~~ → documentado como **FASE 4C** con roadmap completo del sistema de tangibles "Always ship a tangible" (skill `/pdf-brand` + biblioteca pública + bundles)
- [x] ~~Compartir en comunidades (Reddit, foros domótica ES, Menéame)~~ → documentado como **FASE 4B** con playbook concreto por canal
- [ ] Cross-promotion recíproca con newsletters similares en español (≥200 subs, swap formal con pieza editorial)
- [ ] Pop-up de salida en artículos web (exit intent)
- [ ] Firma de email personal con link a ROBOHOGAR

---

## FASE 9: Optimización Newsletter (cuando haya >200 subs)

### A/B Testing

- [ ] Testear sender name: "Rafael" vs "ROBOHOGAR" vs "Rafael de ROBOHOGAR"
- [ ] Testear formato CTA: botón ámbar vs text link
- [ ] Testear template: minimalista vs con hero image
- [ ] Testear subject: pregunta vs statement vs número
- [ ] Referencia: `references/newsletter/email-marketing-playbook.md` sección Testing
- [ ] Solo 1 de cada 7 tests da resultado significativo — paciencia

### Segmentación por engagement

> Implementar 5 tiers del playbook (sección Segmentation).

- [ ] Tier 1 (clicked 30d): recibe todo
- [ ] Tier 2 (clicked 60d): recibe 75% de envíos
- [ ] Tier 3 (opened 90d): solo el mejor contenido
- [ ] Tier 4 (sin engagement 90-180d): solo re-engagement flow
- [ ] Tier 5 (180+ días): sunset flow → suprimir
- [ ] Resultados esperados: +15-30% opens, -20-40% complaints
- [ ] Requiere plan Scale de Beehiiv para segmentación avanzada

### Deliverability audit

- [ ] Verificar SPF/DKIM/DMARC con herramienta online (ej: mxtoolbox.com)
- [ ] Monitorear Gmail Primary vs Promotions (enviar test emails)
- [ ] Revisar bounce rate y spam complaints vs benchmarks del playbook
- [ ] Implementar sunset flow para inactivos >90 días
- [ ] Referencia: playbook sección Deliverability

### Upgrade a Beehiiv Scale (cuando >2,500 subs o revenue lo justifique)

- [ ] Evaluar ROI: ¿el revenue (afiliados + sponsors) cubre los $34/mes?
- [ ] Activar: segmentación avanzada, A/B testing nativo, analytics detallados
- [ ] Activar: automations completas (welcome series de 6 emails)
- [ ] Evaluar: API access para subscribers → integrar en pipeline de automatización
- [ ] Considerar: Beehiiv MCP (si disponible en el plan)

---

## FASE 10: Pipeline Avanzado (cuando el workflow manual sea el bottleneck)

> Criterio de activación: cuando publicar el artículo semanal empiece a robar >4h/semana o cuando el research manual se escape de ritmo. Hoy (abr 2026) los skills cubren lo esencial — este pipeline avanzado es optimización, no urgencia.

### 1. Research aggregator automatizado

`/research-digest` actual usa web search bajo demanda. El siguiente paso es un script que corra solo en cron.

- [ ] Implementar `utilities/research_aggregator.py` (pendiente)
  - RSS feeds: The Robot Report, IEEE Spectrum, Weekly Robotics, TechCrunch Robotics, Xataka, XatakaHome, blogs Roborock/Dreame/Ecovacs
  - Firecrawl API para scraping de fuentes sin RSS
  - Claude API (Haiku) para categorización + relevancia + resumen ES
  - Output mismo formato que el skill manual (compatible con `/content-draft`)
- [ ] Cron semanal (lunes 8:00 CET) vía Make.com o cron local
- [ ] Reemplazo del workflow manual de `/research-digest` cuando esté estable

### 2. Make.com (orquestación) — 9€/mes

- [ ] Scenario 1: cron lunes → aggregator → commit + push del digest
- [ ] Scenario 2: artículo publicado (webhook Beehiiv) → trigger `/social-content` → Buffer API
- [ ] Activar cuando haya >30 subs (volumen que justifique el coste)

### 3. Buffer (programación social) — 6€/mes

- [ ] Conectar Instagram, LinkedIn, WhatsApp Channel
- [ ] Horarios: IG L/M/V 12:00 · LinkedIn Ma/J 9:00 · WhatsApp Ma 10:00
- [ ] Free tier (3 canales, 10 posts/canal) puede bastar al inicio

### 4. Beehiiv MCP (cuando esté en plan de pago)

- [ ] Upgrade a Beehiiv Scale ($34/mes) para API access
- [ ] Añadir a `.mcp.json`:
  ```json
  {
    "beehiiv": {
      "url": "https://mcp.beehiiv.com/mcp",
      "headers": { "Authorization": "Bearer <token>" }
    }
  }
  ```
- [ ] V1: consultar métricas desde Claude Code
- [ ] V2: crear drafts directamente (elimina el copy-paste manual — el mayor bottleneck actual)

### 5. Pipeline end-to-end (objetivo: ~1h/artículo vs ~3h actuales)

```
┌── LUNES 8:00 — AUTOMÁTICO ───────────────────────────────────┐
│ Cron → research_aggregator.py                                 │
│ RSS + Firecrawl → Claude API Haiku → digest.md               │
│ Commit + push automático                                      │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── LUNES/MARTES — MANUAL (~15 min) ──────────────────────────┐
│ Rafael lee digest → elige tema del backlog → define ángulo  │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── SEMIAUTOMÁTICO (skills) ──────────────────────────────────┐
│ /content-draft → HTML + hero + inlines + PASOS               │
│ /nano-banana  → (ya ejecutado por /content-draft)            │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── MANUAL (~45-60 min) ──────────────────────────────────────┐
│ Rafael edita voz → crea draft en Beehiiv (via MCP V2)       │
│ → preview mobile → programa envío                            │
└──────────────────────────────────────────────────────────────┘
                           ↓
┌── POST-PUBLICACIÓN — AUTOMÁTICO ─────────────────────────────┐
│ Webhook Beehiiv → Make.com → /post-publish                   │
│ → /social-content → Buffer programa publicación              │
│ → vault sync + commit + push                                 │
└──────────────────────────────────────────────────────────────┘
```

### 6. Qué NO automatizar (nunca)

- Decidir qué publicar (juicio editorial)
- Escribir con voz propia (personalidad de marca)
- Revisar antes de enviar (calidad y consistencia)
- Responder a replies de suscriptores (relación humana)

Automatizar estos bloques destruiría el diferencial de ROBOHOGAR frente a feeds automatizados de tech-news sin alma.

---

*Guía viva — actualizar cuando se complete cada FASE.*
*Fuentes: `docs/plan-v2.md`, `docs/website-brief.md`, `references/newsletter/email-marketing-playbook.md`, research de mercado (abr 2026)*
*Última actualización sección final (FASE 3-10): 2026-04-17*
