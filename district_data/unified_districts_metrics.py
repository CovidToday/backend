#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install wget
#!pip install urllib3


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from subprocess import call
from scipy.stats.distributions import gamma,lognorm
import json
import wget
import os
import os.path
from datetime import datetime
import pytz
from collections import OrderedDict
#from google.colab import drive
import math

from datetime import datetime,timedelta
from urllib.request import urlopen
import collections
import copy
#os.chdir('/content/gdrive/My Drive')
#drive.mount('/content/gdrive')


# In[ ]:


if os.path.exists("test.json"):
  os.remove("test.json")
wget.download('https://api.covid19india.org/v4/data-all.json', os.path.join(os.getcwd(),"test.json"))


# In[ ]:





# In[ ]:


def convert(dat):
    return datetime.strptime(dat, '%Y-%m-%d').strftime('%d %B')


# In[ ]:


dataset=pd.read_csv('population_districts.csv')
population=pd.DataFrame()
population["District"]=dataset['District']
population["Population"]=dataset['Population']
population = population.set_index('District')
population


# In[ ]:


d={}
for i in dataset['State_Code'].unique():
    d[i] = [dataset['District'][j] for j in dataset[dataset['State_Code']==i].index]


# In[ ]:


state_id = d
x=datetime.now(pytz.timezone('Asia/Kolkata')).date()
dd=pd.date_range(start="2020-01-30",end=x)
dates=[]
for i in range(len(dd)):
  dates.append((str(dd[i])[:10]))
#dates
dates1=[]
for w in range (len(dates)):
  if len(dates[w]):
    dates1.append(convert(dates[w]))


# In[ ]:


{
  "MH":["Mumbai", "Thane", "Pune", "Palghar", "Aurangabad"],
  "TN":["Chennai", "Chengalpattu"],
  "KA":["Bengaluru Urban"],
  "GJ":["Ahmedabad", "Surat"],
  "WB":["Kolkata"],
  "HR":["Gurugram"],
  "TG":["Hyderabad"],
}


# In[ ]:


'''
from datetime import timedelta
start=datetime.now()
x1=datetime.now(pytz.timezone('Asia/Kolkata')).date()
#x1 = datetime.today()
#y1 = timedelta(days=7)
y1=[]
x1=str(x1)[:10]
for i in range(7,0,-1):
  y1.append(str(datetime.today()-timedelta(days=i))[:10])
#print(y1)
##y1=str(y1)[:10]
t=y1
t
'''
def dates_gen(periods=7):
  t = pd.Series(pd.date_range(end = datetime.now(pytz.timezone('Asia/Kolkata'))-timedelta(1), periods = periods)).dt.strftime('%Y-%m-%d').tolist()

  return t


# In[ ]:


t = dates_gen()


# # Positivity Rate (All metrics)

# ## From the begining

# In[ ]:


start=datetime.now()
states={}
csv_dates=[]
csv_states=[]
csv_total_cases=[]
csv_cum_recovered=[]
csv_daily_recovered=[]
csv_cum_deceased=[]
csv_daily_deceased=[]
csv_positivity_rate_cumulative=[]
csv_daily_positive_cases=[]
csv_daily_positivity_rate=[]
csv_daily_positive_cases_ma=[]
csv_daily_positivity_rate_ma=[]
csv_test_per_million=[]
csv_daily_tested=[]
csv_cum_tested=[]

csv_daily_case_per_million = []
csv_daily_test_per_million = []
csv_daily_test_ma = []
csv_daily_deceased_ma = []

test=json.load(open('test.json'))


for j in state_id.keys():
  for k in state_id[j]:
    test_per_million = ['']*len(dates)
    pos_cum = ['']*len(dates)
    pos_rate_cum = ['']*len(dates)
    daily_pos = ['']*len(dates)
    daily_pos_ma = ['']*len(dates)
    daily_tested = ['']*len(dates)
    daily_pos_rate = ['']*len(dates)
    daily_pos_rate_ma = ['']*len(dates)
    tested_cum = ['']*len(dates)
    tested_daily = ['']*len(dates)
    deceased_cum = ['']*len(dates)
    daily_deceased = ['']*len(dates)
    recovered_cum = ['']*len(dates)
    daily_recovered = ['']*len(dates)


    daily_case_per_million = ['']*len(dates)
    daily_test_per_million = ['']*len(dates)
    daily_test_ma = ['']*len(dates)
    daily_deceased_ma = ['']*len(dates)

    for i in range(len(dates)):

      if dates[i] in test.keys():
          temp=test[dates[i]]
          if j in temp.keys():

            if 'districts' in temp[j].keys():

              if k in temp[j]['districts']:

                if 'total' in temp[j]['districts'][k].keys():

                  if 'confirmed' in temp[j]['districts'][k]['total'].keys():

                    pos_cum[i]=temp[j]['districts'][k]['total']['confirmed']

                  if 'tested' in temp[j]['districts'][k]['total'].keys():
                    tested_cum[i]=abs(temp[j]['districts'][k]['total']['tested'])
                    test_per_million[i]=temp[j]['districts'][k]['total']['tested']*1000000/int(population["Population"][k])

                  if 'deceased' in temp[j]['districts'][k]['total'].keys():
                    deceased_cum[i]=temp[j]['districts'][k]['total']['deceased']

                  if 'recovered' in temp[j]['districts'][k]['total'].keys():
                    recovered_cum[i]=temp[j]['districts'][k]['total']['recovered']

                  if len(str(pos_cum[i])) and len(str(tested_cum[i])):
                    pos_rate_cum[i]= pos_cum[i]*100/tested_cum[i]


                if 'delta' in temp[j]['districts'][k].keys():
                  if 'confirmed' in temp[j]['districts'][k]['delta'].keys():
                    daily_pos[i]=temp[j]['districts'][k]['delta']['confirmed']
                    try:
                      daily_case_per_million[i] =temp[j]['delta']['confirmed']*1000000/int(population["Population"][k])   #New
                    except:
                      daily_case_per_million[i]= ''
                  if 'tested' in temp[j]['districts'][k]['delta'].keys():
                    daily_tested[i]=abs(temp[j]['districts'][k]['delta']['tested'])
                    try:
                      daily_test_per_million[i] = temp[j]['delta']['tested']*1000000/int(population["Population"][k])    #New
                    except:
                      daily_test_per_million[i] = ''
                  if 'deceased' in temp[j]['districts'][k]['delta'].keys():
                    daily_deceased[i]=temp[j]['districts'][k]['delta']['deceased']

                  if 'recovered' in temp[j]['districts'][k]['delta'].keys():
                    daily_recovered[i]=temp[j]['districts'][k]['delta']['recovered']

                  if len(str(daily_pos[i])) and len(str(daily_tested[i])):
                    daily_pos_rate[i]=int(daily_pos[i])*100/int(daily_tested[i])



    for w in range(7,len(daily_pos)):
                  sum1=0
                  sum2=0
                  for s in range(7):
                    if (len(str(daily_pos[w-s]))!=0 and len(str(daily_tested[w-s]))!=0):
                      sum1+=int(daily_pos[w-s])
                      sum2+=int(daily_tested[w-s])
                  if (sum2!=0):
                    daily_pos_rate_ma[w]=sum1*100/abs(sum2)

    for w in range(7,len(daily_pos)):
                  sum1=0
                  count=0
                  for s in range(7):
                    if (len(str(daily_pos[w-s]))!=0):
                      sum1+=int(daily_pos[w-s])
                      count+=1
                  if count!=0:
                    daily_pos_ma[w]=sum1/count


    for w in range(7,len(daily_tested)):
      sum1=0
      count=0
      for s in range(7):
        if (len(str(daily_tested[w-s]))!=0):
          sum1+=int(daily_tested[w-s])

          count+=1
      if count!=0:
        daily_test_ma[w]=sum1/count


    for w in range(7,len(daily_deceased)):
      sum1=0
      count=0
      for s in range(7):
        if (len(str(daily_deceased[w-s]))!=0):
          sum1+=int(daily_deceased[w-s])
          count+=1
      if count!=0:
        daily_deceased_ma[w]=sum1/count



    #print(daily_pos_rate[-15:],k)

    for i in range(len(dates)-1):
                  csv_dates.append(dates1[i])
                  csv_states.append(k)
                  csv_total_cases.append(pos_cum[i])
                  csv_positivity_rate_cumulative.append(pos_rate_cum[i])
                  csv_daily_positive_cases.append(daily_pos[i])
                  csv_cum_recovered.append(recovered_cum[i])
                  csv_daily_recovered.append(daily_recovered[i])
                  csv_cum_deceased.append(deceased_cum[i])
                  csv_daily_deceased.append(daily_deceased[i])
                  csv_daily_positivity_rate.append(daily_pos_rate[i])
                  csv_daily_positive_cases_ma.append(daily_pos_ma[i])
                  csv_daily_positivity_rate_ma.append(daily_pos_rate_ma[i])
                  csv_daily_tested.append(daily_tested[i])
                  csv_cum_tested.append(tested_cum[i])
                  csv_test_per_million.append(test_per_million[i])


                  csv_daily_case_per_million.append(daily_case_per_million[i])
                  csv_daily_test_per_million.append(daily_test_per_million[i])
                  csv_daily_test_ma.append(daily_test_ma[i])
                  csv_daily_deceased_ma.append(daily_deceased_ma[i])

    states[k]={
                                  'dates':dates1[:-1],
                                  'cum_positive_cases':pos_cum[:-1],
                                  'cum_positivity_rate':pos_rate_cum[:-1],
                                  'daily_positive_cases':daily_pos[:-1],
                                  'cum_recovered':recovered_cum[:-1],
                                  'daily_recovered':daily_recovered[:-1],
                                  'cum_deceased':deceased_cum[:-1],
                                  'daily_deceased':daily_deceased[:-1],
                                  'daily_positivity_rate':daily_pos_rate[:-1],
                                  'daily_positive_cases_ma': daily_pos_ma[:-1],
                                  'daily_positivity_rate_ma':daily_pos_rate_ma[:-1] ,
                                  'daily_tests': daily_tested[:-1],
                                  'cum_tests': tested_cum[:-1],
                                  'test_per_million':test_per_million[:-1],
                                  'daily_cases_per_million':daily_case_per_million[:-1],
                                  'daily_tests_per_million':daily_test_per_million[:-1],
                                  'daily_tests_ma':daily_test_ma[:-1],
                                  'daily_deceased_ma':daily_deceased_ma[:-1]
                            }
end=datetime.now()
print(end-start)


# In[ ]:


dates1


# ## Append Method

# In[ ]:


'''
csv_dates=[]
csv_states=[]
csv_total_cases=[]
csv_cum_recovered=[]
csv_daily_recovered=[]
csv_cum_deceased=[]
csv_daily_deceased=[]
csv_positivity_rate_cumulative=[]
csv_daily_positive_cases=[]
csv_daily_positivity_rate=[]
csv_daily_positive_cases_ma=[]
csv_daily_positivity_rate_ma=[]
csv_test_per_million=[]
csv_daily_tested=[]
csv_cum_tested=[]

#New
csv_daily_case_per_million = []
csv_daily_test_per_million = []
csv_daily_test_ma = []
csv_daily_deceased_ma = []

temp1 = json.load(open('positivity_Rate_dist.json'))

test_json_url = 'https://api.covid19india.org/v3/data-all.json'
test_json = json.loads(urlopen(test_json_url).read())
test= test_json


for x in t:
  temp = test[x]

  states={}
  for j in state_id.keys():
    for k in state_id[j]:

      test_per_million = temp1[k]['test_per_million']
      pos_cum = temp1[k]['cum_positive_cases']
      pos_rate_cum = temp1[k]['cum_positivity_rate']
      daily_pos = temp1[k]['daily_positive_cases']
      daily_pos_ma = temp1[k]['daily_positive_cases_ma']
      daily_pos_rate = temp1[k]['daily_positivity_rate']
      daily_pos_rate_ma = temp1[k]['daily_positivity_rate_ma']
      tested_cum = temp1[k]['cum_tests']
      daily_tested = temp1[k]['daily_tests']
      deceased_cum = temp1[k]['cum_deceased']
      daily_deceased = temp1[k]['daily_deceased']
      recovered_cum = temp1[k]['cum_recovered']
      daily_recovered = temp1[k]['daily_recovered']

      #New added
      daily_case_per_million  = temp1[k]['daily_cases_per_million']
      daily_test_per_million  = temp1[k]['daily_tests_per_million']
      daily_test_ma  = temp1[k]['daily_tests_ma']
      daily_deceased_ma  = temp1[k]['daily_deceased_ma']

      dates=temp1[k]['dates']
      if convert(x) not in dates :
        print(1)
        dates.append(convert(x))
        test_per_million.append('')
        pos_cum.append('')
        pos_rate_cum.append('')
        daily_pos.append('')
        daily_pos_ma.append('')
        daily_pos_rate.append('')
        daily_pos_rate_ma.append('')
        tested_cum.append('')
        daily_tested.append('')
        deceased_cum.append('')
        daily_deceased.append('')
        recovered_cum.append('')
        daily_recovered.append('')
        i=len(dates)-1

      for l in range(len(dates)):
        if convert(x)==dates[l]:
          i=l
          break

      if dates[i] in test.keys():
          temp=test[dates[i]] #New
          # Previoustemp=json.load(open('test.json'))[dates[i]]
          if j in temp.keys():
            if 'districts' in temp[j].keys():
              if k in temp1.keys():
                  if 'total' in temp[j]['districts'][k].keys():
                    if 'confirmed' in temp[j]['districts'][k]['total'].keys():
                      pos_cum[i]=temp[j]['districts'][k]['total']['confirmed']

                    if 'tested' in temp[j]['districts'][k]['total'].keys():
                      tested_cum[i]=abs(temp[j]['districts'][k]['total']['tested'])
                      test_per_million[i]=temp[j]['districts'][k]['total']['tested']*1000000/int(population["Population"][k])

                    if 'deceased' in temp[j]['districts'][k]['total'].keys():
                      deceased_cum[i]=temp[j]['districts'][k]['total']['deceased']

                    if 'recovered' in temp[j]['districts'][k]['total'].keys():
                      recovered_cum[i]=temp[j]['districts'][k]['total']['recovered']

                    if len(str(pos_cum[i])) and len(str(tested_cum[i])):
                      pos_rate_cum[i]= pos_cum[i]*100/tested_cum[i]

                  if 'delta' in temp[j].keys():
                    if 'confirmed' in temp[j]['districts'][k]['delta'].keys():
                      daily_pos[i]=temp[j]['districts'][k]['delta']['confirmed']
                      try:
                        daily_case_per_million[i] =temp[j]['delta']['confirmed']*1000000/int(population["Population"][k])   #New
                      except:
                        daily_case_per_million[i]= ''

                    if 'tested' in temp[j]['districts'][k]['delta'].keys():
                      daily_tested[i]=abs(temp[j]['districts'][k]['delta']['tested'])
                      try:
                        daily_test_per_million[i] = temp[j]['delta']['tested']*1000000/int(population["Population"][k])    #New
                      except:
                        daily_test_per_million[i] = ''

                    if 'deceased' in temp[j]['districts'][k]['delta'].keys():
                      daily_deceased[i]=temp[j]['districts'][k]['delta']['deceased']

                    if 'recovered' in temp[j]['districts'][k]['delta'].keys():
                      daily_recovered[i]=temp[j]['districts'][k]['delta']['recovered']

                    if len(str(daily_pos[i])) and len(str(daily_tested[i])):
                      daily_pos_rate[i]=int(daily_pos[i])*100/int(daily_tested[i])

      for w in range(7,len(daily_pos)):
        sum1=0
        sum2=0
        for s in range(7):
          if (len(str(daily_pos[w-s]))!=0 and len(str(daily_tested[w-s]))!=0):
            sum1+=int(daily_pos[w-s])
            sum2+=int(daily_tested[w-s])
        if (sum2!=0):
          daily_pos_rate_ma[w]=sum1*100/abs(sum2)

      for w in range(7,len(daily_pos)):
        sum1=0
        count=0
        for s in range(7):
          if (len(str(daily_pos[w-s]))!=0):
            sum1+=int(daily_pos[w-s])
            count+=1
        if count!=0:
          daily_pos_ma[w]=sum1/count

      #New
      for w in range(7,len(daily_tested)):
        sum1=0
        count=0
        for s in range(7):
          if (len(str(daily_tested[w-s]))!=0):
            sum1+=int(daily_tested[w-s])

            count+=1
        if count!=0:
          daily_test_ma[w]=sum1/count

      #New
      for w in range(7,len(daily_deceased)):
        sum1=0
        count=0
        for s in range(7):
          if (len(str(daily_deceased[w-s]))!=0):
            sum1+=int(daily_deceased[w-s])
            count+=1
        if count!=0:
          daily_deceased_ma[w]=sum1/count


      st=k
      for i in range(len(dates)):

          csv_dates.append(dates[i])
          csv_states.append(st)
          csv_total_cases.append(pos_cum[i])
          csv_positivity_rate_cumulative.append(pos_rate_cum[i])
          csv_daily_positive_cases.append(daily_pos[i])
          csv_cum_recovered.append(recovered_cum[i])
          csv_daily_recovered.append(daily_recovered[i])
          csv_cum_deceased.append(deceased_cum[i])
          csv_daily_deceased.append(daily_deceased[i])
          csv_daily_positivity_rate.append(daily_pos_rate[i])
          csv_daily_positive_cases_ma.append(daily_pos_ma[i])
          csv_daily_positivity_rate_ma.append(daily_pos_rate_ma[i])
          csv_daily_tested.append(daily_tested[i])
          csv_cum_tested.append(tested_cum[i])
          csv_test_per_million.append(test_per_million[i])

          #New
          csv_daily_case_per_million.append(daily_case_per_million[i])
          csv_daily_test_per_million.append(daily_test_per_million[i])
          csv_daily_test_ma.append(daily_test_ma[i])
          csv_daily_deceased_ma.append(daily_deceased_ma[i])
      #print(st)

      states[st]={
                      'dates':dates,
                      'cum_positive_cases':pos_cum,
                      'cum_positivity_rate':pos_rate_cum,
                      'daily_positive_cases':daily_pos,
                      'cum_recovered':recovered_cum,
                      'daily_recovered':daily_recovered,
                      'cum_deceased':deceased_cum,
                      'daily_deceased':daily_deceased,
                      'daily_positivity_rate':daily_pos_rate,
                      'daily_positive_cases_ma': daily_pos_ma,
                      'daily_positivity_rate_ma':daily_pos_rate_ma ,
                      'daily_tests': daily_tested,
                      'cum_tests': tested_cum,
                      'test_per_million':test_per_million,

                      #New
                      'daily_cases_per_million':daily_case_per_million,
                      'daily_tests_per_million':daily_test_per_million,
                      'daily_tests_ma':daily_test_ma,
                      'daily_deceased_ma':daily_deceased_ma
                }



states['datetime']=str(datetime.now(pytz.timezone('Asia/Kolkata')))
with open('positivity_Rate_dist.json', 'w') as outfile:
    json.dump(states, outfile,indent=4)'''


# In[ ]:


states['datetime']=str(datetime.now(pytz.timezone('Asia/Kolkata')))
with open('positivity_Rate_dist.json', 'w') as outfile:
    json.dump(states, outfile,indent=4)


# In[ ]:


n_states=0
for i in state_id.values():
  for k in i:
    n_states+=1

n_dates = len(list(test.keys()))

rows = n_states*n_dates


# In[ ]:


rows/36


# In[ ]:


csv_dates[-1]


# In[ ]:


df=pd.DataFrame()

df['dates']=csv_dates[:rows]
df['state']=csv_states[:rows]
df['cum_positive_cases']=csv_total_cases[:rows]
df['cum_positivity_rate']=csv_positivity_rate_cumulative[:rows]
df['cum_recovered']=csv_cum_recovered[:rows]
df['daily_recovered']:csv_daily_recovered[:rows]
df['cum_deceased']=csv_cum_deceased[:rows]
df['daily_deceased']:daily_deceased[:rows]
df['daily_positive_cases']=csv_daily_positive_cases[:rows]
df['daily_positivity_rate']=csv_daily_positivity_rate[:rows]
df['daily_positive_cases_ma']=csv_daily_positive_cases_ma[:rows]
df['daily_positivity_rate_ma']=    csv_daily_positivity_rate_ma[:rows]
df['daily_tests']=csv_daily_tested[:rows]
df['cum_tested']=csv_cum_tested[:rows]
df['test_per_million']=csv_test_per_million[:rows]

#New
df['daily_cases_per_million'] = csv_daily_case_per_million[:rows]
df['daily_tests_per_million'] = csv_daily_test_per_million[:rows]
df['daily_tests_ma'] = csv_daily_test_ma[:rows]
df['daily_deceased_ma'] = csv_daily_deceased_ma[:rows]

df.to_csv('positivity_Rate_dist.csv',index=False)


# In[ ]:


df_to_concat = copy.deepcopy(df)


# In[ ]:


data_recovered = pd.DataFrame()
districts=[]
data_deceased = pd.DataFrame()
data_confirmed = pd.DataFrame()
for s in state_id.keys():
    st=state_id[s]
    districts+=st
    print(st)
    for k in st:
      data_confirmed[k] = np.array(states[k]['daily_positive_cases'])
      data_deceased[k] = np.array(states[k]['daily_deceased'])
      data_recovered[k] = np.array(states[k]['daily_recovered'])


# # CFR

# In[ ]:


def n2z(x):
    x[np.logical_or(np.isnan(x),np.isinf(x))] = 0
    return x


# In[ ]:


len(dates)


# In[ ]:


data_recovered = data_recovered.replace(r'^\s*$', np.NaN, regex=True).fillna(0)
data_recovered = data_recovered.astype(np.int32)
data_confirmed = data_confirmed.replace(r'^\s*$', np.NaN, regex=True).fillna(0)
data_confirmed = data_confirmed.astype(np.int32)
data_deceased = data_deceased.replace(r'^\s*$', np.NaN, regex=True).fillna(0)
data_deceased = data_deceased.astype(np.int32)
data_deceased['date'] = dates[:-1]
data_recovered['date'] = dates[:-1]
data_confirmed['date'] = dates[:-1]


# In[ ]:


json_data={}
cfr = pd.DataFrame()
final=pd.DataFrame()
for st in districts:
    print("cfr() -- Working : ",st)

    state=st
    boots = 100
    conf = []
    for n in range(boots):
        #print("Iteration: ",n+1,end='\r')
        if n  == boots//4:
          print("Progress : 25%")
        if n  == boots//2:
          print("Progress : 50%")
        if n  == (boots*3)//4:
          print("Progress : 75%")
        if n  == boots-1:
          print("Progress : 100%")

        dataset = np.copy(data_confirmed[state].values)
        mean = 13.0+(20.9-8.7)/4*np.random.normal()
        sd = 12.7+(26.0-6.4)/4*np.random.normal()
        phi = np.sqrt(sd**2 + mean**2)
        mu = np.log(mean**2/phi)
        sigma = np.sqrt(np.log(phi**2/mean**2))
        L = lognorm(s=sigma,scale=np.exp(mu))
        for i in range(len(dataset)-1,-1,-1):
            send_forward = np.round(L.rvs(np.max([dataset[i],0])))
            send_forward = send_forward[i+send_forward<len(dataset)]
            dataset[i] = 0
            for j in np.unique(np.int32(send_forward)):
                dataset[i+j] += np.sum(send_forward==j)
        conf.append(dataset)
    CFR = np.cumsum(data_deceased[state].values)/np.cumsum(conf,axis=1)
    col_mean = np.nanmean(CFR, axis=0)
    inds = np.where(np.isnan(CFR))
    CFR[inds] = np.take(col_mean, inds[1])
    #temp1=list(pd.Series(dates).dt.strftime('%m-%d-%Y'))
    #print(temp1[0])
    temp={}
    temp = {
        'dates':dates1[:-1],
        'cfr1_point':list(n2z(100*np.cumsum(data_deceased[state].values)/np.cumsum(data_confirmed[state].values))),
        'cfr2_point':list(n2z(100*np.cumsum(data_deceased[state].values)/(np.cumsum(data_deceased[state].values)+np.cumsum(data_recovered[state].values)))),
        'cfr3_point':list(n2z(100*np.median(CFR,axis=0))),
        'cfr3_l95':list(n2z(100*np.quantile(CFR,0.025,axis=0))),
        'cfr3_u95':list(n2z(100*np.quantile(CFR,0.975,axis=0))),
        'cfr3_l50':list(n2z(100*np.quantile(CFR,0.25,axis=0))),
        'cfr3_u50':list(n2z(100*np.quantile(CFR,0.75,axis=0))),
        }
    a=st
    #print(a)
    states[state].update(temp)
    json_data[state] = temp
    cfr_state=pd.DataFrame()
    cfr_state['state']=([str(a)]*(len(dates)))[:-1]   #Reminder this method has to change when append method is implemented
    cfr_state['dates']=dates1[:-1]                     #Remove [1:] when append method
    cfr_state['cfr1_point']=(list(100*n2z(np.cumsum(data_deceased[state].values)/np.cumsum(data_confirmed[state].values))))
    cfr_state['cfr2_point']=(list(100*n2z(np.cumsum(data_deceased[state].values)/(np.cumsum(data_deceased[state].values)+np.cumsum(data_recovered[state].values)))))
    cfr_state['cfr3_point']=(list(100*n2z(np.median(CFR,axis=0))))
    cfr_state['cfr3_l95']=(list(100*n2z(np.quantile(CFR,0.025,axis=0))))
    cfr_state['cfr3_u95']=(list(100*n2z(np.quantile(CFR,0.975,axis=0))))
    cfr_state['cfr3_l50']=(list(100*n2z(np.quantile(CFR,0.25,axis=0))))
    cfr_state['cfr3_u50']=(list(100*n2z(np.quantile(CFR,0.75,axis=0))))
    cfr=pd.concat([cfr, cfr_state])



# In[ ]:


cfr.to_csv('cfr_district.csv',index=False)
from datetime import datetime
json_data['datetime']=str(datetime.now())


# In[ ]:


json_data_indented = json.dumps(json_data, indent = 4)
with open("cfr_district.json", "w") as outfile:
    outfile.write(json_data_indented)


# # Doubling Rate

# In[ ]:


def calc_doublingtimes(x):
    vals = []
    for i in range(x.shape[0]):
        for j in range(i+1,x.shape[0]):
            if len(str(x[j])) and len(str(x[i])):
                vals.append(np.log(2)*(j-i)/np.log(int(x[j])/int(x[i])))
    return np.mean(vals),np.mean(vals)-1.96*np.std(vals),np.mean(vals)+1.96*np.std(vals)


# In[ ]:


start=datetime.now()
x=datetime.now(pytz.timezone('Asia/Kolkata')).date()
dd=pd.date_range(start="2020-01-30",end=x)
dd = dd [:-1]
datess=[]
for i in range(len(dd)):
  datess.append((str(dd[i])[:10]))


# In[ ]:


stt=states


# In[ ]:


dates1 = dates[:-1]
json_data={}
test=json.load(open('test.json'))
for j in state_id.keys():
    cumul=['']*len(dates)
    #st=state_id[j]
    for st in state_id[j]:
        #print(st)
        cumul=states[st]['cum_positive_cases']
        cumul_cases=np.array(cumul)
        dbt = np.zeros((3,cumul_cases.shape[0]))
        for i in range(cumul_cases.shape[0]):
            dbt[:,i] = calc_doublingtimes(cumul_cases[i-7:i])
        #st=state_id[j]
        #temp={}
        temp1 = {'dates':dates1,'dbt_point':pd.Series((list(dbt[0,:]))).replace([np.inf, -np.inf], np.nan).fillna('').tolist(),'dbt_l95':pd.Series((list(dbt[1,:]))).replace([np.inf, -np.inf], np.nan).fillna('').tolist(),'dbt_u95':pd.Series((list(dbt[2,:]))).replace([np.inf, -np.inf], np.nan).fillna('').tolist()}
        states[st].update(temp1)
        json_data[st] = temp1


# In[ ]:


json_data_indented = json.dumps(json_data, indent = 4)
with open("doubling_rate_dist.json", "w") as outfile:
    outfile.write(json_data_indented)


# # RT

# In[ ]:


rt_json = {}

rt = pd.DataFrame()
for j in state_id.keys():
  for st in state_id[j]:
    state=st
    print("Working : ",state)

    temp = pd.DataFrame()
    #temp["active"] = data_confirmed[state]
    temp["active"] = np.array(data_confirmed[state]).clip(0).tolist()

    temp.to_csv('confirmed.csv')
    call(['RScript.exe','scripts/Rt_analysis_newGT_TJ.R'])

    values = {
            'rt_point':[],
            'rt_sd':[],
            'rt_l95':[],
            'rt_u95':[],
            'rt_l50':[],
            'rt_u50':[],
            't_end':[]
            }

    for df in [pd.read_csv('rt_temp/'+temp) for temp in os.listdir('rt_temp/')]:
        values['rt_point'].append(df['Mean(R)'])
        values['rt_sd'].append(df['Std(R)'])
        values['rt_l95'].append(df['Quantile.0.025(R)'])
        values['rt_u95'].append(df['Quantile.0.975(R)'])
        values['rt_l50'].append(df['Quantile.0.25(R)'])
        values['rt_u50'].append(df['Quantile.0.75(R)'])
        values['t_end'].append(df['t_end']-1)
    for i in values:
        values[i] = np.median(values[i],axis=0)
    values['dates'] = list(data_confirmed['date'][values['t_end']-1])
    rt_state=pd.DataFrame()
    rt_state['state']=[str(state)]*len(values['dates'])
    rt_state['dates']= values['dates']
    rt_state['rt_point'] = values['rt_point']
    rt_state['rt_sd'] = values['rt_sd']
    rt_state['rt_l95'] = values['rt_l95']
    rt_state['rt_u95'] = values['rt_u95']
    rt_state['rt_l50'] = values['rt_l50']
    rt_state['rt_u50'] = values['rt_u50']
    rt=pd.concat([rt, rt_state])

    rt_json[st] = values



# In[ ]:


for st in state_id.keys():
    dist = state_id[st]
    for district in dist:
        states[district].update(rt_json[district])


# In[ ]:


rt.to_csv('rt.csv',index=False)


# ## Rt shifting

# In[ ]:


def shift_rt_metrics(dict,key,days):
  values_shifted = collections.deque(dict[key])
  values_shifted.rotate(-1*days)

  new_val = list(values_shifted)

  size = len(dict['dates'])

  for i in range(days):
    new_val[size-1-i]=''

  return new_val



# In[ ]:


rt_json_shifted = copy.deepcopy(rt_json)
days = 2
for sta in state_id.keys():
    for st in state_id[sta]:
        rt_json_shifted[st]['rt_point'] = shift_rt_metrics(rt_json[st],'rt_point',days)
        rt_json_shifted[st]['rt_sd'] = shift_rt_metrics(rt_json[st],'rt_sd',days)
        rt_json_shifted[st]['rt_l95'] = shift_rt_metrics(rt_json[st],'rt_l95',days)
        rt_json_shifted[st]['rt_u95'] = shift_rt_metrics(rt_json[st],'rt_u95',days)
        rt_json_shifted[st]['rt_l50'] = shift_rt_metrics(rt_json[st],'rt_l50',days)
        rt_json_shifted[st]['rt_u50'] = shift_rt_metrics(rt_json[st],'rt_u50',days)
        rt_json_shifted[st]['t_end'] = shift_rt_metrics(rt_json[st],'t_end',days)


# In[ ]:


for st in state_id.keys():
    dist = state_id[st]
    leng = len(dates[:-1])

    #states[state]['dates'] =  temp1['India']['dates']
    for state in dist:
        for keys in list(rt_json_shifted[state].keys())[:-1]:
            if len(rt_json_shifted[state][keys])<leng:
                rt_json_shifted[state][keys].extend(['' for i in range(leng-len(rt_json_shifted[state][keys]))])

        rt_json_shifted[state]['dates'] = dates[:-1]


# In[ ]:


states_shifted = copy.deepcopy(states)

for sta in state_id.keys():
    for st in state_id[sta]:
        states_shifted[st].update(rt_json_shifted[st])


# In[ ]:


for sta in state_id.keys():
    for state in state_id[sta]:
        for key in rt_json[state].keys():
          try:
            rt_json[state][key]=rt_json[state][key].tolist()
          except:
            pass


# In[ ]:


for sta in state_id.keys():
    for state in state_id[sta]:
        for key in states[state].keys():
          try:
            states[state][key]=states[state][key].tolist()
          except:
            pass


# In[ ]:


for st in state_id.keys():
    dist = state_id[st]

    leng = len(dates[:-1])

        #states[state]['dates'] =  temp1['India']['dates']
    for state in dist:
        for keys in list(states[state].keys())[1:]:
            if len(states[state][keys])<leng:
                states[state][keys].extend(['' for i in range(leng-len(states[state][keys]))])


# In[ ]:


for st in state_id.keys():
    dist = state_id[st]
    leng = len(dates[:-1])

    #states[state]['dates'] =  temp1['India']['dates']
    for state in dist:
         for keys in list(states_shifted[state].keys())[1:]:
            if len(states_shifted[state][keys])<leng:
                states_shifted[state][keys].extend(['' for i in range(leng-len(states_shifted[state][keys]))])


# In[ ]:


for sta in state_id.keys():
    for st in state_id[sta]:
        states[st]['dates'] = dates[:-1]
        states_shifted[st]['dates'] = dates[:-1]


# ## Rt changes for review

# In[ ]:


with open('rt_shifted.json', 'w') as outfile:
  json.dump(rt_json_shifted, outfile,indent=4)


# In[ ]:


with open('rt.json', 'w') as outfile:
  json.dump(rt_json, outfile,indent=4)


# In[ ]:


'''
df_list = [df,cfr,rt]
all_dataframes = pd.concat(df_list)
all_dataframes.to_csv('complete_districts_all_metrics.csv',index=False)'''


# In[ ]:


len(dates)


# In[ ]:





# In[ ]:


rt_graph = copy.deepcopy(rt_json_shifted)

de =10

for s in state_id.keys():
    for st in state_id[s]:
        for k in rt_json_shifted[st].keys():
            rt_graph[st][k] = rt_json_shifted[st][k][:-10]


# In[ ]:


with open('rt_graph.json', 'w') as outfile:
  json.dump(rt_graph, outfile,indent=4)


# # Complete

# In[ ]:


cols=list(states['Mumbai'].keys())
q=['state']
complete=pd.DataFrame(columns=q+cols)
keys=list(states.keys())[:-1]
for i in keys:
  temp=pd.DataFrame()
  d=len(states['Mumbai']['dates'])

  temp['state']=[str(i)]*d

  for j in cols:
    print(i,j)
    temp[j]=list(states[i][j])[:d]
  complete = pd.concat([complete,temp])


# In[ ]:


cols=list(states_shifted['Mumbai'].keys())
q=['state']

complete_shifted=pd.DataFrame(columns=q+cols)

keys=list(states_shifted.keys())[:-1]

for i in keys:
  temp=pd.DataFrame()
  d=len(states_shifted['Mumbai']['dates'])
  temp['state']=[str(i)]*d

  for j in cols:
    print(i,j)
    temp[j]=list(states_shifted[i][j])

  complete_shifted = pd.concat([complete_shifted,temp])


# In[ ]:


complete[complete['state']=='Ahmedabad']


# In[ ]:


complete.to_csv('complete_districts.csv',index=False)


# In[ ]:


complete_shifted.to_csv('allmetrics_districts.csv',index=False)


# In[ ]:


states_indented = json.dumps(states, indent = 4)
with open("covidtoday_dist.json", "w") as outfile:
    outfile.write(states_indented)


# In[ ]:


states_indented = json.dumps(states_shifted, indent = 4)
with open("allmetrics_districts.json", "w") as outfile:
    outfile.write(states_indented)


# In[ ]:





# In[ ]:
