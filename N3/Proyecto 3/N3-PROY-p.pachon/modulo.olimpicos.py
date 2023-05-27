# -*- coding: utf-8 -*-



def cargar_atletas(direccion: str) -> list:
    
    atletas= []
    archivo= open(direccion)
    titulos= archivo.readline().split(",")
    
    lineas= archivo.readlines()
    for i in range (len(lineas)):
        
        atleta={}
        linea= lineas[i].split(",")
        for y in range(len(linea)):
            atleta[titulos[y]]=linea[y]
        atletas.append(atleta)

    archivo.close()
    return atletas     

       
a= cargar_atletas("atletas.csv")
                        

def atletas_por_anio(atletas: list, anio: int) -> dict:
    
    #anio= str(anio)
    
    dicc_eventos= {}
    lista_nombre_atletas= []
    lista_eventos= []
    for cada_atleta in atletas:
        
        evento= cada_atleta["evento"]
        
        if cada_atleta["anio"] == anio and evento not in lista_eventos:
            
            lista_eventos.append(evento)
            
        
    for cada_evento in lista_eventos:
        
        
            
        for cada_atleta in atletas:
            
            
            
            evento= cada_atleta["evento"]
            
            if cada_evento == evento and cada_atleta["nombre"] not in lista_nombre_atletas:
                
                lista_nombre_atletas.append(cada_atleta["nombre"])
                
        dicc_eventos[cada_evento]= lista_nombre_atletas
        
        lista_nombre_atletas= []
    
    return dicc_eventos
        
#print(atletas_por_anio(a,2000))

        
def ejecutar_medallas_en_rango(atletas: list) -> None:
    
    return None
    
    
    
    

