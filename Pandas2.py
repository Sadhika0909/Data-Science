import pandas as pd

data=pd.read_csv("titanic.csv")

ad=data.loc[data["Age"]<18,"Name"]
print(ad)

sf=data.loc[(data["Sex"]=="female")&(data["Survived"]==1),"Name"]
print(sf)

#manipulitating data
data.iloc[0:3,3]="Sadhika"
print(data["Name"])
data.to_csv("Changeddata.csv")

#slicing a set of rows amd columns
print("Slicing your data:\n",data.iloc[9:25,2:5]) 

#creating new columns in the dataframe
data["Test"]=data["Fare"]+2
data["Test2"]=data["Fare"]*data["Pclass"]
print(data.head())

data["S/S"]=data["Siblings/Spouses Aboard"]+5
print(data.head())

#Renaming columns
datar=data.rename(columns={"Pclass":"Passenger Class","Parents/Children Aboard":"Parents/Children"})
print(datar.info())

#using agg() to perform multiple aggrications on columns
print(data.agg({"Age":["min","max","median"],"Fare":["min","max","median"]}))

#grouping data and calculating mean
print(data[["Sex","Age"]].groupby("Sex").mean())

#Counting the passengers in each Pclass
print(data["Pclass"].value_counts())
print(data["Survived"].value_counts())

#Sorting data
print(data.sort_values(by="Age"))
print(data.sort_values(by=["Age","Pclass"],ascending=False))


