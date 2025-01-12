#importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#loading the data
data=pd.read_csv("iris.csv")
#reading the first few rows
print(data.head())
#see the details of the data
print(data.info())

#data preprocessing
data["species"]=data["species"].replace({"setosa":0,"versicolor":1,"virginica":2})
#data visualization
plt.scatter(data["petal_length"],data["species"],color="green")
plt.xlabel("Petal Length")
plt.ylabel("Flower type(0,1,2)")
plt.show()

#splitting the data
x=data.drop("species",axis=1)
#flower type
y=data["species"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
#training the computer
model=DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
#testing the computer
predictions=model.predict(x_test)
#printing accuracy
print("Accuracy: ",metrics.accuracy_score(predictions,y_test)*100,"%")
