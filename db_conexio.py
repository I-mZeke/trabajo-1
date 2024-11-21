import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",  
        user="tu_usuario",
        password="tu_contraseña",
        database="nombre_base_datos"
    )