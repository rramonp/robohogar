---
name: ROBOHOGAR ElevenLabs — contador local de saldo + endpoint /v1/usage/character-stats
description: La API key ROBOHOGAR no tiene permiso user_read (bloquea /v1/user/subscription HTTP 401), pero SÍ funciona /v1/usage/character-stats. utilities/elevenlabs_balance.py es el contador local que sincroniza desde ese endpoint y bloquea TTS pre-flight si saldo insuficiente.
type: reference
originSessionId: 694cdfe5-2c47-4440-8302-3ac733e34a02
---
**Endpoint que SÍ funciona con la API key actual de ROBOHOGAR:**

```
GET https://api.elevenlabs.io/v1/usage/character-stats
  ?start_unix=<ms>&end_unix=<ms>&aggregation_interval=day
  → {"time": [...], "usage": {"All": [créditos_por_día...]}}
```

**Endpoints bloqueados** (devuelven HTTP 401 `missing_permissions: user_read`):
- `/v1/user/subscription` (saldo + plan info)
- `/v1/user` (perfil)

**Plan de Rafael (verificado 2026-04-26 vía dashboard):**
- Plan: **Creator** ($22/mo).
- Límite: **121.880 créditos/mes** (Creator base = 100k, los 21.880 extras vienen de algún rollover/upgrade — usar siempre el número del dashboard, no asumir 100k).
- Reset day: **25** (renueva mensualmente el 25).
- Ratio observado chars→créditos: **0,79** (52,7K créditos / 66,7K chars en Multilingual v2 last week 2026-04-19→26).

**Contador local — utilities/elevenlabs_balance.py:**

```bash
# Sincroniza saldo desde la API (idempotente, lectura pura — no consume créditos)
python utilities/elevenlabs_balance.py sync --tier Creator --limit 121880 --reset-day 25 --ratio 0.79

# Pre-check antes de TTS
python utilities/elevenlabs_balance.py check --chars <N>

# Snapshot manual si la API falla
python utilities/elevenlabs_balance.py set --credits N --tier Creator --limit 121880 --reset-day 25 --ratio 0.79

# Estado actual
python utilities/elevenlabs_balance.py status
```

**Estado persistido en** `utilities/_state/elevenlabs-balance.json` (gitignored — varía con cada generación TTS, no debe viajar al repo público).

**Hook integrado en** `utilities/generate_audio.py`:
- Pre-flight `pre_check(total_chars)` antes del primer chunk TTS — aborta si saldo insuficiente.
- Post-flight `record_usage(slug, chars)` solo si TTS+concat+upload pasaron — no contabiliza fallos.

**Override `ROBOHOGAR_ELEVENLABS_FORCE=1`** salta el bloqueo (útil si pagaste overage y el contador no lo refleja todavía).

**Reset mensual perezoso:** cada lectura comprueba si el día actual ≥ reset_day y la última actualización es del periodo anterior → reinyecta `monthly_credit_limit` automáticamente. No requiere cron job.

**Skill `/audiobook-generate` § Pre-requisitos** documenta el flujo. Los `sync` consumen 1 request HTTP de lectura (no consume créditos TTS).

Memoria origen: incidente 2026-04-25 con `la-objecion` (regeneración falló en chunk 1 con HTTP 401 quota_exceeded a mitad del pipeline) + decisión 2026-04-26 de Rafael de construir contador local en lugar de bloquear por la limitación de permisos de la API key.
