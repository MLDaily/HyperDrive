import sys
import os
from Drive.models import Places, UserInfo, UserPlaces
reload(sys)
sys.setdefaultencoding('utf-8')

l = []
ids = []
usr = []

with open('../../scripts/user_sorted.txt') as f:
    values = f.read().split('\n')
    for i in values:
    	if i.split(':')[0] not in ids:
    		ids += [i.split(':')[0]]
    	usr += [i.split(':')]

ids = ids[:-1]
print ids

with open('CN_places.txt') as f:
    values = f.read().split('\n')
    for i in values:
    	# if i.split(':') not in ids:
    	l += [i.split(',')]

with open('CN_places.txt') as f:
    locations = {}
    for i in f:
    	name = i.split(',')[1]
        locations[name] = i.split(',')[0]

for i in ids:
	UserInfo.objects.create(uid=i,uname='user'+i,upass='pass'+i)

for i in l:
	Places.objects.create(pid=i[0],pname=i[1],plat=i[2],plon=i[3],ptype=i[4],ploc=i[6])

for i in usr:
	UserPlaces.objects.create(userid=i[0] ,placeid=locations[i[1]] )