archi = "cupicharts.csv"

def cargar_cupicharts(ruta_archivo: str) -> dict:

    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    
    dicc = {}
    
    encabezado = archivo.readline().strip().split(',')
    
    linea = archivo.readline().strip()
    
    while linea != "":
        cont = linea.split(",")
        
        diccio = {}
        for i in range(len(encabezado)):
            diccio[encabezado[i]] = cont[i]
        
        if diccio['genre'] not in dicc:
            dicc[diccio['genre']] = []
            dicc[diccio['genre']].append(diccio)
            
        elif diccio['genre'] in dicc:
            dicc[diccio['genre']].append(diccio)
            
        linea = archivo.readline().strip()
    
    return dicc


def bus_popu(cupicharts: dict, artista_buscado: str, popularidad_min: int, popularidad_max: int) -> list:
    
    lista = []
    
    for genero in cupicharts:
        c = 0
        while c < len(cupicharts[genero]):
            if cupicharts[genero][c]["performer"] == artista_buscado and int(cupicharts[genero][c]["popularity"]) >= popularidad_min and int(cupicharts[genero][c]["popularity"]) <= popularidad_max:
                lista.append(cupicharts[genero][c])
            c += 1
                
    return lista

def buscar_canciones_por_genero_anio_explicitud(cupicharts: dict, genero_buscado: str, anio_lanzamiento_buscado: str, criterio_explicito_buscado: bool):
    
    lista = []
    
    g_bus = cupicharts[genero_buscado]
    for i in g_bus:
        if i["release_date"] == anio_lanzamiento_buscado and i["explicit"] == criterio_explicito_buscado:
            lista.append(i)
            
    return lista
    
def buscar_cancion_mas_escuchada(cupicharts: dict) -> dict:    
    if cupicharts == {}:
        return {}
    
    generos = list(cupicharts.keys())
    mas_esc = cupicharts[generos[0]][0]
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["play_count"] > mas_esc["play_count"]:
                mas_esc = c
                
    return mas_esc
    
def obtener_apariciones_posicion(cupicharts: dict, posicion_buscada: int) -> int:
    
    cuenta_p = 0
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if int(c["peak_pos"]) == posicion_buscada:
                cuenta_p += 1
        
    return cuenta_p


def buscar_posicion_mas_frecuente(cupicharts: dict) -> dict:

    if cupicharts == {}:
        return {"posicion":0, 
                "cantidad":0}
    
    max_pos = 1
    p_can = 0
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if int(c["peak_pos"]) == 1:
                p_can += 1
            if int(c["peak_pos"]) > max_pos:
                max_pos = int(c["peak_pos"])
    
    dicci = {"posicion":1,
             "cantidad":p_can}
    pos = 1
    
    while pos <= max_pos:
        temp = 0
        for genero in cupicharts:
            for c in cupicharts[genero]:
                if int(c["peak_pos"]) == pos:
                    temp += 1
        if temp > dicci["cantidad"]:
            dicci["posicion"] = pos
            dicci["cantidad"] = temp
        pos += 1
            
    return dicci
            
    


#def prueba(cupicharts:dict):
#   print()
    
#print(cargar_cupicharts(archi))
#print(bus_popu(cargar_cupicharts(archi), "Kendrick Lamar", 94, 98))
#print(prueba1(cargar_cupicharts(archi), "Kendrick Lamar", 15, 98))
#print(buscar_canciones_por_genero_anio_explicitud(cargar_cupicharts(archi), "country", "2025-05-23", 'False'))
#print(buscar_cancion_mas_escuchada(cargar_cupicharts(archi)))
#print(obtener_apariciones_posicion(cargar_cupicharts(archi), 1))
print(buscar_posicion_mas_frecuente(cargar_cupicharts(archi)))
#print(prueba(cargar_cupicharts(archi)))