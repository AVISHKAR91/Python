# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:44:28 2022

@author: dhpcap
"""

# Today's concept is dictionary

d={'a':2, 'b':4, 'c':5}
print(d['a'])   #2
try:
    print(d['x'])
except KeyError:
    print ("Key not found")

for k,v in d.items():
    if v==5:
        print(k)

d['a']=10
print(d)

d['b']=20
print(d)

v=d.get('a')
print(v)

v=d.get('a')
if v!=None:
    print("Found")
    print(v)
else:
    print("Not Found")
    
v=d.setdefault('x',-1)
if v!=-1:
    print(v)
    
else:
    print("Not Found")
print(d)

k,v = d.popitem()
print(k,v)
print(d)

v=d.pop('a')
print(v)
print(d)

#to display all keys whose values are > 10

d={'a':10, 'b':20, 'c':2,'s':3}

for k,v in d.items():
    if v>10:
        print(f"{k}---->{v}")
print(d)

for k in d.keys():
    if d[k] >= 10:
        print(f"{k} --> {d[k]}")
        

























