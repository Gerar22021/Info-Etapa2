class Plato():
    def __init__(self, nombre= None, receta= None,*args) -> None:
        self.nombre = nombre
        self.receta = receta
        self.ingredientes = [*args]
        self.disponible = True

    def __str__(self):
        return f'Nombre del plato: {self.nombre}\nIngredientes: {self.ingredientes}\nReceta: \n{self.receta}\nDisponible: {self.disponible}'

class Ingrediente():
    def __init__(self, nombre, caducidad = None, cantidad = 0) -> None:
        self.nombre = nombre
        self.caducidad = caducidad
        self.cantidad = cantidad

class Menu():

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.platos = []

class Almacen():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.heladera = {}
        self.mercaderia = {}
        self.verduras = {}
        self.condimentos = {}

    def controlStock(self):
        pass

    def __str__(self):
        return f'{self.heladera}'





