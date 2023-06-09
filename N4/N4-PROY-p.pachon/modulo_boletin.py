# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Modulo de Funciones

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2
"""
import pandas as pd
import matplotlib.pyplot as plt


def cargar_matriz_estadisticas(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0, facultades + 1):
        estadisticas.append([0] * (elementos + 1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, elementos + 1):
            estadisticas[i][j] = datos[j].strip()
        i += 1
        linea = archivo.readline()
    archivo.close()

    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0, oferentes + 1):
        puestos.append([0] * (ocupantes + 1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, ocupantes + 1):
            puestos[i][j] = datos[j].strip()
        i += 1
        linea = archivo1.readline()
    archivo1.close()

    return puestos


def cargar_matriz_dobles(ruta_archivo: str) -> list:

    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    programa_1 = 35
    programa_2 = 35
    dobles = []
    for i in range(0, programa_1 + 1):
        dobles.append([0] * (programa_2 + 1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, programa_2 + 1):
            dobles[i][j] = datos[j].strip()
        i += 1
        linea = archivo2.readline()
    archivo2.close()

    return dobles


def puestos_atendidos(puestos: list, facultad: str) -> int:

    atendidos = 0
    for i in range(1, len(puestos)):
        if puestos[i][0] == facultad:
            for j in range(1, len(puestos[i])):
                atendidos += int(puestos[i][j])
    return atendidos


def puestos_ocupados(puestos: list, facultad: str) -> int:

    ocupados = 0
    facultades = puestos[1:]  #
    facultad_index = puestos[0].index(facultad)

    for fila in facultades:
        ocupados += int(fila[facultad_index])

    return ocupados


def facultad_mas_servicial(puestos: list) -> tuple:

    facultades = puestos[1:]
    facultad_mas_servicial = facultades[0]
    facultad_mas_servicial_index = 0
    facultad_mas_servicial_porcentaje = 0

    for i in range(1, len(facultades)):
        facultad = facultades[i]
        facultad_index = i
        facultad_atendidos = puestos_atendidos(puestos, facultad[0])
        facultad_ocupados = puestos_ocupados(puestos, facultad[0])
        facultad_porcentaje = facultad_atendidos / facultad_ocupados

        if facultad_porcentaje > facultad_mas_servicial_porcentaje:
            facultad_mas_servicial = facultad
            facultad_mas_servicial_index = facultad_index
            facultad_mas_servicial_porcentaje = facultad_porcentaje

    return (facultad_mas_servicial[0],
            round(facultad_mas_servicial_porcentaje, 2))


def hay_facultad_generosa(puestos: list, facultad: str,
                          porcentaje: float) -> tuple:
    porcentaje /= 100
    facultad_ocupados = puestos_ocupados(puestos, facultad)
    porcentaje_puestos = facultad_ocupados * porcentaje
    facultad_index = puestos[0].index(facultad)

    for facultad_row in puestos[1:]:
        facultad_name = facultad_row[0]

        facultad_a_facultad_interes = int(facultad_row[facultad_index])

        if facultad_a_facultad_interes >= porcentaje_puestos:
            facultad_porcentaje = (facultad_a_facultad_interes /
                                   facultad_ocupados) * 100
            return (facultad_name, round(facultad_porcentaje, 2))

    return ("No existe facultad generosa", 0)


def calcular_autocubrimiento(puestos: list, estadisticas: list) -> list:

    facultades = puestos[1:]
    autocubrimiento_facultades = [0] * len(facultades)

    for i in range(0, len(facultades)):
        facultad = facultades[i]
        facultad_atendidos = puestos_atendidos(puestos, facultad[0])
        facultad_ocupados = puestos_ocupados(puestos, facultad[0])
        facultad_porcentaje = facultad_atendidos / facultad_ocupados
        autocubrimiento_facultades[i] = facultad_porcentaje

    estadisticas[0].append("Autocubrimiento")
    for i in range(1, len(estadisticas)):
        estadisticas[i].append(round(autocubrimiento_facultades[i - 1], 2))

    return estadisticas


def doble_mas_comun(dobles: list) -> tuple:
    max_count = 0
    max_programs = None

    for i in range(1, len(dobles)):
        for j in range(i + 1, len(dobles)):
            count = int(dobles[i][j]) + int(dobles[j][i])
            if count > max_count:
                max_count = count
                max_programs = (dobles[0][i], dobles[j][0])

    return ((max_programs[0] + ' - ' + max_programs[1]), max_count)


def mostrar_pga_promedio(estadisticas: list) -> None:
    pga_facultades = [0] * len(estadisticas)
    facultades = estadisticas[1:]

    for i in range(0, len(facultades)):
        facultad = facultades[i]
        pga_facultades[i] = float(facultad[6])

    facultades_pga = dict()
    for i in range(0, len(facultades)):
        facultades_pga[facultades[i][0]] = pga_facultades[i]

    df = pd.DataFrame(facultades_pga.items(), columns=['Facultad', 'PGA'])
    df = df.sort_values(by=['PGA'])

    plt.bar(df['Facultad'], df['PGA'])
    plt.ylim(3.5, 4.2)
    plt.title('PGA promedio de las facultades')
    plt.xlabel('Facultad')
    plt.ylabel('PGA')
    plt.xticks(rotation=90)
    plt.show()
    plt.savefig('pga_promedio.png')


def mostrar_puestos_estudios_dirigidos(puestos: list) -> None:
    estudios_dirigidos_index = puestos[0].index("Estudios Dirigidos")

    facultad_names = []  # Names of the faculties
    estudios_dirigidos_values = [
    ]  # Number of positions offered to Estudios Dirigidos by each faculty

    for facultad_row in puestos[1:]:
        facultad_names.append(facultad_row[0])  # Name of the faculty
        # Number of positions that the faculty offers to Estudios Dirigidos
        estudios_dirigidos_values.append(
            int(facultad_row[estudios_dirigidos_index]))

    plt.figure(figsize=(10, 10))
    plt.pie(estudios_dirigidos_values, labels=facultad_names)
    plt.title('Puestos de cada facultad en Estudios Dirigidos')
    plt.savefig('puestos_estudios_dirigidos.png')
    plt.show()


mostrar_puestos_estudios_dirigidos(cargar_matriz_puestos("matriz_puestos.csv"))