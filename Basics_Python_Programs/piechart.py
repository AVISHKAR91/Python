# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:24:21 2022

@author: dhpcap
"""

import matplotlib.pyplot as plt

slices=[10,20,30,40,50]
act=['excercise', 'sleeping','eating','working','playing']
cols=['green','blue','lightgreen','red','purple']

#plt.pie(slices,labels=activities,colors=cols,startangle=90,counterclock=False)
plt.pie(slices, labels=act,colors=cols,shadow=True, explode=(0,0,0.4,0,0),startangle=90)
plt.title('This my first in matplotlib piechart is on next line')
plt.show()