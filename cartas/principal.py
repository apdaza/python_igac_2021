from librerias.cartas import *

mesa, jugador = jugar(barajar(baraja()), [], [])
                      
if mesa < jugador and jugador <= 21:
    print("Gana el jugador")
elif mesa <= 21:
    print("Gana la mesa")
else:
    print("Gana el jugador")
    
