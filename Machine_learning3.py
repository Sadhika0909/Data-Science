import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data=pd.read_csv("Fruit.csv")
print(data.head())
print(data.info())

data["fruit_type"]=data["fruit_type"].replace({"Apple":0,"Orange":1,"Banana":2,"Grapes":3})

plt.scatter(data["fruit_sweetness"],data["fruit_type"],color="magenta")
plt.xlabel("Fruit Sweetness")
plt.ylabel("Fruit type(0,1,2,3)")
plt.show()


x=data.drop("fruit_type",axis=1)
y=data["fruit_type"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

model=DecisionTreeClassifier(max_depth=4,random_state=1)
model.fit(x_train,y_train)

predictions=model.predict(x_test)

print("Accuracy: ",metrics.accuracy_score(predictions,y_test)*100,"%")