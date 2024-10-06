from libro import Libro
from gestion import GestionBiblioteca

def menu():
    gestion = GestionBiblioteca()
    
    while True:
        print("\nMenú:")
        print("1. Agregar un libro a la biblioteca")
        print("2. Listar los libros en la biblioteca")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
        
        elif opcion == "2":
            gestion.listar_libros()
        
        elif opcion == "3":
            titulo = input("Ingrese el título del libro: ")
            gestion.buscar_por_titulo(titulo)
        
        elif opcion == "4":
            autor = input("Ingrese el autor del libro: ")
            gestion.buscar_por_autor(autor)
        
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
