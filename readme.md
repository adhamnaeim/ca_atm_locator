# atm locator web scraper
---
job listing: https://www.upwork.com/jobs/~01b797bc43b8fe3900
contractor needs the ATM's info in all of Canada scraped from the following website https://www.theexchangenetwork.ca/find-an-atm/#top
---
### constraints

websites requires both a city and province/state or postal/zipcode to query a search. going through every posstal code is tedious since there is near 900k postal codes. best probable solution is to search for each city in every province/state. the following apporach narrows down the query to 221 cities to query.

the POST api used to generate responses is in the following link https://www.theexchangenetwork.ca/wp-json/ficanex-find-an-atm/1/find-atm, which uses the following payload for example {"city":"Calgary","province":"Alberta"}

after testing the api response on postman without any specific headers, it can successfully! fyi the website limits for 10 records but the API response results in much more.
---
### solution

no need to scrape each city for each province/state in every run since we can save them in a dictionary to save processing power.
for loop on each city in each province, check api response if there is a result. append result in a datatable and export them to a json file.