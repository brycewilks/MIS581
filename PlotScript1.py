# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:14:43 2023

@author: bryce
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

# Read the CSV file into a pandas DataFrame
# Replace 'your_data.csv' with the actual path to your CSV file
df = pd.read_csv('C:/Users/bryce/Downloads/MIS581_FInal/stations.csv')

# List of station IDs to plot
station_ids_to_plot = [
'USC00045026','USC00043551','USC00048758','USC00041697','USC00048606','USC00040931','USC00043357','USC00045679','USC00046136','USW00023225'
]

# Filter data for stations in the specified list
df_selected_stations = df[df['STATION_ID'].isin(station_ids_to_plot)]

# Create a Basemap instance for California
m = Basemap(
    projection='merc',
    # llcrnrlat=df_selected_stations['LATITUDE'].min() - 1,
    # urcrnrlat=df_selected_stations['LATITUDE'].max() + 1,
    # llcrnrlon=df_selected_stations['LONGITUDE'].min() - 1,
    # urcrnrlon=df_selected_stations['LONGITUDE'].max() + 1,
    llcrnrlat=32,
    urcrnrlat=43,
    llcrnrlon=-125,
    urcrnrlon=-112,
    resolution='i'
)

# Draw boundaries, coastlines, and states
m.drawcountries()
m.drawcoastlines()
m.drawstates()

# Convert lat-lon to x-y coordinates
x, y = m(df_selected_stations['LONGITUDE'].tolist(), df_selected_stations['LATITUDE'].tolist())

# Plot points on the map
m.scatter(x, y, s=50, color='blue', marker='o', label='Selected Stations')

# Add labels and legend
plt.title('Top 10 Locations for Reservoirs')
plt.legend()
plt.savefig('C:/Users/bryce/Downloads/MIS581_FInal/Top10Stations.png', dpi = 100)

# Show the plot
plt.show()
