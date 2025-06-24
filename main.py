import pygame

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

info = pygame.display.Info()
ancho_pantalla = info.current_w
alto_pantalla = info.current_h
ancho_ventana = int(ancho_pantalla * 0.8)
alto_ventana = int(alto_pantalla * 0.8)

fuente = pygame.font.SysFont("Calibri", 40)

pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))

pygame.display.set_caption("Sudoku")

pantalla_actual = 1

porcentaje_fondo = 100

color_fondo = (172, 203, 225)

musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

boton_jugar = pygame.Rect(ancho_ventana // 2 - 100, alto_ventana // 2 - 60, 200, 60)

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
        pygame.draw.rect(pantalla, (87, 137, 173), boton_jugar, 2)
        texto = fuente.render("Jugar", True, (23, 38, 48))
        pantalla.blit(texto, (boton_jugar.x + 55, boton_jugar.y + 10))
    pygame.display.flip()
    pantalla.fill(color_fondo)
    
    
