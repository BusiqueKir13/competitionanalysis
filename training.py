# подключаем urlopen из модуля urllib

import urllib.response
from urllib.request import urlopen
import urllib.request
# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup
import random
import requests
import lxml.html
import datetime #импортируем возможность устанавливать дату
import pandas as pd
import numpy as np
# from requests_html import HTMLSession




#старт программы
innedit = input("Введите ИНН:") # вводим инн организации
year_edit = input("Введите год:") # вводим дату за который должны выводится закупки организации
year = int(year_edit) #указываем год в будущем выбор из комбобокса
first_day_of_year = datetime.date.min.replace(year = year).strftime('%d.%m.%Y') #установка первой даты диапазона с которой будет уточняться закупки
last_day_of_year = datetime.date.max.replace(year = year).strftime('%d.%m.%Y') #установка последней даты диапазона с которой будет уточняться закупки + перевод в понимаемый сайтом формат оформления даты
# Список десктопных user agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"]
# Выбор случайной строки user agent
user_agent = random.choice(user_agents)
# Указываем user agent в заголовках запроса перед выполнением запроса
headers = {"User-Agent": user_agent}
#Составляем URL адрес на который будет заходить программа.
urlmain = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString="
search_inn = str(innedit) #указываем ИНН - в дальнейшем из строки ввода информации
morph_filter = "&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&" #установка фильтра для поиска
numberpage = "pageNumber=1&sortDirection=false&"
recordperpage = "recordsPerPage=_500" #установка максимального количества позиций отображаемых на странице
otherfilter = "&showLotsInfoHidden=false&sortBy=UPDATE_DATE&fz44=on&pc=on&currencyIdGeneral=-1&"
datefilter = "publishDateFrom="
daty = first_day_of_year
datefilter2 = "&publishDateTo="
dateto = last_day_of_year
yearfilter = datefilter+daty+datefilter2+dateto
filterset = morph_filter+numberpage+recordperpage+otherfilter
resultsearch = urlmain+search_inn+filterset+yearfilter
print(resultsearch) #отображаем результат - валидную url ссылку которая ведет на результат поиска
print('Пожалуйста, подождите... Нужно немного времени для сбора данных') # чтобы не было скучно
url = [resultsearch]
# session = HTMLSession()
# r = session.get(url)

for x in url:
                     html_code = str(urllib.request.urlopen(x).read().decode('UTF-8')) #Открываем страницу и декодируем ее посредством кодировки UT8, она используется на сайте
                     html_code = "".join(line.strip() for line in html_code.split("\n"))
                     # отправляем исходный код страницы на обработку в библиотеку
                     soup = BeautifulSoup(html_code,  'lxml')
                     # находим название страницы с помощью метода find()
                     s = soup.find("div",{'class': "col-9 search-results"}) # выбираем данные, которые необходимы для дальнейшей обработки (тело результата поиска)

                     customer = soup.find_all("div",{'class': "registry-entry__body-href"})
                     # for n in customer:
                          # tags=soup.findAll("div",{'class': "registry-entry__body-href"} )
                     #     for z in tags:
                     #         print(z.getText()) #избавляемся от тегов

                     nameprocurement = soup.find_all("div",{'class': "registry-entry__body-value"}) # вывод предмета контракта
                     # for f in nameprocurement:
                     #      tags=soup.findAll("div",{'class': "registry-entry__body-value"} )
                     #     for a in tags:
                     #         print(a.getText()) #избавляемся от тегов

                     nmc = soup.find_all("div",{'class': "price-block__value"}) #dвывод НМЦК контракта
                     # for h in nmc:
                         # tags=soup.findAll("div",{'class': "price-block__value"} )
                     #     for u in tags:
                     #         print(u.getText()) #избавляемся от тегов

                     ikzak = soup.find_all("div",{'class': "registry-entry__header-mid__number"})
                     # for h in ikzak:
                          # tags=soup.findAll("div",{'class': "registry-entry__header-mid__number"})
                     #     for t in tags:
                     #         print(t.getText()) #избавляемся от тегов
                     for n in customer, ikzak, nameprocurement, nmc:
                         tag1=soup.find_all("div",{'class': "registry-entry__body-href"} )
                         tag2=soup.find_all("div",{'class': "registry-entry__header-mid__number"})
                         tag3=soup.find_all("div",{'class': "registry-entry__body-value"} )
                         tag4=soup.find_all("div",{'class': "price-block__value"})
                         for t in tag1:
                             print(t.getText())
                         for y in tag2:
                              print(y.getText())
                         for u in tag3:
                              print(u.getText())
                         for i in tag4:
                              print(i.getText())


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.DataFrame( columns=["Заказчик", "ИКЗ", "Предмет закупки","НМЦК"], index=[tag1,tag2,tag3,tag4])
df._append(df, ignore_index=True).replace(' ','')




print(df)
