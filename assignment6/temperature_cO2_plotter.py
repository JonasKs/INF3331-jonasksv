import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_CO2(yearfrom=1751, yearto=2012):
    """Plot CO2 values from year x to year"""
    csvfile = '/home/ubuntu/Documents/inf3331/co2.csv'
    contains = pd.read_csv(csvfile, sep=',')
    contains = contains.set_index('Year')
    years = contains.loc[yearfrom:yearto, 'Carbon']
    plt.plot(years)
    plt.xlabel('Year')
    plt.ylabel('Carbon')
    plt.title('CO2 per year')

    #Make Matplotlib write to BytesIO
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    #figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode("ascii")
    plt.close() # Had to be done to clean figure from memory.
    return figdata_png

#plot_CO2(1755,2012)

def plot_temperature(month, yearfrom=1816, yearto=2012, ymin=None, ymax=None):
    """Plot CO2 levels for specified month from year x to year x"""
    csvfile = '/home/ubuntu/Documents/inf3331/temperature.csv'
    contains = pd.read_csv(csvfile, sep=',')
    contains = contains.set_index('Year')
    years = contains.loc[yearfrom:yearto, month]
    plt.plot(years)
    plt.xlabel('Year')
    plt.ylabel('Carbon level')
    plt.title('co2 in {} month, from {} to {}'.format(month,yearfrom,yearto))
    plt.ylim(ymin, ymax)

    #Make Matplotlib write to BytesIO
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    #figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue()).decode("ascii")
    plt.close() # Had to be done to clean figure from memory
    return figdata_png

#plot_temperature('September', 1816, 1888)
