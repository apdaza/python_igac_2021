from unidad import UnidadDeTiempo
from cronometro import Cronometro
"""
u = UnidadDeTiempo()

for i in range(100):
    u.avanzar()
    print(u.valor)
"""
c = Cronometro()
c.minuto.valor = 59
for i in range(100):
    c.avanzar()
    print(c.retornar_tiempo())
