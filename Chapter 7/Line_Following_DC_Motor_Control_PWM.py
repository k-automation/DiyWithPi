#!/usr/bin/env python
#  Raspberry Pi Line Following Robot
#
#  Sai Yamanoor & Srihari Yamanoor
#  yamanoorsai@gmail.com
#
#import of modules
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(8,GPIO.OUT) #connected to 1A
GPIO.setup(9,GPIO.OUT) #connected to 2A
GPIO.setup(10,GPIO.OUT) #connected to 3A
GPIO.setup(11,GPIO.OUT) #connected to 4A



motor1 = GPIO.PWM(10,1000)
motor2 = GPIO.PWM(9,1000)

motor1.start(10)
motor2.start(10)

while True:
	motor1.ChangeDutyCycle(25)
	motor2.ChangeDutyCycle(25)
	sleep(15)
	motor1.ChangeDutyCycle(50)
	motor2.ChangeDutyCycle(50)
	sleep(15)
	motor1.ChangeDutyCycle(75)
	motor2.ChangeDutyCycle(75)
	sleep(15)
	motor1.ChangeDutyCycle(100)
	motor2.ChangeDutyCycle(100)
	sleep(15)
	
	
	
