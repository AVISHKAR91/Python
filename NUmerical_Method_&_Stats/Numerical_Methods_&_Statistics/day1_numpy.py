# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:21:46 2022

@author: dhpcap
"""

import numpy as np

a=np.array([1,2,3,4,5,6])
print(a)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)

a=np.zeros(10, dtype='int')
print(a)

a=np.ones((3,5), dtype='float')
print(a)

a=np.full((3,5),1.23)
print(a)

a=np.arange(0,20,2)
print(a)
array7=np.arange(6)
print(array7)
array8 = np.arange(-2,24,4)
print(array8)

b=np.linspace(0,1,6)
print(b)

i=np.eye(3)   #identity matrix
print(i)

c=np.random.normal(0,1,(3,3))
print(c)


d=np.random.seed(4)
print(d)
x1=np.random.randint(10,size=6)   #1-D RANDOM ARRAY
print(x1)
x2=np.random.randint(10,size=(3,4))  #2-D Random array
print(x2)
x3=np.random.randint(10,size=(3,4,5))
print(x3)
d=np.empty((2,3))
print(d)

a=np.random.randint(10,size=(3,4))
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.T)


arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)

arr=np.arange(40)
newarr=arr.reshape(5,4,2)
print(newarr) 

A = np.array([4,7,3,4,8])
print(A==4)
print(A<5)

B=np.arange(12)
print(B)
print(B>5)

a=np.array([1,2,3])
b=np.array([True,True,False])
c=a[b]
print(c)

a=np.arange(1,10)
b=a>5
print(b)
c=a[b]
print(c)

a=np.array([[1,2,3],
           [4,5,6],
           [7,8,9]])
indices=np.array([[False,False,True],
                 [False,False,True],
                 [False,False,True]])


print(a[indices])

a=np.array([3,4,610,24,89,45,43,46,99,100])
print(a)
print(a%3!=0)
print(a%5==0)

b=(a%3)==0 
c=(a%5)==0
print(np.logical_or(a%3==0 , a%5==0))
    
a[a%3==0] =42
print(a)

array1 = np.array([[3,6],[4,2]])
array2 = np.array([[10,20],[15,12]])

array3=array1+array2
array4=array1-array2
array5=array1*array2     #multiplicatiplication
array6=array1@array2     #matrix multiplicatiplication
array7=array2/array1
array8=array2%array1

print(array1**3)
print(array3)
print(array4)
print(array5)
print(array6)
print(array7)
print(array8)

demoarray=np.array([[10,-7,0,20],
                    [-5,1,200,40],
                    [30,1,-1,4]])
demoarray.transpose()


    






















