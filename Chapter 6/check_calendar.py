############################################
# Raspberry PI Personal Assistant
# yamanoorsai@gmail.com
# This is an example used to set alerts based on events and appointments
############################################

import calendar_special
import time
import datetime
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(24,gpio.OUT)

while True:
    
    feed = calendar_special.calendar_query()   # retrieve events from calendar
    for i, an_event in enumerate(feed.entry):
       
        
        for a_when in an_event.when: #We retrieve the start time and end time for each appointment/event
            try:
                start_time = datetime.datetime.strptime(a_when.start_time.split(".")[0], "%Y-%m-%dT%H:%M:%S")
                end_time = datetime.datetime.strptime(a_when.end_time.split(".")[0], "%Y-%m-%dT%H:%M:%S")
            
            except ValueError:
                print(ValueError)
                continue
            current_time = datetime.datetime.now()

            if end_time > current_time: #Has the event ended
                print '\t%s. %s' % (i, an_event.title.text,)
                print '\t\tStart time: %s' % (a_when.start_time,)
                print '\t\tEnd time:   %s' % (a_when.end_time,)
                for reminder in a_when.reminder:
                    if reminder.method == "alert" \
                       and start_time - datetime.timedelta(0,60*int(reminder.minutes))<current_time:
                        print '\t%s. %s' % (i, an_event.title.text,)
                        print '\t\tStart time: %s' % (a_when.start_time,)
                        print '\t\tEnd time:   %s' % (a_when.end_time,)
                        count = 0
                        gpio.output(24,gpio.HIGH)
                        time.sleep(1)
                        gpio.output(24,gpio.LOW)
                        time.sleep(1)
                    
