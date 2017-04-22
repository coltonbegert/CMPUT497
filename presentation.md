# 497 presentation
##nIntroduction
Sometimes develpoment can be hard so I want to show you guys the problems that i encountered and why they ended up defeating me in this project.

## SPI
We will start with spi becuase it is a really cool interface on these cards. I stands fro serial __
and is awesome becuase it has pretty decent throughput. On some of these chips it can cycle around 8mhz which allows for pretty decent transfers.

* downside of spi : single connection
* need a chip select pin to tell which device can use the bus
* bus contention causes any mess up on duty cycling to cause nothing to come out


## Duty cycling
* sharing a bus causes you to duty cycle the devices.
* turn on the sd card get data turn off sdcard. turn on camera ...
* sd card requires filesystem initialization and that takes an annoying amout of time if you need to r/w data in such low buffer chunks.


# RAM limitations
* 256kb for program and data. A 5 mp picture is ~1-3mb.
* fill the buffer 10 -30 times for each picture this requires duty cyling camera then sd card and cycle through until all the data is written.
* jpegs dont have good error correction so this is super easy to corrupt the photo.

### camera
* missing an arduino shield.
* parrallel interface
* hacking the rpi camera interface.
* individual adv for every pin on the parallel line and 200 pages

14/ 35% on sunday 42dbm
6/40 59 dbm thursday
