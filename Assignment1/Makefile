
UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
	OPENGLFLAGS = -framework GLUT -framework OpenGL -framework Cocoa
else
	OPENGLFLAGS = -lGL -lGLU -lm -lglut
endif

Default:
	gcc -Wall -std=c99 $(FLAGS) simulator.c -o sim.elf $(OPENGLFLAGS)
	./sim.elf
ifeq ($(UNAME), Darwin)
	open frequency.png
else
	xdg-open frequency.png
endif

d:
	gcc -ggdb -Wall -std=c99 motivatingExample.c -o ex -lGL -lGLU -lglut -lX11

clean:
	rm *.elf
