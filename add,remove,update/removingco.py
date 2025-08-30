import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df=pd.DataFrame(data)
print(df)
#df.drop(columns=["columnname"] ,inplace=True)
df.drop(columns=["Performance Score", "Age"],inplace=True)
print(df)