# Setup laptop — ElevenLabs API Key

> **Archivo temporal.** Léelo en la laptop, completa los pasos, y bórralo con el último comando. Se creó 2026-04-22 tras configurar ElevenLabs en el desktop.

## Qué está configurado ya en el desktop

- Suscripción ElevenLabs Starter yearly ($5/mes) con commercial license.
- API key restringida (solo `Text to Speech: Access` + `Voices: Read`; resto `No Access`).
- Key guardada en Chrome Password Manager (busca "ElevenLabs" en `chrome://passwords`) → sincroniza con la laptop automáticamente si estás logueado con la misma cuenta Google.
- Voz narrador elegida: **Luis** (`voice_id = GojDwihhnL1f7RrBuXsJ`, peninsular male, narrative_story).
- Plan completo: [docs/plan-audiolibros-ficciones.md](docs/plan-audiolibros-ficciones.md).

## Qué hay que hacer aquí (laptop) — 4 pasos

### 1. Copiar la API key desde Chrome Password Manager

- Abre Chrome logueado con la misma cuenta Google que usas en el desktop.
- Ve a `chrome://passwords` → busca la entrada de ElevenLabs / robohogar.
- Copia el valor del campo password (formato `sk_...`, ~51 caracteres).

### 2. Crear `settings.local.json` en la laptop

Crea el archivo `C:\Users\bakal\robohogar\.claude\settings.local.json` con este contenido exacto:

```json
{
  "env": {
    "ELEVENLABS_API_KEY": "PEGAR_AQUI_LA_KEY_DE_CHROME"
  }
}
```

Sustituye `PEGAR_AQUI_LA_KEY_DE_CHROME` (entre las comillas dobles) por la key que copiaste. Guarda.

El archivo está en `.gitignore` línea 138 — no se commitea nunca, es local de cada máquina por diseño.

### 3. Verificar que la key autentica en la laptop

En terminal, desde la raíz del repo:

```bash
python utilities/verify_elevenlabs_auth.py
```

**Resultado esperado:**

```
Key cargada: sk_XXXX... (51 chars)
Probando: https://api.elevenlabs.io/v1/voices

AUTH OK -- HTTP 200, 23 voces accesibles

Voces ES detectadas (2, primeras 10):
  - David Martin - Confident and Balanced  id=Nh2zY9kknu...  accent=peninsular  gender=male
  - Luis - Polished, Mature and Credible   id=GojDwihhnL...  accent=peninsular  gender=male
```

Si sale `HTTP 401` → la key copiada no es correcta. Vuelve al paso 1.
Si sale `HTTP 403` → la key no tiene permiso `Voices: Read`. Se resuelve en el dashboard ElevenLabs.

### 4. Verificar ffmpeg en la laptop

```bash
ffmpeg -version
```

Si sale `command not found` → instalar:

```powershell
winget install Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
```

Después de instalar, **cerrar la terminal actual y abrir una nueva** (winget modifica el PATH pero la terminal activa no lo ve hasta reiniciar). Re-ejecutar `ffmpeg -version` para confirmar.

## Cuando todo pase — borrar este archivo

Desde la raíz del repo:

```bash
git rm LAPTOP-SETUP-ELEVENLABS.md
git commit -m "chore: setup laptop ElevenLabs completado"
git push
```

O abre la conversación con Claude en la laptop y dile *"borra LAPTOP-SETUP-ELEVENLABS.md y commitea"*.
