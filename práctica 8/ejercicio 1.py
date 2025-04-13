class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1

class B:
    def __init__(self, y):
        self.y = y

    def incrementaYZ(self):
        self.y += 1
        self.z += 1 

    def incrementaZ(self):
        self.z += 1

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

d = D(1, 2, 3)
d.incrementaXYZ()
print(d.x, d.y, d.z)