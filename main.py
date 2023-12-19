import requests
import json
from canada_cities import canada_cities

output = []

for province, cities in canada_cities.items():
    for n,city in enumerate(cities):
        print(f'accessing {city} of {province}, city no. {n} out of {len(cities)}. \n/-******-/')
        data = {"city":city,"province":cities}
        response = requests.post('https://www.theexchangenetwork.ca/wp-json/ficanex-find-an-atm/1/find-atm',data=data)
        response = response.json()
        if int(response['count']) > 0:
             for atm in response['locations']:
                 output.append(atm)

csv_output = json.dumps(output)
with open("output.json", "w") as outfile:
    outfile.write(csv_output)