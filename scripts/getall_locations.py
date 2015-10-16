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
    # write_to_file('')

def write_to_file(fname, loc):
    with open(fname, "a+") as f:
        for i in loc:
            f.write(':'.join(i) + '\n')

def locations_map(folder , map_loc):
    path = os.getcwd()
    path = path[:-7]
    path += "gps data/"
    os.chdir(path + folder + "/Trajectory/coord/")
    
    file_init = "initial_map.txt"
    file_fin = "final_map.txt"

    with open(file_init) as f:
        values = f.read().split('\n')
        for v in values:
            map_loc += [v.split(':')]

    with open(file_fin) as f:
        values = f.read().split('\n')
        for v in values:
            map_loc += [v.split(':')]
            # map_loc =s [[ids,name]]
        
    return map_loc
        # print len(ids), len(latlong), count


def go():
    map_loc = []
    for i in range(0,10):
        path = os.getcwd()
        fname = "00" + str(i)
        map_loc = locations_map(fname, map_loc)
        os.chdir(path)
    write_to_file('user_places.txt',map_loc)

if __name__ == '__main__':
    go()