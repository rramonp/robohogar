# Estrategia de Automatización — TUROBOT

## Principio clave
**Automatizar todo EXCEPTO juicio editorial y voz.** Esas dos cosas son lo que hace que una newsletter merezca la suscripción.

## Pipeline completo por issue (cada 2 semanas, ~3 hrs tú)

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

---

## 1. Research Aggregation (script Python)

### Script: `utilities/research_aggregator.py`
Se ejecuta quincenalmente (manual o cron):

1. **Fetch RSS feeds** (feedparser library):
   - Tier 1: IEEE Spectrum Robotics, The Robot Report, TechCrunch Robotics, The Verge
   - Tier 2: r/RobotVacuums (RSS bridge), newsrooms iRobot/Roborock/Ecovacs/Dreame
   - Tier 3: Xataka (robotics), Xataka Smart Home, ComputerHoy domótica

2. **Filtra** últimos 14 días, deduplica por similitud de título (fuzzy matching)

3. **Firecrawl API** scraping de top 10-15 artículos más relevantes (full text markdown)

4. **Claude API** categoriza y puntúa:
   - Categorías: Consumer Robots, Robot Vacuums, Lawn Robots, Humanoids, AI/Software, Industry, Reviews
   - Relevancia: 1-5 para newsletter de robótica doméstica española
   - Genera resumen de 1 línea por artículo

5. **Output:** `05_Personal/05-01_Robotica Newsletter/Research/Research Digest YYYY-MM-DD.md` en Obsidian

6. **Coste:** ~0€ (Firecrawl free 500 créditos/mes + Claude API ~$0.10/run)

### Google Alerts (7 alertas, RSS semanal)
```
"home robot" OR "robot doméstico"
"robot vacuum" OR "robot aspirador" 2026
"humanoid robot" home OR consumer
"robótica doméstica"
iRobot OR Roborock OR Ecovacs announcement
Tesla Bot OR Figure OR Boston Dynamics consumer
"robot cortacésped"
```

---

## 2. Content Creation (Claude-assisted)

### System prompt para borradores (personalizar con tu voz)
```
Eres el editor de TUROBOT, una newsletter en español sobre robótica doméstica.
Tono: directo, con opinión, sin hype. Como hablar con un amigo que sabe de tech.

PROHIBIDO:
- "En el vertiginoso mundo de..." / "En la era de..."
- "Es importante destacar que..." / "Sin duda alguna..."
- "En este sentido..." / "Un enfoque holístico..."
- Frases que empiecen con "Como [profesional], sabemos que..."
- Hedging: "podría ser", "quizás", "es posible que" (toma partido)

OBLIGATORIO:
- Empezar con imagen concreta o anécdota, nunca frase genérica
- Mezclar frases cortas con largas
- Opiniones fuertes: "Este robot es una estafa a 800€"
- Español coloquial natural cuando proceda
- Datos específicos (precios, fechas, specs)
```

### Técnicas anti "voz de IA"
- TÚ escribes el ángulo/opinión en 1 frase → Claude desarrolla
- TÚ añades anécdotas personales, humor, referencias locales
- TÚ eliminas todo lo que suene a "IA resumiendo nota de prensa"
- Referencia experiencia real (IA no puede generar esto)
- Discrepa del consenso — IA siempre hedgea, tú tomas partido

---

## 3. Social Media Automation (Make.com + Buffer)

### Plataformas
| Plataforma | Prioridad | Automatizable | ROI |
|---|---|---|---|
| **LinkedIn** | ALTA | Sí | Alto — profesionales tech España |
| **X/Twitter** | ALTA | Sí | Alto — descubrimiento, comunidad robótica |
| **Threads** | MEDIA | Sí | Medio — creciente pero inestable |

### Flujo Make.com (~9€/mes)
```
Trigger: RSS del newsletter (nueva issue publicada)
    ↓
Módulo 1: Parsear RSS → extraer título, resumen, link
    ↓
Módulo 2: HTTP request a Claude API
    - Genera: LinkedIn (300 palabras), X (280 chars × 3), Threads (500 chars)
    ↓
Módulo 3: Router paralelo
    ├→ Buffer API: LinkedIn (martes 9:00 CET)
    ├→ Buffer API: 3 posts X (repartidos en 3 días)
    └→ Buffer API: Threads (miércoles)
    ↓
Módulo 4: Email notificación con preview
```

### De cada issue se generan automáticamente:
- 1 post largo LinkedIn (insight + opinión + CTA)
- 3-5 posts X (hot take por tema + link)
- 1 hilo X (historia principal en 5-7 posts)
- 1 post Threads

### Herramientas
- **Buffer** ($6/mes Essentials) — scheduling LinkedIn + X + Threads
- **Make.com** ($9/mes Core) — flujo RSS → Claude → Buffer
- **Alternativa simple:** dlvr.it ($9.99/mes) — RSS-to-social directo, más simple pero sin IA

---

## 4. Knowledge Management en Obsidian

### Principio: nada de research es one-shot
Todo alimenta una Wiki acumulativa. Cada dato se cataloga y es reutilizable.

### Wiki auto-creciente
Cada Research Digest procesado:
1. Script detecta robots/empresas mencionados
2. Si no existe nota Wiki → crea desde template
3. Si existe → añade bullet con noticia + fecha + fuente
4. Las notas acumulan info progresivamente

### Flujo de conocimiento
```
Fuentes externas (RSS, Alerts, web)
    ↓
Research Digest (auto) ──→ Wiki/ se enriquece
    ↓
Tú seleccionas temas para el issue
    ↓
Escribes artículo (linkando a Wiki)
    ↓
Publicado ──→ Issues/ (backup) + Wiki/ (se enriquece) + Métricas/
    ↓
Próximo issue: Wiki ya tiene contexto → escribes MÁS RÁPIDO
```

### Plugins Obsidian
| Plugin | Función |
|---|---|
| Templater | Auto-crear estructura de cada issue |
| Dataview | Queries: "robots con precio < 5000€" |
| QuickAdd | Captura rápida de links a Wiki |
| Omnivore/ReadItLater | Web clipping → Research/Clippings |

---

## Stack y costes

| Componente | Herramienta | Coste/mes |
|---|---|---|
| Newsletter + blog | TBD | 0-25€ |
| Dominio | .es | ~1€ |
| Social scheduling | Buffer | 6€ |
| Automatización | Make.com | 9€ |
| Research scraping | Firecrawl free | 0€ |
| Claude API | Research + social | ~1€ |
| Obsidian | Free | 0€ |
| **Total** | | **~17-42€/mes** |

## Tiempo por issue: ~3 hrs
| Paso | Tiempo |
|---|---|
| Escanear digest + curar | 15 min |
| Escribir ángulos | 15 min |
| Claude genera borrador | 10 min |
| Editar + personalidad | 75 min |
| Formatear + publicar | 15 min |
| Revisar cola social | 10 min |
| Engagement (opcional) | 20 min |
| **Total** | **~2.5-3 hrs** |
