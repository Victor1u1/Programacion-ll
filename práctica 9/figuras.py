import tkinter as tk
import random
import math
from abc import ABC, abstractmethod

class Coloreado:
    def como_colorear(self):
        return "Colorear los cuatro lados"

class Figura(ABC):
    def __init__(self, color="Sin color"):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio, color="Azul"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

def generar_figuras():
    salida.delete("1.0", tk.END)  
    figuras = []

    for _ in range(5):
        tipo = random.randint(1, 2)
        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio)

        figuras.append(figura)

    for fig in figuras:
        salida.insert(tk.END, f"Figura: {fig.__class__.__name__}\n")
        salida.insert(tk.END, f"Área: {fig.area():.2f}\n")
        salida.insert(tk.END, f"Perímetro: {fig.perimetro():.2f}\n")
        salida.insert(tk.END, f"Color: {fig.get_color()}\n")
        if isinstance(fig, Coloreado):
            salida.insert(tk.END, f"Cómo colorear: {fig.como_colorear()}\n")
        salida.insert(tk.END, "--------------------------\n")

ventana = tk.Tk()
ventana.title("Figuras Aleatorias con Coloreado")
ventana.geometry("450x400")

titulo = tk.Label(ventana, text="Generador de Figuras", font=("Arial", 16))
titulo.pack(pady=10)

btn_generar = tk.Button(ventana, text="Generar Figuras", command=generar_figuras)
btn_generar.pack()

salida = tk.Text(ventana, height=18, width=50)
salida.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
btn_salir.pack()

ventana.mainloop()
