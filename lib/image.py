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
	# if passwd == "":
	# 	passwd = " "
	#selain jpeg bmp langsung show error msg (?)
	if (fname.endswith('jpeg') or fname.endswith('bmp')) == 0:
		return "steghide: could not extract any data with that passphrase!".split('\n')
	else:
		args = ['steghide', 'extract', '-sf', fname, '-p', passwd]
		proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
		out,err = proc.communicate()
		if out:
			return out
		return err
