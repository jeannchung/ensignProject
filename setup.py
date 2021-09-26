import requests
import json
import pandas as pd

## print(response.status_code) ##
response = requests.get('https://data.cms.gov/data-api/v1/dataset/35da9162-d09f-434d-83fd-5dfe6b2c6d77/data')

## pulls data from mentioned API, formats it into text
data = response.text

## data is extracted, now need to parse data into JSON
data_json = json.loads(data)

# for i in range(len(data_json)):
#     if data_json[i]['provider_state']:
#         print(data_json[i]['provider_state'])

# print (data_json[0]['provider_state'])
# print(data_json.get('provider_state', 'CA'))

testState = data_json[0]['provider_state']
print (testState)
print (type(testState))