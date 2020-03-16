import requests
from bs4 import BeautifulSoup
import html.parser
import matplotlib.pyplot as plt
import numpy as np
import pylab
import datetime
import pandas as pd
import csv

FILENAME = "C:\GitSiAOD\Values.csv"

def parcerView(df):
    rolling_mean_10 = df.rolling(window=10).mean()
    
    rolling_mean_100 = df.rolling(window=100).mean()

    plt.figure(num="NOK/RUB Currency", figsize=(10,9))

    plt.plot(df,'b', label = 'main')
    plt.title('NOK/RUB(10) Currencies')
    plt.ylabel('Currencies')
    plt.xlabel('Dates')
    
    plt.plot(rolling_mean_10, 'g', label = 'average mean 10 days')
    plt.plot(rolling_mean_100, 'r', label = 'average mean 100 days')

    plt.legend(loc = 'upper right')
    pylab.show()

def parcerData(start_date, end_date):

    url = 'http://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01535&UniDbQuery.FromDate=' + str(start_date) + '&UniDbQuery.ToDate=' + str(end_date)

    r = requests.get(url) #запрос на подключение к сайту

    soup = BeautifulSoup(r.text, 'html.parser') #сохранение html-кода страницы

    titles = soup.select('table.data tr') #выбор колонок

    date_currency = []

    for title in titles[2:]: #[2:] отсеивает первые два элемента, так как они являются названием таблицы и столбцов
        tds = title.select("td") #выбор столбцав каждой колонки
        dates_string = tds[0].text
        d = datetime.datetime.strptime(dates_string, '%d.%m.%Y')

        currency_string = tds[2].text #выбор столбца даты и значений
        cur = currency_string.replace(",",".")# числа сохранены в массиве с запятой в то время как нам нужна точка
        c = float(cur)

        date_currency.append({"date": d,"currency":c})

    with open(FILENAME, "w", newline="") as file:
        columns = ("date", "currency")
        writer = csv.DictWriter(file, columns)
        writer.writeheader()

        writer.writerows(date_currency)

    dataset = pd.read_csv(FILENAME, sep=',', index_col=['date'], parse_dates=['date'])
    parcerView(dataset)

# main
print("1-Посмотреть период от 01.01.2010 до 03.03.2020\n2-Ввести свой период(вы должны быть уверены, что информация существует)")
answer = input()


if(answer == '1'):
    parcerData('01.01.2010', '03.03.2020')
elif(answer == '2'):
    print("Введите начальную дату(дд.мм.гггг)")
    req = input()

    print("Введите конечную дату(дд.мм.гггг)")
    req2 = input()

    parcerData(req, req2)