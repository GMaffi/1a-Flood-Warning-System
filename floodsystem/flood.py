from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for i in stations:
        rel_level = i.relative_water_level()
        if rel_level != None and rel_level > tol:
            stations_over_threshold.append((i, rel_level))

    return stations_over_threshold