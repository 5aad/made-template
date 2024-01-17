# Project Plan

## Title
Analyzing the impact of environmental factors on public health (Year 2022)

## Summary and Rationale
This data science project aims to explore the relationship between hospital data of tuberculosis patients and the air quality in a regions of Bavaria and Brandenburg. Analyzing such data can provide valuable insights into potential correlations and
factors that might influence the spread of tuberculosis and compare between two regions.


## Datasources
### Datasource1: Deutchland Hospital Patients 
* Metadata URL: https://www-genesis.destatis.de/genesis/online#astructure
* Data URL: https://www-genesis.destatis.de/genesis/online?operation=abruftabelleBearbeiten&levelindex=0&levelid=1699407973798&auswahloperation=abruftabelleAuspraegungAuswaehlen&auswahlverzeichnis=ordnungsstruktur&auswahlziel=werteabruf&code=23131-0011&auswahltext=&nummer=2&variable=2&name=GES055&werteabruf=Werteabruf#abreadcrumb
* Data Type: csv

The dataset contains information about hospital patients, including their age, region, year of admission, gender, and whether they have confirmed tuberculosis (TB).

### Datasource2: Deutchland Air Quality
* Metadata URL: https://www.umweltbundesamt.de/en/data/air/air-data
* Data URL: https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=1&year=2022&lang=en
* Data Type: csv

The dataset contains information about air quality, including dust particle type, dust particle size and station location.

## Main Questions
1. Do air quality metrics (such as PM2.5 and PM10) and the number of tuberculosis cases in the region have a statistically significant relationship?
2. Is there a vulnerable population that is particularly vulnerable to the effects of poor air quality on tuberculosis risk, such as age groups or those with pre-existing health disorders, and how can this knowledge guide public health interventions?
3. What are the potential peaks for tuberculosis incidence in connection to air quality, and how does the relationship between air quality and tuberculosis cases change throughout different geographic locations within the region?

## Final Report
The final report [here](https://github.com/5aad/made-template/blob/main/project/report.ipynb).