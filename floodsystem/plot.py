import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation

def plot_water_levels(station, dates, levels):
    '''plots the water levels and typpical range for the station with the entered data'''
    
    #plot river level graph
    plt.plot(dates, levels)

    #plot typical low and high
    typ_range = station.typical_range
    typ_min = []
    typ_max = []
    for i in range(len(dates)):
        typ_min.append(typ_range[0])
        typ_max.append(typ_range[1])
    plt.plot(dates, typ_min, 'b--')
    plt.plot(dates, typ_max, 'b--')

    #add titles and labels
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.show()