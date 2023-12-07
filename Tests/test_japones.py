import sys
import os

# Obtener la ruta absoluta del archivo actual (main.py)
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Calcular la ruta del directorio padre, que es 'IDEOLINGO'
ruta_directorio_padre = os.path.abspath(os.path.join(ruta_actual, '..'))

# Añadir esa ruta a sys.path
if ruta_directorio_padre not in sys.path:
    sys.path.insert(0, ruta_directorio_padre)

from Biblioteca.Japones import Japones

# Crear una instancia de la clase Japones
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
