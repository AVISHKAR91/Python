# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 15:23:58 2022

@author: dhpcap
"""

'''
1.	How to create an empty and a full NumPy array of 4 by 2 ?
'''

import numpy as np
d=np.empty((2,3))
print(d)
f=np.full((4,2), 3.4)
print(f)

'''
2.	Create a Numpy array of 5 by 2  and filled with all zeros
'''
arr=np.zeros((5,2))
print(arr)

'''
3.	Create a Numpy array filled with all ones. (note create 1-D array fo 3 elements and 2-D array of 3 by 3 )
'''
a=np.arange(3)
print(a)
b=np.arange(1,10).reshape(3,3)
print(b)
x=np.ones(3)
y=np.ones((3,3))
print(x)
print(y)

'''
4.	Find the most frequent value in a NumPy array
'''
x = np.array([1,2,3,4,5,1,2,1,1,1])
print("Original array:")
print(x)

print("Most frequent value in the above array:")
print(np.bincount(x).argmax())

'''
5.	How to build an array of all combinations of two NumPy arrays?
{hint perform the addition of two array)
'''
a=np.arange(9).reshape(3,3)
b=np.arange(11,20).reshape(3,3)
add=a+b
print(add)

'''
6.	How to check whether specified values are present in NumPy array?
{hint: “in” operator is used to check whether certain element and values are present in a given sequence and hence return Boolean values ‘True” and “False“.)
'''
print(a)
if 22 in a:
    print("True")
else:
    print("False")

'''
7.	Flatten a 2d numpy array into 1d array
'''
a=np.arange(9).reshape(3,3)
b=a.reshape(-1)
print(b)

'''
8.	Counts the number of non-zero values in the array
'''
print(a)
cnt_non_zero = np.count_nonzero(a)
print(cnt_non_zero)

'''
9.	Count the number of elements along a given axis
(hint: In Python, numpy.size() function count the number of elements along a given axis.)
'''
a=np.arange(9).reshape(3,3)
b=np.size(a, axis=1)
print(b)
    
'''
10.	Change data type of given numpy array
(hint :-numpy.astype() function to change the data type of the underlying data of the given numpy array.

 '''
a=np.arange(9).reshape(3,3)
b=a.astype(float)
print(b)

'''
11.	Reverse a numpy array
'''
print(a)
b=a.reshape(-1)
rev=np.flip(b)
print(rev)

'''
12.	Hint  numpy.flip() function reverses the order of array elements along the specified axis. Or by using -1 , reversal of the array is possible
'''
print(a)
b=np.flip(a,axis=1)
print(b)

