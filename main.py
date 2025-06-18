import pygame

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

ancho = 1200
alto = 900

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Sudoku")

pantalla_actual = 1

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
