from random import randint

def entregar_instrumento():
  a = randint(0, 3)
  if a == 0:
    return Guitarra(["Do", "Re", "Mi"])
  elif a == 1:
    return Tiple(["Do", "Re", "Mi"])
  elif a == 2:
    return ContraBajo(["Do", "Re", "Mi"])
  else:
    return Violin(["Do", "Re", "Mi"])

class Instrumento:
  def __init__(self, notas = []):
    self.notas = notas

class Guitarra(Instrumento):
  def afinar(self):
    print("afinando guitarra en " + self.notas[0])
  
  def tocar(self):
    for n in self.notas:
      print("tocando guitarra en " + n)

class Tiple(Instrumento):
  def afinar(self):
    print("afinando tiple en " + self.notas[0])
  
  def tocar(self):
    for n in self.notas:
      print("tocando tiple en " + n)

class Violin(Instrumento):
  def afinar(self):
    print("afinando violin en " + self.notas[0])
  
  def tocar(self):
    for n in self.notas:
      print("tocando violin en " + n)

class ContraBajo(Instrumento):
  def afinar(self):
    print("afinando contrabajo en " + self.notas[0])
  
  def tocar(self):
    for n in self.notas:
      print("tocando contrabajo en " + n)