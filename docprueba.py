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

def prueba(cupicharts: dict, genero_buscado: str):
    
    lista = []
    
    g_bus = cupicharts[genero_buscado]
    for i in g_bus:
        lista.append(i["explicit"])
        
    return lista
    
    
    
#print(cargar_cupicharts(archi))
#print(bus_popu(cargar_cupicharts(archi), "Kendrick Lamar", 94, 98))
#print(prueba1(cargar_cupicharts(archi), "Kendrick Lamar", 15, 98))
print(buscar_canciones_por_genero_anio_explicitud(cargar_cupicharts(archi), "country", "2025-05-23", 'False'))
#print(prueba(cargar_cupicharts(archi), "country"))