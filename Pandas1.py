import pandas as pd


data=pd.read_csv("titanic.csv")

print(data.head())
print(data.shape)
print(data["Survived"])
print(data["Pclass"])
print(data["Age"].max())
print(data["Sex"].shape)
print(data["Siblings/Spouses Aboard"])
print(data["Parents/Children Aboard"])
print(data["Fare"].max())
print(data.info())
print(data.describe())

col=data[["Age","Survived"]]
print(col.head())
print(col.shape)

#filtering data based on condition
ps=data[data["Age"]>35]
print(ps.head())
print(ps.shape)

s=data[data["Sex"]=="female"]
print(s.head())
print(s.shape)

#multiple  conditions
c=data[data["Pclass"].isin([1,2])]
print(c[["Name","Pclass"]].head())
print(c.shape)

age=data[(data["Age"]>18)&(data["Age"]<50)]
print(age[["Name","Age"]].head())
print(age.shape)

f1=data[(data["Sex"]=="male")&(data["Pclass"]==1)]
print("The mean fare of the male passengers in 1st class: ",f1["Fare"].mean)

f3=data[(data["Sex"]=="female")&(data["Pclass"]==3)]
print("The mean fare of female passengers in 3rd class is: ",f3["Fare"].mean)

aage=data[(data["Survived"]==1)]
print("The average age of all the people who survived is: ",aage["Age"].mean)
