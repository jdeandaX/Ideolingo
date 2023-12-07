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

from Biblioteca.Polaco import Polaco

class TestPolaco(unittest.TestCase):
    def setUp(self):
        self.polaco = Polaco()

    def test_identificar_escritura_o_dialecto(self):
        self.assertEqual(self.polaco.identificar_escritura_o_dialecto("Cześć"), "Polaco")
        self.assertEqual(self.polaco.identificar_escritura_o_dialecto("Hello"), "No es Polaco")

    def test_numeros_del_1_al_10(self):
        self.assertEqual(self.polaco.numeros_del_1_al_10(), ["jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć", "dziesięć"])

    def test_traducir_a_espanol(self):
        self.assertEqual(self.polaco.traducir_a_espanol("Cześć"), "Hola")
        self.assertEqual(self.polaco.traducir_a_espanol("Desconocido"), "Traducción no disponible")

    def test_dias_de_la_semana(self):
        self.assertEqual(self.polaco.dias_de_la_semana(), ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"])

    def test_frases_comunes(self):
        frases = self.polaco.frases_comunes()
        self.assertEqual(frases["Cześć"], "Hola")
        self.assertEqual(frases["Dziękuję"], "Gracias")
        self.assertEqual(frases.get("Desconocido", "No incluido"), "No incluido")

if __name__ == '__main__':
    unittest.main()
