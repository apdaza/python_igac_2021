numero_uno = 15
numero_dos = 4

# para ver el tipo de las variables
print(type(numero_uno))
print(type(numero_dos))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
producto = numero_uno * numero_dos
division = numero_uno // numero_dos
potencia = numero_uno ** numero_dos

print(type(suma), type(resta), type(producto), type(division))
print(suma, resta, producto, division, potencia)

"""
Ejemplo de nombres de variables
validas
"""

_mi_valor_ = 'un valor'
mi_valor = 'otro valor'
valor = "otro valor 2"
valor1 = "otro valor"

# asignaciones múltiples
a, b, c = 1, 2, 3

print(a)
print(a, b, c)

#comparando varables
print(mi_valor == valor1)
print(_mi_valor_ == valor1)

x = y = z = 25
print(x, y, z)
print(x == z)


def mi_funcion():
    print("esto es una función")
    v = 34
    print(v)

mi_funcion()

print("fuera de mi función")

cadena = "esto es un texto en una variable"
print(cadena[2])
print(cadena[-2])
print(cadena[4:10])
print(cadena[4:])
print(cadena[:-3]

saludo = "hola"

print(saludo * 5)



