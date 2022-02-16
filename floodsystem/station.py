# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        '''checks if the height range data is consistent. it is inconsistent if the max height
        is less than the min height of the data is not present'''
        typ_range = self.typical_range
        if typ_range == None:
            return False
        else:
            if typ_range[1] > typ_range[0]:
                return True
            else:
                return False

    def relative_water_level(self):
        '''Returns the current water level relative to the typpical range where the typical minimum is
        0 and the typical maximum is 1'''
        if self.typical_range_consistent == False:
            return None
        elif self.latest_level == None:
            return None
        elif self.typical_range == None:
            return None
        else:
            level = self.latest_level
            typ_range = self.typical_range
            rel_range = (level - typ_range[0])/(typ_range[1] - typ_range[0])
            return rel_range


def inconsistent_typical_range_stations(stations):
    '''returns a list of the stations in the input list which have inconsistent rage data'''
    inconsistent_stations = []
    for i in stations:
        if i.typical_range_consistent() == False:
            inconsistent_stations.append(i)
    return inconsistent_stations
