import matplotlib.pyplot as plt

#plotting line graph for y=x
x=[1,2,3,4,5]
y=[1,2,3,4,5]

#plotting and showing the graph
plt.plot(x,y)
plt.show()

x=[3,10,17,24,25,31]
y=[0,6,8,13,18,21]
plt.plot(y,x)
plt.show()

#adding formatting to the graph
plt.plot(x,y,"b--")
plt.show()

#limiting the number on each axis
plt.plot(x,y)
plt.axis([0,10,0,200])
plt.show()

plt.plot(x,y)
plt.axis([0,60,0,100])
plt.show()

#adding label, title, line width and legend
plt.plot(x,y,"g--",label="y=x",linewidth=3)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Title")
plt.legend()
plt.show()

#plotting multiple graphs
plt.plot([1,3,5,7,9],[0,2,4,6,8],"b--",label="Y=X**2",linewidth=2)
plt.plot([0,2,3,4,9],[1,5,6,7,8],"r--",label="Y=X**3",linewidth=2)
plt.plot([1,4,5,7,10],[1,4,6,8,9],"go",label="Y=X**4",linewidth=1)
plt.axis([0,10,0,10])
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Graph")
plt.legend()
plt.show()
