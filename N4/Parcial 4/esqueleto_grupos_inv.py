


import pandas as pd 
import matplotlib.pyplot as plt 

archivo = pd.read_csv("estadisticas_facultades.csv")

def cantidad_grupos_investigacion_facultades(datos, num_min_grupos:int):
    datos_filtrados = datos[datos['Grupos de investigacion'] >= num_min_grupos]
    plt.pie(datos_filtrados['Grupos de investigacion'], labels = datos_filtrados['Unnamed: 0'])
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()

cantidad_grupos_investigacion_facultades(archivo, 10)