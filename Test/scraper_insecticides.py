#!/bin/python scraper_insecticides.py

import os
import pandas as pd
from bs4 import BeautifulSoup

# check the current path
print(os.getcwd())

# store some url for data source
base_page = "https://pesticide.baphiq.gov.tw/web/Insecticides_MenuItem5_3.aspx"
webHostURL = "https://pesticide.baphiq.gov.tw/web/"

'''
Data format:
    category
    class
    chineseName
    englishName
    code
    originBrand
    registerBrand
    useRange
    activeIngredients
    license
'''

# create a empty dictionary
dataCategory = []
dataClass = []
dataChineseName = []
dataEnglishName = []
dataCode = []
dataOriginBrand = []
dataRegisterBrand = []
dataUseRange = []
dataActiveIngredients = []
dataLicense = []

# get source directory
fileList = os.listdir(os.getcwd() + "\\dpl")

for source_file in fileList:
    print(source_file)
    source_file_path = os.getcwd() + "\\dpl\\" + source_file
    print(source_file_path)

    # use encoding "utf-8-sig" to avoid display chinese character in windows
    save_page = open(source_file_path, encoding='utf-8-sig')
    # save_page = open(os.getcwd() + "\\A-MX-1.html")

    html_tree = BeautifulSoup(save_page.read(), 'html.parser')

    # get dpl Category & Class
    dplClassifyTree = html_tree.find_all("option", selected="selected")

    dplCategory = dplClassifyTree[0].attrs.get('value')
    print(dplCategory)
    dplClass = dplClassifyTree[1].attrs.get('value')
    print(dplClass)

    # get dpl item
    dplItems = html_tree.find_all("table", id="ctl00_ContentPlaceHolder1_GridView1")

    if len(dplItems) > 0:
        dplItems = dplItems[0]

        for item in dplItems:
            if (item.name == "tr") and (len(item.contents) > 4):
                print(item.text)

                print(item.contents)
                print(len(item.contents))

                count = 0
                while count < len(item.contents):
                    content = item.contents[count]
                    if content.name == "td":
                        print(content)

                        if content.text != "":
                            print(content.text)
                            if count == 1:
                                names = content.text
                                nameList = names.split()
                                print("Names: ")
                                print(nameList)
                                if len(nameList) < 2:
                                    chineseName = nameList[0]
                                    dataChineseName.append(chineseName)
                                    dataEnglishName.append("null")
                                else:
                                    chineseName = nameList[0]
                                    dataChineseName.append(chineseName)
                                    englishName = nameList[1]
                                    dataEnglishName.append(englishName)

                                dataCategory.append(dplCategory)
                                dataClass.append(dplClass)

                            if count == 2:
                                code = content.text
                                print("Code: " + code)
                                dataCode.append(code)

                            if count == 3:
                                origin_brand = content.text
                                print("origin_brand: " + origin_brand)
                                dataOriginBrand.append(origin_brand)

                            if count == 4:
                                reg_brand = content.text
                                print("reg_brand: " + reg_brand)
                                dataRegisterBrand.append(reg_brand)

                            if count == 5:
                                use_range = webHostURL + content.contents[0].attrs.get("href")
                                print("use_range: " + use_range)
                                dataUseRange.append(use_range)

                            if count == 6:
                                ingredients = webHostURL + content.contents[0].attrs.get("href")
                                print("ingredients: " + ingredients)
                                dataActiveIngredients.append(ingredients)

                            if count == 7:
                                license = webHostURL + content.contents[0].attrs.get("href")
                                print("license: " + license)
                                dataLicense.append(license)

                    count += 1

            # for content in item.contents:
            #     print(content.text)

        #
        print("Run complete file: " + source_file)

'''
Data format:
    category
    class
    chineseName
    englishName
    code
    originBrand
    registerBrand
    useRange
    activeIngredients
    license
'''

d = {
    '0_category': dataCategory,
    '1_class': dataClass,
    '2_chineseName': dataChineseName,
    '3_englishName': dataEnglishName,
    '4_code': dataCode,
    '5_originBrand': dataOriginBrand,
    '6_registerBrand': dataRegisterBrand,
    '7_useRange': dataUseRange,
    '8_activeIngredients': dataActiveIngredients,
    '9_license': dataLicense,
}
df = pd.DataFrame(data=d)

print(df)

df.to_csv('dplOut.csv', index=False, encoding='utf-8')

print("Program exist of run complete the whole script")
