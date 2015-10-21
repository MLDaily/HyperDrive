import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def write_to_file(fname, locations):
    with open(fname, "a+") as f:
        for i in locations:
            f.write(i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4]+','+i[5]+','+i[6]+'\n')

def locations_list():
    with open("../CN/IN.txt",'r') as f:
        lines = f.read().split('\n')
        locations = []
        count =0
        for i in lines:
            try:
                locations += [[i.split('\t')[0],i.split('\t')[1],\
                                 i.split('\t')[4], i.split('\t')[5], i.split('\t')[7], \
                                 i.split('\t')[16], i.split('\t')[17]]]

            except IndexError:
                count += 1
                continue

        print len(locations), count

        write_to_file('../CN/IN_places.txt',locations)

if __name__ == '__main__':
    locations_list()