class Pila:
    def _init_(self, n):
        self._arreglo = [0] * n  # Lista de tamaño fijo
        self._top = -1
        self._n = n

    def push(self, e):
        if not self.isFull():
            self._top += 1
            self._arreglo[self._top] = e

    def pop(self):
        if not self.isEmpty():
            valor = self._arreglo[self._top]
            self._top -= 1
            return valor
        return None  # Si está vacía

    def peek(self):
        if not self.isEmpty():
            return self._arreglo[self._top]
        return None  # Si está vacía

    def isEmpty(self):
        return self._top == -1

    def isFull(self):
        return self._top == self._n - 1

# Ejemplo de uso
pila = Pila(5)
pila.push(10)
pila.push(20)
print("Tope de la pila:", pila.peek())  
print("Elemento desapilado:", pila.pop())  