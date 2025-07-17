import pandas as pd

data ={
    "Name":['fahad','nida','bukhtawar','ali'],
    "Age":[47,24,28,30],
    "Salary":[70000,2000,60000,80000],
    "Performance_Score":[85,98,10,75],
}

df=pd.DataFrame(data)

high_salary=df[df['Salary'] >50000]

print("Employee with salary >50000")
print(high_salary)

# filtering rows salary >50k AND age  >30

filtered=df[(df['Age']>30) & (df['Salary']>50000)]
print("Employee with Age >30 +salary >50000")
print(filtered)
# filtering rows salary >50k OR age  >30
print("Employee with OR")
filtered_or =df[(df['Age'] > 30) | (df['Performance_Score'] > 50)]
print(filtered_or)