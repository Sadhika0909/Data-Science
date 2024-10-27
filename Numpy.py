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

#Permutation 
print(np.random.permutation(a4))
print(np.random.permutation(a4))
print(np.random.permutation(a4))

#Random number
ar=np.random.randint(4,20,9)
print(ar)
n1=np.random.permutation(ar)
print(np.random.permutation(ar))
aa=np.random.randint(5,35,(4,5))
print(aa)

#sorting the array
print(n1)
print(np.sort(n1))
print(n1)

l=[3,2,77,11,4,98]
l.sort()
print(l)

#string slicing
str="Sadhika is beautiful"
print(str[1:5])
print(str[5:15])

#Array slicing 
print(n1[2:7])
print(n1[:8])
print(n1[::-1])
print(n1)

#select indices
print(n1[[4,2,3,1,6]])

#conditional slicing
print(n1[n1%2==0])
print(n1[n1>5])
print(n1[n1%3==0])

#2D array slicing
print(aa[0:1,1:])
print(aa)
print(aa[1:3,:2])

#Operators with arrays
aa1=np.arange(1,5)
print(aa1)
aa2=np.arange(6,10)
print(aa2)
print(aa1+aa2)
