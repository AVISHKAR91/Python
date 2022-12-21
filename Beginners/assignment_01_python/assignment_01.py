# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:09:23 2022

@author: dhpcap
"""

#First Assignment of python analytics

import numpy as np
First_dealer=np.arange(60).reshape(10,6) # Yearwise sales of each item by first dealer
print(First_dealer) 

second_dealer=np.arange(61,121).reshape(10,6)  #Yearwise sales of each item by second dealer
print(second_dealer) 

both_dealers=First_dealer+second_dealer  #Find year wise sales of each item by both the dealers
print(both_dealers)

years = np.arange(2001,2011) #It prints 10 years as row
print(years)
Product = ["TV", "FreeZe", "Mobile", "W/M", "AC", "Dishwashers"] #It prints 6 products as column
print(Product)

print(years)
print(np.sum(a,axis=1))  # yearwise sales of first_dealer
print(years)
print(np.sum(b,axis=1))  # yearwise sales of second_dealer

print(First_dealer[1,0:]) #Display sales of a particular year for First dealer
print(second_dealer[6,0:]) #Display sales of a particular year for Second dealer

print(First_dealer[0: ,0:2]) #Display sales of TV and freeze for first dealer
print(second_dealer[0: ,0:2]) #Display sales of TV and freeze for second dealer








