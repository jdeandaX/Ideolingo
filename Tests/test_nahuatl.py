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

from Biblioteca.Nahuatl import Nahuatl

class TestNahuatl(unittest.TestCase):
    def setUp(self):
        self.nahuatl = Nahuatl()

    def test_identificar_escritura_o_dialecto(self):
        self.assertEqual(self.nahuatl.identificar_escritura_o_dialecto("tlacatl"), "Náhuatl")
        self.assertEqual(self.nahuatl.identificar_escritura_o_dialecto("persona"), "No es Náhuatl")

    def test_numeros_del_1_al_10(self):
        self.assertEqual(self.nahuatl.numeros_del_1_al_10(), ["ce", "ome", "yei", "nahui", "macuilli", "chicuace", "chicome", "chicuei", "chicnahui", "mahtlactli"])

    def test_traducir_a_espanol(self):
        self.assertEqual(self.nahuatl.traducir_a_espanol("Niltze"), "Hola")
        self.assertEqual(self.nahuatl.traducir_a_espanol("Desconocido"), "Traducción no disponible")

    def test_dias_de_la_semana(self):
        self.assertEqual(self.nahuatl.dias_de_la_semana(), ["Tonalpohualli", "Tonalteteuctli", "Tonalteteuctontli", "Tonalteteuctome", "Tonalteteuctontli", "Tonalteteuctomahtlactli", "Tonalteteuctome"])

    def test_frases_comunes(self):
        frases = self.nahuatl.frases_comunes()
        self.assertEqual(frases["Niltze"], "Hola")
        self.assertEqual(frases["Tlazohcamati"], "Gracias")
        self.assertEqual(frases.get("Desconocido", "No incluido"), "No incluido")

if __name__ == '__main__':
    unittest.main()
