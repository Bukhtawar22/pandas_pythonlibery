
import pandas as pd


'''
 yes use krty hai jb ek data hai os m vlue missed hai lekin ap ko frk nhi parta isnk iawa kam chl jata hai toh os m ye use krty

dropna()

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

df.dropna(inplace=True)
print(df)