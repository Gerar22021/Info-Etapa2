import tkinter as tk

def saludar():
    pass

ventana1 = tk.Tk()
ventana1.title('Gestor de menú semanal')
ventana1.geometry('700x700')

etiqueta1 = tk.Label(ventana1, text='Bienvenido al organizador de menú', font=('arial', 20))
etiqueta1.grid(column=2)

boton1 = tk.Button(ventana1, text='Platos', font=('arial',20), command=saludar)
boton1.grid(column=1,row=2)
boton2 = tk.Button(ventana1, text='Almecen', font=('arial',20), command=saludar)
boton2.grid(column=2,row=2)

ventana1.mainloop()