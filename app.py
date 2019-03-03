# coding=utf-8
# 
# The main Flask app
# 
# The "/" and "/datetime" is for testing purpose, make sure the server is
# reachable.
# 
# To measure network round trip time, use the "/echo/<requestNum>" URL, such as
# 
# http://<server_name>/echo/1
# 
from flask import Flask
from datetime import datetime
app = Flask(__name__)



@app.route('/')
def hello():
	return 'Hello, World!'



@app.route('/datetime')
def getDatetime():
	return 'Datetime is {0}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))



@app.route('/echo/<requestNum>')
def echo(requestNum):
	return 'response {0}'.format(requestNum)



if __name__ == '__main__':
	# accept incoming requests from anywhere
	app.run(host='0.0.0.0', port=80, debug=True)