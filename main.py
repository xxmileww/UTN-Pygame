import pygame

pygame.init()
pantalla = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

pantalla_actual = 1

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
