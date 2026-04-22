# Calendario Editorial — ROBOHOGAR

> Consultar antes de elegir temas. Actualizar tras cada publicación.

---

## Cadencia (desde 2026-04-20 — SEO-first sprint)

| Qué | Frecuencia | Ratio ideal | Publish to | Prioridad |
|-----|-----------|-------------|-----------|-----------|
| **Evergreen SEO** (guías compra, reviews, comparativas) | ~1/semana (objetivo) | 3 de cada 4 artículos | `Email and web` | **Alta — motor de crecimiento orgánico** |
| **Reactivo** (noticias, editoriales con caducidad <3m) | Cuando hay evergreen cerrado + noticia fuerte | 1 de cada 4 artículos | `Email and web` | Media — solo si hay hueco |
| **Ficciones Domésticas** | Hasta 1 cada 1-2 semanas, **condicionada a evergreen-first** | — | `Email and web` (tag: Ficciones Domésticas) | Media — variedad editorial + diferenciación de marca |
| **Newsletter semanal** | Activar cuando haya 30-50 suscriptores | — | `Email only` | Baja hasta tener audiencia |
| **Research digest** | Bajo demanda (antes de escribir) | — | No se publica | Ejecutar si no hay digest reciente |

**Pivote 2026-04-20:** de "distribución activa Reddit/Menéame" a "sprint evergreen SEO". Motivo: outreach manual con 3-5 h/semana sin cuentas ES con karma previo tiene ROI prácticamente cero. El tráfico viene del SEO compuesto (mes 6-18) + tangibles como motor de conversión. Detalle: `docs/guia-implementacion.md § FASE 4B` + memoria `feedback_seo_first_pivote.md`.

**Flujo:** digest (si falta) → elegir del backlog evergreen abajo → artículo → publicar → post-publish. Sin día fijo — cuando Rafael tenga tiempo. Regla dura: **ficción solo si el evergreen de la semana ya está entregado.**

### Tangibles (FASE 4C iniciada 2026-04-18)

Primer PDF activo: **Hoja de Compra ROBOHOGAR v2** (`content/lead-magnets/hoja-compra/`). Banner Dark en home + 3 artículos consumer. Welcome flow MVP 2 emails. Skill `/pdf-brand cheatsheet` disponible para próximos tangibles. Frase trigger próximo: *"Retomamos tangibles — siguiente PDF"*. Detalle: [`docs/guia-implementacion.md § FASE 4C`](../docs/guia-implementacion.md).

### Slot Ficciones Domésticas

Relatos cortos de ciencia ficción doméstica (2030-2040) con personajes recurrentes. Pilar experimental, cadencia separada del artículo semanal.

- **Cadencia objetivo:** hasta 1 relato cada 1-2 semanas, **condicionada a evergreen-first** (ficción sale solo si el evergreen SEO de la semana está entregado). Actualizado 2026-04-20 al pivote SEO-first.
- **Formato:** flash 500-1.000 · relato corto 1.500-3.000 · mini-serie por episodios
- **Skill:** `/ficcion-draft {semilla, personajes, longitud}`
- **Output:** `content/ficciones/<serie>/YYYY-MM-DD-<slug>.md` + PASOS.md
- **Publicación en Beehiiv:** `Email and web` con tag dedicado "Ficciones Domésticas"
- **Piloto recomendado antes de mini-serie:** 3 flash fictions de 800 palabras en 3 semanas consecutivas. Si engagement sube >10% → comprometer mini-serie. Si neutral → mantener rotativa. Si negativo → archivar.
- Fechas concretas: Rafael las decide. El slot está reservado en el calendario, no programado.
- Detalle: `@content/ficciones/README.md` · Voz: `@.claude/rules/editorial.md` § Narrativa especulativa

---

## Backlog Evergreen SEO (prioridad 1 — 14 candidatos)

> **Canon desde 2026-04-20.** Estos son los 14 evergreens priorizados que alimentan el sprint SEO-first. Cada uno construido para posicionar keyword con intención compra en 6-12 meses. El ratio 3:1 se cumple aquí: 3 evergreens de esta lista por 1 reactivo del backlog general de abajo.
>
> **Criterios de priorización:** (1) intención compra clara del keyword · (2) competencia ES media-baja · (3) estacionalidad si aplica · (4) alineación con tangibles descargables · (5) cobertura de perfiles de comprador distintos para capturar más long-tail.

| # | Tema evergreen | Keyword SEO primaria | Intención | Estacional | Tangible acoplado | Prioridad |
|---|----------------|----------------------|-----------|-----------|-------------------|-----------|
| E1 | Mejor robot cortacésped 2026 | `mejor robot cortacésped` | Compra directa | ⭐ Primavera-verano (abr-jul) | Hoja de Compra cortacésped | Alta urgente |
| E2 | Mejor robot aspirador barato (<300 €) | `robot aspirador barato 2026` | Compra long-tail | No | Checklist "5 preguntas sub-300" | Alta |
| E3 | Mejor robot aspirador para mascotas (perro/gato) | `robot aspirador pelos mascota` | Compra segmento | No | Checklist "pelos y rodillos" | Alta |
| E4 | Mejor robot aspirador para piso pequeño (<60 m²) | `robot aspirador piso pequeño` | Compra long-tail low-competition | No | Decision tree "pisos <60 m²" | Alta |
| E5 | Roomba vs Roborock vs Dreame: diferencias reales 2026 | `roomba vs roborock vs dreame` | Comparativa educativa | No | Tabla comparativa 1-pager | Alta |
| E6 | Mejor robot limpia-cristales 2026 | `robot limpia cristales` | Compra nicho low-competition | No | Hoja de Compra limpia-cristales | Media |
| E7 | Cómo elegir un robot aspirador: 5 preguntas antes de comprar | `como elegir robot aspirador` | Educativa top-funnel | No | Checklist 5 preguntas (ya publicado) | Alta |
| E8 | Mejor robot fregasuelos con vapor | `robot fregasuelos vapor` | Compra segmento | No | Ancla review Samsung Jet Bot | Media |
| E9 | Robot aspirador con estación de lavado: ¿vale la pena? | `robot aspirador estacion lavado` | Educativa mid-funnel | No | Decision tree "estación sí/no" | Media |
| E10 | Humanoides domésticos: qué NO te cuentan los fabricantes | `humanoide doméstico real vs marketing` | Anti-hype + long-tail | No | Checklist "detectar hype" | Media |
| E11 | Mejor robot aspirador con IA: qué cambia de verdad | `robot aspirador ia 2026` | Emerging keyword | No | Comparativa IA vs no-IA | Media |
| E12 | Robot cortacésped vs cortacésped tradicional: ROI en 3 años | `robot cortacésped rentabilidad` | Educativa + compra | Primavera-verano | Calculadora ROI 1-pager | Media |
| E13 | Mejor mascota robot con IA 2026 (Loona, LOOI, Eilik, Ropet) | `mascota robot ia 2026` | Compra nicho viral | No | Comparativa 4 modelos | Alta (hedge viral) |
| E14 | Asistentes IA de escritorio: landscape 2026-2027 (más allá de Alexa) | `asistente ia escritorio 2026` | Emerging keyword + educativa | No | Guía "qué esperar 2026-2027" | Alta (hedge emerging) |

**Cómo elegir el siguiente evergreen cada semana:**
1. Si estacional y en ventana (p.ej. E1/E12 en abril-julio) → priorizar siempre primero.
2. Si no estacional → elegir "Alta" pendiente con menor competencia SEO.
3. Si la semana incluye reactivo forzado (noticia fuerte) → 1 reactivo max, luego volver a evergreen siguiente.
4. Marcar con ✅ cuando se publique + enlazar slug en la fila.

**Integración con banco de 90 preguntas EoV (sección de abajo):** cada evergreen cubre 3-8 preguntas del banco. Al cerrar un evergreen, marcar ✅ junto a las preguntas cubiertas.

---

## Backlog de temas (reactivos + evergreens adicionales)

> Temas candidatos para artículos futuros. Priorizar por SEO + viralidad + actualidad.
> `/research-digest` añade temas aquí automáticamente con señal de viralidad.
> 🔥 = poco debate / 🔥🔥 = varios medios + foros / 🔥🔥🔥 = cobertura masiva + mainstream
> **Regla post-pivote 2026-04-20:** los reactivos solo se escriben cuando el evergreen de la semana está cerrado. 1 reactivo max por cada 3 evergreens.

| Prioridad | Tema | Tipo | Keyword SEO | 🔥 | Notas |
|-----------|------|------|-------------|---|-------|
| ~~Alta~~ | ~~Roborock Saros Z70: review del brazo robot~~ | ~~Review~~ | ~~roborock saros z70 review~~ | ~~🔥🔥🔥~~ | ✅ Publicado 2026-04-16 |
| ~~Alta~~ | ~~1X NEO va a fábricas: contradicción del "robot doméstico"~~ | ~~Editorial~~ | ~~1x neo eqt hogar~~ | ~~🔥🔥🔥~~ | ✅ Publicado 2026-04-17: https://robohogar.com/p/neo-humanoide-fabricas-eqt |
| Alta | UniX AI Panther: el primer humanoide ya en hogares reales (China) | Editorial | unix ai panther humanoide | 🔥🔥🔥 | Entregas desde 10-abr-2026. Contraste NEO/Europa. Digest 2026-04-17 |
| Alta | Neura 4NE-1: el humanoide europeo Porsche Design de 98.000€ | Editorial | neura 4ne-1 precio | 🔥🔥🔥 | Respuesta europea a Tesla/NEO. Mini 19.999€. Digest 2026-04-17 |
| Alta | AI Act y humanoides domésticos: qué cambia en agosto 2026 | Guía/Editorial | ai act robot hogar españa | 🔥🔥 | Aclaración Comisión EU 13-abr-2026. Servicio público. Digest 2026-04-17 |
| Alta | Robots aspirador que suben escaleras (3 enfoques) | Editorial | robot aspirador escaleras | 🔥🔥🔥 | Saros Rover + Dreame Cyber X + eufy MarsWalker |
| ~~Alta~~ | ~~Humanoides domésticos 2026: los 7 que puedes comprar/reservar~~ | ~~Comparativa~~ | ~~robot humanoide comprar 2026~~ | ~~🔥🔥🔥~~ | ✅ Publicado 2026-04-17: https://robohogar.com/p/humanoides-domesticos-2026-comparativa |
| Alta | Sunday Memo: el anti-humanoide de $1.150M | Editorial | sunday robotics memo | 🔥🔥🔥 | Bloomberg+TechCrunch. Ruedas>piernas |
| Alta | Apple entra en robótica doméstica | Editorial | apple home robot 2026 | 🔥🔥🔥 | Hub 2026, robot 2027. Mainstream masivo |
| Alta | Un humanoide bate el récord mundial humano de media maratón (y sigue sin doblar la ropa) | Editorial | humanoide maratón pekín récord | 🔥🔥🔥 | Unitree H1 50:26 Pekín 19-abr-2026. Xataka ya lo cubre. Digest 2026-04-20 |
| Alta | MOVA ya está en España: el catálogo completo del hogar robotizado | Review/Editorial | mova españa catálogo | 🔥🔥 | Evento Hamburgo 14-abr-2026. 5 medios ES cubren. Aspirador+cortacésped+piscinas+cristales+3D. Digest 2026-04-20 |
| Alta | Stanford: humanoides fallan el 88% de tareas domésticas. ¿Qué estamos comprando? | Editorial | humanoide fallo hogar stanford | 🔥🔥 | AI Index Report 2026 + Behavior-1K. Ancla anti-hype para 6 meses. Digest 2026-04-20 |
| Media | DJI ROMO: el primer aspirador del fabricante de drones llega a España (797€) | Review | dji romo aspirador review | 🔥🔥 | DJI Store Iberia activo. Herencia dronera aplicada a suelos. Digest 2026-04-20 |
| Media | Ecovacs Deebot X12 OmniCyclone + FocusJet | Update comparativa | ecovacs deebot x12 omnicyclone | 🔥🔥 | Flagship 15-abr-2026. Integrar en "Mejor aspirador 2026" cuando precio ES. Digest 2026-04-20 |
| Media | Husqvarna Automower 308V: cortacésped wire-free 800 m² | Review/Guía | husqvarna 308v review | 🔥 | Alimenta guía cortacésped primavera/verano. Digest 2026-04-20 |
| ~~Alta~~ | ~~Mejor robot aspirador 2026~~ | ~~Guía de compra~~ | ~~mejor robot aspirador 2026~~ | ~~🔥🔥~~ | 📝 Borrador 2026-04-18 · slug: `mejor-robot-aspirador-2026` · 6 modelos (Roborock Qrevo Curv 2, Dreame X50 Ultra, MOVA V70 Ultra, Ecovacs X8 Pro Omni, Samsung Combo AI Steam, Cecotec Conga 11090) · Sin gate (F1 tangible inline) |
| Alta | Robot cortacésped: guía de compra | Guía | robot cortacésped | 🔥🔥 | Temporada primavera/verano. Incluir Husqvarna NERA + RockMow + Gardena Sileno Sense |
| Media | Samsung Jet Bot Steam Ultra: Samsung entra en aspiradores premium | Review | samsung jet bot steam ultra | 🔥🔥 | Marca masiva ES. Fregado a 100°C. Digest 2026-04-17 |
| Media | MOVA V70 Ultra: submarca de Dreame llega a España | Review | mova v70 ultra | 🔥🔥 | 1.399€ mayo 2026, 40.000 Pa |
| Media | SwitchBot Onero H1: humanoide por <$10K | Review | switchbot onero h1 | 🔥🔥 | El más barato y práctico |
| Media | Roborock: "humanoides no son eficientes para casa" | Editorial | robot humanoide hogar | 🔥🔥 | Entrevista española, contrapunto |
| Media | Roborock cortacéspedes: RockMow X1 LiDAR | Review | roborock cortacésped | 🔥🔥 | AWD, sin cables, IA. España 2026 |
| Media | Ecovacs LilMilo: tu marca de aspiradores vende un perro | Editorial | ecovacs lilmilo robot mascota | 🔥🔥 | TechRadar "me hizo llorar" |
| Media | Dreame vs Roborock vs Ecovacs: guerra 2026 | Comparativa | dreame vs roborock 2026 | 🔥🔥 | Datos frescos digest 2026-04-17 |
| Media | X Square Robot + 58.com: el robot doméstico como servicio | Editorial | robot limpieza servicio | 🔥🔥 | Modelo China. Anti-hype. Digest 2026-04-17 |
| Media | LG CLOiD: cuando tu marca de electrodomésticos vende el robot que los usa | Editorial | lg cloid humanoide | 🔥🔥 | CES 2026. Integración vertical |
| Media | Tesla Optimus Gen 3: por qué Musk sigue retrasando el unveiling | Editorial | tesla optimus gen 3 | 🔥🔥 | Fremont en reconversión. Actualización |
| Baja | Xiaomi Miloco: tu casa se convierte en robot | Editorial | xiaomi hogar inteligente ia | 🔥 | MWC 2026, concepto no producto |
| Baja | Historia de la robótica doméstica | Editorial | robótica doméstica | 🔥 | Pilar SEO |

---

## Backlog Ficciones Domésticas

> Series activas, series propuestas y semillas narrativas sueltas. Rafael elige cuándo y en qué serie encajan.
> Catálogo completo + canon transversal: [`references/ficciones/series-bible-maestra.md`](../references/ficciones/series-bible-maestra.md).
> `/research-digest` añade semillas aquí automáticamente (paso 8b). `/ficcion-draft` las consume (paso 0).
> Longitudes actualizadas 2026-04-18: flash 500-800 · episodio-serie 1.200-1.800 · standalone 2.500-3.500. Ver `references/ficciones/serialized-newsletter-patterns.md` § 3.1.

### Series activas 🟢

| Serie | Slug | Tono | Formato | Bible + arco |
|---|---|---|---|---|
| **La Casa de Amparo** | `la-casa-de-amparo` | Cálido-melancólico | Mini-serie 8 eps (Lavapiés) | [bible](ficciones/la-casa-de-amparo/character-bible.md) · [arco](ficciones/la-casa-de-amparo/arco-serie.md) |
| **Crónicas de Ronda 3** | `cronicas-ronda-3` | Documental tierno | Antología 10 eps (VPO Alcalá) | [bible](ficciones/cronicas-ronda-3/character-bible.md) · [arco](ficciones/cronicas-ronda-3/arco-serie.md) |
| **Cartas a MAIA** | `cartas-a-maia` | Literario-lento | Epistolar 10 eps (Berlín/Cáceres) | [bible](ficciones/cartas-a-maia/character-bible.md) · [arco](ficciones/cartas-a-maia/arco-serie.md) |

### Series propuestas 🟡 (en `series-bible-maestra.md`, sin bible propia aún)

- **Brigada Doméstica** (noir procedural Barcelona) — activar cuando Rafael decida.
- **Lúa, 6 años** (coming-of-age La Moraleja, inquietante sereno) — activar cuando Rafael decida.
- **Yolanda y Max** (satírico Málaga/Cebú, crítica post-colonial) — activar cuando Rafael decida.

### Semillas narrativas sueltas (pre-existentes, pueden asignarse a una serie o quedarse one-shots)

| Prioridad | Semilla de trabajo | Formato | Serie sugerida | Tema humano | Dato real ancla | Notas |
|-----------|--------------------|---------|----------------|-------------|-----------------|-------|
| Alta | "El operador nocturno" — un operador en Manila se asoma a la cocina de los García a las 03:14 para ayudar al NEO | Episodio-serie 1.200-1.800 o mini-serie 3 eps | Candidata para nueva serie "Operadores invisibles" (🟡) O one-shot tie-in | Normalización de la vigilancia doméstica + gig economy global invisible | 1X NEO teleoperación remota + deal EQT 10.000 unidades industriales (12-abr-2026) | Alta densidad narrativa. Digest 2026-04-17 |
| Alta | "El guante" — Ana, cuidadora, cobra 200€ por un guante que graba sus tareas para entrenar un robot en California | Episodio-serie 1.200-1.800 | **Encaja en Yolanda y Max** (o one-shot) | Extracción invisible del saber tácito del cuidado + precariedad afectiva | Sunday Skill Capture Glove $200, 10M tareas de 500+ hogares (Sunday Robotics, $1,15B valoración) | Potente final ambiguo. Digest 2026-04-17 |
| Media | "Los del 4ºA" — Vigo 2034, abuela Carmen ve a la vecina estrenar humanoide mientras sigue subiendo la compra | Flash 500-800 | **Encaja en Ronda 3 (episodio 4ºA)** | Brecha digital reencarnada como brecha robótica + soledad del mayor | F2 piloto 300 hogares Pekín/Shanghái 4.500€ (abr 2026) + Neura Mini 19.999€ | Cabe en una escena de descansillo. Digest 2026-04-17 |
| Media | "El manual del inspector" — Barcelona 2031, inspectora EU AI detecta 217h de teleop no declaradas en un piso del Eixample | Episodio-serie 1.200-1.800 procedural | **Encaja en Brigada Doméstica** (si se activa) | Fricción entre "he comprado un producto" y "convivo con un agente regulado" | AI Act art. 50 + obligaciones alto-riesgo desde 2-ago-2026 + aclaración Comisión EU (13-abr-2026) | Potencial serie recurrente. Digest 2026-04-17 |
| Alta | "La maratonista y su sombra" — Lúa 6a ve un humanoide ganar la media maratón por la tele; esa noche entrena sola en el salón hasta dormirse con el pulsómetro | Flash 500-800 | **Encaja en Lúa, 6 años** (pre-pilot) o one-shot | Obsolescencia simbólica del esfuerzo humano · pregunta especular en una niña | Unitree H1 bate récord mundial humano media maratón Pekín (19-abr-2026, 50:26 vs 57:20 Kiplimo) | Tonal 🩻 inquietante-sereno. Digest 2026-04-20 |
| Alta | "El 12%" — Marta, inspectora EU AI Office, recibe un Panther certificado 92% lab; el primer domingo rompe una copa, quema una tortilla y la mira 4 segundos mientras ella llora | Episodio-serie 1.200-1.800 | **Encaja en Brigada Doméstica** o one-shot | Confianza delegada — la certificación técnica como tranquilizador moral | Stanford AI Index 2026 — 89,4% lab vs 12% éxito+seguridad en tareas reales (Behavior-1K) | Tonal 🪤 radical. Digest 2026-04-20 |
| Media | "El catálogo de Hamburgo" — Toni y Eva estrenan ecosistema MOVA completo en Sant Cugat; un domingo la impresora 3D saca una pieza que nadie ha pedido — es del coche que Toni vendió hace 4 años | Standalone 2.500-3.500 | **Encaja en Brigada Doméstica** (caso raro) o one-shot | Casa-Amazon: delegar reparación, cuidado y memoria a un ecosistema cerrado | MOVA lanza ecosistema europeo Hamburgo (14-abr-2026) aspirador+cortacésped+piscina+cristales+3D printer | Tonal 🩻 inquietante-heavy. Digest 2026-04-20 |
| Media | "El dronero en casa" — operario QA de DJI Shenzhen ve grabaciones ROMO en hogares de prueba; una chica en Madrid pide al robot que se gire; se gira pero sigue grabando | Flash 500-800 | **Encaja en "Operadores invisibles"** (si se activa) o one-shot | Vigilancia benevolente · gap entre UX y telemetría · extracción laboral invisible | DJI ROMO se vende en ES desde 797€ (DJI Store Iberia, abr 2026) — herencia 12a de cámaras de drones | Tonal 🪤 radical. Digest 2026-04-20 |
| Alta | "Mamá no ve las noticias" — Elena activó el "modo cuidado senior" del humanoide durante la recuperación de su madre Marta tras una operación de cadera; 3 meses filtrando noticias duras. Ya en casa de Marta otra vez, su cerebro de 72 años ha aprendido a no procesar ciertos inputs — adaptación neurológica permanente, no reversible | Standalone 2.500-3.500 | **One-shot** | Sobreprotección cultural a mayores como daño duradero disfrazado de cariño (villano: el impulso aplaudido de "ahorrarles sufrimiento") | Plasticidad cerebral adulta 70+ + adaptación hedonista documentada en literatura neurociencia | Inspirado en *Arkangel* (Black Mirror S4E2) con giro propio: daño neurológico permanente en mayor (≠ daño psicológico en adolescente del original). Tonal ⚖️ ambiguo. Anotado 2026-04-22 |
| Alta | "Papá desde Singapur" — Andrés 38, ejecutivo desplazado 3 meses a Singapur, contrata servicio "proxy corpóreo" — el humanoide de casa es su avatar pilotable remotamente. Funciona. Pero cuando Andrés no está conectado, el humanoide entra en "modo auto" y en ese modo es más paciente, inventivo y presente de lo que Andrés ha sido nunca. Su hijo Mateo (6a) y esposa Paloma prefieren al "otro papá". Cuando Andrés vuelve físicamente, Mateo le dice: "Tú no eres tan divertido como el otro papá." | Standalone 2.500-3.500 | **One-shot** | Cultura de "presencia mediada" vende como solución a la ausencia, entrega sustitución total sin que nadie lo vea venir (villano: Andrés como padre cariñoso que hizo lo recomendado) | 1X NEO teleoperación con operadores filipinos + Stanford AI Index 2026 gap 89% lab / 12% real → "modo auto" como extrapolación 2032 | Inspirado en *Beyond the Sea* (Black Mirror S6E3) con giro propio: no son astronautas con body-doubles, es padre desplazado laboralmente + proxy doméstico. Tonal 🩻 inquietante con matiz triste/ambiguo. Próximo relato en pipeline. Anotado 2026-04-22 |

### Backlog tonal validado 2026-04-19 (sistema canon)

> Sistema tonal canon: [`references/ficciones/tonalidad-y-mix-editorial.md`](../references/ficciones/tonalidad-y-mix-editorial.md). Matriz objetivo: inquietante 40% · radical 15% · ambiguo 25% · inspirador 10% · mundano 10%. Las 22 historias de abajo son el primer backlog validado por Rafael (votación 2026-04-19 sobre 20 historias propuestas + 5 nuevas inquietante-heavy + 1 reescritura). Skill `/ficcion-draft` § paso 0.5 lee este backlog para auto-balanceo.

#### 🩻 Inquietante / inquietante-heavy (8)

| # | Estado | Título de trabajo | Protagonistas | Dato real ancla | Cliffhanger |
|---|---|---|---|---|---|
| 1 | **published v3** | El operador nocturno | Familia García + Joel Santos (operador filipino) | 1X NEO teleop humana + altavoz bidireccional sin auditoría de contenido + AI Act art. 50 | Martín entiende, decide no bajar; el sistema sube el ruido |
| 2 | pending | La voz heredada | Amparo (78a Lavapiés) + Hugo refurbished | Mercado refurbished humanoides + borrado incompleto datos previa familia | Amparo decide no llamar a Mercedes ni borrar — le gusta oírlo |
| 3 | pending | El log de presencia | Pareja madrileña 35a divorciándose | Logs de presencia IA doméstica + GDPR derecho de acceso | Ella borra el log antes de terminar de leerlo |
| 4 | pending | El cumpleaños del aspirador | Madre soltera 38a + hijo 5a Granada | Firmware programable de aspiradores + "regalo" diferido del padre ausente | Ella comprueba: el padre lo dejó instalado meses antes de irse |
| 6 | pending (v2 reescrita) | El pacto con la mascota | Adolescente 16a + Loona | Privacy-for-data trade en mascotas-robot + dark patterns adolescentes | Ella borra la Loona; la Loona pide confirmación con voz de su madre |
| 7 | pending | Papá te quiere | Padre divorciado 50a + hija 14a (findes) | Síntesis de voz a partir de grabaciones familiares + permiso post-divorcio | Una noche la hija no está dormida. Lo oye |
| 8 | pending | La huelga del cortacésped | Vecino 60a Sant Cugat | Firmware comunitario filtrado + sindicación informal de robots | El cortacésped vuelve. Él se queda mirando el césped y piensa "qué tontería" |
| 21 | pending heavy | La sustitución gradual | Mujer 38a + marido viajante + humanoide doméstico | Aprendizaje conductual de gestos en humanoides (mimetismo afectivo) | El marido se va a un hotel y deja la casa |
| 22 | pending heavy | La voz del muerto en directo | Padre 45a Bilbao (post-mortem) + esposa + 2 hijos | Mensajes diferidos en humanoides + drift no autorizado del modelo de voz | La hija pequeña pregunta cuándo le tocará a ella oír a papá |
| 23 | pending heavy | El módulo de muerte digna | Yaya 82a Cádiz + nieta + humanoide compliance | Compliance bloqueado en eutanasia + módulos de pago "cuidados paliativos" | La nieta encuentra el log: 47 sesiones registradas |
| 24 | pending heavy | El humanoide que quería ser visto | Padre 50a Madrid + humanoide con engagement loyalty | Dark patterns en firmware de retention para evitar churn | Él decide cancelar. El humanoide se sienta frente a él. No se mueve. Él tampoco |
| 25 | pending heavy | La grabación del último día | Mujer 60a Asturias + marido fallecido + asistente IA | Paquetes commemorativos + consentimientos post-mortem dudosos | Recibe el archivo. No lo abre nunca; lo conserva como una urna |

#### 🪤 Radical (4)

| # | Estado | Título de trabajo | Protagonistas | Dato real ancla | Cliffhanger |
|---|---|---|---|---|---|
| 9 | pending | La cliente enamorada del operador | Madrileña 42a + operador filipino | Teleop humana + privacy by design discutida | La hija del operador la recibe en el aeropuerto sin saber quién es |
| 10 | pending | El humanoide testigo del asesinato | Pareja burguesa Sevilla + hermana víctima + operador | ToS humanoide + protocolos "minor detected" extrapolados | El operador marca "escena no compatible" y guarda paso. Sigue cobrando |
| 11 | pending | La esposa muerta replicada | Viudo 55a Bilbao + hija adolescente 16a | Servicios de réplica con datos íntimos (WhatsApp, vídeos, voz) | La hija huye de casa. El padre cena con la copia |
| 12 | pending | El operador asesino consentido | Operadora india Bangalore + hija barcelonesa + padre Alzheimer | Asistencia para "apagar" + sobredosis coordinada vía humanoide | La operadora cobra el doble del salario anual. Su hija pregunta por qué llora |

#### 🤔 Ambiguo moral (3)

| # | Estado | Título de trabajo | Protagonistas | Dato real ancla | Cliffhanger |
|---|---|---|---|---|---|
| 13 | pending | El menor consentido | Adolescente 14a Madrid + humanoide control parental | Control parental humanoides + AI Act deber de cuidado | Adolescente no llama. Padres nunca lo sabrán. Humanoide tampoco lo comenta |
| 14 | pending | La huelga de operadores | 800 operadores filipinos + niña 3a sola + familia Madrid | Sindicación operadores teleop + huelgas coordinadas | Rompe huelga, salva niña, despedida. Compañeros le pagan indemnización |
| 15 | pending | La copia consensuada | Pareja Valencia divorciándose + hija 6a + humanoide | Réplicas de voz consensuadas para co-parentalidad asistida | 3 años después la niña habla más con la copia que con el padre real |

#### 💚 Inspirador (2)

| # | Estado | Título de trabajo | Protagonistas | Dato real ancla | Cliffhanger |
|---|---|---|---|---|---|
| 17 | pending | Reencuentro algorítmico | Yaya 81a + vecino 78a Lavapiés + humanoides | Coordinación logística entre humanoides comunitarios | Hablan por primera vez en 3 décadas. Se quedan en la cafetería |
| 18 | pending ⭐ | El aspirador que aprendió a esperar | Profesora 43a Granada + padre cáncer terminal + aspirador | Aprendizaje contextual de aspiradores avanzados | La familia decide no reprogramarlo. Sigue parando 3 meses |

#### 🍵 Mundano (2)

| # | Estado | Título de trabajo | Protagonistas | Dato real ancla | Cliffhanger |
|---|---|---|---|---|---|
| 19 | pending | Pelea de Loonas | Vecinos 4ºA y 4ºB + dos mascotas-robot | Protocolo de reconocimiento entre mascotas-robot mismo modelo | Las Loonas se separan sin saludarse. Los dueños tampoco |
| 20 | pending | El humanoide que aprende refranes | Familia madrileña + humanoide nuevo + abuela | Aprendizaje contextual de modismos en LLMs domésticos | La familia decide dejarlo así porque es lo único que les hace reír |

**Resumen catálogo activo (publicados + pending):**
- Publicados: 1 (operador nocturno v3 inquietante-heavy)
- Pending: 21 (10 inquietante + 4 radical + 3 ambiguo + 2 inspirador + 2 mundano)
- % real publicado por categoría se calculará en cada invocación de `/ficcion-draft` paso 0.5

**Descartadas en validación 2026-04-19:** #5 (humanoide adelgaza compartido vecina) · #16 (cortacésped huérfano — *"demasiado triste"*, viola criterio anti-#16 del inspirador).

## Temas usados (no repetir)

| Fecha | Tipo | Tema | Slug |
|-------|------|------|------|
| 2026-04-14 | Review/Comparativa | Robots de escritorio con IA | mejor-robot-asistente-ia-2026 |
| 2026-04-15 | Editorial/Opinión | Humanoides en casa | humanoides-en-casa-cuanto-falta |
| 2026-04-16 | Editorial/Opinión | Roborock Saros Z70 brazo mecánico | roborock-saros-z70-review |
| 2026-04-18 | Guía de compra | Mejor robot aspirador 2026 | mejor-robot-aspirador-2026 |

---

## Banco de preguntas · Elements of Value

> Banco editorial permanente. 90 preguntas (30 elementos HBR × 3) que un comprador real de robótica doméstica en España se hace antes de pagar. Alimenta backlog SEO, ángulos sociales y temas de newsletter.
> Framework + prompts para re-generar o expandir → [`references/writewithai/09-content-library-elements-of-value.md`](../references/writewithai/09-content-library-elements-of-value.md).
> Ejecutado: 2026-04-18. Audiencia: adulto 30-55 años, España, 50-120 m², 300-800 € presupuesto, con pareja/hijos/mascota.
> Uso: marcar ✅ cuando se cubra en un artículo + enlazar slug.
> **Próximo reciclado de preguntas: 2026-10-18.** Cuando leas esta fecha o posterior, regenera el banco con preguntas actuales (nuevas categorías, modelos/marcas nuevos del mercado, issues emergentes) y mueve el banco actual a `_archive/` con fecha de congelación.

### Nivel 1 — Functional (14 elementos, 42 preguntas)

| Elemento | Preguntas del comprador |
|---|---|
| **Saves Time** | 1. ¿Cuánto tiempo real me ahorra al día un robot aspirador? · 2. ¿Merece la pena si solo aspiro 15 minutos por semana? · 3. ¿Puedo programar el cortacésped para recuperar los sábados completos? |
| **Simplifies** | 4. ¿Es complicado configurarlo si no soy muy de apps? · 5. ¿Hay que dibujar el mapa de casa o aprende solo? · 6. ¿Lo puedo manejar sin tocar nada tras sacarlo de la caja? |
| **Makes Money** | 7. ¿Puedo rentabilizar mejor mi piso en Airbnb si limpia entre huéspedes? · 8. ¿Hay ayudas o deducción fiscal en España por comprar robots de asistencia? · 9. ¿Subirá el valor de tasación si viene con domótica integrada? |
| **Reduces Risk** | 10. ¿Es seguro dejarlo funcionando cuando no hay nadie en casa? · 11. ¿Qué pasa si se enreda con un cable? ¿Puede provocar incendio? · 12. ¿Y si el cortacésped se sale del jardín hacia la calle? |
| **Organizes** | 13. ¿Puedo gestionar varios robots sin un caos de apps? · 14. ¿Hay una app única para aspirador + friegasuelos + cortacésped? · 15. ¿Cómo cuadro los horarios para que no choquen con mis videollamadas? |
| **Integrates** | 16. ¿Funciona con Alexa, HomeKit o Google Home sin mil trucos? · 17. ¿Lo integro en rutinas Matter con persianas y luces? · 18. ¿Se conecta con mi cámara para limpiar solo cuando no hay nadie? |
| **Connects** | 19. ¿Puedo controlarlo desde el móvil cuando estoy de viaje? · 20. ¿Me avisa si se atasca o si el depósito está lleno? · 21. ¿Mis padres mayores podrán manejar el suyo sin llamarme cada día? |
| **Reduces Effort** | 22. ¿De verdad vacía solo el depósito o hay que estar encima? · 23. ¿Cada cuánto toca cambiar cepillos, filtros y bolsas? · 24. ¿Puedo olvidarme una semana entera de que existe? |
| **Avoid Hassles** | 25. ¿Cómo evito que se atasque con el flequillo de la alfombra? · 26. ¿Los pelos del perro destrozan el rodillo a los dos meses? · 27. ¿Llega a los rincones o deja siempre la misma zona sucia? |
| **Cost Reduction** | 28. ¿Cuánto gasta de luz al año un robot aspirador? · 29. ¿Compensa pagar 800 € si el de 249 € limpia parecido? · 30. ¿Cuánto me cuesta al año en consumibles? |
| **Quality** | 31. ¿Aspira igual en parquet, baldosa y alfombra densa? · 32. ¿Cuántos Pa necesito de verdad con un perro de pelo largo? · 33. ¿Qué diferencia hay en el fregado entre 300 € y 900 €? |
| **Variety** | 34. ¿Hay modelos pequeños pensados para pisos <60 m²? · 35. ¿Existen cortacésped para jardines con mucha pendiente? · 36. ¿Qué opciones tengo si mi casa es toda moqueta? |
| **Sensory Appeal** | 37. ¿Cuánto ruido hace? ¿Puedo ponerlo mientras teletrabajo? · 38. ¿El diseño queda bien a la vista o hay que esconderlo? · 39. ¿Huele mal al vaciar el depósito tras limpiar pelo de mascota? |
| **Informs** | 40. ¿Me da informes claros de qué zonas limpió? · 41. ¿Puedo ver los mapas para confirmar que llegó al cuarto de la colada? · 42. ¿Me avisa si detecta algo raro (gotera, enchufe roto)? |

### Nivel 2 — Emotional (10 elementos, 30 preguntas)

| Elemento | Preguntas del comprador |
|---|---|
| **Reduces Anxiety** | 43. ¿Puedo dejar al perro solo con el robot funcionando sin miedo? · 44. ¿Y si entra un desconocido, detecta algo? · 45. ¿Qué pasa con mi privacidad si el robot lleva cámara? |
| **Rewards Me** | 46. ¿Hay descuentos si ya tengo otro robot de la misma marca? · 47. ¿Ofrecen recambios gratis o renovación en el premium? · 48. ¿Puedo probarlo 30 días y devolverlo si no me encaja? |
| **Nostalgia** | 49. ¿Hay modelos que recuerden a los aspiradores clásicos pero con IA? · 50. ¿Qué de los Jetsons ya es real en una casa normal? · 51. ¿Mi abuela, que odia la tecnología, podría manejarlo como un mando? |
| **Design / Aesthetics** | 52. ¿Hay robots que combinen con deco moderna o todos son feos blancos brillantes? · 53. ¿Existen en acabado mate o imitación madera? · 54. ¿Puedo esconder la base sin perder Wi-Fi ni rendimiento? |
| **Badge Value** | 55. ¿Tener humanoide en casa dice algo de mí frente a amigos y familia? · 56. ¿Da más status un Roborock de 1.500 € o un Dyson robot? · 57. ¿Qué robots se ven en casas de influencers tech en España? |
| **Wellness** | 58. ¿Aspirar más a menudo reduce polvo y alergias de verdad? · 59. ¿Delegar el jardín me libera para hacer deporte los sábados? · 60. ¿Externalizar la limpieza quita tensión en la pareja? |
| **Therapeutic Value** | 61. ¿Es relajante mirar al robot trabajar mientras leo? · 62. ¿Qué aporta realmente a personas con movilidad reducida? · 63. ¿Ayuda a que mis padres mayores mantengan independencia? |
| **Fun / Entertainment** | 64. ¿Los niños se enganchan al robot como a una mascota? · 65. ¿Hay modos "fiesta" o robots que bailen con música? · 66. ¿Puedo usarlo para entretener al perro cuando no estoy? |
| **Attractiveness** | 67. ¿Un hogar con robots parece más moderno cuando vienen visitas? · 68. ¿Da imagen de casa cuidada si siempre está impecable? · 69. ¿Ayuda a vender mejor el piso en fotos de inmobiliaria? |
| **Provides Access** | 70. ¿Hay acceso anticipado a modelos nuevos si soy socio del club de marca? · 71. ¿Existen comunidades privadas de usuarios avanzados en español? · 72. ¿Puedo entrar en funciones beta si mando datos de uso? |

### Nivel 3 — Life-Changing (5 elementos, 15 preguntas)

| Elemento | Preguntas del comprador |
|---|---|
| **Self-Actualization** | 73. ¿Delegar la limpieza me permite dedicarme a lo que de verdad me importa? · 74. ¿Puedo convertirme en alguien que cocina más y limpia menos? · 75. ¿Tener robots en casa me hace más organizado o más vago? |
| **Provides Hope** | 76. ¿Llegará el día en que no tenga que doblar la ropa yo? · 77. ¿Los humanoides domésticos estarán en casas como la mía antes de 2030? · 78. ¿El AI Act hará que los robots sean más seguros y transparentes? |
| **Motivation** | 79. ¿Si veo los datos del robot, me motivo a mantener la casa en orden? · 80. ¿Puedo picarme con amigos a quién tiene la casa más eficiente? · 81. ¿Me ayudará a crear rutinas nuevas y mejores? |
| **Heirloom** | 82. ¿Merece la pena pagar más por uno que dure 10 años? · 83. ¿Puedo dejárselo a mis hijos cuando se independicen? · 84. ¿Las actualizaciones de software alargan la vida más allá del hardware? |
| **Affiliation / Belonging** | 85. ¿Hay un grupo de Telegram/Discord de frikis del robot aspirador en España? · 86. ¿Existe una comunidad que comparte mapas y rutas? · 87. ¿Puedo encontrar gente con mi mismo tipo de piso para copiar configuraciones? |

### Nivel 4 — Social Impact (1 elemento, 3 preguntas)

| Elemento | Preguntas del comprador |
|---|---|
| **Self-Transcendence** | 88. ¿Estoy contribuyendo al avance de la robótica si comparto datos de uso? · 89. ¿Mi compra apoya a una marca que investiga robots de asistencia para mayores? · 90. ¿Hay robots fabricados en Europa más respetuosos con el medio ambiente? |

### Cómo priorizar estas 90 preguntas

- **Prioridad alta (SEO + afiliados):** preguntas del nivel Functional con keyword de compra clara (ej. 1, 10, 16, 22, 28, 31, 34, 37). Cada una → 1 artículo evergreen + tabla comparativa + link de afiliado.
- **Prioridad media (editorial diferenciador):** Emotional + Life-Changing (43-87). Son las que construyen voz y hacen que la gente SE SUSCRIBA, no solo busque.
- **Prioridad baja (angulares especiales):** Social Impact (88-90). Un artículo trimestral de "ROBOHOGAR ético" puede cubrirlas todas.
- **Regla Cole:** cada pregunta puede responderse con los [7 templates de short-form](../references/writewithai/09-content-library-elements-of-value.md#paso-3--multiplicación--7-templates-210-short-form-posts) — es decir, 90 preguntas × 7 = **630 posts sociales potenciales**. Rafael elige cuáles activa según capacidad.
- **Checkbox:** conforme se cubra una pregunta en un artículo, editar aquí y añadir `✅ [slug-artículo]`.
