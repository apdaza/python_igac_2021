from puntos import Punto
from math import pi

class Figura:
  def __init__(self, p1 = Punto(), p2 = Punto()):
    self.p1 = p1
    self.p2 = p2

class Cuadrado(Figura):  
  def calcular_area(self):
    return self.p1.calcular_distancia(self.p2) ** 2

class Rectangulo(Figura):
  def calcular_area(self):
    p3 = Punto(self.p1.x, self.p2.y)
    return self.p1.calcular_distancia(p3) * self.p2.calcular_distancia(p3)

class Circulo(Figura):
  def calcular_area(self):
    return pi * self.p1.calcular_distancia(self.p2) ** 2

    