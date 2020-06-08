**COVID TODAY (covidtoday.in)**

**DATASETS FOR DAILY OUTBREAK INDICATORS – INDIA AND STATES**

**DATA DOCUMENTATION- HOW TO USE THE DATA**

This document has description about all the datasets which can be used for various analytics.

To access the data for any of these keys use the following command: **value = data[&#39;state&#39;][&#39;key name&#39;]**

Here data is object where all of the json file is loaded.

eg1. To get daily Rt point estimates for Punjab: **value = data[&#39;Punjab&#39;][&#39;rt\_point&#39;]**

eg2. To get daily positivity rate (moving avg) for India: **value = data[&#39;India&#39;][&#39;daily\_positive\_cases\_ma&#39;]**

In all of the datafiles India&#39;s hierarchy is kept same as of other states because from the view point of data, the keys for India would be same as any other state for all indices. The Structure of Json files is as follows- The first layer of keys has the state name (including India) : e.g. &#39;Kerala , &#39;Delhi&#39;, etc. For each state the keys are as follows:

| **Json file** | **Key name** | **Indicator obtained** |
| --- | --- | --- |
| **rt.json** | dates | [DD Month name] e.g. &#39;22 March&#39; |
|
 | rt\_point | Rt, Pooled mean |
|
 | rt\_std | Rt, Standard Deviation |
|
 | rt\_l95 | Rt, lower limit of 95% confidence interval |
|
 | rt\_u95 | Rt, upper limit of 95% confidence interval |
|
 | rt\_l50 | Rt, lower limit of 50% confidence interval |
|
 | rt\_u50 | Rt, upper limit of 50% confidence interval |
|
 | cases\_mean | Estimated number of new symptom onsets on that date (used for calculating Rt), Mean
 |
|
 | cases\_sd | Number of new symptom onsets on that date, Standard Deviation |
|
 |
 |
 |
| **cfr.json** | dates | [DD Month name] e.g. &#39;22 March&#39; |
|
 | cfr1\_point | Crude NFR or Naïve CFR [Deaths/Total Cases]
 |
|
 | cfr2\_point | Outcome adjusted CFR [Deaths/(Recov+Deaths)]
 |
|
 | cfr3\_point | Corrected CFR or Lag adjusted CFR [Deaths/Lag adjusted Cases] |
|
 | cfr3\_l95 | Corrected CFR, lower limit of 95% confidence interval
 |
|
 | cfr3\_u95 | Corrected CFR, upper limit of 95% confidence interval
 |
|
 | cfr3\_l50 | Corrected CFR, lower limit of 50% confidence interval
 |
|
 | cfr3\_u50 | Corrected CFR, upper limit of 50% confidence interval |
|
 |
 |
 |
| **positivity\_rate.json** | dates | [DD Month name] e.g. &#39;22 March&#39; |
|
 | positivity\_rate\_cumulative | Cumulative Positivity Rate |
|
 | daily\_positive\_cases | Number of daily new confirmed cases \* |
|
 | daily\_positivity\_rate | Daily Positivity Rate |
|
 | daily\_positive\_cases\_ma | Number of daily new confirmed cases, 7-day moving average |
|
 | daily\_positivity\_rate\_ma | Daily Positivity Rate, 7-day moving average |
|
 | test\_per\_million | Tests per million for that state |
|
 |
 |
 |
| **india\_mobility\_indented.json** | dates | [DD Month name] e.g. &#39;22 March&#39; |
|
 | retail | Retail and Recreation Mobility\*\* |
|
 | grocery | Grocery and Pharmacy Mobility\*\* |
|
 | parks | Parks Mobility \*\* |
|
 | transit | Transit stations Mobility\*\* |
|
 | workplace | Workplace Mobility\*\* |
|
 | residential | Residential Mobility \*\* |
|
 | average\_mobility | Average of normalised mobility from Retail, Grocery, Transit, Workplace |

\*unaltered data from covid19india.org, formatted for time-series analysis

\*\*mobility data from www.google.com/covid19/mobility, normalised for weekend baseline bias

| **The API End Points to get the data** |
| --- |
| **rt.json:** [**https://raw.githubusercontent.com/CovidToday/CovidToday\_Website/master/backend/jsonfiles/rt.json**](https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/rt.json)
 |
| **cfr.json:** [**https://raw.githubusercontent.com/CovidToday/CovidToday\_Website/master/backend/jsonfiles/cfr.json**](https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/cfr.json)
 |
| **positivity\_Rate.json:** [**https://raw.githubusercontent.com/CovidToday/CovidToday\_Website/master/backend/jsonfiles/positivity\_Rate.json**](https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/positivity_Rate.json)
 |
| **india\_mobility\_indented.json:** [**https://raw.githubusercontent.com/CovidToday/CovidToday\_Website/master/backend/jsonfiles/india\_mobility\_indented.json**](https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/india_mobility_indented.json)
 |
