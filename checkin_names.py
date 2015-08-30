from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep
from random import random


def fetch():
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
        try:
            location = geolocator.reverse(line)
            address = location.address
            new_line = line[:-1] + ',"' + address + '"\n'
            nf.write(new_line)
            sleep(random())
            print(new_line)
        except GeocoderTimedOut:
            nf.close()
            f.close()
            sleep(10)
            fetch()

    nf.close()
    f.close()

if __name__ == '__main__':
    fetch()