#!/usr/local/bin/python
#import modules
import web
from web import form
import RPi.GPIO as GPIO
import os

#Set board
GPIO.setmode(GPIO.BCM)
#Initialize the pins that have to be controlled
GPIO.setup(25,GPIO.OUT)
GPIO.output(25,False)
#used for controlling the appliance
global state
state = False

#defining the structure
urls = ('/', 'index')
render = web.template.render('templates')


#buttons used on the webpage
appliances_form = form.Form(
    form.Button("appbtn", value="tree", class_="btntree"),
    form.Button("appbtn", value="Santa", class_="btnSanta"),
    form.Button("appbtn", value="audio", class_="btnaudio")
    )

class index:
        
	def GET(self):
                form = appliances_form()
		return render.index(form, "Raspberry Pi Christmas lights controller")
        def POST(self):
                userData = web.input()

                if userData.appbtn == "tree":
                        global state
			state = not state
                elif userData.appbtn == "Santa":
                        state = False
                elif userData.appbtn == "audio":
                        os.system("mpg321 /home/pi/test.mp3")
    
            

                GPIO.output(25,state)
                raise web.seeother('/')
if __name__ == '__main__':
        app = web.application(urls,globals())
        app.run()
