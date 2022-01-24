from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

cam_centre = (52.2053, 0.1218)

stations = stations_within_radius(build_station_list(), cam_centre, 10)

station_names=[]
for i in stations:
    station_names.append(i.name)

print(sorted(station_names))