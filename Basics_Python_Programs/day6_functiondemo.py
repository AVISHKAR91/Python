# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:50:10 2022
practise
@author: dhpcap
"""
'''
ans="y"
while ans=="y":
    str1=input("enter a string")
    mid=len(str1)//2
    print(str1[mid-1:mid+2])
    ans=input("continue(y/n)?")
'''
  
def getStringMiddle (str1):
    mid = len(str1)//2
    return str1[mid-1:mid+2]

ans="y"
while ans=="y":
    str1=input("Enter a string")
    s=getStringMiddle(str1)
    print(s)
    ans=input("continue(y/n)?")
    

