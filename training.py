# подключаем urlopen из модуля urllib
from datetime import date
from urllib.request import urlopen
import urllib.request
# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup
import random
import requests
import os
import re
import lxml.html
import sys



procedure_number = []
customer = []
method_of_conducting = []
date_of_placement = []
nmc = []
inn_customer = []
contract_price = []
data_url = []
# data_dict = {'Номер процедуры': procedure_number,
#              'Заказчик': customer,
#              'ИНН' : inn_customer,
#              'Дата размещения': date_of_placement,
#              'НМЦ': nmc,
#              'Цена контракта' : contract_price,
#              'Ссылка': data_url}

# Список десктопных user agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"
]

# Выбор случайной строки user agent
user_agent = random.choice(user_agents)

# Указываем user agent в заголовках запроса перед выполнением запроса
headers = {"User-Agent": user_agent}
urlmain = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString="
search_inn = "7729082090"
morph_filter = "&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&"
numberpage = "pageNumber=1&sortDirection=false&"
recordperpage = "recordsPerPage=_500"
otherfilter = "&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&pc=on&currencyIdGeneral=-1&"
datefilter = "publishDateFrom="
datefrom = "01.01.2023"
datefilter2 = "&publishDateTo="
dateto = "31.12.2023"
yearfilter = datefilter+datefrom+datefilter2+dateto
filterset = morph_filter+numberpage+recordperpage+otherfilter
resultsearch = urlmain+search_inn+filterset+yearfilter
print(resultsearch)
url = [
# "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=3666029505&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_500&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&pc=on&currencyIdGeneral=-1&publishDateFrom=01.01.2023&publishDateTo=31.12.2023"
resultsearch
]
# перебираем адрес из списка

for x in url:
    # получаем исходный код очередной страницы из списка
    html_code = str(urllib.request.urlopen(x).read().decode('UTF-8'))

    # отправляем исходный код страницы на обработку в библиотеку
    soup = BeautifulSoup(html_code,  'lxml')

        # находим название страницы с помощью метода find()
    s = soup.findAll("div", {'class': "col-9 search-results"} ) # выбираем данные, которые необходимы для дальнейшей обработки (тело результата поиска)
    customer = soup.find_all("div", {'class': "registry-entry__body-href"}) # вывод наименование ораганизации
    nameprocurement = soup.find_all("div", {'class': "registry-entry__body-value"}) # вывод предмета контракта
    nmc = soup.find_all("div", {'class': "price-block__value"}) #dвывод НМЦК контракта

    # выводим его на экран
    print(customer, nameprocurement, nmc)

