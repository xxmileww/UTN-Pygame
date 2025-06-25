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
color_fuente = (40, 62, 99)


musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

alto_botones = 80
ancho_botones = 250
espacio_botones = 20

boton_jugar = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones) 
boton_ajustes = pygame.Rect(boton_jugar.x, boton_jugar.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
# boton_quitar = pygame.Rect()

ejecutando = True
while ejecutando:
    if pantalla_actual == 1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
        pygame.draw.rect(pantalla, (87, 137, 173), boton_jugar, 2)
        titulo = fuente_titulo.render("Sudoku", True, color_fuente)
        jugar = fuente_botones.render("Jugar", True, color_fuente)
        ajustes = fuente_botones.render("Ajustes", True, color_fuente)
        pantalla.blit(titulo, (ancho_pantalla * 0.28, alto_pantalla * 0.07))
        pantalla.blit(jugar, (boton_jugar.x + 85, boton_jugar.y + 15))
        pantalla.blit(ajustes, (boton_ajustes.x + 75, boton_ajustes.y + 15))
    pygame.display.flip()
    pantalla.fill(color_fondo)
    

