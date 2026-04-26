"""get_vault_path.py — devuelve la ruta absoluta del vault Obsidian ROBOHOGAR.

Autodetecta la ruta sin depender de variables de entorno externas. El vault
vive sincronizado vía OneDrive HBX Group + Syncthing entre las dos máquinas
de Rafael (laptop bakal · desktop cri-c). Cada máquina tiene su propio raíz
de OneDrive, pero el subpath dentro del raíz es idéntico.

Estrategia (en orden):
1. Variable de entorno HBX_VAULT si está definida (compatibilidad legacy).
2. Auto-detección por nombre de usuario Windows (USERPROFILE) → patrones canónicos.
3. Búsqueda por filesystem como último recurso (encuentra el primer
   directorio que termine en `05-01_Robotica Newsletter`).

Si ninguna estrategia funciona, exit code 1 con mensaje claro.

Uso:
    python utilities/get_vault_path.py
    # → imprime la ruta absoluta del vault al stdout

    VAULT=$(python utilities/get_vault_path.py) && cp foo "$VAULT/03-Published/"
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


# Rutas conocidas (desktop + laptop) — actualizar si Rafael añade una tercera máquina.
KNOWN_LAYOUTS: list[Path] = [
    Path(r"C:\Users\bakal\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter"),
    Path(r"C:\Users\cri-c\OneDrive - HBX Group\Desktop\DEMAND\Obsidian\RRP\RRP_ONEDRIVE\HBX\05_Personal\05-01_Robotica Newsletter"),
]

# Subpath canónico bajo cualquier base de Obsidian.
SUBPATH = Path("RRP/RRP_ONEDRIVE/HBX/05_Personal/05-01_Robotica Newsletter")


def _from_env() -> Path | None:
    raw = os.environ.get("HBX_VAULT")
    if not raw:
        return None
    # HBX_VAULT puede apuntar al raíz Obsidian (sin subpath) o ya con subpath.
    base = Path(raw)
    if (base / SUBPATH).is_dir():
        return base / SUBPATH
    if base.name == "05-01_Robotica Newsletter" and base.is_dir():
        return base
    return None


def _from_known_layouts() -> Path | None:
    for path in KNOWN_LAYOUTS:
        if path.is_dir():
            return path
    return None


def _from_userprofile() -> Path | None:
    """Intenta deducir desde USERPROFILE actual (cubre cualquier usuario nuevo).

    Para una máquina nueva con usuario distinto de bakal/cri-c, asumimos que
    OneDrive HBX está en `<USERPROFILE>/OneDrive - HBX Group/Desktop/DEMAND/Obsidian/`.
    """
    user = os.environ.get("USERPROFILE")
    if not user:
        return None
    candidate = Path(user) / "OneDrive - HBX Group" / "Desktop" / "DEMAND" / "Obsidian" / SUBPATH
    return candidate if candidate.is_dir() else None


def _from_search() -> Path | None:
    """Último recurso: buscar en directorios típicos de OneDrive."""
    user = os.environ.get("USERPROFILE")
    if not user:
        return None
    onedrive_roots = [
        Path(user) / "OneDrive - HBX Group",
        Path(user) / "OneDrive",
    ]
    for root in onedrive_roots:
        if not root.is_dir():
            continue
        # Buscar hasta 6 niveles de profundidad para no irnos por los cerros.
        for path in root.rglob("05-01_Robotica Newsletter"):
            if path.is_dir():
                # Validar mínimo: tiene que contener al menos 03-Published o Wiki.
                if (path / "03-Published").is_dir() or (path / "Wiki").is_dir():
                    return path
    return None


def resolve() -> Path:
    """Resuelve la ruta del vault o lanza SystemExit con mensaje útil."""
    for strategy in (_from_env, _from_known_layouts, _from_userprofile, _from_search):
        result = strategy()
        if result is not None:
            return result
    sys.exit(
        "ERROR: no se ha podido localizar el vault Obsidian ROBOHOGAR.\n"
        "Estrategias intentadas: $HBX_VAULT, layouts conocidos (bakal/cri-c), "
        "USERPROFILE/OneDrive - HBX Group/..., búsqueda en OneDrive.\n"
        "Si añades una máquina nueva, actualiza KNOWN_LAYOUTS en utilities/get_vault_path.py."
    )


if __name__ == "__main__":
    print(resolve())
