import math

f = open("gps data/000/Trajectory/coord/3.txt", "r")

lat = []
lon = []

for i in f:
    coord = i.split(",")
    lat.append(float(coord[0]))
    lon.append(float(coord[1]))

f.close()

i = 0
max_distance = 0
while i < len(lat) - 1:
    R = 6371000
    phi1 = math.radians(lat[i])
    phi2 = math.radians(lat[i+1])
    dphi = math.radians(lat[i+1] - lat[i])
    dl   = math.radians(lon[i+1] - lon[i])
    a = (math.sin(dphi/2)**2) + (math.cos(phi1) * math.cos(phi2) * math.sin(dl/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    if d > max_distance:
        max_distance = d
    i += 1

print(max_distance)