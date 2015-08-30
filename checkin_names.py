from geopy.geocoders import Nominatim
from time import sleep
from random import random

geolocator = Nominatim()

count = 0

f = open('checkin_latlon.txt', 'r')
nf = open('checkin_locations.txt', 'r')

for nline in nf:
    count += 1
    print(f.readline())

print("Count: {}".format(count))

nf.close()

nf = open('checkin_locations.txt', 'a')


for line in f:
    location = geolocator.reverse(line)
    address = location.address
    new_line = line[:-1] + ',"' + address + '"\n'
    nf.write(new_line)
    sleep(random()*3)
    print(new_line)