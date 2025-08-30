import pandas as pd
"""
1- how big is your dateset
2-what are the names of columns

shape and columns
"""

# smaple data fram
data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df = pd.DataFrame(data)
print(df)
print(f"Shape:{df.shape}")
print(f"Column name: {df.columns}")