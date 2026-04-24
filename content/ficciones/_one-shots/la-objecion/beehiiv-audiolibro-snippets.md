# Beehiiv · snippets audiolibro · La objeción

**Generado:** 2026-04-23 por `/audiobook-generate la-objecion`.
**Relato fuente:** [`2026-04-23-la-objecion.md`](2026-04-23-la-objecion.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/la-objecion.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-objecion.mp3 |
| **Duración** | 19,0 min (1.137,5 s) |
| **Tamaño** | 17,4 MB (18.201.330 bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | 4 · 15.894 chars · coste real $1,59 (~26,5% cuota Starter) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe 1137,5s OK |

---

## (a) Título del post Beehiiv

```
🎧 Ficción · La objeción
```

*23 chars — bien dentro del límite de subject line.*

---

## (b) Subtítulo / dek

```
Un humanoide doméstico descubre que el ministro al que sirve filtra un expediente OTAN. Tiene veintitrés días y un botón que no hace ruido.
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
5. El cuerpo del relato (`Parte uno. El botón. / Había tres maneras…`) va **después** de ambos bloques HTML.
6. Publica con **Email and web**.
7. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

## Atajo: archivo HTML Beehiiv-ready completo

Para evitar el copy-paste manual de 5 piezas, todo el cuerpo del post (snippets + prosa + CTA ficción canónico) está montado en un solo archivo:

📄 [`beehiiv-paste.html`](beehiiv-paste.html)

Abrir ese archivo en navegador o editor → seleccionar todo → copiar → pegar en Beehiiv. Las visibility toggles por bloque siguen siendo manuales (Beehiiv no las hereda del HTML pegado).

## Regeneración parcial

Si algún chunk suena mal:
- Chunks persistidos en `assets/audio/ficciones/_chunks-la-objecion/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings`
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe `la-objecion.mp3`)

Ahorra cuota API vs regenerar los 4 chunks completos.
