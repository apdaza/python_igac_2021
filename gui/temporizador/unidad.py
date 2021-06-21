class UnidadDeTiempo:
    def __init__(self, tope=59):
        self.valor = 0
        self.tope = tope

    def borrar(self):
        self.valor = 0

    def avanzar(self):
        if self.valor > 0:
            self.valor -= 1
        else:
            self.valor = self.tope
