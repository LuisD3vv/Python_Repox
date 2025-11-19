import pygame, os,random,math,io
from pygame import mixer
#print(pygame.__version__)


# siempre utilizar rutas absolutas
ruta = os.path.join(os.path.dirname(__file__))


print(ruta)
# inicializar a pygame
pygame.init()


# crear la pantalla (dimensiones de la pantalla)
pantalla = pygame.display.set_mode((800,600))


# titulo e Icono
pygame.display.set_caption(os.path.join(ruta,"Space Invaders"))
icono = pygame.image.load(os.path.join(ruta,"images/cool.png"))
pygame.display.set_icon(icono)
fondo = pygame.image.load(os.path.join(ruta,'images/Fondo.jpg'))

#agregar musica
mixer.music.load(os.path.join(ruta,"sounds/MusicaFondo.mp3"))
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# Jugador y posicion
img_jugador = pygame.image.load(os.path.join(ruta,"images/spaceship.png"))
# posicion total se resto el tamano del icono del jugador a la mitad de los ejes.
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variable enemigo

img_enemigo = []

enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load(os.path.join(ruta,"images/enemigo.png")))
    # posicion total se resto el tamano del icono del jugador a la mitad de los ejes.
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


#variable de la bala
balas = []
img_bala = pygame.image.load(os.path.join(ruta,"images/bala.png"))
# posicion total se resto el tamano del icono del jugador a la mitad de los ejes.
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = True

# tranformar texto a bytes solo necesario si convertimos a ejecutable
def fuente_bytes(fuente):
    with open(fuente,'rb') as f:
        tft_bytes = f.read()
        return io.BytesIO(tft_bytes)


# Puntaje
puntaje = 0
texto_x = 10
texto_y = 10

# texto final
fuente = 'fonts/Pikabu.ttf'
fuente_final = pygame.font.Font(os.path.join(ruta,fuente),45)
fuente = pygame.font.Font(os.path.join(ruta,fuente),25)


# Texto al finalizar
def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO',True,(255,255,255))
    pantalla.blit(mi_fuente_final,(160,250))


# funcion mostrar puntaje
def mostrar_puntaje(x,y):
    # Definir los colores y formato del texto
    texto = fuente.render(f"Puntaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(x,y))


# Definir la funcion jugador, de movimiento
def jugador(x:int,y:int):
    pantalla.blit(img_jugador, (x,y))


# Definir la funcion enemigo, de movimiento
def enemigo(x:int,y:int,ene:int):
    pantalla.blit(img_enemigo[ene], (x,y))


# Definir la funcion disparar bala        
def disparar_bala(x: int,y: int):
    pantalla.blit(img_bala,(x + 16,y + 10))


# evaluar colisiones
def calcular_colisiones(x_1,y_1,x_2,y_2):
    # Formula para calcular distancia entre dos puntos
    distancia = math.sqrt(pow((x_2-x_1),2) + pow((y_2-y_1),2))
    # definiendo el hitbox de nuestro personaje
    if distancia < 27:
        return True
    return False


# Loop del juego
se_ejecuta=True
while se_ejecuta:
    pantalla.blit(fondo,(0,0))
    # iterar sobre los eventos
    
    for evento in pygame.event.get():
        # evento para cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # evento si se presiono una teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
                print("Flecha izquierda presionada")
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
                print("Flecha derecha presionada")
            # Disparar bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound(os.path.join(ruta,"sounds/disparo.mp3"))
                sonido_bala.play()
                nueva_bala = { 'x':jugador_x,'y': jugador_y,'velocidad': -5}
                balas.append(nueva_bala)
            # evento si se dejo de presionar una flecha
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                    jugador_x_cambio = 0

    # evento modificar ubicacion jugador
    jugador_x += jugador_x_cambio
    # mantener_dentro de los bordes
    if jugador_x <= 1:
        jugador_x = 1
    elif jugador_x >= 735:
        jugador_x = 734
    
    # ubicacion de enemigos
    for e in range(cantidad_enemigos):
        #fin el juego
        # Calcular el choque con la funcion colision
        if enemigo_y[e] > 490:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
                jugador_x_cambio = 0
                texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 735:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]
            
        #colision
        for bala in balas:
            colision = calcular_colisiones(enemigo_x[e],enemigo_y[e],bala['x'],bala['y'])
            if colision:
                sonido_colision = mixer.Sound(os.path.join(ruta,"sounds/Golpe.mp3"))
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0,736)
                enemigo_y[e] = random.randint(20,200)
                break
        enemigo(enemigo_x[e],enemigo_y[e],e)
        
        #movimiento bala
    
        for bala in balas:
            if bala['y'] <= 64:
                bala['y'] = 500
                balas.remove(bala)
            if bala_visible:
                disparar_bala(bala['x'],bala['y'])
                bala["y"] += bala["velocidad"]
        bala = [bala for bala in balas if bala['y']>0]
        
    jugador(jugador_x,jugador_y)
    # motrar puntaje
    mostrar_puntaje(texto_x,texto_y)
    # evento para actualizar todo
    pygame.display.update()