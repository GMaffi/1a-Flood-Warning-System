from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

from haversine import haversine as hs



def test_stations_by_distance():
    '''tests that each station in the list resturned by the stations_by_distance function
    has a distance higher than the one before it'''

    coord = (0, 0)
    stations = stations_by_distance(build_station_list(), coord)

    for i in range(1, len(stations)):
        current_station = stations[i]
        previous_station = stations[i-1]
        assert current_station[1] >= previous_station[1]

def test_stations_within_radius():
    '''tests that the distance from each station returned by the stations_within_radius
    function is less than the specified distance from the coordinate provided'''
    coord = (52.2, 0)
    radius = 20
    stations = stations_within_radius(build_station_list(), coord, radius)
    for i in stations:
        assert  hs(i.coord, coord) <= radius

