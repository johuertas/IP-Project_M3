#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cupicharts as c

##### Funciones auxiliares (NO MODIFICAR):

def mostrar_cancion(cancion: dict) -> None:
    """
    Muestra la información de una canción en Cupicharts.

    Parámetros:
        cancion (dict): Diccionario con la información de la canción.
    """
    if cancion is not None and cancion != {}:
        print("\n")
        print("#" * 50)
        
        print((
            "Título: {}\n"
            "Fecha en el top: {}\n"
            "Artista: {}\n"
            "Posición máxima: {}\n"
            "Semanas en el top: {}\n"
            "Álbum: {}\n"
            "Fecha de lanzamiento: {}\n"
            "Popularidad: {}\n"
            "Explícita: {}\n"
            "Número de oyentes: {}\n"
            "Número de reproducciones: {}\n"
            "Duración: {}\n"
        ).format(
            cancion["title"], cancion["chart_week"],
            cancion["performer"], cancion["peak_pos"],
            cancion["wks_on_chart"], cancion["album_name"],
            cancion["release_date"], cancion["popularity"],
            cancion["explicit"], cancion["listeners"],
            cancion["play_count"], cancion["duration_s"]
        ))
        print("#" * 50)
    else:
        print("Error: Diccionario de canción inválido.")
    
def mostrar_canciones(canciones: list) -> None:
    """
    Muestra la información de una lista de canciones en Cupicharts.

    Parámetros:
        canciones (list): Lista de diccionarios con la información de las canciones.
    """
    if canciones is not None and canciones != []:
        print("\n Canciones en Cupicharts:")
        print("-" * 50)
        
        for cancion in canciones:
            mostrar_cancion(cancion)
        
        print("-" * 50)
    else:
        print("Error: Lista de canciones inválida.")
        
def mostrar_canciones_en_album(canciones: list) -> None:
    """
    Muestra los títulos de las canciones en un álbum específico.

    Parámetros:
        canciones (list): Lista con los títulos de las canciones del álbum.
    """
    if canciones is not None and canciones != []:
        print("\n Canciones en el álbum:")
        print("-" * 50)
    
        for cancion in canciones:
            print(cancion)
            
        print("-" * 50)
    else:
        print("Error: Lista de canciones inválida.")
##### Fin de funciones auxiliares



# Funciones a implementar (solo aquellas con TODOs):

# Función 2:
def ejecutar_buscar_canciones_por_artista_popularidad(cupicharts: dict) -> None:
    """
    Ejecuta la búsqueda de las canciones de un artista con un rango de popularidad específico.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
    
    Se debe pedir al usuario el nombre del artista y un rango de popularidad (mínima y máxima).
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentran canciones que cumplan con el artista y el rango de popularidad, se muestra el siguiente mensaje:
            - "No se encontraron canciones del artista [X] con popularidad entre [Y] y [Z]."
            
        - Si se encuentran canciones, se imprime el mensaje:
            - "Las canciones del artista [X] con popularidad entre [Y] y [Z] son:"
            Luego, se usa la función auxiliar mostrar_canciones() para mostrar las canciones encontradas.

        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
            
        Donde: 
            - [X] es el nombre del artista ingresado por el usuario.
            - [Y] es la popularidad mínima ingresada por el usuario.
            - [Z] es la popularidad máxima ingresada por el usuario.
    """
    # TODO 10: Implemente la función tal y como se describe en la documentación.
    
    X = input("Nombre del artista: ")
    Y = int(input("Popularidad mínima: "))
    Z = int(input("Popularidad máxima: "))
    
    respuesta = c.buscar_canciones_por_artista_popularidad(cupicharts, X, Y, Z)
    
    if respuesta == []:
        print("No se encontraron canciones del artista [X] con popularidad entre [Y] y [Z].")
    else:
        for i in respuesta:
            print("Las canciones del artista", X, "Con popularidad entre", Y, "y", Z)
            mostrar_canciones(i)
        

# Función 3:
def ejecutar_buscar_canciones_por_genero_anio_explicitud(cupicharts: dict) -> None:
    """
    Ejecuta la búsqueda de las canciones de un género musical específico lanzadas en un año determinado, con una opción para filtrar por canciones con letras explícitas.
    
    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
        
    Se debe pedir al usuario el género musical, el año de lanzamiento y si desea filtrar por canciones con letras explícitas.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentran canciones que cumplan con el género musical, el año y la opción de explícito, se muestra el siguiente mensaje:
            - "No se encontraron canciones del género musical [X] lanzadas en el año [Y] con la opción de explícito [Z]."
            
        - Si se encuentran canciones, se imprime el mensaje:
            - "Las canciones del género musical [X] lanzadas en el año [Y] con la opción de explícito [Z] son:"
            Luego, se usa la función auxiliar mostrar_canciones() para mostrar las canciones encontradas.
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
            
        Donde:
            - [X] es el género musical ingresado por el usuario.
            - [Y] es el año de lanzamiento ingresado por el usuario.
            - [Z] es la opción de explícito ingresada por el usuario (True o False).
    """
    # TODO 11: Implemente la función tal y como se describe en la documentación.
    pass

# Función 4:
def ejecutar_buscar_cancion_mas_escuchada(cupicharts: dict) -> None:
    """
    Ejecuta la búsqueda de la canción más escuchada en Cupicharts.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentra ninguna canción, se muestra el siguiente mensaje:
            - "No se encontraron canciones en Cupicharts."

        - Si se encuentra una canción, se imprime el encabezado:
            - "La canción más escuchada es: "
            Luego, se usa la función auxiliar mostrar_cancion() para mostrar la información de la canción encontrada.
    """
    # TODO 12: Implemente la función tal y como se describe en la documentación.
    pass


# Función 5:
def ejecutar_obtener_apariciones_posicion(cupicharts: dict) -> None:
    """
    Ejecuta la función para obtener el número total de canciones que alcanzaron una posición específica en el chart.
    
    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.

    Se debe pedir al usuario la posición del chart a buscar.
    
    Existen 2 casos posibles para mostrar el resultado:

        - Si se encuentra la posición, se imprime el mensaje:
            - "La posición #[X] fue alcanzada por [Y] canciones."

        - Si no se encuentra la posición o no hay canciones en esa posición, se muestra el siguiente mensaje:
            - "No se encontraron canciones para la posición #[X]."
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
        
        Donde:
            - [X] es la posición del chart ingresada por el usuario.
            - [Y] es el número total de canciones que alcanzaron esa posición.
    """
    # TODO 13: Implemente la función tal y como se describe en la documentación.
    pass
        

# Función 6:
def ejecutar_buscar_posicion_mas_frecuente(cupicharts: dict) -> None:
    """
    Ejecuta la búsqueda de la posición alcanzada por más canciones en Cupicharts.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
    
    Existen 2 casos posibles para mostrar el resultado:
        
        - Si no se encuentra ninguna posición, se muestra el siguiente mensaje:
            - "No se encontraron posiciones en Cupicharts."

        - Si se encuentra una posición, se imprime el mensaje:
            - "La posición más frecuente es #[X] y fue alcanzada por [Y] canciones."

        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
        
        Donde:
            - [X] es el número de posición.
            - [Y] es el número total de canciones que alcanzaron esa posición.
    """
    # TODO 14: Implemente la función tal y como se describe en la documentación.
    pass


# Función 7:
def ejecutar_crear_url_canciones(cupicharts: dict) -> None:
    """
    Ejecuta la función para crear URLs de canciones en Cupicharts.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
    
    A modo de ejemplo, se muestra la URL generada para la primera canción del género musical "pop" en Cupicharts.
    
    El mensaje tiene el siguiente formato:
        "La URL de la canción [A] hecha por el artista [B] y alcanzando el chart en el [C] es: [D]"
        
        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
        
        Donde:
            - [A] es el título de la canción.
            - [B] es el nombre del artista.
            - [C] es la fecha en que alcanzó el chart.
            - [D] es la URL generada para la canción.
    """
    if "pop" in cupicharts and cupicharts["pop"] != []:
        c.crear_url_canciones(cupicharts)
        primera_cancion = cupicharts["pop"][0]
        print("La URL de la canción", primera_cancion["title"], "hecha por el artista", primera_cancion["performer"], "y alcanzando el chart en el", primera_cancion["chart_week"], "es:", primera_cancion["url"])
        
        
# Función 8:
def ejecutar_recomendar_cancion(cupicharts: dict) -> None:
    """
    Ejecuta la función para recomendar una canción en Cupicharts.

    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
        
    Se le debe pedir al usuario los siguientes criterios:
        - Género musical de la canción a buscar.
        - Número de oyentes mínimo.
        - Duración mínima de la canción en segundos.
        - Duración máxima de la canción en segundos.
        - Fecha de lanzamiento mínima (en formato YYYY-MM-DD).
        - Fecha de lanzamiento máxima (en formato YYYY-MM-DD).
    
    Existen 2 casos posibles para mostrar el resultado:
        - Si no se encuentra ninguna canción que cumpla con los criterios, se muestra el siguiente mensaje:
            - "No se encontró ninguna canción que cumpla con los criterios."
            
        - Si se encuentra una canción, se imprime el encabezado:
            - "La canción recomendada es: "
            Luego, se usa la función auxiliar mostrar_cancion() para mostrar la información de la canción encontrada. 
    """
    # TODO 15: Implemente la función tal y como se describe en la documentación.
    pass


# Función 9:
def ejecutar_relacionar_album_con_canciones(cupicharts: dict) -> None:
    """
    Ejecuta la función que relaciona el álbum con las canciones que lo componen por medio de un diccionario.
    
    Parámetros:
        cupicharts (dict): Diccionario con la información de las canciones en Cupicharts.
        
    Se le debe pedir al usuario el nombre del álbum a buscar.
    
    Existen 2 casos posibles para mostrar el resultado:
        - Si no se encuentra el álbum, se muestra el siguiente mensaje:
            - "No se encontró el álbum [X]."
            
        - Si se encuentra el álbum, se imprime el mensaje:
            - "Las canciones del álbum [X] son:"
            Luego, se usa la función auxiliar mostrar_canciones_en_album() para mostrar las canciones del álbum encontrado.
            
        Nota: Aquí, los corchetes se usan para indicar la ubicación de la información definida a continuación.
        
        Donde:
            - [X] es el nombre del álbum ingresado por el usuario.
    """
    album = input("Ingrese el nombre del álbum: ")
    albumes = c.relacionar_album_con_canciones(cupicharts)
    if album in albumes:
        print("Las canciones del álbum", album, "son:")
        mostrar_canciones_en_album(albumes[album])
    else:
        print("No se encontró el álbum " + album + ".")
        
        
###### Funciones del menú (NO MODIFICAR):
def iniciar_aplicacion() -> None:
    """
    Función principal de la aplicación.
    """
    ejecutando = False
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si su archivo se llama cupicharts.csv: ")
    if archivo == "":
        archivo = "cupicharts.csv"
        
    cupicharts = c.cargar_cupicharts(archivo)
    if cupicharts != {} and cupicharts is not None:
        ejecutando = True
        print("#" * 50)
        print("¡Bienvenido a la aplicación de Cupicharts!")
        print("#" * 50)
        
        while ejecutando:
            ejecutando = mostrar_menu_principal(cupicharts)
            if ejecutando:
                input("Presione Enter para continuar...")
    else:
        print("\nError: No se ha podido cargar el archivo. \nRevise su implementación de la función: cargar_cupicharts() en cupicharts.py")


def mostrar_menu_principal(cupicharts: dict) -> bool:
    """
    Muestra el menú principal de la aplicación y ejecuta la opción seleccionada por el usuario.

    Parámetros:
        cupicharts (dict): Diccionario con las canciones de Cupicharts.
    
    Retorna:
        bool: True si se desea continuar, False si se desea salir.
    """
    print("\nMenú de opciones:")
    print("1. Buscar canciones por artista y rango de popularidad.")
    print("2. Buscar canciones por género musical, año y explicitud.")
    print("3. Buscar canción más escuchada.")
    print("4. Obtener el número de canciones que alcanzaron una posición máxima determinada.")
    print("5. Obtener la posición más frecuente en Cupicharts")
    print("6. Crear URLs para las canciones.")
    print("7. Recomendar una canción.")
    print("8. Relacionar un álbum con sus canciones.")
    print("9. Salir.")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_canciones_por_artista_popularidad(cupicharts)
    elif opcion_elegida == "2":
        ejecutar_buscar_canciones_por_genero_anio_explicitud(cupicharts)
    elif opcion_elegida == "3":
        ejecutar_buscar_cancion_mas_escuchada(cupicharts)
    elif opcion_elegida == "4":
        ejecutar_obtener_apariciones_posicion(cupicharts)
    elif opcion_elegida == "5":
        ejecutar_buscar_posicion_mas_frecuente(cupicharts)
    elif opcion_elegida == "6":
        ejecutar_crear_url_canciones(cupicharts)
    elif opcion_elegida == "7":
        ejecutar_recomendar_cancion(cupicharts)
    elif opcion_elegida == "8":
        ejecutar_relacionar_album_con_canciones(cupicharts)
    elif opcion_elegida == "9":
        print("\n¡Gracias por usar la aplicación de Cupicharts!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Por favor inténtelo de nuevo.")
    
    return continuar_ejecutando


if __name__ == "__main__":
    iniciar_aplicacion()