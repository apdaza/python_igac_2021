class Animal:
  def informar_tipo(self):
    return type(self)

class Gato(Animal):
  def comunicar(self):
    return "miau"

class Perro(Animal):
  def comunicar(self):
    return "guau"

class Perico(Animal):
  def comunicar(self):
    return "rua"
