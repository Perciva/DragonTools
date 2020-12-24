import subprocess
import hashlib
import requests
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

def virustotalCheck(fname):
	sha256sum = sha256(fname)
	headers =  {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
		'X-Tool': 'vt-ui-main',
		'X-VT-Anti-Abuse-Header': 'MTYwNjkyMDM3NjAtWkc5dWRDQmlaU0JsZG1scy0xNjA2NDg0NDc4Ljg3Mw==',
		'Accept-Ianguage': 'en-US,en;q=0.9,es;q=0.8'
	}
	prompt = requests.get(f'https://www.virustotal.com/ui/files/{sha256sum}', headers=headers)
	positives = int(prompt.json()['data']['attributes']['last_analysis_stats']['malicious'])
	total = int(prompt.json()['data']['attributes']['last_analysis_stats']['undetected']) + positives
	if positives:
		result = f"""
			<h4 class="small font-weight-bold">VirusTotal<span
		            class="float-right">{int(positives/total*100)}%</span></h4>
		    <div class="progress mb-4">
		        <div class="progress-bar bg-danger" role="progressbar" style="width: {int(positives/total*100)}%"
		            aria-valuenow="{positives}" aria-valuemin="0" aria-valuemax="{total}"></div>
		    </div>
		"""
		return result
	else:
		return "clear"

