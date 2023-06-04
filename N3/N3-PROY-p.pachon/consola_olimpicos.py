# -*- coding: utf-8 -*-



import modulo_olimpicos as olim

def ejecutar_cargar_atletas() -> list:
    
    archivo = input("Por favor ingrese el nombre del archivo CSV con los atletas: ")
    atletas = olim.cargar_atletas(archivo)
    if len(atletas) == 0:
        print("El archivo seleccionado no es válido. No se pudieron cargar los atletas olímpicos")
    else:
        print("Se cagaron", len(atletas), "atletas a partir del archivo.")
    return atletas



def ejecutar_atletas_por_anio(atletas: list) -> None:

    anio = input("Ingrese el año de su interés: ")
    print(olim.atletas_por_anio(atletas, anio))

    
def ejecutar_medallas_en_rango(atletas: list) -> None:

    nombre = input("Ingrese el nombre del atleta de su interés: ")
    aniomenor = int(input("Ingrese el límite inferior del rango: "))
    aniomayor = int(input("Ingrese el límite superior del rango: "))
    print(olim.medallas_en_rango(atletas, nombre, aniomenor, aniomayor))


def ejecutar_atletas_por_pais(atletas: list) -> list:

    pais = input("Ingrese el nombre del país de su interés: ")
    print(olim.atletas_por_pais(atletas, pais))
    

def ejecutar_pais_con_mas_atletas(atletas: list) -> None:
    
    print(olim.pais_con_mas_atletas(atletas))
    

def ejecutar_medallistas_por_evento(atletas: list) -> None:
    
    evento = input("Ingrese el evento de su interés: ")
    print(olim.medallistas_por_evento(atletas, evento))
    

def ejecutar_atletas_con_mas_medallas_que(atletas: list) -> None:

    limite = int(input("Ingrese el mínimo de medallas: "))
    print(olim.atletas_con_mas_medallas_que(atletas, limite))
    

def ejecutar_atleta_estrella(atletas: list) -> None:
    
    print(olim.atleta_estrella(atletas))
    
    
def ejecutar_mejor_pais_en_un_evento(atletas: list) -> None:
    
    evento = input("Ingrese el evento de su interés: ")
    print(olim.mejor_pais_en_un_evento(atletas, evento))
    
    
def ejecutar_todoterreno(atletas: list) -> str:
    
    print(olim.todoterreno(atletas))
    
    
def ejecutar_medallistas_por_nacion_y_genero(atletas: list) -> None:
    
    pais = input("Ingrese el país de su interés: ")
    genero = input("Ingrese el género de su interés (m o f): ")
    print(olim.medallistas_por_nacion_y_genero(atletas, pais, genero))
    
    
def ejecutar_porcentaje_medallistas(atletas: list) -> None:
    
    print(olim.porcentaje_medallistas(atletas))    


def mostrar_menu():
    """Imprime las opciones de ejecución disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar un archivo de atletas")
    print("2. Consultar los atletas de un año dado")
    print("3. Consultar las medallas de un atleta en un periodo")
    print("4. Consultar los atletas de un país dado")
    print("5. Consultar el país con más medallistas")
    print("6. Consultar todos los medallistas de un evento dado")
    print("7. Consultar los atletas más populares")
    print("8. Consultar el atleta estrella de todos los tiempos")
    print("9. Consultar el mejor país en un evento")
    print("10. Consultar el atleta Todoterreno")
    print("11. Consultar los medallistas por nación y género")
    print("12. Consultar el porcentaje de atletas que son medallistas")
    print("13. Salir de la aplicación")
	
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    atletas = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            atletas=ejecutar_cargar_atletas()
        elif opcion_seleccionada == 2:
            ejecutar_atletas_por_anio(atletas)
        elif opcion_seleccionada == 3:
            ejecutar_medallas_en_rango(atletas)
        elif opcion_seleccionada == 4:
            ejecutar_atletas_por_pais(atletas)
        elif opcion_seleccionada == 5:
            ejecutar_pais_con_mas_atletas(atletas)
        elif opcion_seleccionada == 6:
            ejecutar_medallistas_por_evento(atletas)
        elif opcion_seleccionada == 7:
            ejecutar_atletas_con_mas_medallas_que(atletas)
        elif opcion_seleccionada == 8:
            ejecutar_atleta_estrella(atletas)
        elif opcion_seleccionada == 9:
            ejecutar_mejor_pais_en_un_evento(atletas)
        elif opcion_seleccionada == 10:
            ejecutar_todoterreno(atletas)
        elif opcion_seleccionada == 11:
            ejecutar_medallistas_por_nacion_y_genero(atletas)
        elif opcion_seleccionada == 12:
            ejecutar_porcentaje_medallistas(atletas)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor seleccione una opción válida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()