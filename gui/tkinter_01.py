import tkinter as tk

def responder():
    print("Hola mundo")
    
root = tk.Tk()
boton = tk.Button(root, text="Saludar", command=responder)
boton.pack()
root.mainloop()
