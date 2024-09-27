class Productos:
    def __init__(self):
        # Diccionario de productos
        self.productos = {
            1: {
                "Nombre": "Orden de tacos", 
                "Descripcion": "Tacos al pastor",
                "Precio": 50,
                "Stock": 10,
                "Tipo": "Comida",
                "Fecha_Añadido": "2023-08-15"
            }
        }

    def mostrar_productos(self):
        print("Productos:")
        for id_producto, detalles in self.productos.items():
            print(f"ID Producto: {id_producto}")
            for key, value in detalles.items():
                print(f"{key}: {value}")
        print()

class Clientes:
    def __init__(self):
        # Diccionario de clientes
        self.clientes = {
            1: {
                "Nombre": "Juan",
                "Apellido": "Pérez",
                "Email": "juan.perez@example.com",
                "Teléfono": "123456789",
                "Fecha_Nacimiento": "2000-01-01",
                "Fecha_Registro": "2023-09-01"
            }
        }

    def mostrar_clientes(self):
        print("Clientes:")
        for id_cliente, detalles in self.clientes.items():
            print(f"ID Cliente: {id_cliente}")
            for key, value in detalles.items():
                print(f"{key}: {value}")
        print()

class Ordenes:
    def __init__(self):
        # Diccionario de órdenes
        self.ordenes = {
            1: {
                "ID_Cliente": 1,
                "Fecha_Orden": "2023-09-20",
                "Total": 150,
                "Método_Pago": "Tarjeta",
                "Estado": "Completada",
                "Mesa": 5
            }
        }

    def mostrar_ordenes(self):
        print("Órdenes:")
        for id_orden, detalles in self.ordenes.items():
            print(f"ID Orden: {id_orden}")
            for key, value in detalles.items():
                print(f"{key}: {value}")
        print()

class Empleados:
    def __init__(self):
        # Diccionario de empleados
        self.empleados = {
            1: {
                "Nombre": "Carlos",
                "Apellido": "Ramírez",
                "Puesto": "Mesero",
                "Salario": 8000,
                "Fecha_Contratación": "2022-06-15",
                "Estado": "Activo"
            }
        }

    def mostrar_empleados(self):
        print("Empleados:")
        for id_empleado, detalles in self.empleados.items():
            print(f"ID Empleado: {id_empleado}")
            for key, value in detalles.items():
                print(f"{key}: {value}")
        print()

# Crear instancias de las clases
productos = Productos()
clientes = Clientes()
ordenes = Ordenes()
empleados = Empleados()

# Mostrar datos de cada clase
productos.mostrar_productos()
clientes.mostrar_clientes()
ordenes.mostrar_ordenes()
empleados.mostrar_empleados()
