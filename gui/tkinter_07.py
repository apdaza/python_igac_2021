import tkinter as tk

def ventana_nueva():
    ventana = tk.Toplevel(root)
    ventana.title("Ventana Nueva")
    ventana.geometry("400x400")
    ventana.focus_set()
    boton = tk.Button(ventana, text="No hago nada")
    boton.pack()
    
root = tk.Tk()
root.geometry("640x480")
boton = tk.Button(root, text="Abrir ventana", command=ventana_nueva)
boton.pack()
root.mainloop()
