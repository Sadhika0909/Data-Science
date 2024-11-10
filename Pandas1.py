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
