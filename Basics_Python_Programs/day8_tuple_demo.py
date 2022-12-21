# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:33:44 2022

@author: dhpcap
"""

a = 12,13,14, "Avishkar"
b = (10,20,30,"Pankaj")
print(a)
print(b)

x=a[0]
y=b[1]
z=b[3]

print(x)
print(y)
print(z)

x,y,z = b

a=10,20,12,30,40,10,33
print(a.count(10))

if 10 in a:
    print(a.index(10))
    
def f1(x,y):
    x=x+10
    y=y+20
    return x,y
x,y = f1(5,4)
print(x,y)
a,b = f1(3,40)
print(a,b)


#swap the  numbers
a=12
b=100
a,b=b,a
print(a,b)

a=12
print(type(a))

# functions with variable number of parameters
def f2(x,y, *t):
    print(x,y)
    print(t)
    
def addition(x,y, *t1):
    ans=x+y
    print(x,y)
    for n in t1:
        ans=ans+n
    return ans

f2(1,2)
f2(1,2,3,4,54,5,6)
d=addition(1,2,3)
print(d)

d=addition(10,2,3,4,5,6,7,8)
print(d)