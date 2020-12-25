import subprocess
import hashlib
import requests
import json
from bs4 import BeautifulSoup as bs

def exiftool(fname):
	args = ['exiftool', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def sha1(fname):
	hash_sha1 = hashlib.sha1()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_sha1.update(chunk)
	return hash_sha1.hexdigest()

def sha256(fname):
	hash_sha256 = hashlib.sha256()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_sha256.update(chunk)
	return hash_sha256.hexdigest()

def hashsum(fname):
	return [['md5',md5(fname)], ['sha1',sha1(fname)], ['sha256',sha256(fname)]]

def file(fname):
	args = ['file', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8')
	return err.decode('utf-8')

def binwalk(fname):
	args = ['binwalk', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def strings(fname):
	args = ['strings', fname, '| tail']
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def pngcheck(fname):
	args = ['pngcheck', '-7', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out,err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def virustotalCheck(fname):
	# sha256sum = sha256(fname)
	# url = 'https://www.virustotal.com/vtapi/v2/file/report'
	# params = {'apikey': '6201732de559c1e9c089e897ce858f0df21efb98f417e51c5ec6a08031abcf6e', 'resource': sha256sum}
	# response = requests.get(url, params=params)
	with open('temp/sample.txt', 'r') as f:
		response = f.readline()
	# convert json str to array
	response = json.loads(response)
	scans = response.get("scans")
	hits = []
	for key, val in scans.items():
		result = scans.get(key)
		if result.get("detected") == True:
			hits.append({key: val})
	return hits
