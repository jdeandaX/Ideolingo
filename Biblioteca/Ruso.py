from .Idioma import Idioma

class Ruso(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # El ruso utiliza el alfabeto cirílico
        if all('А' <= char <= 'я' for char in texto):  # Verifica si el texto está en cirílico
            return "Cirílico"
        else:
            return "No es Ruso"

    def numeros_del_1_al_10(self):
        return ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]

    def traducir_a_espanol(self, texto):
        # Implementación simplificada
        traducciones = {
            "Привет": "Hola",
            "Спасибо": "Gracias",
            "До свидания": "Adiós",
            "Извините": "Lo siento"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

    def frases_comunes(self):
        return {
            "Привет": "Hola",
            "Спасибо": "Gracias",
            "До свидания": "Adiós",
            "Извините": "Lo siento",
            "Меня зовут...": "Me llamo..."
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
