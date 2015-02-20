#!/usr/bin/env python 
#Weasley weather clock example
import serial
import glob
import pprint
import pywapi
from time import sleep

def scan():
    return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')+ glob.glob('/dev/ttyACM*')

pp = pprint.PrettyPrinter(indent=4)

sport_data = scan()

for name in scan():
    serialport = serial.Serial(name,9600)
    sleep(5)
    serialport.write(bytes("A",'ascii'))
    sleep(1)
    response = serialport.read()
    if(response==b'A'):
        sport = name
        serialport.close()
        break


seport = serial.Serial(name,9600,timeout=45)
result = pywapi.get_weather_from_noaa('KORD')
pp.pprint(result)
    
temperature = int(float(result['temp_f']))
wndspeed    = int(float(result['wind_mph']))
    
#print(temperature)
print(wndspeed)
    
temperature_string= "S"+str(temperature)
#print(temperature_string)
seport.write(bytes(temperature_string,'ascii'))

sleep(5)

if(temperature>40):
    seport.write(bytes("G",'ascii'))
    sleep(5)
    seport.write(bytes("P4",'ascii'))
    sleep(5)
    seport.write(bytes("M1",'ascii'))
    sleep(5)
    seport.write(bytes("T-3",'ascii'))
    sleep(5)

if(temperature<40) and (wndspeed<30):
    seport.write(bytes("B",'ascii'))
    sleep(5)
    seport.write(bytes("M1",'ascii'))
    sleep(5)
    seport.write(bytes("P5",'ascii'))
    sleep(5)


if(temperature<40) and (wndspeed>30):
    seport.write(bytes("R",'ascii'))
    sleep(5)
    seport.write(bytes("M2",'ascii'))
    sleep(5)
    seport.write(bytes("P3",'ascii'))
    sleep(5)
    seport.write(bytes("T-1",'ascii'))
    sleep(5)
    
if(result['weather']=='Overcast'):
    seport.write(bytes("H",'ascii'))
    sleep(5)
    seport.write(bytes("T-4",'ascii'))
    sleep(5)

if(result['weather']=='Light Snow') or (result['weather']=='Snow') or (result['weather']=='Flurries'):
    seport.write(bytes("H",'ascii'))
    sleep(5)
    seport.write(bytes("T-2",'ascii'))
    sleep(5)

if(result['weather']=='Thunderstorm'):
    seport.write(bytes("H",'ascii'))
    sleep(5)
    seport.write(bytes("T-5",'ascii'))
    sleep(5)
    seport.write(bytes("R",'ascii'))
    sleep(5)
    seport.write(bytes("P3",'ascii'))
    sleep(5)

if(result['weather']=='Rain') or (result['weather']=='Light Rain'):
    seport.write(bytes("H",'ascii'))
    sleep(5)
    seport.write(bytes("T-2",'ascii'))
    sleep(5)
    seport.write(bytes("M1",'ascii'))
    sleep(5)
    
    
       

    

#serialport.close()
    
                     
