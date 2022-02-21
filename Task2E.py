<<<<<<< HEAD
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import date, timedelta
=======
import datetime
from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.plot import plot_water_levels
>>>>>>> 6ad10b0aa38e87c91e1748420637d611d2d8297f

stations = build_station_list()
update_water_levels(stations)

N = 5
stations_by_rel_level = stations_highest_rel_level(stations, N)

for i in stations_by_rel_level:
    station = i[0]

    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_levels(station, dates, levels)
