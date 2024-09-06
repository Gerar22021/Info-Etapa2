import pymysql

conexion = pymysql.connect(
    host='localhost',
    user='root',
    password='facil'
)

cursor = conexion.cursor()

def crear_bd():
    sql_create = "CREATE DATABASE IF NOT EXISTS restaurante"
    cursor.execute(query=sql_create)
    sql_use = "USE restaurante"
    cursor.execute(query=sql_use)
    print("Base de datos 'restaurante' fue creada exitosamente! ")

def crear_tabla_platos():
    sql_create_table = """CREATE TABLE IF NOT EXISTS platos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(20) NOT NULL,
        precio DECIMAL(10,2) NOT NULL
    )"""
    cursor.execute(query=sql_create_table)
    conexion.commit()
    print("Tabla 'platos' fue creada exitosamente! ")

def insertar_datos():
    cursor.execute("INSERT INTO platos (nombre,precio) VALUES ('Pizza mozzarella', 8000)")
    cursor.execute("INSERT INTO platos (nombre,precio) VALUES ('Pizza margarita', 10000)")
    cursor.execute("INSERT INTO platos (nombre,precio) VALUES ('Pizza napolitana', 10000)")

    conexion.commit()

    print("Platos insertados correctamente!")

def consultar_platos():
    cursor.execute("SELECT * FROM platos")

    platos = cursor.fetchall()

    for plato in platos:
        print(f'ID:{plato[0]}\nNombre: {plato[1]}\nPrecio: {plato[2]}\n----------------')

crear_bd()
crear_tabla_platos()
insertar_datos()
consultar_platos()
cursor.close()
conexion.close()