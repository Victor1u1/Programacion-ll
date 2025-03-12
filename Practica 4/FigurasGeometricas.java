public class FigurasGeometricas {
    double area(double radio) { // círculo
        return Math.PI * radio * radio;
    }

    double area(double base, double altura) { // rectángulo
        return base * altura;
    }

    double area(double base, float altura) { // T. rectángulo
        return (base * altura) / 2;
    }

    double area(double a, double b, double h) { // trapecio
        return ((a + b) * h) / 2;
    }

    double area(float lado, double apotema) { // pentágono 
        return (5 * lado * apotema) / 2;
    }


    public static void main(String[] args) {
        FigurasGeometricas f = new FigurasGeometricas();

        System.out.println("Círculo: " + f.area(2.0)); 
        System.out.println("Rectángulo: " + f.area(7.0, 5.3)); 
        System.out.println("T. Rectángulo: " + f.area(3.8,7)); 
        System.out.println("Trapecio: " + f.area(4.0, 4.0, 3.0));
        System.out.println("Pentágono: " + f.area(7, 2.8)); 
    }
}
