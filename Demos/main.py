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
from Biblioteca.Coreano import Coreano
from Biblioteca.Ruso import Ruso
from Biblioteca.Noruego import Noruego
from Biblioteca.Arabe import Arabe
from Biblioteca.Chino import Chino
from Biblioteca.Tailandes import Tailandes
from Biblioteca.Nahuatl import Nahuatl
from Biblioteca.Polaco import Polaco

def obtener_instancia_idioma(opcion):
    return {
        '1': Japones(),
        '2': Coreano(),
        '3': Ruso(),
        '4': Noruego(),
        '5': Arabe(),
        '6': Chino(),
        '7': Tailandes(),
        '8': Nahuatl(),
        '9': Polaco
    }.get(opcion, None)

def imprimir_menu():
    print("\nSelecciona un idioma:")
    print("1. Japonés")
    print("2. Coreano")
    print("3. Ruso")
    print("4. Noruego")
    print("5. Árabe")
    print("6. Chino")
    print("7. Tailandés")
    print("8. Náhuatl")
    print("9. Polaco")
    print("0. Salir")

def imprimir_metodos():
    print("\nSelecciona un método:")
    print("1. Identificar escritura o dialecto")
    print("2. Números del 1 al 10")
    print("3. Traducir a español")
    print("4. Días de la semana")
    print("5. Frases comunes")
    print("0. Volver al menú principal")

def ejecutar_metodo_y_guardar(idioma, opcion):
    texto_prueba = "Texto de prueba"
    resultado = ""

    if opcion == '1':
        resultado = idioma.identificar_escritura_o_dialecto(texto_prueba)
    elif opcion == '2':
        resultado = str(idioma.numeros_del_1_al_10())
    elif opcion == '3':
        resultado = idioma.traducir_a_espanol(texto_prueba)
    elif opcion == '4':
        resultado = str(idioma.dias_de_la_semana())
    elif opcion == '5':
        resultado = str(idioma.frases_comunes())

    # Escribir en el archivo
    with open("resultados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Resultado ({idioma.__class__.__name__}, Método {opcion}): {resultado}\n")

    print(resultado)

if __name__ == '__main__':
    while True:
        imprimir_menu()
        opcion_idioma = input("Ingresa tu opción: ")
        if opcion_idioma == '0':
            break

        idioma = obtener_instancia_idioma(opcion_idioma)
        if idioma:
            while True:
                imprimir_metodos()
                opcion_metodo = input("Ingresa tu opción: ")
                if opcion_metodo == '0':
                    break
                ejecutar_metodo_y_guardar(idioma, opcion_metodo)
        else:
            print("Opción de idioma no válida.")
