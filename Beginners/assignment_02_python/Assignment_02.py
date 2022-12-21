# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:55:31 2022

@author: dhpcap
"""

import pandas as pd

mydf=pd.read_csv("F:\CDAC\Analytics Using python\product.csv")
print(mydf)

mydf.dropna(inplace=True)  #To delete all rows which has null or nan value in atleast one column
print(mydf)

mydf.dropna(thresh=3, inplace=True)  #To delete row if the row has less than 3 not null values
print(mydf)

mydf.dropna(how='all', inplace=True) # To delete row if all column have null values
print(mydf)

mydf.fillna('Avishkar', inplace=True)  #replace avishkar to null values
print(mydf)

mydf.describe()  #description of dataframe

print(mydf[['pro_name', 'price']].head())   #It show first 5 row 

print(mydf[['pro_name', 'price']].tail())   #It show last 6 row

mydf.info()  # It show information of dataframe




