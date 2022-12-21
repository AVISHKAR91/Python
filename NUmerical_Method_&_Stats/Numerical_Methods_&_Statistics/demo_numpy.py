# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:38:34 2022

@author: dhpcap
"""
import numpy as np
a=np.arange(1,10).reshape(3,3)
b=np.arange(11,20).reshape(3,3)
print(a)
print(b)

SUM=np.sum(a)
print(SUM)
x=np.sum(a, axis=0)
print(x)
y=np.sum(a, axis=1)
print(y)
print(np.vstack(y))

concat =np.concatenate((a,b), axis=1)
print(concat)

array1=np.array([4,5,6])
array2=np.array([[1,2,3],[14,15,16]])
print(np.vstack((array1,array2)))

a=np.arange(1,11)
print(a)
print(np.array_split(a, 2))