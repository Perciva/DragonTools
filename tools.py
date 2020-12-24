import subprocess
import hashlib
import requests
from bs4 import BeautifulSoup as bs
import json

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
		return out.decode('utf-8')
	return err.decode('utf-8')

def strings(fname):
	args = ['strings', fname, '| tail']
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8')
	return err.decode('utf-8')

def virustotalCheck(fname):
	sha256sum = sha256(fname)
	# url = 'https://www.virustotal.com/vtapi/v2/file/report'
	# params = {'apikey': '6201732de559c1e9c089e897ce858f0df21efb98f417e51c5ec6a08031abcf6e', 'resource': sha256sum}
	# response = requests.get(url, params=params)
	with open("sample.json") as f:
		response = f.read()
	print(type(response))
	print(type(json.loads(response)))
	return json.loads(response)
	# return response.items()
	# return str(response.json()['positives']) + ' Positives, out of : ' + str(response.json()['total']) + ' Total<br><a href="' + str(response.json()['permalink'])+ '">Check It out here</a>'
	# return response.json()
	# return response.json()
	# print(response.json()['scans']['Bkav'])
	# found = []
	# for result in response.json()['scans']:
	# 	return result
	# 	if result['detected'] == True:
	# 		found.append(result)
	# return found
