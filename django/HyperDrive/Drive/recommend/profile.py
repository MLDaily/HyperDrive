import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def user_locations():
	loc = []

	with open('user_places.txt') as f:
	    values = f.read().split('\n')
	    for i in values:
	        loc += [i.split(':')]
	    