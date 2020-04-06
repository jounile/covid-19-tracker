import json
import requests
import datetime
from datetime import timedelta

data = requests.get('https://pomber.github.io/covid19/timeseries.json')
from_date = input()
#print(from_date)

countries = ['US', 'Italy', 'France','Germany', 'Austria', 'Sweden', 'Russia', 'Finland', 'Estonia']
for country in countries:
    print('')
    print(country)
    country = data.json()[country]
    if country:
        confirmed = None
        deaths = None
        confirmed_trend = None
        deaths_trend = None
        prev_confirmed_difference = None
        prev_deaths_difference = None
        confirmed_difference = None
        deaths_difference = None
        darrow = None
        for info in country:
            if confirmed is not None:
                confirmed_difference = info['confirmed'] - confirmed
            if deaths is not None:
                deaths_difference = info['deaths'] - deaths
            confirmed = info['confirmed']
            deaths = info['deaths']
            if prev_confirmed_difference is not None:
                if prev_confirmed_difference < confirmed_difference:
                    confirmed_trend = "<span style='color:red'>&uarr;</span>"
                else:
                    confirmed_trend = "&darr;"
            if prev_deaths_difference is not None:
                if prev_deaths_difference < deaths_difference:
                    deaths_trend = "<span style='color:red'>&uarr;</span>"
                else:
                    deaths_trend = "&darr;"
            d1 = datetime.datetime.strptime(info['date'], '%Y-%m-%d')
            d2 = datetime.datetime.strptime(from_date, '%Y-%m-%d')
            
            if d1 >= d2:
                print(info['date'] +
                " confirmed: " + str(info['confirmed']) +
                " " + str(confirmed_difference) +
                " " + str(confirmed_trend) +
                " deaths:" + str(info['deaths']) +
                " " + str(deaths_difference) +
                " " + str(deaths_trend))
            
            prev_confirmed_difference = confirmed_difference
            prev_deaths_difference = deaths_difference

