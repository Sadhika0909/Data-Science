import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("titanic.csv")

gendercount=data["Sex"].value_counts()
plt.bar(gendercount.index,gendercount.values,color="cyan")
plt.xlabel("Gender")
plt.ylabel("Total amount in the titanic")
plt.title("Total amount of male and female in the titanic")
plt.show()

n=data.groupby("Sex")["Fare"].mean()
plt.bar(n.index,n.values,color="cyan")
plt.xlabel("Gender")
plt.ylabel("Average fare")
plt.title("Average fare of male and female in the titanic")
plt.show()


pclass=data["Pclass"].value_counts()
color=["r","b","m"]
plt.pie(pclass,labels=["1st class","2nd class","3rd class"],colors=color,startangle=90,shadow=True)
plt.title("Pie chart")
plt.show() 
