import sys, math
from group import *
from profile import *
from personal import *
import os
reload(sys)
sys.setdefaultencoding('utf-8')


with open('CN_places.txt') as f:
    locations = {}
    values = f.read().split('\n')
    for i in values:
        try:
            typ = i.split(',')[4]
            name = i.split(',')[1]
            lat = i.split(',')[2]
            lon = i.split(',')[3]
            locations[name] = [lat,lon]
        except IndexError:
            pass
            

def locate_nearest_personal(userid, nearest):
    usergroup = find_user_group(userid)
    userlocs = user_visited(userid)

    # distsum = 0
    usersum = {}
    for k in usergroup:
        usersum[k] = 0
        for i in userlocs:
            usersum[k] += calculate_dist(locations[i],locations[k])

    return sorted(usersum,key=lambda x: (usersum[x]),reverse=True)[:nearest]


def calculate_dist(ll1, ll2):
    R = 6371000
    phi1 = math.radians(float((ll1[0])))
    phi2 = math.radians(float((ll2[0])))
    dphi = math.radians(float(ll1[0]) - float(ll2[0]))
    dl   = math.radians(float(ll1[1]) - float(ll2[1]))
    a = (float(math.sin(float(dphi)/2)**2)) +\
            (float(math.cos(float(phi1)) * float(math.cos(float(phi2)))\
                * float(math.sin(float(dl)/2)**2)))
    c = 2 * math.atan2(float(math.sqrt(a)), float(math.sqrt(1-a)))
    d = R * c

    return d