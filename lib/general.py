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
		res = out.decode('utf-8').split('\n')
		kiri = []
		kanan = []
		# print("1")
		for r in res:
			if r:
				kiri.append(r[0:r.index(':')])
				kanan.append(r[r.index(":")+2:])

		table = f"""
			<table style = "width:100%; border: 1px white solid; text-align: center">
				<tr style= "border: 1px white solid">
					<th style= "border: 1px white solid"> Description </th>
					<th style= "border: 1px white solid"> Result </th>
				</tr>
				
		"""

		for z in range(len(kiri)):

			row = f"""
				<tr style= "border: 1px white solid">
					<td style= "border: 1px white solid">{kiri[z]}</td>
					<td style= "border: 1px white solid">{kanan[z]}</td>
				</tr>
			"""
			# print("asdasd")
			table = table + row
		

		table = table + "</table>"
		# print(table)
		return table
	return err.decode('utf-8').split('\n')

def binwalk(fname):
	args = ['binwalk', fname]
	proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
	out, err = proc.communicate()
	if out:
		res = out.decode('utf-8').split('\n')
		res = str(res[3]).split(' ')
		res[:] =  [x for x in res if x]
		table = f"""
			<table style = "width:100%; border: 1px white solid; text-align: center">
				<tr style= "border: 1px white solid">
					<th style= "border: 1px white solid"> Decimal </th>
					<th style= "border: 1px white solid"> Hexadecimal </th>
					<th style= "border: 1px white solid"> Description </th>
				</tr>
				<tr style= "border: 1px white solid">
					<td style= "border: 1px white solid">{res[0]}</td>
					<td style= "border: 1px white solid">{res[1]}</td>
					<td style= "border: 1px white solid">{" ".join(res[2:])}
				</tr>
			</table>
		"""
		return table
	return err.decode('utf-8').split('\n')

def virustotalCheck(fname):
	try:
		sha256sum = sha256(fname)
		url = 'https://www.virustotal.com/vtapi/v2/file/report'
		params = {'apikey': '6f24efbef7ddb97cc5c19e528f086afd7578b44383c73d4aacfa854d0e73bb39', 'resource': sha256sum}
		response = requests.get(url, params=params)
		if response.json()['verbose_msg'] == "The requested resource is not among the finished, queued or pending scans":
			return "Please wait a few minutes for another request, your request has been sent to the queue"

		if response.json()['positives'] > 0:
			found = []
			for attr, value in response.json()['scans'].items():
				if value['detected'] == True:
					tmp = []
					tmp.append(attr)
					tmp.append(value['result'])
					found.append(tmp)
			return response.json()['positives'], response.json()['total'], response.json()['permalink'], found
		else:
			return "Virustotal didn't find anything suspicious with this file"
	except:
		return "Please wait a few minutes for another request, your request has been sent to the queue"

def hashsum(fname):
	table = f"""
			<table style = "width:100%; border: 1px white solid; text-align: center">
				<tr style= "border: 1px white solid">
					<th style= "border: 1px white solid"> Algorithm </th>
					<th style= "border: 1px white solid"> Result </th>
				</tr>
				<tr style= "border: 1px white solid">
					<td style= "border: 1px white solid">md5</td>
					<td style= "border: 1px white solid">{md5(fname)}</td>
				</tr>
				<tr style= "border: 1px white solid">
					<td style= "border: 1px white solid">sha1</td>
					<td style= "border: 1px white solid">{sha1(fname)}</td>
				</tr>
				<tr style= "border: 1px white solid">
					<td style= "border: 1px white solid">sha256</td>
					<td style= "border: 1px white solid">{sha256(fname)}</td>
				</tr>
			</table>
		"""
	return table

def strings(fname):
	args = ['strings', fname]
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
