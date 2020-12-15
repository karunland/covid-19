import matplotlib.pyplot as my_object
from urllib.request import urlopen
import json
from tkinter import *

covid_url = "https://api.covid19api.com/total/dayone/country/"
# data = json.loads(urlopen(covid_url).read().decode("utf-8"))

def deaths_fromjson_deaths(country_):

    data1 = json.loads(urlopen(covid_url + country_).read().decode("utf-8"))

    my_list_deaths = []
    
    for item in data1:
        my_list_deaths.append(item['Deaths'])
        # pprint( item['Date'] +" total deats : "+ item['Deaths'])
        print(item['Date'] +" TOTAL DEATHS ="+ str(item['Deaths']))
        # print(item['Deaths'])


    return my_list_deaths


def deaths_fromjson_confirmed(country_):
    my_list2_confirmed = []
    data1 = json.loads(urlopen(covid_url + country_).read().decode("utf-8"))
    for item in data1:
        my_list2_confirmed.append(item['Confirmed'])
    for item in my_list2_confirmed:
        print(item)

    return my_list2_confirmed


def deaths_day_by_day(deaths_list_):

    x = len(deaths_list_)
    deaths_daybyday_list = []

    deaths_daybyday_list.append(0)  # ilk gunlerden 0 kısı oldu

    for y in range(x):
        if y != x - 1:

            result = deaths_list_[y + 1] - deaths_list_[y]
            if result >= 0:
                deaths_daybyday_list.append(result)

    for item in deaths_daybyday_list:
        print(item)

    return deaths_daybyday_list

def ı_clicked(args):
    if args == 1:

        some = my_listbox.curselection()                        # cursor sectıgınız ulke
        country = my_listbox.get(some)                          # degşskene atma
        my_object.plot(deaths_fromjson_deaths(country))
        my_object.ylabel(country+" TOTAL DEATH")
        my_object.show()                                        # ulke bılgılerını çekme (toplam ölü sayısı) ve çizdirme
        my_object.close()

    if args == 2:
        some = my_listbox.curselection()                        # cursor sectıgınız ulke
        country = my_listbox.get(some)                          # degşskene atma
        my_object.plot(deaths_fromjson_confirmed(country))
        my_object.ylabel(country + " Confırmed")
        my_object.show()                                        # ulke bılgılerını çekme (toplam ölü sayısı)
        my_object.close()

    if args == 3:
        pass

    if args == 4:

        some = my_listbox.curselection()                         # cursor sectıgınız ulke
        country = my_listbox.get(some)                           # degşskene atma
        x = deaths_day_by_day(deaths_fromjson_deaths(country))
        my_object.ylabel(country + " Deaths per day")
        my_object.plot(x)
        my_object.show()                                         # gun gun ölü sayısı bulma func
        my_object.close()

    if args == 5:
       my_object.close()

url_of_countries = 'https://api.covid19api.com/countries'
data_ofcountry = json.loads(urlopen(url_of_countries).read().decode("utf-8"))
countries_list = list()

for item in data_ofcountry:
    countries_list.append(item['Slug'])        #ulke ısımler

countries_list.sort()                          # alfabetık sıralama



my_frame = Tk()
my_frame.title("covid-19")
my_frame.geometry("300x500+400+200")
my_listbox = Listbox(my_frame, height=350, selectmode=EXTENDED)

for iitem in countries_list:  # listeye aktarma json dan
    my_listbox.insert(END, iitem)


button1 = Button(my_frame, text="1)Deaths", command=lambda: ı_clicked(1))
button2 = Button(my_frame, text="2)Confirmed", command=lambda: ı_clicked(2))
button3 = Button(my_frame, text="3)kontrol", command=lambda: ı_clicked(3))
button4 = Button(my_frame, text="4)günün ölü sayısı", command=lambda: ı_clicked(4))
button5 = Button(my_frame, text="5)figure dosyasını kapat", command=lambda: ı_clicked(5))

my_listbox.pack(side=RIGHT)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

my_object.xlabel("Days")


mainloop()
