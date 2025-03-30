import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, otro): 
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __mul__(self, escalar):  
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)

    def magnitud(self):  
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def producto_escalar(self, otro):  
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def producto_vectorial(self, otro):  
        return Vector3D(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

v1 = Vector3D(2, 3, 4)
v2 = Vector3D(5, 6, 7)

print("Suma:", f"({(v1 + v2).x}, {(v1 + v2).y}, {(v1 + v2).z})")
print("Multiplicación por escalar:", f"({(v1 * 3).x}, {(v1 * 3).y}, {(v1 * 3).z})")
print("Magnitud de v1:", v1.magnitud())
print("Producto escalar:", v1.producto_escalar(v2))
producto_vec = v1.producto_vectorial(v2)
print("Producto vectorial:", f"({producto_vec.x}, {producto_vec.y}, {producto_vec.z})")