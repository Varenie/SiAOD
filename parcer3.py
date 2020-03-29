import requests
from bs4 import BeautifulSoup
import html.parser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab
import datetime
import json
import csv

FILENAME = "C:\\GitSiAOD\\Weather.csv"
NEWFILENAME = "C:\\GitSiAOD\\NewWeather.csv"
def parcerData(start_date, end_date, station, city):
    url = 'https://api.meteostat.net/v1/history/daily?station=' + str(station) +'&start=' + str(start_date) + '&end=' + str(end_date) + '&key=HOmpes1N'

    r = requests.get(url) #запрос на подключение к сайту
    dictdata = json.loads(r.text)

    with open(FILENAME, 'w', newline='') as file:
        columns = ("date","temperature","temperature_min","temperature_max","precipitation","snowfall","snowdepth","winddirection","windspeed","peakgust","sunshine","pressure")
        writer = csv.DictWriter(file, columns)
        writer.writeheader()

        writer.writerows(dictdata["data"])

    with open(FILENAME, 'r') as f:
        incl_col = [0, 1]                          # индексы нужных столбцов
        new_csv = []                              # новый список для нового файла
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            col = list(row[i] for i in incl_col)
            new_csv.append(col)                   # заполняем новый список нужными столбцами

    with open(NEWFILENAME, 'w') as f:               # создаем новый файл
        writer = csv.writer(f, delimiter=",")
        writer.writerows(new_csv)
            
    dataset = pd.read_csv(NEWFILENAME, sep=',', index_col=['date'], parse_dates=['date'])

    plt.plot(dataset,'b', label = 'main')
    plt.title('Weather of ' + str(city))
    plt.ylabel('Temperature')
    plt.xlabel('Dates')
    plt.show()

# main
print("1-Погода в Хамерфесте\n2-Погода в Минске")
answer = input()

if(answer == '1'):
    print("1-Посмотреть период от 01.01.2010 до 03.03.2020\n2-Ввести свой период(вы должны быть уверены, что информация существует)")
    answer2 = input()

    if(answer2 == '1'):
        parcerData('2010-01-01', '2020-03-03', '01052', 'Hammerfest')
    elif(answer2 == '2'):
        print("Введите начальную дату(гггг-мм-дд)")
        req = input()

        print("Введите конечную дату(гггг-мм-дд)")
        req2 = input()

        parcerData(req, req2, '01052', 'Hammerfest')
elif(answer == '2'):
    print("1-Посмотреть период от 01.01.2010 до 03.03.2020\n2-Ввести свой период(вы должны быть уверены, что информация существует)")
    answer2 = input()

    if(answer2 == '1'):
        parcerData('2010-01-01', '2020-03-03', '24944', 'Minsk')
    elif(answer2 == '2'):
        print("Введите начальную дату(гггг-мм-дд)")
        req = input()

        print("Введите конечную дату(гггг-мм-дд)")
        req2 = input()

        parcerData(req, req2, '24944', 'Minsk')
    