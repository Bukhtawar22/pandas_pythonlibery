import pandas as pd



data ={
    "Name":['bukhthware','fahad','nida'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000],
}
df=pd.DataFrame(data)
print(df)


'''
.mean()
.sum()
.min()
.max()

'''

avg_salary=df["Salary"].mean()
print(avg_salary)