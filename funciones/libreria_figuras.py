from math import sqrt, pi

def capturar_punto():
    x = int(input("Ingrese el valor en x: "))
    y = int(input("Ingrese el valor en y: "))
    return x, y
            
def calcular_distancia(punto1, punto2):
    return sqrt(((punto1[0] - punto2[0]) ** 2) + ((punto1[1] - punto2[1]) ** 2))

def area_cuadrado(punto1, punto2):
    lado = calcular_distancia(punto1, punto2)
    area = lado * lado
    return area

def perimetro_cuadrado(punto1, punto2):
    lado = calcular_distancia(punto1, punto2)
    perimetro = lado * 4
    return perimetro

def area_circulo(punto1, punto2):
    radio = calcular_distancia(punto1, punto2)
    area = pi * radio ** 2
    return area

def perimetro_circulo(punto1, punto2):
    radio = calcular_distancia(punto1, punto2)
    perimetro = 2 * pi * radio
    return perimetro

def area_rectangulo(punto1, punto2):
    punto_nuevo = punto1[0], punto2[1]
    base = calcular_distancia(punto_nuevo, punto2)
    altura = calcular_distancia(punto1, punto_nuevo)
    area = base * altura
    return area

def perimetro_rectangulo(punto1, punto2):
    punto_nuevo = punto1[0], punto2[1]
    base = calcular_distancia(punto_nuevo, punto2)
    altura = calcular_distancia(punto1, punto_nuevo)
    perimetro = 2 * base + 2 * altura
    return perimetro
