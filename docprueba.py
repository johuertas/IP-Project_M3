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

def crear_url_canciones(cupicharts: dict) -> None: 

    for genero in cupicharts:
        for c in cupicharts[genero]:
            gen = genero.replace(" ", "")
            can_art = c["title"].lower().replace(" ", "") + "-" + c["performer"].lower().replace(" ", "")
            if len(can_art) > 30:
                can_art = can_art[:30]
            f_chart = c["chart_week"].replace("-", "")
            
            link = "https://www.cupicharts.com/canciones/" + gen + "/" + can_art + "/" + f_chart
            
            c["url"] = link
            
    return cupicharts


def recomendar_cancion(
        cupicharts: dict,
        genero_buscado: str,
        listeners_min: int,
        duracion_min: float,
        duracion_max: float,
        fecha_lanzamiento_min: str,
        fecha_lanzamiento_max: str
    ) -> dict:

    if cupicharts == {}:
        return {}
    
    pos_fre = buscar_posicion_mas_frecuente(cargar_cupicharts(archi))
    pos_fre = pos_fre["posicion"]
    
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if int(c["peak_pos"]) == pos_fre and \
               c["genre"] == genero_buscado and \
               int(c["listeners"]) >= listeners_min and \
               (float(c["duration_s"]) >= duracion_min and float(c["duration_s"]) <= duracion_max) and \
               (c["release_date"] >= fecha_lanzamiento_min and c["release_date"] <= fecha_lanzamiento_max):
                   return c
               
    return {}

    
    
"""def prueba(cupicharts:dict):
    for genero in cupicharts:
        for c in cupicharts[genero]:"""
    
#print(cargar_cupicharts(archi))
#print(bus_popu(cargar_cupicharts(archi), "Kendrick Lamar", 94, 98))
#print(buscar_canciones_por_genero_anio_explicitud(cargar_cupicharts(archi), "country", "2025-05-23", 'False'))
#print(buscar_cancion_mas_escuchada(cargar_cupicharts(archi)))
#print(obtener_apariciones_posicion(cargar_cupicharts(archi), 1))
#print(buscar_posicion_mas_frecuente(cargar_cupicharts(archi)))
#print(crear_url_canciones(cargar_cupicharts(archi)))
print(recomendar_cancion(cargar_cupicharts(archi), "country", 100, 110.0, 225.0, "2020-01-01", "2025-09-11"))
#print(prueba(cargar_cupicharts(archi)))
