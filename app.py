# coding=utf-8
# 
# The main Flask app
# 
from flask import Flask
from datetime import datetime
app = Flask(__name__)



@app.route('/')
def hello_world():
	return 'Hello, World @ {0}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)