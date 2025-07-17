import pandas as pd


#read data from CSV file into a dataframe

# df =pd.read_csv("sales_data_sample.csv", encoding="latin1")
# print(df)

# df = pd.read_excel("SampleSuperstore.xlsx")
# print(df)

df = pd.read_json("sample_Data.json")
print(df)