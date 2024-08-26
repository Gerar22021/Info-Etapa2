# Realizar un programa que pueda agregar platos a un menu y organizarlos
# en los dias de la semana de forma aleatoria pero teniendo en cuenta la disponibilidad
# de ingredientes (los cuales tambien se puedan agregar a un stock de almacen)
# La idea es que nos mantega al tanto de lo que falte en el almacen para poder realizar los platos del menu
# Tambien se puede tener dos opciones, organizar la semana de forma aleatoria o personalizada

#### Clases ####

#---- Plato
#---- ingrediente
#---- menu
#---- almacen

##### CODIGO DE PRUEBAS ####


# Precargando datos iniciales para mostrar al abrir el programa
from Clases import Plato,Ingrediente,Menu,Almacen

plato0 = Plato('---------PLATOS---------')
plato1 = Plato('Guiso de arroz con pollo', '1)- Dorar el pollo en un poco de aceite. Retirar y reservar.\n2)- Dorar la cebolla picada en la misma olla donde doramos el pollo.\n3)- Agregar el tomate triturado, el puré, los condimentos a gusto, el azúcar y 1/2 litro de agua. Volver a introducir el pollo y dejar cocinar 20 minutos.\n4)- Luego agregar el arroz, el caldito, revolver y dejar cocinar hasta que el arroz este cocido al punto deseado. Mientras se va cociendo, hay que ir agregando agua y revolviendo de tanto en tanto para controlar y evitar que la preparación se seque.\n5)- Finalmente incorporar las arvejas para que se calienten, probar, alinear de sal y listo!...A comer!', '1 pollo trozado en 8\n1 cebolla grande\n1 morrón\n1 tomate')
plato2 = Plato('Tarta de atun', '1)-Picar la cebolla, el morrón y el ajo y rehogarlos en aceite.\n2)-Cuando la cebolla esté transparente, agregar el tomate fresco picado y cocer hasta que tome un color rojo oscuro.\n3)-Agregar el atún y remover hasta integrar. Incorporar también la cucharada de puré de tomates.\n4)-Incorporar los huevos batidos y salpimentar. Agregar el orégano (muy poco).\n5)-Si te gustan, agregar las aceitunas picadas.\n6)-Colocar todo en una tartera chica.\n7)-Cerrar los bordes y llover con semillas de sésamo arriba.\n8)-Llevar a horno fuerte hasta que el hojaldre se vea dorado. ¡Listo! Ya tenés tu tarta de atún.', '1 masa de hojaldre\n1/2 cebolla\n1/2 morrón rojo\n1 diente de ajo\n1 tomate chico\n1 cda. de puré de tomates\n2 latas de atún\n1 papa chica\n1 pizca de orégano\n2 huevos\nAceitunas (opcional)\nSemillas de sésamo\nSal, pimienta y aceite.')

listaDePlatos = []

listaDePlatos.append(plato0)
listaDePlatos.append(plato1)
listaDePlatos.append(plato2)

listaMenus = []

menu1 = Menu('Semana 1')
menu1.platos.append(plato0)
menu1.platos.append(plato1)
menu1.platos.append(plato2)

listaMenus.append(menu1)

# IMPLEMENTANDO LA INTERFAZ GRÁFICA

import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Gestor de menú semanal')
ventana.geometry('400x200')

etiqueta1 = tk.Label(ventana, text='LUNES:', justify= 'left')
etiqueta2 = tk.Label(ventana, text='MARTES:')
etiqueta3 = tk.Label(ventana, text='MIERCOLES:')
etiqueta4 = tk.Label(ventana, text='JUEVES:')
etiqueta5 = tk.Label(ventana, text='VIERNES:')
etiqueta6 = tk.Label(ventana, text='SABADO:')
etiqueta7 = tk.Label(ventana, text='DOMINGO:')

etiqueta1.grid(row=1, column=0)
etiqueta2.grid(row=2, column=0)
etiqueta3.grid(row=3, column=0)
etiqueta4.grid(row=4, column=0)
etiqueta5.grid(row=5, column=0)
etiqueta6.grid(row=6, column=0)
etiqueta7.grid(row=7, column=0)

def organizar():
    pass

boton_organizar = tk.Button(ventana, text='Organizar de forma aleatoria', command=organizar)
boton_organizar.grid(row=0,column=0)

# reloj = tk.Label(ventana, font =
# ('Arial', 60), bg = 'blue', fg = 'white')
# def hora():
#     tiempo_actual =time.strftime('%H:%M')
#     reloj.config(text = tiempo_actual, height=50, width=50)
# ventana.after(1000, hora)
# reloj.pack(anchor = 'center')
# hora()

def agregarPlato():
    ventana = tk.Toplevel()
    ventana.title('Agregar plato')
    ventana.geometry('400x600')

    etiqueta1 = tk.Label(ventana, text= 'Nombre:')
    etiqueta1.grid(row=1,column=1)
    nombrePlato = tk.Entry(ventana, width=26)
    nombrePlato.grid(row=1, column=2, padx=0)
    
    etiqueta2 = tk.Label(ventana, text= 'Ingredientes:')
    etiqueta2.grid(row=2,column=1,padx=20)
    ingreso_ingredientes = tk.Text(ventana, width=20, height=10)
    ingreso_ingredientes.grid(row=2, column=2)

    etiqueta2 = tk.Label(ventana, text= 'Receta:')
    etiqueta2.grid(row=3,column=1,padx=20)
    ingreso_receta = tk.Text(ventana, width=20, height=10)
    ingreso_receta.grid(row=3, column=2)
    lista_platos = []

    
    def agregar_tarea():
        nombre = nombrePlato.get()
        receta = ingreso_receta.get('1.0', 'end-1c')
        Ingredientes = ingreso_ingredientes.get('1.0', 'end-1c')
        if nombre:
            platoX = Plato(nombre,receta,Ingredientes)
            print(platoX)
            listaDePlatos.append(platoX)
            menu1.platos.append(platoX)
            lista_platos.insert(tk.END, platoX.nombre)
            nombrePlato.delete(0, tk.END)
            ingreso_receta.delete('1.0', 'end-1c')
            ingreso_ingredientes.delete('1.0', 'end-1c')
            

    boton_agregar = tk.Button(ventana, text = 'Agregar', command = agregar_tarea)
    boton_agregar.grid(row=4, column=1)
    
    def eliminar_tarea():
        seleccion = lista_platos.curselection()
        if seleccion:
             for c in seleccion:
                if int(c):
                    listaDePlatos.pop(c)
                    lista_platos.delete(seleccion)

    boton_eliminar = tk.Button(ventana, text = 'Eliminar', command = eliminar_tarea)
    boton_eliminar.grid(row=5, column=1)

    lista_platos = tk.Listbox(ventana)
    for plato in listaDePlatos:
            lista_platos.insert(tk.END, f'{plato.nombre}')
    lista_platos.grid(row=6, column=1)

    # cajaNombre = tk.Text(ventana, width=10, height=10)
    # cajaIngredientes = tk.Text(ventana, width=10, height=10)
    # cajaReceta = tk.Text(ventana, width=10, height=10)
    # cajaNombre.grid(row=6,column=2)
    # cajaIngredientes.grid(row=6,column=3)
    # cajaReceta.grid(row=6,column=4)
    # etiquetaNombre = tk.Label(ventana)
    # etiquetaNombre.grid(row=6,column=2, ipadx=0, ipady=0)
    # etiquetaIngredientes = tk.Label(ventana)
    # etiquetaIngredientes.grid(row=6,column=3, ipadx=0, ipady=0)
    # etiquetaReceta = tk.Label(ventana)
    # etiquetaReceta.grid(row=6,column=4, ipadx=0, ipady=0)


    def mostrar():
        seleccion = lista_platos.curselection()
        if seleccion:
             for c in seleccion:
                if int(c):
                    etiquetaNombre = tk.Label(ventana, text= listaDePlatos[c].nombre)
                    etiquetaNombre.config(text=listaDePlatos[c].nombre)
                    etiquetaNombre.grid(row=6,column=2, ipadx=0, ipady=0)
                    etiquetaIngredientes = tk.Label(ventana, text= listaDePlatos[c].ingredientes)
                    etiquetaIngredientes.config(text=listaDePlatos[c].ingredientes)
                    etiquetaIngredientes.grid(row=6,column=3, ipadx=0, ipady=0)
                    etiquetaReceta = tk.Label(ventana, text= listaDePlatos[c].receta)
                    etiquetaReceta.config(text=listaDePlatos[c].receta)
                    etiquetaReceta.grid(row=6,column=4, ipadx=0, ipady=0)

    boton_mostrar = tk.Button(ventana, text = 'Mostrar', command = mostrar)
    boton_mostrar.grid(row=7, column=1)

def agregarMenu():
    ventana = tk.Toplevel()
    ventana.title('Agregar menu')
    ventana.geometry('400x200')
    ingreso_tarea = tk.Entry(ventana)
    ingreso_tarea.pack()
    lista_tareas = []
    def agregar_tarea():
        tarea = ingreso_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
        ingreso_tarea.delete(0, tk.END)
    boton_agregar = tk.Button(ventana, text = 'Agregar', command = agregar_tarea)
    boton_agregar.pack()
    def eliminar_tarea():
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion)
    boton_eliminar = tk.Button(ventana, text = 'Eliminar', command = eliminar_tarea)
    boton_eliminar.pack()
    lista_tareas = tk.Listbox(ventana)
    lista_tareas.pack()
    
def modificarPlato():
    ventana = tk.Toplevel()
    ventana.title('Modificar plato' )
    ventana.geometry ('400x200' )
    marco = tk.Frame(ventana)
    marco.pack(padx = 50, pady = 50)
    scrollbar = tk.Scrollbar (marco)
    scrollbar .pack(side = tk.RIGHT, fill =tk.Y)
    lista = tk.Listbox(marco, yscrollcommand= scrollbar .set, width=100)

    for plato in listaDePlatos:
            lista.insert(tk.END, f'{plato.nombre}')
    lista.pack(side = tk.LEFT, fill =tk.BOTH)
    scrollbar .config(command = lista.yview)

    def Modificar_plato():
        pass

    boton_modificar = tk.Button(ventana, text = 'Modificar', command = Modificar_plato)
    boton_modificar.pack()

    ventana.mainloop ()

def modificarMenu():
    ventana = tk.Toplevel()
    ventana.title('Modificar menú' )
    ventana.geometry ('400x200' )
    marco = tk.Frame(ventana)
    marco.pack(padx = 10, pady = 10)
    scrollbar = tk.Scrollbar (marco)
    scrollbar .pack(side = tk.RIGHT, fill =tk.Y)
    lista = tk.Listbox(marco, yscrollcommand= scrollbar .set)
    for i in range(1):
        lista.insert(tk.END, f'{listaMenus[i].nombre}')
    lista.pack(side = tk.LEFT, fill =tk.BOTH)
    scrollbar .config(command = lista.yview)
    ventana.mainloop ()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'Opciones', menu=menu_principal)

submenu1 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Platos', menu=submenu1)
submenu1.add_command(label = 'Agregar o eliminar', command= agregarPlato)
submenu1.add_command(label = 'Modificar', command= modificarPlato)

submenu2 = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Menús', menu=submenu2)
submenu2.add_command(label = 'Agregar', command= agregarMenu)
submenu2.add_command(label = 'modificar', command= modificarMenu)




# caja1 = tk.Listbox(ventana)
# caja2 = tk.Listbox(ventana)
# caja3 = tk.Listbox(ventana)
# caja4 = tk.Listbox(ventana)
# caja5 = tk.Listbox(ventana)
# caja6 = tk.Listbox(ventana)
# caja1.grid(row=1,column=1)
# caja2.grid(row=1,column=2)
# caja3.grid(row=1,column=3)
# caja4.grid(row=2,column=1)
# caja5.grid(row=2,column=2)
# caja6.grid(row=2,column=3)

ventana.mainloop()

# almacen1 = Almacen('Productos')

# almacen1.heladera['queso'] = 1

# print(almacen1)

# almacen1.heladera['salame'] = 1

# print(almacen1)

# almacen1.heladera['salame'] = almacen1.heladera['salame'] - 1

# print(almacen1)
