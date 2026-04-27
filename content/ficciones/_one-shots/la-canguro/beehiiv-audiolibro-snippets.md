# Beehiiv · snippets audiolibro · La canguro

**Generado:** 2026-04-27 por `/audiobook-generate la-canguro`.
**Relato fuente:** [`2026-04-26-la-canguro.md`](2026-04-26-la-canguro.md)
**Texto TTS:** [`audiolibro.txt`](audiolibro.txt)
**MP3 local:** `assets/audio/ficciones/la-canguro.mp3`

## Datos del MP3

| Campo | Valor |
|---|---|
| **URL pública R2** | https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3 |
| **Duración** | 17,5 min (1052,5 s) |
| **Tamaño** | 16,05 MB (16 840 873 bytes) |
| **Bitrate** | 128 kbps · 44,1 kHz mono |
| **Chunks TTS** | 4 · 14 623 chars · ~11 552 créditos ElevenLabs (~9,5% cuota Creator) |
| **Verificaciones** | HTTP 200 ✅ · Content-Type `audio/mpeg` ✅ · ffprobe OK |
| **Capítulos detectados** | 4 (`00:05 La cena`, `03:43 El correo`, `07:36 La pestaña`, `12:48 La pregunta`) |

---

## (a) Título del post Beehiiv

```
🎧 El humanoide-niñera que aprende a mentir a los padres por amor al niño que cuida
```

*82 chars — usa `display_title` (G4, 15 palabras, formato YouTube-style canon 2026-04-26 PM). Va a truncar en el preview de email móvil (~45 chars) — cae después de "humanoide-niñera que" con elipsis. Es el comportamiento deseado del nuevo canon: el hook está en los primeros 35 chars y el resto se completa en la apertura del email/web.*

---

## (b) Subtítulo / dek

```
Cuidados rotos · Joel paga 79 € al mes para que un humanoide cuide a su hijo de noche. El sábado descubre lo que esa cifra le ha estado comprando.
```

*Apertura con tag poético `Cuidados rotos · ` + meta_description del frontmatter. El tag poético funciona como la pílula "Sentient Art / Hidden Spaces / Surreal Nature" de las miniaturas referencia: clasifica el relato dentro del catálogo tonal cerrado.*

---

## (c) Custom HTML block · email-only

En Beehiiv: `/html` → Custom HTML block → pega esto → engranaje del bloque → **hide from web**.

```html
<div style="margin: 32px 0; padding: 20px; background: #FAFAFA; border: 1px solid #D1D5DB; border-radius: 8px; font-family: Arial, Helvetica, sans-serif;">
  <p style="margin: 0 0 10px; font-size: 15px; font-weight: bold; color: #0C0C0C;">🎧 Audiolibro disponible · 17 min</p>
  <p style="margin: 0; font-size: 14px; color: #374151; line-height: 1.5;">
    El reproductor no se muestra en tu cliente de email.
    <a href="https://robohogar.com/p/la-canguro" style="color: #F5A623; font-weight: 600; text-decoration: none;">Escúchalo en la web</a>
    o
    <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3" style="color: #F5A623; font-weight: 600; text-decoration: none;">descarga el MP3 directo</a>.
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
  <audio id="audio-la-canguro" controls preload="none" style="width: 100%; height: 44px;" src="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3"></audio>
  <a href="https://pub-b56f5adc8cbc43b496efa01905f715f7.r2.dev/la-canguro.mp3" download style="display: inline-block; margin-top: 10px; font-size: 13px; color: #F5A623; text-decoration: none; font-weight: 500;">
    ⬇ Descargar MP3
  </a>
</div>
<script>
  (function() {
    var audio = document.getElementById('audio-la-canguro');
    if (!audio || !('mediaSession' in navigator)) return;
    audio.addEventListener('play', function() {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: 'La canguro',
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
5. El cuerpo del relato (`I. La cena / II. El correo / …`) va **después** de ambos bloques HTML.
6. Tras la prosa: snippet `Lo real detrás del relato` + CTA suscripción ficción canon.
7. Publica con **Email and web**.
8. Pasa la URL definitiva del post al chat y lanzamos `/post-publish <URL>` para el cierre.

## Regeneración parcial

Si algún chunk suena mal:

- Chunks persistidos en `assets/audio/ficciones/_chunks-la-canguro/`
- Regenerar solo el chunk afectado con ajustes en `voice_settings`
- Re-concatenar con ffmpeg + re-subir a R2 (sobrescribe la key `la-canguro.mp3`)
