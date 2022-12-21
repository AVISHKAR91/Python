# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:57:04 2022

@author: dhpcap
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:19:00 2022

@author: anilk
"""

#return factorial of a number
def factorial(n=5):
    '''this function returns factorial of a number'''
    f=1
    for i in range(1,n+1):  #1,2,3,4,5,6
        f=f*i
    return f

def addition(a=45,b=50):
    a=a+10
    b=b+15
    return a+b

def printTable(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
    

choice=0

while choice!=4:
    choice=int(input("1. factorial \n 2. addition \n 3. printTable\n 4.exit \n choice:"))
    #perform the task 
    if choice==1:
        num =int(input("enetr number"))
        ans=factorial(num)
        print(f"factorial : {ans}")
    elif choice==2:
        n1=int(input("enetr number"))
        n2=int(input("enetr number"))
        ans=addition(n1,n2)
        print(f"addition : {ans}")
    elif choice==3:
        num =int(input("enetr number"))
        printTable(num)
    elif choice==4:
        print("Thank you for visiting.......")
