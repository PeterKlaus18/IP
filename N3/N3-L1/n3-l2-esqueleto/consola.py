# -*- coding: utf-8 -*-
import libreria as lib


def ejecutar_invertir_cadena()->None:
    print("Inversor de cadenas usando concatenación")
    palabra = str(input("Por favor ingrese la cadena a invertir: "))
    invertida = lib.invertir_cadena(palabra)
    print("La cadena '", invertida, "' es la cadena invertida ")


def ejecutar_letra_mas_comun()->None:
    print("Evaluador de letra mas común")
    frase = str(input("Por favor digite la frase: "))
    hay = lib.letra_mas_comun(frase)
    print("La letra mas común es: ",hay)


def ejecutar_contar_vocales()->None:
    print("Analizador de frases para conteo de vocales")
    frase = str(input("Por favor ingrese la frase: "))
    rta = lib.contar_vocales(frase)
    if rta == 1:
        print("Hay más vocales en las posiciones impares")
    elif rta ==2:
        print("Hay más vocales en las posiciones pares")
    else:
        print("Hay la misma cantidad de vocales en las dos clases de posiciones")


def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Invertir cadena")
    print("2. Conteo de Vocales")
    print("3. Letra mas comun")
    print("4. Salir")


def iniciar_aplicacion()->None:
    """
    Esta función mantiene el programa funcionando hasta que el usuario seleccione la opción para salir.
    La función primero debe mostrar el menú de opciones usando la función mostrar_menu().
    A continuación, debe solicitarle al usuario una opción.
    Según lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccionó la opción de Salir, la función debe terminar su ejecución para que el programa pueda terminar.
    Si el usuario seleccionó cualquier otra opción, después de ejecutar la opción seleccionada se debe volver
    a mostrar el menú de opciones y se debe repetir el proceso.
    """

    """ TODO: implementar la función """
    mostrar_menu()



iniciar_aplicacion()