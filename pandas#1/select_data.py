import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df=pd.DataFrame(data)
print("Sample dataframe")
print(df)

#selecting single column
print("Name (Single column retuen series )")
name=df['Name']
print(name)

#selecting multiple column
subset =df[["Name","Salary"]]
print('\nSubset with Nmae and Salary')
print(subset)