# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:06:11 2022

@author: dhpcap
"""

a={12,10,13,1,2,3,40,50}
b={10,20,30,12,1,2}
x=a|b         #a.union(b)
print(x)

x=a&b          #a.intersection(b)
print(x)

print(a-b)       #a.difference(b)

a=a-b   #a.difference_update(b) 
print(a)

a={12,10,13,1,2,3,40,50}
print(a^b)  #a.symmetric_difference(b)

a=a^b #a.symmetric_difference_update(b)
print(a)

x=["python","perl","python","java","OS"]
a=set(x)
print(a)

s="Tis is test the set conversion"
b=set(s)
print(b)

b.add("axn")
print(b)

b.update(x)
print(b)

v=b.pop()
print(v)

v=b.remove('o')
print(v)

b.discard('h')
print(b)

c=frozenset(b)
print(c)

a={10,20,3}
b={1,4,5}
print(a.isdisjoint(b))


A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
 
print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))

print("A.issubset(B) : ", A.issubset(B))
print("B.issubset(A) : ", B.issubset(A))

a={10,20}
b={10,20,30,40}
print(b.issuperset(a))
print(a.issubset(b))


