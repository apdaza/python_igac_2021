import tkinter as tk
from punto import Punto

class TkDistancia:
    def __init__(self):
        self.root = tk.Tk()
        self.p1 = Punto(0, 0)
        self.p2 = Punto(0, 0)
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.lbl_punto1 = tk.Label(self.frame, text="Punto 1:")
        self.lbl_punto1.pack()

        self.var_punto1 = tk.StringVar()
        self.txt_punto1 = tk.Entry(self.frame, textvariable=self.var_punto1)
        self.txt_punto1.pack()

        self.lbl_punto2 = tk.Label(self.frame, text="Punto 2:")
        self.lbl_punto2.pack()

        self.var_punto2 = tk.StringVar()
        self.txt_punto2 = tk.Entry(self.frame, textvariable=self.var_punto2)
        self.txt_punto2.pack()

        self.var_distancia = tk.StringVar()
        self.lbl_distancia = tk.Label(self.frame, textvariable=self.var_distancia)
        self.lbl_distancia.pack()

        self.boton = tk.Button(self.frame, text="Calcular distancia", command=self.calcular)
        self.boton.pack()

        self.root.mainloop()

    def calcular(self):
        punto1 = [int(x) for x in self.var_punto1.get().split(",")]
        punto2 = [int(x) for x in self.var_punto2.get().split(",")]

        self.p1.x = punto1[0]
        self.p1.y = punto1[1]

        self.p2.x = punto2[0]
        self.p2.y = punto2[1]

        distancia = self.p1.calcular_distancia(self.p2)

        self.var_distancia.set(str(distancia))

app = TkDistancia()   

