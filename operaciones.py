from db_conexio import obtener_conexion

def listar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos

def agregar_producto(nombre, precio, tipo_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, tipo_id) VALUES (%s, %s, %s)", (nombre, precio, tipo_id))
    conexion.commit()
    conexion.close()

def actualizar_producto(id_producto, nombre, precio, tipo_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET nombre=%s, precio=%s, tipo_id=%s WHERE id=%s", (nombre, precio, tipo_id, id_producto))
    conexion.commit()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (id_producto,))
    conexion.commit()
    conexion.close()
