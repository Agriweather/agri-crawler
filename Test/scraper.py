#!/bin/python scraper.py

import os
import requests
import pandas as pd

# check the current path
print(os.getcwd())

# store some url for data source
page_1 = "http://otserv.tactri.gov.tw/ppm/SearchOk.asp"
page_1_base = "http://otserv.tactri.gov.tw/ppm/"
page_2 = "https://pesticide.baphiq.gov.tw/web/Insecticides_MenuItem5_3.aspx"
page_3 = "http://fims.afa.gov.tw/WFR/PublicFun/QueryFertBrand.aspx"

# check target page exist
page = requests.get(page_1)

# Check current web page encoding
print(page.encoding)

# change web page to 'cp950' which is usually used by Taiwan government > MS950 Microsoft Tradition Chinese
page.encoding = 'cp950'

# show web page header and content -> chinese character will display normally if character set is 'big5'
print(page.headers)
print(page.text)

# pares web page use BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# just print out the requested page
# print(soup.prettify())

# find all hyperlink tag <a> in requested page
hyperlinks = soup.find_all('a')

# get some basic information all about hyperlink tag <a>
# print(hyperlinks)       # print all hyperlink tag <a>
# print(len(hyperlinks))  # print total number of hyperlink tag <a>

'''
Data format: Corp Protection Information system
    data_id:
    source_url:
    chinese_name:
    class_name:
    english_name:
    nick_name:
    symptom:
    infection_way:
    workaround:
    medicine:
        medicine_name:
        use_volume:
        dilution_ratio:
        use_method:
        note:
    
'''

# create a empty dictionary
data_chinese_name = []
data_source_url = []
data_class_name = []

# do each item with link tag
for link in hyperlinks:
    if len(link.text) > 3:
        print("link item:")
        print(link.text)               # get text inner link tag
        print(link.attrs.get('href'))  # get href attribute value from link tag
        print("These should be comment when you are running in production mode")
        reference_link = page_1_base + link.attrs.get('href')
        data_chinese_name.append(link.text)
        data_source_url.append(reference_link)

        # collect data from link reference page
        reference_page = requests.get(reference_link)
        reference_page.encoding = 'big5'
        reference_tree = BeautifulSoup(reference_page.text, 'html.parser')
        title = reference_tree.find('title')

        print(title)
        print(title.text)

        title = title.text
        title_list = title.split()

        print(title_list[2])
        data_class_name.append(title_list[0])

# # test print for data preview - should be commit at production mode
# print(data_chinese_name)
# print(data_source_url)
# print(data_class_name)

d = {
    'chinese_name': data_chinese_name,
    'class_name': data_class_name,
    'source_url': data_source_url
}
df = pd.DataFrame(data=d)

# # test print for preview data frame status and size - should be commit at production mode
# print(df)
# print(len(df))

# test print for preview data frame status and size - should be commit at production mode
for item in range(0, len(df), 1):
    item_name = df.iloc[item]['chinese_name']
    print(str(item) + ' ' + item_name)

df.to_csv('out.csv', index=False, encoding='utf-8')

print("Program executed successful")
