import pandas as pd

#creation of data frames
df=pd.DataFrame({"name":["Sadhika","Stuti","Tom","Ben"],"age":[15,16,17,16],"country":["India","India","USA","UK"]})
print(df.head())
print(df.shape)
print(df["name"])
print(df["age"].max())
print(type(df["age"]))
print(df["country"].shape)
print(df.info())
print(df.describe())