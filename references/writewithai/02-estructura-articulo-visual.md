# 02 — Estructura de artículo (block-by-block)

> Anatomía visual destilada de 30+ artículos Cole/Bush. Cross-refs: [voz](01-voz-y-estructura.md) · [prompts](05-prompts-utiles.md) · [branding](06-branding-visual.md).

## TL;DR

- Todos los artículos Write With AI siguen el mismo esqueleto: **Hero → Saludo → Hook → Framework numerado → Prompt → Screenshot → Cierre con firma**.
- Tres plantillas reutilizables lo cubren todo: **Problem/Solution, Common Mistakes, Step-by-Step**. Se mapean 1:1 a reviews, comparativas y tutoriales ROBOHOGAR.
- El patrón **1/3/1** rige cada párrafo dentro de cualquier bloque.
- El **Substack Long-Form Post Creator** define 5 patrones mezclables: *Mistake, Statistic, Steps, Reasons Why, Story*. Un artículo típico combina 2-3.
- Nuestra plantilla `content/templates/estructura-templates.md` debe incorporar estos 5 patrones + las 3 plantillas maestras.

---

## Anatomía universal de un post Cole/Bush

```
┌──────────────────────────────────────────────────────────────┐
│  HERO IMAGE 1260x900                                         │
│  (tipografía blanca sobre collage editorial)                 │
│  Texto grande: título · subtítulo en italic                  │
└──────────────────────────────────────────────────────────────┘
                              ▼
  H1: "Title That Makes A Promise"
  H3 italic: "Subtitle that adds specificity"
                              ▼
  "Ahoy, Digital Writers!" (saludo ritual)
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  HOOK (1-3 párrafos)                                         │
│  - Frase-chip que abre loop                                  │
│  - 3 frases de contexto (1/3/1)                              │
│  - "That's why today..."                                     │
└──────────────────────────────────────────────────────────────┘
                              ▼
  "Let's dive in!" (puente)
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  H1 "Step 1: [acción]"                                       │
│    Texto (1/3/1)                                             │
│    Ejemplo concreto                                          │
│    ```prompt con {placeholders}```                           │
│    [Screenshot de output]                                    │
│                                                              │
│  H1 "Step 2: [acción]"                                       │
│    (mismo patrón)                                            │
│                                                              │
│  H1 "Step 3: [acción]"  ← aquí suele cortar el paywall       │
└──────────────────────────────────────────────────────────────┘
                              ▼
  Cierre con frase punzante + firma + upsell
  "Chat soon, Cole & Dickie"
```

**Observación clave:** el paywall corta al 30-40% del contenido, justo antes del prompt decisivo del Step 3. Nosotros no tenemos paywall — tenemos SEO. Nuestro equivalente: cerrar con CTA de suscripción después de entregar el valor completo.

---

## Template 1 · Problem / Solution (reviews y comparativas)

**Cuándo:** review de un producto, comparativa entre modelos, tutoriales donde hay un "antes roto y un después arreglado".

```
H1. Título con promesa
H3. Subtítulo específico

[HOOK] Escena del problema (1/3/1)

H2. "El problema con [categoría]"
    Descripción del estado roto.
    3-5 cosas que intentaste y fallaron.
    Por qué falló cada una.

H2. "La solución: [producto/método]"
    Qué es, en una frase.
    Cómo funciona (3 frases).
    Por qué es diferente del resto.

H2. "Cómo aplicarlo paso a paso"
    Paso 1 · Paso 2 · Paso 3
    (cada uno con ejemplo concreto)

H2. "Veredicto"
    Para quién sí, para quién no.
    Precio + link afiliado.
    Alternativa si no encaja.

[CIERRE] Frase punzante + firma + PS
```

**Ejemplo ROBOHOGAR aplicado:**

- H1: *Roborock Saros Z70: por qué NO es el mejor robot de 2026*
- Problema: casas con niños/perros, marketing promete brazo robótico, realidad es distinta.
- Solución: el Q Revo Master, 400 € más barato, limpia mejor.
- Pasos: desempaquetado, mapeo, rutinas, integración HomeKit.
- Veredicto: para qué perfil sí/no + alternativa.

## Template 2 · Common Mistakes (editoriales y guías de compra)

**Cuándo:** artículos tipo "5 errores al comprar X", guías defensivas, posts educativos.

```
H1. "X errores al [acción deseada]"
H3. Subtítulo con número + audiencia

[HOOK] Historia de alguien que cometió los errores (1/3/1)

H2. "Por qué estos errores son tan comunes"
    Contexto psicológico / de mercado.

H2. "Error 1: [nombre del error]"
    Descripción concreta.
    Consecuencia real.
    Cómo corregirlo.

H2. "Error 2..." (repite 3-5 veces)

H2. "Checklist antes de comprar"
    Tabla con 5 puntos accionables.

[CIERRE]
```

**Ejemplo ROBOHOGAR aplicado:**

- "5 errores al comprar tu primer robot aspirador (y qué hacer en su lugar)"
- Error 1: obsesionarte con los Pa de succión sin mirar el cepillo principal.
- Error 2: no medir la altura de tus muebles antes.
- Error 3: pagar por *mopping* cuando no vas a mantenerlo.
- Error 4: elegir un modelo sin repuestos en España.
- Error 5: comprar en Black Friday sin leer la garantía.

## Template 3 · Step-by-Step How-To (tutoriales y setups)

**Cuándo:** configuraciones, integraciones, rutinas, tutoriales técnicos.

```
H1. "Cómo [conseguir resultado] [sin obstáculo]"
H3. Tiempo estimado + prerrequisitos

[HOOK] Estado final deseado en 1 frase.

H2. "Lo que necesitas"
    Lista de materiales/apps/cuentas.

H2. "Paso 1: [acción concreta]"
    Screenshot. Instrucción literal. Error común a evitar.

H2. "Paso 2..." (3-7 pasos)

H2. "Si algo sale mal"
    Troubleshooting rápido.

H2. "Siguiente nivel"
    1-2 pistas para profundizar.

[CIERRE]
```

**Ejemplo ROBOHOGAR aplicado:**

- "Cómo integrar tu robot aspirador con HomeKit sin comprar un hub"
- 5 pasos: cuenta Roborock, Matter, añadir a Casa, rutinas por habitación, automatizar con hora dormir niños.

---

## Los 5 patrones mezclables (Substack Long-Form Post Creator)

Cada artículo puede combinar 2-3 de estos bloques para añadir variedad sin perder cohesión. Cada patrón sigue internamente el ritmo 1/3/1.

| Patrón | Estructura (5 frases) | Ejemplo ROBOHOGAR |
|---|---|---|
| **Mistake** | estado → impacto negativo → por qué pasa → conexión con dolor → cómo evitarlo | "Compré mi primer robot en Black Friday..." |
| **Statistic** | dato que impacta → significado → por qué importa → cómo te afecta → qué hacer | "Solo el 14% de los hogares españoles tiene robot. En Alemania, el 32%." |
| **Steps** | resumen → paso 1 → paso 2 → paso 3 → siguiente | Usar para setup y rutinas |
| **Reasons Why** | afirmación → razón 1 → razón 2 → razón 3 → takeaway | "3 razones para NO comprar un Dreame X50 todavía" |
| **Story / Ejemplo relatable** | historia breve → lección → cómo se conecta → acción → qué hacer | Abrir cualquier newsletter con escena real |

**Mezcla típica para una review de 1200 palabras:** Story (apertura) → Statistic (contexto) → Mistake (objeciones) → Steps (uso real) → Reasons Why (veredicto).

---

## 7 secciones reutilizables para newsletter (7 Proven Newsletter Sections)

Del artículo homónimo de WWAI (parcialmente tras [PAYWALL], framework inferido):

1. **Noticia + comentario editorial** (70% del contenido newsletter ROBOHOGAR)
2. **Review rápida** (rotativa mensual)
3. **Comparativa express** (una tabla, 3 modelos)
4. **Tutorial de 5 pasos** (quincenal)
5. **Opinión editorial / futuro** (30% restante)
6. **Pregunta a la comunidad** (cada 2-3 semanas, PS + poll Beehiiv)
7. **Enlaces de la semana** (3-5 links curados, estilo Axios)

## Axios Newsletter Template · 6 reglas (para decir más con menos)

Del artículo *Axios Newsletter Template For Content Curators*. Reglas inferidas del patrón:

1. **Smart Brevity:** cada item = 1 titular + 1 frase "por qué importa" + 3 bullets.
2. **Bold keywords** en la primera frase para escaneo rápido.
3. **Why it matters** como sub-epígrafe obligatorio.
4. **No relleno:** cada oración debe responder "¿y si borro esto, qué pierdo?".
5. **Orden de lectura:** de abajo arriba — el que más empuja primero.
6. **Link único por item**, en el nombre del producto/fuente.

Aplicable directamente al **bloque "Enlaces de la semana"** de la newsletter ROBOHOGAR.

## Substack Long-Form Post Creator · los 5 patterns combinados

Ya descritos arriba. El valor añadido: **todo artículo largo = 3-5 "bloques" encadenados, cada uno de 5 frases**. Eso da artículos de 800-1500 palabras sin divagación.

---

## Cross-reference a `content/templates/estructura-templates.md`

Qué añadir allí (FASE 4, no parte de esta síntesis):

- Las 3 plantillas maestras (Problem/Solution, Common Mistakes, Step-by-Step) como opciones base.
- Los 5 patrones mezclables como componentes Lego.
- El bloque "Why it matters" del Axios template para cada noticia en newsletter.
- El diagrama ASCII de la anatomía universal al inicio del documento.
- Checklist: `¿He aplicado 1/3/1 en los 3 primeros párrafos?` antes de dar por terminado cualquier borrador.

---

## Aplicabilidad ROBOHOGAR concreta

**Acciones priorizadas:**
1. **Inmediato:** usar Template 1 (Problem/Solution) para la próxima review larga. Template 2 (Common Mistakes) para el siguiente artículo de guía.
2. **Esta semana:** añadir al skill `content-draft` un argumento `--template=problem-solution|mistakes|how-to` que aplique el esqueleto correspondiente.
3. **Próximas 2 semanas:** crear `content/templates/axios-link-roundup.md` con las 6 reglas para el bloque de enlaces del newsletter.
4. **Mes:** probar una newsletter full-Axios (todas las noticias en formato Smart Brevity) y comparar open/CTR con una semana estándar.
