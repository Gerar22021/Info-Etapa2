'''
Desafío 1: Sistema de Gestión de Estudiantes

Desarrollar un pequeño sistema para gestionar una lista de estudiantes en una escuela. 
El sistema debe permitir realizar operaciones básicas sobre una base de datos MySQL.

Base de datos: Debes crear una base de datos llamada escuela y una tabla llamada 
estudiantes que almacene los siguientes datos:

- id (entero, clave primaria, autoincremental)
- nombre (cadena de texto)
- edad (entero)
- grado (cadena de texto)

Menú interactivo: El programa debe mostrar un menú con las siguientes opciones:
-- Agregar un estudiante: El usuario debe ingresar el nombre, edad y grado del estudiante para almacenarlo 
en la base de datos.
-- Ver todos los estudiantes: Mostrar una lista con todos los estudiantes registrados en la base de datos.
-- Actualizar un estudiante: Permitir al usuario modificar los datos de un estudiante existente (nombre, edad 
o grado) usando su id.
-- Eliminar un estudiante: Eliminar un registro de la base de datos según su id.
-- Salir: Cerrar el programa.

El sistema debe validar las entradas del usuario (por ejemplo, asegurarse de que la edad sea un número y 
que los campos no queden vacíos).

'''






'''
Desafío 2: Sistema de Inventario para una Tienda

Desarrollar un sistema de inventario para una tienda que permita registrar, gestionar y consultar los
productos en stock. El sistema debe interactuar con una base de datos MySQL y permitir operaciones
básicas de gestión de inventario.

Base de datos: Crea una base de datos llamada tienda y una tabla llamada productos con los siguientes campos:

- id (entero, clave primaria, autoincremental)
- nombre (cadena de texto)
- cantidad (entero)
- precio (decimal)

Menú interactivo: El programa debe mostrar un menú con las siguientes opciones:

-- Agregar producto: El usuario debe ingresar el nombre del producto, la cantidad en stock y el precio del producto. Estos datos deben guardarse en la base de datos.
-- Ver todos los productos: Mostrar una lista con todos los productos registrados en la base de datos, mostrando su id, nombre, cantidad y precio.
-- Actualizar producto: Permitir al usuario modificar los datos de un producto (nombre, cantidad o precio) usando su id.
-- Eliminar producto: Eliminar un registro de la base de datos según su id.
-- Ver productos en bajo stock: Mostrar los productos cuya cantidad en stock es menor o igual a 5.
-- Salir: Cerrar el programa.

El programa debe validar las entradas del usuario, asegurándose de que la cantidad y el precio sean números válidos.
Asegúrate de que al eliminar un producto se pregunte al usuario si está seguro antes de proceder.

'''