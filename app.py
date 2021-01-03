from flask import Flask, render_template, request, session, send_from_directory
from lib.general import *
from lib.image import *
from lib.misc import *
from werkzeug.utils import secure_filename
import os

# configs can be moved to a safer location on production
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
# 16mb max file upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = b'ay whos joe? joe mama OOOHHHHHHH123124387dsfs098783()*&*)@$^8s'

ALLOWED_EXTENSIONS = {
		'txt', 'pdf',
		'png', 'jpg', 'jpeg', 'gif',
		'pcap', 'pcapng',
		'zip', 'rar'
	}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# main pages
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		if file and file.filename != '' and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			# replace old session
			session['userfile'] = filename
	return render_template('index.html')

@app.route('/general')
def general():
	try:
		filename = "uploads/"+session['userfile']
		return render_template('main/general.html',
			title='Dashboard',
			exiftool=exiftool(filename),
			hashsum=hashsum(filename),
			file=file(filename),
			virustotal=virustotalCheck(filename),
			strings=strings(filename),
			binwalk=binwalk(filename),
			xxd=xxd(filename)
		)
	except:
		return render_template('main/general.html')

@app.route('/image')
def image():
	try:
		filename = "uploads/"+session['userfile']
		return render_template('main/image.html',
			title='Image',
			pngcheck=pngcheck(filename)
		)
	except:
		return render_template('main/image.html')

@app.route('/misc')
def misc():
	try:
		filename = "uploads/"+session['userfile']
		return render_template('main/misc.html')
	except:
		return render_template('main/misc.html')

# Error
@app.route('/404')
def page404():
	return render_template('errors/404.html',
		title='404'
	)

# uploads
@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
	app.run(debug=True)
