import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def most_frequent_type(userid):
    typescount = {}

    with open('CN_places.txt') as f:
        locations = {}
        values = f.read().split('\n')
        for i in values:
            try:
                typ = i.split(',')[4]
                name = i.split(',')[1]
                locations[name] = [typ]
                typescount[typ] = 0
            except IndexError:
                pass

    with open('user_reduced.txt') as f:
        values = f.read().split('\n')

        usertypes = []
        for i in values:
            if userid == i.split(':')[0]:
                for k in i.split(':')[1:]:
                    usertypes += locations[k]

    print 'User has mostly travelled these types of locations : ', usertypes

    for i in usertypes:
        typescount[i] += 1

    maxtype = max(typescount, key=lambda x:(typescount[x]))
    sortd = sorted(typescount, key=lambda x:(typescount[x]))

    return maxtype, sortd