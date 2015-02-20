#!/usr/bin/env python
#  Raspberry Pi Personal assistant
#
#  Sai Yamanoor & Srihari Yamanoor
#  yamanoorsai@gmail.com
#
import parser
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)

while True:
    mail = parsery.mail()
    count = 0
    if mail>0:
        print(mail)
        print("new emails \n")
        while count<10:
            count += 1
            gpio.output(17,gpio.HIGH)
            time.sleep(1)
            gpio.output(17,gpio.LOW)
            time.sleep(1)
        gpio.output(17,gpio.LOW)
    else:
        time.sleep(10)     
    


