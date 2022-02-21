from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)
tol = 0.8

stations_over_threshold = stations_level_over_threshold(stations, tol)

for i in stations_over_threshold:
    print(i[0].name, i[1])