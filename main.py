from funciones import *
import pygame

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

info = pygame.display.Info()
ancho_pantalla = info.current_w
alto_pantalla = info.current_h
ancho_ventana = int(ancho_pantalla * 0.8)
alto_ventana = int(alto_pantalla * 0.8)

fuente_botones = pygame.font.SysFont("Arial Rounded MT", 40)
fuente_titulo = pygame.font.SysFont("Bauhaus 93", 130)
fuente_textos = pygame.font.SysFont("Arial Rounded MT", 100)
fuente_aviso = pygame.font.SysFont("Arial Rounded MT", 30)

pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))

pygame.display.set_caption("Sudoku")

pantalla_actual = 1

porcentaje_fondo = 100

color_fondo = (172, 203, 225)
color_fuente = (40, 62, 99)
color_botones = (206, 226, 242)


musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

alto_botones = 80
ancho_botones = 250
espacio_botones = 20

boton_jugar = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones) 
boton_ajustes = pygame.Rect(boton_jugar.x, boton_jugar.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_puntaje = pygame.Rect(boton_ajustes.x, boton_ajustes.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_salir = pygame.Rect(boton_ajustes.x, boton_puntaje.y + alto_botones + espacio_botones, ancho_botones, alto_botones)

boton_facil = pygame.Rect(ancho_pantalla * 0.10, alto_pantalla * 0.35, ancho_botones, alto_botones)
boton_intermedio = pygame.Rect(ancho_pantalla * 0.32, boton_facil.y, ancho_botones, alto_botones)
boton_dificil = pygame.Rect(ancho_pantalla * 0.55, boton_facil.y, ancho_botones, alto_botones)

ejecutando = True
while ejecutando:
    pantalla.fill(color_fondo)
    if pantalla_actual == 1:
        rec_jugar, rec_ajustes, rec_puntaje, rec_salir = pantalla_inicio(pantalla,color_botones,color_fuente,fuente_titulo,fuente_botones,ancho_pantalla,alto_pantalla,boton_jugar,boton_ajustes,boton_puntaje,boton_salir)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rec_jugar.collidepoint(evento.pos):
                pantalla_actual = 2
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rec_ajustes.collidepoint(evento.pos):
                pantalla_actual = 3
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rec_puntaje.collidepoint(evento.pos):
                pantalla_actual = 4
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rec_salir.collidepoint(evento.pos):
                pygame.quit()
                quit()
    elif pantalla_actual == 2:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_actual = 1
        
        pantalla.fill(color_fondo)

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
    
    elif pantalla_actual == 3:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_actual = 1

        aviso = fuente_aviso.render("Presione esc si desea volver atras", True, color_fuente)
        pantalla.blit(aviso, (ancho_pantalla * 0.02, alto_pantalla * 0.70))


    elif pantalla_actual == 4:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_actual = 1

        aviso = fuente_aviso.render("Presione esc si desea volver atras", True, color_fuente)
        pantalla.blit(aviso, (ancho_pantalla * 0.02, alto_pantalla * 0.70))

    pygame.display.flip()
    
