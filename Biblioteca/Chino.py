from .Idioma import Idioma

class Chino(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # El chino utiliza caracteres chinos, que están en un rango específico de Unicode
        if all('\u4E00' <= char <= '\u9FFF' for char in texto):
            return "Chino"
        else:
            return "No es Chino"

    def numeros_del_1_al_10(self):
        return ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

    def traducir_a_espanol(self, texto):
        traducciones = {
            "你好": "Hola",
            "谢谢": "Gracias",
            "再见": "Adiós",
            "对不起": "Disculpa"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    def frases_comunes(self):
        return {
            "你好": "Hola",
            "谢谢": "Gracias",
            "再见": "Adiós",
            "对不起": "Disculpa",
            "我的名字是...": "Me llamo..."
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
