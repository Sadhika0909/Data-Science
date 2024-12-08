import matplotlib.pyplot as plt

#histogram
ages=[1,4,20,15,53,76,30,100,26,18,21,40,50,5,13]
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins,histtype="stepfilled",rwidth=0.6)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of age intervals")
plt.show()

#scattered plot
x=[1,2,3,4,5,7,8,9]
y=[0,1,0,1,1,1,0,1]
plt.scatter(x,y,label="Scattered plot",color="green",marker="o",s=72)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Scattered plot")
plt.legend()
plt.show()

#pie chart
slices=[4,1,16,9,13]
activities=["sleeping","drawing","reading","homework","eating"]
color=["r","g","b","m","c"]
plt.pie(slices,labels=activities,colors=color,startangle=90,shadow=True)
plt.title("Pie chart")
plt.show()

#stack plot
days=[1,2,3,4,5,6,7]
eating=[9,1,5,7,10,7,12]
sleeping=[9,10,11,11,9,7,11]
homework=[7,6,9,8,7,8,7]
reading=[2,10,8,12,9,8,7]
#adding labels for the legend
plt.plot([],[],color="m",label="Eating",linewidth=5)
plt.plot([],[],color="c",label="Sleeping",linewidth=5)
plt.plot([],[],color="r",label="Homework",linewidth=5)
plt.plot([],[],color="b",label="Reading",linewidth=5)
plt.stackplot(days,eating,sleeping,homework,reading,colors=["m","c","r","b"])
plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Stack plot of activities")
plt.legend()
plt.show()

#Subplot
import numpy as np

def waves(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
#generate time intervals for plotting
t1=np.arange(0,5,0.1)
t2=np.arange(0,5,0.2)
plt.figure()
#first subplot
plt.subplot(222)
plt.plot(t1,waves(t1),"mo")
plt.title("Exponential Decay with Cosine(Coarse)")
#second subplot
plt.subplot(223)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.title("Cosine Wave (Fine)")
plt.tight_layout()
plt.show()
