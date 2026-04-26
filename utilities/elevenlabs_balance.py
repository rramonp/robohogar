"""
elevenlabs_balance.py · Contador local de saldo ElevenLabs

Por qué existe
==============
La API key de ROBOHOGAR no tiene permiso `user_read`, así que el endpoint
oficial /v1/user/subscription devuelve HTTP 401. Sin esa lectura programática
no podemos saber por API si quedan créditos antes de lanzar TTS — y si la
API se queda sin cuota a mitad de los chunks, los créditos parciales NO son
recuperables (incidente origen 2026-04-25 con `la-objecion`).

Este módulo es la proyección local del saldo: Rafael toma una foto puntual
del dashboard de ElevenLabs (https://elevenlabs.io/app/usage), la mete con
`set` y a partir de ahí cada generación TTS llama a `record_usage` para
decrementar el saldo. La fuente de verdad sigue siendo el dashboard; este
contador solo evita lanzar TTS sin margen.

Estado en utilities/_state/elevenlabs-balance.json (gitignored — varía con
cada generación, no debe viajar al repo público).

Uso CLI
=======

  python utilities/elevenlabs_balance.py status
  python utilities/elevenlabs_balance.py set --credits 47300 --tier Creator \\
      --limit 100000 --reset-day 1 --ratio 0.79
  python utilities/elevenlabs_balance.py record --slug la-objecion --chars 19200
  python utilities/elevenlabs_balance.py history [--n 10]
  python utilities/elevenlabs_balance.py check --chars 22000

Uso programático
================

  from utilities.elevenlabs_balance import get_remaining, record_usage, pre_check

  # Antes de lanzar TTS
  ok, msg = pre_check(estimated_chars=22000)
  if not ok: raise SystemExit(msg)

  # Tras éxito de TTS
  record_usage(slug='el-operador-nocturno', chars=19713)

Convenciones
============
- Trackeamos tanto chars (lo que pasamos a la API) como créditos (lo que
  cobra ElevenLabs). El factor `credit_per_char_ratio` lo deduce Rafael del
  dashboard last-week (52.7K créditos / 66.7K chars ≈ 0.79 con Multilingual v2).
- El reset mensual se aplica perezosamente: cada lectura comprueba si el día
  actual ≥ `monthly_reset_day` y la última actualización fue antes del último
  reset → reinyecta `monthly_credit_limit` al saldo.
- Si Rafael paga overage o cambia de plan, simplemente vuelve a llamar `set`
  y el contador se reinicializa con el nuevo snapshot. No hay merge complejo.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Reconfigura stdout a UTF-8 en Windows. cp1252 (default cmd.exe ES) no
# encodea ═ ✅ ⚠️ ❌ y rompe el CLI con UnicodeEncodeError. bash MINGW y
# PowerShell 7+ ya son UTF-8 → el reconfigure es no-op en esos casos.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import requests  # solo lo necesita el modo `sync` que llama a /v1/usage
except ImportError:
    requests = None  # el resto del módulo funciona sin requests

# ─────────────────────────────────────────────────────────────────────────
# Ubicación canónica del estado.
# ─────────────────────────────────────────────────────────────────────────

# Repo root = parent de utilities/.
REPO_ROOT = Path(__file__).resolve().parent.parent

# Archivo de estado — gitignored vía utilities/_state/*.json.
STATE_FILE = REPO_ROOT / "utilities" / "_state" / "elevenlabs-balance.json"

# Versión del schema, por si en el futuro cambia la estructura.
SCHEMA_VERSION = 1

# Valores por defecto al inicializar el archivo. Plan tier "unknown" obliga
# a Rafael a configurar al menos una vez antes de que el contador sea útil.
DEFAULT_STATE: dict[str, Any] = {
    "schema_version": SCHEMA_VERSION,
    "plan_tier": "unknown",
    "monthly_credit_limit": 0,
    "monthly_reset_day": 1,           # día del mes en que ElevenLabs reinicia plan
    "credit_per_char_ratio": 0.79,    # ratio observado last-week en dashboard 2026-04-26
    "remaining_credits": 0,
    "remaining_credits_at_iso": None,
    "remaining_credits_source": None,  # 'dashboard_manual' | 'auto_record' | 'reset'
    "history": [],                     # lista de eventos {iso, slug, chars, credits, after_credits}
}

# Margen de seguridad pre-check: si tras la generación quedaría <5% del límite
# mensual, alertar pero no abortar (puede ser legítimo apurar a fin de mes).
SAFETY_MARGIN_PCT = 5

# Límite duro: si tras la generación quedarían créditos negativos (saldo
# insuficiente sin overage configurado), abortar sin --force.
ABORT_ON_NEGATIVE = True


# ─────────────────────────────────────────────────────────────────────────
# Lectura y escritura del estado.
# ─────────────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    """ISO-8601 UTC con segundos. Usado en historial y timestamps."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_state() -> dict[str, Any]:
    """
    Carga el archivo JSON de estado o devuelve el default si no existe.

    NO aplica reset perezoso aquí — eso pasa en `get_remaining` para que
    `load_state` siga siendo una operación pura de lectura.
    """
    if not STATE_FILE.exists():
        return dict(DEFAULT_STATE)
    try:
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        # Estado corrupto — abortamos en lugar de sobrescribir silenciosamente.
        raise RuntimeError(f"Estado ElevenLabs corrupto en {STATE_FILE}: {exc}") from exc
    # Migración futura: si SCHEMA_VERSION sube, hacer upgrade aquí.
    return data


def save_state(state: dict[str, Any]) -> None:
    """Escribe el estado de forma atómica (temp + rename)."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE_FILE)


# ─────────────────────────────────────────────────────────────────────────
# Reset mensual perezoso.
# ─────────────────────────────────────────────────────────────────────────

def _maybe_apply_monthly_reset(state: dict[str, Any]) -> dict[str, Any]:
    """
    Aplica el reset mensual si procede.

    Lógica: si el día actual >= reset_day Y el último timestamp del estado
    cae en un mes/año anterior al reset más reciente que ya debería haber
    ocurrido → re-inyecta monthly_credit_limit como remaining_credits y
    deja un evento 'reset' en el historial.

    Si no hay timestamp previo (estado fresco) o monthly_credit_limit = 0
    (Rafael aún no lo configuró), no hace nada — devuelve state sin tocar.
    """
    limit = int(state.get("monthly_credit_limit", 0))
    reset_day = int(state.get("monthly_reset_day", 1))
    last_iso = state.get("remaining_credits_at_iso")

    if limit <= 0 or not last_iso:
        return state

    try:
        last_dt = datetime.fromisoformat(last_iso.replace("Z", "+00:00"))
    except ValueError:
        return state

    now = datetime.now(timezone.utc)

    # Calcular cuál fue el último reset que YA debería haber ocurrido.
    # Si hoy día >= reset_day → el último reset fue este mes en reset_day.
    # Si hoy día < reset_day → el último reset fue el mes pasado en reset_day.
    if now.day >= reset_day:
        last_reset_year, last_reset_month = now.year, now.month
    else:
        if now.month == 1:
            last_reset_year, last_reset_month = now.year - 1, 12
        else:
            last_reset_year, last_reset_month = now.year, now.month - 1

    last_reset_dt = datetime(
        last_reset_year, last_reset_month, reset_day, 0, 0, 0,
        tzinfo=timezone.utc,
    )

    if last_dt < last_reset_dt:
        # Hubo al menos un reset entre el último update y ahora — recargar saldo.
        state["remaining_credits"] = limit
        state["remaining_credits_at_iso"] = _now_iso()
        state["remaining_credits_source"] = "reset"
        state["history"].append({
            "iso": _now_iso(),
            "event": "monthly_reset",
            "credits_after": limit,
            "note": f"Reset automático por cruce de día {reset_day}.",
        })
        save_state(state)

    return state


# ─────────────────────────────────────────────────────────────────────────
# API pública del módulo.
# ─────────────────────────────────────────────────────────────────────────

def get_remaining() -> dict[str, Any]:
    """
    Devuelve el snapshot actual del saldo, aplicando reset mensual si toca.

    Output dict con campos: credits, credits_iso, source, plan_tier,
    monthly_limit, ratio, configured (bool), pct_of_monthly.
    """
    state = load_state()
    state = _maybe_apply_monthly_reset(state)
    limit = int(state.get("monthly_credit_limit", 0))
    credits = int(state.get("remaining_credits", 0))
    pct = (credits / limit * 100) if limit > 0 else None
    return {
        "credits": credits,
        "credits_iso": state.get("remaining_credits_at_iso"),
        "source": state.get("remaining_credits_source"),
        "plan_tier": state.get("plan_tier", "unknown"),
        "monthly_limit": limit,
        "ratio": float(state.get("credit_per_char_ratio", 0.79)),
        "configured": state.get("plan_tier", "unknown") != "unknown" and limit > 0,
        "pct_of_monthly": pct,
    }


# ─────────────────────────────────────────────────────────────────────────
# Sync con la API de ElevenLabs.
# ─────────────────────────────────────────────────────────────────────────

# Plan tiers conocidos de ElevenLabs (créditos/mes incluidos, abril 2026).
# Nota: el límite real puede variar si el usuario ha comprado packs extra,
# tiene upgrades retroactivos o rollover. Para casos así pasar `--limit N`
# explícitamente al `sync` o `set` — sobrescribe el default del tier.
KNOWN_TIER_LIMITS = {
    "starter": 30_000,
    "creator": 100_000,
    "pro": 500_000,
    "scale": 2_000_000,
    "business": 11_000_000,
}


def fetch_remote_usage(api_key: str, start_unix_ms: int, end_unix_ms: int) -> int:
    """
    Llama a /v1/usage/character-stats y devuelve la suma de créditos
    consumidos en [start, end].

    Este endpoint NO requiere permiso `user_read`, así que funciona con la
    API key estándar — a diferencia de /v1/user/subscription que está
    bloqueado para nuestra key actual (HTTP 401 missing_permissions).
    """
    if requests is None:
        raise RuntimeError("Falta `requests` (pip install requests).")
    url = "https://api.elevenlabs.io/v1/usage/character-stats"
    r = requests.get(
        url,
        headers={"xi-api-key": api_key},
        params={
            "start_unix": start_unix_ms,
            "end_unix": end_unix_ms,
            "aggregation_interval": "day",
        },
        timeout=10,
    )
    r.raise_for_status()
    data = r.json()
    # Estructura: {"time": [...], "usage": {"All": [...]}}.
    # "All" es la breakdown total; otros breakdowns (voice, model) requieren
    # `breakdown_type` distinto.
    series = data.get("usage", {}).get("All", [])
    return int(sum(series))


def _period_start_for(reset_day: int, now: datetime | None = None) -> datetime:
    """
    Calcula el inicio del periodo de facturación actual.

    Si hoy >= reset_day → inicio = este mes en reset_day.
    Si hoy < reset_day → inicio = mes pasado en reset_day.
    """
    now = now or datetime.now(timezone.utc)
    if now.day >= reset_day:
        year, month = now.year, now.month
    else:
        if now.month == 1:
            year, month = now.year - 1, 12
        else:
            year, month = now.year, now.month - 1
    return datetime(year, month, reset_day, 0, 0, 0, tzinfo=timezone.utc)


def sync_from_api(
    *,
    api_key: str,
    plan_tier: str,
    monthly_limit: int | None = None,
    reset_day: int = 1,
    ratio: float | None = None,
) -> dict[str, Any]:
    """
    Consulta /v1/usage/character-stats para el periodo de facturación actual
    (desde reset_day del mes actual o anterior, según hoy), suma los créditos
    consumidos y computa saldo restante = monthly_limit - consumidos.

    Si `monthly_limit` es None, usa el default del tier de KNOWN_TIER_LIMITS.

    Persiste el snapshot en el estado y devuelve el dict final.
    """
    tier_key = plan_tier.lower()
    if monthly_limit is None:
        monthly_limit = KNOWN_TIER_LIMITS.get(tier_key)
        if monthly_limit is None:
            raise ValueError(
                f"Plan tier '{plan_tier}' desconocido. Pasa `--limit N` explícito "
                f"o usa uno de: {sorted(KNOWN_TIER_LIMITS)}."
            )

    period_start = _period_start_for(reset_day)
    now = datetime.now(timezone.utc)
    start_ms = int(period_start.timestamp() * 1000)
    end_ms = int(now.timestamp() * 1000)

    consumed = fetch_remote_usage(api_key, start_ms, end_ms)
    remaining = monthly_limit - consumed

    state = load_state()
    state["plan_tier"] = plan_tier
    state["monthly_credit_limit"] = int(monthly_limit)
    state["monthly_reset_day"] = int(reset_day)
    state["remaining_credits"] = int(remaining)
    state["remaining_credits_at_iso"] = _now_iso()
    state["remaining_credits_source"] = "api_sync"
    if ratio is not None:
        state["credit_per_char_ratio"] = float(ratio)
    state["history"].append({
        "iso": _now_iso(),
        "event": "api_sync",
        "credits_after": int(remaining),
        "consumed_this_period": int(consumed),
        "period_start_iso": period_start.isoformat(),
        "monthly_limit": int(monthly_limit),
        "note": f"Sync con /v1/usage/character-stats. Consumidos {consumed:,} desde {period_start.date()}.",
    })
    save_state(state)
    return {
        "consumed": int(consumed),
        "remaining": int(remaining),
        "limit": int(monthly_limit),
        "period_start": period_start,
        "now": now,
    }


def set_balance(
    *,
    credits: int,
    plan_tier: str | None = None,
    monthly_limit: int | None = None,
    reset_day: int | None = None,
    ratio: float | None = None,
) -> dict[str, Any]:
    """
    Inicializa o actualiza el balance desde una lectura manual del dashboard.

    Pasar None en un campo deja el valor previo intacto (excepto credits, que
    es obligatorio). Útil para corrección puntual sin re-meter todos los datos.
    """
    state = load_state()
    state["remaining_credits"] = int(credits)
    state["remaining_credits_at_iso"] = _now_iso()
    state["remaining_credits_source"] = "dashboard_manual"
    if plan_tier is not None:
        state["plan_tier"] = plan_tier
    if monthly_limit is not None:
        state["monthly_credit_limit"] = int(monthly_limit)
    if reset_day is not None:
        if not (1 <= reset_day <= 28):
            raise ValueError("reset_day debe estar entre 1 y 28 (evita meses cortos)")
        state["monthly_reset_day"] = int(reset_day)
    if ratio is not None:
        state["credit_per_char_ratio"] = float(ratio)
    state["history"].append({
        "iso": _now_iso(),
        "event": "manual_set",
        "credits_after": state["remaining_credits"],
        "note": f"Snapshot manual del dashboard. Plan {state['plan_tier']}, "
                f"límite {state['monthly_credit_limit']}, reset día {state['monthly_reset_day']}.",
    })
    save_state(state)
    return state


def record_usage(*, slug: str, chars: int, credits: int | None = None) -> dict[str, Any]:
    """
    Registra una generación TTS y decrementa el saldo.

    Si `credits` es None se estima como `chars * ratio`. Si Rafael conoce el
    coste real (vía dashboard tras la generación), puede pasarlo explícito.

    Devuelve el evento añadido (para reporte inmediato).
    """
    state = load_state()
    ratio = float(state.get("credit_per_char_ratio", 0.79))
    estimated = int(round(chars * ratio)) if credits is None else int(credits)

    new_balance = int(state.get("remaining_credits", 0)) - estimated
    state["remaining_credits"] = new_balance
    state["remaining_credits_at_iso"] = _now_iso()
    state["remaining_credits_source"] = "auto_record"

    event = {
        "iso": _now_iso(),
        "event": "tts_generation",
        "slug": slug,
        "chars": int(chars),
        "credits_estimated": estimated,
        "credits_explicit": credits is not None,
        "credits_after": new_balance,
    }
    state["history"].append(event)
    save_state(state)
    return event


def pre_check(*, chars: int) -> tuple[bool, str]:
    """
    Verifica si hay margen para una generación de N chars.

    Returns (ok, message). Si ok=False, message explica el bloqueo.
    Si configured=False, ok=True con warning (sin info no podemos bloquear).
    """
    snap = get_remaining()
    if not snap["configured"]:
        return True, (
            "⚠️  Contador no configurado — sin info de saldo. Verifica "
            "manualmente en https://elevenlabs.io/app/usage o ejecuta "
            "`python utilities/elevenlabs_balance.py set --credits N --tier T "
            "--limit L --reset-day D` antes de generar."
        )
    estimated_credits = int(round(chars * snap["ratio"]))
    after = snap["credits"] - estimated_credits

    if ABORT_ON_NEGATIVE and after < 0:
        return False, (
            f"❌ Saldo insuficiente. Generar {chars:,} chars (~{estimated_credits:,} "
            f"créditos a ratio {snap['ratio']}) dejaría el saldo en {after:,}. "
            f"Saldo actual: {snap['credits']:,} créditos. "
            f"Resetea el {snap['credits_iso']} día {snap['plan_tier']}. "
            f"Opciones: (a) esperar al reset mensual, (b) pagar overage en "
            f"dashboard y luego `set --credits NUEVO_SALDO`, (c) `--force` "
            f"si vas a pagar overage tras la generación."
        )

    if snap["monthly_limit"] > 0:
        pct_after = after / snap["monthly_limit"] * 100
        if pct_after < SAFETY_MARGIN_PCT:
            return True, (
                f"⚠️  Margen estrecho. Tras generar {chars:,} chars (~{estimated_credits:,} "
                f"créditos) quedarían {after:,} ({pct_after:.1f}% del límite mensual "
                f"{snap['monthly_limit']:,}). OK para proceder, pero próxima generación "
                f"podría bloquearse hasta el reset."
            )

    return True, (
        f"✅ Saldo OK. {snap['credits']:,} créditos antes → {after:,} después "
        f"de generar {chars:,} chars (~{estimated_credits:,} créditos a ratio "
        f"{snap['ratio']}). Plan {snap['plan_tier']} · límite {snap['monthly_limit']:,} "
        f"· reset día {load_state().get('monthly_reset_day')}."
    )


# ─────────────────────────────────────────────────────────────────────────
# Formateo del status para el CLI.
# ─────────────────────────────────────────────────────────────────────────

def format_status() -> str:
    """String multilínea con el estado completo, para CLI status / debug."""
    snap = get_remaining()
    state = load_state()
    lines = [
        "═" * 60,
        "ElevenLabs · contador local de saldo",
        "═" * 60,
        f"Plan tier         : {snap['plan_tier']}",
        f"Saldo actual      : {snap['credits']:,} créditos",
        f"Límite mensual    : {snap['monthly_limit']:,} créditos",
    ]
    if snap["pct_of_monthly"] is not None:
        lines.append(f"% del mensual     : {snap['pct_of_monthly']:.1f}%")
    lines += [
        f"Día reset mensual : {state.get('monthly_reset_day')}",
        f"Ratio chars/créd. : {snap['ratio']} (créditos por carácter)",
        f"Última actualiz.  : {snap['credits_iso']} ({snap['source']})",
        f"Configurado       : {'sí' if snap['configured'] else 'NO — corre `set` antes'}",
        f"Eventos en hist.  : {len(state.get('history', []))}",
        "═" * 60,
    ]
    if not snap["configured"]:
        lines += [
            "",
            "Para configurar (una vez, mirando el dashboard ElevenLabs):",
            "  python utilities/elevenlabs_balance.py set \\",
            "      --credits <saldo_actual_visible_dashboard> \\",
            "      --tier <Starter|Creator|Pro|...> \\",
            "      --limit <créditos_mensuales_del_plan> \\",
            "      --reset-day <día_del_mes_de_reset> \\",
            "      --ratio 0.79",
            "",
            "Dashboard: https://elevenlabs.io/app/usage",
        ]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────
# CLI.
# ─────────────────────────────────────────────────────────────────────────

def _cli_status(_args: argparse.Namespace) -> int:
    print(format_status())
    return 0


def _cli_set(args: argparse.Namespace) -> int:
    set_balance(
        credits=args.credits,
        plan_tier=args.tier,
        monthly_limit=args.limit,
        reset_day=args.reset_day,
        ratio=args.ratio,
    )
    print(format_status())
    return 0


def _cli_record(args: argparse.Namespace) -> int:
    event = record_usage(slug=args.slug, chars=args.chars, credits=args.credits)
    print(json.dumps(event, ensure_ascii=False, indent=2))
    print()
    print(format_status())
    return 0


def _cli_history(args: argparse.Namespace) -> int:
    state = load_state()
    history = state.get("history", [])
    n = args.n or 10
    for evt in history[-n:]:
        print(json.dumps(evt, ensure_ascii=False))
    return 0


def _cli_check(args: argparse.Namespace) -> int:
    ok, msg = pre_check(chars=args.chars)
    print(msg)
    return 0 if ok else 1


def _cli_sync(args: argparse.Namespace) -> int:
    """Lee la API key de settings.local.json y sincroniza el saldo."""
    settings = REPO_ROOT / ".claude" / "settings.local.json"
    env = json.loads(settings.read_text(encoding="utf-8")).get("env", {})
    api_key = env.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY no está en .claude/settings.local.json")
        return 1
    result = sync_from_api(
        api_key=api_key,
        plan_tier=args.tier,
        monthly_limit=args.limit,
        reset_day=args.reset_day,
        ratio=args.ratio,
    )
    print(f"Periodo: {result['period_start'].date()} → {result['now'].date()}")
    print(f"Consumido: {result['consumed']:,} créditos")
    print(f"Límite:    {result['limit']:,} créditos")
    print(f"Restante:  {result['remaining']:,} créditos")
    print()
    print(format_status())
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="elevenlabs_balance",
        description="Contador local de saldo ElevenLabs (gitignored, persistente).",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="Muestra el estado actual.").set_defaults(func=_cli_status)

    p_set = sub.add_parser("set", help="Snapshot manual del dashboard.")
    p_set.add_argument("--credits", type=int, required=True, help="Créditos restantes visibles en el dashboard.")
    p_set.add_argument("--tier", type=str, default=None, help="Plan tier: Starter, Creator, Pro, Scale, Business.")
    p_set.add_argument("--limit", type=int, default=None, help="Límite mensual de créditos del plan.")
    p_set.add_argument("--reset-day", type=int, default=None, dest="reset_day", help="Día del mes en que ElevenLabs reinicia el plan (1-28).")
    p_set.add_argument("--ratio", type=float, default=None, help="Ratio créditos/char (default 0.79 para Multilingual v2).")
    p_set.set_defaults(func=_cli_set)

    p_rec = sub.add_parser("record", help="Registra una generación TTS manualmente.")
    p_rec.add_argument("--slug", type=str, required=True)
    p_rec.add_argument("--chars", type=int, required=True)
    p_rec.add_argument("--credits", type=int, default=None, help="Coste real en créditos si lo conoces (sino se estima).")
    p_rec.set_defaults(func=_cli_record)

    p_hist = sub.add_parser("history", help="Últimos N eventos del historial.")
    p_hist.add_argument("--n", type=int, default=10)
    p_hist.set_defaults(func=_cli_history)

    p_chk = sub.add_parser("check", help="Pre-check de margen para N chars.")
    p_chk.add_argument("--chars", type=int, required=True)
    p_chk.set_defaults(func=_cli_check)

    p_sync = sub.add_parser(
        "sync",
        help="Sincroniza saldo desde la API ElevenLabs (/v1/usage/character-stats).",
    )
    p_sync.add_argument("--tier", type=str, required=True, help="Plan: Starter / Creator / Pro / Scale / Business.")
    p_sync.add_argument("--limit", type=int, default=None, help="Override del límite mensual (sino usa default del tier).")
    p_sync.add_argument("--reset-day", type=int, default=1, dest="reset_day", help="Día del mes en que el plan reinicia (default 1).")
    p_sync.add_argument("--ratio", type=float, default=None, help="Override del ratio créditos/char.")
    p_sync.set_defaults(func=_cli_sync)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
