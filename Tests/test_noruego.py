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

from Biblioteca.Noruego import Noruego

class TestNoruego(unittest.TestCase):
    def setUp(self):
        self.noruego = Noruego()

    def test_identificar_escritura_o_dialecto(self):
        resultado = self.noruego.identificar_escritura_o_dialecto("Hei")
        print(f"Test identificar_escritura_o_dialecto (Hei): {resultado}")
        self.assertEqual(resultado, "Noruego")

        resultado = self.noruego.identificar_escritura_o_dialecto("Hello")
        print(f"Test identificar_escritura_o_dialecto (Hello): {resultado}")
        self.assertEqual(resultado, "No es Noruego")

    def test_numeros_del_1_al_10(self):
        resultado = self.noruego.numeros_del_1_al_10()
        print(f"Test numeros_del_1_al_10: {resultado}")
        self.assertEqual(resultado, ["en", "to", "tre", "fire", "fem", "seks", "sju", "åtte", "ni", "ti"])

    def test_traducir_a_espanol(self):
        resultado = self.noruego.traducir_a_espanol("Hei")
        print(f"Test traducir_a_espanol (Hei): {resultado}")
        self.assertEqual(resultado, "Hola")

        resultado = self.noruego.traducir_a_espanol("Desconocido")
        print(f"Test traducir_a_espanol (Desconocido): {resultado}")
        self.assertEqual(resultado, "Traducción no disponible")

    def test_dias_de_la_semana(self):
        resultado = self.noruego.dias_de_la_semana()
        print(f"Test dias_de_la_semana: {resultado}")
        self.assertEqual(resultado, ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"])

    def test_frases_comunes(self):
        frases = self.noruego.frases_comunes()
        print(f"Test frases_comunes: {frases}")
        self.assertEqual(frases["Hei"], "Hola")
        self.assertEqual(frases["Takk"], "Gracias")

if __name__ == '__main__':
    unittest.main()
