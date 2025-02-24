import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas.plotting import scatter_matrix

data=pd.read_csv("adult.csv")

#renaming the columns
data.columns=["Age","Job_type","ID_nb","Degree","Ed_exp","Mariatal_status","Job","Relationship","Race","Gender","Capital_gain","Capital_loss","Hours","Origin","Salary"]

#printing basic informaton about the data set
print(data.describe()) #showing summary
print(data.info()) #showing column name and how many values there are
print(data.isnull().sum())