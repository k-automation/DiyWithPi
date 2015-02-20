import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

GPIO.output(4,GPIO.LOW)

while True:
    GPIO.output(4,GPIO.HIGH)
    sleep(1)
    GPIO.output(4,GPIO.LOW)
    sleep(1)

GPIO.cleanup()
