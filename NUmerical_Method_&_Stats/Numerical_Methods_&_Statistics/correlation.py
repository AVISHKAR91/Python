# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:45:49 2022

@author: dhpcap
"""

import pandas as pd
import seaborn as sns

data= {'A':[4,5,10,6,7,8,8,10],
       'B':[12, 14, 11, 7,8,8,9,13],
       'C':[22, 24, 26,10, 26,29,32,56]}

df = pd.DataFrame(data, columns=['A','B','C'])

df.corr()


df.corr().round(3)
corr=df.corr()
print(corr)

sns.heatmap(corr, cmap ="YlGnBu", linewidths= 0.1)