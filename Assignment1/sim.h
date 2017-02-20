#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
// #include <cmocka.h>
// #include <GLUT/glut.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif


#ifndef BOARDSIZE
#define BOARDSIZE 1000
#endif

#ifndef RANDMAX
#define RANDMAX 5
#endif

#ifndef RANDMIN
#define RANDMIN 0
#endif

#ifndef EDGE
#define EDGE 1
#endif

#ifndef COMM
#define COMM 3
#endif

#ifndef opengl
#define opengl false
#endif

#ifndef slow
#define slow false
#endif

#ifndef smooth
#define smooth false
#endif

#ifndef SEED
#define SEED 0
#endif

#ifndef MAXTIME
#define MAXTIME 1000000
#endif

#ifndef RADIUS
#define RADIUS 250
#endif


typedef struct node{
    double x;
    double y;
    double vx;
    double vy;
} node;

typedef struct event {
    node *point1;
    node *point2;
    double timeOfEvent;
    int type;
    int wall;
    bool valid;
    struct event *next;
    struct event *prev;
} event;

typedef struct {
    float time;
    int edge;
} edgeCol;

typedef struct {
    float time;
    int phase;
} transition;

edgeCol edgeCollision;
transition transitionPhase;

event *HEAD = NULL;
event *TAIL = NULL;

node *point1, *point2;
int quenlength = 0;
int statCounter = 0;
int counter2 =0;
int counter3 =0;
int counter4 = 0;
// current time of the simulation
double currentTime = 0;
bool inRange;
double lastTransition = 0;
double totalInRange = 0;

//Function prototypes
void test();
void ttoedge(node *p);
void bounce(node *p, int edge);
double distance(node *p1, node *p2);
void init();
void remove_event(event *event);
void insert_event(event *new_event);
bool pop_event();
void create_event(int type);
double ttotrans();
void statistics(double t);
