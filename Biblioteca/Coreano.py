from .Idioma import Idioma

class Coreano(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # Simplificado para el ejemplo
        if any('\uAC00' <= char <= '\uD7A3' for char in texto):  # Hangul
            return "Hangul"
        else:
            return "No es Coreano"

    def numeros_del_1_al_10(self):
        return ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십"]

    def traducir_a_espanol(self, texto):
        # Implementación simplificada
        traducciones = {
            "안녕하세요": "Hola",
            "감사합니다": "Gracias",
            "잘 있어요": "Adiós",
            "죄송합니다": "Lo siento"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

    def frases_comunes(self):
        return {
            "안녕하세요": "Hola",
            "감사합니다": "Gracias",
            "잘 있어요": "Adiós",
            "죄송합니다": "Lo siento",
            "제 이름은...입니다": "Mi nombre es..."
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
