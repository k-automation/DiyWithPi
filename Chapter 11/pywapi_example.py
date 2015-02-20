#pywapi example
#A lawn sprinkler is turned on only if there is no rain forecast
#for the date
import pprint
import pywapi
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

def main():
    pp = pprint.PrettyPrinter(indent=4)

    while True:
        result = pywapi.get_weather_from_noaa('KORD')
        pp.pprint(result['weather'])
        

        if (result['weather'] != 'Light Rain' or
            result['weather'] != 'Rain' or
            result['weather'] != 'Thunderstorm'):
                GPIO.output(25,GPIO.HIGH)
        sleep(10)
        GPIO.output(25,GPIO.LOW)
        sleep(2)
        
if __name__ == '__main__':
    main()
