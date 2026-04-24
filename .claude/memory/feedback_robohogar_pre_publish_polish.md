---
name: ROBOHOGAR pre-publish polish — 12 checks (craft + coherencia interna)
description: 12 controles de acabado pre-publicación aplicados a todo borrador ROBOHOGAR (5 craft A1-A5 + 7 coherencia interna B1-B7); origen en 2 incidentes de feedback externo abril 2026
type: feedback
originSessionId: 71f29581-1097-4869-a2e1-3107afa40f67
---
**Rule:** antes de entregar cualquier borrador ROBOHOGAR (review, comparativa, editorial, guía), correr los 12 checks de `@rules/editorial.md § Controles pre-publicación — 12 checks`: 5 de craft (A1-A5) + 7 de coherencia interna (B1-B7). Responder por escrito en `PASOS.md § Controles pre-publicación` con formato `[✅/❌/N/A] — [comentario]`. Si cualquiera falla → reescribir antes de entregar.

**Why:** dos incidentes de feedback externo en abril 2026 revelaron dos disciplinas distintas de acabado pre-publicación que los controles existentes (anti-IA, cero-fantasma, datos-rastreables, editorial-es, formato-beehiiv) no cubrían:

### Incidente Bloque A — "Humanoide bate récord media maratón" (artículo #8, 2026-04-20)

Reviewer externo señaló 5 vicios de *craft* que el artículo tenía a pesar de haber pasado anti-IA, cero-fantasma y editorial-es:

1. **Gancho enterrado en el título (A1).** H1 publicado: *"Un humanoide ha batido el récord mundial humano de media maratón. Lo importante no es el robot."* La tesis contrarian va al final — el 80% de lectores que escanea lee la primera mitad, piensa *"ah, otro récord"* y no llega al giro. Propuesta aceptada: invertir → *"Lo importante no es el robot: un humanoide ha batido el récord humano de media maratón."*
2. **Cifra contrarian sin blindar (A2).** Línea publicada: *"En tareas reales, con el criterio combinado de éxito + seguridad: 12%. Doce."* Un lector espabilado se pregunta *"¿qué significa éxito + seguridad combinados?"* y el artículo no lo define. Propuesta aceptada: añadir parentética ≤10 palabras — *"12% — es decir, completa la tarea sin romper el objeto ni a nadie — en tareas reales"*.
3. **Dato-trampolín (A3).** Línea publicada: *"Hace un año, en la primera edición de esta misma maratón, casi ningún humanoide logró terminar los 21 km… En abril de 2026 cruzaron meta de forma autónoma decenas"* — salto brutal resuelto en media frase, usado como trampolín al siguiente argumento. Dato impresionante desperdiciado. Propuesta: o párrafo corto (cuántos, tiempo mediano, qué cambió técnicamente), o frase suelta (*"Decenas terminaron autónomamente, frente a ninguno en 2025"*) sin verbos de escena no pintada.
4. **Precisión técnica sacrificada por contundencia (A4).** Línea publicada: *"patas optimizadas para una sola tarea"* — el Unitree H1 es un humanoide general-purpose que corre bien, NO un robot-corredor dedicado. Un lector técnico de Reddit desmonta la frase en 30 segundos. Propuesta honesta que refuerza el mismo argumento: *"patas mecánicas que no sufren tendones, calambres ni ampollas, y un equipo entero detrás pendiente de su batería"*.
5. **Cierre desligado del leitmotiv (A5).** El artículo repite varias veces *"leer titulares despacio"* / *"leerlos con las cinco preguntas al lado"*, y luego cierra con *"Ese es, por cierto, el único trabajo que un humanoide no nos va a quitar en los próximos veinte años"* — kicker bueno pero sin atar el verbo recurrente. Propuesta: *"Leer titulares despacio. Ese es, por cierto, el único trabajo que un humanoide no nos va a quitar en los próximos veinte años."* La repetición literal remata.

### Incidente Bloque B — "Mejor robot aspirador 2026" (2026-04-19)

Reviewer externo detectó 7 problemas de *coherencia interna* del artículo consigo mismo:

1. **Recomendación contradictoria (B1).** 3 mensajes distintos sobre el "mejor global" en el mismo artículo: H2 sección 2 dice *"El mejor global: Roborock Qrevo Curv 2"* (pero *"disponible mayo 2026"*); caption de la tabla dice *"Dreame X50 Ultra — mejor compra global hoy"*; veredicto dice *"Dreame X50 Ultra para el comprador medio español"*. Lector escaneando no sabe cuál es. Solución: renombrar H2 Roborock a *"Lo más nuevo: Roborock Qrevo Curv 2 (disponible mayo 2026)"* y dejar Dreame como *"mejor global"* en todas partes.
2. **Promesa cuantitativa rota (B2).** Subtítulo promete *"6 modelos, 3 perfiles"*. El artículo entrega 6 perfiles (Global, Calidad-precio, Revelación, Mascotas, Samsung, Presupuesto) — no 3. Los 3 perfiles no se construyen en ningún sitio. Solución: subtítulo → *"6 modelos, 6 perfiles de uso"* O construir 3 perfiles reales al cierre.
3. **Nomenclatura inconsistente (B3).** Producto Cecotec aparece como *"Cecotec Conga 11090 Ultra Genesis"* (H2 + h3), *"Conga 11090 Ultra"* (cuerpo), *"Cecotec Conga 11090"* (tabla + veredicto). Tres formas del mismo producto. Solución: elegir una forma canónica y aplicarla.
4. **Criterio declarado incumplido sin justificación (B4).** Criterio 3 declarado al inicio: *"Toallita arrastrada no cuenta. Mopa giratoria, vibración sónica o rodillo."* El Samsung Combo AI Steam usa mopa vibratoria + vapor a las mopas en la base, no rodillo ni mopa giratoria. Solución: añadir 1 línea en el card Samsung justificando por qué entra igual (*"no cumple al 100% el criterio 3 por X, lo rescata el ecosistema SmartThings"*).
5. **Paridad visual rota (B5).** 6 productos finalistas, solo 3 con imagen inline (Roborock, Dreame, Ecovacs). Falta foto de MOVA, Samsung, Cecotec. Reviewer señaló solo el Samsung pero el problema afecta a 3 de 6. Solución: o añadir las 3 fotos, o documentar excepción en PASOS.md.
6. **Dato técnico cruzado incoherente (B6).** Línea publicada: *"MOVA V70 Ultra — 40.000 Pa de succión (cifra que Dreame oficialmente no reclama para su propio X50 Ultra, aunque el chasis es prácticamente hermano)"*. El X50 declara ~20.000 Pa; si son *"hermanos"*, los números no pueden ser ciertos a la vez. El propio texto admite la contradicción y la usa como argumento — lector de Reddit desmonta en 30 s. Solución: verificar ficha oficial MOVA V70 Ultra y corregir o reformular (*"comparte diseño con la gama Dreame Flex, aunque la succión declarada es superior"*).
7. **Precios de distinto tipo sin etiquetar (B7).** Línea publicada: *"1.074 € Amazon · 711 € refurbed.es"*. Refurbed.es vende reacondicionado — mezclar precio de nuevo con refurbed sin flag confunde. Solución: *"1.074 € nuevo en Amazon · 711 € reacondicionado en refurbed.es"*. Tres palabras que evitan el malentendido.

### How to apply

- **Orden de ejecución:** los 12 checks son la **última fase pre-output** en `/content-draft` (paso 8.9). Se corren DESPUÉS de anti-IA (§8.5), editorial-es (§8.5 bis), formato Beehiiv (§8.6), tangible (§8.7), banner (§8.8) y ANTES de § 9 Prohibiciones.
- **Formato de respuesta obligatorio en `PASOS.md`:** bloque `## Controles pre-publicación (§ editorial.md — 12 checks)` con cada check listado `[✅/❌/N/A] — [comentario de 1 línea]`.
- **Regla N/A:** solo válida cuando el check no aplica por estructura del artículo:
  - A2 N/A si no hay cifras contrarian en el artículo.
  - A3 N/A si no hay datos de asombro suficientes para merecer tratamiento especial.
  - A5 N/A si el artículo no repite verbo/frase (poco habitual en editorial ROBOHOGAR, pero posible en guías de compra).
  - B1 N/A en editoriales sin recomendación comparativa o ficción.
  - B2 N/A si no hay cifras de cobertura en título/subtítulo/intro.
  - B4 N/A si no hay lista explícita de criterios de selección.
  - B6 N/A si no hay asociaciones narrativas entre productos (*"hermano"*, *"sucesor"*, etc.).
  - B7 N/A si no se comparan datos de tipo mezclado.
  - Documentar POR QUÉ es N/A — no marcar por pereza.
- **Regla iterativa:** la lista crecerá. Cada nuevo incidente de feedback externo se evalúa contra los 12 checks; si revela un vicio no cubierto, se añade como A6/A7/B8/etc. sin romper numeración.
- **Auditoría ligera en `/post-publish`:** grep de B1 (*"mejor global"* cruzado), B2 (cifras promesa vs estructura entregada), B6 (*"hermano de"* / *"sucesor de"* + specs). Triaje igual que cero-fantasma: evidente+fix obvio → auto-fix + reportar; ambiguo → parar y consultar.

### Origen y memorias hermanas

- **Feedback Rafael 2026-04-20** sobre dos artículos consecutivos (maratón #8 del 2026-04-20 + aspiradores del 2026-04-19). Rafael validó: *"es interesante y acertado… iremos mejorando nuestra forma de escribir para ir afinando"*.
- **Complementa** (no sustituye) las reglas hermanas: `feedback_robohogar_no_phantom_references.md` (cero-fantasma), `feedback_robohogar_h2_no_bold.md` (formato Beehiiv), `feedback_article_voice_authority.md` (voz de autoridad propia), `feedback_mobile_first_copy.md` (mobile-first copy).
