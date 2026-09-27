class InventarioTienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if nombre.strip()== "":
            print("El nombre del producto no puede estar sin nada")
            return

        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben de ser valores positivos")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad            
        }

        self.productos.append(producto)
        print("Producto agregado correctamente")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto ["nombre"].lower() == nombre.lower():

                if cantidad <= 0:
                    print("La cantidad debe ser positiva")
                    return
                if cantidad > producto ["cantidad"]:
                    print("No hay suficiente stock")
                    return

                producto["cantidad"] -= cantidad
                print("Venta realizada")
                return

        print("El producto no existe en el inventario")

    def mostrar_inventario(self):
        if len(self.productos) ==0:
            print("El inventario esta vacio")
            return
        print("\n-----INVENTARIO------")

        for producto in self.productos:
            print(f"Producto: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            print("-------")

    def producto_mas_caro(self):
        if len(self.productos) == 0:
         print("El inventario esta vacio")
         return None

        producto_caro = self.productos[0]
        for producto in self.productos:
            if producto["precio"] > producto_caro["precio"]:
                producto_caro = producto 

        return producto_caro["nombre"], producto_caro["precio"]




nombre_tienda = input("Ingresa el nombre de la tienda: ")

tienda = InventarioTienda(nombre_tienda)
while True:
    print("\n=======")
    print(f"    Inventario: {tienda.nombre}")
    print("=======")
    print("1.Agregar producto")
    print("2.Vender producto")
    print("3.Ver inventario")
    print("4.Consultar producto mas caro")
    print("5.Salir")

    opcion = input ("Selecciona una opcion: ")

    if opcion == "1":

        nombre = input("Nombre del producto: ")

        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))

            tienda.agregar_producto(nombre, precio, cantidad)

        except ValueError:
            print("El precio debe de ser un numero y la cantidad un entero.")

    elif opcion == "2":

        nombre = input("Nombre del producto: ")
        
        try:
            cantidad = int(input("Cantidad a vender: "))

            tienda.vender_producto(nombre, cantidad)

        except ValueError:
            print("La cantidad debe de ser un numero entero")

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        resultado = tienda.producto_mas_caro()

        if resultado is not None:
            nombre, precio = resultado

            print(f"El producto mas caro es: {nombre}")
            print(f"Precio: ${precio:.2f}")

    elif opcion == "5":
        print("Programa terminado")
        break

    else:
        print("Opcion no valida. Selecciona una opcion del 1 al 5.")