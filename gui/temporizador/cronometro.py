from unidad import UnidadDeTiempo

class Cronometro:
    def __init__(self):
        self.minuto = UnidadDeTiempo()
        self.segundo = UnidadDeTiempo()
        self.parado = True

    def borrar(self):
        self.minuto.borrar()
        self.segundo.borrar()
        self.parado = True

    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == self.segundo.tope:
            self.minuto.avanzar()
        if self.minuto.valor == 0 and self.segundo.valor == 0:
            self.parado = True

    
    def cambiar_estado(self):
        self.parado = not self.parado

    def retornar_tiempo(self):
        return "{:02d}:{:02d}".format(self.minuto.valor,
                                      self.segundo.valor)
