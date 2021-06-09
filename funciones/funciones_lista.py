def suma_lista(lista):
    if lista == []:
        return 0
    return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4, 5]))
