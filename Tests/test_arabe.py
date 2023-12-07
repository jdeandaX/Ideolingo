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

from Biblioteca.Arabe import Arabe

class TestArabe(unittest.TestCase):
    def setUp(self):
        self.arabe = Arabe()

    def test_identificar_escritura_o_dialecto(self):
        resultado = self.arabe.identificar_escritura_o_dialecto("مرحبا")
        print(f"Test identificar_escritura_o_dialecto (مرحبا): {resultado}")
        self.assertEqual(resultado, "Árabe")

        resultado = self.arabe.identificar_escritura_o_dialecto("Hello")
        print(f"Test identificar_escritura_o_dialecto (Hello): {resultado}")
        self.assertEqual(resultado, "No es Árabe")

    def test_numeros_del_1_al_10(self):
        resultado = self.arabe.numeros_del_1_al_10()
        print(f"Test numeros_del_1_al_10: {resultado}")
        self.assertEqual(resultado, ["واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", "عشرة"])

    def test_traducir_a_espanol(self):
        resultado = self.arabe.traducir_a_espanol("مرحبا")
        print(f"Test traducir_a_espanol (مرحبا): {resultado}")
        self.assertEqual(resultado, "Hola")

        resultado = self.arabe.traducir_a_espanol("Desconocido")
        print(f"Test traducir_a_espanol (Desconocido): {resultado}")
        self.assertEqual(resultado, "Traducción no disponible")

    def test_dias_de_la_semana(self):
        resultado = self.arabe.dias_de_la_semana()
        print(f"Test dias_de_la_semana: {resultado}")
        self.assertEqual(resultado, ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"])

    def test_frases_comunes(self):
        frases = self.arabe.frases_comunes()
        print(f"Test frases_comunes: {frases}")
        self.assertEqual(frases["مرحبا"], "Hola")
        self.assertEqual(frases["شكرا"], "Gracias")

if __name__ == '__main__':
    unittest.main()
