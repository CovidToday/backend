# April-May 2021 district backend updates
<br/>
- Do not pull data for, or run any estimation for following districts (EXCLUSION FILTER: "State_code=AN/GA/TG" OR "District=Unknown")

- Pull data for and run all metrics calculation (except Rt) for 'all' districts (after exluding above). 

- For Rt, only estimate for following districts (RT INCLUSION FILTER: "Cum_cases>=20000" OR "daily_cases>=500)
<br/>
- Pick latest district data from wikipedia, match this compiled data (new population.csv) to covid19india district list. Manually edit population.csv to match with incoming district names. Replace old population.csv in districts_data folder with this new one. 

# district frontend updates
- remove all testing related data 
