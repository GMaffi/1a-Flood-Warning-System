from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

cam_centre = (52.2053, 0.1218)

stations = stations_by_distance(build_station_list(), cam_centre)

print("Nearest 10 stations:")
nearest_ten = []
for i in stations[:10]:
    nearest_ten.append((i[0].name, i[0].town, i[1]))
print(nearest_ten)

print("Furthest 10 stations:")
furthest_ten = []
for i in stations[-10:]:
    furthest_ten.append((i[0].name, i[0].town, i[1]))
print(furthest_ten)
