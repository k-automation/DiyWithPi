from time import sleep
from quick2wire.gpio import pins, Out

with pins.pin(7, direction=Out) as out_pin:
    while True:
        out_pin.value = 1 
        sleep(1)
        out_pin.value = 0
        sleep(1)
out_pin.unexport()

