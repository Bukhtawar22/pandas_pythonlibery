import pandas as pd

#head()
#tail()

df = pd.read_json("sample_Data.json")

print("Display 10 rows of first")
print(df.head(10))
print("Display 10 rows of end")
print(df.tail(10))

