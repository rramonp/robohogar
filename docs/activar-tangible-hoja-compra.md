# Activar tangible "Hoja de Compra" en Beehiiv — checklist Rafael

> Checklist operativo para poner en producción el primer lead magnet de ROBOHOGAR (Hoja de Compra ROBOHOGAR v2). Tiempo estimado: ~60-75 min en una sola sesión, distribuibles en 2 tandas si hace falta. Todo el material (PDF, snippets, emails) ya está listo — este documento te guía paso a paso.

## 📌 Frases trigger para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Arrancar en limpio | **"Retomamos activar-tangible — empezamos paso 1"** |
| Siguiente paso | **"Retomamos activar-tangible — siguiente paso"** |
| Ver estado | **"¿En qué paso del activar-tangible estamos?"** |
| Si algo falla en Beehiiv | **"Retomamos activar-tangible — se rompe en [paso N]"** |

---

## Prerequisitos (verificar antes de empezar)

- [ ] Plan Beehiiv Scale activo (ya confirmado 2026-04-18).
- [ ] PDF Hoja de Compra v2 listo en `content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.pdf` (214 KB, 4 pp). Abrir para verificar que se ve bien.
- [ ] Acceso a Beehiiv dashboard.

---

## Paso 1 — Subir el PDF como Digital Product free (15 min)

Ficha completa pre-rellenada en [`content/lead-magnets/hoja-compra/beehiiv-ficha.md`](../content/lead-magnets/hoja-compra/beehiiv-ficha.md) — ábrela en otra pestaña para copy-paste directo.

### 1.1 — Crear el producto

- [ ] **Beehiiv dashboard → Monetize → Digital Products → New Product**.
- [ ] **File/Download for purchase:** subir `hoja-compra-robohogar-v2.pdf` (214 KB, 4 pp).
- [ ] **Price:** `0 €` (free lead magnet).

### 1.2 — Rellenar los 10 campos desde la ficha

- [ ] **Product name:** `Hoja de Compra ROBOHOGAR · 10 preguntas antes de comprar`
- [ ] **Description:** `PDF 2 páginas. 10 preguntas que te ahorran 600 € antes de comprar tu robot doméstico.`
- [ ] **Product details** (rich text): copiar los 6 bloques con bold en los encabezados (Qué es · Qué cubre · Para quién es · Para quién no es · Qué incluye · Qué pasa al descargarlo). Texto completo en `beehiiv-ficha.md § Product details`.
- [ ] **Call-to-action copy:** `Descargar gratis`
- [ ] **Post-purchase redirect:** (dejar vacío)
- [ ] **Survey:** `No survey` (no cambiar).
- [ ] **Product page URL:** editar a `hoja-de-compra` (borrar el auto-generado largo).
- [ ] **Send review request emails:** ⚠️ **DESACTIVAR toggle (OFF).** En fase 0-30 subs los reviews placeholder hacen daño.
- [ ] **Images:** subir Primary con `content/lead-magnets/hoja-compra/assets/thumbnail-hoja-compra-1280x720.jpg` (47 KB, 16:9 ya recortado y optimizado para product card de Beehiiv). **NO usar directamente la portada del PDF** — es A4 vertical y se desborda.

### 1.3 — Guardar y capturar la URL

- [ ] Guardar el producto. Beehiiv genera URL `https://robohogar.com/products/hoja-de-compra`.
- [ ] **Copiar la URL del digital product.** La necesitas en el Paso 3 (welcome email).
- [ ] Pegar la URL aquí para referencia:
   ```
   URL digital product: ____________________________________
   ```

### 1.4 — Verificar el preview de la landing

- [ ] Abrir el preview del producto en Beehiiv (botón "Preview").
- [ ] Comprobar que Product name + Description + Product details se renderizan bien.
- [ ] **Importante:** los "reviews" (4.0 · 1245 reviews) del preview son placeholder de Beehiiv, NO son tuyos — desaparecen en producción hasta que lleguen reales.

---

## Paso 2 — Activar Double Opt-In (GDPR) (3 min)

> **⚠️ No confundir con "Preferences"** (Audience → Preferences). El Preference Center es otra cosa — es para que los suscriptores elijan tipos de contenido. No lo uses todavía.

1. [ ] **Settings (engranaje lateral) → Emails → Preset Emails → toggle ON "Double Opt-in Email"**.
   - Ruta confirmada con [docs oficiales Beehiiv](https://www.beehiiv.com/support/article/13081072798743-how-to-enable-double-opt-in-and-smart-nudge).
2. [ ] Editar el confirmation email con copy simple (**plain text, sin logos ni imágenes inline** — el header/footer global de Beehiiv ya incluye branding, y plain text mejora deliverability a Primary):
   - Subject: `Confirma tu email (15 segundos)`
   - Heading (H1): `Confirma y empezamos`
   - Cuerpo: `Hola, gracias por suscribirte a ROBOHOGAR. Confirma tu email con el botón de abajo y empezamos: si viniste por la Hoja de Compra, te llega en cuanto confirmes. Si no, recibirás el newsletter de los martes a las 9:00.`
   - Botón CTA: `Confirmar email`
   - **Regla:** no añadir logo ni imágenes en el cuerpo del email. Beehiiv ya inyecta header/footer con el branding global. Elementos visuales extra → Gmail/Outlook lo clasifican en Promotions → menos conversiones.
3. [ ] **Smart Nudge** (debería aparecer en la misma sección Preset Emails): **ON también** — envía recordatorio auto si no confirman en X días, sube conversión double opt-in sin trabajo extra.
4. [ ] Guardar.

---

## Paso 3 — Crear Welcome Automation "MVP 2 emails" (20-25 min)

Este es el corazón del flow. Los copies completos están en [`welcome-flow-setup.md`](welcome-flow-setup.md) § Email 1 y § Email 2 — abrirlo en otra pestaña para copy-paste.

### 3.1 — Desactivar welcome email único (1 min)

1. [ ] **Settings → Emails → Preset Emails → "Welcome Email" → toggle OFF**.
   - Mismo menú donde activaste Double Opt-In en el Paso 2. El Welcome Email nativo vive ahí junto a Double Opt-In, Smart Nudge y otros preset emails.
   - Si no lo desactivas, los suscriptores reciben 3 emails (1 welcome nativo + 2 del automation) → redundante.

### 3.2 — Modificar la Automation existente (15-20 min)

> **Nota:** si ya tienes una Automation "Welcome Email" antigua (trigger "Signed up" + 1 email welcome narrativo), REÚSALA. Editar es más rápido que crear nueva y conserva las métricas históricas como baseline. Si no tienes ninguna, crea una nueva con trigger `Signed up` (Beehiiv respeta double opt-in automáticamente → solo dispara tras confirmar).

1. [ ] **Automations → abrir la automation existente "Welcome Email"** (o New Automation si no tienes ninguna).
2. [ ] **Renombrar:** click en el icono 🖉 junto al título → poner `Welcome MVP — Hoja de Compra`.
3. [ ] **Verificar trigger:** debe ser `Signed up` (con Double Opt-In activo Beehiiv dispara solo tras confirmar — no hace falta cambiarlo).
4. [ ] **Editar el Email existente:**
   - Subject: `Tu PDF (y una pregunta)`
   - Preheader: `La Hoja de Compra ROBOHOGAR está dentro. 15 seg de lectura.`
   - From name: `Rafael de ROBOHOGAR`
   - Cuerpo: **reemplazar por completo** el texto viejo. Copiar el bloque de código de [`welcome-flow-setup.md § Email 1`](welcome-flow-setup.md).
   - **Importante:** sustituir `<URL_DEL_DIGITAL_PRODUCT>` por la URL que copiaste en paso 1.3.
5. [ ] **Añadir Step nuevo → Wait:** `72 hours` (3 días). Click en `+` bajo el Email 1.
6. [ ] **Añadir Step nuevo → Send email:** segundo email tras el Wait.
   - Subject: `Qué esperar (y 2 joyas)`
   - Preheader: `La ruta ROBOHOGAR en 2 minutos + 2 lecturas mientras llega el martes.`
   - From name: `Rafael de ROBOHOGAR`
   - Cuerpo: copiar el bloque de código de [`welcome-flow-setup.md § Email 2`](welcome-flow-setup.md).
   - Sustituir `<URL_DEL_DIGITAL_PRODUCT>` por la misma URL del paso 1.3.
7. [ ] **Publish changes** (botón arriba derecha) — deja la automation LIVE con los cambios.

**Sobre suscriptores previos:** los 4 (o los que sean) que ya recibieron el welcome viejo NO reciben los nuevos emails. Beehiiv solo dispara el flow para suscriptores futuros. Si quieres que esos 4 reciban la Hoja de Compra, enviales un broadcast manual segmentado (no urgente, opcional).

### 3.3 — Prueba en cuenta de test (5 min)

1. [ ] Suscribirse con un email personal (no el de Beehiiv, uno que no esté ya suscrito).
2. [ ] Confirmar el double opt-in cuando llegue.
3. [ ] Verificar que el **Email 1** llega en segundos con el link al PDF funcionando.
4. [ ] Esperar 72 h (o cambiar el delay temporalmente a 5 min, probar y volver a 72 h).
5. [ ] Verificar que el **Email 2** llega con los 2 links a artículos evergreen.
6. [ ] Si algo falla, revisar: (a) URL del digital product correcta, (b) double opt-in activo, (c) automation publicado (ON).

---

## Paso 4 — Insertar los banners en los 3 artículos publicados (15-20 min)

Snippets ya personalizados con UTM en: [`content/templates/banner-lead-magnet-snippets.md`](../content/templates/banner-lead-magnet-snippets.md).

Por cada uno de los 3 artículos:

### 4.1 — Artículo #0 · Robots de escritorio con IA

1. [ ] Abrir el post en **Beehiiv Posts → mejor-robot-asistente-ia-2026 → Edit**.
2. [ ] Insertar bloque HTML (Beehiiv: botón `+` → Custom HTML) **tras el primer callout de intro**, antes del primer `<h2>`.
   - Copiar el snippet del § "Snippet 1" de `banner-lead-magnet-snippets.md`.
3. [ ] Insertar el mismo bloque **tras el veredicto / bloque de conclusión**, antes del CTA gris final de suscripción.
4. [ ] **Save + Publish (re-publish).** Beehiiv no reenvía email, solo actualiza la versión web.

### 4.2 — Artículo #2 · Roborock Saros Z70 review

1. [ ] Beehiiv Posts → `roborock-saros-z70-review` → Edit.
2. [ ] Mismas 2 posiciones: tras intro + tras veredicto.
3. [ ] Snippet del § "Snippet 2" (UTM `src=roborock-saros-z70-review` ya personalizado).
4. [ ] Save + Publish.

### 4.3 — Artículo #5 · Samsung Jet Bot Steam Ultra review

1. [ ] Beehiiv Posts → `samsung-jet-bot-steam-ultra-review` → Edit.
2. [ ] Mismas 2 posiciones: tras intro + tras veredicto.
3. [ ] Snippet del § "Snippet 3" (UTM `src=samsung-jet-bot-steam-ultra-review` ya personalizado).
4. [ ] Save + Publish.

**Nota:** los artículos de humanoides (#1, #3, #4) NO reciben banner — la Hoja de Compra NO cubre humanoides. Esperarán su propio tangible específico.

---

## Paso 5 — Validación end-to-end (10 min)

1. [ ] Abrir en **ventana de incógnito** uno de los 3 artículos con banner activo.
2. [ ] Scroll hasta el banner: debe verse el bloque dark con "Antes de comprar → Descarga gratis la Hoja de Compra ROBOHOGAR".
3. [ ] Click en el botón "Descargar gratis →".
4. [ ] Suscribirse con un email nuevo (no uno ya usado).
5. [ ] Confirmar el double opt-in.
6. [ ] Verificar que llega Email 1 con el PDF.
7. [ ] Descargar el PDF y verificar que es la versión correcta (v2 — portada con icon robot top-left, backcover con "Si te ha servido").
8. [ ] Verificar en Beehiiv analytics que aparece el suscriptor nuevo con el UTM correcto en el campo "source".

Si los 8 pasos funcionan → **tangible operativo** ✅.

---

## Paso 6 — Monitoreo post-lanzamiento (tras 2-3 semanas)

Métricas a revisar en Beehiiv analytics semanalmente:

- [ ] **CVR por artículo** (suscriptores vía `src=<slug>` / visitas únicas al post). Objetivo 3-6 %.
- [ ] **Open rate Email 1** (objetivo ≥60 %).
- [ ] **Click rate del PDF en Email 1** (objetivo ≥40 %).
- [ ] **Reply rate Email 1** (objetivo ≥15 % — señal Gmail Primary).
- [ ] **Open rate Email 2** (objetivo ≥45 %).

Si CVR <2 % en algún artículo → probar cambios de copy del banner o eliminar banner de ese artículo (señal de mal encaje temático — el #0 Asistentes IA es el más probable).

Si reply rate Email 1 <5 % → revisar si la pregunta "¿qué zona te cuesta limpiar?" está funcionando. Puede necesitar reescritura más directa.

---

## Siguiente paso tras validación

Cuando el tangible lleve ≥2 semanas operativo y los 3 artículos estén convirtiendo a tasas razonables:

- Si CVR >4 %: el tangible funciona. Construir **segundo tangible** (Guía primer mes aspirador). Skill `/pdf-brand cheatsheet` ya existe, solo falta redactar el `data.py`.
- Si CVR <2 %: iterar antes de lanzar más tangibles. Revisar copy del banner, posición, y consistencia visual PDF ↔ artículo.

---

## Referencias cruzadas

- PDF source: [`content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.pdf`](../content/lead-magnets/hoja-compra/hoja-compra-robohogar-v2.pdf)
- Snippets banner: [`content/templates/banner-lead-magnet-snippets.md`](../content/templates/banner-lead-magnet-snippets.md)
- Copy emails welcome: [`docs/welcome-flow-setup.md`](welcome-flow-setup.md)
- Regla sistémica: [`.claude/rules/tangibles.md`](../.claude/rules/tangibles.md)
- Skill generador PDF: [`.claude/commands/pdf-brand.md`](../.claude/commands/pdf-brand.md)
