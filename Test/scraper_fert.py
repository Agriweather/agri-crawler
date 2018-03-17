#!/bin/python scraper_insecticides.py

import os
import pandas as pd
from bs4 import BeautifulSoup

# check the current path
print(os.getcwd())

# store some url for data source
base_page = "http://fims.afa.gov.tw/WFR/PublicFun/QueryFertBrand.aspx"
webHostURL = "https://pesticide.baphiq.gov.tw/web/"

# get source directory
fileList = os.listdir(os.getcwd() + "\\fert")
print(fileList)

newFileList = []

for file in fileList:
    if os.path.isfile(os.getcwd() + "\\fert\\" + file):
        newFileList.append(file)

fileList = newFileList
print(fileList)



'''
Data format:
    licenseNumber
    providerName
    productName
    className
    rawMaterial
    licenseDate
    madeFrom
    supplementFacts
    providerInformation
'''

# create a empty dictionary
dataLicenseNumber = []
dataProviderName = []
dataProductName = []
dataClassName = []
dataRawMaterial = []
dataLicenseDate = []
dataMadeFrom = []
dataSupplementFacts = []
dataProviderInformation = []

# start get every source file
for file in fileList:
    # start get each fert item in this source file
    print("start parse each fert item in:" + file)

    # locate each source file
    source_file = file

    # get source file whole path
    source_file_path = os.getcwd() + "\\fert\\" + source_file

    # open saved source file
    save_page = open(source_file_path, encoding='utf-8-sig')

    # parse saved source file
    html_tree = BeautifulSoup(save_page.read(), 'html.parser')
    # print html_tree in pretty format
    # print(html_tree.prettify())

    # get fert item
    fertItems = html_tree.find_all("table", id="Main_m_ResultGrid")
    fertItems = fertItems[0]
    # print fert items
    # print(fertItems)

    fertItems = fertItems.contents
    fertItems = fertItems[1]

    fertItems = fertItems.contents

    # parameters for item counter to
    itemCount = 0

    # make sure fertItems have some fert data (start in position 6)
    if len(fertItems) > 6:

        for item in fertItems:

            if (itemCount > 1) and (len(item) > 2):
                print(item.text)

                itemContent = item.contents

                # parameter for content counter
                contentCount = 0

                for eachContent in itemContent:
                    # print(eachContent)

                    if contentCount == 1:
                        content = eachContent.text
                        print(content)
                        dataLicenseNumber.append(content)

                    if contentCount == 2:
                        providerName = eachContent.text
                        nameList = providerName.split()
                        providerName = nameList[0]
                        print(providerName)
                        dataProviderName.append(providerName)

                    if contentCount == 3:
                        productName = eachContent.text
                        print(productName)
                        dataProductName.append(productName)

                    if contentCount == 4:
                        className = eachContent.text
                        print(className)
                        dataClassName.append(className)

                    if contentCount == 5:
                        rawMaterials = eachContent.text
                        print(rawMaterials)
                        dataRawMaterial.append(rawMaterials)

                    if contentCount == 6:
                        licenseDate = eachContent.text
                        licenseDate = licenseDate.split()
                        licenseDate = licenseDate[0]
                        print(licenseDate)
                        dataLicenseDate.append(licenseDate)

                    if contentCount == 7:
                        madeFrom = eachContent.text
                        print(madeFrom)
                        dataMadeFrom.append(madeFrom)

                    if contentCount == 8:
                        supplementFacts = eachContent.contents[1]
                        print(supplementFacts)
                        dataSupplementFacts.append(supplementFacts)

                    if contentCount == 9:
                        providerInformation = eachContent.contents[1]
                        print(providerInformation)
                        dataProviderInformation.append(providerInformation)

                    contentCount += 1

            itemCount += 1
            # end of a saved source file

d = {
    '0_licenseNumber': dataLicenseNumber,
    '1_providerName': dataProviderName,
    '2_productName': dataProductName,
    '3_className': dataClassName,
    '4_rawMaterial': dataRawMaterial,
    '5_licenseDate': dataLicenseDate,
    '6_madeFrom': dataMadeFrom,
    '7_supplementFacts': dataSupplementFacts,
    '8_providerInformation': dataProviderInformation
}
df = pd.DataFrame(data=d)

print(df)

df.to_csv('fertOut.csv', index=False, encoding='utf-8')

print("Program exist of run complete the whole script")
