import numpy as np
import time

list=[6,23,100,2,36,3,777]
print(type(list))
print(list)

arr=np.array(list)
print(type(arr))
print(arr)

for i in list:
    print(i*5)
print(arr*5)

t1=time.time()
l=[i for i in range(1000000000001)]
t2=time.time()
print("Duration for list ",t2-t1)
t1=time.time()
a=np.arange(0,1000000000001)
t2=time.time()
print("Duration for list ",t2-t1)

ar=np.ones(7,int)
print(ar)

ar1=np.zeros((6,5))
print(ar1)

ar2=np.ones((3,10))
print(ar2)

print(ar1.shape)
print(ar2.shape)

print(ar1.size)
print(ar2.size)

ar3=np.arange(10,100,20)
print(ar3)

ar4=np.linspace(45,60,5)
print(ar4)

ar5=ar3.reshape(4,5)
print(ar5)