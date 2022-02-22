from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for i in stations:
        rel_level = i.relative_water_level()
        if rel_level != None and rel_level > tol:
            stations_over_threshold.append((i, rel_level))
    
    return sorted_by_key(stations_over_threshold, 1, True)

def stations_highest_rel_level(stations, N, tol=50):
    '''returns the N highest relative water levels and their station, ignores 
    those above a specified relative level as not realistic and likely to be erroneous'''
    stations_by_level = []
    for i in stations:
        rel_level = i.relative_water_level()
        if rel_level != None:
            if rel_level < tol:
                stations_by_level.append((i, rel_level))
        
    stations_by_level = sorted_by_key(stations_by_level, 1, True)
    return stations_by_level[:N]