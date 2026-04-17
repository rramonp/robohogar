# Artículo #5: Humanoides domésticos 2026 (Comparativa) — Pasos para publicar

> Comparativa de los 7 humanoides domésticos que puedes comprar/reservar hoy.
> Cierra arco de 3 editoriales humanoides previos vía internal linking.

## SEO (copiar a Beehiiv)

| Campo | Valor |
|-------|-------|
| **Meta title** | `Humanoides domésticos 2026: los 7 que puedes comprar` (52 chars) |
| **Meta description** | `Comparativa honesta de los 7 humanoides domésticos que puedes comprar o reservar en 2026: NEO, Panther, F2, 4NE-1, Figure 03, Unitree R1 y Onero H1.` (151 chars) |
| **Slug** | `humanoides-domesticos-2026-comparativa` |
| **Tags** | `Humanoides`, `Comparativa` (Beehiiv) — añadir `Comparativa` si no existe aún |
| **Publish to** | `Web only` (fase pre-audiencia, <30 subs — reserva envío para cuando haya audiencia) |
| **Content Gate** | ❌ NO activar — artículo evergreen, queremos que se descubra por SEO |

## Hero image — elegir 1 de 3 variantes

Las tres están en `assets/` como `.png` (master) + `.webp` (subir a Beehiiv):

| Variante | Concepto visual | Archivo WebP | Tamaño aprox. |
|---|---|---|---|
| **v7** ⭐ | Lineup clásico en limbo cream infinito (estilo catálogo producto), 7 robots matte alineados sin pared | `hero-humanoides-domesticos-2026-comparativa-v7.webp` | ~60 KB |
| **v6** | Vista cenital top-down, 7 robots tumbados en suelo de madera | `hero-humanoides-domesticos-2026-comparativa-v6.webp` | ~55 KB |
| **v2** | Humanoide blanco en foco central + 6 siluetas fantasma translúcidas en cocina | `hero-humanoides-domesticos-2026-comparativa-v2.webp` | ~45 KB |
| **v3** | Siete pedestales con etiquetas de precio borrosas, 1 robot en el del medio | `hero-humanoides-domesticos-2026-comparativa-v3.webp` | ~40 KB |

> **v1, v4, v5 archivadas** en `assets/_archive/` por neones. v1: carteles LED en pared. v4: paneles luminosos rosa/amarillo/naranja en cuerpos. v5: TV neón con caracteres asiáticos + círculo neón morado en pared. Aprendizaje acumulado: "pared trasera + múltiples robots = Gemini siempre mete neones". v7 resuelve eliminando cualquier arquitectura (backdrop limbo cream infinito tipo estudio).

**Recomendación del agente:** **v7** (limbo lineup clásico catálogo) — aesthetic universalmente reconocido como "comparativa de producto", comunica en <1 segundo a 300px, sin arquitectura que Gemini pueda decorar. v6 (cenital) es original pero "robots tumbados" tiene connotación extraña. v2 es estética pero no comunica "7". v3 puede leerse como "ranking/podio" en vez de comparativa neutra.

Subir el **WebP** elegido a Beehiiv como Post Thumbnail. PNG master queda en repo.

## Imágenes inline del artículo

| Archivo | Ubicación en artículo | Fuente |
|---|---|---|
| `figure-neo-home.jpg` | § 1. 1X NEO | 1X Technologies (reutilizada de artículo NEO-EQT) |
| `figure-unix-panther.jpg` | § 2. UniX AI Panther | The AI Insider / UniX AI |
| `figure-neura-4ne1.webp` | § 4. Neura 4NE-1 | Neura Robotics (oficial) |
| `figure-unitree-r1.webp` | § 6. Unitree R1 | Robotshop / Unitree |

Imágenes NO usadas inline (candidatas alternativas en `assets/`):
- `figure-china-f2.png` — alternativa para § 3 si quieres 5 imágenes en vez de 4
- `figure-figure-03.jpg` — alternativa para § 5 (Figure 03 en Time Magazine)
- `figure-switchbot-onero.jpg` — alternativa para § 7

**Criterio:** 4 inline es óptimo para ~1.400 palabras (1 cada ~350). Más satura el feed de imágenes y aumenta peso del email (si algún día se envía).

## Mapa visual del artículo

```
╔══════════════════════════════════════════════════════════════╗
║  HERO IMAGE (v1/v2/v3, 1200x630 aprox)                       ║
╠══════════════════════════════════════════════════════════════╣
║  H1: Humanoides domésticos 2026: los 7 que puedes comprar... ║
║  Subtítulo · Rafael de ROBOHOGAR · 9 min                     ║
╠══════════════════════════════════════════════════════════════╣
║  ╔═══════ INTRO CALLOUT ÁMBAR ═══════╗                       ║
║  ║ Hook: "Entre 4.500€ y 98.000€..." ║                       ║
║  ║ Promesa: 3 columnas, veredicto    ║                       ║
║  ╚═══════════════════════════════════╝                       ║
╠══════════════════════════════════════════════════════════════╣
║  H2: Cómo hemos clasificado los 7                            ║
║  ¶ 3 filtros: precio · posicionamiento · ventana 2026-27     ║
║  ¶ Presentación de los 7 nombres                             ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 1. 1X NEO — $20.000, pero no para ti                    ║
║  📷 figure-neo-home.jpg                                      ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
║   ¶ link interno → humanoides-en-casa-cuanto-falta           ║
║   ¶ link interno → neo-humanoide-fabricas-eqt                ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 2. UniX AI Panther — ya entrando en casas chinas        ║
║  📷 figure-unix-panther.jpg                                  ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 3. China F2 — el humanoide de 4.500€                    ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  ╔═══════ CTA MID-ARTICLE ═══════╗                           ║
║  ║ ¿Te está sirviendo?          ║                            ║
║  ║ [Suscríbete gratis →]        ║                            ║
║  ╚══════════════════════════════╝                            ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 4. Neura 4NE-1 — el europeo Porsche Design              ║
║  📷 figure-neura-4ne1.webp                                   ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 5. Figure 03 — industrial vestido de doméstico          ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 6. Unitree R1 — el más barato ($4.900)                  ║
║  📷 figure-unitree-r1.webp                                   ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 7. SwitchBot Onero H1 — el pragmático con ruedas        ║
║   H3: Qué es · Lo bueno · Lo malo · Para quién               ║
╠══════════════════════════════════════════════════════════════╣
║  H2: Tabla comparativa resumen (7 filas con badges)          ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 🏆 Nuestro veredicto                                    ║
║   ╔═══ CALLOUT ÁMBAR con síntesis ═══╗                       ║
║   ╚══════════════════════════════════╝                       ║
║   ¶ Si vives en Europa y prisa → 4NE-1 Mini                  ║
║   ¶ Si no tienes prisa → esperar 18 meses                    ║
║   ¶ Dato geopolítico: 5 Asia, 1 EU, 1 US                     ║
║   ¶ link interno → roborock-saros-z70-review                 ║
╠══════════════════════════════════════════════════════════════╣
║  H2: 💡 ¿Sabías que…?                                        ║
║   ¶ Bloomberg: 90K/1,2M + <15% domésticos                    ║
╠══════════════════════════════════════════════════════════════╣
║  H2: ¿Te ha servido?                                         ║
║  [Suscríbete gratis]                                         ║
║  Disclaimer afiliados (italic, gris)                         ║
╚══════════════════════════════════════════════════════════════╝
```

## Pasos para publicar

### 1. Preparación (15 min)

- [ ] Abrir `borrador.html` en navegador para previsualizar
- [ ] Elegir hook de los 3 candidatos del HTML comment (v1 activada)
- [ ] Elegir hero image (v1/v2/v3) — ver sección de arriba

### 2. Validar datos específicos (15-20 min)

Antes de publicar, confirmar que ningún precio ni fecha ha cambiado desde el digest 2026-04-17:

- [ ] NEO: $20.000 + $200 depósito + envíos solo US/CA (1x.tech)
- [ ] UniX AI Panther: entregas desde 10-abr-2026 (comprobar si hay precio internacional anunciado)
- [ ] China F2: 36.000 yuanes / ~4.500€, piloto 300 hogares Pekín+Shanghái
- [ ] Neura 4NE-1: 98.000€ flagship, 19.999€ Mini, 60.000€ flota
- [ ] Figure 03: sin pre-orders todavía (confirmar en figure.ai)
- [ ] Unitree R1: desde $4.900 (unitree.com o robotshop)
- [ ] SwitchBot Onero H1: objetivo <$10.000, CES 2026 (switch-bot.com)

### 3. Editar voz (Rafael, 45-90 min)

- [ ] Aplicar voz plural editorial ("hemos", "os contamos")
- [ ] Añadir 1-2 opiniones personales donde encaje el humor
- [ ] Verificar contra `docs/brand-voice.md` y `rules/editorial.md`
- [ ] Sin superlativos ("revolucionario", "el mejor", "game-changer")
- [ ] Headlines ≤40 chars en móvil (verificar H2 numerados)

### 4. Crear post en Beehiiv (60-75 min)

- [ ] Duplicar post de `mejor-robot-asistente-ia-2026` (también comparativa) como base
- [ ] Settings:
  - [ ] **Publish to: `Web only`** (fase pre-audiencia, reserva envío)
  - [ ] Meta title/description: pegar del SEO de arriba
  - [ ] Post URL: `humanoides-domesticos-2026-comparativa`
  - [ ] Tags: `Humanoides`, `Comparativa`
  - [ ] Content Gate: ❌ NO activar (evergreen, foco SEO)
  - [ ] Comments: Activados
- [ ] Subir hero WebP + activar "Show thumbnail on top"
- [ ] Copiar contenido sección por sección
- [ ] Subir imágenes inline en sus secciones

### 5. Preview + verificar (15 min)

- [ ] Preview móvil (icono 📱 en Design Mode)
- [ ] Verificar tabla comparativa se renderiza bien en 375px
- [ ] Verificar badges (verde/ámbar/rojo) en preview
- [ ] Verificar links internos: humanoides-en-casa + neo-humanoide-fabricas + roborock-saros-z70

### 6. Publicar + post-publish

- [ ] Publish (Web only) desde Beehiiv
- [ ] URL definitiva: `https://robohogar.com/p/humanoides-domesticos-2026-comparativa`
- [ ] Verificar OG image en [opengraph.xyz](https://opengraph.xyz)
- [ ] Pedir a Claude: `/post-publish https://robohogar.com/p/humanoides-domesticos-2026-comparativa`

## Fuentes del artículo

| Dato | Fuente | Cómo verificar |
|---|---|---|
| NEO: $20.000 + $200 depósito + US/CA | 1X Technologies oficial | 1x.tech/discover/neo-home-robot |
| 1X + EQT 10.000 unidades | Palo Alto Today, The Robot Report | Artículo propio NEO-EQT |
| UniX AI Panther entregas 10-abr-2026 | NaturalNews, Omicrono | Buscar "UniX AI Panther delivery" |
| China F2 precio + piloto | Omicrono 15-abr-2026 | omicrono.elespanol.com |
| Neura 4NE-1 98k/19.999/60k | RoboHorizon, Xataka, Gizmodo ES | neura-robotics.com |
| Figure 02 → 30.000 X3 BMW Spartanburg | Figure AI + BMW press | Ya verificado artículo NEO-EQT |
| Unitree R1 $4.900+ | Unitree, The Robot Report, CNET | unitree.com |
| SwitchBot Onero H1 CES 2026 <$10K | The Verge, Mashable, Interesting Engineering | switch-bot.com |
| Bloomberg 90K/1,2M, <15% domésticos | Bloomberg humanoid outlook 2026 | — |

## Links internos (verificar antes de publicar)

- https://robohogar.com/p/humanoides-en-casa-cuanto-falta ✅
- https://robohogar.com/p/neo-humanoide-fabricas-eqt ✅
- https://robohogar.com/p/roborock-saros-z70-review ✅

## Notas editoriales

- **Cierra arco de humanoides**: tras 2 editoriales (humanoides-en-casa + NEO-EQT), esta comparativa es la pieza de referencia que el lector puede marcar/compartir. Útil como entrada al pilar humanoide para nuevos lectores
- **Tono balanceado**: es comparativa, no editorial crítico — mantener opinión pero sin la dureza del NEO-EQT. El lector debe salir sabiendo a qué apostar, no enfadado
- **Evergreen**: los precios/estados se pueden actualizar dentro de 6 meses con edición puntual. Mantener estructura de 7 constante
- **Posibles tangibles futuros** (FASE 4C, no ahora): "Tabla comparativa humanoides 2026 PDF" sería un lead magnet natural desde este artículo
