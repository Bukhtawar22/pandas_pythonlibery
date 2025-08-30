import pandas as pd


'''
NaN (not a number)
None (for object data types)

isnull()
True - NaN is missing
False - value is present

'''

import pandas as pd

data ={
    "Name":['fahad',None,'bukhtawar','ali'],
    "Age":[27,None,28,30],
    "Salary":[5500,None,60000,80000],
    "Performance Score":[85,None,10,75],
}

df=pd.DataFrame(data)
print(df)

print(df.isnull().sum())