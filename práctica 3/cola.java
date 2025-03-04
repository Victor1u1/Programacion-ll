class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int cantidad;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.cantidad = 0;
    }

    public void insert(long e) {
        if (!isFull()) {
            fin = (fin + 1) % n;
            arreglo[fin] = e;
            cantidad++;
        }
    }

    public Long remove() {
        if (!isEmpty()) {
            long valor = arreglo[inicio];
            inicio = (inicio + 1) % n;
            cantidad--;
            return valor;
        }
        return null; // Si está vacía
    }

    public Long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        }
        return null; // Si está vacía
    }

    public boolean isEmpty() {
        return cantidad == 0;
    }

    public boolean isFull() {
        return cantidad == n;
    }

    public int size() {
        return cantidad;
    }
}

public class Main {
    public static void main(String[] args) {
        Cola cola = new Cola(5);
        cola.insert(10);
        cola.insert(20);
        System.out.println("Frente de la cola: " + cola.peek()); // Salida: 10
        System.out.println("Elemento removido: " + cola.remove()); // Salida: 10
    }
}