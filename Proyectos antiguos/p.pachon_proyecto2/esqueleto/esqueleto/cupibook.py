"""
Ejercicio nivel 2: Cupibook: La nueva red social
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""

def crear_amigo( nombre: str, fecha_de_nacimiento: int,
                 genero: str, genero_musical_favorito: str,
                 genero_literario_favorito: str,
                 numero_de_likes: int,
                 numero_de_publicaciones: int, cantidad_de_amigos: int,
                 bloqueado: bool) -> dict:
    """
    Función para crear un amigo en la plataforma. El signo zodiacal se asigna a partir
    de la fecha de nacimiento usando la función auxiliar asignar_signo_zodiacal.

    Parámetros
    ----------
    nombre : str
        Nombre del amigo.
    fecha_de_nacimiento : int
        Fecha de nacimiento del amigo representada como un entero de 8 dígitos
        en formato YYYYMMDD.
    genero : str
        Género del amigo.
    genero_musical_favorito : str
        Género musical favorito del amigo.
    genero_literario_favorito : str
        Género literario favorito del amigo.
    numero_de_likes : int
        Número de likes que tiene el amigo.
    numero_de_publicaciones : int
        Número de publicaciones que tiene el amigo.
    cantidad_de_amigos : int
        Número de amigos que se tienen
    bloqueado : bool
        Valor booleano que indica si un amigo está bloqueado o no.

    Retorno
    -------
    dict
        Diccionario del amigo con su información.

    """
    
    amigo= {"nombre": nombre
            , "fecha_de_nacimiento": fecha_de_nacimiento
            , "genero": genero
            , "genero_musical_favorito": genero_musical_favorito
            , "genero_literario_favorito": genero_literario_favorito
            , "likes": numero_de_likes
            , "numero_de_publicaciones": numero_de_publicaciones
            , "cantidad_de_amigos": cantidad_de_amigos
            , "bloqueado": bloqueado
            , "signo_zodiacal": asignar_signo_zodiacal(fecha_de_nacimiento)}
    
    
    return amigo

def buscar_amigo_por_nombre( nombre:str, a1: dict, a2: dict, a3: dict, 
                            a4: dict ) -> dict:
    """
    Busca el amigo con el nombre pasado por parámetro.
    En caso de no haber coincidencia se retorna None.

    Parámetros
    ----------
    nombre : str
        Nombre del amigo que se desea buscar.
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario del amigo con el nombre pasado por parámetro.
        Retorna None si no lo encuentra.

    """
   
    
    
    if a1["nombre"] == nombre:
        return a1
    elif a2["nombre"] == nombre:
        return a2
    elif a3["nombre"] == nombre:
        return a3
    elif a4["nombre"] == nombre:
        return a4
    else:
        return None


def buscar_amigo_con_mas_likes( a1: dict, a2: dict, a3: dict,
                               a4: dict ) -> dict:
    """
    Determina cuál es el amigo con más likes en la plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario que representa al amigo más famoso de la plataforma
    """
   
    if (a1["likes"] > a2["likes"] 
    and a1["likes"] > a3["likes"] 
    and  a1["likes"] > a4["likes"]):
        return a1
    
    elif (a2["likes"] > a1["likes"] 
    and a2["likes"] > a3["likes"] 
    and  a2["likes"] > a4["likes"]):
        return a2
    
    elif (a3["likes"] > a2["likes"] 
    and a3["likes"] > a1["likes"] 
    and  a3["likes"] > a4["likes"]):
        return a3
    
    elif (a4["likes"] > a2["likes"] 
    and a4["likes"] > a3["likes"] 
    and  a4["likes"] > a1["likes"]):
        return a4
    
    
    else:
        return None
   

def buscar_amigo_con_menos_publicaciones( a1: dict, a2: dict, a3: dict,
                                         a4: dict ) -> dict:
    """
    Determina cuál es el amigo con menos publicaciones en la plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario que representa al amigo con menos publicaciones en la plataforma.
    """
    
    if (a1["numero_de_publicaciones"] < a2["numero_de_publicaciones"] 
    and a1["numero_de_publicaciones"] < a3["numero_de_publicaciones"] 
    and  a1["numero_de_publicaciones"] < a4["numero_de_publicaciones"]):
        return a1
    
    elif (a2["numero_de_publicaciones"] < a1["numero_de_publicaciones"] 
    and a2["numero_de_publicaciones"] < a3["numero_de_publicaciones"] 
    and  a2["numero_de_publicaciones"] < a4["numero_de_publicaciones"]):
        return a2
    
    elif (a3["numero_de_publicaciones"] < a2["numero_de_publicaciones"] 
    and a3["numero_de_publicaciones"] < a1["numero_de_publicaciones"] 
    and  a3["numero_de_publicaciones"] < a4["numero_de_publicaciones"]):
        return a3
    
    elif (a4["numero_de_publicaciones"] < a2["numero_de_publicaciones"] 
    and a4["numero_de_publicaciones"] < a3["numero_de_publicaciones"] 
    and  a4["numero_de_publicaciones"] < a1["numero_de_publicaciones"]):
        return a4
    
    else:
        return None

def asignar_signo_zodiacal( fecha: int ) -> str:
    """
    Función que determina de acuerdo a una fecha dada, el signo zodiacal
    correspondiente.

    Parámetros
    ----------
    fecha : int
        Fecha de nacimiento del amigo representada como un entero de 8 dígitos
        en formato YYYYMMDD.

    Retorno
    -------
    str
        Cadena con el signo zodiacal del amigo.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    x= str(fecha)
    dia= int(x[6]+x[7])
    mes= int(x[4]+x[5])
    
    if (mes == 1 and dia >=21) or (mes ==2 and dia <=19 ):
        return str("acuario")
    
    elif (mes == 2 and dia >=20) or (mes ==3 and dia <=20 ):
        return str("piscis")
    
    elif (mes == 3 and dia >=21) or (mes ==4 and dia <=20 ):
        return str("aries")
    
    elif (mes == 4 and dia >=21) or (mes ==5 and dia <=21 ):
        return str("tauro")
    
    elif (mes == 5 and dia >=22) or (mes ==6 and dia <=21 ):
        return str("geminis")
    
    elif (mes == 6 and dia >=22) or (mes ==7 and dia <=22 ):
        return str("cancer")
    
    elif (mes == 7 and dia >=23) or (mes ==8 and dia <=22 ):
        return str("leo")
    
    elif (mes == 8 and dia >=23) or (mes ==9 and dia <=22 ):
        return str("virgo")
    
    elif (mes == 9 and dia >=23) or (mes ==10 and dia <=22 ):
        return str("libra")
    
    elif (mes == 10 and dia >=23) or (mes ==11 and dia <=22 ):
        return str("escorpio")
    
    elif (mes == 11 and dia >=23) or (mes ==12 and dia <=21 ):
        return str("sagitario")
    
    elif (mes == 12 and dia >=22) or (mes ==1 and dia <=20 ):
        return str("capricornio")
    
    else: 
        return None
    
def es_cupiamigo( amigo1: dict , amigo2: dict) -> bool:
    """
    Función que determina si dos amigos son Cupiamigos.

    Parámetros
    ----------
    amigo1 : dict
        Información del primer amigo.
    amigo2 : dict
        Información del segundo amigo.

    Retorno
    -------
    bool
        True si los dos amigos son Cupiamigos, False de lo contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    if (amigo1["cantidad_de_amigos"] >=3 and amigo2["cantidad_de_amigos"] >=3) and (amigo1["bloqueado"] == False and amigo2["bloqueado"] == False) and (amigo1["genero_musical_favorito"] == amigo2["genero_musical_favorito"]) and (amigo1["genero_literario_favorito"] == amigo2["genero_literario_favorito"]) and (signo_es_compatible(amigo1["signo_zodiacal"], amigo2["signo_zodiacal"])):
        return True
    
    else:
        return False
    
    

def es_cupienemigo( amigo:dict ) -> bool:
    """
    Función que determina si un amigo es Cupienemigo.

    Parámetros
    ----------
    amigo : dict
        Información del amigo.

    Retorno
    -------
    bool
        True si es Cupienemigo, False de lo contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    
    if (amigo["bloqueado"]== True) and (amigo["numero_de_likes"]<5) and (amigo["cantidad_de_amigos"]==0):
        return True
    else:
        return False
    
    
    
    

def signo_es_compatible( amigo1: dict, amigo2: dict ) -> bool:
    """
    Función que determina compatibilidad entre signos de dos amigos.

    Parámetros
    ----------
    amigo1 : dict
        Información el primer amigo.
    amigo2 : dict
        Información el segundo amigo.

    Retorno
    -------
    bool
        True si los dos amigos son compatibles según su signo, False de lo
        contrario.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    
    if amigo1["signo_zodiacal"] == "aries" and (amigo2["signo_zodiacal"]== "geminis" or amigo2["signo_zodiacal"]== "leo" or amigo2["signo_zodiacal"]== "libra" or amigo2["signo_zodiacal"]== "sagitario"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "tauro" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "cancer" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "libra" or amigo2["signo_zodiacal"]== "escorpio" or amigo2["signo_zodiacal"]== "capricornio" or amigo2["signo_zodiacal"]== "piscis"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "geminis" and (amigo2["signo_zodiacal"]== "aries" or amigo2["signo_zodiacal"]== "leo" or amigo2["signo_zodiacal"]== "libra" or amigo2["signo_zodiacal"]== "acuario"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "cancer" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "escorpio" or amigo2["signo_zodiacal"]== "piscis"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "leo" and (amigo2["signo_zodiacal"]== "aries" or amigo2["signo_zodiacal"]== "geminis" or amigo2["signo_zodiacal"]== "leo" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "libra"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "virgo" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "cancer" or amigo2["signo_zodiacal"]== "leo" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "escorpio" or amigo2["signo_zodiacal"]== "capricornio" or amigo2["signo_zodiacal"]== "piscis"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "libra" and (amigo2["signo_zodiacal"]== "aries" or amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "geminis" or amigo2["signo_zodiacal"]== "leo" or amigo2["signo_zodiacal"]== "libra" or amigo2["signo_zodiacal"]== "acuario"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "escorpio" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "cancer" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "piscis"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "sagitario" and (amigo2["signo_zodiacal"]== "aries" or amigo2["signo_zodiacal"]== "sagitariio" or amigo2["signo_zodiacal"]== "acuario"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "capricornio" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "piscis"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "acuario" and (amigo2["signo_zodiacal"]== "geminis" or amigo2["signo_zodiacal"]== "libra" or amigo2["signo_zodiacal"]== "sagitario" or amigo2["signo_zodiacal"]== "acuario"):
        return True
    
    
    elif amigo1["signo_zodiacal"] == "piscis" and (amigo2["signo_zodiacal"]== "tauro" or amigo2["signo_zodiacal"]== "cancer" or amigo2["signo_zodiacal"]== "virgo" or amigo2["signo_zodiacal"]== "escorpio" or amigo2["signo_zodiacal"]== "capricornio"):
        return True
    else:
        return False
    
    
   
    

def amigo_mas_compatibilidad( a1: dict, a2: dict,
                               a3: dict, a4: dict ) -> dict:
    """
    Función que determina el amigo con mayor puntaje de compatibilidad en la
    plataforma.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.

    Retorno
    -------
    dict
        Diccionario con la infromación del amigo con mayor puntaje de
        compatibilidad.

    """

    if 

def contar_amigos_con_generos(a1: dict, a2: dict,
                                a3: dict, a4: dict, genero_musical:str,
                                genero_literario: str) -> int:
    """
    Función que cuenta los amigos con un género musical y un género literario
    favorito determinado.

    Parámetros
    ----------
    a1 : dict
        Diccionario con la información del primer amigo.
    a2 : dict
        Diccionario con la información del segundo amigo.
    a3 : dict
        Diccionario con la información del tercer amigo.
    a4 : dict
        Diccionario con la información del cuarto amigo.
    genero_musical : str
        Género musical a buscar.
    genero_literario : str
        Género literario a buscar.

    Retorno
    -------
    int
        Número de amigos con el género musical y literario favorito pasados
        por parámetro.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None
