#!/bin/bash

# flags smin, smax, r, t, seed, draw, smooth

export SIMFLAGS=""
# HELP="usage: sim.sh [pagesize] [windowsize] [algorithm] -[arguments (mlt)]\n\t-m : runs simulations over all window and page sizes.\n\t\
# -l : prints the number of pages accessed in every window to STDOUT\n\t\
# -t : gives sys time information for every run of the simulator\n "
HELP="example: sh simulator.sh -smin 0 -smax 10 -draw -smooth -t 1000000 -r 250 -seed 1234567\n\t\
-smin [int number] -> the smallest x or y speed the nodes can be given\n\t\
-smax [int number] -> the fastest x or y speed the nodes can be given\n\t\
-r [int number] -> distance the nodes must be apart for communtication to begin\n\t\
-t [int number] -> number of simulated seconds before execution finishes\n\t\
-seed [int seed val] -> seeds the random number generator\n\t\
-draw ->nothing needed will draw the simulation with opengl)\n\t\
-smooth ->nothing needed will insert null events for smooth rendering)\n\t\
\nNo arguments are required for the simulation to run. Default values from example will be used\
time(NULL) is the default seed\n"
if [ $1 = "-h" ]
then
    echo $HELP
    exit
fi;
# stackoverflow.com/questions/18003370/script-parameters-in-bash
for ((i=1;i<=$#;i++));
do

    if [ ${!i} = "-smin" ]
    then ((i++))
        export FLAGS=$FLAGS" -DRANDMIN="${!i};

    elif [ ${!i} = "-smax" ];
    then ((i++))
        export FLAGS=$FLAGS" -DRANDMAX="${!i};

    elif [ ${!i} = "-r" ];
    then ((i++))
        export FLAGS=$FLAGS" -DRADIUS="${!i};

    elif [ ${!i} = "-t" ];
    then ((i++))
        export FLAGS=$FLAGS" -DMAXTIME="${!i};

    elif [ ${!i} = "-seed" ];
    then ((i++))
        export FLAGS=$FLAGS" -DSEED="${!i};

    elif [ ${!i} = "-draw" ];
    then
        export FLAGS=$FLAGS" -Dopengl=true";

    elif [ ${!i} = "-smooth" ];
    then
        export FLAGS=$FLAGS" -Dsmooth=true";
    fi

done;
# echo $FLAGS
make
