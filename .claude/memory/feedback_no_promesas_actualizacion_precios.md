---
name: No prometer actualización futura de precios en artículos
description: Cero promesas de revisión semestral, "verificados en abril 2026", "pueden cambiar en revisiones futuras" — Rafael no va a actualizar
type: feedback
---

Regla dura establecida por Rafael 2026-04-29.

**Prohibido en TODO copy publicable** (cuerpo de artículo, fig caption, disclaimer afiliados, footer de tangible PDF, banner, copy de Beehiiv, social):

- *"Precios actualizados a [mes] [año]"* / *"Precio actualizado a abril 2026"*
- *"Precios consultados a [fecha]"* / *"Precios verificados el [fecha]"* / *"verificados en abril 2026"*
- *"Datos y precios verificados [fecha] — pueden cambiar"* / *"pueden cambiar en revisiones futuras"*
- *"Revisión semestral prevista para [mes] [año]"* / *"Revisión estacional prevista para febrero-marzo 2027"*
- *"Próxima revisión de precios: [fecha]"*
- Cualquier formulación que implique al lector que ROBOHOGAR va a volver a este artículo a poner precios nuevos.

**Why:** Rafael es un único editor con 3-5 h/semana y un backlog evergreen creciente. No va a poder volver atrás cada 6 meses a revisar precios artículo por artículo. Cualquier promesa de actualización futura es una mentira programada al lector. Los evergreens se quedan con los precios del momento de publicación; si en 12 meses el precio real es más bajo, *es lo que hay* — no se promete actualizar lo que no se va a actualizar. Hermana de [`feedback_tangible_no_promises_no_byline.md`](feedback_tangible_no_promises_no_byline.md) (no roadmap futuro en tangibles) y [`feedback_robohogar_no_fake_testing_claims.md`](feedback_robohogar_no_fake_testing_claims.md) (no claims de acción no realizada).

**How to apply:**

- Tabla comparativa de precios — eliminar líneas tipo *"Precios actualizados a abril 2026"* del intro de la tabla. Sustituir por *"Lo importante, en una fila."* sin fecha.
- Fig caption de tabla highlighted — eliminar *"Precios verificados en Amazon.es, MediaMarkt e idealo.es el 18-abr-2026"*. La fecha de verificación es ruido editorial; el dato vive sin ella.
- Disclaimer afiliados al final del artículo — eliminar la coletilla *"Datos y precios verificados [fecha] — revisión semestral prevista para [fecha]"*. El disclaimer cierra tras *"Todas las marcas pertenecen a sus respectivos propietarios."*.
- PDF tangible — el footer del PDF no lleva *"pueden cambiar en revisiones futuras"*. Cierra tras *"ninguno en este PDF."*.
- Body del artículo — frase tipo *"Precios actuales verificados en abril 2026:"* antes de una lista de precios → *"Precios en España:"* o eliminar la línea entera si la lista tiene contexto suficiente.

**Excepción permitida (factual, sin promesa):** mencionar *"según la ficha oficial de Samsung"*, *"según Amazon.es a la fecha de publicación"* dentro de una frase concreta sobre un dato concreto — NO como coletilla genérica de cierre. La diferencia: la versión permitida ancla el dato en su fuente y no implica que volveremos a actualizarlo; la versión prohibida promete revisión.

**Verificación pre-output (greps obligatorios sobre cualquier borrador, fig caption, disclaimer o PDF tangible antes de entregar):**

```bash
# (a) Promesas explícitas de revisión — debe ser 0
grep -niE 'revisión\s+(semestral|estacional|de\s+precios)\s+prevista|próxima\s+revisión.*precio|pueden\s+cambiar\s+en\s+revisiones?\s+futuras?|verifica\s+precios\s+reales' <archivo>

# (b) Coletillas de fecha de verificación — debe ser 0
grep -niE 'precios?\s+(actualizad|consultad|verificad)[oa]s?\s+(a|en|el)\s+([0-9]{1,2}-?[a-z]{3}|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre|enero|febrero|marzo)' <archivo>

# (c) "Datos y precios verificados [fecha]" en disclaimers — debe ser 0
grep -niE 'datos\s+y\s+precios\s+verificad' <archivo>
```

Si alguno devuelve match en cuerpo / disclaimer / fig caption / PDF, reescribir antes de entregar.

**Aplicación retroactiva (hecha 2026-04-29):** limpiados 8 borradores + 6 published + 1 master template + 1 PDF tangible v3. Lo que queda como histórico no migrado: frontmatter `evergreen_note` (HTML comments invisibles al lector) en samsung + humanoides, PASOS.md de varios artículos, social/.md frontmatter, registro-articulos.md columna evergreen con paréntesis "(revisar precios cada 6m)", PDFs hoja-compra v1 y v2 archivados. Esos viven en internal-only y no se ven al lector — pueden esperar a un sweep posterior.

**Skills herederos:** `/content-draft` paso 8.x (greps a-c en pre-output). `/post-publish` triaje: match evidente → auto-fix en borrador + published. `/pdf-brand` validators bloquean los 3 patrones a-c. `/social-content` no propaga estas coletillas (verificado: los snippets pre-publicados no las contienen).
