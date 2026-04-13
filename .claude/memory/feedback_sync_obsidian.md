---
name: Sync guía a Obsidian vault
description: Siempre copiar guia-implementacion.md del repo al vault de Obsidian después de cada cambio
type: feedback
---

Cada vez que se actualice `docs/guia-implementacion.md` en el repo, copiar también a Obsidian:
`$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md`

**Why:** Rafael trabaja con la guía desde Obsidian, no desde el repo. Si solo se actualiza el repo, no ve los cambios.
**How to apply:** Después de cada `Edit` a guia-implementacion.md, ejecutar `cp` del repo al vault.
