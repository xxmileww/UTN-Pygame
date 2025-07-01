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

resolucion_automatica = (ancho_ventana, alto_ventana)
resoluciones = resolucion_automatica,(1280, 720),(1600, 900),(1920, 1080)
indice_resolucion = 0

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

espacio_botones = int(ancho_ventana * 0.05)
ancho_botones = int(ancho_ventana * 0.15)
alto_botones = int(alto_ventana * 0.1)
ancho_total = 3 * ancho_botones + 2 * espacio_botones

x_inicio = (ancho_ventana - ancho_total) // 2
y_botones = int(alto_ventana * 0.5)

ancho_volver = 200
alto_volver = 60 

x_volver = ancho_ventana - ancho_volver - 300  
y_volver = alto_ventana - alto_volver - 50    

ancho_reinicio = 245
alto_reinicio = 60

x_reinicio = ancho_ventana - ancho_reinicio - 600
y_reinicio = alto_ventana - alto_reinicio - 50

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
        boton_jugar = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.25, ancho_ventana * 0.3, alto_ventana * 0.1)
        boton_ajustes = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.40, ancho_ventana * 0.3, alto_ventana * 0.1)
        boton_puntaje = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.55, ancho_ventana * 0.3, alto_ventana * 0.1)
        boton_salir = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.70, ancho_ventana * 0.3, alto_ventana * 0.1)

        rec_jugar = pygame.draw.rect(pantalla, color_botones, boton_jugar, border_radius = 25) 
        rec_ajustes = pygame.draw.rect(pantalla, color_botones, boton_ajustes, border_radius = 25 ) 
        rec_puntaje = pygame.draw.rect(pantalla, color_botones, boton_puntaje, border_radius = 25)
        rec_salir = pygame.draw.rect(pantalla, color_botones, boton_salir, border_radius = 25)

        titulo = fuente_titulo.render("Sudoku", True, color_fuente)
        jugar = fuente_botones.render("Jugar", True, color_fuente)
        ajustes = fuente_botones.render("Ajustes", True, color_fuente)
        puntaje = fuente_botones.render("Puntaje", True, color_fuente)
        salir = fuente_botones.render("Salir", True, color_fuente)

        pantalla.blit(titulo, (ancho_ventana * 0.35, alto_ventana * 0.07))
        pantalla.blit(jugar, centrar_texto(boton_jugar, jugar))
        pantalla.blit(ajustes, centrar_texto(boton_ajustes, ajustes))
        pantalla.blit(puntaje, centrar_texto(boton_puntaje, puntaje))
        pantalla.blit(salir, centrar_texto(boton_salir, salir))

                
    elif pantalla_actual == 2:
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
        espacio_botones = int(ancho_ventana * 0.05)
        ancho_botones = int(ancho_ventana * 0.15)
        alto_botones = int(alto_ventana * 0.1)
        ancho_total = 3 * ancho_botones + 2 * espacio_botones

        x_inicio = (ancho_ventana - ancho_total) // 2
        y_botones = int(alto_ventana * 0.5)
        boton_facil = pygame.Rect(x_inicio, y_botones, ancho_botones, alto_botones)
        boton_intermedio = pygame.Rect(x_inicio + ancho_botones + espacio_botones, y_botones, ancho_botones, alto_botones)
        boton_dificil = pygame.Rect(x_inicio + 2 * (ancho_botones + espacio_botones), y_botones, ancho_botones, alto_botones)

        rec_facil = pygame.draw.rect(pantalla, color_botones, boton_facil, border_radius=25)
        rec_intermedio = pygame.draw.rect(pantalla, color_botones, boton_intermedio, border_radius=25)
        rec_dificil = pygame.draw.rect(pantalla, color_botones, boton_dificil, border_radius=25)
        
        dificultad = fuente_textos.render("Seleccione la dificultad", True, color_fuente)
        rect_titulo = dificultad.get_rect(center=(ancho_ventana // 2, int(alto_ventana * 0.3)))
        pantalla.blit(dificultad, rect_titulo)

        facil = fuente_botones.render("Fácil", True, color_fuente)
        intermedio = fuente_botones.render("Intermedio", True, color_fuente)
        dificil = fuente_botones.render("Difícil", True, color_fuente)

        pantalla.blit(facil, centrar_texto(boton_facil, facil))
        pantalla.blit(intermedio, centrar_texto(boton_intermedio, intermedio))
        pantalla.blit(dificil, centrar_texto(boton_dificil, dificil))

        aviso = fuente_aviso.render("Presione esc si desea volver atras", True, color_fuente)
        pantalla.blit(aviso, (ancho_ventana * 0.02, alto_ventana * 0.90))
                    
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

                if boton_cambiar_res.collidepoint(evento.pos):
                    indice_resolucion = (indice_resolucion + 1) % len(resoluciones)
                    nueva_resolucion = resoluciones[indice_resolucion]
                    ancho_ventana, alto_ventana = nueva_resolucion
                    pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
                    fondo_imagen = pygame.image.load("fondo.png")
                    fondo_imagen = pygame.transform.scale(fondo_imagen, (ancho_ventana, alto_ventana))

        if musica_activada:
            color_boton_musica = color_botones
        else:
            color_boton_musica = (255, 100, 100)

        boton_musica = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.35, ancho_ventana * 0.3, alto_ventana * 0.1)
        boton_cambiar_res = pygame.Rect(ancho_ventana * 0.35, alto_ventana * 0.50, ancho_ventana * 0.3, alto_ventana * 0.1)

        pygame.draw.rect(pantalla, color_boton_musica, boton_musica, border_radius=20)
        texto_musica = fuente_botones.render("Música", True, color_fuente)
        pantalla.blit(texto_musica, centrar_texto(boton_musica, texto_musica))

        pygame.draw.rect(pantalla, color_botones, boton_cambiar_res, border_radius=20)
        res_actual = f"{ancho_ventana}x{alto_ventana}"
        texto_res = fuente_botones.render(f"Resolución: {res_actual}", True, color_fuente)
        pantalla.blit(texto_res, centrar_texto(boton_cambiar_res, texto_res))

        aviso = fuente_aviso.render("Presione esc si desea volver atras", True, color_fuente)
        pantalla.blit(aviso, (ancho_ventana * 0.02, alto_ventana * 0.85))

    elif pantalla_actual == 4:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    pantalla_actual = 1

        boton_volver = pygame.Rect(ancho_ventana * 0.05, alto_ventana * 0.85, ancho_ventana * 0.2, alto_ventana * 0.08)
        pygame.draw.rect(pantalla, color_botones, boton_volver, border_radius=20)
        texto_volver = fuente_botones.render("Volver", True, color_fuente)
        pantalla.blit(texto_volver, centrar_texto(boton_volver, texto_volver))

    
    elif pantalla_actual == 5:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    pantalla_actual = 1
                elif boton_reinicio.collidepoint(evento.pos):
                    tablero_juego = ocultar_numeros(base_tablero, dificultad_actual)
                    tiempo_juego = 0
                    errores = 0                          
            if evento.type == evento_timer:
                tiempo_juego += 1

        dibujar_sudoku( pantalla,tablero_juego, x_tablero, y_tablero, tamaño_celda, grosor_borde, color_negro, color_negro, color_celda_vacia, fuente_numero) 

        minutos = tiempo_juego // 60
        segundos = tiempo_juego % 60
        texto_timer = fuente_timer.render(f"Tiempo: {minutos:02}:{segundos:02}", True, color_fuente)
        pantalla.blit(texto_timer, (ancho_ventana - 550, 40))
        texto_errores = fuente_timer.render(f"Errores: {errores}/{errores_maximos}", True, color_fuente)
        pantalla.blit(texto_errores, (ancho_ventana - 545, 100))
        
        boton_volver = pygame.Rect(ancho_ventana * 0.05, alto_ventana * 0.85, ancho_ventana * 0.2, alto_ventana * 0.08)
        boton_reinicio = pygame.Rect(ancho_ventana * 0.75, alto_ventana * 0.85, ancho_ventana * 0.2, alto_ventana * 0.08)

        pygame.draw.rect(pantalla, color_botones, boton_volver, border_radius=20)
        texto_volver = fuente_botones.render("Volver", True, color_fuente)
        pantalla.blit(texto_volver, centrar_texto(boton_volver, texto_volver))

        pygame.draw.rect(pantalla, color_botones, boton_reinicio, border_radius=20)
        texto_reinicio = fuente_botones.render("Reiniciar juego", True, color_fuente)
        pantalla.blit(texto_reinicio, centrar_texto(boton_reinicio, texto_reinicio))


    pygame.display.flip()
    
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
y_volver = alto_ventana - alto_volver - 50    

ancho_reinicio = 245
alto_reinicio = 60

x_reinicio = ancho_ventana - ancho_reinicio - 600
y_reinicio = alto_ventana - alto_reinicio - 50

boton_jugar = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones) 
boton_ajustes = pygame.Rect(boton_jugar.x, boton_jugar.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_puntaje = pygame.Rect(boton_ajustes.x, boton_ajustes.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_salir = pygame.Rect(boton_ajustes.x, boton_puntaje.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_volver = pygame.Rect(x_volver, y_volver, ancho_volver, alto_volver)
boton_cambiar_res = pygame.Rect(ancho_pantalla * 0.33, alto_pantalla * 0.28, ancho_botones, alto_botones)
boton_musica = pygame.Rect(boton_cambiar_res.x, boton_cambiar_res.y + alto_botones + espacio_botones, ancho_botones, alto_botones)
boton_reinicio = pygame.Rect(x_reinicio, y_reinicio, ancho_reinicio, alto_reinicio)


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
                elif boton_reinicio.collidepoint(evento.pos):
                    tablero_juego = ocultar_numeros(base_tablero, dificultad_actual)
                    tiempo_juego = 0
                    errores = 0                          
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

        pygame.draw.rect(pantalla, color_botones, boton_reinicio, border_radius= 20)            
        texto_reinicio = fuente_botones.render("reiniciar juego", True, color_fuente)
        pantalla.blit(texto_reinicio, (boton_reinicio.x + 20, boton_reinicio.y +20))


    pygame.display.flip()
    
