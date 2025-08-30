import pandas as pd


# smaple data fram
data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df=pd.DataFrame(data)
print("Sample DataFrame ")
print(df)
print("Descriptive Statistics")
print(df.describe())