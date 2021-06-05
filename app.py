
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def moscowtime():
  tz_NY = pytz.timezone('Europe/Moscow')
  datetime_NY = datetime.now(tz_NY)
  return 'Hello World ! Time is : {}'.format(datetime_NY.strftime("%H:%M:%S"))
  

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
