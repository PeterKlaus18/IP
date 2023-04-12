# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 01:13:55 2022

@author: Nicolas
"""

import numpy as np
import math


def calcular_fuerza_gravedad(masa_1: float, masa_2: float, distancia: float)->float:
    
    """Calcula la fuerza de gravedad universal entre dos cuerpos celestes dadas
    sus masas y la distancia entre ellos.
    masa_1: Masa del primer cuerpo celeste en kilogramos
    masa_2: Masa del segundo cuerpo celeste en kilogramos
    distancia: Distancia entre los 2 cuerpos celestes en metros
    Retorno: La fuerza de atracción entre los 2 cuerpos, en newtons"""
    
    f= float(6.67e-11) * float(masa_1)*float( masa_2)
    g=float(distancia)
    x= float(math.pow(g,2))
    
    f/= float(x)
   
    return f


def calcular_constante_K(masa: float)->float:
    
    """Calcula el valor de la constante K de Kepler, dada la masa del cuerpo
    celeste orbitado.
    masa: Masa del cuerpo celeste orbitado en kilogramos
    Retorno: Valor de la constante K de Kepler, en s2/m3, para dicho cuerpo celeste
    """
    m=float(masa)
    
    k= 4* 3.14**2
    k/= 6.67e-11*m
    return k

def calcular_periodo(masa: float, distancia_media: float)->float:
    
    """Calcula el periodo orbital, es decir la duración del año, de un cuerpo celeste dada la masa del cuerpo celeste sobre el cual este orbita y la distancia media
    al mismo.
    masa: Masa del cuerpo celeste orbitado en kilogramos
    distancia_media: Distancia media entre los cuerpos celestes expresada en metros
    Retorno: Periodo orbital del cuerpo celeste en segundos, redondeado a tres cifras decimales"""
    
    d=float(distancia_media)
    
    k= calcular_constante_K(masa)
    p= np.sqrt( k * d**3)
    return p

def calcular_distancia_media(masa: float, periodo: float)->float:
    
    """Calcula la distancia media de un cuerpo celeste al cuerpo al cual orbita,
    dada la masa del cuerpo celeste orbitado y su periodo orbital.
    masa
    float
    Masa del cuerpo celeste orbitado en kilogramos
    periodo
    float
    Periodo orbital del cuerpo celeste en segundos
    Retorno
    float
    Distancia media entre los cuerpos celestes expresada en metros, redondeada a tres cifras decimales
    
    """
    p=float(periodo)
    
    o=p**2
    
    
    k= calcular_constante_K(masa)
    o/= k
    
    x= math.pow(o, 1/3)
    
    return x

def calcular_aceleracion(vf: float, vi: float, dt: float)->float:
    
    """Calcula la aceleración de un cuerpo según la velocidad inicial, la velocidad final y el tiempo en el que transcurre el cambio de velocidad.
    vf
    float
    Velocidad final en m/s
    vi
    float
    Velocidad inicial en m/s
    dt
    float
    Tiempo en el que sucede el cambio de velocidad
    Retorno
    float
    Aceleración del cuerpo, en m/s2
    """
    vf= float(vf)
    vi= float(vi)
    a= vf - vi
    dt= float(dt)
    a/= dt
    return a

def calcular_magnitud_de_la_fuerza(masa: float, vf: float, vi: float, dt: float)-> float:
    
    """Calcula la fuerza de la fuerza según la masa del objeto, su velocidad inicial, su velocidad final y el tiempo.
    masa
    float
    Masa del objeto en kilogramos
    vf
    float
    Velocidad final en m/s
    vi
    float
    Velocidad inicial en m/s
    dt
    float
    Tiempo en el que sucede el cambio de velocidad
    Retorno
    float
    Magnitud de “La Fuerza”, en m/s2 """
    
    a= calcular_aceleracion(vf, vi, dt)
    m= float(masa)
    f= m * a
    return f

def calcular_momento(masa: float, velocidad: float)->float:
    
    """Calcula el momento de un cuerpo según su masa y su velocidad de movimiento.
    masa
    float
    Masa del objeto en kilogramos
    velocidad
    float
    Velocidad de movimiento en m/s
    Retorno
    float
    Momento del objeto, kg*m/s
    """
    masa= float(masa)
    velocidad= float(velocidad)
    
    m= masa * velocidad
    return m

def calcular_velocidad_colision(masa_1: float, masa_2: float, velocidad_1: float, velocidad_2: float)-> float:
    
    """Calcula la velocidad final después de una colisión entre 2 cuerpos.
    Parámetros
   
    masa_1
    float
    Masa del objeto 1 en kilogramos
    masa_2
    float
    Masa del objeto 2 en kilogramos
    velocidad_1
    float
    Velocidad de movimiento del objeto 1 en m/s
    velocidad_2
    float
    Velocidad de movimiento del objeto 2 en m/s
    Retorno
    float
    Velocidad final después de la colisión de los 2 cuerpos, en m/s, redondeada a tres cifras decimales
    """
    masa_1= float(masa_1)
    masa_2= float(masa_2)
    velocidad_1= float(velocidad_1)
    velocidad_2= float(velocidad_2)
    m1= calcular_momento(masa_1, velocidad_1)
    m2= calcular_momento(masa_2, velocidad_2)
    v= m1+m2
    v/= masa_1 + masa_2
    return v
    
    
        
    
        
    
    