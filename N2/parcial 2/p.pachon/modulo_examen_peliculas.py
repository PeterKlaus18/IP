# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:42:38 2023

@author: Nicolas
"""

import modulo_peliculas as mod
def costo_envio(peso:float, temporadabaja:bool, envioexpress:bool)->float:
    
    
    x=peso
    p=0
    if x>0 and x<=30:
        p=25000
        if envioexpress == True:
            t=p* 0.025
            p+=t
        if temporadabaja == True:
            t=p* 0.2
            p-=t
        return p
        
    if x>30 and x<=60:
        p=48000
        if envioexpress == True:
            t=p* 0.105
            p+=t
        if temporadabaja == True:
            t=p* 0.2
            p-=t
        return p
       
    if x>60 and x<=300:
        p=115000
        if envioexpress == True:
            t=p* 0.2
            p+=t
        if temporadabaja == True:
            t=p* 0.2
            p-=t
        return p

    
    
def buscar_dia_mas_tarde_genero(genero: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    
    if genero in p1["genero"]:
        if not(p1["hora"]< p2["hora"] and genero in p2["genero"]) and not (p1["hora"]< p3["hora"]and genero in p3["genero"]) and not (p1["hora"]< p4["hora"]and genero in p4["genero"]) and not (p1["hora"]< p5["hora"]and genero in p5["genero"]):
            return p1  
    
    if genero in p2["genero"]:
        if not(p2["hora"]< p1["hora"] and (genero in p1["genero"])) and not (p2["hora"]< p3["hora"]and genero in p3["genero"]) and not (p2["hora"]< p4["hora"]and genero in p4["genero"]) and not (p2["hora"]< p5["hora"]and genero in p5["genero"]):
            return p2
        
    if genero in p3["genero"]:
        if not(p3["hora"]< p2["hora"]and genero in p2["genero"]) and not (p3["hora"]< p1["hora"]and genero in p1["genero"]) and not (p3["hora"]< p4["hora"]and genero in p4["genero"]) and not (p3["hora"]< p5["hora"]and genero in p5["genero"]):
            return p3
        
    if genero in p4["genero"]:
        if not(p4["hora"]< p2["hora"]and genero in p2["genero"]) and not (p4["hora"]< p3["hora"]and genero in p3["genero"]) and not (p4["hora"]< p1["hora"]and genero in p1["genero"]) and not (p4["hora"]< p5["hora"]and genero in p5["genero"]):
            return p4
        
    if genero in p5["genero"]:
        if not (p5["hora"]< p2["hora"]and genero in p2["genero"]) and not (p5["hora"]< p3["hora"]and genero in p3["genero"]) and not (p5["hora"]< p4["hora"]and genero in p4["genero"]) and not (p5["hora"]< p1["hora"]and genero in p1["genero"]):
            return p5
    else:
        return None
    


def suma_tiempo(dia: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> int:
    
    a=0
    
    if dia in p1["dia"]:
       a+=int(p1["duracion"])
    if dia in p2["dia"]:
       a+=int(p2["duracion"])
    if dia in p3["dia"]:
       a+=int(p3["duracion"])
    if dia in p4["dia"]:
       a+=int(p4["duracion"])
    if dia in p5["dia"]:
       a+=int(p5["duracion"])
    
    return a
        

def dia_mas_tiempo(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
        
    dia="Lunes"
    lu=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Martes"
    ma=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Miércoles"
    mi=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Jueves"
    ju=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Viernes"
    vi=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Sábado"
    sa=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    dia="Domingo"
    do=suma_tiempo(dia, p1, p2, p3, p4, p5)
    
    a=""
    if lu > ma and lu > mi and lu > ju and lu > vi and lu > sa and lu > do:
        a="Lunes"
    if ma > lu and ma > mi and ma > ju and ma > vi and ma > sa and ma > do:
        a="Martes"
    if mi > ma and mi > lu and mi > ju and mi > vi and mi > sa and mi > do:
        a="Miércoles"
    if ju > ma and ju > mi and ju > lu and ju > vi and ju > sa and ju > do:
        a="Jueves"    
    if vi > ma and vi > mi and vi > ju and vi > lu and vi > sa and vi > do:
        a="Viernes"    
    if sa > ma and sa > mi and sa > ju and sa > vi and sa > lu and sa > do:
        a="Sábado"    
    if do > ma and do > mi and do > ju and do > vi and do > sa and do > lu:
        a="Domingo"    
            
    return a

    
    
def balancear_peliculas(dia: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> None:
    
    
    dmt= dia_mas_tiempo(p1, p2, p3, p4, p5)
    if (dmt in p1["dia"]) and (dia  not in p1["dia"]):
        
        
        nueva_hora= p1["hora"]
        control_horario= False
        mod.reagendar_pelicula(p1, nueva_hora, dia, control_horario, p1, p2, p3, p4, p5)
        
    if (dmt in p2["dia"]) and (dia  not in p2["dia"]):
        
        
        nueva_hora= p2["hora"]
        control_horario= False
        mod.reagendar_pelicula(p2, nueva_hora, dia, control_horario, p1, p2, p3, p4, p5)
        
    if (dmt in p3["dia"]) and (dia  not in p3["dia"]):
        
        
        nueva_hora= p3["hora"]
        control_horario= False
        mod.reagendar_pelicula(p3, nueva_hora, dia, control_horario, p1, p2, p3, p4, p5)
        
    if (dmt in p4["dia"]) and (dia  not in p4["dia"]):
        
        
        nueva_hora= p4["hora"]
        control_horario= False
        mod.reagendar_pelicula(p4, nueva_hora, dia, control_horario, p1, p2, p3, p4, p5)
        
        
    if (dmt in p5["dia"]) and (dia  not in p5["dia"]):
        
        
        nueva_hora= p5["hora"]
        control_horario= False
        mod.reagendar_pelicula(p5, nueva_hora, dia, control_horario, p1, p2, p3, p4, p5)
    

        





















 
    