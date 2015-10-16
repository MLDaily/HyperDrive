import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

loc = []

with open('user_places.txt') as f:
    values = f.read().split('\n')
    for i in values:
        loc += [i.split(':')]

    for i in loc:
        i[0] = int(i[0])
    
loc = sorted(loc,key=lambda x: (x[0],x[1]))

def write_to_file(fname, loc):
    with open(fname, "a") as f:
        for i in loc:
            f.write(':'.join(i) + '\n')

print loc

for i in loc:
    i[0] = str(i[0])

write_to_file('user.txt',loc)