# Beehiiv · snippets audiolibro · Pipo

**Generado:** 2026-04-27 por `/audiobook-generate pipo`.
**Relato fuente:** [`2026-04-27-pipo.md`](2026-04-27-pipo.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/pipo.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/pipo.mp3 |
| **Duración** | 18,5 min (1110,2 s) |
| **Tamaño** | 17,3 MB (17 348 KB) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Voz** | **Gabo - Deep, Evocative and Resonant** (My Voices ElevenLabs · default desde 2026-04-27, primer uso · sustituye Luis) |
| **Chunks TTS** | 4 · 14 010 chars · ~11 068 créditos ElevenLabs (~9,1% cuota Creator) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK |
| **Capítulos detectados** | 6 (`00:05 Las manos`, `03:36 El altar`, `06:39 El circuito`, `10:37 ¿Jugamos?`, `12:51 La llamada`, `14:56 El termo`) |

---

## (a) Título del post Beehiiv

```
🎧 El cazador que apunta a la nieta de chatarra que el robot lleva dos años soldando
```

*84 chars — usa `display_title` (G1, banda B, 14 palabras, formato YouTube-style canon 2026-04-26 PM). Va a truncar en el preview de email móvil (~45 chars) — cae después de "que apunta a la nieta de chatarra" con elipsis. Es el comportamiento deseado del nuevo canon: el hook está en los primeros 40 chars y el resto se completa en la apertura del email/web.*

---

## (b) Subtítulo / dek

```
Cuidados rotos · Un padre vuelve al pinar donde tiró el robot de su hijo y se encuentra con que lleva dos años soldando una hija de chatarra.
```

*Apertura con tag poético `Cuidados rotos · ` + meta_description del frontmatter. El tag poético funciona como la pílula tonal del catálogo cerrado de 10 (eje afecto-cuidado: vínculo primario sustituido o quebrado).*

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · 18 min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/pipo" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/pipo.mp3" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
  </p>
</div>
```

---

## (d) Custom HTML block · web-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from email**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid rgba(12,12,12,0.15); border-radius: 8px; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <p style="margin: 0 0 12px; font-size: 14px; font-weight: 600; color: #0C0C0C;">
    🎧 Escuchar · <span style="color: #6B7280; font-weight: 400;">18 min</span>
  </p>
  <audio id="audio-pipo" controls preload="none" style="width: 100%; height: 44px;" src="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/pipo.mp3"></audio>
  <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/pipo.mp3" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-pipo');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: 'Pipo',
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
5. El frontispicio (`Pipo` centrado entre Snippet 2 y primer H2) va a continuación.
6. El cuerpo del relato (`I. Las manos / II. El altar / …`) va **después** del frontispicio.
7. Tras la prosa: snippet `Lo real detrás del relato` + CTA suscripción ficción canon.
8. Publica con **Email and web**.
9. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

## Regeneración parcial

Si algún chunk suena mal:

- Chunks persistidos en `assets/audio/ficciones/_chunks-pipo/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings` (más stability si suena inestable; más similarity_boost si cambia timbre)
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `pipo.mp3`)
