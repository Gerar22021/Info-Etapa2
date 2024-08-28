# Realizar un programa que pueda agregar platos a un menu y organizarlos
# en los dias de la semana de forma aleatoria pero teniendo en cuenta la disponibilidad
# de ingredientes (los cuales tambien se puedan agregar a un stock de almacen)
# La idea es que nos mantega al tanto de lo que falte en el almacen para poder realizar los platos del menu
# Tambien se puede tener dos opciones, organizar la semana de forma aleatoria o personalizada


from Clases import Plato,Ingrediente,Menu,Almacen
import random


# Precargando datos iniciales para mostrar al abrir el programa

plato0 = Plato('---------PLATOS---------')
plato1 = Plato('Guiso de arroz con pollo', '1)- Dorar el pollo en un poco de aceite. Retirar y reservar.\n2)- Dorar la cebolla picada en la misma olla donde doramos el pollo.\n3)- Agregar el tomate triturado, el puré, los condimentos a gusto, el azúcar y 1/2 litro de agua.\nVolver a introducir el pollo y dejar cocinar 20 minutos.\n4)- Luego agregar el arroz, el caldito,\nrevolver y dejar cocinar hasta que el arroz este cocido al punto deseado.\nMientras se va cociendo, hay que ir agregando agua y revolviendo\nde tanto en tanto para controlar y evitar que la preparación se seque.\n5)- Finalmente incorporar las arvejas para que se calienten,\nprobar, alinear de sal y listo!...A comer!', '1 pollo trozado en 8\n1 cebolla grande\n1 morrón\n1 tomate')
plato2 = Plato('Tarta de atun', '1)-Picar la cebolla, el morrón y el ajo y rehogarlos en aceite.\n2)-Cuando la cebolla esté transparente, agregar el tomate fresco picado\ny cocer hasta que tome un color rojo oscuro.\n3)-Agregar el atún y remover hasta integrar.\nIncorporar también la cucharada de puré de tomates.\n4)-Incorporar los huevos batidos y salpimentar.\nAgregar el orégano (muy poco).\n5)-Si te gustan, agregar las aceitunas picadas.\n6)-Colocar todo en una tartera chica.\n7)-Cerrar los bordes y llover con semillas de sésamo arriba.\n8)-Llevar a horno fuerte hasta que el hojaldre se vea dorado.\n¡Listo! Ya tenés tu tarta de atún.', '1 masa de hojaldre\n1/2 cebolla\n1/2 morrón rojo\n1 diente de ajo\n1 tomate chico\n1 cda. de puré de tomates\n2 latas de atún\n1 papa chica\n1 pizca de orégano\n2 huevos\nAceitunas (opcional)\nSemillas de sésamo\nSal, pimienta y aceite.')

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
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Gestor de menú semanal')
ventana.geometry('450x200')


# Muestra los dias de la semana en la primer columna; el almuerzo y cena en las siguientes
etiqueta1 = tk.Label(ventana, text='LUNES:')
etiqueta2 = tk.Label(ventana, text='MARTES:')
etiqueta3 = tk.Label(ventana, text='MIERCOLES:')
etiqueta4 = tk.Label(ventana, text='JUEVES:')
etiqueta5 = tk.Label(ventana, text='VIERNES:')
etiqueta6 = tk.Label(ventana, text='SABADO:')
etiqueta7 = tk.Label(ventana, text='DOMINGO:')
etiqueta8 = tk.Label(ventana, text='ALMUERZO')
etiqueta9 = tk.Label(ventana, text='CENA')
etiqueta1.grid(row=1, column=0)
etiqueta2.grid(row=2, column=0)
etiqueta3.grid(row=3, column=0)
etiqueta4.grid(row=4, column=0)
etiqueta5.grid(row=5, column=0)
etiqueta6.grid(row=6, column=0)
etiqueta7.grid(row=7, column=0)
etiqueta8.grid(row=0, column=1)
etiqueta9.grid(row=0, column=2)


# Crea listas desplegables con los platos disponibles y los muestra en pantalla
lunesAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
lunesCena = ttk.Combobox(ventana, state="readonly", width=25)
martesAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
martesCena = ttk.Combobox(ventana, state="readonly", width=25)
miercolesAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
miercolesCena = ttk.Combobox(ventana, state="readonly", width=25)
juevesAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
juevesCena = ttk.Combobox(ventana, state="readonly", width=25)
viernesAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
viernesCena = ttk.Combobox(ventana, state="readonly", width=25)
sabadoAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
sabadoCena = ttk.Combobox(ventana, state="readonly", width=25)
domingoAlmuerzo = ttk.Combobox(ventana, state="readonly", width=25)
domingoCena = ttk.Combobox(ventana, state="readonly", width=25)
lunesAlmuerzo.grid(row=1,column=1)
lunesCena.grid(row=1,column=2)
martesAlmuerzo.grid(row=2,column=1)
martesCena.grid(row=2,column=2)
miercolesAlmuerzo.grid(row=3,column=1)
miercolesCena.grid(row=3,column=2)
juevesAlmuerzo.grid(row=4,column=1)
juevesCena.grid(row=4,column=2)
viernesAlmuerzo.grid(row=5,column=1)
viernesCena.grid(row=5,column=2)
sabadoAlmuerzo.grid(row=6,column=1)
sabadoCena.grid(row=6,column=2)
domingoAlmuerzo.grid(row=7,column=1)
domingoCena.grid(row=7,column=2)

# Crea una lista solo con los nombres de los platos
listaDePlatosNombres = []
for x in listaDePlatos:
    listaDePlatosNombres.append(x.nombre)

# Agrega los nombres de los platos a las listas desplegables
lunesAlmuerzo['values'] = listaDePlatosNombres
lunesCena['values'] = listaDePlatosNombres
martesAlmuerzo['values'] = listaDePlatosNombres
martesCena['values'] = listaDePlatosNombres
miercolesAlmuerzo['values'] = listaDePlatosNombres
miercolesCena['values'] = listaDePlatosNombres
juevesAlmuerzo['values'] = listaDePlatosNombres
juevesCena['values'] = listaDePlatosNombres
viernesAlmuerzo['values'] = listaDePlatosNombres
viernesCena['values'] = listaDePlatosNombres
sabadoAlmuerzo['values'] = listaDePlatosNombres
sabadoCena['values'] = listaDePlatosNombres
domingoAlmuerzo['values'] = listaDePlatosNombres
domingoCena['values'] = listaDePlatosNombres

## Funciones ##
def agregarPlato():
    ventana = tk.Toplevel()
    ventana.title('Agregar plato')
    ventana.geometry('850x700')

    etiqueta1 = tk.Label(ventana, text= 'Nombre:')
    etiqueta1.grid(row=1,column=1)
    nombrePlato = tk.Entry(ventana, width=50)
    nombrePlato.grid(row=1, column=2, padx=0)
    
    etiqueta2 = tk.Label(ventana, text= 'Ingredientes:')
    etiqueta2.grid(row=2,column=1,padx=20)
    ingreso_ingredientes = tk.Text(ventana, width=50, height=10)
    ingreso_ingredientes.grid(row=2, column=2)

    etiqueta2 = tk.Label(ventana, text= 'Receta:')
    etiqueta2.grid(row=3,column=1,padx=20)
    ingreso_receta = tk.Text(ventana, width=50, height=10)
    ingreso_receta.grid(row=3, column=2)
    lista_platos = []

    
    def agregar_tarea():
        nombre = nombrePlato.get()
        receta = ingreso_receta.get('1.0', 'end-1c')
        Ingredientes = ingreso_ingredientes.get('1.0', 'end-1c')
        if nombre:
            platoX = Plato(nombre,receta,Ingredientes)
            listaDePlatos.append(platoX)
            menu1.platos.append(platoX)
            listaDePlatosNombres.append(platoX.nombre)
            print(listaDePlatosNombres)
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
                    #listaDePlatosNombres.remove(c)

    boton_eliminar = tk.Button(ventana, text = 'Eliminar', command = eliminar_tarea)
    boton_eliminar.grid(row=5, column=1)

    lista_platos = tk.Listbox(ventana)
    for plato in listaDePlatos:
            lista_platos.insert(tk.END, f'{plato.nombre}')
    lista_platos.grid(row=6, column=1)

    etiquetaNombre = tk.Label(ventana)
    etiquetaNombre.grid(row=6,column=2)
    etiquetaIngredientes = tk.Label(ventana)
    etiquetaIngredientes.grid(row=6,column=3, ipadx=0, ipady=0)
    etiquetaReceta = tk.Label(ventana)
    etiquetaReceta.grid(row=6,column=4)

    def mostrar():
        seleccion = lista_platos.curselection()
        if seleccion:
             for c in seleccion:
                if int(c):
                    etiquetaNombre.config(text=listaDePlatos[c].nombre)
                    etiquetaIngredientes.config(text=listaDePlatos[c].ingredientes)
                    etiquetaReceta.config(text=listaDePlatos[c].receta)
                    

    boton_mostrar = tk.Button(ventana, text = 'Mostrar', command = mostrar)
    boton_mostrar.grid(row=7, column=1)

def modificarPlato():
    ventana = tk.Toplevel()
    ventana.title('Modificar plato' )
    ventana.geometry ('400x400' )
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
        ventana = tk.Toplevel()
        ventana.title('Agregar menu')
        ventana.geometry('400x200')

        

    boton_modificar = tk.Button(ventana, text = 'Modificar', command = Modificar_plato)
    boton_modificar.pack()

    ventana.mainloop ()

def agregarMenu():
    ventana = tk.Toplevel()
    ventana.title('Agregar menu')
    ventana.geometry('400x200')
    ingreso_plato = ttk.Combobox(ventana, state="readonly", width=25)
    ingreso_plato.pack()
    ingreso_plato['values'] = listaDePlatosNombres
    lista_tareas = []
    def agregar_tarea():
        tarea = ingreso_plato.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)

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

def organizar():
    print(len(listaDePlatosNombres))
    lunesAlmuerzo['values']=listaDePlatosNombres
    lunesCena['values'] = listaDePlatosNombres
    martesAlmuerzo['values'] = listaDePlatosNombres
    martesCena['values'] = listaDePlatosNombres
    miercolesAlmuerzo['values'] = listaDePlatosNombres
    miercolesCena['values'] = listaDePlatosNombres
    juevesAlmuerzo['values'] = listaDePlatosNombres
    juevesCena['values'] = listaDePlatosNombres
    viernesAlmuerzo['values'] = listaDePlatosNombres
    viernesCena['values'] = listaDePlatosNombres
    sabadoAlmuerzo['values'] = listaDePlatosNombres
    sabadoCena['values'] = listaDePlatosNombres
    domingoAlmuerzo['values'] = listaDePlatosNombres
    domingoCena['values'] = listaDePlatosNombres
    lunesAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    lunesCena.current(random.randrange(1,len(listaDePlatosNombres)))
    martesAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    martesCena.current(random.randrange(1,len(listaDePlatosNombres)))
    miercolesAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    miercolesCena.current(random.randrange(1,len(listaDePlatosNombres)))
    juevesAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    juevesCena.current(random.randrange(1,len(listaDePlatosNombres)))
    viernesAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    viernesCena.current(random.randrange(1,len(listaDePlatosNombres)))
    sabadoAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    sabadoCena.current(random.randrange(1,len(listaDePlatosNombres)))
    domingoAlmuerzo.current(random.randrange(1,len(listaDePlatosNombres)))
    domingoCena.current(random.randrange(1,len(listaDePlatosNombres)))


# Crea el boton para la organizacion aleatoria
boton_organizar = tk.Button(ventana, text='Organizar de forma aleatoria', command=organizar)
boton_organizar.grid(row=8,column=2)


# Barra de menu
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Opciones', menu=menu_principal)

submenu1 = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Platos', menu=submenu1)
submenu1.add_command(label = 'Agregar o eliminar', command= agregarPlato)
submenu1.add_command(label = 'Modificar', command= modificarPlato)

submenu2 = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Menús', menu=submenu2)
submenu2.add_command(label = 'Agregar', command= agregarMenu)
submenu2.add_command(label = 'modificar', command= modificarMenu)

ventana.mainloop()