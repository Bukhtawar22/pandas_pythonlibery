import pandas as pd



data ={
    "Name":['bukhthware','fahad','nida','bk','ali'],
    "Age":[28,34,22,34,28],
    "Salary":[50000,60000,45000,52000,85000],
}
df=pd.DataFrame(data)
print(df)
'''
-sum()
-mean()
-count()
-min()
-max()
-std()

'''
grouped= df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
