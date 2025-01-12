import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("titanic.csv")

gender=["Male","Female"]
number=data["Sex"]
plt.bar(gender,number,color="cyan")
plt.xlabel("Gender")
plt.ylabel("Total amount in the titanic")
plt.title("Total amount of male and female in the titanic")
plt.show()

g=data["Sex"]
n=data[["Sex","Fare"]].groupby("Sex").mean()

plt.bar(g,n,color="cyan")
plt.xlabel("Gender")
plt.ylabel("Average fare")
plt.title("Average fare of male and female in the titanic")
plt.show()

slices=[data["Fare"]]
pclass=[data["Pclass"]]
color=["r","b","m","c","g"]
plt.pie(slices,labels=pclass,colors=color,startangle=90,shadow=True)
plt.title("Pie chart")
plt.show() 
