import unittest
import sys
import os

# Obtener la ruta absoluta del archivo actual (main.py)
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Calcular la ruta del directorio padre, que es 'IDEOLINGO'
ruta_directorio_padre = os.path.abspath(os.path.join(ruta_actual, '..'))

# Añadir esa ruta a sys.path
if ruta_directorio_padre not in sys.path:
    sys.path.insert(0, ruta_directorio_padre)

from Biblioteca.Coreano import Coreano

class TestCoreano(unittest.TestCase):
    def setUp(self):
        self.coreano = Coreano()

    def test_identificar_escritura_o_dialecto(self):
        self.assertEqual(self.coreano.identificar_escritura_o_dialecto("안녕하세요"), "Hangul")
        self.assertEqual(self.coreano.identificar_escritura_o_dialecto("Hello"), "No es Coreano")

    def test_numeros_del_1_al_10(self):
        self.assertEqual(self.coreano.numeros_del_1_al_10(), ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십"])

    def test_traducir_a_espanol(self):
        self.assertEqual(self.coreano.traducir_a_espanol("안녕하세요"), "Hola")
        self.assertEqual(self.coreano.traducir_a_espanol("감사합니다"), "Gracias")
        self.assertEqual(self.coreano.traducir_a_espanol("Desconocido"), "Traducción no disponible")

    def test_dias_de_la_semana(self):
        self.assertEqual(self.coreano.dias_de_la_semana(), ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"])

    def test_frases_comunes(self):
        frases = self.coreano.frases_comunes()
        self.assertEqual(frases["안녕하세요"], "Hola")
        self.assertEqual(frases["감사합니다"], "Gracias")
        self.assertEqual(frases.get("Desconocido", "No incluido"), "No incluido")

    # Puedes agregar más pruebas según sea necesario

if __name__ == '__main__':
    unittest.main()
