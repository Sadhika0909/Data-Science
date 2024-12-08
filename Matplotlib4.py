import matplotlib.pyplot as plt
import numpy as np

#Bar Chart
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
sales=[124,220,294,155,187,299,279]
plt.bar(days,sales,color="cyan")
plt.xlabel("Days of the week")
plt.ylabel("Number of sales")
plt.title("Weekly sales")
plt.show()

#Line graph
hours=np.arange(1,11,1)
temperature=[27,28,30,30,30,31,32,33,35,32]
plt.plot(hours,temperature,marker="o",linestyle="-",color="magenta")
plt.xlabel("Hours")
plt.ylabel("Temperature")
plt.title("Temperature throughout the day")
plt.grid(True)
plt.show()

#Box Plot
english=[17,17,18,20,21,21,21,21,22,23]
physics=[16,16,16,19,22,22,25,27,27,27]
maths=[17,22,22,22,22,22,25,25,28,29]
plt.boxplot([english,physics,maths],label=["English","Physics","Maths"],patch_artist=True)
plt.title("Box Plot of subject grades")
plt.ylabel("Scores")
plt.show()

