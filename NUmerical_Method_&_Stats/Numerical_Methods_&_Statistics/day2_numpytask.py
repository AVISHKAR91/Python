# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:00:50 2022

@author: dhpcap
"""
'''
1. Element-wise addition of 2 numpy arrays
 Given are 2 similar dimensional numpy arrays, how to get a numpy array output
in which every element is an element-wise sum of the 2 numpy arrays?
'''
import numpy as np

a=np.arange(1,10).reshape(3,3)
print(a)
b=np.arange(11,20).reshape(3,3)
print(a)

add = a +b
print(add)

'''
2. Multiplying a matrix (numpy array) by a scalar
 Given a numpy array (matrix), how to get a numpy array output which is equal to
the original matrix multiplied by a scalar?
'''
a=np.arange(1,10).reshape(3,3)
b=np.arange(11,20).reshape(3,3)
mul=a*b
print(mul)

'''
3. Identity Matrix
 Create an identity matrix of dimension 4-by-4
'''
print(np.eye(4))

'''
4. Array re-dimensioning
 Convert a 1-D array to a 3-D array
'''
onedim=np.arange(1,10)
print(onedim)
threedim=onedim.reshape(3,3)
print(threedim)

'''
5. Array datatype conversion
 Convert all the elements of a numpy array from float to integer datatype
'''

a=np.array([12.4, 5.5, 6.7, 9.8, 3.5])
print(a)
print(type(a))
a=a.astype(int)
print(a)

'''
6.	Obtaining Boolean Array from Binary Array
•	Convert a binary numpy array (containing only 0s and 1s) to a booleannumpy array
'''
a=np.array([[0,0,0,1],[1,0,1,0],[1,0,1,1],[0,1,0,0]])
print(a)
a=a.astype(bool)
print(a)

'''
7.	Horizontal Stacking of Numpy Arrays
•	Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in 2D arrays)
'''
a=np.arange(12).reshape(2,6)
print(a)
b=np.arange(12,24).reshape(2,6)
print(b)
d=np.hstack((a,b))
print(d)

'''
8.	Vertically Stacking of Numpy Arrays
•	Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)
'''
f=np.vstack((a,b))
print(f)

'''
9.	Custom Sequence Generation
•	Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
'''
a=np.arange(0,100,2)
print(a)

'''
10.	Getting the positions (indexes) where elements of 2 numpy arrays match
•	From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
'''
x=np.array([0,2,3,4,5,6,8])
y=np.array([11,2,3,1,9,7,8])

z=np.where(x==y)
print(z)

'''
11.	Generation of given count of equally spaced numbers within a specified range
•	Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)
'''
demo=np.linspace(0, 100, num=5)
print(demo)

'''
12.	Matrix Generation with one particular value
•	Output a matrix (numpy array) of dimension 2-by-3 with each and every value equal to 5

'''
matrix1 =np.arange(6).reshape(2,3)
print(matrix1)
xyz=np.five((2,3))
print(xyz)

'''
13.	Array Generation of random integers within a specified range
•	Output a 5-by-5 array of random integers between 0 (inclusive) and 10 (exclusive)
'''
a=np.random.randint(10,size=(5,5))
print(a)

'''
14.	Matrix Multiplication
•	Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices (as a numpy array)
'''

arr1 = np.arange(1,10).reshape(3,3)

'''
15.	Matrix Transpose
•	Output the transpose of a matrix (as numpy array)
'''
print(a)
print(a.T)























