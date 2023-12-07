from .Idioma import Idioma

class Arabe(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # El árabe utiliza un alfabeto específico
        if all('\u0600' <= char <= '\u06FF' or char in "،؟" for char in texto):  # Verifica si el texto está en árabe
            return "Árabe"
        else:
            return "No es Árabe"

    def numeros_del_1_al_10(self):
        # Números del 1 al 10 en árabe
        return ["واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", "عشرة"]

    def traducir_a_espanol(self, texto):
        # Implementación simplificada
        traducciones = {
            "مرحبا": "Hola",
            "شكرا": "Gracias",
            "وداعا": "Adiós",
            "عفوا": "Disculpa"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]

    def frases_comunes(self):
        return {
            "مرحبا": "Hola",
            "شكرا": "Gracias",
            "وداعا": "Adiós",
            "عفوا": "Disculpa",
            "اسمي...": "Me llamo..."
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
