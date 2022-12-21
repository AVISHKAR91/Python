# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:03:28 2022

@author: dhpcap
"""
'''
Loops in Python

1. For Loop : If you know how many times you want to repeate
'''

for i in range(5): #0,1,2,3,4
    print(i)
    
for A in range(10, 20):
    print(A)
    
for x in range(10, 21, 2):
    if i%3==0:
        break
else:
    print(" in else print")
        
    print(x)
    
"2. While Loop : Until condition got"

ans ="y"
while ans=="y":
    num=int(input("Enter number"))
    if(num == 42):
        print("Yeepe ! You guess the number")
        break
    else:
        print("oops! Please try again")
    ans=input("continue(y/n)")
else:
    print("You lost all chances")
    

a = 2
print(type(a))

a, b, c = 1, 2, 3
print(a, b, c)
