class Cola:
    def _init_(self, n):
        self._arreglo = [0] * n  # Lista de tamaño fijo
        self._inicio = 0
        self._fin = -1
        self._n = n
        self._cantidad = 0

    def insert(self, e):
        if not self.isFull():
            self._fin = (self._fin + 1) % self._n
            self._arreglo[self._fin] = e
            self._cantidad += 1

    def remove(self):
        if not self.isEmpty():
            valor = self._arreglo[self._inicio]
            self._inicio = (self._inicio + 1) % self._n
            self._cantidad -= 1
            return valor
        return None  # Si está vacía

    def peek(self):
        if not self.isEmpty():
            return self._arreglo[self._inicio]
        return None  # Si está vacía

    def isEmpty(self):
        return self._cantidad == 0

    def isFull(self):
        return self._cantidad == self._n

    def size(self):
        return self._cantidad

# Ejemplo de uso
cola = Cola(5)
cola.insert(10)
cola.insert(20)
print("Frente de la cola:", cola.peek()) 
print("Elemento removido:", cola.remove()) 