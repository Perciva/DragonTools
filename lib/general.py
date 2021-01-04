import subprocess
import requests
import json
from .tools import *

def file(fname):
	args = ['file', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8')
	return err.decode('utf-8')

def exiftool(fname):
	args = ['exiftool', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def binwalk(fname):
	args = ['binwalk', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def foremost(fname):
	args = ['foremost', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	#args2 = ['strings', '/output/audit.txt']
	#proc2 = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc2.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')


def virustotalCheck(fname):
	sha256sum = sha256(fname)
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	params = {'apikey': '6201732de559c1e9c089e897ce858f0df21efb98f417e51c5ec6a08031abcf6e', 'resource': sha256sum}
	response = requests.get(url, params=params)
	print(response.json())
	if response.json()['response_code'] > 0:
		found = []
		for attr, value in response.json()['scans'].items():
			if value['detected'] == True:
				found.append(attr)
		return response.json()['positives'], response.json()['total'], response.json()['permalink'], found
	else:
		return 0

def hashsum(fname):
	return [['md5',md5(fname)], ['sha1',sha1(fname)], ['sha256',sha256(fname)]]

def strings(fname):
	args = ['strings', fname, '| tail']
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')

def xxd(fname):
	args = ['xxd', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out,err = proc.communicate()
	if out:
		return out.decode('utf-8').split('\n')
	return err.decode('utf-8').split('\n')
