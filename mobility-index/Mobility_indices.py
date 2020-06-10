#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(u'pip install wget')


# In[2]:


from __future__ import print_function
from scipy.io import loadmat
from tqdm import tqdm
# from google.colab import drive
import numpy as np
import scipy
import os
import matplotlib.pyplot as plt
import csv
import pandas as pd
import wget
# drive.mount('/content/gdrive')


# In[3]:


wget.download('https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv', os.getcwd()+"//Global_Mobility_Report.csv")


# In[4]:


with open('Global_Mobility_Report.csv', newline='') as f:
    reader = csv.reader(f)
    g_list = list(reader)


# In[5]:


def normalize(arr):
  slope = int(arr[-1])-int(arr[-2])
  return int(arr[-1])+slope


# In[6]:


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


# In[7]:


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
for row in g_list:
  if(row[1]=='India'):
    # print(row)
    if(len(row[2])<1):
      row[2]='India'
    if row[2] not in  india_dict.keys():
      india_dict[row[2]] = {}
    # print(row)
    state = row[2]
    dates = row[4]
    #print(dates)
    retail = row[5]
    grocery = row[6]
    parks = row[7]
    transit = row[8]
    workplace = row[9]
    residential = row[10]
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
      india_dict[state]['workplace'].append(row[9])
      india_dict[state]['retail'].append(row[5])
      india_dict[state]['grocery'].append(row[6])
      india_dict[state]['parks'].append(row[7])
      india_dict[state]['transit'].append(row[8])
      india_dict[state]['residential'].append(row[10])
    temp=[]
    if(len(india_dict[state]['retail'][-1])>0):
      temp.append(int(india_dict[state]['retail'][-1]))
    if(len(india_dict[state]['grocery'][-1])>0):
      temp.append(int(india_dict[state]['grocery'][-1]))
    if(len(india_dict[state]['transit'][-1])>0):
      temp.append(int(india_dict[state]['transit'][-1]))
    if(len(india_dict[state]['workplace'][-1])>0):
      temp.append(int(india_dict[state]['workplace'][-1]))
    count = 0
    sum=0
    for i in temp:
      sum+=i
      count+=1
    if(len(temp)>0):
        avg=sum/count
        india_dict[state]['average_mobility'].append(str(avg))
    else:
        india_dict[state]['average_mobility'].append('')
#     if(len(india_dict[state]['retail'][-1])>0 and len(india_dict[state]['grocery'][-1])>0 and len(india_dict[state]['transit'][-1])>0 and len(india_dict[state]['workplace'][-1])>0 ):
#       avg = (int(india_dict[state]['retail'][-1])+int(india_dict[state]['grocery'][-1])+int(india_dict[state]['transit'][-1])+int(india_dict[state]['workplace'][-1]))/4
#       india_dict[state]['average_mobility'].append(str(avg))  # To change for average
#     else:
#       india_dict[state]['average_mobility'].append('')  # To change for average
    india_dict[state]['dates'].append(convert(row[4]))
    #print(india_dict[state]['dates'])
    
    for i in range(len(india_dict[state]['dates'])):
      csv_state.append(state)
      csv_dates.append(india_dict[state]['dates'][i])
      csv_retail.append(india_dict[state]['retail'][i])
      csv_grocery.append(india_dict[state]['grocery'][i])
      csv_parks.append(india_dict[state]['parks'][i])
      csv_transit.append(india_dict[state]['transit'][i])
      csv_workplace.append(india_dict[state]['workplace'][i])
      csv_residential.append(india_dict[state]['residential'][i])
      csv_average_mobility.append(india_dict[state]['average_mobility'][i])
      
    #print(row[4])3


# In[8]:


df=pd.DataFrame()
df['state']=csv_state
df['csv_dates']=csv_dates
df['csv_retail']=csv_retail
df['csv_grocery']=csv_grocery
df['csv_parks']=csv_parks
df['csv_transit']=csv_transit
df['csv_workplace']=csv_workplace
df['csv_residential']=csv_residential
df['csv_average_mobility']=csv_average_mobility
df.to_csv('mobility.csv',index=False)


# In[9]:


from datetime import datetime
import json
india_dict['datetime']=str(datetime.now())
mobility_json_indented = json.dumps(india_dict, indent = 4)
mobility_json = json.dumps(india_dict)


# In[10]:


with open("india_mobility.json", "w") as outfile: 
    outfile.write(mobility_json)


# In[15]:


with open("india_mobility_indented.json", "w") as outfile: 
    outfile.write(mobility_json_indented)


# In[ ]:




