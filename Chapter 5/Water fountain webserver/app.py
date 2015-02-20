#! /usr/bin/python

##############################################
#
#
#
# Raspberry Pi enabled Water fountain example
#
#
#
#
##############################################
from __future__ import with_statement
import json
import Queue
import argparse
from LPD8806 import *
import pyaudio
import audioop
import sys
import math
#LPD8806 Initialization
num = 64;
led = LEDStrip(num)

from logging.handlers import RotatingFileHandler
from random import randint
from threading import Thread
from datetime import datetime, timedelta
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, jsonify
from sys import exit


#Flask framework
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True # !!! Set this to False for production use !!!
#RGB values
rgb_array = [0,0,0]
HEX = '0123456789abcdef'
HEX2 = dict((a+b, HEX.index(a)*16 + HEX.index(b)) for a in HEX for b in HEX)

#HEX 2 RGB       
def rgb(triplet):
    triplet = triplet.lower()
    rgb_array[0] = HEX2[triplet[0:2]]
    rgb_array[1] = HEX2[triplet[2:4]]
    rgb_array[2] = HEX2[triplet[4:6]]
    return  (HEX2[triplet[0:2]],HEX2[triplet[2:4]],HEX2[triplet[4:6]])

def triplet(rgb):
    return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/set/<hex_val>', methods=['GET', 'POST'])
def send_command(hex_val):

    return_object = {'output' : None , 'error' : None, 'success' : False}
    rgb_val = rgb(hex_val)
    led.fill(Color(rgb_val[0],rgb_val[1],rgb_val[2],0.98))
    led.update()
    app.logger.debug("Given colour_val : %s, converted it to %s" % (hex_val, rgb_val))

    return_object['success'] = True
    return jsonify(return_object)

if __name__ == "__main__":
     try:
        app.run('0.0.0.0')
     except KeyboardInterrupt:
        exit(0)
    
