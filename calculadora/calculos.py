import operaciones

if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    print(f"Suma: {operaciones.suma(a, b)}")
    print(f"Resta: {operaciones.resta(a, b)}")
    print(f"Producto: {operaciones.producto(a, b)}")
    print(f"División: {operaciones.division(a, b)}")
