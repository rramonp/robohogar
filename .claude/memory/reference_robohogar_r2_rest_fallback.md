---
name: ROBOHOGAR — fallback REST API para upload R2 cuando el endpoint S3 falla
description: Existe un script alternativo upload_rss_to_r2_via_api.py que sube el feed RSS vía api.cloudflare.com (rango 104.19) cuando el endpoint S3 r2.cloudflarestorage.com (rango 172.64) está caído por outage parcial de Cloudflare.
type: reference
originSessionId: 4763d061-ea50-4792-bfd0-6665d955e8f2
---
Si el upload del feed RSS de ROBOHOGAR a Cloudflare R2 da `ConnectTimeoutError` con el endpoint S3 (`<account>.r2.cloudflarestorage.com`, IP rango `172.64.x.x`) y otros sitios funcionan: probablemente outage parcial de routing de Cloudflare en ese rango. Pasos:

1. **Diagnosticar primero, no asumir:** `ping 172.64.66.1` (IP del endpoint S3) vs `ping 1.1.1.1` o `ping 104.18.54.45` (otros rangos Cloudflare). Si el primero falla y los otros van, es outage parcial — no es problema local del laptop.
2. **Confirmar mirando commits recientes:** si `git log content/podcast/feed.xml` muestra un upload reciente desde el mismo equipo sin cambios locales, refuerza la hipótesis "fallo de proveedor", no local. Esa pista evita acciones destructivas como desinstalar software (incidente origen 2026-04-25).
3. **Fallback funcional:** correr `python utilities/upload_rss_to_r2_via_api.py` en lugar del script S3 (`upload_rss_to_r2.py`). Sube el mismo feed por la REST API de Cloudflare (`api.cloudflare.com`, rango 104.19) — distinta IP, distinta ruta de peering, suele funcionar cuando el S3 falla.
4. **Pre-requisito**: clave `CLOUDFLARE_API_TOKEN` en `.claude/settings.local.json` (gitignored). Token con permiso `Account > Workers R2 Storage > Edit`. Validable con `GET https://api.cloudflare.com/client/v4/user/tokens/verify`. Token actual creado 2026-04-25 al desbloquear `el-que-viene-a-tomar-cafe`.
5. **Cuando el outage se resuelva**, el script S3 original vuelve a ser válido y es el default (más simple, sin token adicional). El REST queda como fallback estructural documentado para futuros outages.

Mismo patrón vale para upload de MP3 si reapareciera el outage en el rango — actualmente solo el feed.xml tiene el fallback REST escrito, pero el patrón se replica fácil para cualquier objeto R2.
