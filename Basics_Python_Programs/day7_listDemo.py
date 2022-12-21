# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:27:05 2022

@author: dhpcap
"""

list=[1,2,34,5,2,1,2,7,9]
print(list)
print("count", list.count(2))

list.append(11)
print(list)
list1=[10,20,30,40]
list.extend(list1)
print(list)

list.insert(0,89)
print(list)

list.pop()
print(list)

list.pop(-1)
print(list)

if 34 in list:
    list.remove(34)
    print("Found & remove successfully\n",list)
else:
    print("Not Found")
    
if 11 in list:
    print(list.index(11))
else:
    print("Not Found")
    
list.reverse()
print(list)

list1=list.copy()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)
print(list)

#to write code to accept data from user and store it in the list

lst=[]
ans="y"
while ans=="y":
    num=int(input("Enter a Number:"))
    lst.append(num)
    ans=input("continue(y/n)")
    
print(lst)

lst1=[1,2,34,5,2,1,2,7,9]
num=int(input("Which number you want to delete:"))
while num in lst1:
    lst1.remove(num)
print(lst1)

