import tkinter as tk

def comando():
    print(cb_var.get())

root = tk.Tk()
cb_var = tk.IntVar()
check = tk.Checkbutton(root, text="Prueba", variable=cb_var, command=comando)
check.pack()
root.mainloop()
