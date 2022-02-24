from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
update_water_levels(stations)

N = 5
stations_by_rel_level = stations_highest_rel_level(stations, N, 20)

for i in stations_by_rel_level:
    station = i[0]

    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_level_with_fit(station, dates, levels, 4)