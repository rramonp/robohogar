"""
data.py — Data structure del tangible "Hoja de Compra" para el skill /pdf-brand.

Este archivo es la fuente de datos estructurados que alimenta el template Jinja2
`cheatsheet.html.jinja2`. Convive con `contenido.md` (fuente humana legible).

Uso:
    uv run skills/pdf_brand/cli.py cheatsheet content/lead-magnets/hoja-compra/data.py

O bien, desde el command /pdf-brand, Claude extrae este dict directamente.

Cuando el contenido.md cambia, actualizar este data.py en paralelo (o al revés).
"""

data = {
    # ─── Identidad + versionado ───────────────────────────────
    "slug": "hoja-compra",
    "version": "v3",

    # ─── Portada ──────────────────────────────────────────────
    "title_big": "Hoja de",
    "title_small": "Compra",
    "subtitle": "10 preguntas para no pagar de más al comprar tu robot doméstico",
    "descriptor": "El documento que el vendedor no quiere que tengas. Aspiradores, cortacéspedes, mascotas-robot y afines.",
    "decorative_number": "10",
    "intro_paragraphs": [
        "En los últimos 6 meses en España se han vendido más robots domésticos que en los 3 años anteriores juntos. Entre 300 € y 2.000 €, con nombres que rotan cada 9 meses y claims de marketing que casi siempre mienten en el titular.",
        "Estas 10 preguntas son las que nos hacemos nosotros antes de comprar — y las que más nos han ahorrado dinero. Respóndelas en orden antes de darle al botón. <strong>Si fallas en 3 o más, no es el modelo para ti por mucho que la oferta diga -40 %.</strong>",
    ],

    # ─── Sección items — preguntas ────────────────────────────
    "items_section_title": "Las 10 preguntas",
    "items_section_lead": "Respóndelas en orden. La primera con <em>no</em> clara te dice que ese modelo no es para ti.",
    "items_section_lead_cont": "Las 5 que la gente olvida hasta que ya ha comprado.",
    "items_per_page": 5,
    "running_header_title": "Hoja de Compra ROBOHOGAR",

    "items": [
        # ─── PREGUNTAS 1-5 (página 2) ───
        {
            "num": 1,
            "title": "¿Cuántos m² reales va a limpiar / cortar?",
            "body_paragraphs": [
                "Mide con Google Maps el área del piso menos las habitaciones donde nunca entrará (trastero, habitación del bebé).",
            ],
            "bullets": [
                {"label": "<50 m²:", "text": "cualquier modelo sirve, no pagues premium."},
                {"label": "50-120 m²:", "text": "gama media alta."},
                {"label": ">120 m²:", "text": "autonomía + estación autolimpiable obligatorias."},
            ],
            "callout": {
                "label": "Trampa",
                "text": "la mayoría de robots no guarda mapas multi-planta bien. Si tienes 3 plantas, verifica antes — es el dolor número 1 reportado.",
            },
        },
        {
            "num": 2,
            "title": "¿Qué tipo de suelo — y en qué proporción?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "Uniforme", "text": "(baldosa <em>o</em> parquet <em>o</em> vinilo): cualquiera limpia bien."},
                {"label": "Mixto + alfombras gruesas:", "text": "mínimo 10.000 Pa."},
                {"label": "Parquet flotante + vinilo:", "text": 'mopa giratoria con dosificación de agua. Nada de "arrastra trapo mojado".'},
            ],
            "callout": {
                "label": "Atajo",
                "text": "con alfombras gruesas + perro, busca modelos con levantamiento automático de mopa al detectar alfombra.",
            },
        },
        {
            "num": 3,
            "title": "¿Mascotas y de qué tipo?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "Pelo corto:", "text": "rodillo antienredos razonable cumple."},
                {"label": "Perro pelo largo / gato persa:", "text": "rodillo antienredos obligatorio. Ecovacs OZMO Roller y Dreame nuevos lo hacen bien."},
                {"label": 'Perro que "arrastra":', "text": "pretratamiento de manchas con chorro de agua (Ecovacs X8 Pro Omni)."},
            ],
            "callout": {
                "label": "Truco ES",
                "text": 'en Amazon.es, filtra las reviews del modelo por "pelo largo". 10 min y ves si la gente se queja del rodillo trenzado.',
            },
        },
        {
            "num": 4,
            "title": "¿Qué autolimpia la estación?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "Básica:", "text": "vacía polvo. Bolsa cada 6-8 semanas."},
                {"label": "Avanzada:", "text": "+ autolava mopa. Rellenar agua cada 7-10 días."},
                {"label": "Premium:", "text": "+ auto-dosifica detergente + auto-rellena. Rellenar cada 2-3 semanas."},
            ],
            "callout": {
                "label": "Realidad",
                "text": "si vas a usarlo 2 veces/semana, la básica compensa. Si es diario, paga la avanzada o la premium — amortizas la diferencia en tiempo humano.",
            },
        },
        {
            "num": 5,
            "title": "¿Qué umbrales tengo en casa?",
            "body_paragraphs": [
                "Medir con regla. Sin esto, pifia garantizada.",
            ],
            "bullets": [
                {"label": "0-2 cm:", "text": "cualquier robot."},
                {"label": "2-4 cm:", "text": "Roborock y Dreame modernos."},
                {"label": "4-6 cm:", "text": "solo Dreame X50 Ultra (patas extensibles) y pocos más."},
                {"label": ">6 cm:", "text": "ningún robot de hoy."},
            ],
            "callout": {
                "label": "Dato ES",
                "text": "umbral típico de baño en España es 2,5-3 cm. Medir antes de pagar.",
            },
        },
        # ─── PREGUNTAS 6-10 (página 3) ───
        {
            "num": 6,
            "title": "¿App en español y soporte técnico ES?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "✅ Soporte ES fuerte:", "text": "Cecotec, Samsung, Xiaomi (con matices)."},
                {"label": "⚠️ Decente:", "text": "Roborock, Dreame, Ecovacs (via distribuidores; RMA 1-2 semanas)."},
                {"label": "❌ Débil/inexistente:", "text": "imports AliExpress, marcas sin entidad EU."},
            ],
            "callout": {
                "label": "Regla",
                "text": "si la app no está en español, asume que tampoco el manual ni el chat de soporte. En una avería la diferencia cuesta horas.",
            },
        },
        {
            "num": 7,
            "title": "¿Cuánto cuestan los consumibles al año?",
            "body_paragraphs": [
                "TCO a 3 años, no precio inicial:",
            ],
            "bullets": [
                {"label": "", "text": "Filtros HEPA: 15-30 €/año."},
                {"label": "", "text": "Mopas de recambio: 20-50 €/año."},
                {"label": "", "text": "Bolsas de polvo: 10-25 €/año."},
                {"label": "", "text": "Cepillo + rodillo: 15-40 €/año."},
            ],
            "callout": {
                "label": "Truco",
                "text": 'busca antes en Amazon.es <em>"[modelo] recambio mopa"</em>. Si no aparecen o son carísimos, descartar.',
            },
        },
        {
            "num": 8,
            "title": "¿Qué ecosistema smart home tengo?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "Alexa / Google:", "text": "casi todos compatibles."},
                {"label": "Apple HomeKit:", "text": "Roborock y Ecovacs premium."},
                {"label": "SmartThings:", "text": "Samsung nativo; resto via Matter (aún irregular)."},
                {"label": "Matter puro:", "text": "poco maduro en 2026. Espera 12 meses."},
            ],
            "callout": {
                "label": "Regla",
                "text": "no compres un robot con el único ecosistema que NO tienes. La integración siempre decepciona.",
            },
        },
        {
            "num": 9,
            "title": "¿Cuánto ruido y cuándo va a trabajar?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "<60 dB:", "text": "pasable en segundo plano."},
                {"label": "60-70 dB:", "text": "molesto pero usable."},
                {"label": ">70 dB:", "text": "solo cuando no estás."},
            ],
            "callout": {
                "label": "Cortacésped",
                "text": "muchos ayuntamientos ES prohíben motor eléctrico antes de 9:00 o después de 21:00. Verificar.",
            },
        },
        {
            "num": 10,
            "title": "¿Qué pasa si se rompe o me arrepiento?",
            "body_paragraphs": [],
            "bullets": [
                {"label": "Garantía EU:", "text": "2 años mínimo (3 en algunas CCAA). Exigirla."},
                {"label": "Amazon:", "text": "30 días sin preguntas. Aprovecha para probar en casa real."},
                {"label": "Refurbished", "text": "(refurbed.es, BackMarket): hasta -40 %, prueba 30 días."},
            ],
            "callout": {
                "label": "Señal",
                 'text': 'si la marca solo ofrece "canje completo" en vez de piezas sueltas, asume que a los 3 años es chatarra.',
            },
        },
    ],

    # ─── Back cover ───────────────────────────────────────────
    "backcover_title": "Y si ya compraste · y te equivocaste",
    "backcover_lead": "Plan de acción según lo lejos que estés del momento 0.",
    "anexo": {
        "title": "4 escenarios y qué hacer en cada uno",
        "steps": [
            {"label": "Aún dentro de 30 días:", "text": 'Amazon o tienda con devolución gratis. No esperes a "ver si me acostumbro".'},
            {"label": "Entre 30 días y 2 años:", "text": 'activar garantía ante cualquier fallo real. Documentar con vídeo. No "no me convence".'},
            {"label": "Fuera de garantía:", "text": "vender en Wallapop / Vinted Home antes de que baje más. Un robot de 2 años pierde 50-60 % de precio."},
            {"label": "Antes de repetir compra:", "text": "relee las 10 preguntas con lo aprendido. Probablemente fallaste en 2-3 — ahí está el dolor real."},
        ],
    },
    "close_hook": {
        "eyebrow": "Si te ha servido",
        "title": "Reenvía esta Hoja a quien esté mirando robots.",
        "subtitle": "No hace falta permiso. Lo único que pedimos es que le sirva al siguiente.",
    },
    "resources": [
        'Reviews y comparativas semanales → <a href="https://robohogar.com">robohogar.com</a>',
        "Responde al email de bienvenida con tu caso. Lo leemos todos.",
    ],
    "disclaimer": (
        "Documento editorial independiente. Las marcas citadas (Roborock, Dreame, Ecovacs, "
        "Samsung, Cecotec, Xiaomi y otras) pertenecen a sus respectivos propietarios. "
        "No patrocinado. Algunos links del contenido ROBOHOGAR pueden ser afiliados; "
        "ninguno en este PDF. Datos y precios verificados en abril 2026 — "
        "pueden cambiar en revisiones futuras."
    ),
}
