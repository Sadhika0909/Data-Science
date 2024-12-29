import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=pd.read_csv("Data.csv")
x=a.iloc[:,:-1].values
y=a.iloc[:,-1].values
print(x)
print(y)

#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])
print(x)

#Encoding categorial data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder 
td=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
x=np.array(td.fit_transform(x))
print(x)
