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

from Clases import Plato,Ingrediente,Menu,Almacen

# plato1 = Plato('Guiso de arroz con pollo', '1)- Dorar el pollo en un poco de aceite. Retirar y reservar.\n2)- Dorar la cebolla picada en la misma olla donde doramos el pollo.\n3)- Agregar el tomate triturado, el puré, los condimentos a gusto, el azúcar y 1/2 litro de agua. Volver a introducir el pollo y dejar cocinar 20 minutos.\n4)- Luego agregar el arroz, el caldito, revolver y dejar cocinar hasta que el arroz este cocido al punto deseado. Mientras se va cociendo, hay que ir agregando agua y revolviendo de tanto en tanto para controlar y evitar que la preparación se seque.\n5)- Finalmente incorporar las arvejas para que se calienten, probar, alinear de sal y listo!...A comer!', '1 pollo trozado en 8', '1 cebolla grande', '1 morrón', '1 tomate')

# print(plato1)

almacen1 = Almacen('Productos')

almacen1.heladera['queso'] = 1

print(almacen1)

almacen1.heladera['salame'] = 1

print(almacen1)

almacen1.heladera['salame'] = almacen1.heladera['salame'] - 1

print(almacen1)
