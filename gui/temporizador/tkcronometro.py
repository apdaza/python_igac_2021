from tkinter import *
from cronometro import Cronometro
from threading import *
from time import sleep

class TkCronometro(Thread):
    def __init__(self):
        self.root = Tk()
        self.crono = Cronometro()
        self.crono.minuto.valor = 3
        self.frame = Frame(self.root)
        self.frame.pack()

        self.valor = StringVar()
        self.display = Label(self.frame,
                             textvariable = self.valor,
                             font=("Helvetica", 30))
        self.display.pack(side=TOP, padx=10, pady=10)

        self.boton_iniciar = Button(self.frame, text="Iniciar/Parar",
                                    command = self.cambiar_estado)
        self.boton_iniciar.pack(side=LEFT)

        self.boton_borrar = Button(self.frame, text="Borrar",
                          command = self.borrar)
        self.boton_borrar.pack(side=RIGHT)

        Thread.__init__(self)
        self.start()

        self.root.mainloop()

    def cambiar_estado(self):
        self.crono.cambiar_estado()

    def borrar(self):
        self.crono.borrar()

    def run(self):
        while True:
            if not self.crono.parado:
                self.crono.avanzar()
                
            sleep(0.1)
            self.valor.set(self.crono.retornar_tiempo())
            if self.crono.minuto == 0 and self.crono.segundo == 0:
                self.cambiar_estado()

    def callback(self):
        self.root.quit()
        

app = TkCronometro()
