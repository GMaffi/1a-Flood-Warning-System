"""
Flood warning needs to be by town

Risk of flooding greatest when:
Water level high and rising and therefore data can be extrapolated to predict it will be very high in the future (using coefficients of polynomial in 2f)

When examining stations should probably examine the top x number of stations on water level, using 2b.

Need to determine the time window we will be examining - should be long enough to give good accuracy to fit but short enough to avoid runge's pheonmenon. 
Needs to be fairly short probably.

Severe, high, moderate, low ratings dependent on threshold water levels - these need to be determined.
Use extrapolation to predict the maximum water level expected and then assign rating based on the thresholds

"""
#from types import NoneType
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit_coeff
import datetime
import numpy as np

stations = build_station_list()
update_water_levels(stations)

# initial time period we want to examine (whole time period = 2*dt days)
dt = 2

# generate list of stations above a threshold of 0.8m
# fetch_measure_levels funciton only works when tol above a certain value - can only take a maximum number of stations
# therefore use stations_by_rel_level
N = 50
stations_by_rel_level = stations_highest_rel_level(stations, N, 20)

# generate list of tuples of polynomial coefficients, using value of dt and p from 2f intially
p_coeff = []
for i in stations_by_rel_level:
    station = i[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    p_coeff.append(polyfit_coeff(dates, levels, 4))

# compute the maximum water level expected when the data is extrapolated dt days into future
x = np.linspace(0, dt, 10)
max_water_level = []
for i in p_coeff:
    poly = np.poly1d(i)
    y = poly(x)
    max_water_level.append(max(y))

# not every station  has a town
# there may be cases where there are different alert levels for the town - only the highest should be shown
# ideally should sort towns by risk level on output

set_towns_severe = set()
set_towns_high = set()
set_towns_moderate = set()
set_towns_low =  set()

# initial guess for warning water level thresholds
severe = 5.0
high = 4.0
moderate = 2.5
low = 1.5

# print the towns for each risk level
for x, y in zip(stations_by_rel_level, max_water_level):
    station = x[0]
    if station.town == None:
        pass
    if y >= severe:
        set_towns_severe.add(station.town)
    elif y >= high:
        set_towns_high.add(station.town)
    elif y >= moderate:
        set_towns_moderate.add(station.town)
    elif y >= low:
        set_towns_low.add(station.town)
    else:
        pass

print("TOWNS WITH SEVERE FLOOD RISK: ")
print(set_towns_severe)
print("TOWNS WITH HIGH FLOOD RISK: ")
print(set_towns_high)
print("TOWNS WITH MODERATE FLOOD RISK: ")
print(set_towns_moderate)
print("TOWNS WITH LOW FLOOD RISK: ")
print(set_towns_low)
# Could use 2f to test the values of dt and p to give the optimum polynomial fit over a time range 2*dt
# Could see if we could increase N, the number of stations being examined, or try to create a list of stations over a minimum value

# Using below code all stations appear have a town associated 
"""set_towns = set()
list_stations_no_town = []
for station in stations:
    if station.town == NoneType:
        list_stations_no_town.append(station.name)
    else:
        set_towns.add(station.town)
print(len(set_towns))
print(len(list_stations_no_town))
"""