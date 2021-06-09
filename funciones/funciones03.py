from operaciones import *

def saludar(nombre, saludo = "Hola "):
    print(saludo + nombre)

def saludar_lista(lista):
    for item in lista:
        saludar(item, "Buen día ")

def saludar_lista3(*lista):
    for item in lista:
        saludar(item, "Buen día ")

def saludar_lista2(nombres, saludos):
    for saludo in saludos:
        for nombre in nombres:
            saludar(nombre, saludo)

def media(*numeros):
    return sum(numeros)/len(numeros)

def mostrar_parametros(**parametros):
    for k, v in parametros.items():
        print(k, v)

def suma(valor1, valor2):
    return valor1 + valor2
    
#saludar_lista(["alejandro", "miguel", "ana"])

saludar_lista2(["alejandro", "maria", "pedro", "oscar"], ["buen día ", "chao "])

print(media(1, 2, 3, 10, 23, 45))

print(media(5))

saludar_lista3("alejandro", "ana")

mostrar_parametros(nombre = "alejandro", anio = 48, musica = "rock clasico")

print(suma(media(1, 2, 3), media(sum([4,5,6]), 5)))

print(fibbo(10))
print(fibbo_recursivo(10))

print(potencia(5, 3))
