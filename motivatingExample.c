#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
// #include <cmocka.h>

#ifndef BOARDSIZE
#define BOARDSIZE 1000
#endif

#ifndef RANDMAX
#define RANDMAX 5
#endif

#ifndef EDGE
#define EDGE 1
#endif

#ifndef COMM
#define COMM 3
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
    bool valid;
    struct event *next;
    struct event *prev;
} event;

event *HEAD = NULL;
event *TAIL = NULL;

node *point1, *point2;
int quenlength = 0;
// current time of the simulation
double currentTime = 0;
bool inRange;
double lastTransition = 0;
double totalInRange = 0;

//Function prototypes
void test();
float ttoedge(node *p);
void bounce(node *p);
double distance(node *p1, node *p2);
void init();
void remove_event(event *event);
void insert_event(event *new_event);
bool pop_event();
void create_event(int type);
double ttotrans();

int main(int argc, char const *argv[]) {
    srand(0);
    init();
    int counter = 0;
    // simulation will run for 1000 events
    while (counter++ < 10) {
        printf("%d\n", counter);
        if (!pop_event()) {
            // no more events
            printf("Ran out after %d events\n", counter);
            break;
        }
    }
    printf("%f\n", 100*totalInRange/currentTime);

    // node pointArray[2];

    // test();

    return 0;
}

void test() {
    node *point;
    point = malloc(sizeof(node));

    point->x = 200;
    point->y = 0;
    point->vx = 200;
    point->vy = 300;
    printf("%f\n", ttoedge(point));

}
double randr(int a) {return (double)(((double)rand()/(double)RAND_MAX) * (double)a);}

void init() {
    point1 = malloc(sizeof(node));
    point2 = malloc(sizeof(node));
    // ((rand()%2) ? -1 : 1) * randr(RANDMAX);

    point1->x = randr(BOARDSIZE);
    point1->y = randr(BOARDSIZE);
    point1->vx = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
    point1->vy = ((rand()%2) ? -1 : 1) * randr(RANDMAX);

    point2->x = randr(BOARDSIZE);
    point2->y = randr(BOARDSIZE);
    point2->vx = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
    point2->vy = ((rand()%2) ? -1 : 1) * randr(RANDMAX);

    printf("init:: x1: %f, y1: %f, x2: %f, y2: %f,",point1->x, point1->y,  point2->x,  point2->y);
    printf("vx1: %f, vy1: %f, vx2: %f, vy2: %f\n",point1->vx, point1->vy,  point2->vx,  point2->vy);

    if (distance(point1, point2) < 250) {
        inRange = true;
    }

    create_event(1);
    create_event(2);

}

float ttoedge(node *p) {
    double minTime = 1.0/0.0; // positive infinity
    double newTime;

    if (p->vx < 0) {
        newTime = (p->x / -p->vx);
        if (newTime < minTime && newTime >=0) {
            minTime = newTime;
        }
        // printf("1, %f\n", newTime);
    } else {
        newTime = (BOARDSIZE- p->x) / p->vx;
        if (newTime < minTime) {
            minTime = newTime;
        }
        // printf("2, %f\n", newTime);
    }

    if (p->vy < 0) {
        newTime = p->y / -p->vy;
        if (newTime < minTime) {
            minTime = newTime;
        }
        // printf("3, %f\n", newTime);
    } else {
        newTime = (BOARDSIZE - p->y) / p->vy;
        if (newTime < minTime) {
            minTime = newTime;
        }
        // printf("4, %f\n", newTime);
    }
    return minTime;
}

// gives a node a random velocity vector upon wall collision
void bounce(node *p) {
    // printf("AHHHHHHHHH\n");
    bool changed = false;
    if(p->x <= 0.01) {
        p->vx = randr(RANDMAX);
        p->vy = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
        changed = true;
    }
    if (p->x >= BOARDSIZE-0.01) {
        p->vx = -randr(RANDMAX);
        p->vy = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
        changed = true;
    }
    if(p->y <= 0.01) {
        p->vx = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
        p->vy = randr(RANDMAX);
        changed = true;
    }
    if (p->y >= BOARDSIZE-0.01) {
        p->vx = ((rand()%2) ? -1 : 1) * randr(RANDMAX);
        p->vy = -randr(RANDMAX);
        changed = true;
    }
    if (changed) return;
    printf("fperror\n");
}

// Returns the euclidea distance between two nodes
double distance(node *p1, node *p2) {
    return sqrt(pow((p1->x-p2->x), 2) + pow((p1->y - p2->y), 2));
}

void update() {
    // printf("update:: x1: %f, x2: %f, y1: %f, y2: %f\n",point1->x, point1->y,  point2->x,  point2->y);
    double elapsedTime = HEAD->timeOfEvent - currentTime;
    point1->x += elapsedTime*point1->vx;
    point1->y += elapsedTime*point2->vy;
    point2->x += elapsedTime*point2->vx;
    point2->y += elapsedTime*point2->vy;
    printf("update:: x1: %f, y1: %f, x2: %f, y2: %f\n",point1->x, point1->y,  point2->x,  point2->y);
}
// Remove and Item from the queue and handle it

void print_queue() {
    printf("QUEUE::");
    for (event *e = HEAD;e !=NULL ; e = e->next) {
        printf(" %fs,", e->timeOfEvent);
    }
    printf("end\n");
}
bool pop_event() {
    // printf("QUEUE LENGTH%d\n", quenlength);
    print_queue();
    // no evnet to pop
    if (HEAD == NULL) return false;
    update();
    currentTime = HEAD->timeOfEvent;
    // printf("time: %f\n", currentTime);

    int eventType = HEAD->type;
    printf("et:%d\n", eventType);
    if (eventType == 1) {
        bounce(point1);
        // remove_event(HEAD);
        // create_event(1);
    } else if (eventType == 2) {
        bounce(point2);
        // remove_event(HEAD);
        // create_event(2);

    } else if (eventType == 3) {
        // this is where we can determine if it is entering or exiting the area
        if (inRange) {
            // printf("hello\n");
            totalInRange += currentTime - lastTransition;
        }
        //     lastTransition = currentTime;
        // } else {
        // }
        lastTransition = currentTime;
        inRange = !inRange;


        //after handling the event

    }

    remove_event(HEAD);
    create_event(eventType);

    // remove_event(HEAD);
    return true;
}

// create a new event to handle a state
void create_event(int type) {
    if (type == 1) {
        event *new_event = malloc(sizeof(event));
        // new_event->point1
        new_event->type = 1;
        new_event->valid = true;
        printf("ttoedge1: %f\n", ttoedge(point1));
        new_event->timeOfEvent = currentTime + ttoedge(point1);
        insert_event(new_event);
        // return;
    } else if (type == 2) {
        event *new_event = malloc(sizeof(event));
        new_event->type = 2;
        new_event->valid = true;
        printf("ttoedge2: %f, vx = %f, vy = %f\n", ttoedge(point2), point2->vx, point2->vy);
        new_event->timeOfEvent = currentTime + ttoedge(point2);
        insert_event(new_event);
        // return;
    }

        // this is the type of entering or exiting area of influence.
        // for loop to determine if anything happens before a bounce
        // printf("hi\n");
    double timeToTransition = ttotrans();
    // printf("hello\n");
    if (timeToTransition == -1) {
        return;
    } else {
        if (HEAD->timeOfEvent > timeToTransition) {
            event *new_event = malloc(sizeof(event));
            new_event->type = 3;
            new_event->valid = true;
            new_event->timeOfEvent = currentTime + timeToTransition;
            insert_event(new_event);
        }

    }
}

double ttotrans() {
    // printf("here ttotrans\n");
    double vxt = point1->vx - point2->vx;
    double vyt = point1->vy - point2->vy;

    double tcpa = (vxt*point1->x - vxt*point2->x + vyt*point1->y - vyt*point2->y)/(vxt*point1->vx - vxt*point2->vx + vyt*point1->vy - vyt*point2->vy);

    if (isnan(tcpa)) {
        /* code */
        // printf("hello\n");
        return -1;
    }
    // double curDist = distance(point1, point2);
    // printf("current Distance: %f\n", curDist);
    // if (curDist < 250) {
    //     //calc time to exit
    // }

    double root = sqrt(pow(point1->x + point1->vx*tcpa + point2->x + point2->vx*tcpa,2) + pow(point1->y + point1->vy*tcpa + point2->y + point2->vy*tcpa,2));
    // printf("init:: x1: %f, y1: %f, x2: %f, y2: %f,",point1->x, point1->y,  point2->x,  point2->y);
    // printf("vx1: %f, vy1: %f, vx2: %f, vy2: %f\n",point1->vx, point1->vy,  point2->vx,  point2->vy);
    // printf("vx1: %f, vx2: %f, vy1: %f, vy2: %f\n",point1->vx, point1->vy,  point2->vx,  point2->vy);
    if (isnan(root)) return -1;
    // if ()
    if (inRange) {
        return 250 + root;
    } else {
        if (root > 250) {
            return -1;
        } else {
            return 250 - root;
        }
    }
}

    // if < curtime ret -val else ret +val
//     void insert_event(event *new_event) {
//
//         // event *new_event = malloc(sizeof(event));
//         printf("next event at %f\n", new_event->timeOfEvent);
//         if (HEAD == NULL)  {
//             printf("head null\n");
//             new_event->prev = NULL;
//             new_event->next = NULL;
//             HEAD = new_event;
//             TAIL = HEAD;
//             quenlength++;
//             if (HEAD == NULL) printf("head should not be null\n");
//         } else {
//             // INSERT ITEMS INTO THE QUEUE IN A SORTED ORDER
//             int depth = 0;
//             bool changed = false;
//             for (event *current = HEAD; current != NULL; current = current->next) {
//                 printf("current time:%f,new time:%f\n", current->timeOfEvent, new_event->timeOfEvent);
//                 depth++;
//                 if (new_event->timeOfEvent < current->timeOfEvent) {
//                     changed = true;
//                     new_event->prev = current->prev;
//                     new_event->next = current;
//                     current->prev = new_event;
//                     quenlength++;
//                 }
//             }
//             if (!changed) {
//                 new_event->prev = TAIL;
//                 new_event->next = NULL;
//                 // ->prev = new_event;
//                 TAIL = new_event;
//                 quenlength++;
//             }
//             printf("depth: %d\n", depth);
//         }
//     }
// }

void insert_event(event *e) {

    double it = 0;
    int i = 0;
    if (HEAD == NULL) {
        HEAD = e;
        HEAD->next = NULL;
        it = 0;
    } else if (e->timeOfEvent < HEAD->timeOfEvent){
        it = HEAD->timeOfEvent;
        e->next = HEAD;
        HEAD = e;
    } else {
        for (event *current = HEAD; ; current = current->next) {
            i++;
            if (current->next == NULL) {
                current->next = e;
                e->next = NULL;
                break;
            } else {
                if (e->timeOfEvent < current->next->timeOfEvent) {
                    it = current->next->timeOfEvent;
                    e->next = current->next;
                    current->next = e;
                    break;
                }
            }
        }
    }
    // printf("insert_event at depth %d. This %f < %f!\n", i, e->timeOfEvent, it);
}

void remove_event(event *e) {
    if (e == HEAD) {
        // HEAD == NULL;
        HEAD = HEAD->next;
    } else {
        for (event *current = HEAD; ; current = current->next) {
            if (current->next == e) {
                current->next = current->next->next;
            }
        }
    }
    free(e);
}

// remove an event from the queue
// void remove_event(event *event) {
//     // if (HEAD == NULL) printf("1head should not be null\n");
//     printf("REMOVING VALUE\n");
//     quenlength--;
//
//     // if (e == HEAD) {
//     //     HEAD = e->next;
//     // }
//     // if (e->prev == NULL) {
//     //     TAIL = e->prev;
//     // }
//
//
//     // /* base case */
//     //   if(HEAD == NULL || e == NULL)
//     //     return;
//     //
//     //   /* If node to be deleted is head node */
//     //   if(HEAD == e) {
//     //       printf("should do this\n");
//     //       HEAD = e->next;
//     //       if (HEAD == NULL) printf("3head should not be null\n");
//     //   }
//     //
//     //   /* Change next only if node to be deleted is NOT the last node */
//     //   if(e->next != NULL) e->next->prev = e->prev;
//     //
//     //   /* Change prev only if node to be deleted is NOT the first node */
//     //   if(e->prev != NULL) e->prev->next = e->next;
//     //
//     //   /* Finally, free the memory occupied by del*/
//     //   free(e);
//     //   return;
//   // }
// //     e->prev->next = e->next;
// //     e->next->prev = e->prev;
// //
// //
// //
// //
// //
//     if (event->prev == NULL) {
//         HEAD = event->next;
//         // event->next->prev = NULL;
//     } else {
//         event->prev->next = event->next;
//     }
//     if (event->next == NULL) {
//         TAIL = event->prev;
//         // event->prev->next = NULL;
//     } else {
//         event->next->prev = event->prev;
//     }
//     if (HEAD == NULL) printf("2head should not be null\n");
//     free(event);
// }
// // remove item from list of active users
// void remove_user(char *name, uint8_t name_len){
//     for (user_t *user = head; user != NULL; user = user->next) {
//         if (user->name_len == name_len) {
//             int different = 0;
//             for (int i = 0; i< name_len; i++) {
//                 if (name[i] != user->name[i]) {
//                     different = 1;
//                 }
//             }
//             // if the correct name is found it is deleted
//             // linked list deletion
//             if (!different) {
//                 if (user->prev == NULL) {
//                     head = user->next;
//                     // user->next->prev = NULL;
//                 } else {
//                     user->prev->next = user->next;
//                 }
//                 if (user->next == NULL) {
//                     tail = user->prev;
//                 } else {
//                     user->next->prev = user->prev;
//                 }
//                 // free both name and struct
//                 free(user->name);
//                 free(user);
//             }
//         }
//     }
// }