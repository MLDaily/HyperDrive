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
                    userlocs += k

    return userlocs