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

plato1 = Plato('Guiso de arroz con pollo', '1)- Dorar el pollo en un poco de aceite. Retirar y reservar.\n2)- Dorar la cebolla picada en la misma olla donde doramos el pollo.\n3)- Agregar el tomate triturado, el puré, los condimentos a gusto, el azúcar y 1/2 litro de agua. Volver a introducir el pollo y dejar cocinar 20 minutos.\n4)- Luego agregar el arroz, el caldito, revolver y dejar cocinar hasta que el arroz este cocido al punto deseado. Mientras se va cociendo, hay que ir agregando agua y revolviendo de tanto en tanto para controlar y evitar que la preparación se seque.\n5)- Finalmente incorporar las arvejas para que se calienten, probar, alinear de sal y listo!...A comer!', '1 pollo trozado en 8', '1 cebolla grande', '1 morrón', '1 tomate', )
plato2 = Plato('Tarta de atun', '1)-Picar la cebolla, el morrón y el ajo y rehogarlos en aceite.\n2)-Cuando la cebolla esté transparente, agregar el tomate fresco picado y cocer hasta que tome un color rojo oscuro.\n3)-Agregar el atún y remover hasta integrar. Incorporar también la cucharada de puré de tomates.\n4)-Incorporar los huevos batidos y salpimentar. Agregar el orégano (muy poco).\n5)-Si te gustan, agregar las aceitunas picadas.\n6)-Colocar todo en una tartera chica.\n7)-Cerrar los bordes y llover con semillas de sésamo arriba.\n8)-Llevar a horno fuerte hasta que el hojaldre se vea dorado. ¡Listo! Ya tenés tu tarta de atún.', '1 masa de hojaldre', '1/2 cebolla', '1/2 morrón rojo', '1 diente de ajo', '1 tomate chico', '1 cda. de puré de tomates', '2 latas de atún', '1 papa chica', '1 pizca de orégano', '2 huevos', 'Aceitunas (opcional)', 'Semillas de sésamo', 'Sal, pimienta y aceite.')
plato3 = Plato()
plato4 = Plato()
plato5 = Plato()
plato6 = Plato()
plato7 = Plato()
plato8 = Plato()
plato9 = Plato()
plato10 = Plato()
plato11 = Plato()
plato12 = Plato()
plato13 = Plato()
plato14 = Plato()

listaDePlatos = []

listaDePlatos.append(plato1)
listaDePlatos.append(plato2)

listaMenus = []

menu1 = Menu('Semana 1')
menu1.platos.append(plato1)
menu1.platos.append(plato2)
menu1.platos.append(plato3)
menu1.platos.append(plato4)
menu1.platos.append(plato5)
menu1.platos.append(plato6)
menu1.platos.append(plato7)
menu1.platos.append(plato8)

listaMenus.append(menu1)

# IMPLEMENTANDO LA INTERFAZ GRÁFICA

import tkinter as tk
ventana = tk.Tk()
ventana.title('Gestor de menú semanal')
ventana.geometry('400x200')

def agregarPlato():
    ventana = tk.Toplevel()
    ventana.title('Agregar plato')
    ventana.geometry('400x500')

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
        if nombre:
            platoX = Plato(nombre)
            listaDePlatos.append(platoX)
            menu1.platos.append(platoX)
            lista_platos.insert(tk.END, platoX.nombre)
            nombrePlato.delete(0, tk.END)
            

    boton_agregar = tk.Button(ventana, text = 'Agregar', command = agregar_tarea)
    boton_agregar.grid(row=4, column=2)
    
    def eliminar_tarea():
        seleccion = lista_platos.curselection()
        if seleccion:
            print(seleccion)
            lista_platos.delete(seleccion)
            for x in listaDePlatos:
                if x.nombre == seleccion:
                    listaDePlatos.remove(x)

    boton_eliminar = tk.Button(ventana, text = 'Eliminar', command = eliminar_tarea)
    boton_eliminar.grid(row=5, column=2)

    lista_platos = tk.Listbox(ventana)
    for plato in listaDePlatos:
            lista_platos.insert(tk.END, f'{plato.nombre}')
    lista_platos.grid(row=6, column=2)

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




caja1 = tk.Listbox(ventana)
caja2 = tk.Listbox(ventana)
caja3 = tk.Listbox(ventana)
caja4 = tk.Listbox(ventana)
caja5 = tk.Listbox(ventana)
caja6 = tk.Listbox(ventana)
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
