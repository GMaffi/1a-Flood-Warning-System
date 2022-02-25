import matplotlib.dates 
import numpy as np

def polyfit(dates, levels, p):
    d_float = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(d_float - d_float[0], levels, p)
    poly = np.poly1d(p_coeff)
    d0 = d_float[0]
    return (poly, d0)

def polyfit_coeff(dates,levels,p):
    d_float = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(d_float - d_float[0], levels, p)
    return p_coeff
