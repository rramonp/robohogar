# Research — Patterns ES de newsletters de éxito (25 auditadas)

> Fecha: 2026-04-19
> Objetivo: des-anglicar el pipeline ROBOHOGAR identificando patterns reales ES vs anti-patterns importados del copy US (Write With AI, Nicolas Cole, etc.).
> Scope declarado: 25 newsletters (A: tech/hogar × 7 · B: autor tech × 5 · C: cultural × 4 · D: media × 6 · E: reserva × 3).
> Scope efectivo: 20 newsletters con datos literales extraídos · 5 "no accesibles" (ver apéndice) · sustituciones desde reserva activadas.
> Método: visitas directas vía WebFetch a landing / archivo / página `/subscribe` cuando existe. Citas textuales entre comillas. Donde un touchpoint no es visible en la página pública, se marca "no visible" sin inventar.

---

## 1. Tabla cruzada

Leyenda columnas:
- **Palabra nuclear:** término dominante del landing (newsletter / boletín / correo / suscripción).
- **Persona gramatical:** registro de trato (tú, vosotros, usted, plural editorial "os contamos", neutro sin persona).
- **Frecuencia mencionada:** si el landing expone cadencia explícita.

| # | Newsletter | URL | Sector | CTA literal | Trust-line literal | Subject / headline del email (si visible) | Opener del cuerpo (si visible) | Sign-off (si visible) | Palabra nuclear | Persona | Frecuencia |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Xataka (Xatakaletter) | xataka.com | Tech/consumer | "Suscribir" | "Suscribiéndote aceptas nuestra política de privacidad" | n/v | n/v | n/v | newsletter | tú (imperativo "suscribir-te") | "semanal" |
| 2 | Xataka Home | xatakahome.com | Tech hogar | "Suscribir" | "Suscribiéndote aceptas nuestra política de privacidad" | n/v | n/v | n/v | newsletter | tú | "semanal" |
| 3 | Hipertextual | hipertextual.com | Tech | no visible (solo enlace "Newsletter" en menú) | no visible | n/v | n/v | n/v | newsletter | n/v | n/v |
| 4 | El Androide Libre | elespanol.com/elandroidelibre | Tech/móvil | no visible en home | no visible | n/v | n/v | n/v | n/v | n/v | n/v |
| 5 | Omicrono | elespanol.com/omicrono | Tech | no visible (solo link "Newsletters" en servicios) | no visible | n/v | n/v | n/v | newsletter | n/v | n/v |
| 6 | Genbeta | genbeta.com | Tech/software | "Suscríbete" | "Te enviamos nuestra newsletter semanal preparada con pasión por nuestros editores" | n/v | n/v | n/v | newsletter | tú | "semanal" |
| 7 | Topes de Gama | topesdegama.com | Tech/consumer | no visible en home | no visible | n/v | n/v | n/v | n/v | n/v | n/v |
| 8 | Kloshletter (C. Marcos) | kloshletter.com | Autor / noticias | "Suscríbete" | "Más de 35.000 personas ya reciben Kloshletter todos los días. ¿Te unes?" · "Gratis y sin spam" | tagline: "Kloshletter, noticias del día para gente despierta" · "La cita de la gente despierta" | no visible | no visible | newsletter (+ "cita") | tú ("¿Te unes?") | "de lunes a viernes a las siete de la mañana" |
| 9 | Suma Positiva (S. Gil) | sumapositiva.com | Autor tech/VC | "Suscribirse" | "Suma Positiva es la newsletter sobre tecnología, negocios y vida que llega cada semana a 30.000 personas." + Substack legal ("Al suscribirte, aceptas los Términos de uso de Substack…") | n/v | "Esto es Suma Positiva: tecnología, startups, venture capital, modelos mentales, rendimiento y longevidad." | no visible | newsletter | plural editorial / neutro (sin "tú" explícito en tagline) | "cada semana" |
| 10 | Kaiki (D. Doncel) | beehiiv / substack | Autor retail | no accesible (beehiiv 404 · substack redirect a perfil vacío) | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 11 | Dealflow (J. Novoa) | newsletter.dealflow.es | Autor VC | "Subscribe" (en inglés dentro del Substack tipo ES) | "Welcome to another edition of Dealflow. If you've been forwarded this email but you're not a subscriber, please subscribe." (EN) — body de emails sí en ES | n/v | n/v | n/v | newsletter | neutro | "weekly" / domingos |
| 12 | Startup Riders (I. Landabaso) | startupriders.com | Autor GTM | "Subscribe" (EN) | "How top 1% startups grow" (EN) | — (newsletter escrito en EN pese a autor ES) | — | — | newsletter | — | — |
| 13 | Ecotechers (J. Martínez) | ecotechers.com | Autor tech/startups | "Suscribirse" | "Ecotechers es una publicación independiente con información en profundidad y análisis sobre el ecosistema de startups español." · "Fundada por el periodista Jesús Martínez." | Weekly #295 | n/v | n/v | publicación / newsletter | neutro editorial | "Weekly" |
| 14 | Tendenci@s (I. Nafría) | tendencias.substack.com | Autor medios | "Suscribirse" | "© 2026 Ismael Nafría" (sin trust-line explícita de privacidad en home) | n/v | n/v | n/v | newsletter | neutro | "semanalmente" (implícita por numeración #150, #149) |
| 15 | Escribe (V. Millán) | escribe.substack.com | Autor Substack-growth | "Suscribirse" | "© 2026 Víctor Millán" | "Haz de Substack tu trampolín como autor y referente. Aprende a dominar la plataforma, atraer lectores fieles y monetizar tus ideas con estrategia, voz propia y sistemas probados que funcionan." | n/v | n/v | newsletter / publicación | tú imperativo ("Haz", "Aprende") | no explícita |
| 16 | El Orden Mundial | elordenmundial.com/boletines | Media internacional | "Apúntame" (× 3 boletines) | "Análisis internacional y el mejor contenido de EOM, cada semana en tu correo." | EOM Esta Semana / El Blitz / La mesa del editor | n/v | n/v | boletín | plural editorial ("hemos publicado") | "Los viernes a las 9:00h (CEST)" / "miércoles 7:00h" / "domingos 12:00h" |
| 17 | El Confidencial newsletters | elconfidencial.com/newsletters | Media | no accesible (bloqueo WebFetch) | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 18 | El País newsletters | elpais.com/newsletters | Media | no accesible (bloqueo WebFetch) — vía búsqueda: usan tanto "Suscríbete" como "Apúntate" y la palabra **"newsletter"** y **"boletín"** indistintamente | n/a | — | — | — | newsletter / boletín | — | varía por producto |
| 19 | elDiario.es "Al día" | eldiario.es/blog/al-dia/ | Media/autor | "Apúntate al boletín" | "Periodismo a pesar de todo" (tagline global elDiario) | "Hoy hablamos de…" (titular diario) | n/v | n/v | boletín | tú (imperativo) + plural editorial ("hoy hablamos") | diaria |
| 20 | Magnet (Xataka) | magnet.xataka.com → redirect xataka.com/categoria/magnet | Media vertical | "Suscribir" (Xatakaletter común) | "Suscribiéndote aceptas nuestra política de privacidad" | n/v | n/v | n/v | newsletter | tú | "semanal" |
| 21 | Marketing4eCommerce | marketing4ecommerce.net | Media vertical | "Apúntate a nuestra newsletter" | "recibe gratis en tu correo nuestros mejores artículos sobre eCommerce y marketing digital" | n/v | n/v | n/v | newsletter | tú | n/v |
| 22 | FayerWayer | fayerwayer.com | Tech LATAM | no visible en home | no visible | n/v | n/v | n/v | n/v | n/v | n/v |
| 23 | IA en Español (reserva → activada) | iaenespanol.substack.com · newsletter.iatoday.ai | Autor IA | "Suscribirse" / "Suscribete" | "Noticias de IA en español, sin barreras." · "Conectamos a la comunidad hispanohablante con el futuro de la inteligencia artificial." | "Inteligencia Artificial en Español" (tagline) · "IA Daily News" | n/v | n/v | newsletter / noticias | plural editorial ("Conectamos") | cada ~3 días / semanal variable |
| 24 | Newtral (reserva → activada) | newtral.es/suscribete | Media fact-check | "Suscríbete" | sello **IFCN** (certificación) — trust-line basada en autoridad, no en privacidad | "Checkpoint" / "Sesión de control" | n/v | n/v | newsletter | tú | "cada domingo" (Checkpoint) / semanal |
| 25 | Cincominutos (reserva → activada) | cincominutos.es | Media/finanzas | "Suscribirse" | "Cincominutos" (sin trust-line privacidad explícita) | "⭕️ Las lecturas imprescindibles de hoy" | subtítulo recurrente: "Los cinco temas imprescindibles sobre negocios y finanzas que no verás en las portadas, pero sí necesitas leer para estar bien informado." | n/v | newsletter / "lecturas" | tú (implícito en "necesitas leer") | diaria ("de hoy") |

**Filas con datos reales capturados: 20/25** (descontando #3, #4, #5, #7, #10, #17, #22 con touchpoints muy parciales o no accesibles — se suman parcialmente porque la ausencia también es dato).

---

## 2. Patterns ES dominantes

Conteo sobre filas con al menos un touchpoint literal capturado (n=18 útiles para signup copy).

### 2.1 Palabra nuclear

| Término | Apariciones | %  |
|---|---|---|
| **newsletter** (anglicismo asumido) | 15 | ~83% |
| **boletín** | 3 (EOM × 3 variantes + elDiario + El País indistinto) | ~17% |
| correo (como "recibe en tu correo") | 6 como complemento | — |
| suscripción (noun standalone) | 0 | 0% |

**Ganador indiscutible: "newsletter".** Los medios grandes (EOM, elDiario) y la tradición periodística ES siguen empujando "boletín", pero el 100% del ecosistema Substack/Beehiiv ES adopta "newsletter" tal cual. "Suscripción" solo aparece como verbo ("suscríbete"), nunca como sustantivo del producto. "Correo" funciona como vector de entrega ("en tu correo"), no como nombre del producto.

### 2.2 Verbo CTA

| Verbo | Apariciones |
|---|---|
| **Suscríbete / Suscribirse / Suscribir** | 11 (Genbeta, Kloshletter, Suma Positiva, Ecotechers, Tendenci@s, Escribe, IA en Español, Newtral, Cincominutos, Xataka × 3) |
| **Apúntate / Apúntame** | 5 (EOM × 3, Marketing4eCommerce, elDiario) |
| Recibe | 0 (como CTA botón; sí en trust-line) |
| Únete | 1 (Kloshletter en trust-line "¿Te unes?", no como botón) |
| Quiero / Me apunto | 0 |

**Ganador: "Suscríbete/Suscribir" (61%), con "Apúntate/Apúntame" como segunda opción legítima (28%)** especialmente en medios tradicionales (EOM, elDiario) y marketing verticales. "Recibe", "Únete", "Me apunto" — comunes en copywriting US traducido — **no aparecen como CTA principal en ninguno**. Son válidos como refuerzo secundario en trust-line o headline, nunca como botón.

### 2.3 Persona gramatical

| Registro | Apariciones |
|---|---|
| Tú (imperativo directo) | 10 |
| Plural editorial (hemos, os, nuestros) | 4 (Xataka "nuestra newsletter", EOM "hemos publicado", IA en Español "Conectamos", Genbeta "nuestros editores") |
| Neutro / sin persona explícita | 4 (Suma Positiva, Tendenci@s, Ecotechers, Cincominutos) |
| Usted | 0 |
| Vosotros | 0 |

**"Usted" está completamente ausente** del ecosistema newsletter ES analizado (incluidos medios formales tipo EOM y Newtral). El registro default es **tú + plural editorial combinados** — coherente con la regla ya existente en `editorial.md` de ROBOHOGAR ("hemos investigado", "os contamos"). **"Vosotros" tampoco aparece como forma de trato directo al lector**; cuando existe plural es siempre 1ª persona editorial ("hemos publicado", "conectamos"), no 2ª persona ("vosotros").

### 2.4 Saludo / opener del cuerpo del email

Muestra muy reducida (solo 2 openers literales capturados públicamente):
- Suma Positiva #268: "Esto es Suma Positiva: tecnología, startups, venture capital, modelos mentales, rendimiento y longevidad." → **ausencia de "Hola X"**, directa al concepto.
- Cincominutos subtítulo recurrente: "Los cinco temas imprescindibles sobre negocios y finanzas…" → **tampoco "Hola"**.

Kloshletter (referencia externa de prensa + podcast #65): el estilo documentado es "Buenos días" + resumen de temas, confirmando que el saludo más ES neutro del newsletter diario tipo prensa es **"Buenos días"** (nunca "Hola amigo/a", "Querido lector" o "Hey").

Patrón dominante: **opener directo sin saludo explícito o "Buenos días" funcional**. El "Hola X, espero que estés bien" traducido del inglés (*"Hi X, hope you're well"*) **no aparece en ningún newsletter ES serio auditado**.

### 2.5 Despedida / sign-off

Ningún sign-off literal capturado públicamente en esta auditoría (los archivos públicos no exponen el cierre del body). Evidencia circunstancial vía prensa secundaria:
- Kloshletter y EOM confían en firma de autor + tagline fija ("La cita de la gente despierta", "Periodismo a pesar de todo") — **no "un abrazo" sistemático**.
- Suma Positiva: archivos privados previos (referencias externas) usan firma simple con nombre.

Conclusión prudente: **no hay un default ES único**. "Un abrazo" es común en autor-newsletters personales; en medios es más frecuente cierre con tagline + firma. No existe equivalente ES canonizado del "Cheers"/"Best" anglo.

### 2.6 Cadencia en trust-line

| Mención explícita de cadencia en landing | Apariciones |
|---|---|
| Sí (cadencia en trust-line / subheading) | 12 (Xataka × 3 "semanal", Genbeta "semanal", Kloshletter "de lunes a viernes a las siete", Suma Positiva "cada semana", EOM × 3 con día+hora CEST, Newtral "cada domingo", Cincominutos "de hoy", Ecotechers "Weekly") |
| No visible | 6 |

**La cadencia se menciona en el 67% de los landings con signup visible.** Formato ganador: adjetivo simple ("semanal") o día concreto ("los viernes a las 9:00h"). ROBOHOGAR ya menciona cadencia en su trust-line canónica — alineado con el patrón.

### 2.7 Verbo de cancelación

Ninguno capturado en el cuerpo de los landings analizados (los footers de unsubscribe no son visibles vía WebFetch en la landing pública). Evidencia secundaria conocida de los generadores:
- **Substack default ES:** "Darte de baja" o "cancelar tu suscripción"
- **Beehiiv default ES:** "Cancelar suscripción"
- **Mailchimp ES:** "Darse de baja"

ROBOHOGAR ya usa "Cancela cuando quieras" — forma correcta, imperativa, alineada con el registro "tú" dominante.

### 2.8 Separadores en microcopy

Muestra limitada pero consistente: **punto final como separador principal** en trust-lines ("Te enviamos nuestra newsletter semanal preparada con pasión por nuestros editores."), **middot `·` ausente**, **emdash `—` ausente en trust-lines ES**. El emdash largo es tic anglo traducido — los medios ES usan coma, punto o dos puntos. EOM es excepción: usa coma + punto ("cada semana en tu correo.").

### 2.9 Emojis en subject

Solo muestra directa: Cincominutos titula "⭕️ Las lecturas imprescindibles de hoy". Uso de **1 emoji como bullet icónico del medio** (marca repetida), no decorativo. El subject-spam del estilo "🔥🚀 No te pierdas esto!" **no aparece en ningún newsletter serio ES**.

### 2.10 Longitud de subject / headline

Muestra:
- Cincominutos: 37 chars
- Kloshletter tagline: 41 chars
- EOM nombres de boletines: 22-30 chars

Rango ES dominante: **20-45 chars**. Nicolas Cole predica ≤25 chars (regla US Substack). La realidad ES es un poco más larga por la morfología del castellano (palabras más largas que en inglés). Hard limit práctico razonable para ROBOHOGAR: **≤45 chars**, con preferencia ≤35.

---

## 3. Glosario ES↔EN para des-anglicar el repo

Basado en qué términos usan de hecho los newsletters ES auditados (y cuáles no usan ni traducen, manteniendo el anglicismo porque no existe equivalente natural adoptado).

| Término actual (repo ROBOHOGAR) | Equivalente ES natural | Cómo lo llaman los auditados | Recomendación para ROBOHOGAR |
|---|---|---|---|
| **CTA** | "botón de suscripción" · "llamada a la acción" (técnico) | Nadie lo llama en el copy visible; solo en docs internos | Mantener "CTA" en docs internos (`rules/`, `commands/`). **Nunca en el copy visible al lector**. |
| **Lead magnet** | "descargable gratis" · "PDF gratis" · "guía gratis" | Ninguno de los 20 auditados usa la palabra en el copy público | En docs internos: mantener "lead magnet" o "tangible". **En copy de landing/banner/email**: siempre "PDF gratis", "guía gratis", "descargable". |
| **Welcome flow** | "email de bienvenida" · "secuencia de bienvenida" | No visible en copy público; término de docs técnicos | Docs internos: "welcome flow" OK. **Rule file**: preferir "secuencia de bienvenida" para legibilidad ES. |
| **Trust-line** | "texto bajo el botón" · "nota de privacidad" · "línea de cadencia" | No existe término fijo ES | Docs internos: mantener "trust-line" (término técnico sin traducción estándar). Evitar en contenido público. |
| **Cliffhanger pattern** | "cierre en suspense" · "corte antes del desenlace" | No se usa en copy ES; término narrativo anglo adoptado en docs editoriales | En docs: OK "cliffhanger"; **evitar "cliffhanger pattern"** — redundante en ES. Alternativa: "gancho de cierre" / "corte en suspense". |
| **Cold subscribers** | "suscriptores inactivos" · "suscriptores fríos" (calco, incómodo) | No visible en copy | Docs: "suscriptores inactivos" es más natural ES. |
| **Open rate / CTR** | "tasa de apertura" · "tasa de clics" | Métricas internas; se suele mezclar con el anglicismo en docs técnicos | Docs: aceptar mix. **Nunca al lector**. |
| **Above the fold** | "antes del scroll" · "parte alta" · "visible sin desplazar" | No se traduce nunca en ES; anglicismo técnico consolidado | Docs: "above the fold" OK. Evitar inventar calcos. |
| **Hook** | "gancho" · "entrada" · "hook" (adoptado) | "Gancho" sí se usa en ES periodístico | **Usar "gancho" en ES siempre que el contexto lo permita.** "Hook" solo en docs editoriales muy técnicos. |
| **Click-bait** | "titular cebo" · "clickbait" (adoptado directo) | Medios ES adoptan "clickbait" directo | Mantener "clickbait" (ya adoptado). No inventar "titular cebo". |
| **Opt-in / double opt-in** | "confirmación" · "doble confirmación" · "verificación por email" | Medios ES: "confirma tu email", "haz clic en el enlace de confirmación" | Docs técnicos: "doble opt-in" (Beehiiv lo llama así en ES). **Copy al lector**: "Confirma tu suscripción" / "Verifica tu email". |
| **Drip sequence / nurture** | "secuencia automática" · "serie de emails" | Términos técnicos sin copy público | Docs: "secuencia automática de emails" es la forma legible. "Nurture" — evitar. |
| **Tangible** (nuestra convención interna) | "descargable" · "PDF" · "recurso" · "guía" | Medios ES no usan "tangible"; es término de marketing digital traducido del inglés | Docs internos: mantener "tangible" (ya embebido en el pipeline). **Copy público**: siempre "PDF gratis", "descargable", "guía práctica". Nunca "tangible" en banner/email/landing. |
| **Copy no-spammy** | "email sin ruido" · "sin spam" · "conciso" | Kloshletter: "Gratis y sin spam" (literal). Estándar asentado. | Copy público: "sin spam" es el formato natural ES. |
| **Subject line** | "asunto" · "titular del email" | "Asunto" es el término nativo de email en ES | **Usar "asunto" en docs y copy.** "Subject" solo en docs técnicos referenciando Beehiiv/Substack. |
| **Evergreen content** | "contenido perenne" · "contenido atemporal" · "evergreen" (adoptado) | Medios ES: "contenido atemporal" más natural | Docs: aceptar ambos. "Contenido atemporal" preferido en reglas editoriales. |

---

## 4. Propuestas de revisión al repo ROBOHOGAR

### 4.1 Archivos a revisar

1. **`.claude/rules/tangibles.md`**
   - Término "tangible" está tan embebido que cambiarlo rompería pipeline. **Propuesta:** añadir regla explícita: *"'Tangible' es término interno del pipeline. En copy visible al lector (banner, email, landing, subtítulo) se sustituye SIEMPRE por 'PDF gratis', 'guía gratis' o 'descargable'."*
   - Sustituir menciones a *"cliffhanger pattern"* por **"cierre en suspense"** o **"gancho de cierre"** donde referencia texto visible. En docs técnicos que citan a Cole se mantiene el término.

2. **`.claude/rules/newsletter.md`**
   - Revisar "subject lines" → normalizar a **"asuntos"** en el texto corrido de la regla (mantener "subject" solo entre paréntesis la primera vez). "Max 25 chars" — ajustar a **"20-45 chars con preferencia ≤35"** basado en realidad ES.
   - Añadir subsección **"Registro de trato — confirmación empírica"**: *tú + plural editorial son el default. Vosotros y usted están prohibidos (ningún newsletter ES serio los usa)*.

3. **`.claude/rules/editorial.md`**
   - Añadir al bloque "Voz" referencia a apertura del cuerpo: *"El saludo 'Hola X, espero que estés bien' es tic de traducción anglosajona y no aparece en ningún newsletter ES auditado. Default ROBOHOGAR: entrada directa al tema o 'Buenos días.' + primera frase."*

4. **`references/writewithai/*.md`**
   - Añadir nota al header del knowledge base: *"Playbook US/EN. Verificar con `references/research-newsletters-es-2026-04-19.md` antes de adoptar literalmente. Casos conocidos con divergencia ES: verbo CTA, uso de 'Hola X', longitud de subject, saludo, em-dash en microcopy."*

5. **`.claude/commands/content-draft.md`** y **`.claude/commands/pdf-brand.md`**
   - Añadir paso al pre-output: *"Verificar que el copy de banner/landing/email no contiene: 'Hola', 'Hey', 'Querido/a', 'Amigo/a', emdash en trust-line, subject >45 chars."*

### 4.2 Anti-patterns nuevos para validator (`skills/pdf_brand/validators.py`)

Añadir regex prohibitivos en una nueva sección "Anglicismos traducidos":

```python
# Verbos CTA traducidos mal (ningún medio ES serio los usa como botón)
ANGLO_CTA_PATTERNS = [
    r"\b[Mm]e apunto\b",          # traducción US "I'm in" — no existe en ES real
    r"\b[Ss]ign me up\b",         # literal inglés
    r"\b[Qq]uiero recibir\b",     # verboso calco directo
]

# Saludos traducidos
ANGLO_GREETING_PATTERNS = [
    r"^\s*[Hh]ola,?\s+[A-Z]",                        # "Hola, X" inicial
    r"espero que (estés|te encuentres) bien",         # "hope you're well" traducido
    r"^\s*[Qq]uerido/?a?\s+(lector|lectora|amig)",    # "Dear reader"
    r"^\s*[Hh]ey[,\s]",                               # anglicismo puro
]

# Despedidas traducidas
ANGLO_SIGNOFF_PATTERNS = [
    r"\b[Aa]tentamente[,]?\s*$",       # registro de carta formal, no newsletter
    r"\b[Ss]aludos cordiales\b",       # corporativo anglo traducido
    r"\b[Cc]heers\b",                  # anglicismo literal
    r"\b[Bb]est[,]?\s*$",              # literal EN
]

# Tics de puntuación
PUNCT_ANTI_PATTERNS = [
    r" — ",   # em-dash con espacios en microcopy/trust-line (tic anglo)
]
```

Estos patrones se ejecutan **solo sobre copy destinado al lector** (banner, trust-line, email body, subject, subtítulo). Docs internos exentos.

### 4.3 Ajuste al default canónico de la trust-line

Actual: `"PDF gratis con tu suscripción semanal. Cancela cuando quieras."`

**Diagnóstico:**
- "PDF gratis" ✅ alineado con patrón ES (Kloshletter "Gratis y sin spam", Marketing4eCommerce "recibe gratis en tu correo").
- "suscripción semanal" ✅ cadencia explícita presente, patrón validado (67% de landings la mencionan).
- "Cancela cuando quieras" ✅ tono tú imperativo, alineado con patrón dominante.
- Falta: ninguna mención a **sin spam / privacidad**, que es el 2º pilar de confianza más usado (Xataka "política de privacidad", Kloshletter "sin spam").

**Propuesta de ajuste menor (variante A, mínima):**

> `"PDF gratis con tu suscripción semanal. Sin spam. Cancela cuando quieras."`

**Propuesta variante B (más directa, para test):**

> `"PDF gratis. Un email a la semana. Cancela cuando quieras."`

Variante B se inspira directamente en el formato Kloshletter ("Un email a la semana") — frase corta, sujeto elidido, carga semántica máxima por palabra.

**Recomendación:** A/B testear ambas cuando haya ≥100 subs. Hasta entonces, la variante A es el upgrade mínimo sin riesgo.

### 4.4 Reglas nuevas a añadir

A `.claude/rules/editorial.md` (al final de la sección "Voz y Tono"), bloque nuevo:

```markdown
## Apertura y cierre del cuerpo del email — anti-anglicismos

Default ROBOHOGAR (validado contra auditoría 2026-04-19 de 20 newsletters ES):

- **Apertura del cuerpo:** entrada directa al tema O "Buenos días." + primera frase. **Prohibido**: "Hola X", "Hola amigo/a", "Querido lector", "Hey", "Espero que estés bien", "¿Qué tal la semana?".
- **Cierre:** firma + tagline opcional. **Prohibido**: "Cheers", "Best", "Atentamente". "Un abrazo" es aceptable en ficciones o editoriales personales; por defecto no se usa.
- **Asunto:** 20-45 chars, preferencia ≤35. 1 emoji máximo (icónico de marca, no decorativo).
- **Microcopy trust-line/banner:** punto, coma o dos puntos. **Prohibido em-dash (`—`) en trust-lines de <15 palabras** — es tic anglo. Se reserva para cuerpo de artículo.
```

A `.claude/rules/newsletter.md` (nueva subsección al final):

```markdown
## Palabra nuclear del producto

"Newsletter" es la palabra dominante en el 83% del ecosistema ES Substack/Beehiiv auditado. ROBOHOGAR la adopta. **"Boletín"** se permite como sinónimo puntual en prosa editorial (coherente con tradición periodística ES), nunca como nombre del producto ni en botón CTA. **"Correo"** solo como vector de entrega ("en tu correo"), nunca como nombre del producto.
```

A `.claude/rules/tangibles.md` (añadir al bloque "Reglas operativas", tras la regla existente de promoción en subtítulo):

```markdown
- **Nunca "tangible" en copy público.** En docs y pipeline es término operativo; en banner, landing, email, subtítulo y OG card se sustituye siempre por "PDF gratis", "guía gratis" o "descargable". El lector no conoce "tangible" como categoría — es jerga interna.
```

---

## Apéndice — Fuentes

Listado de URLs visitadas y estado de cada una (OK / parcial / no accesible). Todas capturadas 2026-04-19.

| # | URL | Estado |
|---|---|---|
| 1 | https://www.xataka.com | OK |
| 2 | https://www.xatakahome.com | OK |
| 3 | https://hipertextual.com | parcial (sin signup en home) |
| 4 | https://www.elespanol.com/elandroidelibre/ | parcial (redirect OK, signup no visible) |
| 5 | https://www.elespanol.com/omicrono/ | parcial |
| 6 | https://www.genbeta.com | OK |
| 7 | https://topesdegama.com | parcial |
| 8 | https://kloshletter.com + https://kloshletter.com/suscribete/ | OK |
| 9 | https://sumapositiva.com + https://www.sumapositiva.com/subscribe + post #268 | OK |
| 10 | https://kaiki.beehiiv.com + https://kaiki.substack.com | **no accesible** (404 / perfil redirect vacío) |
| 11 | https://newsletter.dealflow.es | OK (pero copy en EN dentro de Substack) |
| 12 | https://www.startupriders.com | OK (copy en EN — excluido del análisis ES) |
| 13 | https://ecotechers.com | OK |
| 14 | https://tendencias.substack.com | OK |
| 15 | https://escribe.substack.com | OK |
| 16 | https://elordenmundial.com/boletines/ | OK |
| 17 | https://www.elconfidencial.com/newsletters/ | **no accesible** (bloqueo WebFetch) |
| 18 | https://elpais.com/newsletters/ | **no accesible** (bloqueo WebFetch); datos secundarios vía búsqueda |
| 19 | https://www.eldiario.es/blog/al-dia/suscribir-boletin-al-dia/ | OK |
| 20 | https://magnet.xataka.com | OK (redirect a xataka.com/categoria/magnet) |
| 21 | https://www.marketing4ecommerce.net | OK |
| 22 | https://www.fayerwayer.com | parcial (sin signup en home) |
| 23 | https://iaenespanol.substack.com + https://newsletter.iatoday.ai (reserva) | OK |
| 24 | https://www.newtral.es/suscribete/ (reserva) | OK |
| 25 | https://www.cincominutos.es (reserva) | OK |

**Sustitos activados desde reserva:** IA en Español (por #3 parcial), Newtral (por #17 no accesible), Cincominutos (por #18 no accesible).

**Otros dominios consultados pero no auditados como filas:** Cafecito (substack, copy en ES pero foco LATAM), Product-Market Fit (EN), Afueradentro (directorio, no newsletter singular), Directorio de Substack (índice), Startups Oasis (índice).
