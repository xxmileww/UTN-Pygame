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
    
def pantalla_inicio(pantalla: Surface, color_botones: tuple, color_fuente: tuple, fuente_titulo: Font, fuente_botones: Font, ancho_pantalla: int, alto_pantalla: int, boton_jugar: Rect, boton_ajustes: Rect, boton_puntaje: Rect, boton_salir: Rect) -> Rect:

    rec_jugar = pygame.draw.rect(pantalla, color_botones, boton_jugar, border_radius = 25) 
    rec_ajustes = pygame.draw.rect(pantalla, color_botones, boton_ajustes, border_radius = 25 ) 
    rec_puntaje = pygame.draw.rect(pantalla, color_botones, boton_puntaje, border_radius = 25)
    rec_salir = pygame.draw.rect(pantalla, color_botones, boton_salir, border_radius = 25)

    titulo = fuente_titulo.render("Sudoku", True, color_fuente)
    jugar = fuente_botones.render("Jugar", True, color_fuente)
    ajustes = fuente_botones.render("Ajustes", True, color_fuente)
    puntaje = fuente_botones.render("Puntaje", True, color_fuente)
    salir = fuente_botones.render("Salir", True, color_fuente)

    pantalla.blit(titulo, (ancho_pantalla * 0.28, alto_pantalla * 0.07))
    pantalla.blit(jugar, (boton_jugar.x + 90, boton_jugar.y + 25))
    pantalla.blit(ajustes, (boton_ajustes.x + 80, boton_ajustes.y + 25))
    pantalla.blit(puntaje, (boton_puntaje.x + 80, boton_puntaje.y + 25))
    pantalla.blit(salir, (boton_salir.x + 100, boton_salir.y + 25))

    return rec_jugar, rec_ajustes, rec_puntaje, rec_salir

def pantalla_dificultad(pantalla: Surface, color_botones: tuple, color_fuente: tuple, fuente_botones: Font, ancho_pantalla: int, alto_pantalla: int, boton_facil: Rect, boton_intermedio: Rect, boton_dificil: Rect, fuente_textos: Font, fuente_aviso: Font) -> Rect:
        
        
        rec_facil = pygame.draw.rect(pantalla, color_botones, boton_facil, border_radius =  25)
        rec_intermedio = pygame.draw.rect(pantalla, color_botones, boton_intermedio, border_radius = 25)
        rec_dificil = pygame.draw.rect(pantalla, color_botones, boton_dificil, border_radius = 25)

        dificultad = fuente_textos.render("Seleccione la difícultad", True, color_fuente)
        facil = fuente_botones.render("Fácil", True, color_fuente)
        intermedio = fuente_botones.render("Intermedio", True, color_fuente)
        dificil = fuente_botones.render("Difícil", True, color_fuente)
        aviso = fuente_aviso.render("Presione esc si desea volver atras", True, color_fuente)

        pantalla.blit(dificultad, (ancho_pantalla * 0.16, alto_pantalla * 0.18))
        pantalla.blit(facil, (boton_facil.x + 90, boton_facil.y + 30))
        pantalla.blit(intermedio, (boton_intermedio.x + 53, boton_intermedio.y + 30))
        pantalla.blit(dificil, (boton_dificil.x + 90, boton_dificil.y + 30))
        pantalla.blit(aviso, (ancho_pantalla * 0.02, alto_pantalla * 0.70))

        return rec_facil, rec_intermedio, rec_dificil