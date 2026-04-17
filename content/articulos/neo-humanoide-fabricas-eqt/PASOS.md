# Artículo #4: NEO va a fábricas — Pasos para publicar

> Editorial crítico sobre el pivote industrial de 1X mientras sigue cobrando pre-orders domésticos.
> Continuación directa de [humanoides-en-casa-cuanto-falta](../humanoides-en-casa-cuanto-falta/).

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `NEO va a fábricas: ¿humanoide doméstico o industrial?` (54 chars) |
| **Meta description** | `1X firma con EQT para desplegar 10.000 NEO industriales. Sigue cobrando $200 a familias por un envío solo a EE.UU. ¿Pivote o doble juego?` (139 chars) |
| **Slug** | `neo-humanoide-fabricas-eqt` |
| **Tags** | `Humanoides`, `Opinión` |
| **Publish to** | `Email and web` (aparece en landing + se envía por email) |
| **Content Gate** | ❌ NO activar — es editorial de 30% del mix, gate-arlo reduce impacto del pilar |

## Hero image — elegir 1 de 3 variantes

Las tres están en `assets/` como `.png` (master) + `.webp` (subir a Beehiiv):

| Variante | Concepto visual | Archivo WebP | Tamaño |
|---|---|---|---|
| **v1** | El apretón corporativo — mano robot + mano humana en traje, fondo split cocina/almacén | `hero-neo-humanoide-fabricas-eqt-v1.webp` | 41 KB |
| **v2** | Uniforme industrial en cocina — humanoide con chaleco alta visibilidad entregando taza de café | `hero-neo-humanoide-fabricas-eqt-v2.webp` | 54 KB |
| **v3** | La caja que nunca llegó — caja vacía en cocina + silueta humanoide alejándose a almacén | `hero-neo-humanoide-fabricas-eqt-v3.webp` | 29 KB |

**Recomendación del agente:** **v2** (uniforme industrial en cocina) es la que más claro comunica la contradicción a 300px — reconocible en 2 segundos y sin ambigüedad. v1 es la segunda opción si Rafael prefiere tono más "boardroom". v3 es la más sutil y melancólica, pero requiere "mirar más" para entender — peor ROI como thumbnail.

Subir el **WebP** elegido a Beehiiv como Post Thumbnail. El PNG master queda en repo como backup.

## Imágenes inline del artículo

| Archivo | Ubicación en artículo | Estado | Fuente sugerida |
|---|---|---|---|
| `1x-neo-home-robot.jpg` | Sección "El pitch doméstico que sigue vivo" | ✅ Ya en `assets/` (copiado del artículo humanoides) | 1X Technologies |
| `figure-neo-warehouse.jpg` | Sección "La contradicción del anuncio" | ⚠️ **Pendiente — sourcear manualmente** | Ver notas abajo |

### Sourcear `figure-neo-warehouse.jpg`

El borrador referencia una imagen de NEO en entorno industrial/warehouse para ilustrar el deal con EQT. Opciones:

1. **The Robot Report** — artículo del 12-abr-2026 sobre el deal 1X+EQT. Buscar "1X EQT NEO deal" en therobotreport.com. Normalmente publican la imagen de prensa de 1X.
2. **Palo Alto Today** — fuente original del anuncio (12-abr-2026). palaaltotoday.com.
3. **1X Press Kit** — 1x.tech/press suele tener imágenes licenciables con atribución.
4. **Fallback:** si no hay foto clara de NEO en warehouse, duplicar la 1x-neo-home-robot.jpg y la sección "La contradicción del anuncio" se queda sin imagen inline (el texto aguanta). Priorizar ritmo sobre foto de stock.

Una vez descargada: guardar en `assets/` con el nombre `figure-neo-warehouse.jpg` (<300 KB). Si el nombre de archivo cambia, actualizar el `<img src>` en `borrador.html`.

## Mapa visual del artículo

```
╔══════════════════════════════════════════════════════════════╗
║  HERO IMAGE (WebP elegido, 1200x630 aprox)                   ║
╠══════════════════════════════════════════════════════════════╣
║  H1: NEO va a fábricas: ¿humanoide doméstico o industrial?   ║
║  Subtítulo · Rafael de ROBOHOGAR · 7 min                     ║
╠══════════════════════════════════════════════════════════════╣
║  ╔═══════ INTRO CALLOUT ÁMBAR ═══════╗                       ║
║  ║ Hook: "Hace cinco días..."        ║                       ║
║  ║ Tesis + qué vamos a probar        ║                       ║
║  ╚═══════════════════════════════════╝                       ║
╠══════════════════════════════════════════════════════════════╣
║  H2: La contradicción del anuncio                            ║
║  ¶ Deal 1X + EQT (12-abr-2026)                               ║
║  📷 figure-neo-warehouse.jpg  ← sourcear manualmente         ║
║  ¶ Pre-orders domésticos siguen vivos                        ║
║  ¶ Pregunta transición                                       ║
╠══════════════════════════════════════════════════════════════╣
║  H2: Lo que dice 1X (y lo que no dice)                       ║
║   H3: El pitch doméstico que sigue vivo                      ║
║    ¶ $20K + $200 depósito + Q3-Q4 2026                       ║
║    📷 1x-neo-home-robot.jpg  ← ya en assets/                 ║
║    ¶ "Q3-Q4 2026 es el tercer plazo…"                        ║
║   H3: El World Model como humo estratégico                   ║
║    ¶ aprendizaje por vídeo · contradicción con industrial    ║
║   H3: La teleoperación en la letra pequeña                   ║
║    ¶ link interno → humanoides-en-casa-cuanto-falta          ║
╠══════════════════════════════════════════════════════════════╣
║  ╔═══════ CTA MID-ARTICLE ═══════╗  (centrado, sin borde)    ║
║  ║ ¿Te está sirviendo?          ║                            ║
║  ║ [Suscríbete gratis →]        ║                            ║
║  ╚══════════════════════════════╝                            ║
╠══════════════════════════════════════════════════════════════╣
║  H2: La contradicción que nadie explica                      ║
║   H3: Humanoide "doméstico" que solo viaja a dos países      ║
║   H3: Robot entrenado "para casa"… en un almacén             ║
║    ╔═══ CALLOUT ÁMBAR con dato EQT ═══╗                      ║
║    ╚══════════════════════════════════╝                      ║
║    ¶ precedente Figure Robotics                              ║
║   H3: A quién responde 1X de verdad                          ║
╠══════════════════════════════════════════════════════════════╣
║  H2: Lo que no te cuentan  (solo texto, ritmo H3+¶)          ║
║   H3: El dinero de verdad está en la fábrica                 ║
║   H3: "El primer humanoide doméstico" dejó de ser promesa    ║
║   H3: Si compras NEO hoy, pagas por participar en el beta    ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 🏆 Nuestro veredicto                                    ║
║   ╔═══ CALLOUT ÁMBAR con frase síntesis ═══╗                 ║
║   ╚═════════════════════════════════════════╝                ║
║   ¶ qué significa                                            ║
║   ¶ ¿Y Europa? Predicción 2028 + 30.000€                     ║
║   ¶ cierre → link interno a roborock-saros-z70-review        ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 💡 ¿Sabías que…?                                        ║
║   ¶ Bloomberg: 90K humanoides 2026 → 1,2M 2030               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: ¿Te ha servido?                                         ║
║  H2: Cada semana más como esto en tu bandeja                 ║
║  [Suscríbete gratis]                                         ║
║  Disclaimer afiliados (italic, gris)                         ║
╚══════════════════════════════════════════════════════════════╝
```

## Pasos para publicar

### 1. Preparación (15 min)

- [ ] Abrir `borrador.html` en navegador (doble clic) para previsualizar contenido
- [ ] **Elegir hook** de los 3 candidatos del HTML comment al inicio (v1 ya está activada en el borrador)
- [ ] Revisar que el artículo suena a ROBOHOGAR, no a comunicado

### 2. Source imagen inline pendiente (10-20 min)

- [ ] Buscar `figure-neo-warehouse.jpg` en The Robot Report / 1X press kit
- [ ] Descargar a `assets/` con ese nombre exacto, <300 KB
- [ ] Alternativa: eliminar la línea `<img src="assets/figure-neo-warehouse.jpg">` del borrador si no se encuentra

### 3. Editar voz (Rafael, 45-90 min)

- [ ] Aplicar voz: plural editorial ("hemos investigado", "os contamos") — ya está en el borrador pero revisar
- [ ] Añadir 1-2 opiniones personales / humor / anécdotas donde encajen
- [ ] Verificar contra `docs/brand-voice.md` y `rules/editorial.md`
- [ ] Sin superlativos vacíos ("revolucionario", "increíble", "el mejor") — revisar búsqueda
- [ ] Sin "honesta", "sin filtro", "guía definitiva"
- [ ] Ajustar títulos/H2 si hace falta (mobile-first: ≤40 chars en headlines)

### 4. Crear post en Beehiiv (45-60 min)

- [ ] Duplicar post de `humanoides-en-casa-cuanto-falta` en Beehiiv (mismo template editorial)
- [ ] Settings:
  - [ ] Publish to: `Email and web`
  - [ ] Meta title: pegar del SEO de arriba
  - [ ] Meta description: pegar del SEO
  - [ ] Post URL: `neo-humanoide-fabricas-eqt`
  - [ ] Tags: `Humanoides`, `Opinión`
  - [ ] Content Gate: ❌ NO activar (editorial)
  - [ ] Comments: Activados
- [ ] Subir hero WebP como Post Thumbnail + activar "Show thumbnail on top"
- [ ] Copiar contenido del borrador sección por sección al template de Beehiiv
- [ ] Subir imágenes inline en sus secciones correspondientes

### 5. Preview + verificar (10 min)

- [ ] Preview en móvil (icono 📱 en Design Mode)
- [ ] Enviar test email a email personal
- [ ] Verificar que el WebP del hero carga rápido
- [ ] Verificar links internos: humanoides-en-casa-cuanto-falta + roborock-saros-z70-review

### 6. Publicar

- [ ] Send / Publish desde Beehiiv
- [ ] Capturar URL definitiva: `https://robohogar.com/p/neo-humanoide-fabricas-eqt`
- [ ] Verificar OG image en [opengraph.xyz](https://opengraph.xyz) inmediatamente tras publicar

### 7. Post-publicación

- [ ] Pedir a Claude: `/post-publish https://robohogar.com/p/neo-humanoide-fabricas-eqt` (14 pasos automáticos incluidos registro + vault sync + commit)
- [ ] Pedir a Claude: `/social-content` para preparar posts LinkedIn/X/IG (aunque aún no tengamos seguidores, dejarlos programados)

## Fuentes del artículo

| Dato | Fuente | Cómo verificar |
|---|---|---|
| Deal 1X + EQT, 10.000 NEO, 12-abr-2026 | Palo Alto Today, The Robot Report | Buscar "1X EQT NEO 2026" |
| NEO pre-orders $20K + $200 depósito + Q3-Q4 2026 | 1X Technologies official | 1x.tech/neo |
| 1X World Model | The Robot Report (2026) | Buscar "1X World Model 2026" |
| Teleop + zonas opt-out | 1X docs + WSJ contexto | Referencia cruzada con humanoides-en-casa-cuanto-falta |
| Figure 02 BMW Spartanburg 30.000 X3 | Figure AI + BMW press | Ya verificado en artículo humanoides |
| AI Act art. 50 + alto riesgo agosto 2026 | Economist & Jurist 13-abr-2026, AI Act Explorer | — |
| Bloomberg 90K/1,2M humanoides | Bloomberg outlook 2026 | Buscar "Bloomberg humanoid robot 2026 outlook" |

Todos los links están en el HTML del borrador. Digest fuente: `content/drafts/research-digest-2026-04-17.md`.

## Links internos (verificar antes de publicar)

- https://robohogar.com/p/humanoides-en-casa-cuanto-falta (ya publicado ✅)
- https://robohogar.com/p/roborock-saros-z70-review (ya publicado ✅)

## Notas editoriales

- **Es una continuación del editorial "Humanoides en casa"** — el lector que haya leído ese puede entrar directo al ángulo del pivote. El lector nuevo necesita contexto en la intro.
- **No descalificar a 1X** — es crítica al *pitch*, no a la empresa. Mantener el tono analítico del párrafo final ("esto no descalifica a 1X como empresa").
- **El villano es la contradicción del marketing, no el robot.** Línea editorial coherente con el pilar de Ficciones Domésticas ("el robot nunca es el villano").
