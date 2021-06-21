import tkinter as tk

def operacion():
    print(rb_var.get())

root = tk.Tk()
rb_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="1", variable=rb_var, value=1, command=operacion )
radio1.pack()
radio2 = tk.Radiobutton(root, text="2", variable=rb_var, value=2, command=operacion )
radio2.pack()
root.mainloop()
