# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#numpy creates array which stores homogenues data

a=np.array([1,2,3,4,5,6])
print (a)
print(type(a))

#properties
print(a.ndim) # for n dimension
print(a.shape)
print(a.data) #for memory location of where data stoired
print(a.dtype) #type of data

b = np.ones((3,3)) # for create 2-D Array
print(b)


b = np.zeros((3,3)) # for create 2-D Array
print(b)


c = np.empty((4,4)) # for create 2-D Array
print(c)

d=np.array([[1,2,3],[5,6,7],[10,20,30]])
print (d)

d=np.arange(20)
print(d)


d=np.arange(2,20)
print(d)


d=np.arange(2,20,2)
print(d)

d=np.arange(2,20,2).reshape((3,3), order='F')   #starting from 2 with diffrence 2 until 20 order by rowwise
print(d)

d=np.arange(2,20,2).reshape((3,3), order='C')  #starting from 2 with diffrence 2 until 20 order by rowwise
print(d)

e=np.arange(10,28,2).reshape((3,3), order='F') #starting from 10 with diffrence 2 till 28
print(e)

f=d+e
print(f)

f=d-e
print(f)

#membership multipliccation
f=d*e
print(f)

f=np.dot(d,e)
print(f)

print(d)
print(np.sum(d))

print(np.sum(d,axis=1))  #0 for vertical sum & 1 for horizontal 

print(np.mean(d,axis=0))  # for mean of vertical value
print(np.mean(d,axis=1))  # for mean of horizontal value
print(np.median(d))


a=np.array([1,2,3])
b=np.array([10,20,30])

f=np.vstack((a,b))  # for create matrix row column wise but vertically as above data assign
print(f)

d=np.hstack((a,b))  # for create matrix row column wise but horizontally as above data assign
print(d)

'''
ihyujhvf v
jmnjnhb jnbg
kjn kmnh
'''

a=np.arange(50).reshape(5,10)
print(a)
print(a[1:4,2:8])   #1:4 specific row and 2:8 means in column 
print(a[1:,2:])  #[row starting : row ending],[column starting : columjn ending]
print(a[:5,3:])
print(a[:5,-1])   # -1 means last column

a=np.arange(20)
print(a)

print(a[a>5])

b=a[a>7]
c=b[b%5==0]
print(c)

a=np.arange(50).reshape(5,10)
# reverse the rows or columns based on axis
#b=np.flip(a,axis=0) #reverse column from bottom
b=np.flip(a,axis=1) #reverse rows from last
print(b)



