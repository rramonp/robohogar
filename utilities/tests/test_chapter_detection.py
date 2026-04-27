"""
Tests de regresión del detector de capítulos en `generate_audio.py`.

Cada caso de este archivo nace de un bug histórico real. Si en un futuro
alguien edita `CHAPTER_HEADING_RE`, `detect_chapters` o `assert_no_chapters_lost`
y rompe uno de estos casos → bug devuelto a producción. Los tests son la
red de seguridad permanente; ejecutar antes de mergear cambios al regex.

Ejecutar:
    python -m pytest utilities/tests/test_chapter_detection.py -v
o
    python -m unittest utilities.tests.test_chapter_detection

Cada test docstring describe el bug origen + slug + fecha. Cuando aparezca
el siguiente bug del regex (habrá uno, siempre lo hay), añadir un test
nuevo aquí ANTES de fixear el regex — la disciplina de "test primero" mata
la deuda.
"""

import sys
import unittest
from pathlib import Path

# Permitir importar generate_audio directamente al ejecutar el test
# desde el repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from generate_audio import (  # noqa: E402
    detect_chapters,
    assert_no_chapters_lost,
    LAX_CHAPTER_HEADING_RE,
    CHAPTER_HEADING_RE,
)


class DetectChaptersTests(unittest.TestCase):
    """Verifica detect_chapters sobre convenciones canónicas + casos de bug."""

    def test_pipo_heading_con_interrogacion(self):
        """Bug 2026-04-27 (slug pipo): `Parte cuatro. ¿Jugamos?` no matcheaba.

        El regex exigía `\\.\\s*$` y se rompía con `?`. El filtro post-regex
        de orden secuencial hacía break al saltar el 4 → solo 3/6 detectados
        en pipo. Fix: terminador ampliado a `[.?!]`. El título debe preservar
        el `?` semántico (no es ruido como sí lo es el `.`).
        """
        text = (
            "Parte uno. Las manos.\n\nFoo.\n\n"
            "Parte dos. El altar.\n\nBar.\n\n"
            "Parte tres. El circuito.\n\nBaz.\n\n"
            "Parte cuatro. ¿Jugamos?\n\nQux.\n\n"
            "Parte cinco. La llamada.\n\nQuux.\n\n"
            "Parte seis. El termo.\n\nFin.\n"
        )
        chs = detect_chapters(text)
        self.assertEqual(len(chs), 6, f"esperados 6 capítulos, obtenidos {len(chs)}: {chs}")
        self.assertEqual(chs[3]["title"], "¿Jugamos?", "el `?` debe preservarse en el título")
        self.assertEqual(chs[5]["title"], "El termo", "capítulo 6 debe llegar (el filtro post-regex no debe haber roto la secuencia)")

    def test_heading_con_exclamacion(self):
        """Hermanas regla del fix pipo: `!` también se permite como terminador."""
        text = (
            "Parte uno. Llegada.\n\nFoo.\n\n"
            "Parte dos. ¡Vámonos!\n\nFin.\n"
        )
        chs = detect_chapters(text)
        self.assertEqual(len(chs), 2)
        self.assertEqual(chs[1]["title"], "¡Vámonos!", "`!` debe sobrevivir en el título")

    def test_heading_con_coma_es_legitimo(self):
        """Bug 2026-04-26 (slug el-operador-nocturno): regex con `[^,;:\\n]`
        rechazaba 3 headings con coma legítima → 0 detectados, fallback "Relato".
        Fix terciario: regex pasó a `[^;:\\n]` (sí coma, no `;:`).
        """
        text = (
            "Parte uno. Madrid, un martes a las tres y catorce.\n\nFoo.\n\n"
            "Parte dos. Manila, el mismo martes, las nueve y catorce.\n\nBar.\n\n"
            "Parte tres. Madrid, sábado, doce y seis del mediodía.\n\nFin.\n"
        )
        chs = detect_chapters(text)
        self.assertEqual(len(chs), 3, f"3 headings con coma deben matchear, no {len(chs)}")
        self.assertIn("Madrid", chs[0]["title"])
        self.assertIn("Manila", chs[1]["title"])

    def test_heading_canon_corto_sin_prefijo_parte(self):
        """Convención canónica corta: `Uno. La cocina.` (sin `Parte ` delante)."""
        text = (
            "Uno. La cocina.\n\nFoo.\n\n"
            "Dos. La hermana.\n\nFin.\n"
        )
        chs = detect_chapters(text)
        self.assertEqual(len(chs), 2)
        self.assertEqual(chs[0]["title"], "La cocina")

    def test_parrafo_con_ordinal_NO_matchea(self):
        """Bug 2026-04-25 (slug papa-desde-singapur): regex sin límite de
        título capturaba párrafos enteros que empiezan por `Tres meses antes`.
        Fix: límite 1-60 chars en el título + filtro post-regex de orden.
        """
        # Párrafo narrativo que empieza por ordinal pero NO es heading.
        # No matchea porque el "punto final" del párrafo está más allá de 60 chars.
        text = (
            "Parte uno. Llegada.\n\n"
            "Tres meses antes de aquel verano, Manuel pensaba que la vida tenía "
            "un orden razonable y que las cosas que dejaba en el monte se "
            "quedaban en el monte.\n\n"
            "Fin.\n"
        )
        chs = detect_chapters(text)
        self.assertEqual(len(chs), 1, f"el párrafo `Tres meses antes...` NO debe matchear (chs detectados: {chs})")

    def test_orden_secuencial_recorta_falsos_positivos(self):
        """El filtro post-regex descarta capítulos fuera de orden.

        Si el regex captura un `Cinco.` espurio sin haber pasado por
        1-4 → break en el filtro de orden, ignora el 5.
        """
        # Heading legítimo 1 + falso positivo "Cinco. ..." en línea propia.
        text = (
            "Parte uno. Apertura.\n\nFoo.\n\n"
            "Cinco. Capítulos antes había pensado todo lo contrario.\n"  # esto no debería existir como heading legítimo, pero el regex laxo podría pillarlo
            "Algo más.\n"
        )
        chs = detect_chapters(text)
        # Sólo el 1 vale; el "Cinco." se descarta por orden.
        self.assertEqual(len(chs), 1)
        self.assertEqual(chs[0]["number"], 1)


class AssertNoChaptersLostTests(unittest.TestCase):
    """Verifica el guard pre-TTS — abort si laxo > estricto."""

    def test_match_perfecto_no_aborta(self):
        """Caso happy: laxo y estricto detectan los mismos headings."""
        text = (
            "Parte uno. Las manos.\n\nFoo.\n\n"
            "Parte dos. El altar.\n\nFin.\n"
        )
        # No raise.
        assert_no_chapters_lost(text)

    def test_pipo_con_interrogacion_no_aborta_ahora_que_regex_arreglado(self):
        """Tras el fix de `?`/`!` el guard NO debe abortar en pipo."""
        text = (
            "Parte uno. Las manos.\n\nFoo.\n\n"
            "Parte dos. El altar.\n\nBar.\n\n"
            "Parte tres. El circuito.\n\nBaz.\n\n"
            "Parte cuatro. ¿Jugamos?\n\nQux.\n\n"
            "Parte cinco. La llamada.\n\nQuux.\n\n"
            "Parte seis. El termo.\n\nFin.\n"
        )
        assert_no_chapters_lost(text)

    def test_aborta_si_estricto_se_queda_corto(self):
        """Simulación de bug futuro: si una convención nueva escapa al regex
        estricto pero el laxo la ve, debe abortar con SystemExit listando
        los headings perdidos. Esto blinda contra regression del propio fix.
        """
        # Construimos un caso adversarial: heading con terminador inválido
        # para el estricto actual (un `;` por ejemplo, que el regex prohíbe).
        # El laxo no exige terminador concreto, así que sí lo ve.
        text = (
            "Parte uno. Apertura.\n\nFoo.\n\n"
            "Parte dos. Cierre con punto y coma;\n\nFin.\n"
        )
        # Verificación previa: laxo lo ve, estricto no.
        lax_count = len(LAX_CHAPTER_HEADING_RE.findall(text))
        strict_count = len(detect_chapters(text))
        self.assertGreater(lax_count, strict_count,
                           "el setup del test asume convención nueva fuera del estricto; ajustar si el regex estricto se amplía a `;`")
        # El guard debe abortar con SystemExit.
        with self.assertRaises(SystemExit) as ctx:
            assert_no_chapters_lost(text)
        self.assertIn("Headings perdidos", str(ctx.exception))


class RealAudiolibrosRegressionTests(unittest.TestCase):
    """Carga los `audiolibro.txt` reales del repo y verifica el conteo
    contra el número esperado de capítulos. Si en el futuro alguien edita
    el regex y rompe los relatos publicados, este test lo detecta.
    """

    REPO_ROOT = Path(__file__).resolve().parent.parent.parent

    EXPECTED = {
        # slug → número de capítulos esperado
        "pipo": 6,
        "la-objecion": 9,
        "el-operador-nocturno": 3,
        "el-que-viene-a-tomar-cafe": 3,
        "la-canguro": None,  # opcional: comprobar que está si existe
    }

    def test_audiolibros_publicados_detectan_todos_capitulos(self):
        for slug, expected in self.EXPECTED.items():
            txt_path = self.REPO_ROOT / "content" / "ficciones" / "_one-shots" / slug / "audiolibro.txt"
            if not txt_path.exists():
                # Algunos slugs pueden no tener audiolibro.txt (relato sin audio o legacy).
                if expected is None:
                    continue
                self.fail(f"falta {txt_path} pero EXPECTED dice {expected} capítulos")
            text = txt_path.read_text(encoding="utf-8")
            chs = detect_chapters(text)
            if expected is None:
                continue
            self.assertEqual(
                len(chs), expected,
                f"{slug}: esperados {expected} capítulos, detectados {len(chs)} → {[c['title'] for c in chs]}"
            )
            # Y el guard pre-TTS no debe abortar.
            assert_no_chapters_lost(text)


if __name__ == "__main__":
    unittest.main()
