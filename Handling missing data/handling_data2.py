


'''
fillna()
fillna(value,inplace=Ture)

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

# print("for fillna()")
# df.fillna(0,inplace=True)
# print(df)

#calculated value taky har jaga 0 na pass ho

print("for fillna() with calculated valeu")
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)
