# Beehiiv · snippets audiolibro · La objeción

**Generado:** 2026-04-25 por `/audiobook-generate la-objecion` (regeneración para piloto distribución FASE 3 — añade chunks-index.json + covers).
**Relato fuente:** [`2026-04-23-la-objecion.md`](2026-04-23-la-objecion.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/la-objecion.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-objecion.mp3 |
| **Duración** | 19,1 min (1143,1s) |
| **Tamaño** | 17,4 MB (18.290.773 bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | 4 · 15.894 chars · coste real ~$1,59 (~1,6% cuota Creator 100k) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK (1143,10s, 128 kbps) |
| **chunks-index.json** | 9 capítulos (`Parte uno.` a `Parte nueve.`) — reconstruido manualmente, ver "Notas" abajo |
| **Cover YouTube** | `assets/audio/ficciones/covers/la-objecion-yt-1280x720.png` (962 KB) |
| **Cover podcast** | `assets/audio/ficciones/covers/la-objecion-podcast-1400x1400.jpg` (171 KB) |

---

## (a) Título del post Beehiiv

```
🎧 Ficción · La objeción
```

*24 chars — cabe limpio en subject line de email (límite recomendado 45 chars per `@rules/newsletter.md`).*

---

## (b) Subtítulo / dek

```
Un humanoide doméstico descubre que el ministro al que sirve filtra un expediente OTAN. Tiene veintitrés días y una alarma silenciosa.
```

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · 19 min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/la-objecion" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-objecion.mp3" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
  </p>
</div>
```

---

## (d) Custom HTML block · web-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from email**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;">
    🎧 Escuchar · <span style="color: #6B7280; font-weight: 400;">19 min</span>
  </p>
  <audio id="audio-la-objecion" controls preload="none" style="width: 100%; height: 44px;" src="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-objecion.mp3"></audio>
  <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-objecion.mp3" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-la-objecion');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: 'La objeción',
        artist: 'ROBOHOGAR · Ficciones Domésticas',
        artwork: []
      });
    });
  })();
</script>
```

---

## Orden de pegado en Beehiiv

1. **(a)** como título del post.
2. **(b)** como subtítulo.
3. **(c)** primer Custom HTML block inmediatamente después del subtítulo → engranaje → **hide from web**.
4. **(d)** segundo Custom HTML block inmediatamente después → engranaje → **hide from email**.
5. El cuerpo del relato (`Parte uno. / Parte dos. / …`) va **después** de ambos bloques HTML.
6. Publica con **Email and web**.
7. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

---

## Capítulos detectados (chunks-index.json)

9 capítulos correctos, reconstruidos manualmente desde el patrón `Parte uno.` a `Parte nueve.` del `audiolibro.txt`. Timestamps calculados con velocidad efectiva 14,11 chars/sec sobre el texto completo + offset de intro (2,53s) + silencio (2,0s).

| Cap. | Inicio | Título |
|---|---|---|
| 1 | 00:05 | El botón |
| 2 | 01:02 | Octubre del treinta y cuatro |
| 3 | 03:28 | Hernán |
| 4 | 07:35 | La diapositiva |
| 5 | 09:46 | La cláusula |
| 6 | 12:25 | Los veintitrés días |
| 7 | 14:49 | Dos de mayo |
| 8 | 16:11 | Managua |
| 9 | 17:03 | La una y dieciséis |

Estos son los timestamps que `/audiobook-distribute` usará para los chyrons del MP4 YouTube + chapters timestamped en la descripción.

---

## Notas de regeneración 2026-04-25

- **Bug detectado en `utilities/generate_audio.py`:** el regex de detección de capítulos solo matchea `Uno. / Dos. / Tres.` aislados al inicio de línea, pero este relato (y otros del repo) usa `Parte uno. / Parte dos.`. Resultado del run inicial: 2 falsos positivos al final del texto (líneas con "Uno." y "Dos." en otro contexto narrativo). Fix manual aplicado al chunks-index.json. **Pendiente:** extender el regex del script para soportar también `Parte X.` para que los próximos relatos no necesiten fix manual.
- **Cambio de plan ElevenLabs:** Starter (40k chars/mes) → Creator (100k chars/mes) durante la regeneración. Coste mensual sube a $22 vs $5 anterior. Decisión motivada por la cadencia mensual de audiolibros que excede la cuota Starter.

## Regeneración parcial

Si algún chunk suena mal (transición rara, nombre pronunciado torcido):

- Chunks persistidos en `assets/audio/ficciones/_chunks-la-objecion/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings` (stability / similarity_boost)
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `la-objecion.mp3`)

Ahorra cuota API vs regenerar los 4 chunks completos.
