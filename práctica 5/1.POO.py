import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return self.b**2 - 4*self.a*self.c

    def get_raiz1(self):
        d = self.get_discriminante()
        if d >= 0:
            return (-self.b + math.sqrt(d)) / (2*self.a)
        return None

    def get_raiz2(self):
        d = self.get_discriminante()
        if d > 0:
            return (-self.b - math.sqrt(d)) / (2*self.a)
        return None

    def resolver(self):
        d = self.get_discriminante()
        if d > 0:
            r1 = self.get_raiz1()
            r2 = self.get_raiz2()
            print(f"La ecuación tiene dos raíces {r1:.6f} y {r2:.5f}")
        elif d == 0:
            r1 = self.get_raiz1()
            if r1 == int(r1): 
                print(f"La ecuación tiene una raíz {int(r1)}")
            else:
                print(f"La ecuación tiene una raíz {r1:.5f}")
        else:
            print("La ecuación no tiene raíces reales")

a, b, c = map(float, input("Ingrese a, b, c: ").split())
ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.resolver()