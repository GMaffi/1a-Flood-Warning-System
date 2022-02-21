import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.show()