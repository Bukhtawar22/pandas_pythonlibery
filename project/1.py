import pandas as pd 



df = pd.read_csv('khaadi_data.csv')
print(df.columns)

df.drop(columns=['Availability','Product Link','Img Path','Product Description'], inplace=True)
print(df)

df.to_csv('khaadi_data_clean.csv')