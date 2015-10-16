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
    print len(locations.keys())


def locations_map(folder = '000'):
    path = os.getcwd()
    path = path[:-7]
    path += "/gps data/"
    os.chdir(path + folder + "/Trajectory/coord/")
    nof = len(os.listdir(path + folder + "/Trajectory/coord/"))
    print("nof: " + str(nof))
    for fno in range(1, nof-2):
        print fno
        # filename = str(fno) + ".txt"
        # f = open(filename, "r")
        # lat = []
        # lon = []
        # tim = []

        # for i in f:
        #     coord = i.split(",")
        #     lat.append(float(coord[0]))
        #     lon.append(float(coord[1]))
        #     x = coord[2]
        #     x = x[1:-2]
        #     tim.append(x)
        
        # f.close()
        # initial, final = get_initial_final(lat, lon, tim)
        
        # distance = get_distance(initial, final)
        
        # write_to_file("initial.txt", initial, fno)
        # write_to_file("final.txt", final, fno)

        
def go():
    for i in range(0,10):
        path = os.getcwd()
        fname = "00" + str(i)
        locations_map(fname)
        os.chdir(path)
