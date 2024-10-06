from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return pi * self.radio ** 2

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"Área del círculo: {circulo.calcular_area():.2f}")
        
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.calcular_area():.2f}")
        
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado)
            print(f"Área del cuadrado: {cuadrado.calcular_area():.2f}")
        
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
