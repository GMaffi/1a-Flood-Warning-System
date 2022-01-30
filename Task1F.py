from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

inconsistent_stations = inconsistent_typical_range_stations(stations)

names = []

for i in inconsistent_stations:
    names.append(i.name)

print(names)
