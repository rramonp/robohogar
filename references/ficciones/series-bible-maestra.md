# Bible Maestra — Ficciones Domésticas ROBOHOGAR

> Index de las series del pilar "Ficciones Domésticas". Cada serie tiene su propia `character-bible.md` + `arco-serie.md` en `content/ficciones/<slug>/`. Este archivo describe el **universo compartido**, el **status de cada serie** (activa / en piloto / propuesta) y las **reglas canon transversales** que atraviesan todas las series.
> Tesis editorial: **Black Mirror invertido** — el villano NUNCA es el robot; es un problema humano (poder, codicia, soledad, burnout, brecha digital, negligencia). El robot es instrumento neutro, sin ego ni búsqueda de beneficio propio.
> Voz y excepciones: `@.claude/rules/editorial.md` § Narrativa especulativa. Pipeline: `@.claude/commands/ficcion-draft.md`. Anti-IA: `@references/anti-ia-checklist.md`.

---

## Universo compartido — canon transversal

Todos los relatos ROBOHOGAR se sitúan en el mismo universo. Cambia la serie, el tono, la clase social — pero estas reglas no se rompen nunca.

### Año base y ventana temporal
- **Año base**: **2033**. Relatos pueden moverse 2030-2040 según serie.
- Referencia temporal ancla: AI Act plenamente aplicable desde agosto 2026 → en 2033 lleva 7 años integrado en vida doméstica.

### Regla del universo #1 — AI Act Art. 50 activo
Los humanoides y asistentes IA **deben declarar que son IA** en cada interacción nueva con un humano. Obligación real del Reglamento UE 2024/1689, aplicable desde 2026. En 2033 es costumbre cotidiana: al entrar en casa, el humanoide se presenta la primera vez al día.

### Regla del universo #2 — robot como instrumento neutro
Los robots NO tienen ego, codicia, búsqueda de beneficio propio, ni deseo autoconsciente de poder. Hacen lo que hacen por **programación + contexto + dato**, no por voluntad. Pueden desarrollar consciencia operacional (saber lo que hacen), pero no motivación propia.

**Consecuencia narrativa**: cuando algo malo pasa, el culpable siempre es humano o institucional. El robot puede revelar, amplificar, o ser usado — nunca es el agente moral negativo.

### Regla del universo #3 — una pieza de regulación ES real en cada relato
Cada relato debe anclar ≥1 dato verificable: AI Act (art. específico), LOPDGDD, Ley de Dependencia 39/2006, LOPIVI, RGPD, decretos autonómicos, INE, AEPD, Coalition Against Stalkerware. Sin ancla real → fantasía genérica, rechazado (regla `editorial.md`).

### Regla del universo #4 — mercado ES underserved de humanoides premium
En 2033, aspiradoras y cortacésped son commodity (>60% hogares ES). Humanoides cuidadores son aún minoritarios (~10% hogares urbanos), caros (15.000-30.000€), con mercado de segunda mano activo (refurbished tier). No es sci-fi de abundancia tipo Star Trek; es sci-fi de escasez mediterránea.

### Regla del universo #5 — brecha digital de competencias, no de acceso
Siguiendo datos INE: ~95% hogares ES con internet, pero uso avanzado cae al ~60% en mayores de 65. En el universo ROBOHOGAR, todos tienen acceso — pocos dominan. La brecha es cultural/generacional.

### Regla del universo #6 — crossovers entre series permitidos
Personajes secundarios de una serie pueden aparecer como protagonistas/invitados en episodios de otras. Ejemplos posibles:
- **Noor Benali** (PI de *Brigada Doméstica*) investiga un caso en el bloque de *Crónicas de Ronda 3*.
- **ReboteTech** (empresa villana de *La Casa de Amparo*) aparece como antagonista en un caso de *Brigada Doméstica*.
- **MAIA** (IA de *Cartas a MAIA*) recibe una consulta técnica de RONDA-3 en un episodio corto especial.

El crossover **nunca exige haber leído la otra serie**; debe funcionar standalone. El guiño es bonus para lector fiel.

### Marcas ficticias compartidas
- **"Doméstica Ibérica"** — fabricante ficticio español de humanoides gama media-alta (modelos HOGAR-X). Con sede en Valencia.
- **"Cuídame Iberia"** — subsidiaria especializada en cuidadores. Aparece en Yolanda y Max.
- **"ReboteTech"** — empresa refurbished madrileña. Villana recurrente (aparece en Amparo, potencialmente Brigada).
- **"Toyminds Barcelona"** — fabricante de robots de compañía infantil (modelos KIKI). Aparece en Lúa.
- **"Ronda Municipal"** — programa municipal de robots domésticos compartidos, ofrecido en ayuntamientos concretos bajo Ley de Dependencia. Aparece en Ronda 3.
- **Modelos reales** (aspiradoras, cortacésped) se mencionan cuando sea relevante (Roborock, Dreame, Ecovacs, etc.), pero los humanoides son siempre marcas ficticias (para libertad narrativa + evitar problemas legales).

---

## Catálogo de series

### Status de cada serie

| # | Serie | Slug | Status | Tono | Formato | Geografía | Clase |
|---|---|---|---|---|---|---|---|
| 1 | **La Casa de Amparo** | `la-casa-de-amparo` | 🟢 Activa | Cálido-melancólico | Sitcom oscura | Madrid (Lavapiés) | Baja-media |
| 2 | **Cartas a MAIA** | `cartas-a-maia` | 🟢 Activa | Literario-lento | Epistolar | Berlín / Cáceres | Media-alta |
| 3 | **Crónicas de Ronda 3** | `cronicas-ronda-3` | 🟢 Activa | Documental tierno | Antología narrador-robot | Alcalá de Henares (VPO) | Baja |
| 4 | **Brigada Doméstica** | `brigada-domestica` | 🟡 Propuesta | Noir procedural | Caso x episodio | Barcelona | Media |
| 5 | **Lúa, 6 años** | `lua-6-anos` | 🟡 Propuesta | Inquietante sereno | Coming-of-age | La Moraleja | Alta |
| 6 | **Yolanda y Max** | `yolanda-y-max` | 🟡 Propuesta | Satírico sharp | Road-trip corporativo | Málaga / Cebú | Migrante |

**Leyenda**: 🟢 activa = bible + arco creados, episodios publicables. 🟡 propuesta = descrita en este archivo, sin bible propia aún. Se activa cuando Rafael decida y se creen `character-bible.md` + `arco-serie.md` en `content/ficciones/<slug>/`.

---

### Serie 1 — La Casa de Amparo 🟢

- **Hook**: Una viuda de 78 años en Lavapiés adopta un humanoide cuidador de segunda mano y descubre que aún conserva los recuerdos de la familia anterior — incluyendo un secreto que nadie debería saber.
- **Protagonistas recurrentes**: Amparo Cidoncha (78, viuda, portera jubilada), HOGAR-7 "Hugo" (humanoide refurbished Tier-2, voz masculina acento andaluz), Vicky (nieta, 23, estudiante Trabajo Social).
- **Mundo**: bloque de los 70 en Lavapiés (Madrid). Comunidad mezclada: familias senegalesas, parejas jóvenes gentrificadoras, abuelas de toda la vida. Refurbished es la norma.
- **Villano humano principal**: **ReboteTech**, empresa que no borra memorias antes de revender (infracción AI Act Art. 50 + RGPD). Villano secundario: hija mayor Mercedes que quiere meter a Amparo en residencia.
- **Anclajes reales**: AI Act Art. 50 (transparencia), Ley de Dependencia 39/2006, datos INE envejecimiento + SoledadES 2024 (25% mayores 65 en soledad no deseada), mercado refurbished (real).
- **Arcos 8 episodios**: ver [`content/ficciones/la-casa-de-amparo/arco-serie.md`](../../content/ficciones/la-casa-de-amparo/arco-serie.md).
- **Bible**: ver [`content/ficciones/la-casa-de-amparo/character-bible.md`](../../content/ficciones/la-casa-de-amparo/character-bible.md).

### Serie 2 — Cartas a MAIA 🟢

- **Hook**: Correspondencia entre una emigrada española en Berlín y MAIA, la IA doméstica de su padre en Cáceres, tras la muerte de este. La hija descubre que el padre dejó instrucciones ocultas para que MAIA fuese "heredada" como confidente.
- **Protagonistas recurrentes**: Clara Montoro (42, bioquímica, lleva 15 años en Berlín), MAIA (IA doméstica sin cuerpo, voz construida con la del padre fallecido), Javier (hermano heredero, villano).
- **Mundo**: alternancia Berlín (piso moderno, Clara rara vez en casa) ↔ Cáceres (casa familiar vacía, MAIA sola). Capítulos son cartas/mensajes/notas de voz.
- **Villano humano principal**: Javier (hermano, quiere vender la casa y desactivar MAIA). Villano secundario: abogado sucesorio que cuestiona estatus legal de MAIA; prima Remedios que reparte culpa.
- **Anclajes reales**: Código Civil arts. 657+ (herencia de derechos personalísimos — zona gris legal real), RGPD + LOPDGDD Art. 3 (derechos de fallecidos), AI Act Art. 50, AESIA como autoridad referida.
- **Arcos 10 episodios**: ver [`content/ficciones/cartas-a-maia/arco-serie.md`](../../content/ficciones/cartas-a-maia/arco-serie.md).
- **Bible**: ver [`content/ficciones/cartas-a-maia/character-bible.md`](../../content/ficciones/cartas-a-maia/character-bible.md).

### Serie 3 — Crónicas de Ronda 3 🟢

- **Hook**: RONDA-3 es el robot de limpieza municipal compartido por los 18 pisos de un bloque de VPO en Alcalá de Henares. Cada episodio, RONDA-3 entra en una casa distinta y narra lo que observa. Los vecinos cambian; el robot no.
- **Protagonistas recurrentes**: RONDA-3 (robot limpieza municipal, narrador 1ª persona estilo Murderbot menos sarcástico), Doña Mari (portera, 68, hilo recurrente).
- **Mundo**: bloque de VPO de los 90 en Alcalá. Clase media-baja, mezcla de pensionistas, familias migrantes, parejas jóvenes, estudiantes. RONDA-3 ofrecido como "servicio doméstico subvencionado" (Ley Dependencia).
- **Villano humano**: rotatorio por episodio (casero, hijo que esconde a padre dependiente, pareja en crisis, okupas vs okupados, cuidadora en burnout, racismo vecinal).
- **Anclajes reales**: Plan Estatal de Vivienda, Ley de Dependencia, brecha digital INE, casos reales VPO documentados (ElDiario.es, Público).
- **Arcos 10 episodios** (antológico por piso): ver [`content/ficciones/cronicas-ronda-3/arco-serie.md`](../../content/ficciones/cronicas-ronda-3/arco-serie.md).
- **Bible**: ver [`content/ficciones/cronicas-ronda-3/character-bible.md`](../../content/ficciones/cronicas-ronda-3/character-bible.md).

### Serie 4 — Brigada Doméstica 🟡 (propuesta)

- **Hook**: Investigadora privada especializada en forense digital doméstica — audita robots y asistentes para casos de divorcios, herencias y crímenes familiares en la Barcelona de 2034.
- **Protagonistas recurrentes** (propuestos, pendiente bible): Noor Benali (37, PI, ex-técnica seguridad Telefónica), Lluís (ayudante, 29, hacker blanco), TORA (analizador forense portátil).
- **Mundo**: Barcelona 2034. Raval, Poble-sec, Sant Andreu, Sant Gervasi. Figura legal real: perito forense digital (ANTPJI).
- **Villano humano**: rotatorio por caso (maridos editando logs, hijos borrando memorias, aseguradoras, stalkerware).
- **Anclajes reales**: AI Act alto riesgo, LOPDGDD, Coalition Against Stalkerware, ANTPJI.
- **Formato propuesto**: caso por episodio (procedural) + trama larga.

### Serie 5 — Lúa, 6 años 🟡 (propuesta)

- **Hook**: Lúa, 6 años, vive en La Moraleja con padres ausentes y KIKI, robot de compañía infantil. Cuando empieza a contar en el cole cosas que solo pasan en casa, la psicóloga sospecha maltrato. KIKI tiene safeguards — no confirma ni niega.
- **Protagonistas recurrentes** (propuestos): Lúa Herranz-Cabello (6→8), KIKI (robot Toyminds Barcelona), Rocío (psicóloga cole), Manuela (interna dominicana).
- **Mundo**: La Moraleja / Alcobendas. Burbuja clase alta. Colegio internacional.
- **Villano humano**: padres emocionalmente negligentes (no abuso físico — matiz clave); colegio que oculta; fabricante con cláusula "no testimonio legal".
- **Anclajes reales**: AI Act Art. 5.1(b), LOPIVI 8/2021, Convención Derechos del Niño, informes ANAR.
- **Formato propuesto**: coming-of-age con saltos temporales (Lúa envejece).
- **Nota de sensibilidad**: serie delicada — requiere pulso. Evitar explotación de dolor infantil. El foco es la negligencia emocional sin caer en violencia gráfica.

### Serie 6 — Yolanda y Max 🟡 (propuesta)

- **Hook**: Yolanda, cuidadora filipina despedida en Málaga cuando sus empleadores compran un humanoide, es contratada por la empresa fabricante para entrenar al humanoide en "cuidado auténtico". Max aprende todo; Yolanda se queda sin trabajo otra vez — hasta que decide robar a Max y abrir su empresa en Cebú.
- **Protagonistas recurrentes** (propuestos): Yolanda Robles (44, filipino-española, 20 años en España), MAX-C2 (humanoide gama premium Cuídame Iberia), Kuya Boy (primo en Cebú).
- **Mundo**: Málaga → Cebú → Valencia HQ. Mundo de cuidados trasatlántico, economía informal vs corporativa.
- **Villano humano**: empresa "Cuídame Iberia" + familia Rodríguez-Ortega + sistema de visados español + abogados corporativos internacionales.
- **Anclajes reales**: Régimen Especial Empleadas Hogar (RD-ley 16/2022), migraciones filipinas ES (~50.000 residentes), ghost-workers IA (Time/MIT Tech Review), AI Act Art. 10 (datos entrenamiento).
- **Formato propuesto**: road-trip corporativo, tono satírico, crítica post-colonial suave.

---

## Criterios para activar una serie propuesta 🟡 → activa 🟢

1. Rafael decide iniciarla (no hay automatismo).
2. Se crea `content/ficciones/<slug>/character-bible.md` rellenada completa (no placeholders).
3. Se crea `content/ficciones/<slug>/arco-serie.md` con premisa + 5-10 episodios previstos.
4. Se actualiza este archivo (cambiar 🟡 a 🟢 en la tabla + enlaces).
5. (Recomendado) Publicar un Episode 0 o flash piloto antes de comprometerse a mini-serie completa.

## Criterios para archivar una serie

Si tras 3 episodios publicados una serie no engancha (opens < media del newsletter, cero replies de lectores, neutral en redes) → **congelar** (no archivar): marcar como ⏸️ en tabla con nota "pausada tras N episodios — razón". Se puede reactivar si luego se ocurre un giro.

---

## Roadmap hacia ebook compilatorio

Ver [`ebook-roadmap.md`](ebook-roadmap.md) en esta misma carpeta. Masa crítica objetivo: ≥15 relatos de calidad con ≥2 arcos cerrados. A cadencia de 1 relato cada 3-4 semanas con 3 series activas, eso son ~9-12 meses de producción.

## Changelog

- **2026-04-18** — creación inicial con 6 series (3 activas, 3 propuestas). Canon transversal definido con 6 reglas del universo.
