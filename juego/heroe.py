import pygame
from pygame.sprite import Sprite
import util

class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.images = [util.cargar_imagen('imagenes/Mammooth01.png'),
                       util.cargar_imagen('imagenes/Mammoth02.png'),
                       util.cargar_imagen('imagenes/Mammoth03.png')]
        self.image  = self.images[0]
        
        self.rect = self.image.get_rect()
        self.rect.move_ip(200, 10)
        self.vida = 100

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT] and self.rect.x <= 640 - self.rect.width:
            self.rect.x += 10
        elif teclas[pygame.K_LEFT] and self.rect.x >= 10:
            self.rect.x -= 10
        elif teclas[pygame.K_UP] and self.rect.y >= 10:
            self.rect.y -= 10
            
        elif teclas[pygame.K_DOWN] and self.rect.y <= 480 - self.rect.height:
            self.rect.y += 10
