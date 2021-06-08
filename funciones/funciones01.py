from random import randint
def saludar_funcion(nombre):
    return "hola " + nombre

def saludar_procedimiento(nombre):
    print("Hola " + nombre)

variable = saludar_funcion("alejandro")
print(variable)

saludar_procedimiento("alejandro")

print(randint(0, 17))

