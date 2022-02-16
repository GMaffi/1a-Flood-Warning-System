from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)
tol = 0.8

stations_over_theshold = stations_level_over_threshold(stations, tol)

sorted_by_level=sorted_by_key(stations_over_theshold, 1, True)

for i in sorted_by_level:
    print(i[0].name, i[1])