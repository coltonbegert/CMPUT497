Default:
	gcc -Wall -std=c99 motivatingExample.c -o ex -framework GLUT -framework OpenGL -framework Cocoa
	./ex

d:
	gcc -ggdb -Wall -std=c99 motivatingExample.c -o ex -lGL -lGLU -lglut -lX11
