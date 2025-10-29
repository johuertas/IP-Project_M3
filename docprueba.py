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
        for i in range(len(cupicharts[genero])):
            if cupicharts[genero][i]["performer"] == artista_buscado and (cupicharts[genero]["popularity"] >= popularidad_min and cupicharts[genero][i]["popularity"] <= popularidad_max):
                lista.append(genero[i])
                
    return lista
    
    
    
#print(cargar_cupicharts(archi))
print(bus_popu(cargar_cupicharts(archi), "Kendrick Lamar", 15, 98))