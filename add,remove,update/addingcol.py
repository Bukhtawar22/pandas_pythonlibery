import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[27,25,28,30],
    "Salary":[5500,2000,60000,80000],
    "Performance Score":[85,98,10,75],
}

df=pd.DataFrame(data)
print(df)


#square brakects df["Column_name"]= some_data

df["Bonus"] = df["Salary"]*0.1  # create new COL
print(df) 

#using insert()
#df.insert(location,"Column_name",some_data)

df.insert(1,"Emplyee Id",[10,505,44,54])
print(df)