from instrumentos import *


class Banda:
  def __init__(self):
    self.musicos = []
    self.crear_banda()

  def crear_banda(self):
    cant = randint(5, 10)
    print("traemos " + str(cant) + " musicos")
    for i in range(cant):
      self.musicos.append(entregar_instrumento())

  def afinar_banda(self):
    for m in self.musicos:
      m.afinar()

  def tocar(self):
    for m in self.musicos:
      m.tocar()

  
