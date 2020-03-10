import requests
from bs4 import BeautifulSoup
import html.parser
import matplotlib.pyplot as plt
import numpy as np
import pylab
import datetime

print("1-Посмотреть период от 01.01.2010 до 03.03.2020\n2-Ввести свой период(вы должны быть уверены, что информация существует)")
answer = input()


if(answer == '1'):
    url = 'http://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01535&UniDbQuery.FromDate=01.01.2010&UniDbQuery.ToDate=03.03.2020'

    r = requests.get(url) #запрос на подключение к сайту

    soup = BeautifulSoup(r.text, 'html.parser') #сохранение html-кода страницы

    titles = soup.select('table.data tr') #выбор колонок

    dates = []
    currency = []

    for title in titles[2:]: #[2:] отсеивает первые два элемента, так как они являются названием таблицы и столбцов
        tds = title.select("td") #выбор столбцав каждой колонки
        dates_string = tds[0].text
        currency_string = tds[2].text #выбор столбца даты и значений
        dates.append(dates_string) 
        currency.append(currency_string)

    newDate = []
    newCurrency = []

    #конвертация из строки в формат даты
    for date in dates:
        d = datetime.datetime.strptime(date, '%d.%m.%Y')
        newDate.append(d)

    #конвертация из строки в число с плавающей точкой
    for current in currency:
        cur = current.replace(",",".")# числа сохранены в массиве с запятой в то время как нам нужна точка
        c = float(cur)
        newCurrency.append(c)

    plt.figure(num="NOK/RUB Currency", figsize=(10,9), dpi= 80)
    plt.plot(newDate, newCurrency)
    plt.title('NOK/RUB(10) Currencies')
    plt.ylabel('currencies')
    plt.xlabel('Dates')
    pylab.show()

elif(answer == '2'):
    print("Введите начальную дату(дд.мм.гггг)")
    req = input()

    print("Введите конечную дату(дд.мм.гггг)")
    req2 = input()
    url = 'http://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01535&UniDbQuery.FromDate=' + str(req) + '&UniDbQuery.ToDate=' + str(req2)

    r = requests.get(url) #запрос на подключение к сайту

    soup = BeautifulSoup(r.text, 'html.parser') #сохранение html-кода страницы

    titles = soup.select('table.data tr') #выбор колонок

    dates = []
    currency = []

    for title in titles[2:]: #[2:] отсеивает первые два элемента, так как они являются названием таблицы и столбцов
        tds = title.select("td") #выбор столбцав каждой колонки
        dates_string = tds[0].text
        currency_string = tds[2].text #выбор столбца даты и значений
        dates.append(dates_string) 
        currency.append(currency_string)

    newDate = []
    newCurrency = []

    #конвертация из строки в формат даты
    for date in dates:
        d = datetime.datetime.strptime(date, '%d.%m.%Y')
        newDate.append(d)

    #конвертация из строки в число с плавающей точкой
    for current in currency:
        cur = current.replace(",",".")# числа сохранены в массиве с запятой в то время как нам нужна точка
        c = float(cur)
        newCurrency.append(c)

    plt.figure(num="NOK/RUB Currency", figsize=(10,9), dpi= 80)
    plt.plot(newDate, newCurrency)
    plt.title('NOK/RUB(10) Currencies')
    plt.ylabel('currencies')
    plt.xlabel('Dates')
    pylab.show()

else:
    print("Неверный вариант")