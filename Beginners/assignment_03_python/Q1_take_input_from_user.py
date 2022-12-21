# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:32:53 2022

@author: dhpcap
"""
'''
1. Accept 10 integers from user and print their average value on the screen
'''

n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    element =int(input(f" enter {num} number:"))
    sum = sum + element
    
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)