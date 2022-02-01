# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations




def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    trange_a = None
    s_a = MonitoringStation(s_id, m_id, label, coord, trange_a, river, town)
    assert s_a.typical_range_consistent() == False

    trange_b = (1.6, 0.5)
    s_b = MonitoringStation(s_id, m_id, label, coord, trange_b, river, town)
    assert s_b.typical_range_consistent() == False

    trange_c = (1.2, 2.4)
    s_c = MonitoringStation(s_id, m_id, label, coord, trange_c, river, town)
    assert s_c.typical_range_consistent() == True

