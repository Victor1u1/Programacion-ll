public class Main {

    static class Punto {
        int x, y;
        Punto(int x, int y) { this.x = x; this.y = y; }
        public String toString() { return "(" + x + ", " + y + ")"; }
    }

    static class Circulo {
        Punto c;
        double r;
        Circulo(Punto c, double r) { this.c = c; this.r = r; }
        public String toString() { return "Circulo en " + c + " con radio " + r; }
        public double area() { return Math.PI * r * r; }
        public double perimetro() { return 2 * Math.PI * r; }
    }

    public static void main(String[] args) {
        Circulo circulo = new Circulo(new Punto(7, 9), 11);
        System.out.println(circulo);
        System.out.printf("Área: %.2f\nPerímetro: %.2f\n", circulo.area(), circulo.perimetro());
    }
}
