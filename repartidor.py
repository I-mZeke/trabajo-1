from db_conexio import obtener_conexion

def listar_repartidores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM repartidores")
    repartidores = cursor.fetchall()
    conexion.close()
    return repartidores

def agregar_repartidor(nombre, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO repartidores (nombre, telefono) VALUES (%s, %s)", (nombre, telefono))
    conexion.commit()
    conexion.close()

def actualizar_repartidor(id_repartidor, nombre, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE repartidores SET nombre=%s, telefono=%s WHERE id=%s", (nombre, telefono, id_repartidor))
    conexion.commit()
    conexion.close()

def eliminar_repartidor(id_repartidor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM repartidores WHERE id=%s", (id_repartidor,))
    conexion.commit()
    conexion.close()
