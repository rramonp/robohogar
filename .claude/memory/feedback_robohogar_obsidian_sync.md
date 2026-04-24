---
name: Sync guía ROBOHOGAR a Obsidian vault tras cada edit
description: Después de cada edit a docs/guia-implementacion.md (y docs ROBOHOGAR que Rafael consulte en Obsidian), copiar inmediatamente al vault. Si no, Rafael ve contenido stale y tiene que pedir el sync manualmente.
type: feedback
---

Regla dura: tras cualquier `Edit` a `docs/guia-implementacion.md` en el repo robohogar, **sincronizar inmediatamente al vault Obsidian** donde Rafael lee y trabaja.

**Path de destino:**
```
$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md
```

En Windows bash:
```bash
cp "c:/Users/bakal/robohogar/docs/guia-implementacion.md" "c:/Users/bakal/OneDrive - HBX Group/Desktop/DEMAND/Obsidian/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md"
```

**Why:** Rafael lee y trabaja la guía desde el vault Obsidian (sync entre desktop, laptop y móvil vía Syncthing), no desde el repo. Si solo se actualiza el repo, ve contenido desactualizado y tiene que pedir el sync manualmente — fricción evitable.

**How to apply:** tras cada edit a `guia-implementacion.md` ejecutar el `cp` al vault. **Aplica también a cualquier otro doc ROBOHOGAR que Rafael consulte desde Obsidian** (calendario editorial, registro-articulos, registro-ficciones, docs/plan-*.md, etc.): si el agente los edita en el repo, verificar si existe copia en el vault y sincronizar.

**Excepción — archivos con progreso activo del usuario (p.ej. checkboxes que Rafael marca).** Para esos, NO hacer `cp` completo (sobrescribiría el progreso). Hacer edits quirúrgicos en el vault. La guía de implementación en ROBOHOGAR no tiene checkbox progress editable por Rafael, así que default = `cp` completo. Si un futuro doc sí lo tuviera, marcarlo explícitamente y cambiar estrategia.

**Incidentes de origen:** Rafael verificó 2026-04 que edits al repo sin sync al vault dejaban la guía desactualizada cuando él trabajaba desde Obsidian (laptop + móvil).
