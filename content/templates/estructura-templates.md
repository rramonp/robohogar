# Estructura de Templates Beehiiv — ROBOHOGAR

Referencia para `/content-draft` al generar HTML de artículos nuevos.
Basado en los artículos publicados reales, no en templates genéricos.

**Fuente de verdad:** los artículos publicados en Beehiiv. Si Rafael modifica
un template en Beehiiv, actualizar este documento.

---

## Template 1: Review/Comparativa

**Ejemplo real:** https://robohogar.com/p/mejor-robot-asistente-ia-2026
**Uso:** 70% del contenido — reviews de producto, comparativas, guías de compra

### Estructura de bloques (en orden)

```
HERO IMAGE (thumbnail del artículo, WebP)
H1: Título con keyword SEO
  Subtítulo: 1 frase descriptiva de lo que cubre el artículo
  Autor + fecha + tiempo de lectura

INTRO CALLOUT (borde ámbar izquierdo)
  Párrafo: contexto y qué vas a encontrar en el artículo

--- separador ---

POR CADA PRODUCTO RECOMENDADO:
  H2: "N. Nombre — Subtítulo descriptivo"
    📷 Imagen del producto (foto real del fabricante)
    CARD INFO: 3 columnas (Precio | Suscripción | Lo clave)
    H3: "👍 Lo bueno"
      Lista con bullets (3-4 puntos)
    H3: "👎 Lo malo"
      Lista con bullets (3-4 puntos)
    H3: "🎯 Para quién es"
      Párrafo corto
    CALLOUT GRIS: "Mi opinión:" + texto en cursiva
    BOTÓN CTA: "Consultar [Producto] en Amazon" (link afiliado)

--- separador ---

CTA MID-ARTICLE (fondo gris, centrado)
  "¿Te está sirviendo? Publicamos cada semana"
  Botón ámbar: "Suscríbete gratis"

--- separador ---

H2: "❌ ¿Y los que NO recomiendo?"
  POR CADA PRODUCTO NO RECOMENDADO:
    H3: "Nombre — Precio"
      Párrafo con motivos (corto, directo)

H2: "📊 Comparativa"
  TABLA: Producto | Precio | Lo clave | Nota (⭐)

H2: "🏆 Entonces, ¿cuál me compro?"
  📷 Imagen mascota (opcional)
  Texto con recomendaciones por escenario
  BOTÓN CTA: link al ganador en Amazon

H2: "💡 ¿Sabías que…?"
  Párrafo con dato curioso + link a fuente

H2: "¿Te ha servido?"
H2: "Cada semana más como esto en tu bandeja"
  📷 OG image del artículo
  Botón: "Suscríbete gratis"
  Texto legal afiliados

FOOTER (automático Beehiiv)
  "Keep Reading" (automático)
  Copyright + social links + unsubscribe
```

---

## Template 2: Editorial/Opinión

**Ejemplo real:** https://robohogar.com/p/humanoides-en-casa-cuanto-falta
**Uso:** 30% del contenido — futuro, tendencias, opinión, análisis

### Estructura de bloques (en orden)

```
HERO IMAGE (thumbnail del artículo, WebP)
H1: Título con gancho editorial
  Subtítulo: 1 frase que resume la tesis del artículo
  Autor + fecha + tiempo de lectura

INTRO CALLOUT (borde ámbar izquierdo)
  Párrafo: "Hemos investigado..." — qué se ha hecho y qué veredicto adelanta

--- separador ---

H2: Sección contexto (ej: "La carrera que nadie esperaba")
  Párrafo 1: gancho + dato impactante
  📷 Imagen de contexto (foto prensa/evento, NO generada)
  Párrafo 2: datos de financiación, empresas, tendencia
  Párrafo 3: transición al análisis

--- separador ---

H2: Sección análisis principal (ej: "Los que más ruido hacen")
  POR CADA EMPRESA/ROBOT RELEVANTE:
    H3: "Nombre — Subtítulo con opinión"
      Párrafo 1: qué prometen / qué han hecho
      📷 Imagen del robot/empresa (foto real, después del párrafo que la justifica)
      Párrafo 2: realidad vs promesa, datos concretos
      (NO hay pros/contras, NO hay cards de precio — es narrativo)

--- separador ---

CTA MID-ARTICLE (fondo gris, centrado)
  "¿Te está sirviendo? Publicamos cada semana"
  Botón ámbar: "Suscríbete gratis"

--- separador ---

H2: Sección exposé/análisis profundo (ej: "El que ya puedes comprar (con truco)")
  POR CADA PUNTO:
    H3: "Nombre — Dato impactante"
      Párrafo: análisis crítico
      📷 Imagen del producto (foto real)
      CALLOUT ÁMBAR (si hay dato bomba): texto con fuente
      Párrafo: veredicto parcial

H2: Sección "lo que no te cuentan" (solo texto — ritmo rápido)
  Párrafo intro: "Aquí va lo que nadie te dice:"
  H3: Punto 1
    Párrafo corto + dato
  H3: Punto 2
    Párrafo corto
  H3: Punto 3
    Párrafo corto
  (SIN imágenes — opinión pura, el texto es el protagonista)

--- separador ---

H2: "🏆 Mi veredicto"
  CALLOUT ÁMBAR: frase síntesis (ej: "Como los coches eléctricos en 2012")
  Párrafo: predicción concreta con datos
  Párrafo: ¿y España/Europa?
  Párrafo: cierre con gancho memorable

--- separador ---

H2: "💡 ¿Sabías que…?"
  Párrafo con dato curioso + link a fuente

H2: "¿Te ha servido?"
H2: "Cada semana más como esto en tu bandeja"
  📷 OG image del artículo
  Botón: "Suscríbete gratis"
  Texto legal afiliados

FOOTER (automático Beehiiv)
  "Keep Reading" (automático)
  Copyright + social links + unsubscribe
```

---

## Diferencias clave entre templates

| Aspecto | Review/Comparativa | Editorial/Opinión |
|---|---|---|
| **Estructura por producto** | Card info + pros/contras + CTA Amazon | Narrativo, sin cards ni listas |
| **Imágenes** | Fotos de producto + mascota | Fotos prensa/evento + contexto |
| **Tabla comparativa** | Sí (obligatoria) | No |
| **Botones afiliado** | Sí (por cada producto recomendado) | No |
| **Sección "No recomiendo"** | Sí | No aplica |
| **Callouts** | "Mi opinión" por producto (gris) | Callouts ámbar para datos bomba |
| **Tono** | Práctico, concreto, "esto sí, esto no" | Analítico, opinado, con predicciones |
| **Sección solo texto** | No | Sí ("lo que no te cuentan" — ritmo H3+párrafo rápido) |

## Reglas comunes a ambos templates

- Primera persona SIEMPRE plural ("hemos investigado", "nos parece")
- Imágenes inline: después del párrafo que las justifica, NUNCA bajo el H2
- CTA mid-article obligatorio entre la mitad del artículo
- Sección "Sabías que" + CTA final siempre al cierre
- Hero image: WebP comprimido, composición close-up, sin neones (ver asset-catalog.md)
- "Keep Reading" lo genera Beehiiv automáticamente — no incluir sección manual de "Más en ROBOHOGAR"
