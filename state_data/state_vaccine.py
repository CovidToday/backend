#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import wget
import json
import os
import time
from datetime import datetime


# In[2]:


api = "https://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv"

if "cowin_vaccine_data_statewise.csv" in os.listdir("."):
    os.remove("cowin_vaccine_data_statewise.csv")

wget.download(api,"cowin_vaccine_data_statewise.csv")

#dataset=pd.read_csv('https://raw.githubusercontent.com/CovidToday/backend/master/testing-and-cfr/population.csv')
dataset=pd.read_csv('population.csv',index_col='State',usecols=['State','Population'])
population = dataset.T.to_dict()


# In[3]:


use_cols = [
    'Updated On', 'State', 'Total Individuals Vaccinated',
    'Total Sessions Conducted', 'Total Sites ', 'First Dose Administered',
    'Second Dose Administered', 'Male(Individuals Vaccinated)',
    'Female(Individuals Vaccinated)', 'Transgender(Individuals Vaccinated)',
    'Total Covaxin Administered', 'Total CoviShield Administered',
    'Total Individuals Vaccinated', 'Total Doses Administered'
]


# In[4]:


vacc = pd.read_csv("cowin_vaccine_data_statewise.csv")
vacc = vacc[use_cols]

#vacc.loc[313,"State"] = "Andhra Pradesh"

if len(vacc[vacc['State']=='Updated On'])>0:
    for idx in vacc[vacc['State']=='Updated On'].index:
        vacc.loc[idx,'State'] = vacc.loc[idx-1,'State']


# Updated On
# State
# 
# RAW DATA
# 1. Total Individuals Registered - “cum_reg”
# 2. Total Sessions Conducted - “sessions”
# 3. Total Sites - “sites”
# 4. First Dose Administered — “cum_firstdose”
# 5. Second Dose Administered — “cum_seconddose”
# 6. Male(Individuals Vaccinated)- “cum_male”
# 7. Female(Individuals Vaccinated)- “cum_female”
# 8. Transgender(Individuals Vaccinated) — “cum_trans”
# 9. Total Covaxin Administered — “cum_covaxin”
# 10. Total CoviShield Administered — “cum_covishield”
# 11. Total Individuals Vaccinated — Dont pull into our data
# 12. Total Doses Administered — “cum_doses”
# 
# 
# METRICS
# 1. “Daily_doses” = delta of “cum_doses”
# 2. “daily_doses_ma” = 7 day mvg avg of “daily_doses”
# (calculate a 7day moving avg same as we did earlier for daily cases and tests)
# 3. “daily_doses_per_million” = “daily_doses_ma” / population 
# 4. “pct_population_onedose” = “first dose administered”/population
# 5. “pct_population_twodose” (% fully vaccinated) = “second dose administered”/population
# 6. “Pct_population_reg” = “cum_reg”/population
# 7. “Pct_covishield” = “cum_covishield”/ “cum_covaxin”
# 8. “Pct_female” = female/ (female+male+trans)

# In[5]:


def convert_vacc(dat): 
    try:
        return datetime.strptime(dat, '%d/%m/%Y').strftime('%d %B')
    except:
        return datetime.strptime(dat, '%d-%m-%Y').strftime('%d %B')

def get_daily_series(a):
    return [t - s for s, t in zip(a, a[1:])]

def moving_avg(data, window_size=7):
    numbers_series = pd.Series(data)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    return moving_averages_list[window_size - 1:]


# In[6]:


def to_json(df):
    json = {}
    keys = df['State'].unique()
    
    for state in keys:
        sub_df = df[df['State']==state]
        sub_df = sub_df.dropna(axis=0)
        json[state] = {}
        
        # From raw data
        json[state]['dates'] = sub_df['Updated On'].apply(convert_vacc).to_list()
        json[state]['cum_reg'] = list(sub_df['Total Individuals Vaccinated'].iloc[:,0])
        json[state]['sessions'] = list(sub_df['Total Sessions Conducted'])
        json[state]['daily_firstdose'] = list(sub_df['First Dose Administered'])
        json[state]['daily_seconddose'] = list(sub_df['Second Dose Administered'])
        
        male_dose = sub_df['Male(Individuals Vaccinated)']
        female_dose = sub_df['Female(Individuals Vaccinated)'] 
        trans_dose = sub_df['Transgender(Individuals Vaccinated)']
        json[state]['cum_male'] = list(male_dose)
        json[state]['cum_female'] = list(female_dose)
        json[state]['cum_trans'] = list(trans_dose)
        
        '''
        Total Covaxin Administered — “cum_covaxin”
        Total CoviShield Administered — “cum_covishield”
        Total Individuals Vaccinated — Dont pull into our data
        Total Doses Administered — “cum_doses"
        '''
        json[state]['cum_covaxin'] = list(sub_df['Total Covaxin Administered'])
        json[state]['cum_covishield'] = list(sub_df['Total CoviShield Administered'])
        json[state]['cum_doses'] = list(sub_df['Total Doses Administered'])
        
        
        # Derived metrics
        daily_doses = get_daily_series(sub_df['Total Doses Administered'])
        json[state]['daily_doses'] = daily_doses
        
        daily_doses_ma = moving_avg(daily_doses)
        json[state]['daily_doses_ma'] = daily_doses_ma
        
        json[state]['daily_doses_per_million'] = list(np.array(daily_doses_ma)*1000000/population[state]['Population'])
        
        json[state]['pct_population_onedose'] = list(sub_df['First Dose Administered']*100/population[state]['Population'])
        
        seconddose = list(sub_df['Second Dose Administered']*100/population[state]['Population'])
        
        json[state]['pct_population_twodose'] = seconddose
        
        json[state]['pct_population_reg'] = list(sub_df['Total Individuals Vaccinated'].iloc[:,0]*100/population[state]['Population'])
        
        covishield_prop = list(sub_df['Total CoviShield Administered']*100/(sub_df['Total CoviShield Administered']+sub_df['Total Covaxin Administered']))
        json[state]['pct_covishield'] = covishield_prop
        
        #covaxine_prop = list(sub_df['Total Covaxin Administered']/population[state]['Population'])
        #json[state]['pct_covaxine'] = covishield_prop*100
        
        #covishield_prop = list(sub_df['Total Covaxin Administered']/sub_df['Total Doses Administered'])
        #json[state]['covishield_dose_prop'] = list(sub_df['Total Covaxin Administered']/sub_df['Total Doses Administered'])
        
    
        json[state]['pct_female'] = list(female_dose/(male_dose+female_dose+trans_dose))
        
        
    return json


# In[7]:


state_vacc = to_json(vacc)

with open("state_vaccine.json","w") as file:
    json.dump(state_vacc,file)


# In[ ]:




