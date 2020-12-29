from flask import Flask, render_template, request
from lib.general import *
from lib.image import *
from lib.misc import *

app = Flask(__name__)

# dummyFileName = 'temp/dummyVirus'
# dummyFileName = "temp/DummyFile.txt"
dummyFileName = 'temp/cobacoba.png'

# main pages
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/general')
def general():
	return render_template('main/general.html',
		title='Dashboard',
		exiftool=exiftool(dummyFileName),
		hashsum=hashsum(dummyFileName),
		file=file(dummyFileName),
		virustotal=virustotalCheck(dummyFileName),
		strings=strings(dummyFileName),
		binwalk=binwalk(dummyFileName),
		xxd=xxd(dummyFileName)
	)

@app.route('/image')
def image():
	return render_template('main/image.html',
		title='Image',
		pngcheck=pngcheck(dummyFileName)
	)

@app.route('/archive')
def archive():
	return render_template('main/archive.html',
		title='Archive',
	)

@app.route('/misc')
def misc():
	return render_template('main/misc.html')

# Error
@app.route('/404')
def page404():
	return render_template('errors/404.html',
		title='404'
	)

if __name__ == "__main__":
	app.run(debug=True)
