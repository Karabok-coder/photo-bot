# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from progress.bar import Bar
import datetime
from info import *


def GetSite(sitenum, i):
    #для 3-го сайта другое выражение поэтому так
    if sitenum == 3: return requests.get(sites[sitenum - 1] + s_last_1 + str(i) + s_last_3)
    return requests.get(sites[sitenum - 1] + s_last_1 + str(i) + s_last_2)

logo = open("logo.txt", "r").readlines()
logo_s = "\n"

sitenum = 1
last = 1
before_ = 2

for i in range(len(logo)):
    logo_s += logo[i]

print(logo_s + "\n")

while True:
    sitenum = int(input("Номер сайта (1-3): "))
    if (sitenum >= 1) and (sitenum <= 3): break

while True:
    last = int(input("С какой страницы скачивать (от 1): "))
    before_ = int(input("До какой страницы скачивать (> чем прошлый): "))
    if (before_ > last): break

photo = []

print("\nНачало работы.\n")

bar = Bar('Поиск ссылок', max = before_ - last)

for i in range(last, before_):
    r = GetSite(sitenum, i)
    bar.next()
    for url in re.findall('(https://unsplash.com/photos/[a-zA-Z0-9-]+/download)', r.text):
        photo.append(url)
bar.finish()

print(f"Найдено {len(photo)} ссылок. Приступаю к скачиванию...")

for i in range(len(photo)):
    bar = Bar(f'Скачивание {i + 1}-й фотографии', max = 3)
    bar.next()
    r = requests.get(photo[i], allow_redirects=True)
    bar.next()
    with open("photo/" + str(datetime.datetime.now()) + "_" + str(i) + '.png', 'wb') as new_file: new_file.write(r.content)
    bar.next()

bar.finish()
print('\n')