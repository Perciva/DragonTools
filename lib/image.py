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
	args = ['steghide', 'extract', '-sf', fname, '-p', passwd]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out,err = proc.communicate()
	# args2 = ['y']
	# proc = subprocess.Popen(args2, stdout=subprocess.PIPE, shell=False)
	# out2,err2 = proc.communicate()
	if out == "steghide: could not extract any data with that passphrase!":
		return "Test"
	return err2
