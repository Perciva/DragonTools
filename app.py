from flask import Flask, render_template, request
from tools import *

app = Flask(__name__)


dummyFileName = ''

# Index
@app.route('/')
def index():
	return render_template('index.html', title='Dashboard')
	# return render_template('index.html', title='Dashboard', exiftool=exiftool(dummyFileName), hashsum=hashsum(dummyFileName), file=file(dummyFileName), virustotal=virustotalCheck(dummyFileName))


# Form stuff
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST' and request.form['submit'] == 'Login':
		return request.form['email'] + " " + request.form['password']
	else:
		return render_template('login.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST' and request.form['submit'] == 'Register':
		return request.form['firstName'] + " " + request.form['lastName'] + " " + request.form['email'] + " " + request.form['password']+ " " + request.form['confirmPassword']
	else:
		return render_template('register.html', title='Register')

@app.route('/forgotPassword', methods=['GET', 'POST'])
def forgotPassword():
	if request.method == 'POST' and request.form['submit'] == 'forgotPassword':
		return request.form['email']
	else:
		return render_template('forgot-password.html', title='Forgot Password')

# Error
@app.route('/404')
def page404():
	return render_template('404.html', title='404')

if __name__ == "__main__":
	app.run(debug=True)
