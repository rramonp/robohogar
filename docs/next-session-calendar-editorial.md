# Próxima sesión: Calendario Editorial + Newsletter Semanal

> Contexto: ROBOHOGAR tiene 2 artículos publicados (review + editorial), 0 suscriptores,
> crecimiento orgánico puro (SEO + Beehiiv). Falta el tercer tipo de contenido: newsletter
> semanal por email. También falta un sistema de calendario que gestione todo.

## Lo que hay que hacer

### 1. Definir cadencia semanal

Decidir con Rafael:
- ¿Qué día se publica artículo web? (¿lunes? ¿miércoles?)
- ¿Qué día se envía newsletter por email? (martes 9:00 CET según reglas actuales)
- ¿El newsletter incluye el artículo de esa semana o es contenido independiente?
- ¿Semanas alternas (semana A = artículo, semana B = newsletter) o ambos cada semana?
- Realista con 3-5 hrs/semana de dedicación
- **Decisión tomada:** Artículos → `Email and web` (inbox + SEO). Newsletter → `Email only` (solo suscriptores, no aparece en landing)

### 2. Crear template Newsletter Issue

Es el tercer template que falta. Proceso:
- Diseñar la estructura del newsletter en Beehiiv (Rafael en Design Mode)
- Basarse en la estructura de plan-v2.md (5 secciones: La Noticia, En Prueba, El Futuro, Dato Curioso, Enlace de la Semana)
- Rafael publica el primer newsletter, exporta el HTML
- Guardar como `content/templates/newsletter-issue-beehiiv-export.html`
- Documentar estructura en `content/templates/estructura-templates.md`

### 3. Montar registro de newsletters

Crear un archivo que catalogue cada envío:

```markdown
# Registro de Newsletters — ROBOHOGAR

| # | Fecha | Subject | Temas cubiertos | Open Rate | CTR | Notas |
|---|-------|---------|----------------|-----------|-----|-------|
| 001 | 2026-04-XX | ... | ... | % | % | Primer issue |
```

Esto permite:
- No repetir temas
- Ver qué subjects funcionan mejor
- Trackear métricas por issue
- Planificar temas futuros

### 4. Calendario editorial mensual

Crear un sistema (puede ser un .md o el template de Obsidian) que muestre:
- Semana 1: qué artículo + qué newsletter
- Semana 2: qué artículo + qué newsletter
- etc.
- Temas planificados para las próximas 4 semanas
- Temas usados (para no repetir)

### 5. Actualizar skills

- `/content-draft` — añadir tipo "Newsletter" con su template HTML
- `/research-digest` — que sugiera temas para newsletter además de artículos
- `/post-publish` — que funcione también para newsletters enviados por email
- `/social-content` — que genere posts promocionando el newsletter, no solo artículos

### 6. Preparar Newsletter #1

- Lanzar `/research-digest` para tener material fresco
- Elegir 3-5 noticias de la semana
- Redactar con la estructura de 5 secciones
- Subject line <25 chars, curiosity gap
- Enviar como "Email and web" (no solo web)
- Recordar: límite 800KB en imágenes para email

## Estado actual para referencia

- **Artículos publicados:** 2 (review comparativa + editorial opinión)
- **Templates HTML:** 2 (review + editorial). Falta newsletter.
- **Frecuencia actual:** semanal (prometido en la landing y tagline)
- **Suscriptores:** 0 (crecimiento orgánico, sin distribución personal)
- **Buffer:** configurado con LinkedIn + Instagram
- **Skills activos:** research-digest, content-draft, nano-banana, social-content, post-publish, obsidian-robohogar
