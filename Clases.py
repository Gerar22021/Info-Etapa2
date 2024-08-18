class Plato():
    def __init__(self, nombre, receta,*args):
        self.nombre = nombre
        self.receta = receta
        self.ingredientes = [*args]
        self.disponible = True

    def __str__(self):
        return self.nombre

class Ingrediente():
    pass

class Menu():
    def __init__(self, platos):
        self.platos = [platos]

class Almacen():
    pass

