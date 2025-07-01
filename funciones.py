import random
import pygame
from pygame import Rect, Surface
from pygame.font import Font

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

def mezclar_lista_original(lista_original: list)-> list:
    '''
    Genera una lista con los números de una lista original mezclados sin repeticiones.

    Parámetros:\n
    lista_original (list): Lista originar a ser mezclada.

    Retorna:\n
    list: Lista mezclada de números sin repeticiones.
    '''
    lista_original = lista_original
    lista_mezclada = []

    while len(lista_mezclada) < len(lista_original):
        indice = random.randint(0, len(lista_original) - 1)
        numero = lista_original[indice]

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

def generar_tablero_sudoku(lista_original: list)-> list:
    '''
    Genera un tablero de Sudoku completo de 9x9 basado en una fila base que es rotada.

    Parámetros:\n
    lista_original (list): Lista de números a usar en el tablero de sudoku.

    Retorna:\n
    list: Matriz de 9 listas (filas) que representan el Sudoku.
    '''
    lista_original = lista_original
    base = mezclar_lista_original(lista_original)
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
    dificultad (str): Nivel de dificultad elegida (Fácil, Intermedio o Difícil).

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
    tablero (list): El tablero de Sudoku completo (9x9) con todos los números visibles.

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
    Calcula el puntaje del jugador basándose en la dificultad seleccionada, los errores que tuvo y el tiempo que le tomo.

    Parametros:\n
    dificultad (str): Nivel de dificultad elegido (Fácil, Intermedio o Difícil).
    errores (int): Cantidad de errores cometidos.
    tiempo (int): Tiempo que tardó el jugador.

    Retorna:\n
    int: El puntaje total calculado.
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
    

def dibujar_sudoku(pantalla: Surface, tablero: list, borde_x:int, borde_y: int ,tamaño_celda: int, grosor_linea:int, color_linea: tuple, color_celda: tuple, color_oculto: tuple,  fuente_num: Font):
    """
    Dibuja el tablero de Sudoku en pygame.(falta completar)
    
    """
    for fila in range(9):
        for columna in range(9):
            valor = tablero[fila][columna]

            x= borde_x + (columna * tamaño_celda)
            y = borde_y + (fila * tamaño_celda)

            borde_celda= pygame.Rect(x, y, tamaño_celda, tamaño_celda)

            if valor == "":
                pygame.draw.rect(pantalla, color_oculto, borde_celda)
            else:
                pygame.draw.rect(pantalla, (230,230,230), borde_celda)
                texto_superficie = fuente_num.render(str(valor), True, color_celda)
                texto_rect = texto_superficie.get_rect(center=borde_celda.center)
                pantalla.blit(texto_superficie, texto_rect)

    for i in range(10): 
        if i % 3 == 0:
            grosor_linea = 3 
        else:
            grosor_linea = 1
        pygame.draw.line(pantalla, color_linea, (borde_x, borde_y + i * tamaño_celda),
                         (borde_x + 9 * tamaño_celda, borde_y + i * tamaño_celda), grosor_linea)
        pygame.draw.line(pantalla, color_linea, (borde_x + i * tamaño_celda, borde_y),
                         (borde_x + i * tamaño_celda, borde_y + 9 * tamaño_celda), grosor_linea)
