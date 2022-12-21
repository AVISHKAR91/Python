# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:14:21 2022

@author: dhpcap
"""

import pandas as pd
import numpy as np

data= pd.read_csv("50_Startups.csv")
print(data)
print(data.head(10))
print(data.isnull())
print(data.duplicated('R&D Spend'))
print(data.info())
df=(data.drop_duplicates(subset=['R&D Spend']))
print(df)
print(len(df))
max_RnD = np.max(df['State'])
print(max_RnD)
