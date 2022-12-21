# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:41:35 2022

@author: dhpcap
"""

import pandas as pd
mydata=pd.read_table("http://bit.ly/chiporders")
print(mydata)
print(mydata.shape)

print(mydata[["order_id","quantity"]].head()) #only head data show
print(mydata[["order_id","quantity"]].tail()) #only tail data show

x=mydata[["order_id"]]
print(type(x))

print(mydata.info())

mydf=pd.read_csv(r"F:\CDAC\Analytics Using python\studentdata11.csv")
print(mydf)
print(mydf.isnull())
print(mydf.describe())
print(mydf.info())

# To delete all rows which has null or nan value in atleast one column
mydf.dropna(inplace=True)
print(mydf)

#To delete row if the row has less than 2 not null values
mydf.dropna(thresh=2,inplace=True)  
print(mydf)

#delete only if all values in the row are null
mydf.dropna(how='all', inplace=True)
print(mydf)

mydf.fillna(0, inplace=True)
print(mydf)


mymovies=pd.read_table("http://bit.ly/movieusers", sep="|", header=None)
print(mymovies)