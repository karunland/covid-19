import matplotlib.pyplot as my_object
from urllib.request import urlopen
import json
from tkinter import *


class covid:
    def __init__(self, covid_url="https://api.covid19api.com/total/dayone/country/", country_='Turkey',
                 country_list='https://api.covid19api.com/countries'):
        self.data_covid = json.loads(urlopen(covid_url + country_).read().decode("utf-8"))
        self.json_countries = json.loads(urlopen(country_list).read().decode("utf-8"))

        self.countries = [item['Country'] for item in self.json_countries]
        self.confirmed = [item['Confirmed'] for item in self.data_covid]
        self.deaths = [item['Deaths'] for item in self.data_covid]


    def draw(self):
        pass


if __name__ == '__main__':
    obj = covid()

