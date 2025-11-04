#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Función 1:
def cargar_cupicharts(ruta_archivo: str) -> dict:
    """
    Carga un archivo CSV (Comma-Separated Values) con la información de las canciones 
    y la organiza en un diccionario donde las llaves son los géneros musicales.

    Parámetros:
        ruta_archivo (str): Ruta al archivo CSV con la información musical.
        Ejemplo: "./cupicharts.csv" (si el archivo CSV está en el mismo directorio que este archivo).

    Retorno:
        dict: Diccionario estructurado de la siguiente forma:

            - Las llaves representan los géneros musicales de las canciones.
                - El género musical al cual pertenece cada canción se encuentra en la columna "genre" del archivo CSV.
                - El género musical es un string no vacío, en minúscula y sin espacios al inicio o al final. 
                  Ejemplo: "pop".

            - Los valores son listas de diccionarios, donde cada diccionario representa una canción.
                - Cada diccionario contiene los siguientes campos basados en las columnas del archivo CSV:

                    "title" (str): Título de la canción.
                                   Ejemplo: "Die With a Smile"
                                   
                    "chart_week" (str): Semana en que alcanzó el chart en formato "YYYY-MM-DD".
                                        Ejemplo: "2025-06-28"
                                        
                    "performer" (str): Artista o intérprete de la canción.
                                       Ejemplo: "Lady Gaga"
                                       
                    "peak_pos" (int): Posición máxima alcanzada en el chart.
                                      Ejemplo: 1
                                      
                    "wks_on_chart" (int): Número de semanas que la canción ha estado en el chart.
                                          Ejemplo: 44
                                          
                    "album_name" (str): Nombre del álbum al que pertenece la canción.
                                        Ejemplo: "Die With A Smile"
                                        
                    "release_date" (str): Fecha de lanzamiento de la canción en formato "YYYY-MM-DD".
                                          Ejemplo: "2024-08-16"
                                          
                    "popularity" (int): Popularidad de la canción en una escala del 1 al 100.
                                        Ejemplo: 98
                                        
                    "explicit" (bool): Indica si la canción tiene contenido explícito.
                                       Ejemplo: False
                                       
                    "listeners" (int): Número de oyentes que han escuchado la canción.
                                       Ejemplo: 1412509
                                       
                    "play_count" (int): Número de reproducciones de la canción.
                                        Ejemplo: 23765285
                                        
                    "duration_s" (float): Duración de la canción en segundos.
                                          Ejemplo: 251.667
                                          
                    "genre" (str): Género musical de la canción.
                                   Ejemplo: "art pop"
                                   
    Notas importantes:
        1. Al usar readline(), agregue strip() de esta forma: readline().strip() para garantizar que se eliminen los saltos de línea.
            - Documentación de str.strip(): https://docs.python.org/es/3/library/stdtypes.html#str.strip
            - Documentación de readline(): https://docs.python.org/es/3/tutorial/inputoutput.html#methods-of-file-objects
            
        2. Al usar open(), agregue la codificación "utf-8" de esta forma: open(archivo, "r", encoding="utf-8") para garantizar la lectura de caracteres especiales del archivo CSV.               
    """
    # TODO 1: Implemente la función tal y como se describe en la documentación.
    
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    
    dicc = {}
    
    encabezado = archivo.readline().strip().split(',')
    
    linea = archivo.readline().strip()
    
    while linea != "":
        cont = linea.split(",")
        
        diccio = {}
        for i in range(len(encabezado)):
            
            if cont[i].isnumeric() == True:
                diccio[encabezado[i]] = int(cont[i])
            elif cont[i] == 'True' or cont[i] == 'False':
                diccio[encabezado[i]] = bool(cont[i])
            elif cont[i].replace(".", "").isnumeric() == True and "." in cont[i]:
                diccio[encabezado[i]] = float(cont[i])
            else:
                diccio[encabezado[i]] = cont[i]
            
        
        if diccio['genre'] not in dicc:
            dicc[diccio['genre']] = []
            dicc[diccio['genre']].append(diccio)
            
        elif diccio['genre'] in dicc:
            dicc[diccio['genre']].append(diccio)
            
        linea = archivo.readline().strip()
    
    return dicc
    
    


# Función 2:
def buscar_canciones_por_artista_popularidad(cupicharts: dict, artista_buscado: str, popularidad_min: int, popularidad_max: int) -> list:
    """
    Busca canciones de un artista específico y cuyo nivel de popularidad esté dentro del rango proporcionado.

    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
        artista_buscado (str): Nombre del artista a buscar.
        popularidad_min (int): Valor mínimo de popularidad en el rango de 1-100 (inclusivo).
        popularidad_max (int): Valor máximo de popularidad en el rango de 1-100 (inclusivo).

    Notas:
        - La búsqueda es sensible a mayúsculas y minúsculas, por lo que el nombre del artista debe coincidir exactamente.
        - La popularidad de las canciones debe estar en el rango de popularidad_min a popularidad_max, ambos inclusivos, es decir, 
            se consideran también las canciones cuya popularidad es igual a popularidad_min o popularidad_max.
        
    Retorno:
        list: Lista de diccionarios que representan las canciones que cumplen con las condiciones.
              Si no hay coincidencias, se retorna una lista vacía.
    """
    # TODO 2: Implemente la función tal y como se describe en la documentación.
    
    lista = []
    
    for genero in cupicharts:
        c = 0
        while c < len(cupicharts[genero]):
            if cupicharts[genero][c]["performer"] == artista_buscado and cupicharts[genero][c]["popularity"] >= popularidad_min and cupicharts[genero][c]["popularity"] <= popularidad_max:
                lista.append(cupicharts[genero][c])
            c += 1
                
    return lista
    


# Función 3:
def buscar_canciones_por_genero_anio_explicitud(cupicharts: dict, genero_buscado: str, anio_lanzamiento_buscado: str, criterio_explicito_buscado: bool) -> list:
    """
    Busca canciones de un género musical específico, lanzadas en un año determinado y que coincidan con el criterio de contenido explícito.

    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
        genero_buscado (str): Género musical de la canción a buscar. Debe tener una coincidencia exacta.
        anio_lanzamiento_buscado (str): Año de lanzamiento de la canción en formato "YYYY".
        criterio_explicito_buscado (bool): Indica si se busca contenido explícito (True) o no explícito (False).

    Notas:
        - La búsqueda es sensible a mayúsculas y minúsculas, por lo que el género musical debe coincidir exactamente.
        - El campo "explicit" del diccionario debe coincidir con el valor booleano proporcionado (True o False).
        
    Retorno:
        list: Lista de diccionarios de canciones que cumplen con todas las condiciones.
              Si no hay coincidencias, se retorna una lista vacía.
    """
    # TODO 3: Implemente la función tal y como se describe en la documentación.
    
    lista = []
    
    g_bus = cupicharts[genero_buscado]
    for i in g_bus:
        if anio_lanzamiento_buscado in i["release_date"] and i["explicit"] == criterio_explicito_buscado:
            lista.append(i)
            
    return lista

# Función 4:
def buscar_cancion_mas_escuchada(cupicharts: dict) -> dict:
    """
    Busca la canción más escuchada dentro de todas las canciones de Cupicharts.
    Se considera la canción más escuchada aquella que tiene la mayor cantidad de reproducciones.
    
    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
    
    Retorno:
        dict: La canción más escuchada, representada como un diccionario.
                Si no hay canciones en el diccionario, se retorna un diccionario vacío.
                Si hay varias canciones con la misma cantidad de reproducciones, retorna la primera encontrada.
    """
    # TODO 4: Implemente la función tal y como se describe en la documentación.
       
    if cupicharts == {}:
        return {}
    
    generos = list(cupicharts.keys())
    mas_esc = cupicharts[generos[0]][0]
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["play_count"] > mas_esc["play_count"]:
                mas_esc = c
                
    return mas_esc
        

# Función 5:
def obtener_apariciones_posicion(cupicharts: dict, posicion_buscada: int) -> int:
    """
    Obtiene el número de canciones que tuvieron una posición máxima específica en el chart.
    
    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
        posicion_buscada (int): Posición máxima en el chart a buscar, como un entero positivo.

    Retorno:
        int: Número de canciones que tuvieron la posición máxima especificada.
             Si no se encuentran canciones con dicha posición, retorna 0.
    """
    # TODO 5: Implemente la función tal y como se describe en la documentación.
    
    cuenta_p = 0
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["peak_pos"] == posicion_buscada:
                cuenta_p += 1
        
    return cuenta_p
    


# Función 6:
def buscar_posicion_mas_frecuente(cupicharts: dict) -> dict:
    """
    Busca la posición máxima más frecuente dentro de todas las canciones de Cupicharts.
    Se considera la posición más frecuente a aquella que tiene la mayor cantidad de canciones en dicha posición.
    
    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
    
    Retorno:   
        dict: Un diccionario con las siguientes llaves:
            - "posicion": (int) La posición máxima más frecuente.
            - "cantidad": (int) Número de canciones que alcanzaron esa posición.
            
            Si hay más de una posición con la misma cantidad de canciones, se retorna la primera posición encontrada.
            Si no hay canciones en el diccionario, se retorna el siguiente diccionario:
            {"posicion": 0, "cantidad": 0}
    """
    # TODO 6: Implemente la función tal y como se describe en la documentación.
    
    if cupicharts == {}:
        return {"posicion":0, 
                "cantidad":0}
    
    max_pos = 1
    p_can = 0
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["peak_pos"] == 1:
                p_can += 1
            if c["peak_pos"] > max_pos:
                max_pos = c["peak_pos"]
    
    dicci = {"posicion":1,
             "cantidad":p_can}
    pos = 1
    
    while pos <= max_pos:
        temp = 0
        for genero in cupicharts:
            for c in cupicharts[genero]:
                if c["peak_pos"] == pos:
                    temp += 1
        if temp > dicci["cantidad"]:
            dicci["posicion"] = pos
            dicci["cantidad"] = temp
        pos += 1
            
    return dicci

# Función 7:
def crear_url_canciones(cupicharts: dict) -> None: 
    """
    Crea una URL para cada canción siguiendo un formato específico y la agrega al diccionario de cada canción.
    Esta función modifica el diccionario recibido como parámetro de forma permanente, añadiendo una nueva llave "url" a cada canción
    con el siguiente formato: "https://www.cupicharts.com/canciones/[X]/[Y]/[Z]
    Nota: Aquí, los corchetes se usan para indicar la ubicación para la información definida a continuación:
    
    Donde:
        - [X]: Género musical de la canción en minúsculas y sin espacios o caracteres especiales.
        - [Y]: Título de la canción y el nombre del artista, separados por un guion (-), en minúsculas y sin espacios ni caracteres especiales.
        - [Z]: Fecha en la que alcanzó el chart, en formato "YYYYMMDD"

    Reglas de formato:
        - El género musical debe estar en minúsculas y sin espacios al inicio o al final.
            - Un caracter es especial si no es alfanumérico (letras y números).
        - El título de la canción y el nombre del artista deben estar en minúsculas, sin espacios ni caracteres especiales, con los dos datos separados por un guion (-).
        - La longitud máxima del titulo de la canción y el nombre del artista combinados es de 30 caracteres (incluyendo el guión). 
            Si excede este límite, se limita a 30 caracteres.
        - La fecha en la que alcanzó el chart debe estar en formato "YYYYMMDD", es decir, sin guiones ni espacios.
        
    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
        
    Ejemplo:
        Para una canción de género musical "Pop", título "Poker Face" y artista "Lady Gaga", en fecha "2025-01-01",
        la URL generada sería: "https://cupicharts.com/canciones/pop/pokerface-ladygaga/20250101"
        
    Nota:
        La función str.isalnum() permite verificar si una cadena es alfanumérica:
        https://docs.python.org/es/3/library/stdtypes.html#str.isalnum
    """
    # TODO 7: Implemente la función tal y como se describe en la documentación.
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            gen = genero.replace(" ", "")
            can_art = c["title"] + "-" + c["performer"] 
            if len(can_art) > 30:
                can_art = can_art[:30]
            f_chart = c["chart_week"].replace("-", "")
            
            link = "https://www.cupicharts.com/canciones/" + gen + "/" + can_art + "/" + f_chart
            
            c["url"] = link
            
    
    

# Función 8:
def recomendar_cancion(
        cupicharts: dict,
        genero_buscado: str,
        listeners_min: int,
        duracion_min: float,
        duracion_max: float,
        fecha_lanzamiento_min: str,
        fecha_lanzamiento_max: str
    ) -> dict:
    """
    Recomienda la primera canción que cumpla con las siguientes condiciones:
        - Su posición máxima alcanzada en el chart (peak_pos) debe ser la más frecuente (Usar la función: buscar_posicion_mas_frecuente()).
        - Pertenerce al género dado por parámetro.
        - Su número de oyentes (listeners) es mayor o igual a listeners_min.
        - Su duración está dentro del rango de duración especificado (inclusivo).
        - Su fecha de lanzamiento está dentro del rango de fechas especificado (inclusivo).

    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.
        genero_buscado (str): Género de la canción a buscar. Debe coincidir exactamente con una de las llaves del diccionario.
        listeners_min (int): Número mínimo de oyentes.
        duracion_min (float): Duración mínima de la canción.
        duracion_max (float): Duración máxima de la canción.
        fecha_lanzamiento_min (str): Fecha mínima de lanzamiento en formato "YYYY-MM-DD".
        fecha_lanzamiento_max (str): Fecha máxima de lanzamiento en formato "YYYY-MM-DD".

    Notas:
        - Tenga en cuenta que el número de oyentes mínimo y el rango de duración son inclusivos, 
            es decir, se consideran también las canciones cuyo número de oyentes es igual a listeners_min y cuya 
                duración es igual a duracion_min o duracion_max.
        
    Retorno:
        dict: Primer diccionario de canción que cumpla con todos los criterios.
                  Si no hay coincidencias o el diccionario está vacío, retorna un diccionario vacío.
    """
    # TODO 8: Implemente la función tal y como se describe en la documentación.
    
    if cupicharts == {}:
        return {}
    
    pos_fre = buscar_posicion_mas_frecuente(cupicharts)
    pos_fre = pos_fre["posicion"]
    
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["peak_pos"] == pos_fre and \
               c["genre"] == genero_buscado and \
               c["listeners"] >= listeners_min and \
               c["duration_s"] >= duracion_min and c["duration_s"] <= duracion_max and \
               c["release_date"] >= fecha_lanzamiento_min and c["release_date"] <= fecha_lanzamiento_max:
                   return c
               
    return {}


# Función 9:
def relacionar_album_con_canciones(cupicharts: dict) -> dict:
    """
    Agrupa las canciones por nombre de álbum, creando un diccionario donde las llaves son los nombres de los álbumes
    y los valores son listas con los títulos de las canciones que pertenecen a cada álbum.

    Parámetros:
        cupicharts (dict): Diccionario de canciones agrupadas por género musical.

    Notas:
        - Dentro de cada álbum, no puede haber canciones repetidas.
    
    Retorno:
        dict: Diccionario donde:
            - Las llaves (str) son los nombres de los álbumes.
            - Los valores (list) son listas con los nombres de las canciones del álbum.
    """
    # TODO 9: Implemente la función tal y como se describe en la documentación.
    
    dicc = {}
    
    for genero in cupicharts:
        for c in cupicharts[genero]:
            if c["album_name"] not in dicc:
                dicc[c["album_name"]] = []
                dicc[c["album_name"]].append(c)
            else:
                dicc[c["album_name"]].append(c)
                
    return dicc
                
