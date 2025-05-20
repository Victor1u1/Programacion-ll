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

# a. Crear dos objetos pintura que tengan anuncios de venta
a1, a2 = Artista("Carlos", "123", 10), Artista("Lucía", "456", 12)
p1 = Pintura("Paisaje", "óleo", [a1], "Paisajismo", Anuncio(1, 1000))
p2 = Pintura("Marina", "acrílico", [a2], "Marina", Anuncio(2, 1200))

print(f"Pintura 1: {p1.titulo}, Anuncio: {p1.anuncio.numero}, Precio: {p1.anuncio.precio}")
print(f"Pintura 2: {p2.titulo}, Anuncio: {p2.anuncio.numero}, Precio: {p2.anuncio.precio}")

# b. Calcular el promedio de experiencia de los artistas de ambas pinturas
def promedio_experiencia(pinturas):
    experiencias = [art.experiencia for p in pinturas for art in p.artistas]
    return sum(experiencias) / len(experiencias)

print("Promedio de experiencia de los artistas:", promedio_experiencia([p1, p2]))

# c. Incrementar el precio en X a la pintura del artista con nombre X
def incrementar_precio(pinturas, nombre, x):
    for p in pinturas:
        if any(art.nombre == nombre for art in p.artistas) and p.anuncio:
            p.anuncio.precio += x

incrementar_precio([p1, p2], "Carlos", 500)

print(f"Nuevo precio de la pintura de Carlos ({p1.titulo}): {p1.anuncio.precio}")
