# Beehiiv · snippets audiolibro · Papá desde Singapur

**Generado:** 2026-04-22 por `/audiobook-generate papa-desde-singapur`.
**Relato fuente:** [`2026-04-22-papa-desde-singapur.md`](2026-04-22-papa-desde-singapur.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/papa-desde-singapur.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/papa-desde-singapur.mp3 |
| **Duración** | 16,9 min (1016,87s) |
| **Tamaño** | 15,5 MB (16.271.195 bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | 4 · 14.215 chars · coste real $1,42 (~23,7 % cuota Starter) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK |

---

## (a) Título del post Beehiiv

```
🎧 Ficción · Papá desde Singapur
```

*32 chars — cabe holgadamente en subject line móvil.*

---

## (b) Subtítulo / dek

```
Andrés se desplaza tres meses por trabajo y contrata un humanoide-avatar para seguir en casa. Cuando vuelve, su hijo de seis años compara.
```

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · 17 min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/papa-desde-singapur" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/papa-desde-singapur.mp3" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
  </p>
</div>
```

---

## (d) Custom HTML block · web-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from email**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;">
    🎧 Escuchar · <span style="color: #6B7280; font-weight: 400;">17 min</span>
  </p>
  <audio id="audio-papa-desde-singapur" controls preload="none" style="width: 100%; height: 44px;" src="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/papa-desde-singapur.mp3"></audio>
  <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/papa-desde-singapur.mp3" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-papa-desde-singapur');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: 'Papá desde Singapur',
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
5. El cuerpo del relato (`Uno. / Dos. / …`) va **después** de ambos bloques HTML.
6. Publica con **Email and web**.
7. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

## Regeneración parcial

Si algún chunk suena mal (transición rara, nombre pronunciado torcido):

- Chunks persistidos en `assets/audio/ficciones/_chunks-papa-desde-singapur/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings` (stability / similarity_boost)
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `papa-desde-singapur.mp3`)

Ahorra cuota API vs regenerar los 4 chunks completos.
