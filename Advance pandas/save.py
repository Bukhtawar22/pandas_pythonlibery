import pandas as pd


data={
    "name":['ali',"nida","bk"],
    "age":[25,46,12],
    "city":["karachi","islambad","lahore"]
}
df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv" , index=False) 
# df.to_excel("output.xlsx" , index=False)
df.to_json("output.json" , index=False)