import tkinter as tk

def operacion1():
    print("Comando del boton 1")

def operacion2():
    print("Comando del boton 2")

def operacion3():
    print("Comando del boton 3")
    
root = tk.Tk()
root.geometry("300x100")
boton1 = tk.Button(root, text="Botón 1", command=operacion1)
boton1.pack()
boton2 = tk.Button(root, text="Botón 2", command=operacion2)
boton2.pack()
boton3 = tk.Button(root, text="Botón 3", command=operacion3)
boton3.pack()
root.mainloop()
