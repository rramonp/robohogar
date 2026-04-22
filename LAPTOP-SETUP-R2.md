# Setup laptop — Cloudflare R2 + verificación completa

> **Archivo temporal.** Creado tras commit `1d9c1b2` (FASE 0 audiolibros cerrada en desktop). Borrar al final con el paso 8.

## Contexto en 3 líneas

- El desktop (`c:\Users\cri-c\robohogar`) tiene FASE 0 audiolibros cerrada al 100%: suscripción ElevenLabs Starter + bucket R2 `robohogar-audio` + credenciales + ffmpeg + bumpers `assets/audio/intro-ficciones.mp3` y `outro-ficciones.mp3` generados con voz Luis.
- La laptop (`c:\Users\bakal\robohogar`) solo tiene la key de ElevenLabs (setup previo). Le faltan las **5 variables de R2** + `boto3` + validación de ambos verificadores.
- Los 6 secretos (1 ElevenLabs + 3 R2 sensibles) están en **Chrome Password Manager** sincronizado con la cuenta Google del desktop → aparecerán solos en la laptop al abrir Chrome.

## Instrucciones para Claude (o Rafael manual) — hazlo en orden

### Paso 1 — git pull

```bash
git pull --ff-only origin main
```

Verifica que aparece el commit `1d9c1b2 feat(audiolibros): FASE 0 completada` y que se descargan:
- `assets/audio/intro-ficciones.mp3` (2.53s, ~76KB)
- `assets/audio/outro-ficciones.mp3` (11.89s, ~225KB)
- `utilities/verify_r2_auth.py`

### Paso 2 — Preparar `.claude/settings.local.json` con placeholders

**(Tarea para Claude en la laptop: edita el archivo `c:\Users\bakal\robohogar\.claude\settings.local.json` para que contenga la estructura final con placeholders en los valores sensibles, preservando el `ELEVENLABS_API_KEY` existente si ya estaba ahí.)**

Estado final esperado:

```json
{
  "env": {
    "ELEVENLABS_API_KEY": "sk_...(preservar el valor actual si ya existe)",
    "R2_ACCOUNT_ID": "PEGAR_ACCOUNT_ID_32_CHAR_HEX",
    "R2_ACCESS_KEY": "PEGAR_ACCESS_KEY_ID",
    "R2_SECRET_KEY": "PEGAR_SECRET_ACCESS_KEY",
    "R2_BUCKET": "robohogar-audio",
    "R2_PUBLIC_URL": "https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev"
  }
}
```

Nota: `R2_BUCKET` y `R2_PUBLIC_URL` están pre-rellenados — son comunes a todas las máquinas (el bucket es uno solo). Solo hay que pegar los 3 placeholders `R2_*` sensibles (y confirmar que ElevenLabs sigue ahí).

Nota seguridad: este archivo está en `.gitignore` línea 138 → no se commitea nunca. Es local por diseño.

### Paso 3 — Pegar las 4 credenciales desde Chrome Password Manager

1. Abrir `chrome://passwords` en la laptop (misma cuenta Google que el desktop).
2. Buscar:
   - `ElevenLabs` / `robohogar ElevenLabs` → la key `sk_...` va en `ELEVENLABS_API_KEY` (confirma que está bien).
   - `ROBOHOGAR Cloudflare R2` → contiene los 3 valores sensibles (Account ID + Access Key ID + Secret Access Key). Copia cada uno en su campo.
3. Guardar el archivo.

**IMPORTANTE:** NO pegar estos valores en el chat con Claude — pegarlos directamente en el archivo. El flujo es Chrome → archivo, no Chrome → chat → archivo.

### Paso 4 — Instalar boto3

```bash
pip install boto3
```

Debe terminar con `Successfully installed boto3-...`.

### Paso 5 — Verificar ElevenLabs (debería seguir funcionando)

```bash
python utilities/verify_elevenlabs_auth.py
```

Resultado esperado:

```
Key cargada: sk_XXX... (51 chars)
AUTH OK -- HTTP 200, 23 voces accesibles

Voces ES detectadas (2, primeras 10):
  - David Martin - Confident and Balanced  id=Nh2zY9kknu...  accent=peninsular
  - Luis - Polished, Mature and Credible   id=GojDwihhnL...  accent=peninsular
```

Si falla con 401 → la key en el JSON no es correcta. Volver al Paso 3.

### Paso 6 — Verificar R2 (smoke test 4/4)

```bash
python utilities/verify_r2_auth.py
```

Resultado esperado:

```
Env cargado desde settings.local.json:
  R2_ACCOUNT_ID: c869eeac...
  R2_BUCKET:     robohogar-audio
  R2_PUBLIC_URL: https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev

Smoke test R2 (upload -> public GET -> delete):
  [1/4] HEAD bucket 'robohogar-audio' OK (credenciales autentican)
  [2/4] PUT 'test-connection-...txt' (55 bytes) OK
  [3/4] GET publico '...' OK (contenido coincide, 55 bytes)
  [4/4] DELETE '...' OK (cleanup)

AUTH OK -- R2 listo para uso. Credenciales, permisos y URL publica verificados.
```

Posibles errores:
- `[1/4] FAIL HeadBucket` → `R2_ACCOUNT_ID` o credenciales mal pegadas. Revisa el Paso 3.
- `[2/4] FAIL PutObject` → el token no tiene permiso Object Write. Raro si usas las mismas creds que desktop.
- `[3/4] FAIL HTTP 403` → Cloudflare bloquea el UA. NO debería pasar — el script ya envía UA de Chrome. Si pasa, abre un issue.

### Paso 7 — Verificar ffmpeg

```bash
ffmpeg -version
```

Si ya estaba instalado de un setup previo, debe devolver versión. Si sale `command not found`:

```powershell
winget install Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
```

Tras instalar, cerrar la terminal actual y abrir una nueva (winget modifica PATH pero la terminal activa no lo ve hasta reiniciar). Re-ejecutar `ffmpeg -version`.

### Paso 8 — Borrar este archivo + commit + push

Cuando los 6 pasos anteriores pasen, desde la raíz del repo:

```bash
git rm LAPTOP-SETUP-R2.md
git commit -m "chore: setup laptop R2 completado"
git push origin main
```

O pide a Claude en la laptop: *"borra LAPTOP-SETUP-R2.md y haz commit + push"*.

## Checklist final — marcar cada uno al ir completando

- [ ] Paso 1: `git pull` ejecutado, commit `1d9c1b2` visible en `git log`, MP3 descargados en `assets/audio/`
- [ ] Paso 2: `.claude/settings.local.json` con la estructura de 6 env vars
- [ ] Paso 3: 4 credenciales pegadas desde Chrome Password Manager (no desde chat)
- [ ] Paso 4: `pip install boto3` completado
- [ ] Paso 5: `verify_elevenlabs_auth.py` devuelve AUTH OK + 23 voces
- [ ] Paso 6: `verify_r2_auth.py` devuelve 4/4 OK
- [ ] Paso 7: `ffmpeg -version` funciona
- [ ] Paso 8: este archivo borrado + commit + push

Con estos 8 checks ✓, laptop está al mismo nivel que desktop y FASE 0 cierra al 100% en ambas máquinas. Listo para disparar FASE 1 piloto desde cualquiera de las dos.

## Si algo rompe — diagnóstico rápido

- **`git pull` da conflict** → no debería; si pasa, pega el mensaje a Claude en la laptop para resolver.
- **El JSON tiene formato inválido (trailing comma, comillas simples)** → `python -c "import json; json.load(open('.claude/settings.local.json'))"` te dice la línea exacta del error.
- **verify_r2_auth.py falla en [3/4] con 403** → el User-Agent del script ya esquiva el bot protection de Cloudflare; si aún falla, propagación lenta — esperar 5 min y reintentar.
- **`python` no se reconoce** → Python no está en PATH de la laptop. Instalar desde [python.org](https://www.python.org/downloads/) o vía `winget install Python.Python.3.12`.

---

**Tras completar y borrar este archivo, volver al desktop y disparar trigger FASE 1 con el relato piloto elegido:**

> *"Retomamos plan audiolibros — empezamos piloto manual con `<slug-relato>`"*

Candidatos del plan: `la-casa-de-amparo`, `operador-nocturno-v2`, u otro de tu elección.
