---
name: ROBOHOGAR guide always synced to Obsidian
description: When updating guia-implementacion.md in robohogar repo, ALWAYS copy to Obsidian vault — Rafael works from Obsidian
type: feedback
originSessionId: ef4f8de7-43ba-4185-acab-b19f2ce0cf8a
---
When updating `docs/guia-implementacion.md` in the robohogar repo, ALWAYS sync to Obsidian vault immediately.

**Why:** Rafael reads and works from the Obsidian vault, not from the repo. If the repo copy is updated but Obsidian isn't, Rafael sees stale content and has to ask for the sync manually.

**How to apply:** After any edit to `guia-implementacion.md`, run:
```
cp "c:/Users/cri-c/robohogar/docs/guia-implementacion.md" "$HBX_VAULT/RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter/Guia Implementacion.md"
```
Same applies to any ROBOHOGAR doc that Rafael references in Obsidian.
