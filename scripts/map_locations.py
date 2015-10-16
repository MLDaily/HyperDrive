import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

with open('../CN/CN_places.txt') as f:
    locations = {}
    for i in f:
        lat = i.split(',')[2]
        lon = i.split(',')[3]
        typ = i.split(',')[4]
        name = i.split(',')[1]
        locations[name] = [lat,lon,typ]

def write_to_file(fname, loc):
    with open(fname, "a+") as f:
        for i in loc.keys():
            f.write(i + ':' + loc[i] + '\n')

def locations_map(folder = '000'):
    path = os.getcwd()
    path = path[:-7]
    path += "gps data/"
    os.chdir(path + folder + "/Trajectory/coord/")
    
    file_init = "initial.txt"
    file_fin = "final.txt"

    # locations = locations_dict()

    map_loc = {}

    with open(file_init) as f:
        values = f.read().split('\n')

        count =0
        for v in values:
            try:
                ids = v.split(':')[0]
                latlong = v.split(':')[1].split(',')
                print '.',
                for loc in locations.keys():
                    if locations[loc][0] in latlong[0] or latlong[0] in locations[loc][0]:
                        if locations[loc][1] in latlong[1] or latlong[1] in locations[loc][1]:
                            map_loc[ids] = loc
                            print ":"
            except IndexError or ValueError:
                pass
        # print ""
        print map_loc
        write_to_file('initial_map.txt',map_loc)
        

    map_loc = {}
    with open(file_fin) as f:
        values = f.read().split('\n')

        count =0
        for v in values:
            try:
                ids = v.split(':')[0]
                latlong = v.split(':')[1].split(',')
                print '.',
                for loc in locations.keys():
                    if locations[loc][0] in latlong[0] or latlong[0] in locations[loc][0]:
                        if locations[loc][1] in latlong[1] or latlong[1] in locations[loc][1]:
                            map_loc[ids] = loc
                            print ':'
            except IndexError or ValueError:
                pass
        print map_loc
        write_to_file('final_map.txt',map_loc)
        
        # print len(ids), len(latlong), count

        
def go():
    for i in range(0,10):
        path = os.getcwd()
        fname = "00" + str(i)
        locations_map(fname)
        os.chdir(path)

if __name__ == '__main__':
    go()
