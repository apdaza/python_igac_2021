from unidad import UnidadDeTiempo

class Cronometro:
    def __init__(self):
        self.hora = UnidadDeTiempo(23)
        self.minuto = UnidadDeTiempo()
        self.segundo = UnidadDeTiempo()
        self.centesima = UnidadDeTiempo(99)
        self.parado = True

    def borrar(self):
        self.hora.borrar()
        self.minuto.borrar()
        self.segundo.borrar()
        self.centesima.borrar()
        self.parado = True

    def avanzar(self):
        self.centesima.avanzar()
        if self.centesima.valor == 0:
            self.segundo.avanzar()
            if self.segundo.valor == 0:
                self.minuto.avanzar()
                if self.minuto.valor == 0:
                    self.hora.avanzar()

    
    def cambiar_estado(self):
        self.parado = not self.parado

    def retornar_tiempo(self):
        return "{:02d}:{:02d}:{:02d}:{:02d}".format(self.hora.valor,
                                             self.minuto.valor,
                                             self.segundo.valor,
                                             self.centesima.valor)
