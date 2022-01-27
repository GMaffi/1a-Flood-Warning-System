from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list



def test_stations_by_distance():

    coord = (0, 0)
    stations = stations_by_distance(build_station_list(), coord)

    for i in range(1, len(stations)):
        assert stations[i, 1] > stations[i-1, 1]

def test_stations_within_radius():
    coord = (50, 0)
    radius = 20
    stations = stations_within_radius(build_station_list(), coord, )
    for i in stations:
        assert i[1] <= radius
        