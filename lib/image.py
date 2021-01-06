import subprocess


def pngcheck(fname):
	args = ['pngcheck', '-7', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out,err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def zsteg(fname):
	args = ['zsteg', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out,err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def steghide(fname,passwd):
	passwd = passwd.split('\n')
	# return passwd
	if (fname.endswith('jpeg') or fname.endswith('bmp')) == False:
		return "steghide: File format not supported!".split('\n')
	elif(fname.endswith("jpeg") or fname.endswith("bmp") or fname.endswith("wav")):
		args = ['steghide', 'extract', '-sf', fname, '-p', passwd]
		proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False) #something happened here
		# return args
		# print("Proc aman")
		out,err = proc.communicate()
		if out:
			return out
		return err
	else:
		return "steghide: could not extract any data with that passphrase!"