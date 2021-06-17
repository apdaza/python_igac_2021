import sys, pygame, util
from pygame.locals import *
from heroe import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

jugando = True

pygame.display.set_caption("El Paso")
fuente = pygame.font.Font(None, 30)
pygame.mouse.set_visible(False)

heroe = Heroe()

while jugando:
    heroe.update()

    screen.blit(heroe.image, heroe.rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
    pygame.time.delay(10)
