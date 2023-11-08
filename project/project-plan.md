# Project Plan

## Title

Analyzing the impact of environmental factors on public health

## Main Question

1. Do air quality metrics (such as PM2.5 and PM10) and the number of tuberculosis cases in the region have a statistically significant relationship?
2. Is there a vulnerable population that is particularly vulnerable to the effects of poor air quality on tuberculosis risk, such as age groups or those with pre-existing health disorders, and how can this knowledge guide public health interventions?
3. What are the potential peaks for tuberculosis incidence in connection to air quality, and how does the relationship between air quality and tuberculosis cases change throughout different geographic locations within the region?

## Description

This data science project aims to explore the relationship between hospital data of tuberculosis patients in a region and that region's air quality data. Analyzing such data can provide valuable insights into potential correlations and factors that might influence the spread of tuberculosis.

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

## Work Packages

1. Clean and explore data: Clean data from the two data sources, ensuring they are in a compatible format and explore the data to gain insights on the hospital patient and air quality of the region. [i1]

2. Data should be same timeframe and region: Compare the same patient and air quality data with the same timeframe and region. [i2]

3. Insight of air quality matrics: Analyze the air quality matrics (such as PM2.5 and PM10) are they enough to find the relation between the environment and public health. [i3]
 

[i1] : https://github.com/5aad/made-template/issues/1
[i2] : https://github.com/5aad/made-template/issues/2
[i3] : https://github.com/5aad/made-template/issues/3
