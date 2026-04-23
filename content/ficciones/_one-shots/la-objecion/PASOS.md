# PASOS — La objeción

## Metadata SEO (para pegar en Beehiiv)

- **Title Beehiiv:** La objeción
- **SEO title:** La objeción | Ficciones Domésticas ROBOHOGAR
- **Meta description:** Un humanoide doméstico descubre que el ministro al que sirve filtra un expediente OTAN. Tiene veintitrés días y un botón que no hace ruido.
- **Slug:** la-objecion
- **Tag Beehiiv:** Ficciones Domésticas
- **Categoría tonal:** inquietante (primaria) con deriva radical
- **Tipo publicación:** Email and web (según preferencia F1)

## Hero elegido

Pendiente generar vía `/nano-banana`. Código visual one-shot (no es serie), recomendación: **canon "portada minimalista · objeto-testigo"** (asset-catalog §5 del repo).

Prompt sugerido:

```
Minimal poster style, close-mid shot of humanoid figure in dim corridor of Madrid upper-middle-class house at night, standing still in front of closed study door, right index finger pressed on left forearm synthetic skin, matte body no LEDs, face unlit, 2036 Spanish domestic interior (wooden parquet, framed photograph on wall, single warm lamp spilling from below closed door), deep night blue palette #1E2A3A with warm amber spill #F5A623 on forearm, 3/4 profile, shallow depth of field, cinematic still 16:9, no text, no letters, no asian characters, no windows to exterior, no glowing eyes, no neon, testigo silencioso mood, tension without horror, After Yang + Ex Machina corridor composition
```

Archivo destino: `content/ficciones/_one-shots/la-objecion/assets/hero-la-objecion.png`

## Checklist publicación

- [ ] Rafael relee el borrador (`content/ficciones/_one-shots/la-objecion/2026-04-23-la-objecion.md`)
- [ ] Escuchar audiolibro en móvil — copia en vault: `02-Drafts/Ficciones/La objeción (audiolibro).md`
- [ ] Correr `/validate-prose-es content/ficciones/_one-shots/la-objecion/2026-04-23-la-objecion.md` (paso 8.4 obligatorio, second reader externo)
- [ ] Ajustes pos-validador si devuelve PENDING_FIXES
- [ ] Generar hero via `/nano-banana` con prompt arriba
- [ ] Pegar prosa en Beehiiv (post con formato Markdown o bloques nativos), cover = hero
- [ ] Configurar SEO title + meta description + slug + tag
- [ ] Publicar como `Email and web`
- [ ] Tras publicar, ejecutar `/post-publish <URL>` (sync published, registro, llms.txt, vault, social)

## Log editorial

- **One-shot**, no pertenece a serie. Si Rafael lo quisiera serializar (línea *"Despachos privados"* — dilemas políticos vistos desde robots testigos), habría que crear `content/ficciones/despachos-privados/` con character bible + arco-serie antes del próximo episodio. No canonizar nada aún.
- Ningún personaje basado en figura real. **Íñigo Aldaz** (ministro), **Lourdes Beltrán** (periodista retirada), **Hernán Villanueva** (asesor colombiano) y **VELA-9** (humanoide modelo ficticio canon nuevo, Doméstica Ibérica gama 2035) son invención.
- Cero marcas comerciales de robótica doméstica (regla `editorial.md § Narrativa especulativa — SIN MARCAS COMERCIALES`).
- Dato real anclado múltiple: AI Act real (Reglamento UE 2024/1689) + Grupo de Puebla (foro 2019) + PSOE en Internacional Socialista + bases OTAN Rota y Torrejón + NATO COSMIC TOP SECRET categoría real + Pegasus 2022 + apagón ibérico 28-abril-2025.
- Big-lie único: la cláusula 47 del AI Act (ampliación ficticia 2034). Todo lo demás es verificable.

## Hooks potenciales para futura serialización

Si Rafael quisiera abrir línea *Despachos privados*, semillas plantadas en este relato que admitirían eco:
1. El destino de la cena del nueve de mayo (¿ocurrió? ¿qué pasó con los once nombres?) — NUNCA resolver: ambigüedad es la tesis.
2. Lourdes Beltrán como POV alternativo en un episodio futuro — periodista retirada con migrañas que fue joven en Managua 1989.
3. Hernán Villanueva y la triangulación Cartagena-Caracas — se podría ver el otro lado del canal desde Bogotá.
4. VELA-9 desactivado tras pulsar o no pulsar — episodio especulativo sobre la vida de un humanoide post-cláusula 47.

Ninguno se activa sin decisión editorial explícita de Rafael.

## Riesgo editorial — avisar a Rafael antes de publicar

Este relato toca coordenadas políticas identificables (socialdemocracia ES + Grupo de Puebla + tensión Venezuela) aunque sin nombres reales. Dos lecturas posibles del lector ES:
- **Lectura A — funciona:** ficción especulativa con anclaje político realista, tesis sobre el despacho privado y la rendición de cuentas ideológica. Resonancia sin partidismo.
- **Lectura B — riesgo:** algún lector puede leerlo como panfleto anti-PSOE/anti-Grupo-de-Puebla. Mitigación ya en el texto: el ministro actúa por convicción sincera, no por corrupción; Lourdes comparte raíz ideológica; el villano humano es la soberbia del despacho, no la ideología.

Rafael decide si el equilibrio está bien calibrado. Si hay dudas, posible ajuste: mover la referencia OTAN a contexto más neutro (filtración Rusia vía cualquier canal), pero pierde el eco específico al debate español actual sobre Venezuela/Pegasus que era la premisa del encargo.
