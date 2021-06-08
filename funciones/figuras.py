from libreria_figuras import *

print("Punto 1")
punto1 = capturar_punto()

print("Punto 2")
punto2 = capturar_punto()

area = area_cuadrado(punto1, punto2)
print("el area del cuadrado es: " + str(area))

perimetro = perimetro_cuadrado(punto1, punto2)
print("el perimetro del cuadrado es: " +str(perimetro))

area = area_circulo(punto1, punto2)
print("el area del circulo es: " + str(area))

perimetro = perimetro_circulo(punto1, punto2)
print("el perimetro del circulo es: " +str(perimetro))

area = area_rectangulo(punto1, punto2)
print("el area del rectangulo es: " + str(area))

perimetro = perimetro_rectangulo(punto1, punto2)
print("el perimetro del rectangulo es: " +str(perimetro))
