# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:38:40 2023

@author: Nicolas
"""

def calcular_agua_corporal(peso: float, C: float):
    """
    calcula el agua corporal total de un paciente a partir de su peso y el factor 
    correspondiente a su género. Para un hombre adulto de 70Kg. la respuesta debe ser 42 Lt
    
    """
    TBW=float(peso)*float(C)

    return TBW  
    
def calcular_deficit_agua(peso: float, C:float, cs:int)-> str:
    
    """
    calcula el déficit de agua corporal. Debe recibir como parámetro el peso de la persona,
    el factor según género y la concentración de sodio medida en plasma.
    La función debe mostrar un mensaje de la forma
    ‘El déficit de agua corporal del paciente es de X'
    El valor del déficit debe presentarse con un único decimal.
    Para un hombre adulto de 70Kg. con concentración de sodio medida en plasma de 155 mEq/l.
    la respuesta debe ser: 1.5 litros
    
    """
    a= calcular_agua_corporal(peso, C)
    TBWD=float(a) *(1-(140/cs))
    
    w=round(TBWD,1)
    
    return "El déficit de agua corporal del paciente es de "+ str(w)


def calcular_distribucion_agua_corporal(peso: float, C:float)-> str:
     """
     calcula los 5 valores explicados dado el peso del paciente y el factor según género y retorna una cadena con el siguiente formato:
'El agua corporal del paciente se encuentra distribuida de la siguiente manera: TBW: aa Lt: LIC bb Lt: LEC cc Lt: plasma: dd Lt y LLT; ee Lt.'
Donde aa, bb, cc, dd, y ee, son los valores correspondientes a cada una de las partes del agua corporal de acuerdo con la explicación dada.
Los valores deben aparecer con una única cifra decimal.
Para calcular el agua corporal se considera que 1 kg 1 L: por lo tanto, en un sujeto adulto de 70 kg el agua se encuentra distribuida de la siguiente manera: TBW. 42 Lt LIG 28 Lt: LEG 14 Lt: plasma: 3.5 Lt. y LLT: 10.5 Lt.
"""
     a= calcular_agua_corporal(peso, C)
    
     b= peso* 0.4
    
     c= peso* 0.2
    
     d= peso* 0.05
    
     e= peso* 0.15
    
     aa=round(a,1)
     bb=round(b,1)
     cc=round(c,1)
     dd=round(d,1)
     ee=round(e,1)    
    
     return "El agua corporal del paciente se encuentra distribuida de la siguiente manera: TBW:"+str(aa)+"  Lt: LIC "+str(bb)+" Lt: LEC "+str(cc)+" Lt: plasma: "+str(dd)+" Lt y LLT; "+str(ee)+" Lt" 
    



















