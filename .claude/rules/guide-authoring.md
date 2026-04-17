# Guide Authoring — documentar como invocación lista para usar

Al añadir contenido a `docs/guia-implementacion.md` (o cualquier documento de workflow del proyecto), incluir SIEMPRE:

1. **Frase trigger exacta** que Rafael debe pronunciar para retomar/invocar el workflow — en tabla o bloque destacado al inicio de la fase/sección
2. **Prompts literales** para cada skill/comando invocable, ej: `/pdf-brand guia "tema" 1-pagina guias-compra`
3. **Inputs esperados** de cada invocación (argumentos obligatorios + opcionales, tipos aceptados)
4. **Outputs esperados** en rutas concretas del repo o descripción exacta de lo que devuelve Claude

## Por qué

Rafael trabaja en sesiones espaciadas (3-5 h/semana). Entre sesiones pasa días o semanas. Cuando vuelve, la guía debe ser autosuficiente — debe poder leer una fase y saber EXACTAMENTE qué decir para que Claude retome desde el punto correcto.

Sin triggers documentados, cada retoma requiere contexto adicional, fricción, pérdida de tiempo.

## Patrón estándar (ejemplo)

```markdown
### 📌 Frases trigger para retomar

| Qué quiero retomar | Frase exacta |
|---|---|
| Arrancar la fase | **"Retomamos <nombre-plan> — empezamos FASE A"** |
| Siguiente paso | **"Retomamos <nombre-plan> — siguiente paso"** |
| Ver estado | **"¿En qué fase de <nombre-plan> estamos?"** |

Con esas frases, Claude debe:
1. Leer este bloque + el plan file correspondiente
2. Revisar qué checkboxes están marcados
3. Retomar en el primer paso pendiente
```

## Anti-patterns

- ❌ Referencias vagas: "ejecuta el skill" → ✅ "ejecuta `/pdf-brand guia ...`"
- ❌ Outputs abstractos: "genera un PDF" → ✅ "genera `assets/lead-magnets/<slug>-v1.pdf`"
- ❌ Pasos sin invocación: "Rafael revisa el borrador" → ✅ "Rafael revisa `content/articulos/<slug>/borrador.html` y ejecuta `/post-publish <URL>`"

## Precedentes del repo

- Digest research 2026-04-17: bloque "📌 Recomendación ROBOHOGAR — Para retomar" con frase exacta al principio
- FASE 4B y 4C `guia-implementacion.md`: 4 frases trigger cada una (una por sub-fase + una de estado)
