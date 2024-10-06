import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"
    
    def vector(self, otro_punto):
        vector_x = otro_punto.x - self.x
        vector_y = otro_punto.y - self.y
        return (vector_x, vector_y)
    
    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

if __name__ == "__main__":
    # Crear y trabajar con puntos
    x1 = float(input("Ingrese la coordenada X del primer punto: "))
    y1 = float(input("Ingrese la coordenada Y del primer punto: "))
    punto1 = Punto(x1, y1)
    print(f"Punto 1: {punto1}, Cuadrante: {punto1.cuadrante()}")

    x2 = float(input("Ingrese la coordenada X del segundo punto: "))
    y2 = float(input("Ingrese la coordenada Y del segundo punto: "))
    punto2 = Punto(x2, y2)
    print(f"Punto 2: {punto2}, Cuadrante: {punto2.cuadrante()}")

    # Calcular vector y distancia entre dos puntos
    vector = punto1.vector(punto2)
    print(f"El vector desde el punto 1 al punto 2 es: {vector}")
    distancia = punto1.distancia(punto2)
    print(f"La distancia entre los dos puntos es: {distancia:.2f}")

    # Crear rectángulo y calcular base, altura y área
    rectangulo = Rectangulo(punto1, punto2)
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")
