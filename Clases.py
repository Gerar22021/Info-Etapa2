class Plato():
    def __init__(self, nombre, receta,*args):
        self.nombre = nombre
        self.receta = receta
        self.ingredientes = [*args]
        self.disponible = True

    def __str__(self):
        return f'Nombre del plato: {self.nombre}\nReceta: {self.receta}\nIngredientes: {self.ingredientes}'

class Ingrediente():
    def __init__(self, nombre, cantidad) -> None:
        self.nombre = nombre
        self.cantidad = cantidad

class Menu():

    def __init__(self, nombre):
        self.nombre = nombre
        self.platos = []

class Almacen():
    def __init__(self, nombre) -> None:
        self.nombre = nombre


