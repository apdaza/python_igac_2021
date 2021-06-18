import pygame
from pygame.sprite import Sprite
import util

class Villano(Sprite):
    def __init__(self, coordenadas, velocidad):
        Sprite.__init__(self)
        self.image = util.cargar_imagen("imagenes/chinchilla.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(coordenadas[0], coordenadas[1])
        self.direccion = "izquierda"
        self.velocidad = velocidad

    def update(self):
        if self.direccion == "izquierda":
            self.rect.x -= self.velocidad
        elif self.direccion == "derecha":
            self.rect.x += self.velocidad
        if self.rect.x <= 0:
            self.direccion = "derecha"
        if self.rect.x >= 608:
            self.direccion = "izquierda"
