from libreria import *

b=barajar(baraja())

jugador1, jugador2 = b[0], b[1]

print("jugador1",jugador1, "jugador2",jugador2)

if valor_carta(jugador1) > valor_carta(jugador2):
    print("gana jugador1")
elif valor_carta(jugador1) == valor_carta(jugador2):
    print ("Empate")
else: 
    print("gana jugador2")
