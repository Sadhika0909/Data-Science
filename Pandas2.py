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


