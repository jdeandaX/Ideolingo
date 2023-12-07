class Idioma:
    def identificar_escritura_o_dialecto(self, texto):
        # Implementación genérica o método abstracto
        raise NotImplementedError("Método para identificar escritura o dialecto no implementado.")

    def numeros_del_1_al_10(self):
        # Devuelve una lista o diccionario de números del 1 al 10 en el idioma específico
        raise NotImplementedError("Método para números del 1 al 10 no implementado.")

    def traducir_a_espanol(self, texto):
        # Traduce un texto dado al español
        raise NotImplementedError("Método para traducir a español no implementado.")

    def dias_de_la_semana(self):
        # Devuelve una lista de los días de la semana en el idioma específico
        raise NotImplementedError("Método para días de la semana no implementado.")

    def frases_comunes(self):
        # Devuelve un diccionario o lista de frases comunes en el idioma específico
        raise NotImplementedError("Método para frases comunes no implementado.")

    def contar_palabras_en_oracion(self, oracion):
        # Cuenta las palabras en una oración dada
        # Esta es una implementación genérica que podría funcionar para varios idiomas
        palabras = oracion.split()
        return len(palabras)
