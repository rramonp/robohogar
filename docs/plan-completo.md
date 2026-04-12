# ROBOHOGAR — Plan Completo del Proyecto

**Dominio:** robohogar.com (comprado 2026-04-12)
**Estado:** Repo pendiente de crear

---

## PASO 1 — Crear repo en GitHub y montar estructura (5 min)

### 1A. Crear en GitHub (web)
1. Ir a https://github.com/new
2. **Repository name:** `robohogar`
3. **Description:** `ROBOHOGAR — Newsletter + blog sobre robótica doméstica con IA, en español`
4. **Visibility:** Private
5. Marcar: **Add a README file**
6. **.gitignore:** Python
7. License: ninguna
8. **Create repository**

### 1B. Clonar y montar estructura (terminal)
```bash
cd C:/Users/bakal
git clone https://github.com/rramonp/robohogar.git
cd robohogar

# Estructura del proyecto
mkdir -p .claude/commands .claude/rules .claude/memory .claude/hooks
mkdir -p docs content/drafts content/published
mkdir -p assets/branding/master assets/branding/flash-1K assets/branding/con-fondo assets/images
mkdir -p references utilities

# Copiar docs desde RRP-DEV (temporal)
cp -r C:/Users/bakal/RRP-DEV/projects/robohogar/docs/* docs/
cp -r C:/Users/bakal/RRP-DEV/projects/robohogar/references/* references/
cp C:/Users/bakal/RRP-DEV/projects/robohogar/assets/landing-prototype.html assets/

# Copiar assets de branding (mascota)
cp C:/Users/bakal/RRP-DEV/projects/robohogar/assets/branding/mascota-prompt.md assets/branding/
cp C:/Users/bakal/RRP-DEV/projects/robohogar/assets/branding/master/*.png assets/branding/master/
cp C:/Users/bakal/RRP-DEV/projects/robohogar/assets/branding/flash-1K/*.png assets/branding/flash-1K/
cp C:/Users/bakal/RRP-DEV/projects/robohogar/assets/branding/con-fondo/*.png assets/branding/con-fondo/
```

### 1C. Crear .mcp.json (en la raíz del repo)
```bash
cat > .mcp.json << 'EOF'
{
  "mcpServers": {
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest"]
    },
    "firecrawl-mcp": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "firecrawl-mcp"]
    }
  }
}
EOF
```

### 1D. Crear .claude/memory/MEMORY.md
```bash
cat > .claude/memory/MEMORY.md << 'EOF'
# Memory Index
EOF
```

### 1E. Primer commit
```bash
git add -A
git commit -m "Initial setup: ROBOHOGAR project structure + research docs

Changes: project structure (.claude/, docs/, content/, assets/, references/),
MCP servers (Firecrawl + Playwright), research de mercado ES+EN,
plan completo, estrategia automatización, landing prototype,
mascota oficial (11 poses, master 2K + flash 1K + con-fondo)

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"

git push
```

### 1F. Verificar que toda la documentación se migró correctamente
Después del `cp`, confirmar que estos archivos existen en el nuevo repo:
```bash
ls docs/                    # plan-original.md, plan-completo.md, estrategia-automatizacion.md
ls references/              # competencia-es.md, competencia-en.md, plataformas-comparativa.md
ls assets/                  # landing-prototype.html
ls assets/branding/         # mascota-prompt.md
ls assets/branding/master/  # 11 archivos .png (2K — assets definitivos)
ls assets/branding/flash-1K/ # 11 archivos .png (1K — borradores)
ls assets/branding/con-fondo/ # 1 archivo .png (mascota en contexto hogar)
```
Si falta algo, copiar manualmente desde `C:/Users/bakal/RRP-DEV/projects/robohogar/`.

**Una vez confirmado**, la carpeta `projects/robohogar/` en RRP-DEV ya no es necesaria — se puede borrar o dejar como backup. El repo nuevo es la fuente de verdad a partir de ahora.

### 1G. Abrir Claude Code en el nuevo repo
- Abrir Claude Code apuntando a `C:/Users/bakal/robohogar`
- Decir: **"configura el CLAUDE.md y las rules para ROBOHOGAR"**
- Claude creará: CLAUDE.md, rules (editorial, SEO, design, automation, config), hooks, y skills migradas (commit, nano-banana, ui-ux-pro-max)

### Estructura final esperada
```
robohogar/
  .claude/
    CLAUDE.md                   # Reglas del proyecto
    commands/                   # Skills: commit, nano-banana, ui-ux-pro-max, research-digest, publish-issue
    rules/                      # editorial.md, seo.md, design.md, automation.md, config.md, literate-code.md
    hooks/                      # autoformat, validate_comments, validate_json, notify, protect_files, git_pull
    memory/
      MEMORY.md
  .mcp.json                    # Firecrawl + Playwright
  docs/
    plan-original.md            # Documento base (Sonnet)
    plan-completo.md            # Este archivo
    estrategia-automatizacion.md
  content/
    drafts/                     # Borradores de artículos
    published/                  # Artículos publicados (backup)
  assets/
    branding/
      mascota-prompt.md         # Fuente de verdad de la mascota (prompts, catálogo, variaciones)
      master/                   # 11 poses en 2K — assets definitivos para web, landing, print
      flash-1K/                 # 11 poses en 1K — borradores, previews rápidos
      con-fondo/                # Mascota en contexto hogar — referencia para escenas domésticas
    images/                     # Imágenes para artículos
    landing-prototype.html      # Prototipo visual
  references/
    competencia-es.md           # Mercado español
    competencia-en.md           # Referentes inglés
    plataformas-comparativa.md  # Ghost vs Substack vs Beehiiv
  utilities/                    # Scripts (research_aggregator.py, etc.)
  README.md
```

---

## Context

Newsletter + blog en español sobre robótica adaptada al hogar, enfocado a España/Europa. Proyecto hobby a largo plazo (3-5 hrs/semana), con visión de monetización futura cuando el mercado madure (2028-2032).

La investigación de mercado confirma que **no existe competencia directa en español** para este nicho. El único competidor tangencial es Integrarobot (Javier Martín, Substack, foco empresarial). Las grandes newsletters de IA en español (IA en Español 42K subs, EvolupedIA 40K subs) tocan robótica ocasionalmente pero ninguna la atiende verticalmente. En inglés, el mayor referente es "we all are robots" (17K subs, Substack). Timing ideal: 2026 = lanzamiento comercial de robots humanoides domésticos.

---

## 2. Nombre y Branding (DECIDIDO: ROBOHOGAR)

### Opción principal: NEXUS
- Pros: corto, memorable, suena tecnológico, ya tiene identidad visual diseñada
- Contras: nombre muy genérico (hay decenas de "Nexus" en tech), difícil de posicionar SEO, dominio .com/.es probablemente ocupado
- Paleta actual: fondo `#ffffff`, acento naranja `#f5a623`, negro `#0c0c0c`
- Tipografía: Jost (títulos) + DM Sans (cuerpo)

### Alternativas propuestas (verificar disponibilidad de dominio)

| Nombre | Concepto | Dominio sugerido | Valoración |
|---|---|---|---|
| **DOMO.bot** | Domótica + robot, directo y SEO-friendly | domo.bot / domobot.es | Alta — memorable, describe el nicho |
| **RoboHogar** | Literalmente "robot + hogar" en español | robohogar.es / robohogar.com | Alta — SEO directo, fácil de recordar |
| **HAUS** | Casa en alemán, minimalista, editorial | haus.bot / hausrobot.es | Media-alta — elegante pero menos SEO |
| **Circuito Hogar** | Evoca conexión, tecnología doméstica | circuitohogar.es | Media — más largo pero descriptivo |
| **Autómata** | Clásico, literario, diferenciador | automata.es / elautomata.es | Media — bonito pero no grita "hogar" |
| **TU ROBOT** | Directo, personal, posesivo | turobot.es | Alta — SEO brutal, muy directo |
| **La Casa Robot** | Editorial, magazine vibe | lacasarobot.es | Media-alta — largo pero evocador |

**Acción:** Verificar disponibilidad de dominios antes de decidir. Priorizar `.es` para España.

---

## 3. Comparativa de Plataformas (para decisión posterior)

### Ghost (Recomendado para blog+newsletter editorial)
- **Precio:** 9-25€/mes (500-1000 miembros), self-hosted gratis
- **Puntos fuertes:** Mejor CMS para estilo magazine editorial, SEO excelente (Node.js rápido, structured data automático, sitemaps), dominio propio desde día 1, 0% comisión, suscripciones de pago nativas, ActivityPub (distribución social web gratis)
- **Puntos débiles:** Sin red de descubrimiento, sin herramientas de referral, requiere algo más de setup inicial
- **Ideal para:** Tu visión de "MIT Technology Review en español para el hogar"

### Substack
- **Precio:** Gratis (10% comisión en suscripciones de pago + Stripe)
- **Puntos fuertes:** Red de descubrimiento (recomendaciones cruzadas), app móvil, community/Notes, donde están TODAS las newsletters de robótica en inglés (podría beneficiarse de cross-pollination)
- **Puntos débiles:** SEO limitado (subdominio substack.com), diseño muy restringido, 10% comisión, sin control de marca
- **Ideal para:** Crecimiento orgánico sin inversión, si priorizas audiencia sobre marca

### Beehiiv
- **Precio:** Gratis hasta 2.5K subs, 49€/mes para monetización
- **Puntos fuertes:** Mejores herramientas de email, red de ads nativa, referral program (Boosts), website builder con SEO, 0% comisión, digital products
- **Puntos débiles:** 49€/mes para desbloquear monetización (caro para hobby), sin red orgánica como Substack
- **Ideal para:** Si priorizas crecimiento agresivo y monetización temprana

### DECISIÓN (2026-04-12): Substack → Ghost cuando escale

**Substack para arrancar.** Razones:
- Coste cero — presupuesto mensual baja a ~17€ (dominio + Buffer + Make.com)
- Red de descubrimiento — todas las newsletters de robótica en inglés están aquí (cross-pollination)
- Cero fricción — 15 min de setup, las 3-5 hrs/semana van a contenido, no a CMS
- Validación rápida — si en 3 meses no hay tracción, no se perdió dinero en infra
- robohogar.com redirige a Substack mientras tanto

**Migrar a Ghost cuando se cumplan 2 de 3:**
- 500+ suscriptores
- El diseño de Substack limita la visión editorial
- El 10% de comisión en suscripciones de pago empieza a doler

**SEO de Substack (débil) mitigado por:** competencia cero en español — no necesitas SEO perfecto, necesitas existir. Cuando migres a Ghost, el contenido migra y el SEO real arranca con base de contenido probado.

---

## 3. Estrategia de Contenido (3-5 hrs/semana)

### Frecuencia: Quincenal (cada 2 semanas)
- Semanal no es sostenible con familia + trabajo + 3-5 hrs/semana
- Quincenal permite calidad sobre cantidad
- Subir a semanal solo cuando tengas sistemas y rutina consolidados

### Calendario editorial (alternando formatos)

| Semana | Formato | Tiempo | Descripción |
|---|---|---|---|
| 1 | **Roundup curado** | ~3 hrs | Top 5-7 noticias de robótica doméstica con tu análisis/comentario en cada una. Pan de cada día — alto valor, esfuerzo moderado |
| 2 | **Artículo original** | ~4-5 hrs | Pieza profunda: review de producto, guía de compra, explicador tecnológico, opinión. Motor SEO |

### Workflow asistido por IA (realista)
1. **Investigación** (45 min): Claude escanea noticias recientes de robótica, lanzamientos, patentes
2. **Outline + borrador** (30 min): Claude produce draft estructurado con tu ángulo/opiniones
3. **Reescritura + voz propia** (90 min): Aquí añades expertise, opiniones, correcciones, experiencia personal. El output de IA es materia prima, no producto final
4. **SEO + formato** (30 min): Meta description, título optimizado, imágenes, formato
5. **Post social** (15 min): Un post en LinkedIn resumiendo el insight clave

### Categorías de contenido (refinadas desde tu documento)
1. **Robots para el hogar** — Neo, Figure 03, Unitree, reviews, comparativas de precio/prestaciones
2. **IA doméstica** — qué modelos corren dentro, capacidades reales vs promesas
3. **Domótica + integración** — Home Assistant, smart home, cómo se conectará todo
4. **Mercado y precios** — cuándo serán asequibles, análisis de escala de producción
5. **Vida con robots** — privacidad, convivencia, dependencia emocional, debate social
6. **Guías de compra** — robots aspirador, cortacésped, cocina (ya disponibles, SEO directo)

### Contenido evergreen de lanzamiento (5 artículos antes de publicar)
1. "¿Qué es un robot doméstico con IA y por qué importa en 2026?"
2. "Los 7 robots humanoides más avanzados — comparativa actualizada"
3. "¿Cuándo costará un robot doméstico menos de 10.000€? Análisis de la curva de precios"
4. "Guía: los mejores robots aspirador de 2026 (comparativa España)"
5. "Privacidad y robots en casa: lo que deberías saber antes de comprar"

---

## 4. SEO — Mina de Oro en Español

### Por qué funciona
- **Cero competencia de calidad** en español para "robótica doméstica", "robot hogar", "robot aspirador comparativa"
- Los resultados actuales son affiliate sites de baja calidad o artículos genéricos de medios generalistas
- Long-tail keywords con 100-1.000 búsquedas mensuales están completamente libres

### Keywords objetivo (verificar volúmenes)
- "mejor robot aspirador 2026" — alto volumen, competencia media (affiliate sites)
- "robot doméstico precio" — volumen creciente, competencia baja
- "robots humanoides para casa" — volumen bajo pero en crecimiento exponencial
- "robot cortacésped jardín pequeño" — volumen medio, competencia baja
- "domótica y robótica hogar" — nicho, cero competencia de calidad
- "neo robot precio españa" — producto específico, cero competencia

### Timeline SEO
- **Meses 1-3:** Indexación, primeros artículos evergreen posicionándose
- **Meses 3-6:** Rankings para long-tail sin competencia
- **Meses 6-12:** Tráfico orgánico estable 500-2.000 visitas/mes
- **Año 2+:** Compounding — artículos viejos siguen generando tráfico

---

## 5. Red Social — Solo LinkedIn

### Por qué LinkedIn y no X/Twitter
- Engagement rate más alto de todas las plataformas (5,2% vs 2,3% en X)
- Audiencia profesional española activa
- Carousels tienen 21,77% de engagement — perfecto para "5 robots a vigilar"
- Posts tienen vida útil de días (vs 15 minutos en X)
- Encaja con el tono editorial sin hype

### Estrategia mínima (30 min/semana)
1. Un post por cada issue del newsletter (resumen del insight clave, no el artículo entero)
2. Carousel visual cuando proceda (3-5 slides)
3. CTA a suscribirse al final
4. 5 min de engagement en comentarios de otros posts de tech/robótica

### Herramienta: Buffer (6€/mes)
- Programa posts en LinkedIn + 1 plataforma más
- AI caption assistance
- Suficiente para el volumen que necesitas

---

## 6. Monetización — Timeline Realista

### Año 1 (Inversión pura, 0-50€/mes)
- Amazon Afiliados España desde el inicio (en guías de compra de robots aspirador, cortacésped)
- Foco: construir librería de contenido + primeros 500-1.000 suscriptores
- Ingreso real: 0-50€/mes por afiliados si las guías de compra rankean

### Año 2 (50-300€/mes)
- SEO compounding → tráfico creciente → más ingresos por afiliados
- Primeros suscriptores de pago (tier premium con análisis profundos)
- Primer patrocinio esporádico si llegas a 2.500+ subs

### Año 3+ (300-1.000€/mes, potencialmente más)
- Newsletter de pago consolidada: 200 subs × 7€ = 1.400€/mes posible
- Patrocinios regulares de marcas del sector
- Digital products (guías PDF, comparativas detalladas)
- El mercado de robots domésticos empieza a madurar → mayor demanda de contenido

### Coste mensual total: ~25-50€
| Concepto | Coste |
|---|---|
| Plataforma (Substack) | 0€ |
| Dominio | ~1€/mes (10€/año) |
| Buffer (3 redes sociales) | 6€ |
| Make.com (automatización social) | 9€ |
| Firecrawl (research scraping) | 0€ (free tier 500 créditos/mes) |
| Claude API (research + social posts) | ~1€/mes |
| Obsidian | 0€ |
| **Total** | **~17-42€/mes** |

### Tiempo por issue: ~3 hrs
| Paso | Tiempo | Quién |
|---|---|---|
| Escanear research digest + curar | 15 min | Tú |
| Escribir ángulos/opiniones | 15 min | Tú |
| Generar borrador | 10 min | Claude |
| Editar + añadir personalidad | 75 min | Tú |
| Formatear + publicar | 15 min | Tú |
| Revisar cola social en Buffer | 10 min | Tú |
| Engagement en comentarios | 20 min | Tú (opcional) |
| **Total** | **~2.5-3 hrs** | |

---

## 7. Competencia — Resumen Ejecutivo

### En español (campo casi vacío)
| Competidor | Plataforma | Foco | Amenaza |
|---|---|---|---|
| **Integrarobot** (Javier Martín) | Substack | Robótica empresarial/industrial, no hogar | Baja (diferente ángulo) |
| **IA en Español** (42K subs) | Substack | IA general, toca robótica ocasionalmente | Media (podrían expandir) |
| **EvolupedIA** (40K subs) | Substack | IA general, artículos sobre robótica física | Media (podrían expandir) |
| **Xataka/El Español** | Web propia | Medios generalistas, cobertura superficial | Baja (no vertical) |
| robotica.es | WordPress | Portal de noticias genérico | Baja (sin voz editorial) |

### En inglés (referentes a seguir)
| Referente | Subs | Qué copiar |
|---|---|---|
| **we all are robots** (Ziegler) | 17K | Numeración de episodios, versión audio, personal brand |
| **Weekly Robotics** (Sadowski) | 5.9K | Formato curated roundup, 300+ issues, 51% open rate |
| **Robots & Startups** (Keay) | 9K | Tier pricing con whale tier ($44K/año para inversores) |
| **Humanoid Press** | N/A | Ticker en tiempo real, foco puramente humanoides |

---

## 8. Ideas Nuevas (enriquecimiento sobre tu documento base)

### Formato
1. **Numeración de episodios** (EP.001, EP.002...): crea coleccionabilidad y hábito
2. **Versión audio** del newsletter: text-to-speech de calidad (ElevenLabs ~11€/mes) — alcance commuters sin crear contenido extra
3. **"Robot del mes"**: sección fija destacando un robot/producto concreto
4. **Tracker de precios**: tabla recurrente con precios actualizados de robots humanoides principales
5. **Sección "Lo que se viene"**: calendario de lanzamientos próximos

### Monetización extra
6. **Lead magnet**: PDF gratuito "Guía 2026: Todo sobre robots para casa" — a cambio del email
7. **Directorio de robots**: página web con todos los robots domésticos, specs y precios — imán SEO permanente
8. **Alertas de ofertas**: email flash cuando un robot baja de precio en Amazon España

### Crecimiento
9. **Cross-promotion con newsletters de IA en español**: contactar a IA en Español y EvolupedIA para recomendaciones cruzadas
10. **Guest posts en Xataka Smart Home**: posicionarte como experto y derivar tráfico
11. **Participar en Spain AI meetups**: red de contactos tech en España

### Branding (recomendación)
12. **NO reutilizar estilo Neon Cyan/Pink cyberpunk de RRP-DEV** — el cyberpunk aliena al público general de la newsletter (familias, early adopters no-técnicos). Mantener la identidad editorial de la landing: fondo `#ffffff`, acento naranja `#f5a623`, Jost + DM Sans. Mascota oficial definida → ver `assets/branding/mascota-prompt.md`.

---

## 8B. Automatización de Contenido — Pipeline Completo

### Principio clave
**Automatizar todo EXCEPTO juicio editorial y voz.** Esas dos cosas son lo que hace que una newsletter merezca la suscripción, y no se pueden delegar.

### Pipeline por issue (cada 2 semanas, ~3 hrs)

```
AUTOMATIZADO (0 hrs)                    TÚ (2.5-3 hrs)
─────────────────────                   ───────────────
RSS feeds + Google Alerts               
    ↓                                   
Script Python agrega noticias           
    ↓                                   
Claude API categoriza + resume          
    ↓                                   
Research Digest .md → Obsidian     →→   Escaneas digest, eliges 3-5 temas (15 min)
                                        Escribes TU ángulo/opinión en 1 línea cada uno (15 min)
                                        ↓
                                        Claude genera borrador desde tus ángulos (10 min)
                                        ↓
                                        Editas, añades personalidad, anécdotas, humor (75 min)
                                        ↓
                                        Formateas y publicas (15 min)
                                        ↓
Newsletter publicada → RSS feed         
    ↓                                   
Make.com detecta RSS nuevo              
    ↓                                   
Claude API genera posts sociales        
    ↓                                   
Buffer programa posts automáticamente   Revisas cola de Buffer, apruebas (10 min)
    ↓                                   
LinkedIn + X + Threads auto-publicados  Engagement: respondes comentarios (20 min opcional)
```

### Script de agregación de research (en el repo nuevo)

`utilities/research_aggregator.py` — se ejecuta quincenalmente (manual o cron):

1. Fetch RSS feeds (feedparser): IEEE Spectrum, Robot Report, TechCrunch robotics, Xataka, etc.
2. Filtra últimos 14 días, deduplica por similitud de título
3. Firecrawl API scraping de los top 10-15 artículos más relevantes
4. Claude API categoriza (Consumer Robots, Robot Vacuums, Humanoids, AI/Software, Industry) y puntúa relevancia 1-5
5. Output: `05_Personal/05-01_Robotica Newsletter/Research/Research Digest YYYY-MM-DD.md` en Obsidian
6. Coste: ~0€ (free tiers de Firecrawl 500 créditos/mes + Claude API ~$0.10/run)

### RSS Feeds a monitorizar

**Tier 1 — Obligatorios:**
- IEEE Spectrum Robotics, The Robot Report, TechCrunch Robotics, The Verge (robots)

**Tier 2 — Robótica consumer/hogar:**
- r/RobotVacuums (via RSS bridge), newsrooms de iRobot/Roborock/Ecovacs/Dreame

**Tier 3 — Fuentes en español:**
- Xataka (robotics), Xataka Smart Home, ComputerHoy domótica

**Google Alerts (7 alertas, entrega semanal RSS):**
- `"home robot" OR "robot doméstico"`
- `"robot vacuum" OR "robot aspirador" 2026`
- `"humanoid robot" home OR consumer`
- `"robótica doméstica"`
- `iRobot OR Roborock OR Ecovacs announcement`
- `Tesla Bot OR Figure OR Boston Dynamics consumer`
- `"robot cortacésped"`

### Cómo evitar que suene a IA

**Frases PROHIBIDAS en el system prompt:**
- "En el vertiginoso mundo de..." / "En la era de..."
- "Es importante destacar que..." / "Sin duda alguna..."
- "En este sentido..." / "Un enfoque holístico..."
- Cualquier frase que empiece con "Como [profesional], sabemos que..."

**Técnicas positivas:**
- Empezar con imagen concreta o anécdota, nunca una frase genérica
- Mezclar frases cortas con largas (IA tiende a frases uniformes medias)
- Tener opiniones fuertes: "Este robot es una estafa a 800€" > "presenta limitaciones respecto a su precio"
- Español coloquial natural: "mola", "flipar", "cacharro", "irse de madre"
- Referenciar experiencia personal real (IA no puede generar esto)
- Discrepar del consenso — IA siempre hace hedging, tú tomas partido

---

## 8C. Redes Sociales — Estrategia Multi-plataforma Automatizada

### Plataformas recomendadas

| Plataforma | Prioridad | Automatizable | Esfuerzo extra | ROI esperado |
|---|---|---|---|---|
| **LinkedIn** | ALTA | Sí (Buffer + Make.com) | 0 min extra | Alto — audiencia profesional tech España |
| **X/Twitter** | ALTA | Sí (Buffer + Make.com) | 0 min extra | Alto — descubrimiento, comunidad robótica activa |
| **Threads** | MEDIA | Sí (Buffer) | 0 min extra | Medio — creciente pero inestable |
| **Bluesky** | BAJA | Sí (API abierta) | 0 min extra | Bajo por ahora, audiencia tech-savvy |
| YouTube/TikTok | NO | No (requiere vídeo) | Mucho | Descartado por tiempo |

**Con automatización completa, puedes estar en LinkedIn + X + Threads sin tiempo adicional.** Todo se genera desde el newsletter publicado.

### Flujo de automatización (Make.com, ~9€/mes)

```
Trigger: RSS del newsletter (nueva issue publicada)
    ↓
Módulo 1: Parsear RSS → extraer título, resumen, link
    ↓
Módulo 2: HTTP request a Claude API
    - System prompt: "Genera posts sociales desde este extracto de newsletter"
    - Variantes: LinkedIn (300 palabras), X (280 chars × 3 posts), Threads (500 chars)
    ↓
Módulo 3: Router (paralelo)
    ├→ Buffer API: Programar post LinkedIn (martes 9:00 CET)
    ├→ Buffer API: Programar 3 posts X (repartidos en 3 días)
    └→ Buffer API: Programar post Threads (miércoles)
    ↓
Módulo 4: Notificación email/Slack con preview de lo programado
```

**Coste total automatización social:** Make.com 9€ + Buffer 6€ = **15€/mes** para 3 plataformas 100% automatizadas.

### De cada issue del newsletter se generan:
- 1 post largo LinkedIn (insight principal + opinión + CTA suscribirse)
- 3-5 tweets/posts X (uno por tema cubierto, con hot take + link)
- 1 hilo X (la historia principal expandida en 5-7 posts)
- 1 post Threads (similar al de LinkedIn pero más corto)

**Tiempo adicional tuyo: ~10 min** para revisar la cola de Buffer antes de que se publique.

---

## 8D. Knowledge Management en Obsidian — Base de Datos Creciente

### Principio: Nada de research es one-shot
Todo lo que se investiga alimenta una base de conocimiento acumulativa. Cada artículo que lees, cada dato que recoges, cada opinión que formas — queda catalogado y es reutilizable.

### Estructura en `05_Personal/05-01_Robotica Newsletter/`

```
05_Personal/
  05-01_Robotica Newsletter/
    Proyecto Robótica Newsletter.md     # MOC (Map of Content) principal
    Calendario Editorial.md             # Planning quincenal
    Decisiones.md                       # Log de decisiones (nombre, plataforma, etc.)
    
    Issues/                             # Un folder por issue
      EP001 - 2026-MM-DD/
        Draft.md                        # Borrador
        Research Notes.md               # Notas de research específicas del issue
        Social Posts.md                 # Posts sociales generados
      EP002 - 2026-MM-DD/
    
    Research/                           # Digests auto-generados + clippings manuales
      Research Digest 2026-04-12.md     # Auto-generado por script
      Research Digest 2026-04-26.md
      Clippings/                        # Artículos guardados manualmente
    
    Wiki/                               # BASE DE DATOS CRECIENTE — el corazón del sistema
      Robots/                           # Una nota por robot/producto
        Roomba j9+.md
        Neo (1X Technologies).md
        Figure 03.md
        Tesla Optimus.md
        Roborock S9 MaxV.md
      Empresas/                         # Una nota por empresa
        1X Technologies.md
        Figure AI.md
        iRobot.md
        Tesla Robotics.md
      Conceptos/                        # Notas evergreen por tema
        Navegación LIDAR vs SLAM.md
        Precios Robots Humanoides.md
        IA en Robótica Doméstica.md
        Privacidad y Robots.md
        Home Assistant Integración.md
      Mercado/                          # Datos de mercado acumulativos
        Precios Históricos.md           # Tabla actualizada de precios
        Competidores Newsletter.md      # Seguimiento de competencia
        Keywords SEO.md                 # Volúmenes y rankings
    
    Métricas/                           # Analytics del newsletter
      Suscriptores.md                   # Evolución mensual
      Tráfico SEO.md                    # Rankings y visitas
      Ingresos.md                       # Revenue tracking
    
    Templates/                          # Plantillas Obsidian
      Template Issue.md
      Template Research Digest.md
      Template Robot Wiki.md
      Template Empresa Wiki.md
    
    _deliverables/                      # PDFs, exports finales
    _archive/                           # Issues publicados archivados
```

### Cómo crece la Wiki automáticamente

**Cada vez que se procesa un Research Digest:**
1. El script detecta robots/empresas mencionados
2. Si no existe nota Wiki para ese robot/empresa → crea una desde template
3. Si existe → añade bullet con la noticia nueva + fecha + fuente
4. Las notas Wiki acumulan información progresivamente

**Cada vez que escribes un artículo:**
1. Los datos/hechos del artículo se linkean a notas Wiki existentes (`[[Neo (1X Technologies)]]`)
2. Si encuentras algo nuevo durante la edición → lo añades a la Wiki en el momento
3. Las notas Wiki se enriquecen con tu opinión editorial (que es lo valioso y no replicable)

### Plugins de Obsidian recomendados

| Plugin | Función | Por qué |
|---|---|---|
| **Templater** | Plantillas con fecha, variables | Auto-crear structure de cada issue |
| **Dataview** | Queries en el vault | "Muestra todos los robots con precio < 5000€" |
| **QuickAdd** | Captura rápida | Hotkey para añadir link + nota a la Wiki desde cualquier lugar |
| **Omnivore/ReadItLater** | Web clipping | Guardar artículos directamente en Research/Clippings |
| **Periodic Notes** | Notas periódicas | Auto-crear folder de issue cada 2 semanas |

### Flujo de conocimiento acumulativo

```
Fuentes externas (RSS, Alerts, web)
    ↓
Research Digest (auto-generado) ──→ Wiki/ se enriquece automáticamente
    ↓
Tú seleccionas temas para el issue
    ↓
Escribes artículo (linkando a Wiki)
    ↓
Artículo publicado ──→ Issues/EPxxx/ (backup)
                   ──→ Wiki/ se enriquece con tu análisis
                   ──→ Métricas/ se actualiza
    ↓
Próximo issue: la Wiki ya tiene contexto acumulado
    → escribes MÁS RÁPIDO porque el research previo está ahí
    → tus opiniones se refinan con datos acumulados
    → puedes hacer artículos "retrospectiva" fácilmente
```

**Resultado:** después de 6 meses tienes una Wiki de robótica doméstica en español que NO existe en ningún otro sitio. Es un activo valiosísimo que hace cada artículo más fácil de escribir y más profundo.

---

## 9. Repositorio GitHub Dedicado

### Por qué repo separado
- Proyecto con vida propia: landing, artículos, assets, scripts, posible theme de Ghost
- Escala independiente: CI/CD propio, deploy propio, secrets propios
- CLAUDE.md propio con reglas de editorial/SEO (no HBX/Tableau/CR%)
- Historial de commits limpio, sin mezclar con trabajo profesional

### Instrucciones para crear el repo

**Paso 1 — Crear en GitHub (web)**
1. Ir a https://github.com/new
2. Repository name: `robotica-newsletter` (o el nombre que elijas, ej: `nexus-robotica`, `domo-bot`)
3. Description: "Newsletter + blog sobre robótica doméstica con IA — en español"
4. Visibility: **Private** (hasta que lances públicamente)
5. Marcar: "Add a README file"
6. .gitignore: Python
7. License: ninguna por ahora
8. Crear

**Paso 2 — Clonar en local**
```bash
cd C:/Users/bakal
git clone https://github.com/rramonp/robotica-newsletter.git
cd robotica-newsletter
```

**Paso 3 — Estructura de carpetas**
```bash
mkdir -p .claude/commands .claude/rules .claude/memory
mkdir -p docs content assets references
mkdir -p content/drafts content/published
mkdir -p assets/branding assets/images
```

Estructura resultante:
```
robotica-newsletter/
  .claude/
    CLAUDE.md                 # Reglas del proyecto (ver abajo)
    commands/                 # Skills específicas del proyecto (futuro)
    rules/                    # Reglas editoriales, SEO, diseño
    memory/
      MEMORY.md               # Índice de memoria del proyecto
  docs/
    plan-original.md          # Tu documento de planificación migrado
    market-research.md        # Investigación de mercado (ES + EN)
    platform-comparison.md    # Comparativa Ghost vs Substack vs Beehiiv
    name-branding.md          # Opciones de nombre y dominio
  content/
    drafts/                   # Borradores de artículos
    published/                # Artículos publicados (backup)
  assets/
    branding/                 # Logo, favicon, og-image
    images/                   # Imágenes para artículos
    landing-prototype.html    # Tu landing HTML actual migrado
  references/                 # Competencia, inspiración, links útiles
  README.md                   # Descripción del proyecto
```

**Paso 4 — CLAUDE.md base** (contenido sugerido)
```markdown
# NEXUS / Robótica Newsletter — Claude Instructions

## Proyecto
Newsletter + blog en español sobre robótica doméstica con IA.
Mercado: España + hispanohablante. Tono: editorial, sin hype, con criterio.

## Idioma
- Responder en español
- Artículos y contenido: español
- Código y commits: español o inglés según contexto

## Reglas editoriales
- Tono: análisis de largo plazo, independiente, accesible
- Sin sensacionalismo ni hype
- Datos verificados, fuentes citadas
- European number format (1.000,50)

## Stack
- Plataforma: [POR DECIDIR — Ghost / Substack / Beehiiv]
- Social: LinkedIn
- Afiliados: Amazon España
- Analytics: [POR DECIDIR]

## Output
- Artículos: content/drafts/ → content/published/
- Assets: assets/
```

**Paso 5 — Primer commit**
```bash
git add -A
git commit -m "Initial project setup: robotica newsletter

Changes: project structure, CLAUDE.md, docs framework

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
git push
```

**Paso 6 — Configurar Claude Code**
- Abrir Claude Code apuntando al nuevo repo
- Los MCP servers se heredan del global settings si están configurados
- Las reglas de RRP-DEV NO aplican — el nuevo repo tiene su propio CLAUDE.md

### Qué hereda de RRP-DEV (solo lo genérico)
- Convenciones de commit (formato, Co-Authored-By)
- Literate code rules (si hay Python)
- MCP servers útiles: Firecrawl (scraping), Playwright (testing web), Gmail
- Estructura `.claude/` (memory, commands, rules)

### Qué NO hereda
- Todo lo HBX: Tableau, CR%, validator, PPTX charts, data rules, design system
- Skills de HBX (platinum-weekly, governance-call, etc.)
- Output paths ($HBX_OUTPUT, $HBX_VAULT)

---

## 10. Obsidian — Sección de Nivel Superior `05_Personal/`

### Estructura completa (ver Sección 8D para detalle de Knowledge Management)

```
05_Personal/
  05-01_Robotica Newsletter/
    Proyecto Robótica Newsletter.md     # MOC principal (Map of Content)
    Calendario Editorial.md
    Decisiones.md

    Issues/                             # Backup de cada issue
      EP001 - 2026-MM-DD/
        Draft.md | Research Notes.md | Social Posts.md

    Research/                           # Auto-generado por script + clippings manuales
      Research Digest YYYY-MM-DD.md
      Clippings/

    Wiki/                               # BASE DE DATOS CRECIENTE
      Robots/                           # Una nota por robot (Neo, Roomba, etc.)
      Empresas/                         # Una nota por empresa (Figure AI, iRobot, etc.)
      Conceptos/                        # Temas evergreen (LIDAR, privacidad, precios)
      Mercado/                          # Datos acumulativos (precios, SEO, competencia)

    Métricas/                           # Suscriptores, tráfico, ingresos
    Templates/                          # Plantillas Obsidian
    _deliverables/
    _archive/
```

### Frontmatter
```yaml
---
type: project
built-with: claude
tags: [personal, robotica, newsletter]
---
```

### Por qué `05_Personal/` y no vault nuevo
- `01_Projects` es HBX profesional → separación clara
- Búsqueda unificada, links cruzados posibles, un solo Syncthing (3 dispositivos ya configurados)
- Si en el futuro tienes más proyectos personales, ya tienes la sección
- Migrar a vault propio siempre es posible si escala mucho

---

## 11. Implementación — Pasos Ordenados

### Fase 0: Setup inicial (hoy — desde RRP-DEV)
1. Guardar documentación de research en `docs/` de este plan (referencia)
2. Guardar memoria del proyecto en RRP-DEV (referencia cruzada al nuevo repo)
3. Crear estructura `05_Personal/05-01_Robotica Newsletter/` en Obsidian vault
4. Crear nota principal del proyecto en Obsidian

### Fase 0.5: Crear repo dedicado (Rafael, manual)
5. Seguir instrucciones de la Sección 9 para crear repo en GitHub
6. Clonar en local, crear estructura de carpetas
7. Configurar CLAUDE.md base
8. Migrar los dos archivos originales desde Google Drive a `docs/` y `assets/`
9. Primer commit

### Fase 1: Decisiones fundamentales ✓ (completada 2026-04-12)
10. ~~Verificar disponibilidad de dominios~~ → robohogar.com disponible y comprado
11. ~~Decidir nombre definitivo~~ → **ROBOHOGAR**
12. ~~Decidir plataforma~~ → **Substack** (migración a Ghost cuando escale)
13. ~~Comprar dominio~~ → **robohogar.com** comprado

### Fase 2: Infraestructura web (semana 2-3)
14. Configurar plataforma elegida (Ghost/Substack/Beehiiv)
15. Adaptar la landing page HTML al tema de la plataforma
16. Configurar newsletter (formulario de suscripción)
17. Alta en Amazon Afiliados España
18. Configurar Google Analytics / Plausible
19. Crear perfil LinkedIn para el proyecto (o usar el personal)

### Fase 2B: Infraestructura de automatización (semana 3-4)
20. Configurar Buffer (6€/mes) — LinkedIn + X + Threads
21. Configurar Make.com (9€/mes) — flujo RSS → Claude API → Buffer
22. Crear `utilities/research_aggregator.py` en el repo
23. Configurar Google Alerts (7 alertas RSS)
24. Configurar RSS feeds en el script de agregación
25. Instalar plugins Obsidian: Templater, Dataview, QuickAdd, Omnivore
26. Crear templates en Obsidian (Issue, Research Digest, Robot Wiki, Empresa Wiki)
27. Test completo del pipeline: script agrega → digest en Obsidian → Claude draft → publicar → Make.com → Buffer → social

### Fase 3: Contenido base (mes 1-2)
28. Ejecutar primera agregación de research → primer digest en Wiki
29. Escribir 5 artículos evergreen antes del lanzamiento público
30. Configurar SEO básico (meta descriptions, sitemap, keywords)
31. Crear lead magnet PDF ("Guía 2026: Todo sobre robots para casa")
32. Poblar Wiki con las primeras 10-15 notas de robots y empresas

### Fase 4: Lanzamiento (mes 2)
33. Publicar web
34. Primer newsletter de bienvenida (EP.001)
35. Automatización social se activa automáticamente (Make.com + Buffer)
36. Contactar Integrarobot, IA en Español, EvolupedIA para cross-promotion

### Fase 5: Ritmo de crucero (mes 3+)
37. Publicación quincenal consistente (roundup + artículo original alternando)
38. Wiki crece automáticamente con cada research digest
39. SEO monitoring (Google Search Console)
40. Evaluar métricas cada trimestre (subs, tráfico, open rate, social reach)
41. Activar afiliados Amazon cuando las guías de compra rankeen
42. Refinar system prompt de Claude con tu voz real (cada 2 meses)

---

## Verificación

- **Obsidian:** verificar que `05_Personal/05-01_Robotica Newsletter/` existe y tiene la nota principal
- **Memoria RRP-DEV:** verificar que el proyecto queda registrado en `.claude/memory/` con referencia al nuevo repo
- **Repo nuevo (manual por Rafael):** seguir instrucciones Sección 9, verificar con `ls -la` que la estructura está completa
- **Documentación:** guardar research de mercado como `.md` referencia en el nuevo repo
