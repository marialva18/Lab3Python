class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    lado = float(input("Ingrese el lado del cuadrado: "))
    rectangulo = Rectangulo(largo, ancho)
    cuadrado = Cuadrado(lado)
    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Área del cuadrado: {cuadrado.calcular_area()}")
