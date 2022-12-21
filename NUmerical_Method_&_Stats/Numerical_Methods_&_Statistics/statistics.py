# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:22:25 2022

@author: dhpcap
"""

#Lab (Python)

data = [9,9,9,8,8,8,8,7,7,7,7,7,6,6,6,6,6,6,5,5]
mean = sum(data) / len(data)
print("Mean : ", mean)

deviation_from_Mean = sum((v - mean) for v in data)
print("Deviation_from_Mean : ", deviation_from_Mean)

squared_deviation= sum((v - mean) ** 2 for v in data)
print("Squared_Deviation : ", squared_deviation)

variance = sum((v - mean) ** 2 for v in data) / len(data)
print("variance : ", variance)

standard_deviation=variance**0.5
print("standard_deviation : ", standard_deviation)





# ------------------------------------------------------------
import numpy as np
print("Mean : ", np.mean(data))
print("variance : ", np.var(data))
print("standard_deviation : ", np.std(data))