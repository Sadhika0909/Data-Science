import numpy as np
import time

list=[1,54,92,233,22,44,12]
print(type(list))
print(list)

#converting list into a numpy array
arr=np.array(list)
print(type(arr))
print(arr)

#multiplying each element with a number
for i in list:
    print(i*2)

print(arr*2)

#mesuring time to create 1 million elements
t1=time.time()
l=[i for i in range(1000000)]
t2=time.time()
print("Duration for list ",t2-t1)

t1=time.time()
a=np.arange(0,1000000)
t2=time.time()
print("Duration for list ",t2-t1)

#creating a numpy array of zeros with five elements
ar=np.zeros(5,int)
print(ar)

#creating an array with 5 rows and 2 columns
a1=np.ones((5,2))
print(a1)

a2=np.zeros((3,4))
print(a2)

#printing the shape of arrays
print(a1.shape)
print(a2.shape)

#printing the size of arrays
print(a1.size)
print(a2.size)

#creating a numpy array using np.arange
a3=np.arange(22,63,4)
print(a3)

#creating a numpy array using linspace
a4=np.linspace(10,22,4)
print(a4)

#reshaping the array
a5=a4.reshape(2,2)
print(a5)