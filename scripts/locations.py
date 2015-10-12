import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def locations_list():
	with open("CN/CN.txt",'r') as f:
		lines = f.read().split('\n')
		locations = []
		count =0
		for i in lines:
			try:
				locations += [[i.split('\t')[0],i.split('\t')[1],i.split('\t')[2], i.split('\t')[3],\
								 i.split('\t')[4], i.split('\t')[5], i.split('\t')[7], \
								 i.split('\t')[16], i.split('\t')[17]]]
			except IndexError:
				count += 1
				continue
		return locations

def locations_map():
	path = os.getcwd()
	path = path[:-7]
	path = 