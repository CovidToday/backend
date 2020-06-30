# Covid Today | www.covidtoday.in 
## Tracking India's progress through the coronavirus epidemic. 
<br/>
<br/>
<p align="center"><img src="https://github.com/CovidToday/backend/blob/master/poster.png?raw=true" width='80%'></p>
<br/>
**Latest datasets and API: https://github.com/CovidToday/indicator-dataset<br/>
Backend repo: https://github.com/CovidToday/backend<br/>
Frontend repo: https://github.com/CovidToday/FrontEnd<br/>
How to start contributing: [CONTRIBUTING.md](CONTRIBUTING.md)**
<br/>
<br/>
<br/>
*As I write this, there is an eerie feeling that tells me that there are enough dashboards tracking COVID-19 in India. But none, like this one. Read me and join in if you find this worth something.*
<br/>
## The Concept 
It is beyond doubt that reckless relaxation of public health measures and social distancing can have a devastating effect in the form of a rapid rise in COVID-19 cases and deaths. **Relaxation of control measures and return to normal social life must happen in a phased manner, based on continous tracking of public health metrics.** [(WHO,](https://www.who.int/publications/i/item/public-health-criteria-to-adjust-public-health-and-social-measures-in-the-context-of-covid-19)[ CDC)](https://www.cdc.gov/coronavirus/2019-ncov/downloads/php/CDC-Activities-Initiatives-for-COVID-19-Response.pdf) These metrics tell us if our hospitals are equipped enough to handle the patient load, whether our testing system is adequate to catch cases, and whether the rate of spread is under control so that public health measures can be optimally adjusted, both spatially and temporally.

### Since no one is tracking these important public health indicators and making them available publicly, we are.

We intend to do this using every bit of publicly available data on COVID-19 in India. We determine public health indicators/metrics across three domains. 
1. **Transmission**: Measures how fast the virus is spreading
```eg: Reproduction Number, Doubling Time, Daily cases...more ```
2. **Testing**: Measures if we are testing enough (Remember, there is no other data without testing)
```eg: Daily tests, Test positivity rate, Tests per million, Contact tracing metrics...more```
3. **Healthcare System**: Measures if our hospitals are ready and how deaths are being prevented 
```eg: Case Fatality Rate (various kinds), Number and occupancy of hospital beds, ICU beds, ventilators, Number of quarantined...```

### Objectives
1. Make a scientifically sound framework which can track the epidemic's progress across multiple relevant domains; based on latest scientific evidence, national advisories and WHO guidance. 
2. Choose appropriate indicators for each domain- Transmission (scale and speed of spread), Testing (testing ramp-up and is it enough), Healthcare system (capacity and outcomes of healthcare). 
3. Integrate required raw data from multiple sources (already existing datasets + de novo data collection).
4. Analyse the raw data through statistically and epidemiologically robust methods to get the desired indicators. 
5. Visualise these indicators in an intuitive and easy-to-understand way on the website, so that people without in-depth knowledge of the topic can understand what we present. 
6. Provide periodical worded analyses of what the numbers show and what that means. We have started that on Twitter (@icart_india), but all ideas are welcome. 
7. Make the indicator datasets publicly available for use by citizens, epidemiologists, researchers, analysts and journalists.

## Open Sourced. Covid Today needs collaborators! 

This project also follows an **'open vision'**, which means although we are committed to the original objectives of the website, we are open to new ideas on how the website/platform can be expanded to better fight the pandemic. 

### Some areas where you can contribute
*Anyone!* Help us gather essential data from the ground-up. Contribute if you can collect any of the following data from your state source:
Number of COVID Care Centres, Dedicated COVID Health Centres and Dedicated COVID Hospitals (hospital beds, ICU beds, ventilators- total and occupied), Number of quarantined, 

*Public health experts, Epidemiologists, Journalists, Medicos!* Help us write short periodical analyses of the numbers we present, exploring and breaking down the trends that lie within and what they mean for the COVID-19 response. Curate insightful analyses on our twitter handle or write on your own platform. 

*Software engineers, Data scientists!* Build and fine-tune the technological backbone. The backend is open sourced on github. Find new issues or have your pick of the existing ones, and help build the code that crunches the numbers and oils the pipeline. We are planning on open sourcing the UI too, get in touch if you want to pitch in.

*Public health experts, Data analysts, Epidemiologists, ML experts, all others!* Build on the concept. Innovate with us on what indicators to show next, how to better present the data for more insightful conclusions, and how to expand the platform to make it more resourceful. We are also exploring the data we see through ML.

**Not on this list? Tell us how you can contribute.**

## How do I start contributing?

**Collaborate on the tech work on Github-** Work on an existing  issue or create a new issue in the repository. <br/>
Do read [CONTRIBUTING.md](CONTRIBUTING.md) to know how to collaborate on Github. <br/>
[Backend repo](https://github.com/CovidToday/backend/issues)- the code which imports, cleans and analyses the data to output various indicators. <br/>
[UI repo](https://github.com/CovidToday/UI/issues)- the code for the website interface and data visualisations<br/>
<br/>
**If you want to collaborate on other stuff-** Fill a short form [here](https://forms.gle/HDCDVYApfRi319k58) (You can report a bug, suggest an improvement, ask a question, or join as a collaborator). You can also get in touch at covidindiatoday@gmail.com
<br/><br/>
Please follow the Code of Conduct this project abides to: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).


## Raw data sources 

Raw data for cases and tests- www.covid19india.org (A brilliant crowdsourced platform which gathers this data from official state bulletins and dashboards)
<br/>Data for mobility index- www.google.com/covid19/mobility
<br/>Population data- www.uidai.gov.in/images/state-wise-aadhaar-saturation.pdf


## About how we calculate the indicators

Visit the Methods page on www.covidtoday.in

Limitations of the method are listed under each indicator. If you have an idea to improve upon them, start an issue in this repo. 




## Project Admins
Mohak (AIIMS Delhi), Rishi (IISER Pune), Pratik (IIIT Hyd; Microsoft), Aditya (VIT Vellore; Barclays), Siddharth (IIIT Gwalior), Apurva (BFCET Bathinda), Abhinav.

## initiative by iCART

India COVID Apex Research Team (iCART) is a volunteer research and development group which comprises professionals and students from multiple fields. We are always open to collaboration with any individual or organisation that shares our interests and vision- *A Science Driven Pandemic Response*. We started as a small group from AIIMS Delhi, and have since grown into a multi-disciplinary team of doctors, biomedical researchers, epidemiologists, students, tech developers and data scientists with the primary focus to act as a catalyst for a science driven response to the COVID-19 pandemic. <br/> 
Our team is engaged in clinical and epidemiological research at some of the best hospitals in the country. In addition, we have developed a comprehensive digital COVID-19 platform spanning across communities, hospitals and laboratories, which is under pilot-testing. <br/> 
<br/> 
You may follow us on Twitter [@icart_india](https://twitter.com/icart_india) where we try to engage in meaningful discussions regarding the COVID-19 epidemic with fellow citizens, experts and journalists.


## inspired by
Multiple projects around the globe that have used data and technology in the war against COVID-19. 
Some of them: www.covidexitstrategy.org, www.covidtracking.com, www.covid19india.org, www.rt.live, www.covid19-projections.com

