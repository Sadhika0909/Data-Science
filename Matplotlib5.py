import matplotlib.pyplot as plt
import numpy as np

scores=[31,94,20,75,53,76,90,100,86,88,61,42,50,55,13]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(scores,bins,histtype="step",rwidth=0.7)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Histogram of scores in a math test")
plt.show()

x=[1,2,3,4,5,7,8,9]
y=[0,1,6,4,2,5,5,1]
plt.scatter(x,y,label="Scattered plot",color="blue",marker="o",s=77)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph:scattered plot")
plt.legend()
plt.show()

colors=["m","c","b","r","g"]
slices=[5,12,2,9,14]
hobbies=["playing","drawing","reading","writing","watching TV"]
plt.pie(slices,labels=hobbies,colors=colors,startangle=90,shadow=True)
plt.title("Pie chart of favorite indoor hobbies")
plt.show() 

days=[1,2,3,4,5,6,7]
playing=[9,1,5,7,10,7,12]
drawing=[9,10,11,11,9,7,11]
reading=[2,10,8,12,9,8,7]
watchingTV=[7,6,9,8,7,8,7]
plt.plot([],[],color="c",label="Playing",linewidth=6)
plt.plot([],[],color="m",label="Drawing",linewidth=6)
plt.plot([],[],color="r",label="Reading",linewidth=6)
plt.plot([],[],color="g",label="Watching TV",linewidth=6)
plt.stackplot(days,playing,drawing,reading,watchingTV,colors=["c","m","r","g"])
plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Stack plot of favorite hobbies")
plt.legend()
plt.show()

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
itemsBought=[284,134,222,177,155,299,269]
plt.bar(days,itemsBought,color="magenta")
plt.xlabel("Days of the week")
plt.ylabel("Number of items bought")
plt.title("Weekly count of items bought")
plt.show()

hours=np.arange(1,11,1)
temperature=[7,8,10,10,10,11,12,13,13,10]
plt.plot(hours,temperature,marker="o",linestyle="-",color="green")
plt.xlabel("Hours")
plt.ylabel("Temperature")
plt.title("Temperature throughout the day")
plt.grid(True)
plt.show()

sociology=[17,22,22,22,24,26,22,22,19,20]
history=[16,16,16,19,22,22,25,25,28,29]
english=[17,17,18,20,21,21,21,21,22,23]
plt.boxplot([english,sociology,history],label=["English","Sociology","History"],patch_artist=True)
plt.title("Box Plot of subject grades")
plt.ylabel("Scores")
plt.show()