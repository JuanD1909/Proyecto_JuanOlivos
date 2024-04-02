class PC:
    def __init__(self, nombre, descripcion, precio, cantidad_disponible):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

class Carrito:
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super().__new__(cls)
            cls.instancia.productos = []
        return cls.instancia

    def agregar_producto(self, producto, cantidad=1):
        for item in self.productos:
            if item["producto"] == producto:
                item["cantidad"] += cantidad
                break
        else:
            self.productos.append({"producto": producto, "cantidad": cantidad})

    def eliminar_producto(self, producto):
        self.productos = [item for item in self.productos if item["producto"] != producto]

    def calcular_total(self):
        return sum(item["producto"].precio * item["cantidad"] for item in self.productos)

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def agregar_al_carrito(self, producto, cantidad=1):
        if cantidad <= producto.cantidad_disponible:
            self.carrito.agregar_producto(producto, cantidad)
            print(f"¡{cantidad} {producto.nombre} añadido al carrito!")
        else:
            print("¡La cantidad deseada no está disponible!")

    def ver_carrito(self):
        if not self.carrito.productos:
            print("¡El carrito está vacío!")
        else:
            print("Productos en el carrito:")
            for item in self.carrito.productos:
                producto = item["producto"]
                print(f"- {producto.nombre}: ${producto.precio} x {item['cantidad']}")
            print(f"Precio total: ${self.carrito.calcular_total()}")

    def hacer_pedido(self):
        if not self.carrito.productos:
            print("¡El carrito está vacío!")
            return

        total = self.carrito.calcular_total()
        print(f"Total del pedido: ${total}")

        direccion = input("Ingrese su dirección de envío: ")
        tarjeta = input("Ingrese su método de pago: ")
        print("¡Pedido confirmado!")

        self.carrito.productos = []

def main():
    pc_gamer = PC("PC Gamer", "Potente computadora diseñada para juegos de alto rendimiento", 1500000, 10)
    laptop = PC("Laptop", "Computadora portátil con pantalla de 15 pulgadas y procesador Intel Core i7", 1200000, 15)
    desktop = PC("Desktop", "Computadora de escritorio con amplio espacio de almacenamiento y tarjeta gráfica dedicada", 1000000, 20)

    nombre_cliente = input("Ingrese su nombre y apellido: ")
    cliente = Cliente(nombre_cliente)

    while True:
        print("\n1. Ver Productos")
        print("2. Ver detalles de Productos")
        print("3. Agregar producto al Carrito")
        print("4. Ver Carrito")
        print("5. Realizar pedido")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nProductos disponibles:")
            print(f"1. {pc_gamer.nombre}")
            print(f"2. {laptop.nombre}")
            print(f"3. {desktop.nombre}")

        elif opcion == "2":
            print("\nDetalles de productos:")
            print(f"1. {pc_gamer.nombre}: {pc_gamer.descripcion}, ${pc_gamer.precio}")
            print(f"2. {laptop.nombre}: {laptop.descripcion}, ${laptop.precio}")
            print(f"3. {desktop.nombre}: {desktop.descripcion}, ${desktop.precio}")

        elif opcion == "3":
            print("\nProductos disponibles:")
            print(f"1. {pc_gamer.nombre}")
            print(f"2. {laptop.nombre}")
            print(f"3. {desktop.nombre}")
            producto_seleccionado = input("Ingrese el número del producto que desea agregar: ")
            cantidad = int(input("Ingrese la cantidad que desea: "))
            if producto_seleccionado == "1":
                cliente.agregar_al_carrito(pc_gamer, cantidad)
            elif producto_seleccionado == "2":
                cliente.agregar_al_carrito(laptop, cantidad)
            elif producto_seleccionado == "3":
                cliente.agregar_al_carrito(desktop, cantidad)
            else:
                print("¡El producto no existe!")

        elif opcion == "4":
            cliente.ver_carrito()

        elif opcion == "5":
            cliente.hacer_pedido()
            break

        elif opcion == "6":
            print("¡Gracias por su visita, hasta luego!")
            break

print("Bienvenido a la Tienda de Tecnología TechTech")
if __name__ == "__main__":
    main()
