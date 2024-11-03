import numpy as np
import time

l=[1,34,6,12,9,50,18,47,43,29,3,30]
a=np.array(l)
print(a)

ar=a.reshape(3,4) 
print(ar)

for i in l:
    print(i*2)

print(ar[ar>30])
ar[ar%2==0]=-1
print(ar)

l1=[3,1,24,45,12,32,11,38]
a1=np.array(l1)
print(a1)

print(np.random.permutation(a1))
print(np.random.permutation(a1))
print(np.random.permutation(a1))

#combining arrays
a2=np.arange(1,9)
a3=np.arange(9,17)
aa=np.vstack((a2,a3))
print(aa)
aa1=np.hstack((a2,a3))
print(aa1)

