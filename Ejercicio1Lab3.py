def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ArithmeticError
            if x > y:
                print("Error: X no puede ser mayor que Y.")
                continue
            porcentaje = (x / y) * 100
            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
            break
        except ValueError:
            print("Error: Ingrese solo números enteros en formato X/Y.")
        except ArithmeticError:
            print("Error: No es posible dividir entre cero.")

if __name__ == "__main__":
    obtener_fraccion()
