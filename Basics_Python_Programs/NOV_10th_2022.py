# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:03:30 2022

@author: dhpcap
"""

lst=[1,5,6,3,4,7,5,6,4,5,6,5]
#count how many times 4 in list
print("count",lst.count(4))

#to add one value at the end of list
lst.append(10)
print(lst)


lst1=[1,2,3]
lst.extend(lst1)
print(lst)

lst.insert(3,45)
print(lst)


#to delete the data from end
lst.pop()
print(lst)


#to delete the data from the perticular position
lst.pop(5)
print(lst)

lst.pop(-5)
print(lst)


if 10 in lst:
    lst.remove(10)
    print(lst)
else:
    print("not found")
    

if 100 in lst:
    print(lst.index(100))
else:
    print("not found")


lst.reverse()
print(lst)

lst1=lst.copy()


lst.sort()
print(lst)


lst.sort(reverse=True)
print(lst1)
print(lst)

lst=[]
ans="y"
while ans=="y":
    num=int(input("enter number"))
    lst.append(num)
    ans=input("continue(y/n)?")
    
    


lst=[1,2,3,4,10,4,5,6,4]    

num=int(input("which number to delete"))

