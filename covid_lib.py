import matplotlib.pyplot as my_object
from urllib.request import urlopen
import json
from tkinter import *


class covid:
    def __init__(self, covid_url='https://api.covid19api.com/total/dayone/country/', my_country='Turkey',
                 country_list='https://api.covid19api.com/countries'):
        self.data_covid = json.loads(urlopen(covid_url + my_country).read().decode("utf-8"))
        self.json_countries = json.loads(urlopen(country_list).read().decode("utf-8"))

        self.countries = [item['Country'] for item in self.json_countries]
        self.confirmed = [item['Confirmed'] for item in self.data_covid]
        self.recovered = [item['Recovered'] for item in self.data_covid]
        self.date = [item['Date'] for item in self.data_covid]
        self.deaths = [item['Deaths'] for item in self.data_covid]

        self.confirmed_percent_recovered = [0]
        self.confirmed_percent_death = [0]

        for item in range(len(self.confirmed)):
            try:
                self.confirmed_percent_death.append(self.deaths[item] / self.confirmed[item] * 100)
                self.confirmed_percent_recovered.append(self.recovered[item] / self.confirmed[item] * 100)
            except ZeroDivisionError:
                self.confirmed_percent_death.append(0)
                self.confirmed_percent_recovered.append(0)

    def print_all_info(self):
        for item in self.data_covid:
            print(item)

    def draw(self):
        pass


if __name__ == '__main__':
    obj = covid()
    for item in range(len(obj.confirmed)):
        # print(f'%{obj.confirmed_percent_recovered[item]} people recovered: %{obj.confirmed_percent_death[item]} people died')
        print('date:{}% {:.2f} people recovered : % {:.2f} people died.'.format(obj.date[item],
                                                                                obj.confirmed_percent_recovered[item],
                                                                                obj.confirmed_percent_death[item]))
