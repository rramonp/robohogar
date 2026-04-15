# Post-Publish — Limpieza y distribución tras publicar un artículo

Ejecuta todas las tareas post-publicación de un artículo en ROBOHOGAR.
Se invoca después de que Rafael confirme que el artículo está publicado en Beehiiv.

## When to activate

- "ya está publicado", "acabo de publicar", "post-publish"
- "limpieza post publicación", "tareas post artículo"
- Después de que Rafael comparta la URL del artículo publicado

## Input necesario

Preguntar a Rafael si no lo ha dado:
1. **URL del artículo publicado** (ej: `https://robohogar.com/p/slug`)
2. **Hero image elegida** (ej: v10) — para saber cuáles borrar
3. **Slug del artículo** — se deduce de la URL si no lo da

## Workflow (ejecutar en orden)

### 1. Mover borrador a published

```bash
cp content/articulos/<slug>/borrador.html content/published/YYYY-MM-DD-<slug>.html
```

### 2. Limpiar variantes de hero no usadas

Borrar todas las variantes de hero excepto la elegida:
```bash
# Mantener solo hero-<slug>-v<elegida>.png y .webp
# Borrar el resto de hero-<slug>-v*.png y .webp
```
Las variantes quedan en el historial de git si se necesitan.

### 3. Actualizar guia-implementacion.md

Marcar todos los checkboxes del artículo como completados y añadir la URL publicada:
```
- [x] Publicado → <URL>
```

### 4. Verificar fuentes en fuentes-por-categoria.md

Leer el artículo publicado y verificar que todas las fuentes nuevas usadas están catalogadas en `references/fuentes-por-categoria.md`. Si falta alguna, añadirla con URL, tipo y notas.

### 5. Actualizar asset-catalog.md

Registrar el hero image elegido en la sección de assets generados del catálogo:
```
| hero-<slug>-v<N> | <fecha> | <prompt resumido> | <modelo> |
```

### 6. Sugerir actualización de Welcome Email

Evaluar si el artículo nuevo debería reemplazar o complementar el link del Welcome Email actual. Mostrar a Rafael:
- El link actual del Welcome Email
- El link del artículo nuevo
- Recomendación: ¿cambiar el link? ¿añadir como segundo link?

Rafael decide. NO cambiar automáticamente.

### 7. Generar contenido social

Invocar `/social-content` con el artículo publicado para generar posts para:
- LinkedIn (1 post)
- X/Twitter (3 posts)
- Instagram (caption para Reel)
- WhatsApp Channel (mensaje)

### 8. Sincronizar con Obsidian

Ejecutar sync de la guía de implementación al vault:
```bash
cp docs/guia-implementacion.md "$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md"
```

Si `/obsidian-robohogar sync-published` está disponible, usarlo también.

### 9. Commit y push

Commit con todos los cambios de esta sesión post-publicación:
```
Post-publish: <título artículo>

Moved to published, cleaned <N> unused variants, updated sources
and asset catalog, synced to Obsidian.
```

Push automático.

### 10. Reportar resumen

Mostrar a Rafael un resumen de todo lo hecho:
```
## Post-publicación completada

- ✅ Borrador → content/published/YYYY-MM-DD-slug.html
- ✅ Limpiadas N variantes no usadas
- ✅ Fuentes verificadas en fuentes-por-categoria.md
- ✅ Asset catalog actualizado
- ✅ Welcome Email: [recomendación]
- ✅ Social content generado (revisar antes de programar)
- ✅ Obsidian sincronizado
- ✅ Commit + push
```

## Rules

- NUNCA cambiar el Welcome Email sin confirmación de Rafael
- NUNCA publicar social content automáticamente — solo generar para revisión
- Si algún paso falla, continuar con los demás y reportar el fallo al final
- El artículo en `content/articulos/<slug>/` NO se borra — se mantiene como carpeta de trabajo con assets
