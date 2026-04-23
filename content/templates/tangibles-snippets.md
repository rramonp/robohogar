# Tangibles inline — plantillas canónicas ROBOHOGAR

> **Fuente de verdad** para todos los tangibles inline de artículos ROBOHOGAR (checklist, decision-tree, dossier, cuadro sí/no, tabla-standalone). Cada tangible se entrega en el borrador con **dos representaciones en orden**:
>
> 1. **Preview renderizado** (HTML con clases CSS del `<style>` global del borrador) — visible en el preview navegador para validar visual.
> 2. **Snippet-block con HTML en estilos inline escapado** (`<pre><code>`) — Rafael copia a Beehiiv vía `/html` → "Custom HTML block".
>
> Regla completa + incidente origen: `@rules/design.md § Bloques de código para snippets HTML inline en borradores § Ampliación 2026-04-23`.
> Variedad editorial (rotar tipo entre artículos consecutivos): `@.claude/commands/content-draft.md § 3 bis — Diversificación de tangible y cierre`.

---

## Principios comunes a todos los tangibles

- **Mobile-first obligatorio.** Todo snippet debe renderizar legible en viewport 375 px sin scroll horizontal ni wrap roto. Sin `@media queries` (Beehiiv Custom HTML no siempre respeta media en email render): el stack vertical natural y padding/font-size generosos son la única defensa.
- **Estilos inline obligatorios en el snippet copy-paste.** Las clases CSS del `<style>` del borrador NO viajan a Beehiiv. Cada elemento lleva `style="..."` con todos los estilos necesarios.
- **Paleta ROBOHOGAR**: crema `#FFF9EF` · ámbar `#F5A623` · gris `#6B7280` · texto `#0C0C0C` · blanco `#FFFFFF` · azul marino `#283642` (solo en CTAs dark).
- **Tipografía**: cuerpo `'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif` · titulares `'DM Sans',sans-serif`.
- **Sin `<strong>` dentro de callout crema** (regla `@rules/editorial.md § Política de negritas`). Usar `<span style="font-weight:700;color:#X;">` cuando se necesite énfasis visual — el color + peso distingue sin sobrecargar.
- **Envolver en `.snippet-block`** con el patrón canónico: header "📋 Snippet N · [tipo] · [descripción]" + hint "En Beehiiv: `/html` → Custom HTML block" + `<pre><code>` con HTML escapado (`<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`).

---

## Rotación de formatos (variedad editorial)

Anti-repetición de tangible entre artículos consecutivos. Ver `@.claude/commands/content-draft.md § 3 bis`. No repetir el mismo tipo en 2 de los últimos 3 artículos.

| Tipo | Cuándo usar | Estado plantilla |
|---|---|---|
| **Checklist accionable** | Guías de compra con decisión lineal (5-7 preguntas/pasos) | ✅ Canonizada abajo |
| **Decision-tree** | Guías de compra con bifurcaciones claras (4-6 preguntas con respuestas → modelo) | ✅ Canonizada abajo |
| **Dossier 3-datos clave** | Editoriales anti-hype · ancla-de-realidad con 3 cifras + fuente | 🟡 Pendiente canonizar con próximo artículo |
| **Cuadro sí / no** | Comparativas binarias: "qué hacer / qué no hacer" en 2 columnas | 🟡 Pendiente canonizar |
| **Tabla standalone comparativa** | Review multi-producto con 4 columnas apretadas (mobile-first dura) | 🟡 Pendiente canonizar |
| **[Nuevos formatos]** | A medida que Rafael introduzca nuevos tangibles, documentar aquí con preview + snippet inline | — |

**Regla para añadir nuevos tipos:** cuando un artículo introduzca un tangible de formato no canonizado todavía, el primer uso se desarrolla ad-hoc en el borrador; tras la aprobación de Rafael, **se extrae a esta tabla + se añade su plantilla** en la sección "Plantillas" de abajo. No se deja ad-hoc dos veces.

---

## Plantillas canónicas

### 1. Checklist accionable

**Cuándo**: guía de compra con 3-7 preguntas/pasos lineales antes del veredicto.

#### Preview renderizado (HTML con clases del borrador)

```html
<div class="checklist">
  <h3>🏁 Checklist — [TÍTULO, ej: 5 preguntas antes de comprar]</h3>
  <ol>
    <li><strong>¿Pregunta 1?</strong><br>
    Respuesta/contexto con opciones por perfil.</li>

    <li><strong>¿Pregunta 2?</strong><br>
    Respuesta/contexto.</li>

    <li><strong>¿Pregunta 3?</strong><br>
    Respuesta/contexto.</li>

    <li><strong>¿Pregunta 4?</strong><br>
    Respuesta/contexto.</li>

    <li><strong>¿Pregunta 5?</strong><br>
    Respuesta/contexto.</li>
  </ol>
</div>
```

CSS global (ya está en todos los borradores ROBOHOGAR):
```css
.checklist { background: #FFF9EF; border: 1px solid #F5A623; border-radius: 10px; padding: 20px; margin: 20px 0; }
.checklist h3 { margin-top: 0; color: #0C0C0C; }
.checklist ol { margin: 12px 0 0 20px; padding: 0; }
.checklist li { margin: 12px 0; }
```

#### Snippet inline copy-paste (para pegar en Beehiiv `/html`)

```html
<div class="snippet-block">
  <p class="snippet-header">📋 Snippet N · Checklist · [DESCRIPCIÓN]</p>
  <p class="snippet-hint">En Beehiiv: escribe <code>/html</code> → "Custom HTML block" → pega el código de abajo.</p>
  <pre><code>&lt;div style="background:#FFF9EF;border:1px solid #F5A623;border-radius:10px;padding:20px;margin:20px 0;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;color:#0C0C0C;"&gt;
  &lt;div style="font-family:'DM Sans',sans-serif;font-size:18px;font-weight:700;color:#0C0C0C;margin:0 0 12px;line-height:1.3;"&gt;🏁 Checklist — [TÍTULO]&lt;/div&gt;
  &lt;ol style="margin:12px 0 0 20px;padding:0;font-size:15px;line-height:1.55;"&gt;
    &lt;li style="margin:12px 0;"&gt;&lt;span style="font-weight:700;"&gt;¿Pregunta 1?&lt;/span&gt;&lt;br&gt;Respuesta/contexto con opciones por perfil.&lt;/li&gt;
    &lt;li style="margin:12px 0;"&gt;&lt;span style="font-weight:700;"&gt;¿Pregunta 2?&lt;/span&gt;&lt;br&gt;Respuesta/contexto.&lt;/li&gt;
    &lt;li style="margin:12px 0;"&gt;&lt;span style="font-weight:700;"&gt;¿Pregunta 3?&lt;/span&gt;&lt;br&gt;Respuesta/contexto.&lt;/li&gt;
    &lt;li style="margin:12px 0;"&gt;&lt;span style="font-weight:700;"&gt;¿Pregunta 4?&lt;/span&gt;&lt;br&gt;Respuesta/contexto.&lt;/li&gt;
    &lt;li style="margin:12px 0;"&gt;&lt;span style="font-weight:700;"&gt;¿Pregunta 5?&lt;/span&gt;&lt;br&gt;Respuesta/contexto.&lt;/li&gt;
  &lt;/ol&gt;
&lt;/div&gt;</code></pre>
</div>
```

**Notas de adaptación**: sustituir `[TÍTULO]` por el título concreto (obligatorio H2 anterior empieza por `Checklist —`). Sustituir cada `¿Pregunta N?` y `Respuesta/contexto.` por el texto del artículo. Añadir o quitar `<li>` según el número de ítems (3-7 máximo). No meter `<strong>` dentro del `<li>` — usar `<span style="font-weight:700;">` como se ve (regla dura: cero bold en callouts crema).

---

### 2. Decision-tree (árbol de decisión)

**Cuándo**: guía de compra con bifurcaciones condicionales (4-6 preguntas que ramifican a modelos concretos). Ejemplo canónico: [`content/articulos/mejor-robot-aspirador-mascotas-2026/borrador.html § árbol de decisión`](../articulos/mejor-robot-aspirador-mascotas-2026/borrador.html).

#### Preview renderizado (HTML con clases del borrador)

```html
<div class="decision-cards">

  <div class="decision-card">
    <p class="q-num">Pregunta 1</p>
    <p class="q-text">¿[Pregunta principal condicional]?</p>
    <div class="path"><span class="path-label">Sí →</span>Pasa a la pregunta 2.</div>
    <div class="path"><span class="path-label">No →</span>Pasa a la pregunta 3.</div>
  </div>

  <div class="decision-card">
    <p class="q-num">Pregunta 2 · [Contexto rama sí]</p>
    <p class="q-text">¿[Subpregunta]?</p>
    <div class="path"><span class="path-label">Sí →</span><span class="path-model">[Modelo A]</span><span class="path-note">[Razón técnica corta].</span></div>
    <div class="path"><span class="path-label">No →</span><span class="path-model">[Modelo B]</span><span class="path-note">[Razón técnica corta].</span></div>
  </div>

  <!-- repetir para preguntas 3, 4... cada bifurcación termina en un modelo -->

</div>
```

CSS global (añadir al `<style>` del borrador si no existe):
```css
.decision-cards { margin: 20px 0; }
.decision-card { background: #FFF9EF; border: 1px solid #F5A623; border-radius: 10px; padding: 16px 18px; margin: 14px 0; }
.decision-card .q-num { font-family: 'DM Sans', sans-serif; font-size: 11px; font-weight: 700; color: #F5A623; text-transform: uppercase; letter-spacing: 1.2px; margin: 0 0 4px; }
.decision-card .q-text { font-family: 'DM Sans', sans-serif; font-size: 16px; font-weight: 700; color: #0C0C0C; line-height: 1.3; margin: 0 0 12px; }
.decision-card .path { font-size: 15px; line-height: 1.4; margin: 8px 0 0; padding: 10px 12px; background: #FFFFFF; border-left: 3px solid #F5A623; border-radius: 4px; }
.decision-card .path-label { font-weight: 700; color: #F5A623; margin-right: 4px; }
.decision-card .path-model { font-weight: 700; color: #0C0C0C; }
.decision-card .path-note { display: block; font-size: 13px; color: #6B7280; margin-top: 3px; font-style: italic; }
```

#### Snippet inline copy-paste (para pegar en Beehiiv `/html`)

```html
<div class="snippet-block">
  <p class="snippet-header">📋 Snippet N · Árbol de decisión · [DESCRIPCIÓN]</p>
  <p class="snippet-hint">En Beehiiv: escribe <code>/html</code> → "Custom HTML block" → pega el código de abajo. Estilos inline compatibles con móvil y email.</p>
  <pre><code>&lt;div style="margin:24px 0;font-family:'Inter',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;"&gt;

  &lt;div style="background:#FFF9EF;border:1px solid #F5A623;border-radius:10px;padding:16px 18px;margin:14px 0;"&gt;
    &lt;div style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;color:#F5A623;text-transform:uppercase;letter-spacing:1.2px;margin:0 0 4px;"&gt;Pregunta 1&lt;/div&gt;
    &lt;div style="font-family:'DM Sans',sans-serif;font-size:16px;font-weight:700;color:#0C0C0C;line-height:1.3;margin:0 0 12px;"&gt;¿[Pregunta principal condicional]?&lt;/div&gt;
    &lt;div style="font-size:15px;line-height:1.4;margin:8px 0 0;padding:10px 12px;background:#FFFFFF;border-left:3px solid #F5A623;border-radius:4px;color:#0C0C0C;"&gt;&lt;span style="font-weight:700;color:#F5A623;margin-right:4px;"&gt;Sí →&lt;/span&gt;Pasa a la pregunta 2.&lt;/div&gt;
    &lt;div style="font-size:15px;line-height:1.4;margin:8px 0 0;padding:10px 12px;background:#FFFFFF;border-left:3px solid #F5A623;border-radius:4px;color:#0C0C0C;"&gt;&lt;span style="font-weight:700;color:#F5A623;margin-right:4px;"&gt;No →&lt;/span&gt;Pasa a la pregunta 3.&lt;/div&gt;
  &lt;/div&gt;

  &lt;div style="background:#FFF9EF;border:1px solid #F5A623;border-radius:10px;padding:16px 18px;margin:14px 0;"&gt;
    &lt;div style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:700;color:#F5A623;text-transform:uppercase;letter-spacing:1.2px;margin:0 0 4px;"&gt;Pregunta 2 · [Contexto rama]&lt;/div&gt;
    &lt;div style="font-family:'DM Sans',sans-serif;font-size:16px;font-weight:700;color:#0C0C0C;line-height:1.3;margin:0 0 12px;"&gt;¿[Subpregunta]?&lt;/div&gt;
    &lt;div style="font-size:15px;line-height:1.4;margin:8px 0 0;padding:10px 12px;background:#FFFFFF;border-left:3px solid #F5A623;border-radius:4px;color:#0C0C0C;"&gt;&lt;span style="font-weight:700;color:#F5A623;margin-right:4px;"&gt;Sí →&lt;/span&gt;&lt;span style="font-weight:700;color:#0C0C0C;"&gt;[Modelo A]&lt;/span&gt;&lt;span style="display:block;font-size:13px;color:#6B7280;margin-top:3px;font-style:italic;"&gt;[Razón técnica corta].&lt;/span&gt;&lt;/div&gt;
    &lt;div style="font-size:15px;line-height:1.4;margin:8px 0 0;padding:10px 12px;background:#FFFFFF;border-left:3px solid #F5A623;border-radius:4px;color:#0C0C0C;"&gt;&lt;span style="font-weight:700;color:#F5A623;margin-right:4px;"&gt;No →&lt;/span&gt;&lt;span style="font-weight:700;color:#0C0C0C;"&gt;[Modelo B]&lt;/span&gt;&lt;span style="display:block;font-size:13px;color:#6B7280;margin-top:3px;font-style:italic;"&gt;[Razón técnica corta].&lt;/span&gt;&lt;/div&gt;
  &lt;/div&gt;

  &lt;!-- repetir para preguntas 3, 4... cada bifurcación termina en &lt;span class="path-model"&gt; con el modelo --&gt;

&lt;/div&gt;</code></pre>
</div>
```

**Notas de adaptación**: numerar `Pregunta 1 / Pregunta 2 / ...` secuencialmente. Cada pregunta va con eyebrow (`q-num`) en ámbar + pregunta principal (`q-text`) en negro + 2 paths (cada uno con etiqueta Sí/No y destino: otra pregunta o modelo final). La profundidad máxima recomendada es 4 bifurcaciones (5 modelos finales); más de eso satura al lector móvil.

---

### 3. Dossier 3-datos clave 🟡 pendiente canonizar

Plantilla a desarrollar con el próximo editorial anti-hype que use este formato. Concepto: 3 tarjetas apiladas, cada una con un dato + fuente + tesis corta. Cuando se haga, copiar aquí preview + snippet inline.

---

### 4. Cuadro sí / no 🟡 pendiente canonizar

Plantilla a desarrollar con el próximo tutorial/guía que use este formato. Concepto: 2 columnas responsive (apilan en móvil) con "qué hacer" / "qué NO hacer" en paralelo.

---

### 5. Tabla standalone comparativa 🟡 pendiente canonizar

Plantilla a desarrollar. Las tablas del borrador ya usan `<table class="comparativa">` con CSS global — para el snippet inline hay que replicar los estilos `<table style="border-collapse:collapse;..."> <th style="..."> <td style="..."> ` con atención especial al máximo de 4 columnas mobile-first (regla `@rules/editorial.md § Formato técnico tablas`).

---

## Cómo usar desde `/content-draft`

Cuando el skill decida el tangible del artículo (paso 3 bis · diversificación), leer la plantilla correspondiente de este archivo, sustituir placeholders con el contenido editorial del artículo y emitir **ambos bloques** en el `borrador.html`:

1. Preview renderizado en la sección del tangible (entre el H2 `Checklist — ...` o `El árbol de decisión...` y el siguiente `<div class="separator"></div>`).
2. `.snippet-block` inmediatamente después del preview, con el HTML en estilos inline escapado.

Si el tangible del artículo es de un tipo **no canonizado todavía** (🟡): desarrollar ad-hoc en el borrador + proponer a Rafael extraer la plantilla a este archivo tras aprobación.
