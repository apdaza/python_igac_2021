from figuras import *


figuras = [Cuadrado(Punto(10, 5), Punto(10,20)), Rectangulo(Punto(10, 5), Punto(5,20)), Circulo(Punto(10, 5), Punto(10,20))]

for f in figuras:
  print(f.calcular_area())
