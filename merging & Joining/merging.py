import pandas as pd

#customer dataframe

df_customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['ali','nida','bk']
})

#order dataframe


df_orders=pd.DataFrame({
    'CustomerID':[1,2,4],
    'orderAmount':[250,450,350]
})

#merging
'''
outer
innner
left
right
'''
df_merged=pd.merge(df_customers,df_orders,on='CustomerID',how='right')
print("innner join")
print(df_merged)

