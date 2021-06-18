import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

jugando = True

pygame.display.set_caption("El Paso")
fuente = pygame.font.Font(None, 30)
fuente2 = pygame.font.Font(None, 65)
fondo = util.cargar_imagen("imagenes/fondo.jpg")
pygame.mouse.set_visible(False)

heroe = Heroe()
villanos = [Villano((100, 120), 7), Villano((200, 280), 10)]

while jugando:
    heroe.update()
    texto_vida = fuente.render("Vida: " + str(heroe.vida), 1, (250, 250, 250))
    screen.blit(fondo, (0, 0))
    screen.blit(heroe.image, heroe.rect)
    screen.blit(texto_vida, (20, 10))
    heroe.image = heroe.images[0]
    for v in villanos:
        v.update()
        screen.blit(v.image, v.rect)
        if heroe.rect.colliderect(v.rect):
            heroe.vida -= 1
            heroe.image = heroe.images[2]
            
    if heroe.vida <= 0:
        jugando = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    pygame.time.delay(10)

texto_final = fuente2.render("Lo siento", 1, (255, 0, 0))
screen.blit(fondo, (0, 0))
screen.blit(texto_final, (120, 240))
pygame.display.update()
