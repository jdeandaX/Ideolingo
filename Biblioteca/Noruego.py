from .Idioma import Idioma

class Noruego(Idioma):
    def identificar_escritura_o_dialecto(self, texto):
        # El noruego utiliza el alfabeto latino con algunos caracteres adicionales
        if all(char.isalpha() or char in "æøåÆØÅ" for char in texto):  # Verifica si el texto está en noruego
            return "Noruego"
        else:
            return "No es Noruego"

    def numeros_del_1_al_10(self):
        return ["en", "to", "tre", "fire", "fem", "seks", "sju", "åtte", "ni", "ti"]

    def traducir_a_espanol(self, texto):
        # Implementación simplificada
        traducciones = {
            "Hei": "Hola",
            "Takk": "Gracias",
            "Farvel": "Adiós",
            "Unnskyld": "Disculpa"
        }
        return traducciones.get(texto, "Traducción no disponible")

    def dias_de_la_semana(self):
        return ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

    def frases_comunes(self):
        return {
            "Hei": "Hola",
            "Takk": "Gracias",
            "Farvel": "Adiós",
            "Unnskyld": "Disculpa",
            "Jeg heter...": "Me llamo..."
        }

    # El método contar_palabras_en_oracion se hereda directamente de Idioma y no necesita ser modificado
