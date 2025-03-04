class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (!isFull()) {
            arreglo[++top] = e;
        }
    }

    public Long pop() {
        if (!isEmpty()) {
            return arreglo[top--];
        }
        return null; // Si está vacía
    }

    public Long peek() {
        if (!isEmpty()) {
            return arreglo[top];
        }
        return null; // Si está vacía
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }
}

public class Main {
    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.push(10);
        pila.push(20);
        System.out.println("Tope de la pila: " + pila.peek()); // Salida: 20
        System.out.println("Elemento desapilado: " + pila.pop()); // Salida: 20
    }
}