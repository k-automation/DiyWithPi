# Import the rpi.gpio module. 
import RPi.GPIO as GPIO 
from time import sleep
# Set the mode of numbering the pins.
GPIO.cleanup() 
GPIO.setmode(GPIO.BCM) 
# GPIO pin 8 is the output. 
GPIO.setup(25, GPIO.OUT) 
#GPIO pin 10 is the input. 

# Initialise GPIO8 to high (true) so that the LED is off. 
GPIO.output(25, True) 
while 1:
	GPIO.output(25,False)
	sleep(3)
	GPIO.output(25,True)
	sleep(3)

