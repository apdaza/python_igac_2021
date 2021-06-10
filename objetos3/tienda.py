from animales import *
from random import randint

class Tienda:
  def __init__(self):
    self.animales = []
    self.elegir_animales()

  def presentar_animales(self):
    for a in self.animales:
      print(a.informar_tipo(), a.comunicar())
  
  def elegir_animales(self):
    cant = randint(5, 10)
    for i in range(cant):
      opc = randint(0, 2)
      if opc == 0:
        self.animales.append(Gato())
      elif opc == 1:
        self.animales.append(Perro())
      else:
        self.animales.append(Perico())