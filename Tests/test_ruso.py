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

from Biblioteca.Ruso import Ruso

class TestRuso(unittest.TestCase):
    def setUp(self):
        self.ruso = Ruso()

    def test_identificar_escritura_o_dialecto(self):
        self.assertEqual(self.ruso.identificar_escritura_o_dialecto("Привет"), "Cirílico")
        self.assertEqual(self.ruso.identificar_escritura_o_dialecto("Hello"), "No es Ruso")

    def test_numeros_del_1_al_10(self):
        self.assertEqual(self.ruso.numeros_del_1_al_10(), ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"])

    def test_traducir_a_espanol(self):
        self.assertEqual(self.ruso.traducir_a_espanol("Привет"), "Hola")
        self.assertEqual(self.ruso.traducir_a_espanol("Спасибо"), "Gracias")
        self.assertEqual(self.ruso.traducir_a_espanol("Desconocido"), "Traducción no disponible")

    def test_dias_de_la_semana(self):
        self.assertEqual(self.ruso.dias_de_la_semana(), ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"])

    def test_frases_comunes(self):
        frases = self.ruso.frases_comunes()
        self.assertEqual(frases["Привет"], "Hola")
        self.assertEqual(frases["Спасибо"], "Gracias")
        self.assertEqual(frases.get("Desconocido", "No incluido"), "No incluido")

    # Puedes agregar más pruebas según sea necesario

if __name__ == '__main__':
    unittest.main()
