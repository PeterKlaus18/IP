
import math

def calcular_distancia_tierra(t1: float, g1: float, t2: float, g2: float)->float:
    
    t11= math.radians(t1)
    t22= math.radians(t2)
    g11= math.radians(g1)
    g22= math.radians(g2)

    
    d= 6371.01 * math.acos(math.sin(t11)*math.sin(t22)+math.cos(t11)*math.cos(t22)*math.cos(g11-g22))
    
    return round(d,2)


t1= 4.624335
g1= -74.063644
t2= 10.963889
g2= -74.796387

print(calcular_distancia_tierra(t1, g1, t2, g2))
 


