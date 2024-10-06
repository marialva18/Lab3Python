def suma(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido para suma.")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido para resta.")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido para producto.")

def division(a, b):
    try:
        if b == 0:
            raise ArithmeticError("Error: No es posible dividir entre cero.")
        return a / b
    except ArithmeticError as e:
        print(e)
    except TypeError:
        print("Error: Tipo de dato no válido para división.")
