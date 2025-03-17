import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas.plotting import scatter_matrix
import plotly.graph_objects as go

data=pd.read_csv("adult.csv")

#renaming the columns
data.columns=["Age","Job_type","ID_nb","Degree","Ed_exp","Mariatal_status","Job","Relationship","Race","Gender","Capital_gain","Capital_loss","Hours","Origin","Salary"]
data.rename(columns={"Job_type":"job type","ID_nb":"id nb","Ed_exp":"ed exp","Mariatal_status":"mariatal","Capital_gain": "capital gain","Capital_loss":"capital loss"},inplace=True)

#printing basic informaton about the data set
print(data.describe()) #showing summary
print(data.info()) #showing column name and how many values there are
print(data.isnull().sum())
print(data.isin(["?"]).sum(axis=0))

for i in data.columns:
    print("----%s---"% i)
    print(data[i].value_counts())

#dropping unused data from the dataset
data.drop(["ID_nb","Mariatal_status","Capital_gain","Capital_loss","Origin"],axis=1,inplace=True)

#unique categories
a=set(data["Salary"])
print(a)

#mapping the data into numarical data using map function
data["Salary"]=data["Salary"].map({" <=50K":0," >50K":1}).astype(int)
print(data.head())
data["Gender"]=data["Gender"].map({" Male":0," Female":1}).astype(int)
print(data.head())
data["Race"]=data["Race"].map({" White":0," Black":1," Asian-Pac-Islander":2," Amer-Indian-Eskimo":3," Other":4})
data["mariatal"]=data["mariatal"].map({" Married-civ-spouse":0," Never-married":1," Divorced":2," Separated":3," Widowed":4," Married-spouse-absent":5," Married-AF-spouse":6})
#data["Degree"]=data["Degree"].map({""})


a=data.groupby("Race").sum()
figure1=go.Figure()
figure1.add_trace(go.Bar(x=a.index,y=a["Race"],fill="tonexty",line_color="red"))
figure1.update_layout(title="Different races")
figure1.write_html("bargraph.html",auto_open=True)
