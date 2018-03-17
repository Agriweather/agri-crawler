#!/bin/python scraper_test.py

import os
import requests
from bs4 import BeautifulSoup

# check the current path
print(os.getcwd())

# store some url for data source
test_page = "http://otserv.tactri.gov.tw/ppm/PlantRpt2.asp?keyword=&Typ=00003B040"

# check target page exist
page = requests.get(test_page)

# Check current web page encoding
print(page.encoding)

# change web page to 'big5' which is usually used by Taiwan government
page.encoding = 'big5'

# show web page header and content -> chinese character will display normally if character set is 'big5'
print(page.headers)
print(page.text)

# collect data from sub page
target_page = BeautifulSoup(page.text, 'html.parser')
print(target_page.prettify())

title = target_page.find('title')

print(title)
print(title.text)

title = title.text
title_list = title.split()

print(title_list)
print(title_list[0])


