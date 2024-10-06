class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Registro: {self.registro}, Edad: {self.edad}, Nota: {self.nota}")
    
    def asignar_edad(self, edad):
        self.edad = edad
    
    def asignar_nota(self, nota):
        self.nota = nota

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    registro = input("Ingrese el número de registro: ")
    edad = int(input("Ingrese la edad del alumno: "))
    nota = float(input("Ingrese la nota del alumno: "))
    
    alumno = Alumno(nombre, registro)
    alumno.asignar_edad(edad)
    alumno.asignar_nota(nota)
    alumno.mostrar_info()
