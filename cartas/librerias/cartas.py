from random import shuffle

def baraja():
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    pintas = ["Picas", "Treboles", "Corazones", "Diamantes"]
    return [(v, p) for v in valores for p in pintas]

def barajar(baraja):
    shuffle(baraja)
    return baraja

def valor_carta(carta):
    if carta[0] in ["J", "Q", "K"]:
        return 10
    if carta[0] == "A":
        return 1
    return int(carta[0])

def validar_as(mano):
    if mano == []:
        return False
    if mano[0][0] == "A":
        return True
    return validar_as(mano[1:])

def preliminar(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + preliminar(mano[1:])

def valor_mano(mano):
    if validar_as(mano) and preliminar(mano) <= 11:
        return preliminar(mano) + 10
    return preliminar(mano)

def mostrar_juego(mesa, jugador):
    print("Mesa __________________________________")
    print(mesa)
    print(valor_mano(mesa))
    print("Jugador _______________________________")
    print(jugador)
    print(valor_mano(jugador))

def jugar(baraja, mesa, jugador):
    if baraja == []:
        print("sin cartas para jugar")
    else:
        mostrar_juego(mesa, jugador)
        if len(mesa) < 2 and len(jugador) < 2:
            print("repartiendo cartas")
            return jugar(baraja[2:], mesa + [baraja[0]], jugador + [baraja[1]])
        elif (valor_mano(jugador) < 18 or valor_mano(jugador) <= valor_mano(mesa)) and valor_mano(mesa) <= 21:
            print("turno jugador")
            return jugar(baraja[1:], mesa, jugador + [baraja[0]])
        elif (valor_mano(mesa) < valor_mano(jugador)) and valor_mano(mesa) < 21 and valor_mano(jugador) <= 21:
            print("turno mesa")
            return jugar(baraja[1:], mesa + [baraja[0]], jugador)
        return valor_mano(mesa), valor_mano(jugador)
