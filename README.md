# Covid Today by iCART <br/>Daily updated datasets for outbreak indicators - India and states 
# How to use the datasets (JSON and CSV)

Dashboard and detailed methods of estimation at www.covidtoday.in <br/>
Contact at covidtodayindia@gmail.com<br/>
Feedback/Contribute at https://forms.gle/HDCDVYApfRi319k58

All dates and times in Indian Standard Time (IST). 

## Getting the indicator(s) you want

To access the data for any of these keys use the following command: **value =
data[‘state’][‘key name’]**

Here data is object where all of the json file is loaded.

eg1. To get daily Rt point estimates for Punjab: **value =
data[‘Punjab’][‘rt_point’]**

eg2. To get daily positivity rate (moving avg) for India: **value =
data[‘India’][‘daily_positive_cases_ma’]**

In all of the datafiles India’s hierarchy is kept same as of other states
because from the view point of data, the keys for India would be same as any
other state for all indices. The Structure of Json files is as follows- The
first layer of keys has the state name (including India) : e.g. ‘Kerala ,
‘Delhi’, etc. For each state the keys are as follows:

| Json file                    | Key name                   | Indicator obtained                                                                  |
|------------------------------|----------------------------|-------------------------------------------------------------------------------------|
| rt.json                      | dates                      | [DD Month name] e.g. ’22 March’                                                     |
|                              | rt_point                   | Rt, Pooled mean                                                                     |
|                              | rt_std                     | Rt, Standard Deviation                                                              |
|                              | rt_l95                     | Rt, lower limit of 95% confidence interval                                          |
|                              | rt_u95                     | Rt, upper limit of 95% confidence interval                                          |
|                              | rt_l50                     | Rt, lower limit of 50% confidence interval                                          |
|                              | rt_u50                     | Rt, upper limit of 50% confidence interval                                          |
|                              | cases_mean                 | Estimated number of new symptom onsets on that date (used for calculating Rt), Mean |
|                              | cases_sd                   | Number of new symptom onsets on that date, Standard Deviation                       |
|                              |                            |                                                                                     |
| cfr.json                     | dates                      | [DD Month name] e.g. ’22 March’                                                     |
|                              | cfr1_point                 | Crude NFR or Naïve CFR [Deaths/Total Cases]                                         |
|                              | cfr2_point                 | Outcome adjusted CFR [Deaths/(Recov+Deaths)]                                        |
|                              | cfr3_point                 | Corrected CFR or Lag adjusted CFR [Deaths/Lag adjusted Cases]                       |
|                              | cfr3_l95                   | Corrected CFR, lower limit of 95% confidence interval                               |
|                              | cfr3_u95                   | Corrected CFR, upper limit of 95% confidence interval                               |
|                              | cfr3_l50                   | Corrected CFR, lower limit of 50% confidence interval                               |
|                              | cfr3_u50                   | Corrected CFR, upper limit of 50% confidence interval                               |
|                              |                            |                                                                                     |
| positivity_rate.json         | dates                      | [DD Month name] e.g. ’22 March’                                                     |
|                              | positivity_rate_cumulative | Cumulative Positivity Rate                                                          |
|                              | daily_positive_cases       | Number of daily new confirmed cases \*                                              |
|                              | daily_positivity_rate      | Daily Positivity Rate                                                               |
|                              | daily_positive_cases_ma    | Number of daily new confirmed cases, 7-day moving average                           |
|                              | daily_positivity_rate_ma   | Daily Positivity Rate, 7-day moving average                                         |
|                              | test_per_million           | Tests per million for that state                                                    |
|                              |                            |                                                                                     |
| india_mobility_indented.json | dates                      | [DD Month name] e.g. ’22 March’                                                     |
|                              | retail                     | Retail and Recreation Mobility\*\*                                                  |
|                              | grocery                    | Grocery and Pharmacy Mobility\*\*                                                   |
|                              | parks                      | Parks Mobility \*\*                                                                 |
|                              | transit                    | Transit stations Mobility\*\*                                                       |
|                              | workplace                  | Workplace Mobility\*\*                                                              |
|                              | residential                | Residential Mobility \*\*                                                           |
|                              | average_mobility           | Average of normalised mobility from Retail, Grocery, Transit, Workplace             |

\*unaltered data from www.covid19india.org, formatted for time-series analysis

\*\*mobility data from www.google.com/covid19/mobility, normalised for weekend
baseline bias

# API for datasets

| API End Points to get the data                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| rt.json: <https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/rt.json>                                           |
| cfr.json: <https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/cfr.json>                                         |
| positivity_Rate.json: <https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/positivity_Rate.json>                 |
| india_mobility_indented.json: <https://raw.githubusercontent.com/CovidToday/CovidToday_Website/master/backend/jsonfiles/india_mobility_indented.json> |


# Terms of Use 

1. You are welcome to share to website content and visualisations, and run analyses using the datasets from COVID TODAY for public health, educational, journalistic and non-commercial uses, including any personal, editorial, academic, or research purposes. Commercial uses are not permitted and will require permission from COVID TODAY.
2. **If the website or datasets are shared/used, attribution must be provided appropriately**. When using datasets from COVID TODAY, attribute as "COVID-19 Outbreak Indicators Dataset by COVID TODAY" and provide a link alongside. When linking to the website, attribute as "COVID TODAY Dashboard" and provide a link alongside. 
3. You should not rely on this website for medical advice or guidance. Since we have no control over the publicly available data our analyses are based on, COVID TODAY hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, reliability, completeness, and non-infringement of third party rights.
4. These terms and conditions are subject to change. Your use of the Website and Datasets constitutes your acceptance of these terms and conditions and any future modifications thereof.

