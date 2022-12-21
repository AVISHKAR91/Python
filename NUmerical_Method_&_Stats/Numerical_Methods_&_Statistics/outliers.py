# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:10:25 2022

@author: dhpcap
"""

import numpy as np

import scipy.stats as stats

data = np.array([14,20,19,22,24,26,27,30,30,31,36,38,44,47,200])

# calculate interquartile range
q3,q1 = np.quantile(data, [0.75,0.25])  
iqr = q3-q1
print(iqr) # display interquartilr range
z = np.abs(stats.zscore(data))
print(z)
data_clean = data [(z<3)]
print(data_clean) 













