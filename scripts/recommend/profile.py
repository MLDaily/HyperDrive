import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def user_visited(userid):
    with open('user_reduced.txt') as f:
        values = f.read().split('\n')
        userlocs = []
        for i in values:
            if userid == i.split(':')[0]:
                for k in i.split(':')[1:]:
                    userlocs += [k]

    return userlocs

def feature_code_extract():
	with open('feature_code.txt') as f:
		values = f.read().split('\n')
		mapval = {}
		for i in values:
			try:
				feat = i.split('\t')[0].split('.')[1]
				name = i.split('\t')[1]
				mapval[feat] = [name]
			except IndexError:
				pass

	return mapval