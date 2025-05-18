
from typing import Tuple
import pandas as pd

def imprimir_matriz(matriz):
    df = pd.DataFrame(matriz)
    print(df)

MOVIMIENTOS = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
def obtener_nuevas_pos_locales(mat: list, pos: Tuple[int,int]) -> list:
    '''
    Función que, a partir de una matriz de tamaño f x c y una posición (pos), devuelve una lista con las nuevas posiciones 
    posibles para un caballo de ajedrez dada su posición actual.
    '''
    nuevas_pos = []
    for mov in MOVIMIENTOS: # Se comprueba cada uno de los movimientos posibles del caballo
        nueva_pos = (pos[0] + mov[0], pos[1] + mov[1])
        if 0 <= nueva_pos[0] < len(mat) and 0 <= nueva_pos[1] < len(mat[0]): # Se comprueba que la nueva posición esté dentro de los límites de la matriz
            nuevas_pos.append(nueva_pos)
    return nuevas_pos

def generar_nuevas_pos_posibles(mat: list) -> dict:
    '''
    Función que, a partir de una matriz de tamaño f x c, devuelve un diccionario con las nuevas siguientes posiciones posibles para cada posición de la matriz, dada la forma de moverse del caballo de ajedrez.
    '''
    nuevas_pos_posibles = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = True # Se simula que el caballo ha pasado por la posición (i, j)
            nuevas_pos_locales = obtener_nuevas_pos_locales(mat, (i, j))
            nuevas_pos_locales.sort(key=lambda x: len(obtener_nuevas_pos_locales(mat, x))) # Se ordenan las nuevas posiciones posibles por el número de nuevas posiciones posibles que tienen a su vez
            nuevas_pos_posibles[(i, j)] = nuevas_pos_locales # Se añaden al diccionario
            mat[i][j] = False # Se desmarca la posición (i, j) como ocupada por el caballo
    return nuevas_pos_posibles

def caballo_llega_a_todo_aux(mat: list, nuevas_pos_posibles: dict, pos: Tuple[int,int], recorridos: int, totales: int, camino: list) -> Tuple[bool, list]:
    '''
    Función auxiliar que, a partir de una matriz de tamaño f x c y una posición inicial para un caballo de ajedrez (pos), devuelve True si el caballo puede llegar a todas las posiciones de la matriz y una lista con el recorrido del caballo.
    Para saber si el caballo ha recorrido todas las posiciones, se usan las variables recorridos (número de posiciones recorridas) y totales (número total de posiciones de la matriz).
    '''
    if recorridos == totales: #Se han recorrido todas las posiciones (se hace así para evitar comprobar la matriz entera)
        return (True, camino) # Se devuelve que existe solución, junto con el camino recorrido
    
    #Si aún faltan posiciones por recorrer, se plantean las nuevas posiciones posibles dada la posición actual
    for nueva_pos in nuevas_pos_posibles[pos]:
        if not mat[nueva_pos[0]][nueva_pos[1]]: # Se comprueba que la nueva posición no haya sido recorrida
            # Se marca la nueva posición como recorrida y se añade al camino
            mat[nueva_pos[0]][nueva_pos[1]] = True
            camino.append(nueva_pos)

            # Se llama recursivamente a la función para comprobar si desde la nueva posición se puede llegar a todas las posiciones
            if caballo_llega_a_todo_aux(mat, nuevas_pos_posibles, nueva_pos, recorridos + 1, totales, camino)[0]:
                return (True, camino)
            
            # Si no, se hace backtracking desmarcando la posición recorrida y eliminándola del camino
            mat[nueva_pos[0]][nueva_pos[1]] = False
            camino.pop()
    # Si ninguna de las nuevas posiciones posibles lleva a una solución, se devuelve False para hacer backtracking
    return (False, None)

def caballo_llega_a_todo(f: int, c: int, pos: Tuple[int, int]) -> Tuple[bool, list]:
    '''
    Función que, a partir de una matriz de tamaño f x c y una posición inicial para un caballo de ajedrez (pos), devuelve True si el caballo puede llegar a todas las posiciones de la matriz y una lista con el recorrido del caballo.
    
    Si no puede llegar a todas las posiciones, devuelve False y una lista vacía.

    Si la posición inicial está fuera de los límites de la matriz, lanza un ValueError.

    >>> caballo_llega_a_todo(8, 8, (7, 1)) # doctest: +ELLIPSIS
    (True, ...)
    >>> caballo_llega_a_todo(3, 3, (0, 0)) # doctest: +ELLIPSIS
    (False, None)
    >>> caballo_llega_a_todo(5, 5, (2, 2)) # doctest: +ELLIPSIS
    (True, ...)
    '''
    if not(0 <= pos[0] < f and 0 <= pos[1] < c):
        raise ValueError("Posición inicial fuera de los límites de la matriz")
    # Creación de una matriz de tamaño f x c para saber si el caballo ha pasado por una posición o no
    # (True si ha pasado, False si no ha pasado)
    matriz = []
    for i in range(f):
        matriz.append([])
        for _ in range(c):
            matriz[i].append(False)

    #Generación de una lista de posiciones posibles para el caballo dada su posición inicial
    # Las posiciones posibles están ordenadas por el número de posiciones posibles que tiene a su vez cada una de ellas
    nuevas_pos_posibles = generar_nuevas_pos_posibles(matriz)
    matriz[pos[0]][pos[1]] = True # Se marca la posición inicial como ocupada por el caballo como visitada
    resultado = caballo_llega_a_todo_aux(matriz, nuevas_pos_posibles, pos, 1, f*c, [pos])
    return resultado
def imprimir_resultado_caballo(resultado: Tuple[bool, list], f: int, c: int) -> None:
    if resultado[0]:
        print("El caballo puede llegar a todas las posiciones de la matriz.")
        print("Recorrido del caballo:")
        matriz_expl = []
        for i in range(f):
            matriz_expl.append([])
            for j in range(c):
                matriz_expl[i].append(resultado[1].index((i, j)))
        print("Pasos de la solución:\n")
        imprimir_matriz(matriz_expl)
    else:
        print("El caballo no puede llegar a todas las posiciones de la matriz.")
def obtener_matriz(cual: int) -> dict:
    '''
    Función auxiliar de se_puede_reducir: sencillamente guarda los diccionarios de transformación para cada uno de los casos.
    '''
    match cual:
        case 1:
            # Diccionario del enunciado
            return {"a":{"a":"b", "b":"b", "c":"a", "d":"d"}, "b":{"a":"c", "b":"a", "c":"d", "d":"a"}, "c":{"a": "b", "b":"a", "c":"c", "d":"c"}, "d":{"a":"d", "b":"c", "c":"d", "d":"b"}}
        case 2:
            # Diccionario propio para hacer más casos de prueba
            return {"n":{"n":"n","a":"a","f":"f", "p":"p"}, "a":{"n":"n","a":"n","f":"a","p":"f"}, "f":{"n":"n","a":"p","f":"n","p":"f"}, "p":{"n":"n","a":"p","f":"a","p":"n"}}
    return {}

def se_puede_reducir(cadena: str, c_final: str, matriz: dict, camino: list = []) -> Tuple[bool, list]:
    '''
    Función que, a partir de una cadena de caracteres y un diccionario de transformación, devuelve True si se puede reducir la cadena a un solo carácter (c_final) y una lista con el camino seguido para llegar a la solución.

    El diccionario de transformación es un diccionario que contiene las transformaciones posibles para cada par de caracteres de la cadena (p.ej: "ab"->"b", "cd"->"a").

    >>> se_puede_reducir("ccccccccc", "d", obtener_matriz(1))
    (False, [])
    >>> se_puede_reducir("acabada", "d", obtener_matriz(1))
    (True, [('aabada', 0), ('bbada', 0), ('aada', 0), ('ada', 1), ('da', 0), ('d', 0)])
    >>> se_puede_reducir("cacccb", "a", obtener_matriz(1))
    (True, [('bcccb', 0), ('bccb', 1), ('bca', 2), ('bb', 1), ('a', 0)])
    >>> se_puede_reducir("fafapaannnnna","f", obtener_matriz(2))
    (True, [('pfapaannnnna', 0), ('aapaannnnna', 0), ('afaannnnna', 1), ('apannnnna', 1), ('apnnnnna', 1), ('apnnnna', 2), ('apnnna', 2), ('apnna', 2), ('apna', 2), ('apa', 2), ('ap', 1), ('f', 0)])
    '''
    if len(cadena) == 1:
        return (cadena == c_final, camino) # Si la cadena tiene un solo carácter, se comprueba si es igual al carácter final
    for i in range(len(cadena) - 1): # Se recorre la cadena buscando pares de caracteres que se puedan transformar
        cadena_nueva = cadena[:i] + matriz[cadena[i]][cadena[i+1]] + cadena[i+2:] # Se transforma la cadena aplicando la transformación del diccionario a un par de caracteres
        resultado = se_puede_reducir(cadena_nueva, c_final, matriz, camino + [(cadena_nueva, i)]) # Se llama recursivamente a la función para comprobar si se puede reducir la cadena transformada a un solo carácter
        if resultado[0]:
            return (True, resultado[1])
    # Si aun probando todas las combinaciones de transformación no se ha llegado a la solución, se devuelve False
    return (False, camino)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
