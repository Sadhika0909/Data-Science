import matplotlib.pyplot as plt

test_scores=[94,74,29,85,53,76,70,100,86,88,81,40,50,65,13]
bins=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(test_scores,bins,histtype="bar",rwidth=0.7)
plt.xlabel("Test Scores")
plt.ylabel("Frequency")
plt.title("Histogram of test scores of students in intervals")
plt.show()

practicing_sport=[2,3,6,11,14,16,17]
scores=[5,1,2,3,2,2,3,]
plt.scatter(practicing_sport,scores,label="Scattered plot",color="blue",marker="o",s=75)
plt.xlabel("Hours spent practicing a sport")
plt.ylabel("Scores in a tournament")
plt.title("Scattered plot of the relationship between hours spent practicing a sport and scores in a tournament")
plt.legend()
plt.show()

expenses=[4,1,56,9,3]
activities=["fun","basic necessities","food","rent","saving"]
color=["g","r","b","c","m"]
plt.pie(expenses,labels=activities,colors=color,startangle=90,shadow=True)
plt.title("Pie chart representing the distribution of expenses in a month")
plt.show()

days=[1,2,3,4,5,6,7]
social_media=[9,1,5,7,10,7,12]
streaming=[9,10,11,11,9,7,11]
gaming=[7,6,9,8,7,8,7]
studying=[2,10,8,12,9,8,7]
#adding labels for the legend
plt.plot([],[],color="c",label="Social Media",linewidth=5)
plt.plot([],[],color="m",label="Streaming",linewidth=5)
plt.plot([],[],color="b",label="Gaming",linewidth=5)
plt.plot([],[],color="g",label="Studying",linewidth=5)
plt.stackplot(days,social_media,streaming,gaming,studying,colors=["c","m","b","g"])
plt.xlabel("Days")
plt.ylabel("Hours")
plt.title("Stack plot representing the weekly usage of smartphone in different activities")
plt.legend()
plt.show()