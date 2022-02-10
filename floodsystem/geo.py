# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from re import A
from .utils import sorted_by_key  # noqa

from haversine import haversine as hs
from floodsystem.station import MonitoringStation


def stations_by_distance(stations, p):
    '''returns a list of the distance from the stations to the 
    coordinate p, sorted with the closest station first'''

    stations_by_dist = []

    for i in stations:
        station_data = (i, hs(p,i.coord))
        stations_by_dist.append(station_data)

    return sorted_by_key(stations_by_dist, 1)

def stations_within_radius(stations, centre, r):
    '''returns a list of all stations within radius r of a geographic coordinate'''
    stations_within_radius = []
    for i in stations:
        if hs(i.coord,centre) < r:
            stations_within_radius.append(i)
            
    return stations_within_radius

#Task 1D
set_river = set()

def rivers_with_station(stations):
    for station in stations:
        set_river.add(station.river)
    return set_river

def stations_by_river(stations):
    d_river_stations = {}
    for station in stations:
        if station.river in d_river_stations:
            d_river_stations[station.river].append(station.name)
        else:
            d_river_stations[station.river] =  [station.name]
    
    return d_river_stations

#Task 1E
def rivers_by_station_number(stations, N):
    d_river_stations = stations_by_river(stations)
    list_river_stations = d_river_stations.items()
    list_river = []
    for tuple in list_river_stations:
	    list_river.append(tuple[0])
    list_number_stations = []
    for tuple in list_river_stations:
        list_number_stations.append(len(tuple[1]))
        list_river_number_stations = list(zip(list_river, list_number_stations))
    list_river_number_stations_sorted = sorted(list_river_number_stations, key=lambda tup: tup[1], reverse=True)
    list_most_riverstations = list_river_number_stations_sorted[0:N]
    return list_most_riverstations