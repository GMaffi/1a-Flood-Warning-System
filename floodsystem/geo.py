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

stations_by_rivers = {}
def stations_by_rivers(stations):
    for ariver in set_river:
        list = []
        for station in stations:
            if station.river == ariver:
                stations_by_rivers[ariver] = list.append(station.name)
    return stations_by_rivers

