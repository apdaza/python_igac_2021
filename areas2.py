# Ejercicio calculo de áreas

opcion = "S"

while opcion == "S" or opcion == "s":
    figura = input("Elija la figura (1-cuadrado / 2-rectangulo): ")

    if figura == "1":
        lado = int(input("Ingrese el valor del lado: "))
        area = lado * lado
        print("el área del cuadrado es : ", str(area))
    elif figura == "2":
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
        area = base * altura
        print("el área del rectangulo es : ", str(area))
    else:
        print("opción no válida")

    opcion = input("Desea realizar otro cálculo? S/n: ")
