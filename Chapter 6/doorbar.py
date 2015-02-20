#!/usr/bin/env python
#  Raspberry Pi Personal assistant
#
#  Sai Yamanoor & Srihari Yamanoor
#  yamanoorsai@gmail.com
#
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.OUT)



while True:
    GPIO.output(17,GPIO.HIGH)
    if(GPIO.input(4)):
        print("High")
    else:
        print("Low")
    
