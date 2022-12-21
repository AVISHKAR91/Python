# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:05:05 2022

@author: dhpcap
"""
def getStringmiddle(str1):
    mid=len(str1)//2
    return str1[mid-1:mid+2]

ans= "y"
while ans=="y":
    str1=input("Enter A String:")
    s=getStringmiddle(str1)
    print(s)
    ans=input("continue (y/n)?")
    

#return factorial of number
def factorial(n):
    '''This function returns factorial of a number'''
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter a number:"))
ans = factorial(num)
print(ans)

#return addition of a and b
def addition(a=45, b=50):
    a=a+10
    b=b+15
    return a+b

ans=addition(5)
ans=addition(b=5, a=3)
print(ans)

def printTable(n):
    for i in range(1,11):
        print(f"{n}*{i} = {n*i}")
        
ans =printTable(7)
print(ans)