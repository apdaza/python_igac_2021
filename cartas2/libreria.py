from random import shuffle

def baraja():
    valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    pintas = ["Picas","Treboles","Corazones","Diamantes"]
    return [(v,p) for v in valores for p in pintas]

def barajar(baraja):
    shuffle(baraja)
    return baraja

def valor_carta(carta):
    if carta[0] in ["J", "Q", "K"]:
        return 10
    if carta[0] == "A":
        return 11
    return int(carta[0])
