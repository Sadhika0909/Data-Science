import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=pd.read_csv("Data.csv")
X=a.iloc[:,:-1].values
y=a.iloc[:,-1].values
print(X)
print(y)

#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X)

#Encoding categorial data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder 
td=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
X=np.array(td.fit_transform(X))
print(X)

#Encoding dependent variable
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)
print(y)

#splitting the dataset into the trainingset and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
#scaling the training set excluding one hot encoded columns
X_train[:,3:]=sc.fit_transform(X_train[:,3:])
X_test[:,3:]=sc.transform(X_test[:,3:])
print(X_train)
print(X_test)