# Write With AI — Knowledge Base ES

Este directorio contiene los playbooks de [Nicolas Cole / Write With AI](https://writewithai.substack.com), destilados y aplicados a ROBOHOGAR.

## ⚠️ Aviso de verificación cruzada

Todo este contenido es **US/EN traducido y adaptado**. Write With AI es la referencia principal para pipeline editorial, pero los patterns de copywriting US no siempre encajan en el ecosistema newsletter ES.

**Antes de adoptar literalmente una frase, longitud, saludo, verbo CTA, subject line o microcopy de estos archivos, verificar contra:**

→ [`../research-newsletters-es-2026-04-19.md`](../research-newsletters-es-2026-04-19.md)

Research empírico sobre 20 newsletters ES de éxito (Kloshletter, Suma Positiva, Xataka, Genbeta, EOM, elDiario, Marketing4eCommerce, Newtral, Cincominutos, Ecotechers, Tendenci@s, Escribe, IA en Español…) con glosario ES↔EN y patterns validados por evidencia.

## Divergencias conocidas entre US/WWA y ES real

| Elemento | WWA dice (EN/US) | Realidad ES (auditada) | Regla ROBOHOGAR |
|---|---|---|---|
| Subject line | ≤25 chars | 20-45 chars, preferencia ≤35 | `@rules/newsletter.md` |
| Verbo CTA | `Sign me up` · `Join N+ readers` · `Me apunto` | `Suscríbete` (61%) / `Apúntate` (28%) | `@rules/tangibles.md § Microcopy` |
| Trust-line microcopy | `Unsubscribe anytime` · `No spam` | `Cancela cuando quieras` · política privacidad explícita | `@rules/tangibles.md § Microcopy` |
| Apertura body email | `Hi X,` + `hope you're well` | Entrada directa · `Buenos días.` | `@rules/editorial.md § Apertura` |
| Cierre body email | `Cheers` · `Best` | Firma + tagline · `Un abrazo` (solo personal) | `@rules/editorial.md § Apertura` |
| Separador microcopy | middot `·` en cascada | Punto final · coma · dos puntos | `@rules/tangibles.md § Microcopy` |
| Em-dash ` — ` en trust-line | Normalizado US | Tic anglo · 0/20 ES | `@rules/editorial.md § Apertura` |
| Palabra nuclear | "newsletter" | "newsletter" (83%) · "boletín" en medios grandes | `@rules/newsletter.md § Palabra nuclear` |
| Tratamiento | `you` | `tú` + plural editorial. Nunca `vosotros` ni `usted` | `@rules/editorial.md § Voz` |
| "Tangible" como palabra | Jerga growth US (Nicolas Cole) | No existe en copy público ES | `@rules/tangibles.md § Reglas operativas` |

## Cuándo seguir WWA sin ajuste

- Arquitectura de funnel (curiosity gap, paid blueprint, cliffhanger pattern).
- Frameworks editoriales (1-3-1, Palahniuk thought verbs).
- Principios de lead magnet (pivote Cole 2026 "tangible = producto").
- Métricas objetivo (open rate, CTR benchmarks).

## Cuándo NO seguir WWA literal

- Copywriting exacto (saludos, CTAs, trust-lines, subjects) — **verificar ES primero**.
- Longitudes basadas en inglés monosilábico (headlines, bullet points).
- Registros de trato (US asume "you" neutro; ES requiere decisión tú/usted/plural).
- Anglicismos consolidados en EN sin equivalente natural ES (`lead magnet`, `welcome flow`, `opt-in`).

## Cambio este archivo cuando

- Se detecta un nuevo pattern US que falla al aplicarse al ES real → añadir fila a la tabla.
- Se audita un nuevo batch de newsletters ES y se valida/invalida una regla existente.
- Skill del pipeline incumple una regla por leer WWA literal sin consultar el research ES.
