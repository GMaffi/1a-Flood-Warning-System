import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.title(station)
    plt.show()