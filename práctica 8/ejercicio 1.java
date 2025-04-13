class A {
    int x, z;

    A(int x, int z) {
        this.x = x;
        this.z = z;
    }

    void incrementaXZ() {
        x++;
        z++;
    }

    void incrementaZ() {
        z++;
    }
}

class B {
    int y;
    A a;

    B(int y, A a) {
        this.y = y;
        this.a = a;
    }

    void incrementaYZ() {
        y++;
        a.z++;
    }

    void incrementaZ() {
        a.z++;
    }
}

class D extends A {
    B b;

    D(int x, int y, int z) {
        super(x, z);
        b = new B(y, this);
    }

    void incrementaXYZ() {
        x++;
        b.y++;
        z++;
    }

    void mostrar() {
        System.out.println(x + " " + b.y + " " + z);
    }
}

public class Main {
    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        d.incrementaXYZ();
        d.mostrar();  
    }
}