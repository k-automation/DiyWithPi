# Web App to run flask framework
# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import csv
import RPi.GPIO as GPIO
from datetime import datetime
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

state = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form,
# We are also defining which type of requests this route is 
# accepting: POST requests in this case

@app.route('/', methods=['POST'])
def record():
    #record all the data from the form
    global state
    if state == False:
        state = True
    else:
        state = False
    GPIO.output(25,state)
    return render_template('form_submit.html')


# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("75")
  )

GPIO.cleanup()
