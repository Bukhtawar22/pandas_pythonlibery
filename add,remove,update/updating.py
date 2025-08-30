import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df=pd.DataFrame(data)
print(df)

#.loc[]
#df.loc[row_index,"Column name"] = new_value
df.loc[0,"Salary"] = 2200
print(df)