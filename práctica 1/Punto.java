public class Punto {
    double x, y;

    Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    double[] coord_cartesianas() {
        return new double[]{x, y};
    }

    double[] coord_polares() {
        double r = Math.sqrt(x * x + y * y);
        double t = Math.toDegrees(Math.atan2(y, x));
        return new double[]{r, t};
    }

    String toStringPunto() {
        return "Punto(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p.toStringPunto());
        System.out.println("Cartesianas: [" + p.coord_cartesianas()[0] + ", " + p.coord_cartesianas()[1] + "]");
        System.out.println("Polares: [" + p.coord_polares()[0] + ", " + p.coord_polares()[1] + "]");
    }
}