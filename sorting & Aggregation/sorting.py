'''
**sorting datas
sorting data 1 column sort_values()


'''
import pandas as pd

data ={
    "Name":['bukhthware','fahad','nida'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000],
}
df = pd.DataFrame(data)

df.sort_values(by="Age",ascending=True, inplace=True)
print("Sorting age by descending ")
print(df)