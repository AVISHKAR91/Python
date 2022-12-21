# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:30:00 2022

@author: dhpcap
"""
'''
Assignment 4 
Q2 - accept amount from user and find the minimum number notes required to get the amount
amount =512
Notes: 2000,500,100,50,10,5,2,1
500-1 note
10 - 1 note
2- 1 coin
amount=20550
2000 – 10 note
500 – 1 note
50 -1 note


'''

notes = (2000, 500, 100, 50, 10, 5, 2,1)
amt = int(input("Enter amount:"))
for i in notes:
    count=amt//i
    print("Note value: ", i,'\t No_of_notes ', count)
    amt=amt%i;

'''
4. A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

marks=int(input("Enter marks:"))
if(marks>=80):
    print("Grade A")
elif(marks>60 and marks<80):
    print("Grade B")
elif marks>50 and marks<60:
    print("Grade C")
elif(marks >45 and marks <50):
    print("Grade D")
elif(marks >= 25 and marks< 45):
    print("Grade E")
else:
    print("Grade F")