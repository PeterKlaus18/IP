

atletas = cargar_atletas("atletas.csv")
atletas_medalla = atletas_por_medalla(atletas)
atletas_medalla_tipo = medallas_por_pais(atletas_medalla, "silver" )
escribir_archivo_por_medalla("silver.txt", atletas_medalla_tipo) 



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
    """

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
    """

    archivo= open(nombre_archivo, "w")

    for cada_pais in atletas_tipo_medalla:
        archivo.write("*********************************\n")
        archivo.write("Pais: " + cada_pais + "\n")
        archivo.write("*********************************\n")

        for cada_atleta in atletas_tipo_medalla[cada_pais]:
            archivo.write(cada_atleta["nombre"] + " - " + cada_atleta["evento"] + " - " + cada_atleta["anio"] + "\n")

    archivo.close()
#print(escribir_archivo_por_medalla("medallistas.txt", medallas_por_pais(atletas_por_medalla(a), "gold")))


#def escribir_archivo_por_medalla(nombre_archivo: str, atletas_tipo_medalla: dict)
