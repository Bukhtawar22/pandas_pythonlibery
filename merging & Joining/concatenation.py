'''
vertically (row-wise)
horizontally (column-wise)


'''
import pandas as pd

df_region1=pd.DataFrame({
    'CustomerID':[1,2,],
    'Name':['ali','nida']
})
df_region2=pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['fahad','bk']
})
#concatenate vertically

df_concat = pd.concat([df_region1,df_region2],axis=1, ignore_index=True)
print(df_concat)