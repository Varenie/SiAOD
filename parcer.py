import requests
from bs4 import BeautifulSoup
import html.parser
import matplotlib.pyplot as plt
import numpy as np
import pylab
import datetime

url = 'http://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01535&UniDbQuery.FromDate=01.01.2010&UniDbQuery.ToDate=03.03.2020'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.select('table.data tr')

dates = []
currency = []

for title in titles[2:]:
    tds = title.select("td")
    dates_string = tds[0].text
    currency_string = tds[2].text
    dates.append(dates_string)
    currency.append(currency_string)

newDate = []
newCurrency = []

for date in dates:
    d = datetime.datetime.strptime(date, '%d.%m.%Y')
    newDate.append(d)

for current in currency:
    cur = current.replace(",",".")
    c = float(cur)
    newCurrency.append(c)

plt.figure(num="NOK/RUB Currency", figsize=(10,9), dpi= 80)
plt.plot(newDate, newCurrency)
plt.title('NOK/RUB(10) Currencies')
plt.ylabel('currencies')
plt.xlabel('Dates')
pylab.show()