import sys
import os
from personal import *

# from Drive.models import Places, UserInfo, UserPlaces
reload(sys)
sys.setdefaultencoding('utf-8')

def location_types():
    with open('CN_places.txt') as f:
        loc_types = {}
        values = f.read().split('\n')

        # print values[:10]

        for i in values:
            try:
                typ = i.split(',')[4]
                loc_types[typ] = []
            except IndexError:
                continue

        # print loc_types.keys()[:10]

        for i in values:
            try:
                typ = i.split(',')[4]
                name = i.split(',')[1]
                loc_types[typ] += [name]
            except IndexError:
                continue

    return loc_types


def find_all_max():
    loc_types = location_types()
    
    lenvalues = []

    for i in loc_types.keys():
        lenvalues += [len(loc_types[i])]

    # print max(lenvalues)

    for i in loc_types.keys():
        if max(lenvalues) == len(loc_types[i]):
            maxtype = i
    return maxtype

def max_user_group():
    maxtype = find_all_max()

    loc_types = location_types()

    maxgroup = loc_types[maxtype]

    return maxgroup[:10]


def find_user_group(userid):
    usermax, usersort = most_frequent_type(userid)

    loc_types = location_types()

    usergroup = loc_types[usermax]

    return usergroup
