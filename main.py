import pygame

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

info = pygame.display.Info()
ancho_pantalla = info.current_w
alto_pantalla = info.current_h
ancho_ventana = int(ancho_pantalla * 0.8)
alto_ventana = int(alto_pantalla * 0.8)

fuente_botones = pygame.font.SysFont("Arial", 40)
fuente_titulo = pygame.font.SysFont("Bauhaus 93", 130)

pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))

pygame.display.set_caption("Sudoku")

pantalla_actual = 1

porcentaje_fondo = 100

color_fondo = (172, 203, 225)
<<<<<<< HEAD
color_fuente = (40, 62, 99)

=======
color_boton = (103, 170, 214)
color_borde = (87, 137, 173)
color_texto = (23, 38, 48)
>>>>>>> 689b31b22e40eabd27f3ec9da9c38e05eeb52f8b

musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

<<<<<<< HEAD
alto_botones = 80
ancho_botones = 250

boton_jugar = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones) 
# boton_quitar = pygame.Rect()
=======
boton_jugar = pygame.Rect(ancho_ventana // 2 - 100, alto_ventana // 2 - 60, 250, 60)
>>>>>>> 689b31b22e40eabd27f3ec9da9c38e05eeb52f8b

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
<<<<<<< HEAD
        pygame.draw.rect(pantalla, (87, 137, 173), boton_jugar, 2)
        titulo = fuente_titulo.render("Sudoku", True, color_fuente)
        jugar = fuente_botones.render("Jugar", True, color_fuente)
        pantalla.blit(titulo, (ancho_pantalla * 0.28, alto_pantalla * 0.07))
        pantalla.blit(jugar, (boton_jugar.x + 85, boton_jugar.y + 15))
=======
        pygame.draw.rect(pantalla, (color_boton), boton_jugar)
        pygame.draw.rect(pantalla, (color_borde), boton_jugar, 2)
        texto = fuente.render("Jugar", True, (color_texto))
        pantalla.blit(texto, (boton_jugar.x + 85, boton_jugar.y + 10))
>>>>>>> 689b31b22e40eabd27f3ec9da9c38e05eeb52f8b
    pygame.display.flip()
    pantalla.fill(color_fondo)
    

