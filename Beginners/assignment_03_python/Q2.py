# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 07:59:39 2022

@author: dhpcap
"""

'''
2. Print the following patterns using loop :
a.
*
**
***
****
'''

n=int(input("How many rows you want:"))
for i in range(n):
     for j in range(i):
         print("*",end="")
     print()
     
'''
         
b.
  *
 ***
*****
 ***
  * 
'''  

n = 3
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = n - 2

for i in range(n, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")          



                                                       

