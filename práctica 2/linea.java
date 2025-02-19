class Punto {
    private int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

class Linea {
    private Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    @Override
    public String toString() {
        return "Línea p1 " + p1 + " y línea p2 " + p2;
    }

    public void dibujaLinea() {
        System.out.println("Dibujando desde p1 " + p1 + " hasta p2 " + p2);
    }
}

public class Main {
    public static void main(String[] args) {
        Punto punto1 = new Punto(5, 5);
        Punto punto2 = new Punto(70, 50);
        Linea linea = new Linea(punto1, punto2);
        System.out.println(linea);
        
        
        
        
        
        
        

        linea.dibujaLinea();
    }
}
