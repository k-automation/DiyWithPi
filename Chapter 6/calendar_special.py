############################################
# Raspberry PI Personal Assistant
# yamanoorsai@gmail.com
# This is an example used to set alerts based on events and appointments
############################################
import gdata.calendar.service
import gdata.service
import gdata.calendar
import time

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'yamanoorsai@gmail.com'
calendar_service.password = 'password'
calendar_service.ProgrammaticLogin()

query = gdata.calendar.service.CalendarEventQuery('default','private','full')
query.start_min = '2013-01-01'
query.start_max = '2013-06-30'

def calendar_query():
  feed = calendar_service.CalendarQuery(query)
  return feed

