import math
class FiguraGeometrica:
    def area(self, *args):
        if len(args) == 1:  # círculo
            radio = args[0]
            return math.pi * radio * radio
        
        elif len(args) == 2:  
            base, altura = args
            return base * altura  # rectángulo
        
        elif len(args) == 2:  # T. rectángulo
            base, altura = args
            return (b * h) / 2
        elif len(args) == 3:                 # trapecio
            a, b, h = args
            return ((a + b) * h) / 2
        
        elif len(args) == 2:  # pentágono
            lado, apotema = args
            return (5 * lado * apotema) / 2
        
        else:
            raise ValueError()
        

f = FiguraGeometrica()

print("Círculo:", f.area(2))
print("Rectángulo:", f.area(7, 5.3))
print("Triángulo Rectángulo:", f.area(3.8, 7))
print("Trapecio:", f.area(4, 4, 3))
print("Pentágono:", f.area(7, 2.8))
