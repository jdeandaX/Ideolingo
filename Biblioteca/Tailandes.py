from .Idioma import Idioma

class Tailandes(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # El tailandés utiliza un rango específico de caracteres Unicode
        if all('\u0E00' <= char <= '\u0E7F' for char in texto):
            return "Tailandés"
        else:
            return "No es Tailandés"

    def numeros_del_1_al_10(self):
        return ["หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]

    def traducir_a_espanol(self, texto):
        traducciones = {
            "สวัสดี": "Hola",
            "ขอบคุณ": "Gracias",
            "ลาก่อน": "Adiós",
            "ขอโทษ": "Disculpa"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์", "วันอาทิตย์"]

    def frases_comunes(self):
        return {
            "สวัสดี": "Hola",
            "ขอบคุณ": "Gracias",
            "ลาก่อน": "Adiós",
            "ขอโทษ": "Disculpa",
            "ผมชื่อ...": "Me llamo..."  # Nota: "ผมชื่อ" es formal para hombres
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
