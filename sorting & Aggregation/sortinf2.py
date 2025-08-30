import pandas as pd



data ={
    "Name":['bukhthware','fahad','nida'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000],
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by=["Age","Salary"],ascending=[True,False], inplace=True)
print("Sorting age by descending ")
print(df)