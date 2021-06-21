from unidad import UnidadDeTiempo

u = UnidadDeTiempo()

for i in range(100):
    u.avanzar()
    print(u.valor)
