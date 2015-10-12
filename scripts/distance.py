# Find max distance of all the files in the coords folder and put the results in distance.txt

import math

nof = 171
max_distance = []
folder = "000"
for fno in range(1, nof+1):
    filename = str(fno) + ".txt"
    f = open("gps data/" + folder + "/Trajectory/coord/" + filename, "r")
    lat = []
    lon = []

    for i in f:
        coord = i.split(",")
        lat.append(float(coord[0]))
        lon.append(float(coord[1]))
    
    f.close()
    
    i = 0
    max_distance.append(0)
    while i < len(lat) - 1:
        R = 6371000
        phi1 = math.radians(lat[i])
        phi2 = math.radians(lat[i+1])
        dphi = math.radians(lat[i+1] - lat[i])
        dl   = math.radians(lon[i+1] - lon[i])
        a = (math.sin(dphi/2)**2) + (math.cos(phi1) * math.cos(phi2) * math.sin(dl/2)**2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        if d > max_distance[fno-1]:
            max_distance[fno-1] = d
        i += 1

f = open("gps data/" + folder + "/Trajectory/coord/distance.txt", "w")
fno = 0

while fno < len(max_distance):
    contents = str(fno+1) + "," + str(max_distance[fno]) + "\n"
    f.write(contents)
    fno += 1
    
f.close()

print(max(max_distance))