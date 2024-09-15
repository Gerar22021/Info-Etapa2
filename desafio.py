import pymysql

conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='facil'
)

cursor = conexion.cursor()

def crear_bd():
    sql_create = "CREATE DATABASE IF NOT EXISTS escuela"
    cursor.execute(query=sql_create)
    sql_use = "USE escuela"
    cursor.execute(query=sql_use)
    print("Base de datos 'escuela' fue creada exitosamente! ")

def crear_tabla_estudiantes():
    sql_create_table = """CREATE TABLE IF NOT EXISTS estudiantes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(20) NOT NULL,
        edad INT NOT NULL,
        grado VARCHAR(10)
    )"""
    cursor.execute(query=sql_create_table)
    conexion.commit()
    print("Tabla 'estudiantes' fue creada exitosamente! ")

def insertar_datos():
    cursor.execute("INSERT INTO Estudiantes (nombre,precio) VALUES ('Pizza mozzarella', 8000)")
    cursor.execute("INSERT INTO Estudiantes (nombre,precio) VALUES ('Pizza margarita', 10000)")
    cursor.execute("INSERT INTO Estudiantes (nombre,precio) VALUES ('Pizza napolitana', 10000)")

    conexion.commit()

    print("Platos insertados correctamente!")

# crear_bd()
# crear_tabla_estudiantes()

while True:
    print("# SISTEMA DE GESTION DE ESTUDIANTES #\n\n-------------------------------------\n")
    print("1)-Agregar estudiante\n2)-Ver todos los estudiante\n3)-Actualizar estudiante\n4)-Eliminar un estudiante\n5)-Salir\n")
    op = input()

    if op == 5:
        break
    
    elif op == 1:
        insertar_datos()

    elif op

