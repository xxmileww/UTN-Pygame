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
fuente_timer = pygame.font.SysFont("Arial Rounded MT", 50)

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


evento_timer = pygame.USEREVENT + 1
pygame.time.set_timer(evento_timer, 1000)  


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
        rec_facil, rec_intermedio, rec_dificil = pantalla_dificultad(pantalla, color_botones, color_fuente, fuente_botones, ancho_pantalla, alto_pantalla, boton_facil, boton_intermedio, boton_dificil, fuente_textos, fuente_aviso)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rec_facil.collidepoint(evento.pos):
                    dificultad_actual = "Fácil"
                    tiempo_juego = 0
                    pantalla_actual = 5
                elif rec_intermedio.collidepoint(evento.pos):
                    dificultad_actual = "Intermedio"
                    tiempo_juego = 0
                    pantalla_actual = 5
                elif rec_dificil.collidepoint(evento.pos):
                    dificultad_actual = "Difícil"
                    tiempo_juego = 0
                    pantalla_actual = 5
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_actual = 1
    
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
    
    elif pantalla_actual == 5:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pantalla_actual = 2 
            if evento.type == evento_timer:
                tiempo_juego += 1
        minutos = tiempo_juego // 60
        segundos = tiempo_juego % 60
        texto_timer = fuente_timer.render(f"Tiempo: {minutos:02}:{segundos:02}", True, color_fuente)
        pantalla.blit(texto_timer, (ancho_ventana - 550, 40))

    pygame.display.flip()
    

