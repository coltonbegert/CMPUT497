# CMPUT 497 Assignment 1 - Simulator
Colton Begert
## Execution
To run with the default settings simply run and an example with all options used.
```bash
sh simulator.sh

sh simulator.sh -smin 0 -smax 10 -draw -smooth -t 1000000 -r 250 -seed 1234567
```
for more options and parameters use
``` bash
sh simulator.sh -h

-smin [int number] -> the smallest x or y speed the nodes can be given
-smax [int number] -> the fastest x or y speed the nodes can be given
-r [int number] -> distance the nodes must be apart for communtication to begin
-t [int number] -> number of simulated seconds before execution finishes
-seed [int seed val] -> seeds the random number generator
-draw ->nothing needed will draw the simulation with opengl)
-smooth ->nothing needed will insert null events for smooth rendering)

No arguments are required for the simulation to run. Default values from example will be used
time(NULL) is the default seed
```

## Expected issues
There will be changes needed in the make file to link the correct libraries for linux. they currently work for mac but all of the frameworks and opengl libraries are different links.

if a node leaves the boundaries or is caught with the wrong communication range state, the program immediately terminates. This was to avoid annoying bugs but removing the exit(1)'s will usually allow the program to fix itself and and continue running.

## Program Description
This program runs fairly quickly so 1-10 million simulated seconds is the default. Output is piped directly into gnuplot where a frequency histogram is created and saved as frequency.png. sometimes the program attempts to open the image before gnuplot finishes and it creates a make error but simply opening the png is fine.

The simulation is a discrete event simulator that has the ability to render the image in realtime. Messing with the area of influence radius while drawing causes the line to appear outside the circles but that is because the circles are hardcoded to be a comm distance of 250. The smooth flag creates null events to be added to the priority queue to force updates in regular intervals.

The priority queue is implemented with a sorted linked list (items are inserted in sorted order). The head is popped every loop and the event is handled. Times for updates are calculated and new events are pushed into the queue. 
