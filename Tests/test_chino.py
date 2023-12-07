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

from Biblioteca.Chino import Chino

class TestChino(unittest.TestCase):
    def setUp(self):
        self.chino = Chino()

    def test_identificar_escritura_o_dialecto(self):
        resultado = self.chino.identificar_escritura_o_dialecto("你好")
        print(f"Test identificar_escritura_o_dialecto (你好): {resultado}")
        self.assertEqual(resultado, "Chino")

        resultado = self.chino.identificar_escritura_o_dialecto("Hello")
        print(f"Test identificar_escritura_o_dialecto (Hello): {resultado}")
        self.assertEqual(resultado, "No es Chino")

    def test_numeros_del_1_al_10(self):
        resultado = self.chino.numeros_del_1_al_10()
        print(f"Test numeros_del_1_al_10: {resultado}")
        self.assertEqual(resultado, ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"])

    def test_traducir_a_espanol(self):
        resultado = self.chino.traducir_a_espanol("你好")
        print(f"Test traducir_a_espanol (你好): {resultado}")
        self.assertEqual(resultado, "Hola")

        resultado = self.chino.traducir_a_espanol("Desconocido")
        print(f"Test traducir_a_espanol (Desconocido): {resultado}")
        self.assertEqual(resultado, "Traducción no disponible")

    def test_dias_de_la_semana(self):
        resultado = self.chino.dias_de_la_semana()
        print(f"Test dias_de_la_semana: {resultado}")
        self.assertEqual(resultado, ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"])

    def test_frases_comunes(self):
        frases = self.chino.frases_comunes()
        print(f"Test frases_comunes: {frases}")
        self.assertEqual(frases["你好"], "Hola")
        self.assertEqual(frases["谢谢"], "Gracias")

if __name__ == '__main__':
    unittest.main()
