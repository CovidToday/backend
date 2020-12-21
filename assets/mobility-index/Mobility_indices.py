# -*- coding: utf-8 -*-
"""Mobility_indices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bx2ELjbx3c38bWmMklMdfYfMjh1OEMsM
"""


from __future__ import print_function
from scipy.io import loadmat
from tqdm import tqdm
#from google.colab import drive
import numpy as np
import scipy
import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
import wget
import simplejson
#drive.mount('/content/gdrive')

wget.download('https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv', os.getcwd()+"/Global_Mobility_Report.csv")
g_list = pd.read_csv('Global_Mobility_Report.csv')

def normalize(arr):
  slope = int(arr[-1])-int(arr[-2])
  return int(arr[-1])+slope

def fn(mon):
  if(mon == "01"):
    return " January"
  if(mon == "02"):
    return " February"
  if(mon == "03"):
    return " March"
  if(mon == "04"):
    return " April"
  if(mon == "05"):
    return " May"
  if(mon == "06"):
    return " June"
  if(mon == "07"):
    return " July"
  if(mon == "08"):
    return " August"
  if(mon == "09"):
    return " September"
  if(mon == "10"):
    return " October"
  if(mon == "11"):
    return " November"
  if(mon == "12"):
    return " December"
def convert(dat): 
    return  str(dat[-2:]) + fn(str(dat[5:7]))

def isNaN(num):
    return num != num

india_dict = {}
df=pd.DataFrame()
csv_state = []
csv_dates = []
csv_retail = []
csv_grocery = []
csv_parks = []
csv_transit = []
csv_workplace = []
csv_residential = []
csv_average_mobility = []
temp=0
columnDict = {}
g_list = g_list[g_list['country_region'] == 'India']
g_list = g_list.drop_duplicates(subset=['sub_region_1', 'date'])
g_list.fillna(method='ffill')
for index, row in g_list.iterrows():
    if isNaN(row['sub_region_1']):
      row['sub_region_1']='India'
    if row['sub_region_1'] not in  india_dict.keys():
      india_dict[row['sub_region_1']] = {}
    state = row['sub_region_1']
    dates = row['date']
    # print(state," ",dates)
    retail = row['retail_and_recreation_percent_change_from_baseline']
    grocery = row['grocery_and_pharmacy_percent_change_from_baseline']
    parks = row['parks_percent_change_from_baseline']
    transit = row['transit_stations_percent_change_from_baseline']
    workplace = row['workplaces_percent_change_from_baseline']
    residential = row['residential_percent_change_from_baseline']
    if 'dates' not in india_dict[state].keys():
      india_dict[state]['dates'] = []
      india_dict[state]['retail'] = []
      india_dict[state]['grocery'] = []
      india_dict[state]['parks'] = []
      india_dict[state]['transit'] = []
      india_dict[state]['workplace'] = []
      india_dict[state]['residential'] = []
      india_dict[state]['average_mobility'] = []
    l = len(india_dict[state]['dates'])
    if(l>1 and l%7<2):
      india_dict[state]['workplace'].append(india_dict[state]['workplace'][-1])
      india_dict[state]['retail'].append(india_dict[state]['retail'][-1])
      india_dict[state]['grocery'].append(india_dict[state]['grocery'][-1])
      india_dict[state]['parks'].append(india_dict[state]['parks'][-1])
      india_dict[state]['transit'].append(india_dict[state]['transit'][-1])
      india_dict[state]['residential'].append(india_dict[state]['residential'][-1])
    else:
      india_dict[state]['workplace'].append(row['workplaces_percent_change_from_baseline'])
      india_dict[state]['retail'].append(row['retail_and_recreation_percent_change_from_baseline'])
      india_dict[state]['grocery'].append(row['grocery_and_pharmacy_percent_change_from_baseline'])
      india_dict[state]['parks'].append(row['parks_percent_change_from_baseline'])
      india_dict[state]['transit'].append(row['transit_stations_percent_change_from_baseline'])
      india_dict[state]['residential'].append(row['residential_percent_change_from_baseline'])
    temp=[]
    if(not isNaN((india_dict[state]['retail'][-1]))):
      temp.append(int(india_dict[state]['retail'][-1]))
    if(not isNaN((india_dict[state]['grocery'][-1]))):
      temp.append(int(india_dict[state]['grocery'][-1]))
    if(not isNaN((india_dict[state]['transit'][-1]))):
      temp.append(int(india_dict[state]['transit'][-1]))
    if(not isNaN((india_dict[state]['workplace'][-1]))):
      temp.append(int(india_dict[state]['workplace'][-1]))
    count = 0
    sum=0
    for i in temp:
      sum+=i
      count+=1
    if(len(temp)>0):
        avg=sum/count
        india_dict[state]['average_mobility'].append(round(avg,2))
    else:
        india_dict[state]['average_mobility'].append('')
    india_dict[state]['dates'].append(convert(row['date']))
      
    for i in range(len(india_dict[state]['dates'])):
      if (temp!=india_dict[state]['dates'][-1]) :
        csv_state.append(state)
        csv_dates.append(india_dict[state]['dates'][-1])
        csv_retail.append(india_dict[state]['retail'][-1])
        csv_grocery.append(india_dict[state]['grocery'][-1])
        csv_parks.append(india_dict[state]['parks'][-1])
        csv_transit.append(india_dict[state]['transit'][-1])
        csv_workplace.append(india_dict[state]['workplace'][-1])
        csv_residential.append(india_dict[state]['residential'][-1])
        csv_average_mobility.append(india_dict[state]['average_mobility'][-1])
        temp=india_dict[state]['dates'][-1]

df=pd.DataFrame()
df['state']=csv_state
df['dates']=csv_dates
df['retail']=csv_retail
df['grocery']=csv_grocery
df['parks']=csv_parks
df['transit']=csv_transit
df['workplace']=csv_workplace
df['residential']=csv_residential
df['average_mobility']=csv_average_mobility
df.fillna(method='ffill')
df.to_csv('mobility.csv',index=False)

from datetime import datetime
import json
india_dict['datetime']=str(datetime.now())
mobility_json_indented = json.dumps(india_dict, indent = 4)
mobility_json = json.dumps(india_dict)
print("Complete")
with open("india_mobility_indented.json", "w") as outfile: 
    outfile.write(simplejson.dumps(india_dict,ignore_nan=True,indent=4))

with open("india_mobility.json", "w") as outfile: 
    outfile.write(simplejson.dumps(india_dict,ignore_nan=True))