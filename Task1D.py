from os import stat
from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()

    x = rivers_with_station(stations)

    print(len(x))
    rivers = []
    for river in x:
        rivers.append(river)
    rivers.sort()
    print(rivers[:10])

    station_Aire = stations_by_river(stations)['River Aire']
    print(station_Aire[:10])

if __name__ == "__main__":
    print("***Task 1D CUED Part 1A Flood Warning System ***")
    run()