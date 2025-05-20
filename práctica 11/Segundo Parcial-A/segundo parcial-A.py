class Anuncio:
    def __init__(self, numero, precio):  
        self.numero, self.precio = numero, precio

class Artista:
    def __init__(self, nombre, ci, experiencia):
        self.nombre, self.ci, self.experiencia = nombre, ci, experiencia

class Obra:
    def __init__(self, titulo, material, artistas, anuncio=None):  
        self.titulo, self.material = titulo, material
        self.artistas, self.anuncio = artistas, anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, artistas, genero, anuncio=None):
        super().__init__(titulo, material, artistas, anuncio)
        self.genero = genero

# a. Crear una pintura con anuncio y otra sin anuncio
a1, a2 = Artista("Mario", "111", 8), Artista("Ana", "222", 15)
p1 = Pintura("Atardecer", "acuarela", [a1], "Naturalismo", Anuncio(10, 900))
p2 = Pintura("Retrato", "óleo", [a2], "Retrato")

print(f"Pintura 1: {p1.titulo}, con anuncio: {p1.anuncio.numero}, Precio: {p1.anuncio.precio}")
print(f"Pintura 2: {p2.titulo}, sin anuncio: {p2.anuncio}")

# b. Mostrar el nombre del artista con más experiencia
def artista_mas_experimentado(pinturas):
    return max((art for p in pinturas for art in p.artistas), key=lambda a: a.experiencia).nombre

print("Artista con más experiencia:", artista_mas_experimentado([p1, p2]))

# c. Agregar anuncio a pintura sin anuncio y calcular total de venta
p2.anuncio = Anuncio(11, 1100)
total = p1.anuncio.precio + p2.anuncio.precio

print(f"Anuncio agregado a {p2.titulo}, nuevo total de venta: {total}")
