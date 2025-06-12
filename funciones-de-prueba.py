
# Usen esta función si quieren ver la matriz para verificar que se ve bien! - Milew

def mostrar_matriz(matriz: list):
    """
    Muestra una matriz en formato tabla con separadores visuales.

    Parámetros:\n
    matriz (list): La matriz a mostrar en consola.
    """
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0

    ancho = 1

    separacion = "-" * (columnas * (ancho + 2) + (columnas + 1))

    for fila in matriz:
        print(separacion)
        print("|", end = "")
        for num in fila:
            print(f" {num} |", end = "")
        print()
    print(separacion)