# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:24:56 2023

@author: bryce
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap

# Read the CSV file into a pandas DataFrame
# Replace 'your_data.csv' with the actual path to your CSV file
df = pd.read_csv('C:/Users/bryce/Downloads/MIS581_FInal/FilteredData.csv')

# List of station IDs to plot
station_ids_to_plot = [
'USC00040029','USC00040136','USC00040144','USC00040212','USC00040449','USC00040693','USC00040741','USC00040790','USC00040798','USC00040924','USC00040931','USC00040943','USC00040983','USC00041159','USC00041194','USC00041244','USC00041253','USC00041312','USC00041424','USC00041428','USC00041614','USC00041697','USC00041758','USC00041838','USC00041907','USC00041912','USC00041916','USC00041948','USC00042012','USC00042090','USC00042214','USC00042239','USC00042294','USC00042319','USC00042327','USC00042346','USC00042402','USC00042500','USC00042598','USC00042709','USC00042713','USC00042805','USC00042920','USC00042934','USC00042941','USC00042964','USC00043038','USC00043083','USC00043157','USC00043161','USC00043182','USC00043191','USC00043261','USC00043357','USC00043402','USC00043463','USC00043491','USC00043551','USC00043573','USC00043578','USC00043714','USC00043747','USC00043761','USC00043800','USC00043824','USC00043855','USC00043875','USC00043896','USC00043914','USC00043939','USC00044211','USC00044223','USC00044259','USC00044297','USC00044374','USC00044405','USC00044422','USC00044500','USC00044534','USC00044555','USC00044710','USC00044863','USC00044890','USC00044957','USC00044997','USC00045026','USC00045064','USC00045118','USC00045119','USC00045233','USC00045360','USC00045502','USC00045532','USC00045598','USC00045679','USC00045756','USC00045795','USC00045866','USC00045915','USC00045933','USC00045941','USC00045983','USC00046027','USC00046074','USC00046136','USC00046168','USC00046175','USC00046194','USC00046252','USC00046328','USC00046336','USC00046377','USC00046399','USC00046506','USC00046508','USC00046521','USC00046602','USC00046624','USC00046635','USC00046657','USC00046663','USC00046699','USC00046719','USC00046730','USC00046826','USC00046926','USC00046940','USC00046946','USC00047085','USC00047109','USC00047111','USC00047195','USC00047306','USC00047339','USC00047414','USC00047470','USC00047672','USC00047681','USC00047702','USC00047767','USC00047776','USC00047779','USC00047785','USC00047821','USC00047851','USC00047880','USC00047888','USC00047902','USC00047933','USC00047965','USC00048014','USC00048045','USC00048135','USC00048218','USC00048351','USC00048353','USC00048380','USC00048587','USC00048606','USC00048702','USC00048758','USC00048839','USC00048999','USC00049001','USC00049035','USW00003104','USW00003122','USW00003144','USW00023119','USW00023129','USW00023155','USW00023157','USW00023158','USW00023161','USW00023174','USW00023179','USW00023182','USW00023187','USW00023188','USW00023190','USW00023225','USW00023230','USW00023232','USW00023233','USW00023234','USW00023237','USW00023258','USW00023259','USW00023271','USW00023272','USW00023273','USW00024213','USW00024216','USW00093107','USW00093111','USW00093112','USW00093115','USW00093134','USW00093193','USW00093209','USW00093230'
]

# Filter data for specified stations
df_selected_stations = df[df['STATION'].isin(station_ids_to_plot)]

# Convert the 'DATE' column to a datetime format
df_selected_stations['DATE'] = pd.to_datetime(df_selected_stations['DATE'])

# Extract year from the 'DATE' column
df_selected_stations['YEAR'] = df_selected_stations['DATE'].dt.year

# Filter data for years since 2000
df_selected_stations = df_selected_stations[df_selected_stations['YEAR'] >= 1970] 

# Calculate the annual sum of 'PRCP+SNOW' for each station
annual_sum_prcp_snow = df_selected_stations.groupby(['STATION', 'YEAR'])['PRCP+SNOW'].sum().reset_index()
print(annual_sum_prcp_snow)

# Calculate the overall average annual sum for each station
overall_avg_annual_sum_prcp_snow = annual_sum_prcp_snow.groupby('STATION')['PRCP+SNOW'].mean().reset_index()

# Merge with the original dataframe to get additional information
heatmap_data = pd.merge(
    overall_avg_annual_sum_prcp_snow,
    df_selected_stations[['STATION', 'LATITUDE', 'LONGITUDE']],
    on='STATION', how='left'
)

# Create a Basemap instance for California
m = Basemap(
    projection='merc',
    llcrnrlat=heatmap_data['LATITUDE'].min() - 1,
    urcrnrlat=heatmap_data['LATITUDE'].max() + 1,
    llcrnrlon=heatmap_data['LONGITUDE'].min() - 1,
    urcrnrlon=heatmap_data['LONGITUDE'].max() + 1,
    resolution='i'
)

# Draw boundaries, coastlines, and states
m.drawcountries()
m.drawcoastlines()
m.drawstates()

# Convert lat-lon to x-y coordinates
x, y = m(heatmap_data['LONGITUDE'].tolist(), heatmap_data['LATITUDE'].tolist())

# Plot a scatter plot with colors corresponding to the overall average annual sum 'PRCP+SNOW' values
plt.scatter(x, y, c=heatmap_data['PRCP+SNOW'], cmap='coolwarm_r', s=50, marker='o', alpha=0.8, vmin=0, vmax=130)

# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Overall Average Annual Sum PRCP+SNOW')

# Add labels and title
plt.title('Heatmap of Overall Average Annual \nRain+Snowfall in California (1970-Present)')
plt.savefig('C:/Users/bryce/Downloads/MIS581_FInal/Avg_Annual_Sum4.png', dpi=100)

# Show the plot
plt.show()

