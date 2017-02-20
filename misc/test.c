#include <stdio.h>
#include <math.h>

typedef struct {
    double x;
    double y;
    double vx;
    double vy;
} node;
node node1, node2;

double timeToTransition(node n1, node n2) {
    double A, B, C, m, b, r, x, y, vx, vy, d, X, t;
    x = n2.x - n1.x;
    y = n2.y - n1.y;
    vx = n2.vx - n1.vx;
    vy = n2.vy - n1.vy;
    m = vy / vx;
    b = y - (m * x);
    r = 3;
    A = 1 + (m * m);
    B = 2 * m * b;
    C = (b * b) - (r * r);
    d = (B * B) - (4 * A * C);
    // printf("y = %fx + %f\n", m, b);
    // printf("d:%f\n", d);
    if (d < 0.001 && d > -0.001) {
        // printf("yahooo\n");
    }
    if (d < 0) return -1;
    X = (-B + sqrt(d)) / (2 * A);
    // if (X > 0) return X;
    // printf("A:%f, B: %f, C:%f, %f\n", A,B,C,d);
    // return X;
    t = (X - x) / vx;
    if (t > 0) {
        return t;
    }
    X =(-B - sqrt(d)) / (2 * A);
    t = (X - x) / vx;
    if (t > 0) {
        return t;
    }

    return -1;
}

int main(int argc, char const *argv[]) {
    node1.x = node1.y = node1.vx = node1.vy = 0;

    node2.x = 2.1213203436;
    node2.y = -2.1213203436;
    node2.vx = -1;
    node2.vy = -1;

    int counter = 100000000;
    while (counter --) {
        timeToTransition(node1, node2);
    }
    printf("Time: %f\n", timeToTransition(node1, node2));
    return 0;
}
