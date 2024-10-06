class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2

if __name__ == "__main__":
    radio1 = float(input("Ingrese el radio del primer círculo: "))
    radio2 = float(input("Ingrese el radio del segundo círculo: "))
    circulo1 = Circulo(radio1)
    circulo2 = Circulo(radio2)
    print(f"Área del círculo 1: {circulo1.calcular_area()}")
    print(f"Área del círculo 2: {circulo2.calcular_area()}")
