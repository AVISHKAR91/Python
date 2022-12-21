# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:10:09 2022

@author: dhpcap
"""

import matplotlib.pyplot as plt

x=[1,2,3]
y=[4,5,6]

x2=[1,2,3]
y2=[6,7,8]

plt.plot(x,y, label="Polpulation", color="red")
plt.plot(x2,y2, label="senus", color="blue")

plt.xlabel('X-Axis',)
plt.xlabel('Y-Axis',)

plt.legend()
plt.grid()
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()