from pandas.core.frame import DataFrame
import requests
import json
import pandas as pd

## print(response.status_code) ##
response = requests.get('https://data.cms.gov/data-api/v1/dataset/35da9162-d09f-434d-83fd-5dfe6b2c6d77/data')

## pulls data from mentioned API, formats it into text
data = response.text

## data is extracted, now need to parse data into JSON
data_json = json.loads(data)

# referencing one specific dictionary for testing purposes
# in this case, returns "015009"
testDict = data_json[0]['federal_provider_number']



# df = pd.DataFrame(testDict, columns = ['federal_provider_number'])

# df.loc[df['federal_provider_number'] == '035014']




# this URL returns the week ending value in which the provider 035014 had personnel vaccination % over 80
# have to find all the providers in each state, get their %s, average them
#  https://data.cms.gov/data-api/v1/dataset/35da9162-d09f-434d-83fd-5dfe6b2c6d77/data?filter[federal_provider_number]=035014&filter[percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time][operator]=>&filter[percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time ][condition][value]=80&column=week_ending


# print (testDict)

# pd.DataFrame.loc[DataFrame[testDict] == '035014']


# for i in range(len(data_json)):
#     if data_json[i]['provider_state']:
#         print(data_json[i]['provider_state'])


# print(data_json.get('provider_state', 'CA'))
# print (data_json[0]['federal_provider_number'])