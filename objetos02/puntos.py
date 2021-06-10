from math import sqrt
class Punto:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def ubicar(self, x, y):
    self.x = x
    self.y = y

  def calcular_distancia(self, p):
    return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
