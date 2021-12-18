from flask import render_template , Flask
import os

app1 = Flask(__name__)

@app1.route('/')
def citiesTimeZones():
    return render_template("index.html")

if __name__=='__main__':
    app1.run(debug=True,host='0.0.0.0',port=int(os.environ['port']))

