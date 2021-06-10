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

  def __str__(self):
    return "coordenadas: x en " + str(self.x) + ", y en " + str(self.y)

class Segmento:
  def __init__(self, p1 = Punto(), p2 = Punto()):
    self.origen = p1
    self.fin = p2

  def crear(self, p1, p2):
    self.origen = p1
    self.fin = p2

  def calcular_longitud(self):
    return self.origen.calcular_distancia(self.fin)


p1 = Punto(10, 5)

p2 = Punto()
p2.ubicar(10, 20)

print(type(p1))
print(p1.x)
print(p1.calcular_distancia(p2))

p1.nombre = "Punto 1"
print(p1.nombre)

s = Segmento()
print(type(s))
s.crear(p1, p2)
print(s.calcular_longitud())

print("el primer punto tiene " + str(p1))
