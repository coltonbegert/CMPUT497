
UNAME := $(shell uname)

Default:
	gcc -Wall -std=c99 $(FLAGS) simulator.c -o sim.elf -framework GLUT -framework OpenGL -framework Cocoa
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
