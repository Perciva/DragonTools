from flask import Flask, render_template, request
from tools import *

app = Flask(__name__)

dummyFileName = 'dummyVirus'
# dummyFileName = "DummyFile.txt"

# main pages
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/general')
def general():
	return render_template('main/general.html', title='Dashboard', exiftool=exiftool(dummyFileName), hashsum=hashsum(dummyFileName), file=file(dummyFileName), virustotal=virustotalCheck(dummyFileName))

@app.route('/image')
def image():
	return render_template('main/image.html')

@app.route('/archive')
def archive():
	return render_template('main/archive.html')

@app.route('/misc')
def misc():
	return render_template('main/misc.html')

# Error
@app.route('/404')
def page404():
	return render_template('errors/404.html', title='404')

if __name__ == "__main__":
	app.run(debug=True)
