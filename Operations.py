import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#maching learning and evaluation tools
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

data=pd.read_csv("adult.csv")

data.columns=["Age","Job_type","ID_nb","Degree","Ed_exp","Mariatal_status","Job","Relationship","Race","Gender","Capital_gain","Capital_loss","Hours","Origin","Salary"]
data.rename(columns={"Job_type":"job type","ID_nb":"id nb","Ed_exp":"ed exp","Mariatal_status":"mariatal","Capital_gain": "capital gain","Capital_loss":"capital loss"},inplace=True)

data=data.replace("?",np.nan)
data.dropna(inplace=True)

#converting income to numeric
data["Salary"]=data["Salary"].apply(lambda x:1 if x.strip() == " >50K" else 0)
data["Gender"]=data["Gender"].apply(lambda x:1 if x.strip() == " female" else 0)
plt.figure(figsize=(8,4))
sns.histplot(data["Age"])
plt.title("Histogram")
plt.show()
