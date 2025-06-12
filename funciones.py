import random

def es_repetido(valor: int, lista: list)-> bool:
    '''
    Verifica si un valor ya existe en una lista.
    
    Parámetros:\n
    valor (int): Es el número a verificar en la lista.
    lista (list): Es la lista donde se busca el número.

    Retorna:\n
    bool: True si el valor está en la lista, False si no está.
    '''
    repetido = False
    for i in range(len(lista)):
        if lista[i] == valor:
            repetido = True
    
    return repetido

def mezclar_lista_original()-> list:
    '''
    Genera una lista con los números del 1 al 9 mezclados sin repeticiones.

    Retorna:\n
    list: Lista mezclada de números del 1 al 9 sin repeticiones.
    '''
    numeros_originales = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista_mezclada = []

    while len(lista_mezclada) < 9:
        indice = random.randint(0, 8)
        numero = numeros_originales[indice]

        if es_repetido(numero, lista_mezclada) == False:
            lista_mezclada.append(numero)

    return lista_mezclada

def rotar(lista: list, posiciones: int)-> list:
    '''
    Rota los elementos de una lista hacia la derecha una cantidad de posiciones.

    Parámetros:\n
    lista (list): La lista a rotar.
    posiciones (int): Cantidad de posiciones a rotar.

    Retorna:\n
    list: Nueva lista rotada.
    '''
    nueva = []
    for i in range(len(lista)):
        nueva.append(lista[(i + posiciones) % len(lista)])

    return nueva

def generar_tablero_sudoku()-> list:
    '''
    Genera un tablero de Sudoku completo de 9x9 basado en una fila base que es rotada.

    Retorna:\n
    list: Matriz de 9 listas (filas) que representan el Sudoku.
    '''
    base = mezclar_lista_original()
    tablero = []

    for i in range(9):
        if i == 0:
            fila = base
        else:
            if i % 3 == 0:
                fila = rotar(tablero[i - 3], 1)
            else:
                fila = rotar(tablero[i - 1], 3)
        tablero.append(fila)

    return tablero
