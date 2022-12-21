# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:46:06 2022

@author: dhpcap
"""
import re  #regular Expression

data="Something is thre in somewhere"
m=re.search("s(.*)e",data,re.I)  #I means ignore

if m!=None:
    print("Found")
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
else:
    print("Pattern not found")
    
    
    
import re  #regular Expression

data="Something is thre in somewhere"
m=re.search("s.*?e",data,re.I)  #I means ignore

if m!=None:
    print("Found")
    print(m.group())
    print(m.span())
  
else:
    print("Pattern not found")
    
    
data = "This is home, sweet home"
m=re.search("^(\w+)\s(\w+)\s(\w+)",data)
if m!=None:
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))
    print(m.group(3))
    print(m.span(3))
else:
    print("Not found")
    
    
data = "This is home, sweet home"
m=re.search("s.*t",data)
if m!=None:
    print("Found")
else:
    print("Not found")
    
    
    
data = "This is home, sweet home"
m=re.match("s.*t",data)
if m!=None:
    print("Found")
else:
    print("Not found")
    
    
data="Something is thre in somewhere"
lst=re.findall("s.*?e",data,re.I)  #I means ignore
if lst!=None:
    print("Found")
    for m in lst:
        print(m.group())
        print(m.span())
else:
    print("Pattern not found")