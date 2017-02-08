import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
i = 0
while 1:
	i = ~i
	GPIO.output(24, i)
	GPIO.output(23, ~i)
	time.sleep(1)	
# print "test"
