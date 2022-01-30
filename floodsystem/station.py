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
        if self.typical_range != None:
            typ_range = self.typical_range
            if typ_range[1] > typ_range[0]:
                return True
            else:
                return False
        else:
            return False

def inconsistent_typical_range_stations(stations):
    '''returns a list of the stations in the input list which have inconsistent rage data'''
    inconsistent_stations = []
    for i in stations:
        if i.typical_range_consistent() == False:
            inconsistent_stations.append(i)
    return inconsistent_stations
