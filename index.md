# Download 
<br/>
## Latest state-wise data
<a href="state_data/allmetrics_states.json" download>JSON</a>
<a href="state_data/allmetrics_states.csv" download>CSV</a>
<br/>
## Latest district-wise data
<a href="tree/master/district_data/allmetrics_districts.json" download>JSON</a>
<a href="district_data/allmetrics_districts.csv" download>CSV</a>

aa


# How to use the datasets (JSON and CSV)

Dashboard and detailed methods of estimation at www.covidtoday.in <br/>
Contact at covidtodayindia@gmail.com<br/>
Feedback/Contribute at https://forms.gle/HDCDVYApfRi319k58

All dates and times in Indian Standard Time (IST). 

## Getting the indicator(s) you want

The table below is an index of how to find the indicator in our json datsets. 
**The csv files are similarly named and have the same parameters as the json files.** 

In all of the datafiles India’s hierarchy is kept same as of other states
because from the view point of data, the keys for India would be same as any
other state for all indices. The Structure of Json files is as follows- The
first layer of keys has the state name (including India) : e.g. ‘Kerala ,
‘Delhi’, etc. For each state the keys are as follows:

| Json file                    | Key name                 | Indicator obtained                                                                  |
|------------------------------|--------------------------|-------------------------------------------------------------------------------------|
| rt.json                      | dates                    | [DD Month] e.g. ’22 March’                                                     |
|                              | rt_point                 | Rt (Effective reproduction number), Pooled mean                                                                     |
|                              | rt_std                   | Rt, Standard Deviation                                                              |
|                              | rt_l95                   | Rt, lower limit of 95% confidence interval                                          |
|                              | rt_u95                   | Rt, upper limit of 95% confidence interval                                          |
|                              | rt_l50                   | Rt, lower limit of 50% confidence interval                                          |
|                              | rt_u50                   | Rt, upper limit of 50% confidence interval                                          |
|                              | cases_mean               | Estimated number of new symptom onsets on that date (used for calculating Rt), Mean |
|                              | cases_sd                 | Number of new symptom onsets on that date, Standard Deviation                       |
|                              |                          |                                                                                     |
| cfr.json                     | dates                    | [DD Month] e.g. ’22 March’                                                     |
|                              | cfr1_point               | Crude NFR or Naïve CFR [Deaths/Total Cases]                                         |
|                              | cfr2_point               | Outcome adjusted CFR [Deaths/(Recov+Deaths)]                                        |
|                              | cfr3_point               | Corrected CFR or Lag adjusted CFR [Deaths/Lag adjusted Cases]                       |
|                              | cfr3_l95                 | Corrected CFR, lower limit of 95% confidence interval                               |
|                              | cfr3_u95                 | Corrected CFR, upper limit of 95% confidence interval                               |
|                              | cfr3_l50                 | Corrected CFR, lower limit of 50% confidence interval                               |
|                              | cfr3_u50                 | Corrected CFR, upper limit of 50% confidence interval                               |
|                              |                          |                                                                                     |
| positivity_rate.json         | dates                    | [DD Month] e.g. ’22 March’                                                     |
|                              | daily_positivity_rate    | Daily Positivity Rate                                                               |
|                              | daily_positivity_rate_ma | Daily Positivity Rate, 7-day moving average                                         |
|                              | cum_positivity_rate      | Cumulative Positivity Rate                                                          |
|                              | daily_positive_cases     | Number of daily new confirmed cases \*                                              |
|                              | daily_positive_cases_ma  | Number of daily new confirmed cases, 7-day moving average                           |
|                              | cum_positive_cases       | Number of cumulative confirmed cases \*                                             |
|                              | daily_tests              | Number of daily tests done \*                                                       |
|                              | cum_tests                | Number of cumulative tests done \*                                                  |
|                              | test_per_million         | Tests per million population for that state                                         |
|                              |                          |                                                                                     |
| india_mobility_indented.json | dates                    | [DD Month name] e.g. ’22 March’                                                     |
|                              | retail                   | Retail and Recreation Mobility\*\*                                                  |
|                              | grocery                  | Grocery and Pharmacy Mobility\*\*                                                   |
|                              | parks                    | Parks Mobility \*\*                                                                 |
|                              | transit                  | Transit stations Mobility\*\*                                                       |
|                              | workplace                | Workplace Mobility\*\*                                                              |
|                              | residential              | Residential Mobility \*\*                                                           |
|                              | average_mobility         | Average of normalised mobility from Retail, Grocery, Transit, Workplace             |

\*unaltered data from www.covid19india.org, formatted for time-series analysis

\*\*mobility data from www.google.com/covid19/mobility, normalised for weekend
baseline bias
<br/><br/>


To access the data for any of these keys use the following command: **value =
data[‘state’][‘key name’]**

Here data is object where all of the json file is loaded.

eg1. To get daily Rt point estimates for Punjab: **value =
data[‘Punjab’][‘rt_point’]**

eg2. To get daily positivity rate (moving avg) for India: **value =
data[‘India’][‘daily_positive_cases_ma’]**


## API for datasets

| API End Points to get the data                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| rt.json: <https://github.com/CovidToday/indicator-dataset/raw/master/rt.json>                                           |
| cfr.json: <https://github.com/CovidToday/indicator-dataset/raw/master/cfr.json>                                         |
| positivity_Rate.json: <https://github.com/CovidToday/indicator-dataset/raw/master/positivity_Rate.json>                 |
| india_mobility_indented.json: <https://github.com/CovidToday/indicator-dataset/raw/master/india_mobility_indented.json> |


<a href="district_data/allmetrics_districts.json" download>Click to Download</a>
<a href="district_data/allmetrics_districts.csv" download>Click to Download</a>
<a href="state_data/allmetrics_states.json" download>Click to Download</a>
<a href="state_data/allmetrics_states.csv" download>Click to Download</a>



# Terms of Use 
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) CreativeCommnons-Attribution-NonCommercial 4.0 International 
1. **This license requires that reusers give credit to the creator.** It allows reusers to distribute, remix, adapt, and build upon the material in any medium or format. You are welcome to share the website content and visualisations, and run independent analyses using the datasets from COVID TODAY **for public health, educational, and journalistic uses, including any personal, editorial, academic, or research purposes. We also grant permission for any derivative use of this data and website content that supports healthcare or medical research (including institutional use by public health and for-profit organizations), or journalistic usage (by nonprofit or for-profit organizations). All other commercial uses are not permitted under the Creative Commons license, and will require permission from the COVID TODAY team.**
2. If the website or datasets are shared/used, attribution must be provided appropriately. When using Datasets from COVID TODAY, **attribute as "COVID-19 Indicators Dataset by Covid Today"** and provide a link. When using content directly from the Website, attribute as "Covid Today Dashboard" and provide a link.
3. You should not rely on this website for medical advice or guidance. Since we have no control over the publicly available data our analyses are based on, COVID TODAY hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, reliability, completeness, and non-infringement of third party rights.
4. These terms and conditions are subject to change. Your use of the Website and Datasets constitutes your acceptance of these terms and conditions and any future modifications thereof.

