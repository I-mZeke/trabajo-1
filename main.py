from operaciones import tipo_producto_operaciones, repartidor_operaciones

def menu():
    while True:
        print("\n--- Menú de Gestión ---")
        print("1. Gestión de repartidores")
        print("2. Gestión de productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_repartidores()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_repartidores():
    while True:
        print("\n--- Gestión de Repartidores ---")
        print("1. Listar")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            repartidores = repartidor_operaciones.listar_repartidores()
            for r in repartidores:
                print(r)
        elif opcion == "2":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            repartidor_operaciones.agregar_repartidor(nombre, telefono)
        elif opcion == "3":
            id_repartidor = input("ID del repartidor a actualizar: ")
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            repartidor_operaciones.actualizar_repartidor(id_repartidor, nombre, telefono)
        elif opcion == "4":
            id_repartidor = input("ID del repartidor a eliminar: ")
            repartidor_operaciones.eliminar_repartidor(id_repartidor)
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Listar")
        print("2. Agregar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            productos = tipo_producto_operaciones.listar_productos()
            for p in productos:
                print(p)
        elif opcion == "2":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            tipo_id = int(input("ID del tipo de producto: "))
            tipo_producto_operaciones.agregar_producto(nombre, precio, tipo_id)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre: ")
            precio = float(input("Nuevo precio: "))
            tipo_id = int(input("Nuevo ID del tipo de producto: "))
            tipo_producto_operaciones.actualizar_producto(id_producto, nombre, precio, tipo_id)
        elif opcion == "4":
            id_producto = input("ID del producto a eliminar: ")
            tipo_producto_operaciones.eliminar_producto(id_producto)
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
