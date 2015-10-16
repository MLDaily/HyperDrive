import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def write_to_file(fname, locations):
    with open(fname, "a+") as f:
        for i in locations:
            f.write(i[0]+','+i[1]+','+i[2]+','+i[3]+','+i[4]+','+i[5]+','+i[6]+'\n')

def locations_list():
    with open("../CN/CN.txt",'r') as f:
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

        write_to_file('../CN/CN_places.txt',locations)

        

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
