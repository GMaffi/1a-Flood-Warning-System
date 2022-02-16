from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)
N = 10

highest_N_levels = stations_highest_rel_level(stations, N)

for i in highest_N_levels:
    print(i[0].name, i[1])