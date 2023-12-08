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

from Biblioteca.Clases import Arabe
from Biblioteca.Clases import Chino
from Biblioteca.Clases import Coreano
from Biblioteca.Clases import Japones
from Biblioteca.Clases import Nahuatl
from Biblioteca.Clases import Noruego
from Biblioteca.Clases import Polaco
from Biblioteca.Clases import Ruso
from Biblioteca.Clases import Tailandes

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

japones = Japones()

# Probar el método de identificación de escritura o dialecto
print(japones.identificar_escritura_o_dialecto("こんにちは"))  # Esperado: Hiragana
print(japones.identificar_escritura_o_dialecto("コンニチハ"))  # Esperado: Katakana
print(japones.identificar_escritura_o_dialecto("日本"))       # Esperado: Kanji

# Probar el método para obtener números del 1 al 10
print(japones.numeros_del_1_al_10())

# Probar el método para obtener los días de la semana
print(japones.dias_de_la_semana())

# Probar el método para obtener frases comunes
print(japones.frases_comunes())

# Probar el método para contar palabras en una oración
print(japones.contar_palabras_en_oracion("これはテストです"))  # Contar palabras en la oración

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

print("Pruebas unitarias de todos los idiomas exitosas!!")