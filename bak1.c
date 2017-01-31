#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#ifndef SIZE
#define SIZE 1000
#endif

#ifndef RANDMAX
#define RANDMAX 5
#endif


typedef struct{
    double x;
    double y;
    double vx;
    double vy;
} node;

//Function prototypes
void test();
float ttoedge(node *p);
void bounce(node *p);
double distance(node *p1, node *p2);

int main(int argc, char const *argv[]) {
    srand(0);

    test();

    return 0;
}

void test() {
    node *point;
    point = malloc(sizeof(node));

    point->x = 200;
    point->y = 0;
    point->vx = 200;
    point->vy = 1;
    printf("%f\n", ttoedge(point));

}

float ttoedge(node *p) {
    double minTime = 1.0/0.0; // positive infinity
    double newTime;
    printf("%f\n", minTime);
    if (p->vx < 0) {
        newTime = p->x / p->vx;
        printf("1: %f\n", newTime);
        if (newTime < minTime) {
            minTime = newTime;
            printf("vx < 0: %f\n", minTime);
        }
    } else {
        newTime = (SIZE - p->x) / p->vx;
        printf("2: %f\n", newTime);
        if (newTime < minTime) {
            minTime = newTime;
            printf("vx >= 0: %f\n", minTime);
        }
    }
    if (p->vy < 0) {
        newTime = (p->y / p->vy);
        printf("3: %f\n", newTime);
        if (newTime < minTime) {
             minTime = newTime;
             printf("vy < 0: %f\n", minTime);
        }
    } else {
        newTime = (SIZE - p->y) / p->vy;
        printf("4: %f\n", newTime);
        if (newTime < minTime) {
            minTime = newTime;
            printf("vy >= 0: %f\n", minTime);
        }
    }
    return minTime;
}

// gives a node a random velocity vector upon wall collision
void bounce(node *p) {
    if(p->x <= 0) {
        p->vx = rand() % RANDMAX;
        p->vy = RANDMAX - (2*(rand()%RANDMAX));
    }
    if (p->x >= SIZE) {
        p->vx = -rand() % RANDMAX;
        p->vy = RANDMAX - (2*(rand()%RANDMAX));
    }
    if(p->y <= 0) {
        p->vx = RANDMAX - (2*(rand()%RANDMAX));
        p->vy = rand() % RANDMAX;
    }
    if (p->y >= SIZE) {
        p->vx = RANDMAX - (2*(rand()%RANDMAX));
        p->vy = -rand() % RANDMAX;
    }
}

// Returns the euclidea distance between two nodes
double distance(node *p1, node *p2) {
    return sqrt(pow((p1->x-p2->x), 2) + pow((p1->y - p2->y), 2));
}
