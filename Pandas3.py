import pandas as pd

data=pd.read_csv("titanic.csv")

print(data.head())

ad=data.loc[data["Fare"]>50,["Name","Age"]]
print(ad)

print("Slicing your data:\n",data.iloc[10:20,2:5]) 

data.iloc[0:3,4]=25
print(data["Age"])

data["Age In Months"]=data["Age"]*12
print(data.head())

data1=data.rename(columns={"Fare":"Ticket Fare"})
print(data1.info())

print(data[["Fare","Pclass"]].groupby("Pclass").mean())
print("@@@@@@@@@@@@")

a=data.sort_values(by="Age",ascending=False)
print(a.head(3))

data["Name Uppercase"]=data["Name"].str.upper()
print(data.head())

data.to_csv("titanic_summary.csv")


