import os
import math

def get_minutes(t1, t2):
    x = t1.split(":")
    y = t2.split(":")
    h1 = int(x[0])
    h2 = int(y[0])
    m1 = int(x[1])
    m2 = int(y[1])
    min_diff = m2 - m1
    hour_diff = (h2 - h1) * 60
    total_min = hour_diff + min_diff
    return total_min

def get_initial_final(lat, lon, tim):
    initial = []
    final = []
    i = 0
    fin = 0
    initial.append([lat[i], lon[i]])
    while i < len(lat) - 1:
        if fin == 1:
            initial.append([lat[i], lon[i]])
            fin = 0
        if get_minutes(tim[i], tim[i+1]) > 60:
            final.append([lat[i], lon[i]])
            fin = 1
        i += 1
    final.append([lat[i], lon[i]])

    return initial, final

def get_distance(initial, final):
    distance = []
    for i in range(0, len(initial)):
        R = 6371000
        phi1 = math.radians(float(initial[i][0]))
        phi2 = math.radians(float(final[i][0]))
        dphi = math.radians(float(final[i][0]) - float(initial[i][0]))
        dl   = math.radians(float(final[i][1]) - float(initial[i][1]))
        a = (math.sin(dphi/2)**2) + (math.cos(phi1) * math.cos(phi2) * math.sin(dl/2)**2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        distance.append(d)
    return distance

def write_to_file(fname, x, uid):
    f = open(fname, "a")
    for i in x:
        f.write(str(uid) + ":" + str(i[0]) + "," + str(i[1]) + '\n')
    # f.write("\n")
    f.close()


def begin(folder = "000"):
    path = os.getcwd() 
    path = path[:-7]
    path += "gps data/"
    os.chdir(path + folder + "/Trajectory/coord/")
    # print path+ folder + "/Trajectory/coord/"
    nof = len(os.listdir(path + folder + "/Trajectory/coord/"))
    # print("nof: " + str(nof))
    # os.chdir(path)
    for fno in range(1, nof-2):
        filename = str(fno) + ".txt"
        f = open(filename, "r")
        lat = []
        lon = []
        tim = []

        for i in f:
            coord = i.split(",")
            lat.append(float(coord[0]))
            lon.append(float(coord[1]))
            x = coord[2]
            x = x[1:-2]
            tim.append(x)
        
        f.close()
        initial, final = get_initial_final(lat, lon, tim)
        
        distance = get_distance(initial, final)
        
        write_to_file("initial.txt", initial, fno)
        write_to_file("final.txt", final, fno)

def go():
    path = os.getcwd()
    for i in range(0,10):
        fname = "00" + str(i)
        begin(fname)
        os.chdir(path)
    # begin('010')
    # os.chdir(path)

if __name__ == "__main__":
    go()
