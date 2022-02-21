from pickle import HIGHEST_PROTOCOL
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    '''Tests stations returned are all over the threshold stated'''
    thresh_list = (0.3, 0.5, 0.7, 1.0)
    for thresh in thresh_list:
        stations_over_threshold = stations_level_over_threshold(stations, thresh)
        for i in stations_over_threshold:
            assert i[1] >= thresh


def test_stations_highest_rel_level():
    '''Tests N stations are returned and relative levels are in descending order'''
    N_list = (3, 7, 15, 27)
    for N in N_list:
        highest_N_levels = stations_highest_rel_level(stations, N)
        assert len(highest_N_levels) == N
        for i in range(1,len(highest_N_levels)):
            current = highest_N_levels[i]
            previous = highest_N_levels[i-1]
            assert current[1] <= previous [1]
    

