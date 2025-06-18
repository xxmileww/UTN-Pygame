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

def obtener_porcentaje(dificultad: str)-> float:
    '''
    Obtiene el porcentaje de celdas que tienen que ocultarse según la dificultad elegida.

    Parámetros:\n
    dificultad (str): Nivel de dificultad elegida (Fácil, Intermedio o Difícil)

    Retorna:\n
    float: Porcentaje de celdas a ocultar según el nivel de dificultad.
    '''
    porcentaje = 0
    match dificultad:
        case "Fácil":
            porcentaje = 0.2
        case "Intermedio":
            porcentaje = 0.4
        case "Difícil":
            porcentaje = 0.6

    return porcentaje

def copiar_tablero(tablero: list)-> list:
    '''
    Crea una copia del tablero original para no modificarlo al ocultar valores.

    Parámetros:\n 
    tablero (list): El tablero de Sudoku completo (9x9) con todos los números visibles

    Retorna:\n 
    list: una nueva lista con las mismas filas y valores del tablero original.
    '''
    copia = []
    for fila in tablero:
        copia.append(fila[:])

    return copia

def ocultar_celdas(tablero: list, cantidad: int)-> list:
    '''
    Oculta la cantidad de celdas aleatorias del tablero, reemplazandolas por strings vacios.

    Parámetros:\n
    tablero (list): Tablero en el que se van a ocultar valores.
    cantidad (int): Cantidad de celdas que deben ocultarse.

    Retorna:\n
    list: El tablero con la cantidad de celdas ocultas.
    '''
    ocultadas = 0
    while ocultadas < cantidad:
        fila = random.randint(0,8)
        columna = random.randint(0,8)
        if tablero[fila][columna] != " ":
            tablero[fila][columna] = " "
            ocultadas += 1

    return tablero

def ocultar_numeros(tablero: list, dificultad: str)-> list:
    '''
    Genera un nuevo tablero con ciertos valores ocultos dependiendo de la dificultad.

    Parámetros:\n 
    tablero (list): El tablero de Sudoku completo con todos los valores visibles.
    dificultad (str): Nivel de dificultad elegido (Fácil, Intermedio o Difícil).

    Retorna:\n
    list: Un nuevo tablero con los números ocultos según la dificultad.
    '''
    porcentaje = obtener_porcentaje(dificultad)
    copia = copiar_tablero(tablero)
    total = 81
    cantidad = int(total * porcentaje)

    tablero_oculto = ocultar_celdas(copia, cantidad)
    
    return tablero_oculto

def calcular_puntaje(dificultad: str, errores: int, tiempo: int)-> int:
    '''
    Calcula el puntaje del jugador mediante la dificultad seleccionada, sus errores y tiempo.

    Parametros:
    dificultad(str): Facil, Intermedio o Dificil
    errores(int): cantidad de errores cometidos
    tiempo(int): tiempo que tardó el jugador

    Retorna:
    int: El puntaje calculado.
    '''
    base = 1000

    match dificultad:
        case "Fácil":
            base *= 1
        case "Intermedio":
            base *= 1.5
        case "Difícil":
            base *= 2

    resta_errores = errores * 50
    resta_tiempo = tiempo // 10
    puntaje = base - resta_errores - resta_tiempo
    return max(0, int(puntaje))
    
