class GestionBiblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def listar_libros(self):
        for libro en self.libros:
            print(libro)
    
    def buscar_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                print(libro)
    
    def buscar_por_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                print(libro)
