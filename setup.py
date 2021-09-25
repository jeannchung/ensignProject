import requests
import json

## print(response.status_code) ##
response = requests.get('https://data.cms.gov/data-api/v1/dataset/3fd78f4b-0a21-4acf-b90c-4fcd7d27d642/data')

## pulls data from mentioned API, formats it into text
data = response.text

## data is extracted, now need to parse data into JSON
data_json = json.loads(data)

# extract data and print using key value format
average = data_json['week_ending']['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time']

## iterate over the list of dataset columns to find the target columns ##
for i in range(len(data_json)):
    if data_json[i]['week_ending']['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time']:
        print("Average:".format*data_json[i]['week_ending'], data_json[i]['percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time'])

