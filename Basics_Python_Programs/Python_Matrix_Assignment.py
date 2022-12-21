# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:23:29 2022

@author: dhpcap
"""
#Q1.
import numpy as np
a=np.array([1,2,3,2,7,8])
a=np.array(a).reshape(2,3)
print(a)
b=np.array([1,3,9,8,2,6]).reshape(3,2)
print(b)
mul = a@b
print(mul)

#Q2. 

a = np.array([1,6,9,0,3,3,8,2,5]).reshape(3,3)
print(a)
print(f"Before swapping:",a[0])
print(f"Before swapping:",a[1])
a[[0,1]] = a[[1,0]]   
print(f"After swapping :",a[0])
print(f"After swapping :",a[1])

R1=a[0]
print(R1)
R2=a[1]
print(R2)
R1=R1*5
print(R1)
print(a[2])
R3=a[2]
print(R3)
sub = R1-R3
print(sub)

#Q3
A=np.array([1,6,9,-20,3,-3,8,-13,5]).reshape(3,3)
print(A)
D=np.triu(A, k=0)
print(D)
D[1]=D[1]/3
D[2]=D[2]/5
print(D[1])
print(D[2])
print(D)

#Q4
#let us consider x=2
x=2
y=[1/(x**n) for n in range(12)]
print(f"Sum is:", sum(y))
    


import matplotlib.pyplot as plt

# let x is from 0 to 10
X = np.arange(11)
Y = [(np.sin(3*x) + np.cos(x*x) + 5) for x in X]
plt.subplot()
plt.plot(X, Y, linewidth=2.0)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X VS Y')
plt.grid()
plt.show()



