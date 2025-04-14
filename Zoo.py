import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas.plotting import scatter_matrix
import plotly.graph_objects as go

data=pd.read_csv("zoo.csv")

data.columns=["animal_name","hair","feathers","eggs","milk","airborne","aquatic","predator","toothed","backbone","breathes","venomous","fins","legs","tail","domestic","catsize"]

print(data.describe()) 
print(data.info()) 
print(data.isnull().sum())
print(data.isin(["?"]).sum(axis=0))

for i in data.columns:
    print("----%s---"% i)
    print(data[i].value_counts())

data.drop(["eggs","milk","toothed","backbone","catsize"],axis=1,inplace=True)

legs=set(data["legs"])
print(legs)

data["domestic"]=data["domestic"].map({0:0,1:1}).astype(int)
print(data.head())
data["hair"]=data["hair"].map({0:0,1:1}).astype(int)
print(data.head())
data["feathers"]=data["feathers"].map({0:0,1:1}).astype(int)
print(data.head())
data["venomous"]=data["venomous"].map({0:0,1:1}).astype(int)
print(data.head())

data.groupby("hair").legs.mean().plot(kind="bar")
plt.show()

data.groupby("feathers").legs.mean().plot(kind="bar")
plt.show()

data.groupby("venomous").legs.mean().plot(kind="bar")
plt.show()

data.groupby("domestic").legs.mean().plot(kind="bar")
plt.show()