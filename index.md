---
---
.
### Download latest *state-wise* data
**<a href="state_data/allmetrics_states.json" download>JSON</a><br/>
<a href="state_data/allmetrics_states.csv" download>CSV</a>** 
<br/>

### Download latest *district-wise* data 
**<a href="district_data/allmetrics_districts.json" download>JSON</a><br/>
<a href="district_data/allmetrics_districts.csv" download>CSV</a>** <br/><br/>
*We currently provide data for selected hotspot districts only. However, we update our district list periodically to reflect the epidemic spread. The latest list of districts included in our dataset is available [here](https://github.com/CovidToday/backend/blob/master/district_data/population_districts.csv).*
<br/>
<br/>


#### What is in the datasets
##### Indicators

  ###### Transmission indicators
  * dbt_
  * rt_
  * daily_cases_per_million
  
  ###### Testing indicators
  * daily_positivity_rate_ma (7 day weighted moving average or weekly positivity rate)
  * daily_positivity_rate
  * cum_positivity_rate
  * daily_tests_per_million
  * test_per_million 
  
  ###### Mortality indicators
  * cfr1_
  * cfr2_
  * cfr3_
<br/>

##### Raw data and moving averages
  * daily_positive_cases
  * cum_positive_cases
  * daily_positive_cases_ma
  * daily_recovered
  * cum_recovered
  * daily_deceased
  * daily_deceased_ma
  * cum_deceased
  * daily_tests
  * daily_tests_ma
  * cum_tests
<br/>
<br/>


#### Abbreviations used in datasets
* `dbt_` : Doubling time (in days)
* `rt_` : Reproduction number 
* `cfr1_` : Crude case fatality rate or Naïve CFR [Deaths/Total Cases] (%)
* `cfr2_` : Outcome adjusted fatality rate [Deaths/(Recov+Deaths)] - maybe more meaningful because it excludes active cases with yet unknown outcome (%)
* `cfr3_` : Corrected fatality rate or Lag adjusted fatality rate [Deaths/Lag adjusted Cases] - refer to Methods on www.covidtoday.in for method of estimation (%)
<br/>

* `cum_` : cumulative
* `_ma` : moving average
* `_point` : mean/median value 
* `_u95` `_l95` : upper and lower 95% confidence intervals 
<br/><br/><br/>



### Relevant links

#### Main website at [www.covidtoday.in](https://www.covidtoday.in)

* [Intro to contributing on our github](https://github.com/CovidToday/backend/blob/master/CONTRIBUTING.md)<br/> 
* [Feedback/Suggestions](https://docs.google.com/forms/d/e/1GV9Jm2u7rmsCe65wKzPTw5jtS38n2tVEGiQCeadKTrCJ7Kvju7RbPSQ/viewform)<br/>
* Email: [covidtodayindia@gmail.com](mailto:covidtodayindia@gmail.com)<br/>
* Twitter: [@icart_india](https://twitter.com/icart_india)<br/>
* Whatsapp Collaborators group: [Join](https://chat.whatsapp.com/DtxTkQv8LEDD6W64RmItAZ), *kindly message your skills and interests upon joining the group.*
<br/><br/><br/>



### Terms of Use 
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) *CreativeCommons-Attribution-NonCommercial 4.0 International* <br/>
* **This license requires that reusers give credit to the creator. This allows our volunteer team to gain exposure and traction, enabling us to work better and faster. Please see the next bullet point to know our preffered attribution.** It allows reusers to distribute, remix, adapt, and build upon the material in any medium or format. You are welcome to share the website content and visualisations, and run independent analyses using the datasets from COVID TODAY **for public health, educational, and journalistic uses, including any personal, editorial, academic, or research purposes. We also grant permission for any derivative use of this data and website content that supports healthcare or medical research (including institutional use by public health and for-profit organizations), or journalistic usage (by nonprofit or for-profit organizations). Any other commercial use is not permitted under the license, and will require permission from the COVID TODAY team.**
* **Attribute as:** When using Datasets from COVID TODAY, attribute as `COVID-19 Indicators Dataset by www.covidtoday.in`. When using content directly from the Website, attribute as `Covid Today India Dashboard` and provide a link to the website.
* You should not rely on this website for medical advice or guidance. Since we have no control over the publicly available data our analyses are based on, COVID TODAY hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, reliability, completeness, and non-infringement of third party rights.
* These terms and conditions are subject to change. Your use of the Website and Datasets constitutes your acceptance of these terms and conditions and any future modifications thereof.
