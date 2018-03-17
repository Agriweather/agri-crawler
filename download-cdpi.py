# !/bin

# import the libraries

import os
import requests

# console output program initial start information
print("Start download original Crops' Diseases Pests Information as raw data")

cwd = os.getcwd()
print("Current working directory: " + cwd)

# shows directory list
rootDirList = os.listdir(cwd)
print("List: ")
print(rootDirList)

# raw data directory & path
rawDataDir = "raw-data"
rawDataDirPath = cwd + "\\" + rawDataDir
print(rawDataDirPath)

# create raw data directory if it is not exists
if rawDataDir in rootDirList:
    print("Directory: " + rawDataDir + " is already exists")
else:
    print("Create a new directory: " + rawDataDir)
    os.mkdir(rawDataDir)

# CDPI directory & path
rawCDPIDataDir = "CDPI"
rawCDPIDataDirPath = rawDataDirPath + "\\" + rawCDPIDataDir
print(rawCDPIDataDirPath)
#

twNationalCDPI_URL = "http://otserv.tactri.gov.tw/ppm/SearchOk.asp"

indexPage = requests.get(twNationalCDPI_URL)
outputFile = "indexCDPI.asp"

output = open(rawCDPIDataDirPath + "\\" + outputFile, "w")
output.write(indexPage.text)
output.close()
