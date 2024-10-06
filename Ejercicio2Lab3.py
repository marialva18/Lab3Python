def obtener_calificaciones():
    while True:
        try:
            calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
            lista_calificaciones = calificaciones.split(',')
            lista_calificaciones = [int(calificacion) for calificacion in lista_calificaciones]
            print(lista_calificaciones)
            break
        except ValueError:
            print("Error: Asegúrese de ingresar números enteros separados por comas.")

if __name__ == "__main__":
    obtener_calificaciones()