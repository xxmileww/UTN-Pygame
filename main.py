import pygame

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

info = pygame.display.Info()
ancho_pantalla = info.current_w
alto_pantalla = info.current_h

pantalla = pygame.display.set_mode((int(ancho_pantalla * 0.8), int(alto_pantalla * 0.8)))

imagen_fondo = pygame.image.load("fondo.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ancho_pantalla, alto_pantalla))

pygame.display.set_caption("Sudoku")

pantalla_actual = 1

musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()

pygame.display.flip()
