# Web App to run flask framework
# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import csv
from datetime import datetime
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

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
    bloodPressure=request.form['BloodPressure']
    SpO2=request.form['SpO2']
    pulse=request.form['pulse']
    #before writing to a csv file, log time stamps
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    logfile = open('static\\comments.csv', 'a')
    logfile.write(",".join([date,time,bloodPressure, SpO2, pulse,'\n']))
    logfile.close()

    return render_template('form_action.html',date=date,time=time,
                           bloodPressure=bloodPressure,
                           SpO2=SpO2,pulse=pulse)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )
