class Producto:
    def __init__(self, nombre, precio, anio):
        self.nombre = nombre
        self.precio = precio
        self.anio = anio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Año: {producto.anio}")
    
    def filtrar_por_anio(self, anio):
        productos_filtrados = [producto for producto in self.productos if producto.anio == anio]
        for producto en productos_filtrados:
            print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Año: {producto.anio}")

if __name__ == "__main__":
    catalogo = Catalogo()
    
    for i in range(3):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        anio = int(input(f"Ingrese el año del producto {i+1}: "))
        producto = Producto(nombre, precio, anio)
        catalogo.agregar_producto(producto)
    
    catalogo.mostrar_productos()
    
    anio_filtrar = int(input("Ingrese el año para filtrar productos: "))
    print(f"Filtrando productos del año {anio_filtrar}:")
    catalogo.filtrar_por_anio(anio_filtrar)
