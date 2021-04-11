import matplotlib.pyplot as my_plot
from urllib.request import urlopen
import json
from tkinter import *


class covid:
    def __init__(self, title='Covid-19', covid_url='https://api.covid19api.com/total/dayone/country/',
                 my_country='Turkey',
                 country_list='https://api.covid19api.com/countries'):

        self.data_covid     = json.loads(urlopen(covid_url + my_country).read().decode("utf-8"))
        self.json_countries = json.loads(urlopen(country_list).read().decode("utf-8"))

        self.countries = [item['Country']   for item in self.json_countries]
        self.confirmed = [item['Confirmed'] for item in self.data_covid]
        self.recovered = [item['Recovered'] for item in self.data_covid]
        self.date      = [item['Date']      for item in self.data_covid]
        self.deaths    = [item['Deaths']    for item in self.data_covid]

        self.death_daily     = self.daily_indormation(self.deaths)
        self.recovered_daily = self.daily_indormation(self.recovered)
        self.confirmed_daily = self.daily_indormation(self.confirmed)

        self.countries.sort()
        self.length = len(self.deaths)

        self.confirmed_percent_recovered = [0]
        self.confirmed_percent_death     = [0]

        for item in range(len(self.confirmed)):
            try:
                self.confirmed_percent_death.append(self.deaths[item] / self.confirmed[item] * 100)
                self.confirmed_percent_recovered.append(self.recovered[item] / self.confirmed[item] * 100)
            except ZeroDivisionError: # Avoid the zero division problem
                self.confirmed_percent_death.append(0)
                self.confirmed_percent_recovered.append(0)

        # ------------------------------------------
        # Create frame
        # ------------------------------------------
        self.frame = Tk()
        self.frame.title(title)
        self.frame.geometry('350x500+400+300')
        self.my_listbox = Listbox(self.frame, height=350, selectmode=EXTENDED)
        for item in self.countries: # Append sorted conrty list
            self.my_listbox.insert(END, item)

        Button_1 = Button(self.frame, text="1)Total Deaths", command=lambda: self.clicked(1))
        Button_2 = Button(self.frame, text="2)Percentage of recovered", command=lambda: self.clicked(2))
        Button_3 = Button(self.frame, text="3)Percentage of deaths", command=lambda: self.clicked(3))

        self.my_listbox.pack(side=RIGHT)
        Button_1.pack()
        Button_2.pack()
        Button_3.pack()

        mainloop()

    def print_all_info(self):
        for item in self.data_covid:
            print(item)

    # API doesn't include death day by day, need to calculate

    def deaths_day_by_day(self, deaths_list_=None):
        deaths_daybyday_list = [0]

        for item in range(self.length):
            if item != self.length - 1:

                result = deaths_list_[item + 1] - deaths_list_[item]
                if result >= 0:
                    deaths_daybyday_list.append(result)

        return deaths_daybyday_list

    def clicked(self, args):
        selected_country = self.my_listbox.get(self.my_listbox.curselection())

        if args == 1:
            my_plot.plot(self.deaths)
            for item in range(self.length):
                print(f'{self.date[item]} : total death = {self.deaths[item]}')
            my_plot.show()
            my_plot.close()

        if args == 2:
            my_plot.plot(self.confirmed_percent_recovered)
            for item in range(self.length):
                print(f'{self.date[item]} : recovered people = {self.recovered_daily[item]}')
            my_plot.show()
            my_plot.close()

        if args == 3:
            my_plot.plot(self.confirmed_percent_death)
            for item in range(self.length-1):
                print(f'{self.date[item+1]} : Today died {self.death_daily[item]}')
            my_plot.show()
            my_plot.close()
        if args == 4:
            my_plot.plot(self.confirmed_percent_death)
            my_plot.plot(self.confirmed_percent_recovered)
            for item in range(self.length-1):
                print(f'{self.date[item + 1]} : Today died {self.death_daily[item]} : Recovered {self.recovered}')
            my_plot.show()
            my_plot.close()

    def draw(self, title):
        # ------------------------------------------
        # Create frame
        # ------------------------------------------
        self.frame = Tk()
        self.frame.title(title)
        self.frame.geometry('350x500+400+300')
        self.my_listbox = Listbox(self.frame, height=350, selectmode=EXTENDED)
        for item in self.countries:  # Append sorted conrty list
            self.my_listbox.insert(END, item)

        Button_1 = Button(self.frame, text="1)Total Deaths", command=lambda: self.clicked(1))
        Button_2 = Button(self.frame, text="2)Percentage of recovered", command=lambda: self.clicked(2))
        Button_3 = Button(self.frame, text="3)Percentage of deaths", command=lambda: self.clicked(3))

        self.my_listbox.pack(side=RIGHT)
        Button_1.pack()
        Button_2.pack()
        Button_3.pack()

        mainloop()


if __name__ == '__main__':
    obj = covid()
