import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,None,28,30],
    "Salary":[5500,None,60000,80000],
    "Performance Score":[85,None,10,75],
}

df=pd.DataFrame(data)
print(df)
'''
methods of interpolate
1-linear
2-polynominal
3-time
4-cubic

'''

df.interpolate(method="linear", axis=0,inplace=True)