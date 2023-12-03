# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:39:46 2023

@author: bryce
"""

import pandas as pd
import os

# Specify the directory containing your CSV files
csv_directory = 'C:/Users/bryce/Downloads/MIS581_FInal/'

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv') and 'stations' not in f and 'ConcatData' not in f]

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each CSV file and read it into a DataFrame
for csv_file in csv_files:
    print("Opening: "+csv_file)
    csv_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(csv_path)
    dfs.append(df)

# Concatenate all DataFrames in the list
concatenated_df = pd.concat(dfs, ignore_index=True)

# Write the concatenated DataFrame to a new CSV file
concatenated_df.to_csv(csv_directory+"ConcatData.csv",index=False)

# print(f"Data has been successfully concatenated and saved to {output_csv_path}.")


def LoopThroughStationCSV(path):
    StationsMap = {}
    with open(path+"stations.csv") as stations:
        stations_rl = stations.readlines()
        for i in range(1,len(stations_rl)):
            st_sl = stations_rl[i].split(",")
            
            location = st_sl[1]
            lat = st_sl[7] 
            lon = st_sl[8] 
            el = st_sl[9] 
            stat = st_sl[0].replace("GHCND:","")
            StationsMap[stat] = str(location)+","+str(lat)+","+str(lon)+","+str(el)
    stations.close()
    
    return StationsMap


path = 'C:/Users/bryce/Downloads/MIS581_FInal/'

StationsMap = LoopThroughStationCSV(path)
with open(path+"ConcatDataUP.csv","w") as up:
    with open(path+"ConcatData.csv") as old:
        old_rl = old.readlines()
        
        for i in range(len(old_rl)):
            station_id = old_rl[i].split(",")[0]
            if i == 0:
                up.write(old_rl[i].strip("\n")+",LOCATION,LATITUDE,LONGITUDE,ELEVATION\n")
            else:
                up.write(old_rl[i].strip("\n") + "," + StationsMap.get(station_id, ",")+"\n")
        
                     
up.close()
old.close()

