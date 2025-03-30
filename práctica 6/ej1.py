import math

class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_cruz(self, otro):
        return AlgebraVectorial(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def es_perpendicular(self, otro):
        return self.producto_punto(otro) == 0
    
    def es_paralelo(self, otro):
        return self.producto_cruz(otro).magnitud() == 0
    
    def proyeccion(self, otro):
        escala = self.producto_punto(otro) / otro.magnitud()**2
        return AlgebraVectorial(escala * otro.x, escala * otro.y, escala * otro.z)
    
    def componente(self, otro):
        return self.producto_punto(otro) / otro.magnitud()

# Ejemplo de uso:
a = AlgebraVectorial(5, -2, 1)
b = AlgebraVectorial(2, 1, -3)

print("¿Son perpendiculares?", a.es_perpendicular(b))
print("¿Son paralelos?", a.es_paralelo(b))
print("Proyección de a sobre b:", vars(a.proyeccion(b)))
print("Componente de a en b:", a.componente(b))