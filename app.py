from datetime import datetime
import pytz
from flask import request , Flask

app1 = Flask(__name__)

# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_NY)
# print("NY time:", datetime_NY.strftime("%H:%M:%S"))
#
# tz_London = pytz.timezone('Europe/London')
# datetime_London = datetime.now(tz_London)
# print("London time:", datetime_London.strftime("%H:%M:%S"))
#
tz_Telaviv = pytz.timezone('Asia/Jerusalem')
datetime_Telaviv = datetime.now(tz_Telaviv)
print("Tel-Aviv time:", datetime_Telaviv.strftime("%H:%M:%S"))

@app1.route('/')
def citiesTimeZones():
    return "Tel-Aviv time:" + datetime_Telaviv.strftime("%H:%M:%S")

if __name__=='__main__':
    app1.run(debug=True,host='0.0.0.0',port=6500)

