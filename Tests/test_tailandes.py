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

from Biblioteca.Tailandes import Tailandes

class TestTailandes(unittest.TestCase):
    def setUp(self):
        self.tailandes = Tailandes()

    def test_identificar_escritura_o_dialecto(self):
        resultado = self.tailandes.identificar_escritura_o_dialecto("สวัสดี")
        print(f"Test identificar_escritura_o_dialecto (สวัสดี): {resultado}")
        self.assertEqual(resultado, "Tailandés")

        resultado = self.tailandes.identificar_escritura_o_dialecto("Hello")
        print(f"Test identificar_escritura_o_dialecto (Hello): {resultado}")
        self.assertEqual(resultado, "No es Tailandés")

    def test_numeros_del_1_al_10(self):
        resultado = self.tailandes.numeros_del_1_al_10()
        print(f"Test numeros_del_1_al_10: {resultado}")
        self.assertEqual(resultado, ["หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"])

    def test_traducir_a_espanol(self):
        resultado = self.tailandes.traducir_a_espanol("สวัสดี")
        print(f"Test traducir_a_espanol (สวัสดี): {resultado}")
        self.assertEqual(resultado, "Hola")

        resultado = self.tailandes.traducir_a_espanol("Desconocido")
        print(f"Test traducir_a_espanol (Desconocido): {resultado}")
        self.assertEqual(resultado, "Traducción no disponible")

    def test_dias_de_la_semana(self):
        resultado = self.tailandes.dias_de_la_semana()
        print(f"Test dias_de_la_semana: {resultado}")
        self.assertEqual(resultado, ["วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์", "วันอาทิตย์"])

    def test_frases_comunes(self):
        frases = self.tailandes.frases_comunes()
        print(f"Test frases_comunes: {frases}")
        self.assertEqual(frases["สวัสดี"], "Hola")
        self.assertEqual(frases["ขอบคุณ"], "Gracias")

if __name__ == '__main__':
    unittest.main()
