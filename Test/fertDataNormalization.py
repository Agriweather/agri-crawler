import os
import pandas as pd

# Get current working directory
print(os.getcwd())
# Get list of current working directory
print(os.listdir(os.getcwd()))

originDataframe = pd.read_csv("fertOUT.csv")

print(originDataframe)

''' Data structure for normalize ferter data
flowID
 

'''

