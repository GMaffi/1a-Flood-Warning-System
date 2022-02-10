#Task1D.py

from os import stat
from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    x = rivers_with_station(stations)
    
    rivers = []
    for river in x:
        rivers.append(river)
    rivers.sort()
    print(str(len(x)) + " stations. First 10 - " + str(rivers[:10]))

    stations_Aire = stations_by_river(stations)['River Aire']
    stations_Aire.sort()
    print(stations_Aire)

    stations_Cam = stations_by_river(stations)['River Cam']
    stations_Cam.sort()
    print(stations_Cam)

    stations_Thames = stations_by_river(stations)['River Thames']
    stations_Thames.sort()
    print(stations_Thames)

if __name__ == "__main__":
    run()