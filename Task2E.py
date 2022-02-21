from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import date, timedelta

stations = build_station_list()
update_water_levels(stations)

highest_5_stations = []
for tuple in stations_highest_rel_level(stations, 5):
        highest_5_stations.append(tuple[0])

tod = date.today()
numdays = 10
date_list = []
for x in range (0, numdays):
    date_list.append(tod- timedelta(days = x))

plot_water_levels(highest_5_stations, date_list)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
