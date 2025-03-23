import math

class Estadisticas:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        media = self.promedio()
        suma_diferencias = sum((x - media) ** 2 for x in self.datos)
        return math.sqrt(suma_diferencias / (len(self.datos) - 1))

    def mostrar_resultados(self):
        print(f"El promedio es {self.promedio():.2f}")
        print(f"La desviación estándar es {self.desviacion():.5f}")

numeros = list(map(float, input().split()))
estadisticas = Estadisticas(numeros)
estadisticas.mostrar_resultados()