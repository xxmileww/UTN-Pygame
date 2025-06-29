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

fondo_imagen = pygame.image.load("fondo.png")
fondo_imagen = pygame.transform.scale(fondo_imagen, (ancho_ventana, alto_ventana))

fuente_botones = pygame.font.SysFont("Arial Rounded MT", 40)
fuente_titulo = pygame.font.SysFont("Bauhaus 93", 130)
fuente_textos = pygame.font.SysFont("Arial Rounded MT", 100)
fuente_aviso = pygame.font.SysFont("Arial Rounded MT", 30)
fuente_timer = pygame.font.SysFont("Arial Rounded MT", 50)
fuente_numero = pygame.font.SysFont("Arial Rounded MT", 40)

pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))

pygame.display.set_caption("Sudoku")

pantalla_actual = 1

porcentaje_fondo = 100

color_fondo = (172, 203, 225)
color_fuente = (40, 62, 99)
color_botones = (149, 215, 245)

errores = 0
errores_maximos = 3

musica_fondo = "musica.mp3"
pygame.mixer.music.load(musica_fondo)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
musica_activada = True

alto_botones = 80
ancho_botones = 250
espacio_botones = 20

ancho_volver = 200
alto_volver = 60 

x_volver = ancho_ventana - ancho_volver - 300  
y_volver = alto_ventana - alto_volver - 60    

boton_jugar = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones) 
boton_ajustes = pygame.Rect(boton_jugar.x, boton_jugar.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_puntaje = pygame.Rect(boton_ajustes.x, boton_ajustes.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_salir = pygame.Rect(boton_ajustes.x, boton_puntaje.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_volver = pygame.Rect(x_volver, y_volver, ancho_volver, alto_volver)
boton_cambiar_res = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones)
boton_musica = pygame.Rect(boton_cambiar_res.x, boton_cambiar_res.y + alto_botones + espacio_botones, ancho_botones, alto_botones)

boton_facil = pygame.Rect(ancho_pantalla * 0.10, alto_pantalla * 0.35, ancho_botones, alto_botones)
boton_intermedio = pygame.Rect(ancho_pantalla * 0.32, boton_facil.y, ancho_botones, alto_botones)
boton_dificil = pygame.Rect(ancho_pantalla * 0.55, boton_facil.y, ancho_botones, alto_botones)

evento_timer = pygame.USEREVENT + 1
pygame.time.set_timer(evento_timer, 1000)  

color_blanco =(255,255,255)
color_negro = (0, 0, 0)
color_gris = (100, 100, 100)
color_azul = (70, 70 ,120)
color_celda_vacia= (245, 245, 245)

tamaño_celda = 40
grosor_borde = 1
tamaño_tablero = tamaño_celda * 9
x_tablero = (ancho_ventana - tamaño_tablero) //4
y_tablero = (alto_ventana - tamaño_tablero) //2


base_tablero = []
tablero_juego = []
dificultad_actual ="facil"
tiempo_juego = 0


ejecutando = True
while ejecutando:
    pantalla.blit(fondo_imagen, (0, 0))
    if pantalla_actual == 1:
        rec_jugar, rec_ajustes, rec_puntaje, rec_salir = pantalla_inicio(pantalla,color_botones,color_fuente,fuente_titulo,fuente_botones,ancho_pantalla,alto_pantalla,boton_jugar,boton_ajustes,boton_puntaje,boton_salir)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rec_jugar.collidepoint(evento.pos):
                pantalla_actual = 2
            elif rec_ajustes.collidepoint(evento.pos):
                pantalla_actual = 3
            elif rec_puntaje.collidepoint(evento.pos):
                pantalla_actual = 4
            elif rec_salir.collidepoint(evento.pos):
                pygame.quit()
                quit()
                
    elif pantalla_actual == 2:
        rec_facil, rec_intermedio, rec_dificil = pantalla_dificultad(pantalla, color_botones, color_fuente, fuente_botones, ancho_pantalla, alto_pantalla, boton_facil, boton_intermedio, boton_dificil, fuente_textos, fuente_aviso)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_numeros = [1,2,3,4,5,6,7,8,9]
                base_tablero = generar_tablero_sudoku (lista_numeros)
            
                if rec_facil.collidepoint(evento.pos):
                    dificultad_actual = "Fácil"
                    tablero_juego = ocultar_numeros(base_tablero, dificultad_actual) 
                    tiempo_juego = 0
                    errores = 0
                    pantalla_actual = 5
                elif rec_intermedio.collidepoint(evento.pos):
                    dificultad_actual = "Intermedio"
                    tablero_juego = ocultar_numeros(base_tablero, dificultad_actual) 
                    tiempo_juego = 0
                    errores = 0
                    pantalla_actual = 5
                elif rec_dificil.collidepoint(evento.pos):
                    dificultad_actual = "Difícil"
                    tablero_juego = ocultar_numeros(base_tablero, dificultad_actual) 
                    tiempo_juego = 0
                    errores = 0
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

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_musica.collidepoint(evento.pos):
                    if musica_activada:
                        pygame.mixer.music.pause()
                        musica_activada = False
                    else:
                        pygame.mixer.music.unpause()
                        musica_activada = True
        if musica_activada:
            color_boton_musica = color_botones
        else:
            color_boton_musica = (255, 100, 100)
       
        pygame.draw.rect(pantalla, color_boton_musica, boton_musica, border_radius=20)
        texto_musica = fuente_botones.render("Música", True, color_fuente)
        pantalla.blit(texto_musica, (boton_musica.x + 80, boton_musica.y + 20))
       
        pygame.draw.rect(pantalla, color_botones, boton_cambiar_res, border_radius=20)
        texto_res = fuente_botones.render("Resolución", True, color_fuente)
        pantalla.blit(texto_res, (boton_cambiar_res.x + 50, boton_cambiar_res.y + 20))
        
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
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    pantalla_actual = 1
            if evento.type == evento_timer:
                tiempo_juego += 1

        dibujar_sudoku( pantalla,tablero_juego, x_tablero, y_tablero, tamaño_celda, grosor_borde, color_negro, color_negro, color_celda_vacia, fuente_numero) 

        
        minutos = tiempo_juego // 60
        segundos = tiempo_juego % 60
        texto_timer = fuente_timer.render(f"Tiempo: {minutos:02}:{segundos:02}", True, color_fuente)
        pantalla.blit(texto_timer, (ancho_ventana - 550, 40))
        texto_errores = fuente_timer.render(f"Errores: {errores}/{errores_maximos}", True, color_fuente)
        pantalla.blit(texto_errores, (ancho_ventana - 545, 100))
        
 
        pygame.draw.rect(pantalla, color_botones, boton_volver, border_radius=20)
        texto_volver = fuente_botones.render("Volver", True, color_fuente)
        pantalla.blit(texto_volver, (boton_volver.x + 55, boton_volver.y + 20))

    pygame.display.flip()
    
