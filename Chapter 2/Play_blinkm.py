#!/usr/bin/python
#python-smbus
import smbus
#create i2c object
bus = smbus.SMBus(1)
#refer to datasheet for script sequence
#Play script option is selected
bus.write_byte(0x09,0x70)
#play script no:6
bus.write_byte(0x09,0x05)
#play the script infinitely
bus.write_byte(0x09,0x00)
bus.write_byte(0x09,0x00)
