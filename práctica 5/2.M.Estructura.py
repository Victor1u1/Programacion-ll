import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros):
    media = promedio(numeros)
    suma_diferencias = sum((x - media) ** 2 for x in numeros)
    return math.sqrt(suma_diferencias / (len(numeros) - 1))

numeros = list(map(float, input().split()))

print(f"El promedio es {promedio(numeros):.2f}")
print(f"La desviación estándar es {desviacion(numeros):.5f}")