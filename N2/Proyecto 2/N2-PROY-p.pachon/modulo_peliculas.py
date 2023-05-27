"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    
    
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    
    
    dictionary={"nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio, "clasificacion": clasificacion, "hora": hora,
                "dia": dia}
    return dictionary
    
def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    
    if p1["nombre"] == nombre_pelicula:
        return p1
    elif p2["nombre"] == nombre_pelicula:
        return p2
    elif p3["nombre"] == nombre_pelicula:
        return p3
    elif p4["nombre"] == nombre_pelicula:
        return p4
    elif p5["nombre"] == nombre_pelicula:
        return p5
    else:
        return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
        
    """ 
    a=""
    if (p1["duracion"] > p2["duracion"]) and (p1["duracion"] > p3["duracion"]) and (p1["duracion"] > p4["duracion"]) and (p1["duracion"] > p5["duracion"]):
        a=p1
    
    if (p2["duracion"] > p1["duracion"]) and (p2["duracion"] > p3["duracion"]) and  (p2["duracion"] > p4["duracion"]) and (p2["duracion"] > p5["duracion"]): 
        a=p2
    
    if (p3["duracion"] > p1["duracion"]) and (p3["duracion"] > p2["duracion"]) and  (p3["duracion"] > p4["duracion"]) and (p3["duracion"] > p5["duracion"]):
        a=p3
    
    if (p4["duracion"] > p1["duracion"]) and (p4["duracion"] > p2["duracion"]) and  (p4["duracion"] > p3["duracion"]) and (p4["duracion"] > p5["duracion"]):
        a=p4
    
    if (p5["duracion"] > p1["duracion"]) and (p5["duracion"] > p2["duracion"]) and  (p5["duracion"] > p3["duracion"]) and (p5["duracion"] > p4["duracion"]):
        a=p5
    
    return a
    
   

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    x=p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    y= int(x/5)
    H= y//60
    M= y%60
    
    return str(H)+":"+str(M)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    a =""
    if anio>int(p1["anio"]) and anio>int(p2["anio"]) and anio>int(p3["anio"]) and anio>int(p4["anio"]) and anio>int(p5["anio"]):
        return  "ninguna"
    
    if anio< int(p1["anio"]):
        a+=str(p1["nombre"])+", "
    if anio< int(p2["anio"]):
        a+=str(p2["nombre"])+", "
    if anio< int(p3["anio"]):
        a+=str(p3["nombre"])+", "
    if anio< int(p4["anio"]):
        a+=str(p4["nombre"])+", "
    if anio< int(p5["anio"]):
        a+=str(p5["nombre"])
  
    return a
    
    
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    
    x=0
    if p1["clasificacion"]== "18+":
        x+=1
    if p2["clasificacion"]== "18+":
        x+=1
    if p3["clasificacion"]== "18+":
        x+=1
    if p4["clasificacion"]== "18+":
        x+=1
    if p5["clasificacion"]== "18+":
        x+=1
    
    return x

    """
    ignorar...
    de funcionar funciona.
    
    uwu
    
    
    if p1["clasificacion"] == "18+":
        if p2["clasificacion"] == "18+":
            if  p3["clasificacion"] == "18+":
                if p4["clasificacion"] == "18+":
                    if  p5["clasificacion"] == "18+":
                        return 5
                if  p5["clasificacion"] == "18+":
                    return 4
            if p4["clasificacion"] == "18+":
                if  p5["clasificacion"] == "18+":
                    return 4
            if  p5["clasificacion"] == "18+":
                return 3
        if p3["clasificacion"] == "18+":
            if p4["clasificacion"] == "18+":
                if  p5["clasificacion"] == "18+":
                    return 4
            if  p5["clasificacion"] == "18+":
                return 3
        if p4["clasificacion"] == "18+":
            if  p5["clasificacion"] == "18+":
                return 4
        if  p5["clasificacion"] == "18+":
            return 3
    if p2["clasificacion"] == "18+":
        if  p3["clasificacion"] == "18+":
            if p4["clasificacion"] == "18+":
                if  p5["clasificacion"] == "18+":
                    return 4
            if  p5["clasificacion"] == "18+":
                return 3
        if p4["clasificacion"] == "18+":
            if  p5["clasificacion"] == "18+":
                return 4
        if  p5["clasificacion"] == "18+":
            return 3
    if p3["clasificacion"] == "18+":
        if p4["clasificacion"] == "18+":
            if  p5["clasificacion"] == "18+":
                return  3
        if  p5["clasificacion"] == "18+":
            return  2
    if p4["clasificacion"] == "18+":
        if  p5["clasificacion"] == "18+":
            return 2
    if  p5["clasificacion"] == "18+":
        return  1
    
    return 0
    """
    

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    
    
    
    
    
    if peli == p1["nombre"]:
        if nuevo_dia == p2["dia"] or nuevo_dia == p3["dia"] or nuevo_dia == p4["dia"] or nuevo_dia == p5["dia"]:
            
            y= p1["duracion"]
            H= y//60
            M= y%60
            u= str(H)+str(M)
            t= int(u)
            
            inicio= nueva_hora
            final= inicio + t 
            
            if final > 2400:
                    ff= final- 2400
                    if ff > p2["hora"] or p3["hora"] or p4["hora"] or p5["hora"]:
                        return False
            
            if inicio < p2["hora"] and final > p2["hora"]:
                return False
            
            if inicio < p3["hora"] and final > p3["hora"]:
                return False
            
            if inicio < p4["hora"] and final > p4["hora"]:
                return False
             
            if inicio < p5["hora"] and final > p5["hora"]:
                return False
            
        
            
        if control_horario == True:
            if ("Documental" in p1["genero"]) and p1["hora"] >= 2200 or p1["hora"] <= 600:
                return False
            if p1["genero"] == "Drama" and p1["dia"] == "Viernes":
                return False
            if p1["dia"] == "Lunes" or "Martes" or "Miércoles" or "Jueves" or "Viernes" and p1["hora"] >= 2300 or p1["hora"] <= 600:
                return False
                 
        else: 
            p1["dia"]=nuevo_dia
            p1["hora"]=nueva_hora
            return True 
        
             
    if peli == p2["nombre"]:
         
         if nuevo_dia == p1["dia"] or nuevo_dia == p3["dia"] or nuevo_dia == p4["dia"] or nuevo_dia ==  p5["dia"]:
             
             y= p2["duracion"]
             H= y//60
             M= y%60
             u= str(H)+str(M)
             t= int(u)
             
             inicio= nueva_hora
             final= inicio + t  
             
             if final > 2400:
                     ff= final- 2400
                     if ff > p1["hora"] or p3["hora"] or p4["hora"] or p5["hora"]:
                         return False
             
             if inicio < p1["hora"] and final > p1["hora"]:
                 return False
             
             if inicio < p3["hora"] and final > p3["hora"]:
                 return False
             
             if inicio < p4["hora"] and final > p4["hora"]:
                 return False
              
             if inicio < p5["hora"] and final > p5["hora"]:
                 return False
             
         
         if control_horario == True:
             if ("Documental" in p2["genero"]) and p2["hora"] >= 2200 or p2["hora"] <= 600:
                 return False
             if p2["genero"] == "Drama" and p2["dia"] == "Viernes":
                 return False
             if p2["dia"] == "Lunes" or "Martes" or "Miércoles" or "Jueves" or "Viernes" and p2["hora"] >= 2300 or p2["hora"] <= 600:
                     return False
                  
         else: 
             p2["dia"]=nuevo_dia
             p2["hora"]=nueva_hora
             return True
         
         
    if peli == p3["nombre"]:
         
         if nuevo_dia == p2["dia"] or nuevo_dia == p1["dia"] or nuevo_dia == p4["dia"] or nuevo_dia == p5["dia"]:
             
             p3["duracion"]=y
             H= y//60
             M= y%60
             u= str(H)+str(M)
             t= int(u)
             
             inicio= nueva_hora
             final= inicio + t 
             
             if final > 2400:
                     ff= final- 2400
                     if ff > p2["hora"] or p1["hora"] or p4["hora"] or p5["hora"]:
                         return False
             
             if inicio < p2["hora"] and final > p2["hora"]:
                 return False
             
             if inicio < p1["hora"] and final > p1["hora"]:
                 return False
             
             if inicio < p4["hora"] and final > p4["hora"]:
                 return False
              
             if inicio < p5["hora"] and final > p5["hora"]:
                 return False
             
         
         if control_horario == True:
             if ("Documental" in p3["genero"]) and p3["hora"] >= 2200 or p3["hora"] <= 600:
                 return False
             if p3["genero"] == "Drama" and p3["dia"] == "Viernes":
                 return False
             if p3["dia"] == "Lunes" or "Martes" or "Miércoles" or "Jueves" or "Viernes" and p3["hora"] >= 2300 or p3["hora"] <= 600:
                 return False
                      
         else: 
             p3["dia"]=nuevo_dia
             p3["hora"]=nueva_hora
             return True

    
    if peli == p4["nombre"]:
        
        if nuevo_dia == p2["dia"] or nuevo_dia == p3["dia"] or nuevo_dia == p1["dia"] or nuevo_dia == p5["dia"]:
            
            p4["duracion"]=y
            H= y//60
            M= y%60
            u= str(H)+str(M)
            t= int(u)
            
            inicio= nueva_hora
            final= inicio + t 
            
            if final > 2400:
                    ff= final- 2400
                    if ff > p2["hora"] or p3["hora"] or p1["hora"] or p5["hora"]:
                        return False
            
            if inicio < p2["hora"] and final > p2["hora"]:
                return False
            
            if inicio < p3["hora"] and final > p3["hora"]:
                return False
            
            if inicio < p1["hora"] and final > p1["hora"]:
                return False
             
            if inicio < p5["hora"] and final > p5["hora"]:
                return False
            
        
        if control_horario == True:
            if ("Documental" in p4["genero"]) and p4["hora"] >= 2200 or p4["hora"] <= 600:
                return False
            if p4["genero"] == "Drama" and p4["dia"] == "Viernes":
                return False
            if p4["dia"] == "Lunes" or "Martes" or "Miércoles" or "Jueves" or "Viernes" and p4["hora"] >= 2300 or p4["hora"] <= 600:
                return False
                 
        else: 
            p4["dia"]=nuevo_dia
            p4["hora"]=nueva_hora
            return True    
         
    if peli == p5["nombre"]:
            
        if nuevo_dia == p2["dia"] or nuevo_dia == p3["dia"] or nuevo_dia == p4["dia"] or nuevo_dia == p1["dia"]:
                
               p5["duracion"]=y
               H= y//60
               M= y%60
               u= str(H)+str(M)
               t= int(u)
                
               inicio= nueva_hora
               final= inicio + t 
                
               if final > 2400:
                        ff= final- 2400
                        if ff > p2["hora"] or p3["hora"] or p4["hora"] or p1["hora"]:
                            return False
                
               if inicio < p2["hora"] and final > p2["hora"]:
                    return False
                
               if inicio < p3["hora"] and final > p3["hora"]:
                    return False
                
               if inicio < p4["hora"] and final > p4["hora"]:
                    return False
                 
               if inicio < p1["hora"] and final > p1["hora"]:
                    return False 
                
            
        if control_horario == True:
            if ("Documental" in p5["genero"]) and p5["hora"] >= 2200 or p5["hora"] <= 600:
                return False
            if p5["genero"] == "Drama" and p5["dia"] == "Viernes":
                return False
            if p5["dia"] == "Lunes" or "Martes" or "Miércoles" or "Jueves" or "Viernes" and p5["hora"] >= 2300 or p5["hora"] <= 600:
                return False
                     
        else:
            p5["dia"]=nuevo_dia
            p5["hora"]=nueva_hora
            return True        
                 
 #uwu        
       
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    
    
    if peli["clasificacion"] == "7+":
        x=7
        
    if peli["clasificacion"] == "13+":
        x=13
        
    if peli["clasificacion"] == "18+":
        x=18
    
    if peli["clasificacion"] == "Todos":
        x=0
    
    if edad_invitado < x:
        if autorizacion_padres == False:
            if (edad_invitado < 15) and ("Terror" in peli["genero"]):
                return False
            if "Documental" not in peli["genero"]:
                return False
            else:
                return True
        if (edad_invitado < 10) and ("Familiar" not in peli["genero"]):
            return False
        else:
            return True
    else:
        return True


