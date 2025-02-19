import turtle
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return f"Línea desde p1 {self.p1} hasta p2{self.p2}"
    def dibuja_Linea(self):
        '''Dibujando con Turtle'''
        pantalla = turtle.Screen()
        t = turtle.Turtle()
        # Punto 1 a punto 2
        t.penup()
        t.goto(self.p1.x, self.p1.y)  
        t.pendown()
        t.dot(6, "blue")
        t.goto(self.p2.x, self.p2.y)
        t.dot(6, "red")

punto1 = Punto(5, 5)
punto2 = Punto(70, 50)
linea = Linea(punto1, punto2)
print(linea)
linea.dibuja_Linea()  
