# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:34:01 2022

@author: dhpcap
"""

import pandas as pd
import numpy as np
df = pd.read_csv("F:\CDAC\Analytics Using python\weather_data_missing.csv")
df

new_df =df.replace(6, value=np.NaN)
new_df

new_df = df.replace(to_replace = [32,9], value=7)
new_df
 
