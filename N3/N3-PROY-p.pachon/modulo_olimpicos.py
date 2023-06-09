# -*- coding: utf-8 -*-


def cargar_atletas(direccion: str) -> list:
    """Función 1:
    Implemente la función cargar_atletas que reciba como parámetro el nombre de un archivo que contiene la
    información de los atletas y la cargue en el programa bajo la forma de una lista de diccionarios.
    Esta función debe retornar la lista de atletas(diccionarios) creada """

    atletas = []
    archivo = open(direccion)
    titulos = archivo.readline().strip().split(",")

    for cada_linea in archivo:
        atleta = {}
        linea = cada_linea.strip().split(",")
        
        for cada_posicion in range(len(linea)):
            atleta[titulos[cada_posicion]] = linea[cada_posicion]
            
        atletas.append(atleta)
        
    archivo.close()

    return atletas
a = cargar_atletas("atletas.csv")

def atletas_por_anio(atletas: list, anio: int) -> dict:
    """Función 2:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y un año de
    interés, y retorne un diccionario, cuyas llaves sean los eventos deportivos en dicho año, y el valor de cada una
    sea una lista con los nombres de los atletas que concursaron ese año en el evento. """

    anio = str(anio)
    dicc_eventos = {}
    lista_nombres = []
    lista_eventos = []

    for cada_atleta in atletas:
        evento = cada_atleta["evento"]

        if cada_atleta["anio"] == anio and evento not in lista_eventos:
            lista_eventos.append(evento)

    for cada_evento in lista_eventos:

        for cada_atleta in atletas:
            evento = cada_atleta["evento"]

            if cada_evento == evento and cada_atleta["nombre"] not in lista_nombres:
                lista_nombres.append(cada_atleta["nombre"])

        dicc_eventos[cada_evento] = lista_nombres
        lista_nombres = []

    return dicc_eventos
# print(atletas_por_anio(a,2000))

def medallas_en_rango(atletas: list,  nombre_atleta: str, anio_i: int, anio_f: int) -> list:
    """Función 3:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), un año de
    inicio, un año final, y el nombre de un atleta de interés, y retorne una lista de diccionarios que represente las
    medallas que ganó dicho atleta en ese periodo de tiempo. Cada diccionario debe tener 3 llaves: “evento”,
    “anio” y “medalla”, cuyos valores son, como sus nombres lo indican, el nombre del evento en el que el atleta
    ganó la medalla, el año en el cual el atleta obtuvo la medalla y la medalla obtenida (“gold”, “silver” o
    “bronze”). """

    lista1 = []
    lista_eventos = []
    lista_anio = []
    lista_medallas = []
    lista_f = []

    for cada_atleta in atletas:

        if cada_atleta["nombre"] == nombre_atleta and anio_i <= int(cada_atleta["anio"]) <= anio_f:
            lista1.append(cada_atleta)

    for cada_evento in lista1:

        if cada_evento["evento"] not in lista_eventos:
            lista_eventos.append(cada_evento["evento"])

    for cada_anio in lista1:

        if cada_anio["anio"] not in lista_anio:
            lista_anio.append(cada_anio["anio"])

    for cada_medalla in lista1:

        if cada_medalla["medalla"] not in lista_medallas:
            lista_medallas.append(cada_medalla["medalla"])

    for index in range(len(lista_anio)):
        dicc = {}

        dicc["evento"] = lista_eventos[index]
        dicc["anio"] = lista_anio[index]
        dicc["medalla"] = lista_medallas[index]

        lista_f.append(dicc)

    return lista_f
# print(medallas_en_rango(a, 1000, 3000, "abdalla abdelgadir el-sheikh"))

def atletas_por_pais(atletas: list, pais: str) -> list:
    """Función 4:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y un país de
    interés, y retorne una lista de diccionarios, que contenga la información de los atletas del país dado (sin
    importar el año en que participaron los atletas). Cada diccionario debe tener 3 llaves: “nombre”, “evento” y
    “anio”, cuyos valores son, como sus nombres los indican, el nombre del atleta, el evento en el que participó el
    atleta y el año de dicho evento. """

    lista1 = []
    lista_eventos = []
    lista_anio = []
    lista_nombres = []
    lista_f = []

    for cada_atleta in atletas:

        if cada_atleta["pais"] == pais:
            lista1.append(cada_atleta)

    for cada_nombre in lista1:

        if cada_nombre["nombre"] not in lista_nombres:
            lista_nombres.append(cada_nombre["nombre"])

    for cada_evento in lista1:

        if cada_evento["evento"] not in lista_eventos:
            lista_eventos.append(cada_evento["evento"])

    for cada_anio in lista1:

        if cada_anio["anio"] not in lista_anio:
            lista_anio.append(cada_anio["anio"])

    for index in range(len(lista_anio)):

        dicc= {}
        
        dicc["nombre"] = lista_nombres[index]
        dicc["evento"] = lista_eventos[index]
        dicc["anio"] = lista_anio[index]

        lista_f.append(dicc)

    return lista_f
# print(atletas_por_pais(a, "colombia"))

def pais_con_mas_atletas(atletas: list) -> dict:
    """Función 5:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y retorne un
    diccionario cuya llave sea el nombre del país que ha tenido más medallistas (en todos los tiempos de los juegos
    olímpicos) y cuyo valor sea la cantidad de medallistas. """

    dicc = {}
    lista_medallistas = []
    paismax = "pais"
    medallistas_max = 0
    lista_paises = []
    cantidad_medallistas = 0

    for cada_atleta in atletas:

        if cada_atleta["medalla"] != "na" and cada_atleta["nombre"] not in lista_medallistas:
            lista_medallistas.append(cada_atleta)

    for cada_atleta in lista_medallistas:

        if cada_atleta["pais"] not in lista_paises:
            lista_paises.append(cada_atleta["pais"])

    for cada_pais in lista_paises:

        for cada_atleta in lista_medallistas:

            if cada_pais == cada_atleta["pais"]:
                cantidad_medallistas += 1

        if cantidad_medallistas > medallistas_max:
            paismax = cada_pais

            medallistas_max = cantidad_medallistas

        cantidad_medallistas = 0

    dicc[paismax] = medallistas_max

    return dicc
# print(pais_con_mas_atletas(a))

def medallistas_por_evento(atletas: list, evento: str) -> list:
    """Función 6:
    Implemente una función que reciba como parámetro la lista completa de atletas(diccionarios), y un evento de
    interés, y retorne una lista de cadenas de caracteres, que contenga los nombres de todos los atletas que han
    ganado alguna medalla en el evento en cuestión (sin importar el año en que la obtuvieron). Si un atleta ha
    ganado más de una medalla en este evento, no debe aparecer repetido el nombre de dicho atleta. """

    lista_medallistas = []

    for cada_atleta in atletas:

        if cada_atleta["evento"] == evento and cada_atleta["medalla"] != "na" and cada_atleta["nombre"] not in lista_medallistas:
            lista_medallistas.append(cada_atleta["nombre"])

    return lista_medallistas
# print(medallistas_por_evento(a, "boxing men's light-welterweight"))

def atletas_con_mas_medallas_que(atletas: list, num_medallas: int) -> dict:
    """Función 7:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y un
    determinado número de medallas, y retorne un diccionario con los atletas que han ganado una cantidad de
    medallas superior al número dado por parámetro (en todos los tiempos). Este diccionario debe tener como
    llaves los nombres de los atletas y como valores el número de medallas ganadas por el atleta correspondiente
    (siempre y cuando ese número sea estrictamente superior al recibido por parámetro) """

    dicc_medallistas = {}
    lista_medallistas = []
    num_medallas
    
    for cada_atleta in atletas:

        if cada_atleta["medalla"] != "na":
            lista_medallistas.append(cada_atleta)

    for cada_medallista in lista_medallistas:

        if cada_medallista["nombre"] not in dicc_medallistas.keys():
            dicc_medallistas[cada_medallista["nombre"]] = 1
        else:
            dicc_medallistas[cada_medallista["nombre"]] += 1

    dicc_medallistas_copia = dicc_medallistas.copy()

    for cada_medallista in dicc_medallistas_copia.keys():

        if dicc_medallistas[cada_medallista] < num_medallas+1:
            del dicc_medallistas[cada_medallista]

    return dicc_medallistas
# print(atletas_con_mas_medallas_que(a, 5))

def atleta_estrella(atletas: list) -> dict:
    """Función 8:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y retorne un
    diccionario que represente al atleta estrella de todos los tiempos (esto es, el atleta que ha obtenido el mayor
    número de medallas a lo largo de todos los años). Este diccionario debe tener como llave el nombre del atleta y
    como valor el número de medallas ganadas. Si dos o más atletas se encuentran empatados, el diccionario debe
    incluir dos o más llaves (nombres de los atletas) con sus respectivos números de medallas. """

    dicc_medallistas = {}
    max_medallas = 0
    atleta_estrella = {}

    for cada_atleta in atletas:

        if cada_atleta["medalla"] != "na":

            if cada_atleta["nombre"] in dicc_medallistas:
                dicc_medallistas[cada_atleta["nombre"]] += 1
            else:
                dicc_medallistas[cada_atleta["nombre"]] = 1

    for nombre in dicc_medallistas:
        
        if dicc_medallistas[nombre] > max_medallas:
            max_medallas = dicc_medallistas[nombre]
            atleta_estrella = {nombre: max_medallas}

    return atleta_estrella
# print(atleta_estrella(a))

def mejor_pais_en_un_evento(atletas: list, evento: str) -> dict:
    """Función 9:
    Implemente una función que reciba como parámetro la lista completa de atletas(diccionarios) y el nombre de
    un evento, y retorne el país que ha tenido mejor desempeño en dicho evento. Esto es: el país que más
    medallas de valor ha ganado en un evento determinado, en todos los tiempos. Esto se determina por el
    número y categoría de las medallas. Es decir, que el mejor país es aquel que tenga más medallas de oro, en
    caso de empate con otro país, será mejor el que tenga más medallas de plata entre estos, y si el empate
    persiste, se definirá por el número de medallas de bronce. La respuesta debe ser un diccionario, cuya llave sea
    el nombre del país, y el valor sea una lista de 3 posiciones que indique el número de medallas ganadas de cada
    tipo ([gold, silver, bronze]). Si se encuentran 2 o más países igual de exitosos y que sean el mejor, el diccionario
    debe contenerlos a todos. """

    dicc_paises = {}
    gold = 0
    lista_paises = []
    dicc_final = {}

    for cada_atleta in atletas:
        if cada_atleta["evento"] == evento and cada_atleta["medalla"] != "na":
            pais = cada_atleta["pais"]
            medalla = cada_atleta["medalla"]
            
            if pais not in dicc_paises:
                num_medallas = {"gold": 0, "silver": 0, "bronze": 0}

                if medalla == "gold":
                    num_medallas["gold"]+= 1
                elif medalla == "silver":
                    num_medallas["silver"]+= 1
                elif medalla == "bronze":
                    num_medallas["bronze"]+= 1

                dicc_paises[pais] = num_medallas
            else:
                if medalla == "gold":
                    dicc_paises[pais]["gold"]+= 1
                elif medalla == "silver":
                    dicc_paises[pais]["silver"]+= 1
                elif medalla == "bronze":
                    dicc_paises[pais]["bronze"]+= 1

    for cada_pais in dicc_paises:

        if dicc_paises[cada_pais]["gold"] > gold:
            gold = dicc_paises[cada_pais]["gold"]
            lista_paises = [cada_pais]

        elif dicc_paises[cada_pais]["gold"] == gold:

            if dicc_paises[cada_pais]["silver"] > dicc_paises[lista_paises[0]]["silver"]:
                lista_paises = [cada_pais]

            elif dicc_paises[cada_pais]["silver"] == dicc_paises[lista_paises[0]]["silver"]:

                if dicc_paises[cada_pais]["bronze"] > dicc_paises[lista_paises[0]]["bronze"]:
                    lista_paises = [cada_pais]

                elif dicc_paises[cada_pais]["bronze"] == dicc_paises[lista_paises[0]]["bronze"]:
                    
                    lista_paises.append(cada_pais)

    for cada_pais in lista_paises:
        lista_medallas = [
            dicc_paises[cada_pais]["gold"],
            dicc_paises[cada_pais]["silver"],
            dicc_paises[cada_pais]["bronze"],
        ]
        dicc_final[cada_pais] = lista_medallas

    return dicc_final
#print(mejor_pais_en_un_evento(a, "athletics women's 100 metres"))

def todoterreno(atletas: list) -> str:
    """Función 10:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y retorne el
    nombre del atleta más “Todoterreno”. Es decir, aquel que haya participado en más eventos diferentes a través
    de los años. Para esta función solo debe contar una vez cada deporte, si un atleta participó en el mismo evento
    en años diferentes, solo debe contarse como un evento único. """
    
    lista_eventos= []
    lista_nombres= []
    dicc_atletas= {}
    
    for cada_atleta in atletas:
        
        if cada_atleta["nombre"] not in lista_nombres:
            lista_nombres.append(cada_atleta["nombre"])
        
    for nombre_actual in lista_nombres:
        lista_eventos= []

        for cada_atleta in atletas:
            nombre= cada_atleta["nombre"]

            if nombre == nombre_actual and cada_atleta["evento"] not in lista_eventos:
                lista_eventos.append(cada_atleta["evento"])

        dicc_atletas[nombre_actual]= len(lista_eventos)

    atleta_todoterreno= list(dicc_atletas.keys())[0]

    for cada_atleta in dicc_atletas:
        if dicc_atletas[cada_atleta] > dicc_atletas[atleta_todoterreno]:
            atleta_todoterreno= cada_atleta

    return atleta_todoterreno
#print(todoterreno(a))

def medallistas_por_nacion_y_genero(atletas: list, pais: str, genero: str) -> dict:
    """Función 11:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), el nombre de
    un país y un género (“m” o “f”), y retorne un diccionario con los medallistas de dicho país y género. Las llaves
    del diccionario deben ser los nombres de cada atleta medallista, y los valores deben ser listas de diccionarios
    que representen las medallas de dicho deportista. Estos últimos diccionarios (los que van dentro de cada lista)
    deben tener 3 llaves: “evento”, “anio” y “medalla”, cuyos valores son, como sus nombres lo indican, el nombre
    del evento en el que el atleta ganó la medalla, el año en el cual el atleta obtuvo la medalla y la medalla
    obtenida (“gold”, “silver” o “bronze”).
    A continuación, se muestra un ejemplo de cómo debe verse uno de los elementos del diccionario principal (el
    de retorno de la función), con las medallas de Yuri Alvear (judoka colombiana) en los años 2012 y 2016:

    {… , “yuri alvear orjuela”: [{“evento”: "judo women's middleweight", “anio”: 2012,
    “medalla”: “bronze”}, {“evento”: "judo women's middleweight", “anio”: 2016,
    “medulla”: “silver”}], …} """
        
    dicc_medallistas= {}

    for cada_atleta in atletas:

        if cada_atleta["pais"] == pais and cada_atleta["genero"] == genero and cada_atleta["medalla"] != "na":
            nombre= cada_atleta["nombre"]
            evento= cada_atleta["evento"]
            anio= cada_atleta["anio"]
            medalla= cada_atleta["medalla"]

            if nombre not in dicc_medallistas:
                dicc_medallistas[nombre]= [{"evento": evento, "anio": anio, "medalla": medalla}]
            else:
                dicc_medallistas[nombre].append({"evento": evento, "anio": anio, "medalla": medalla})

    return dicc_medallistas
#print(medallistas_por_nacion_y_genero(a, "colombia", "f"))

def porcentaje_medallistas(atletas: list) -> float:
    """Función 12:
    Implemente una función que reciba como parámetro la lista completa de atletas (diccionarios), y retorne el
    porcentaje de atletas que ganaron alguna medalla (en todos los tiempos), con dos decimales de aproximación.
    Cada atleta debe considerarse una sola vez así haya participado en varios eventos o en varios años. El
    porcentaje es calculado de la siguiente manera:

    Porcentaje Medallistas = Número de Medallistas/ Número de Atletas """
    
    lista_atletas= []
    lista_medallistas= []

    for cada_atleta in atletas:

        if cada_atleta["nombre"] not in lista_atletas:
            lista_atletas.append(cada_atleta["nombre"])

        if cada_atleta["medalla"] != "na" and cada_atleta["nombre"] not in lista_medallistas:
            lista_medallistas.append(cada_atleta["nombre"])

    porcentaje= round((len(lista_medallistas)/len(lista_atletas))*100, 2)
    
    return porcentaje
#print(porcentaje_medallistas(a))

def atletas_por_medalla(atletas:dict)->dict:
    """recibe como
    parámetro el diccionario de atletas y devuelve otro diccionario donde las llaves son los
    tipos de medallas y como valor la lista de atletas que ganaron las medallas

    """

    dicc_medallas= {"gold": [], "silver": [], "bronze": []}

    for cada_atleta in atletas:
        
        if cada_atleta["medalla"] != "na":
            dicc_medallas[cada_atleta["medalla"]].append(cada_atleta)

    return dicc_medallas
#print(atletas_por_medalla(a))

def medallas_por_pais(atletas_medalla:dict, tipo_medalla:str)->dict:
    """Genera un diccionario donde la llave es el nombre del país y el valor una lista con los
    atletas que han obtenido el tipo de medalla solicitado a lo largo de todos los años.
    
    {'algeria': [{'nombre': 'amar benikhlef', 'genero': 'm', 'edad': '26', 'pais': 'algeria', 'anio':
    '2008', 'evento': "judo men's middleweight", 'medalla': 'silver'},{'nombre': 'taoufik makhloufi',
    'genero': 'm', 'edad': '28', 'pais': 'algeria', 'anio': '2016', 'evento': "athletics men's 800
    metres", 'medalla': 'silver'}, … ],
    …
    …
    “argentina”: [{'nombre': 'matas jess almeyda', 'genero': 'm', 'edad': '22', 'pais': 'argentina',
    'anio': '1996', 'evento': "football men's football", 'medalla': 'silver'},{'nombre': 'roberto fabin
    ayala', 'genero': 'm', 'edad': '23', 'pais': 'argentina', 'anio': '1996', 'evento': "football men's
    football", 'medalla': 'silver'}…]"""

    dicc_medallas_pais= {}
    
    for cada_atleta in atletas_medalla[tipo_medalla]:

        if cada_atleta["pais"] not in dicc_medallas_pais:
            dicc_medallas_pais[cada_atleta["pais"]]= [cada_atleta]

        else:
            dicc_medallas_pais[cada_atleta["pais"]].append(cada_atleta)

    return dicc_medallas_pais
#print(medallas_por_pais(atletas_por_medalla(a), "gold"))

def escribir_archivo_por_medalla(nombre_archivo:str, atletas_tipo_medalla:dict):
    """que recibe como parámetro el diccionario del punto anterior y genera un archivo de tipo txt,
    donde deben registrarse: el nombre de cada país seguido de los nombres de los atletas con el
    evento y el año en que se obtuvo la medalla de ese país.
    El archivo resultante debe ser del tipo
    *********************************
    Pais : united states
    *********************************
    stephen anthony abas - wrestling men's featherweight freestyle - 2004
    nia nicole abdallah - taekwondo women's featherweight - 2004
    brigetta lashea barrett - athletics women's high jump - 2012
    dorothy lee dotsie bausch (cowden-) - cycling women's team pursuit - 2012
    frentorish tori bowie - athletics women's 100 metres - 2016
    christopher cornelius chris byrd - boxing men's middleweight - 1992…
    …
    …
    …
    *********************************
    Pais : russia
    *********************************
    tamila rashidovna abasova - cycling women's sprint - 2004
    bakhtiyar shakhabutdinovich akhmedov - wrestling men's super-heavyweight freestyle - 2008
    khadzhimurat magomedovich akkayev - weightlifting men's middle-heavyweight - 2004
    apti khamzatovich aukhadov - weightlifting men's light-heavyweight - 2012
    lyubov aleksandrovna bruletova - judo women's extra-lightweight - 2000
    yevgeny aleksandrovich chigishev - weightlifting men's super-heavyweight - 2008
    aleksey alekseyevich denisenko - taekwondo men's featherweight - 2016"""

    archivo= open(nombre_archivo, "w")

    for cada_pais in atletas_tipo_medalla:
        archivo.write("*********************************\n")
        archivo.write("Pais: " + cada_pais + "\n")
        archivo.write("*********************************\n")

        for cada_atleta in atletas_tipo_medalla[cada_pais]:
            archivo.write(cada_atleta["nombre"] + " - " + cada_atleta["evento"] + " - " + cada_atleta["anio"] + "\n")

    archivo.close()
print(escribir_archivo_por_medalla("medallistas.txt", medallas_por_pais(atletas_por_medalla(a), "gold")))