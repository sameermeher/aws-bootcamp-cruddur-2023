import uuid
import time
import random
from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from aws_xray_sdk.core import xray_recorder

tracer = trace.get_tracer("create.activity")

class CreateActivity:
  def run(message, user_handle, ttl):
    with tracer.start_as_current_span("create-activity"):
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      # Adding a extra attributes to current span
      span = trace.get_current_span()
      span.set_attribute("app.now", now.isoformat())

      if (ttl == '30-days'):
        ttl_offset = timedelta(days=30) 
      elif (ttl == '7-days'):
        ttl_offset = timedelta(days=7) 
      elif (ttl == '3-days'):
        ttl_offset = timedelta(days=3) 
      elif (ttl == '1-day'):
        ttl_offset = timedelta(days=1) 
      elif (ttl == '12-hours'):
        ttl_offset = timedelta(hours=12) 
      elif (ttl == '3-hours'):
        ttl_offset = timedelta(hours=3) 
      elif (ttl == '1-hour'):
        ttl_offset = timedelta(hours=1) 
      else:
        model['errors'] = ['ttl_blank']

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['user_handle_blank']

      if message == None or len(message) < 1:
        model['errors'] = ['message_blank'] 
      elif len(message) > 280:
        model['errors'] = ['message_exceed_max_chars']

      if model['errors']:
        model['data'] = {
          'handle':  user_handle,
          'message': message
        }   
      else:
        # Start Subsegment
        subsegment = xray_recorder.begin_subsegment("Create Activity")

        # Generate a random sleep time between 50 and 500 milliseconds to replicate delay scenario
        sleep_time = random.randint(50, 500) / 1000
        time.sleep(sleep_time)
        model['data'] = {
          'uuid': uuid.uuid4(),
          'display_name': 'Andrew Brown',
          'handle':  user_handle,
          'message': message,
          'created_at': now.isoformat(),
          'expires_at': (now + ttl_offset).isoformat()
        }

      span.set_attribute("app.user_handle", user_handle)
      
      # Capture details into Subsegment
      subsegment.put_metadata("metadata",{"created_by": user_handle, "display_name": 'Andrew Brown'}, "activity_attributes")
      subsegment.put_annotation("user_handle", user_handle)
      # Close Subsegment
      xray_recorder.end_subsegment()

      return model