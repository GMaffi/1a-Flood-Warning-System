from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

cam_centre = (52.2053, 0.1218)

stations = stations_by_distance(build_station_list(), cam_centre)
print("Nearest 10 stations:")
print(stations[:10])
print("Furthest 10 stations:")
print(stations[-10:])