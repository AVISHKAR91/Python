# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 18:52:35 2022

@author: dhpcap
"""

import numpy as np
np.linspace(2.0, 3.0, num=5)

x=np.linspace(10, 50, num=5, endpoint=True)
print(x)


x=np.linspace(10, 50, num=5, endpoint=True)
print(x)

y=np.linspace(2.0, 3.0, num=5, retstep=True)
print(y)

a=np.arange(1,25).reshape((2,3,4)) #2*3*4=24(total values in array)
print(a)

print(a[0,0,1])
print(a[0,1,0])


print(np.identity(3)) # create identity matrix 3x3 column
print()
print(np.identity(4))

np.eye(3,4)
np.eye(3,4,k=1)
np.eye(3,4,k=-1)
np.eye(3,4,k=2)

