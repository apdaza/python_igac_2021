from random import randint

def generar_secreto(digitos):
    numero = []
    while len(numero) < digitos:
        aleatorio = randint(1,9)
        if aleatorio not in numero:
            numero.append(aleatorio)
    return numero

def capturar_usuario(digitos):
    usuario = ""
    while len(usuario) != digitos:
        usuario = input("ingrese un numero de " + str(digitos) + " dígitos: ")
        enteros = [int(x) for x in usuario]

        for n in enteros:
            apariciones = 0
            for d in enteros:
                if d == n:
                    apariciones += 1
            if apariciones > 1:
                usuario = ""
                break
    return enteros


def comparar(secreto, usuario):
    picas = 0
    fijas = 0

    for n in range(len(secreto)):
        for e in range(len(usuario)):
            if secreto[n] == usuario[e]:
                if n == e:
                    fijas += 1
                else:
                    picas += 1
    return picas, fijas
