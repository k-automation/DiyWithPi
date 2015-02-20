# An example to turn on appliances between select times of the day
#
#
import RPi.GPIO as GPIO
import datetime
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

def main():
    while True:
        #Get current time
        now = datetime.datetime.now()
        #Create datetime objects
        startTime = datetime.datetime(now.year,now.month,now.day,12,55,0)
        endTime = datetime.datetime(now.year, now.month,now.day,13,05,0)
        #Create unix time stamps
        unixStart = (startTime - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
        unixEnd = (endTime - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
        unixNow = (now - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
        #let's wait until it is time to turn on the lights
        if ( unixStart <= unixNow <= unixEnd):
            GPIO.output(25,GPIO.HIGH)
            while ( unixStart <= unixNow <= unixEnd):
                now = datetime.datetime.now()
                unixNow = (now - datetime.datetime(1970,1,1,0,0,0)).total_seconds()
                #print "Triggered", now.hour,":",now.minute,":",now.second
                sleep(1)
            GPIO.output(25,GPIO.LOW)
        
    GPIO.cleanup()



if __name__ == '__main__':
    main()
